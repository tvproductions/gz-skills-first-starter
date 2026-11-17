"""Observable configuration and effects of the invented reference application."""

import builtins
import contextlib
import io
import json
import os
import secrets
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from example_foundations.application import atomic_write_text, run
from example_foundations.cli import main
from example_foundations.configuration import child_environment, load_settings, safe_diagnostics
from example_foundations.domain import render_message


class FoundationsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.config = self.root / "settings.json"
        self.sentinel = secrets.token_hex(24)

    def load(self, *, config_path=None, environ=None, overrides=None, root=None):
        return load_settings(
            config_path=config_path,
            config_root=root or self.root,
            invocation_base=self.root,
            environ=environ or {},
            overrides=overrides or {},
        )

    def write(self, **values):
        self.config.write_text(json.dumps({"schema_version": 1, **values}), encoding="utf-8")

    def test_precedence_and_omitted_overrides(self):
        self.write(message="file", repeat=2, tags=["file"])
        loaded = self.load(
            environ={"EXAMPLE_FOUNDATIONS_MESSAGE": "env", "EXAMPLE_FOUNDATIONS_TAGS": '["env"]'},
            overrides={"repeat": 3},
        )
        self.assertEqual(
            (loaded.settings.message, loaded.settings.repeat, loaded.settings.tags),
            ("env", 3, ("env",)),
        )
        self.assertEqual(loaded.sources["message"], "environment")
        self.assertEqual(loaded.sources["repeat"], "explicit")
        self.assertEqual(self.load().settings.message, "file")

    def test_invalid_json_and_schema_before_effects(self):
        for raw in (
            "{",
            '{"schema_version":1,"message":"a","message":"b"}',
            '{"schema_version":1,"repeat":NaN}',
            '{"schema_version":2}',
            '{"schema_version":true}',
            '{"schema_version":1,"unknown":1}',
            '{"schema_version":1,"repeat":true}',
            '{"schema_version":1,"tags":[1]}',
            '{"schema_version":1,"message":""}',
            "[]",
            "{}",
        ):
            with self.subTest(raw=raw):
                self.config.write_text(raw, encoding="utf-8")
                with self.assertRaises(ValueError):
                    self.load()

    def test_invalid_explicit_selection_never_falls_back(self):
        self.write(message="fallback")
        for selection in ("", "missing.json"):
            with self.subTest(selection=selection), self.assertRaises(ValueError):
                self.load(config_path=selection)
        for value in ("", "missing.json"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.load(environ={"EXAMPLE_FOUNDATIONS_CONFIG": value})

    def test_declared_root_and_regular_file_validation_precedes_open(self):
        with self.assertRaises(ValueError):
            self.load(root=self.root / "missing")
        self.config.mkdir()
        with (
            mock.patch.object(Path, "open", side_effect=AssertionError("not a regular file")),
            self.assertRaises(ValueError),
        ):
            self.load()

    def test_spaced_symlink_target_spelling_is_rejected(self):
        spaced = self.root / "spaced directory"
        spaced.mkdir()
        self.write()
        alias = self.root / "alias.json"
        alias.symlink_to(spaced / "../settings.json")
        with self.assertRaisesRegex(ValueError, "space"):
            self.load(config_path=alias)

    def test_empty_env_invalid_absent_and_unrelated_ignored(self):
        self.assertEqual(self.load(environ={"UNRELATED": "bad"}).settings.repeat, 1)
        for name in ("MESSAGE", "REPEAT", "TAGS", "OUTPUT_FILE"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.load(environ={f"EXAMPLE_FOUNDATIONS_{name}": ""})

    def test_roots_and_path_bases_do_not_depend_on_later_cwd(self):
        other = self.root / "other"
        other.mkdir()
        (other / "settings.json").write_text(
            '{"schema_version":1,"message":"other","output_file":"result.txt"}', encoding="utf-8"
        )
        self.write(message="first")
        loaded = self.load(root=other)
        self.assertEqual(loaded.settings.message, "other")
        self.assertEqual(loaded.settings.output_file, other / "result.txt")
        with contextlib.chdir(other):
            self.assertEqual(self.load().settings.message, "first")
            explicit = self.load(root=other, overrides={"output_file": "result.txt"})
        self.assertEqual(explicit.settings.output_file, self.root / "result.txt")

    def test_host_service_paths_ignore_home_and_null_disables_output(self):
        self.write(output_file="result.txt")
        with mock.patch.dict(os.environ, {"HOME": "/unused/home", "USERPROFILE": "/unused/user"}):
            for scope in ("service", "host"):
                with self.subTest(scope=scope):
                    loaded = self.load(config_path=self.config, overrides={"output_file": None})
                    self.assertIsNone(loaded.settings.output_file)

    def test_secrets_redacted_and_child_forwarding_explicit(self):
        sentinel = self.sentinel
        self.write(credential_ref="env:EXAMPLE_FOUNDATIONS_TOKEN")
        env = {"EXAMPLE_FOUNDATIONS_TOKEN": sentinel, "PATH": "safe-path"}
        loaded = self.load(environ=env)
        self.assertEqual(loaded.settings.credential, sentinel)
        self.assertNotIn(sentinel, repr(loaded))
        self.assertNotIn(sentinel, json.dumps(safe_diagnostics(loaded)))
        self.assertEqual(child_environment(env), {})
        self.assertEqual(child_environment(env, forwarded=("PATH",)), {"PATH": "safe-path"})
        self.assertEqual(
            child_environment(env, forwarded=("EXAMPLE_FOUNDATIONS_TOKEN",)),
            {"EXAMPLE_FOUNDATIONS_TOKEN": sentinel},
        )
        with self.assertRaisesRegex(ValueError, "credential"):
            self.load()

    def test_spaced_settings_and_symlink_targets_not_opened(self):
        target = self.root / "spaced settings.json"
        target.write_text('{"schema_version":1}', encoding="utf-8")
        alias = self.root / "alias.json"
        alias.symlink_to(target)
        with mock.patch.object(Path, "open", side_effect=AssertionError("content accessed")):
            for selected in (target, alias):
                with self.subTest(selected=selected), self.assertRaisesRegex(ValueError, "space"):
                    self.load(config_path=selected)
            with self.assertRaisesRegex(AssertionError, "content accessed"):
                target.read_text()

    def test_domain_values_and_injected_failure(self):
        self.assertEqual(
            render_message("hello world", 2, ("demo",)), "[demo] hello world\n[demo] hello world"
        )
        self.write(output_file="result.txt")
        writer = mock.Mock(side_effect=OSError("invented write failure"))
        with self.assertRaises(OSError):
            run(self.load().settings, write_text=writer)
        writer.assert_called_once()

    def test_atomic_write_failure_preserves_previous_file(self):
        output = self.root / "result.txt"
        output.write_text("prior bytes", encoding="utf-8")
        with (
            mock.patch("example_foundations.application.os.replace", side_effect=OSError("fault")),
            self.assertRaises(OSError),
        ):
            atomic_write_text(output, "replacement")
        self.assertEqual(output.read_text(), "prior bytes")
        self.assertEqual(list(self.root.iterdir()), [output])
        atomic_write_text(output, "new text with spaces")
        self.assertEqual(output.read_text(), "new text with spaces")

    def test_cli_omission_channels_redaction_and_write_failure(self):
        self.write(message="from file", credential_ref="env:EXAMPLE_FOUNDATIONS_TOKEN")
        stdout, stderr = io.StringIO(), io.StringIO()
        with (
            mock.patch.dict(os.environ, {"EXAMPLE_FOUNDATIONS_TOKEN": self.sentinel}, clear=True),
            contextlib.redirect_stdout(stdout),
            contextlib.redirect_stderr(stderr),
        ):
            code = main(["--config-root", str(self.root)])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(stdout.getvalue()), {"text": "from file"})
        self.assertEqual(stderr.getvalue(), "")
        self.assertNotIn(self.sentinel, stdout.getvalue())
        self.write(output_file="result.txt")
        stdout, stderr = io.StringIO(), io.StringIO()
        with (
            mock.patch(
                "example_foundations.cli.atomic_write_text", side_effect=OSError(self.sentinel)
            ),
            contextlib.redirect_stdout(stdout),
            contextlib.redirect_stderr(stderr),
        ):
            code = main(["--config-root", str(self.root)])
        self.assertEqual(code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertNotIn(self.sentinel, stderr.getvalue())

    def test_cli_invalid_environment_names_the_input_without_echoing_value(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with (
            mock.patch.dict(os.environ, {"EXAMPLE_FOUNDATIONS_REPEAT": self.sentinel}, clear=True),
            contextlib.redirect_stdout(stdout),
            contextlib.redirect_stderr(stderr),
        ):
            code = main(["--config-root", str(self.root)])
        self.assertEqual(code, 2)
        self.assertIn("EXAMPLE_FOUNDATIONS_REPEAT", stderr.getvalue())
        self.assertNotIn(self.sentinel, stderr.getvalue())
        self.assertEqual(stdout.getvalue(), "")

    def test_cli_invalid_repeat_value_is_redacted(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                code = main(["--config-root", str(self.root), "--repeat", self.sentinel])
            except SystemExit as error:
                code = error.code
        self.assertEqual(code, 2)
        self.assertNotIn(self.sentinel, stdout.getvalue() + stderr.getvalue())

    def test_cli_empty_root_does_not_open_working_directory_settings(self):
        self.write(message="must not be loaded")
        stdout, stderr = io.StringIO(), io.StringIO()
        with (
            contextlib.chdir(self.root),
            mock.patch.object(Path, "open", side_effect=AssertionError("cwd settings opened")),
            contextlib.redirect_stdout(stdout),
            contextlib.redirect_stderr(stderr),
        ):
            code = main(["--config-root", ""])
        self.assertEqual(code, 2)
        self.assertEqual(stdout.getvalue(), "")

    def test_bounds_and_output_preservation_before_effects(self):
        output = self.root / "spaced output.txt"
        output.write_text("prior output", encoding="utf-8")
        for values in (
            {"repeat": 0},
            {"repeat": 4},
            {"message": "a" * 1025},
            {"tags": ["a"] * 9},
            {"tags": ["a" * 65]},
            {"tags": [""]},
            {"output_file": str(output)},
            {"output_file": str(self.config)},
        ):
            self.write(**values)
            before = self.config.read_bytes()
            with (
                self.subTest(keys=tuple(values)),
                self.assertRaises(ValueError),
                mock.patch("example_foundations.cli.atomic_write_text") as writer,
            ):
                self.load()
            writer.assert_not_called()
            self.assertEqual(self.config.read_bytes(), before)
            self.assertEqual(output.read_text(), "prior output")
        self.write(message="a" * 65536)
        with self.assertRaises(ValueError):
            self.load()
        self.write(repeat=3, message="a" * 1024, tags=["a" * 64] * 8)
        loaded = self.load()
        self.assertEqual(loaded.settings.repeat, 3)
        self.assertEqual(len(loaded.settings.tags), 8)

    def test_rejected_output_paths_are_not_opened_or_written(self):
        output = self.root / "spaced output.txt"
        output.write_text("preserved output", encoding="utf-8")
        alias = self.root / "output-alias"
        alias.symlink_to(output)
        original_path_open, original_open = Path.open, builtins.open

        def protected(value):
            return isinstance(value, (str, Path)) and Path(value).resolve() == output

        def guard_path(path, *args, **kwargs):
            if protected(path):
                raise AssertionError("output content accessed")
            return original_path_open(path, *args, **kwargs)

        def guard_builtin(path, *args, **kwargs):
            if protected(path):
                raise AssertionError("output content accessed")
            return original_open(path, *args, **kwargs)

        for selected in (output, alias):
            self.write(output_file=str(selected))
            before = self.config.read_bytes()
            stdout, stderr = io.StringIO(), io.StringIO()
            with (
                mock.patch.object(Path, "open", guard_path),
                mock.patch.object(builtins, "open", guard_builtin),
                mock.patch("example_foundations.cli.atomic_write_text") as writer,
                contextlib.redirect_stdout(stdout),
                contextlib.redirect_stderr(stderr),
            ):
                self.assertEqual(main(["--config-root", str(self.root)]), 2)
                writer.assert_not_called()
                with self.assertRaisesRegex(AssertionError, "output content"):
                    alias.read_text()
                with (
                    self.assertRaisesRegex(AssertionError, "output content"),
                    builtins.open(output),
                ):
                    pass
            self.assertEqual(stdout.getvalue(), "")
            self.assertEqual(self.config.read_bytes(), before)
            self.assertEqual(output.read_text(), "preserved output")
