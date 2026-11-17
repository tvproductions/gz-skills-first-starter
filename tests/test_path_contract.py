"""Public path rejection must precede target reads and writes."""

import builtins
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from skills_first_starter import cli
from skills_first_starter.native_launch import launch

REF = "a" * 40


class PathContractTests(unittest.TestCase):
    def test_spaced_root_rejected_before_reads_or_parent_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve() / "spaced project"
            root.mkdir()
            target = root / "AGENTS.md"
            target.write_text("keep spaces in contents", encoding="utf-8")
            alias = root.parent / "alias"
            alias.symlink_to(root, target_is_directory=True)
            original = Path.open
            original_builtin = builtins.open

            def guarded(path, *args, **kwargs):
                if path.absolute().is_relative_to(root) or path.resolve().is_relative_to(root):
                    raise AssertionError("target was opened before rejection")
                return original(path, *args, **kwargs)

            def guarded_builtin(file, *args, **kwargs):
                if isinstance(file, (str, Path)):
                    candidate = Path(file)
                    if candidate.absolute().is_relative_to(
                        root
                    ) or candidate.resolve().is_relative_to(root):
                        raise AssertionError("target was opened before rejection")
                return original_builtin(file, *args, **kwargs)

            calls = (
                lambda: cli.configure(root, REF, apply=True),
                lambda: cli.configure(alias, REF, apply=True),
                lambda: cli.localize(root, REF, host="codex", apply=True),
                lambda: cli.status(root),
                lambda: cli.backport(root),
                lambda: launch(root, []),
            )
            with (
                mock.patch.object(Path, "open", guarded),
                mock.patch.object(builtins, "open", guarded_builtin),
                mock.patch.object(cli, "_apply_writes") as writes,
                mock.patch("skills_first_starter.native_launch.subprocess.run") as process,
            ):
                for call in calls:
                    with self.subTest(call=call), self.assertRaisesRegex(ValueError, "space"):
                        call()
                with self.assertRaisesRegex(AssertionError, "target was opened"):
                    target.read_text()
                with (
                    self.assertRaisesRegex(AssertionError, "target was opened"),
                    builtins.open(target),
                ):
                    pass
                stderr = io.StringIO()
                with contextlib.redirect_stderr(stderr):
                    self.assertEqual(
                        cli.main(
                            ["configure", "--project", str(root), "--starter-ref", REF, "--apply"]
                        ),
                        2,
                    )
                writes.assert_not_called()
                process.assert_not_called()
            self.assertEqual(target.read_text(), "keep spaces in contents")
            self.assertEqual(list(root.iterdir()), [target])

    def test_space_free_alias_to_spaced_root_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory).resolve()
            target = parent / "spaced target"
            target.mkdir()
            alias = parent / "alias"
            alias.symlink_to(target, target_is_directory=True)
            for path in (alias, parent / "spaced target/../alias"):
                with self.subTest(path=path), self.assertRaisesRegex(ValueError, "space"):
                    cli.configure(path, REF, apply=True)
            self.assertEqual(list(target.iterdir()), [])

    def test_cli_rejection_and_valid_contents_control(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            bad = root / "bad project"
            bad.mkdir()
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                code = cli.main(
                    ["configure", "--project", str(bad), "--starter-ref", REF, "--apply"]
                )
            self.assertEqual(code, 2)
            self.assertIn("space", stderr.getvalue())
            self.assertEqual(list(bad.iterdir()), [])
            good = root / "good"
            good.mkdir()
            (good / "AGENTS.md").write_text("keep this text with spaces", encoding="utf-8")
            with mock.patch.object(cli, "_inherited_plugins", return_value={}):
                cli.configure(good, REF, apply=True)
            self.assertEqual((good / "AGENTS.md").read_text(), "keep this text with spaces")

    def test_spaced_inherited_config_fails_before_read(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory).resolve() / "user config"
            home.mkdir()
            (home / "config.toml").write_text("invalid TOML [", encoding="utf-8")
            with (
                mock.patch.dict("os.environ", {"CODEX_HOME": str(home)}),
                self.assertRaisesRegex(ValueError, "space"),
            ):
                cli._inherited_plugins("codex")

    def test_spaced_symlink_spelling_cannot_be_erased_by_parent_resolution(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            spaced = root / "spaced parent"
            spaced.mkdir()
            good = root / "good"
            good.mkdir()
            alias = root / "alias"
            alias.symlink_to(spaced / "../good", target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "space"):
                cli.configure(alias, REF, apply=True)
            self.assertEqual(list(good.iterdir()), [])
