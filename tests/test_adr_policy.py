"""Verify policy access, provenance and preservation at the public helper seam."""

import contextlib
import hashlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from skills_first_starter import cli as starter

REF = "a" * 40
POLICY = "docs/engineering/architectural-decisions.md"
LOCAL = ".skills-first/architectural-decisions.md"
URL = f"https://github.com/tvproductions/gz-skills-first-starter/blob/{REF}/{POLICY}"


class ADRPolicyTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        inherited = mock.patch.object(starter, "_inherited_plugins", return_value={})
        inherited.start()
        self.addCleanup(inherited.stop)

    def configure(self, *, root=None, mode=None, apply=False, host="codex"):
        arguments = [
            "configure",
            "--project",
            str(root or self.root),
            "--starter-ref",
            REF,
            "--host",
            host,
        ]
        if mode is not None:
            arguments.extend(("--adr-policy", mode))
        if apply:
            arguments.append("--apply")
        output, errors = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            try:
                code = starter.main(arguments)
            except SystemExit as error:
                code = error.code
        return code, output.getvalue(), errors.getvalue()

    def lock(self, root=None):
        return json.loads(((root or self.root) / ".skills-first/bundle.lock.json").read_bytes())

    def files(self):
        return {
            p.relative_to(self.root).as_posix(): p.read_bytes()
            for p in self.root.rglob("*")
            if p.is_file()
        }

    def test_adr_link_preview_and_apply(self):
        for host in ("codex", "claude", "opencode"):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                code, output, errors = self.configure(root=root, mode="link", host=host)
                self.assertEqual(code, 0, errors)
                self.assertEqual(list(root.iterdir()), [])
                self.assertNotIn(LOCAL, json.loads(output)["writes"])
                code, _, errors = self.configure(root=root, mode="link", host=host, apply=True)
                self.assertEqual(code, 0, errors)
                provenance = self.lock(root)["adr_policy"]
                self.assertEqual(
                    provenance,
                    {
                        "mode": "link",
                        "source_path": POLICY,
                        "source_sha256": hashlib.sha256(
                            (starter.HERE / POLICY).read_bytes()
                        ).hexdigest(),
                    },
                )
                self.assertFalse((root / LOCAL).exists())
                self.assertIn(URL, (root / "AGENTS.skills-first.md").read_text(encoding="utf-8"))
                self.assertFalse((root / ".gz-skills/settings.json").exists())
                backplane = next(
                    p for p in self.lock(root)["components"] if p["name"] == "superpowers-backplane"
                )
                self.assertIs(backplane["enabled_by_default"], False)

    def test_adr_local_preview_and_apply(self):
        for host in ("codex", "claude", "opencode"):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                code, output, errors = self.configure(root=root, mode="local", host=host)
                self.assertEqual(code, 0, errors)
                self.assertIn(LOCAL, json.loads(output)["writes"])
                self.assertEqual(list(root.iterdir()), [])
                code, _, errors = self.configure(root=root, mode="local", host=host, apply=True)
                self.assertEqual(code, 0, errors)
                self.assertEqual((root / LOCAL).read_bytes(), (starter.HERE / POLICY).read_bytes())
                self.assertEqual(self.lock(root)["adr_policy"]["local_path"], LOCAL)
                fragment = (root / "AGENTS.skills-first.md").read_text(encoding="utf-8")
                self.assertIn(LOCAL, fragment)
                self.assertIn(URL, fragment)
                self.assertNotIn("{{ADR_POLICY_", fragment)
                self.assertEqual(starter.status(root)["status"], "configured")

    def test_adr_policy_choice_survives_omitted_flag(self):
        code, _, errors = self.configure(mode="local", apply=True)
        self.assertEqual(code, 0, errors)
        before = self.files()
        for mode in (None, "local"):
            code, output, errors = self.configure(mode=mode, apply=True)
            self.assertEqual(code, 0, errors)
            self.assertEqual(json.loads(output)["writes"], [])
            self.assertEqual(self.files(), before)
        self.assertEqual(self.lock()["adr_policy"]["mode"], "local")

    def test_adr_mode_change_requires_reconciliation(self):
        code, _, errors = self.configure(mode="local", apply=True)
        self.assertEqual(code, 0, errors)
        before = self.files()
        code, _, errors = self.configure(mode="link", apply=True)
        self.assertEqual(code, 2)
        self.assertIn("reconcile", errors.lower())
        self.assertEqual(self.files(), before)

    def test_adr_local_edits_block_all_writes(self):
        target = self.root / LOCAL
        target.parent.mkdir()
        original = b"Project-specific policy with preserved authority.\r\n"
        target.write_bytes(original)
        for apply in (False, True):
            code, _, errors = self.configure(mode="local", apply=apply)
            self.assertEqual(code, 2)
            self.assertIn("reconcile", errors.lower())
            self.assertEqual(self.files(), {LOCAL: original})

    def test_adr_policy_symlinks_are_rejected(self):
        for leaf in (False, True):
            with self.subTest(leaf=leaf), tempfile.TemporaryDirectory() as directory:
                external = Path(directory).resolve()
                with tempfile.TemporaryDirectory() as adopter:
                    root = Path(adopter).resolve()
                    if leaf:
                        (root / ".skills-first").mkdir()
                        (root / LOCAL).symlink_to(external / "policy.md")
                    else:
                        (root / ".skills-first").symlink_to(external, target_is_directory=True)
                    code, _, errors = self.configure(root=root, mode="local", apply=True)
                    self.assertEqual(code, 2)
                    self.assertIn("symlink", errors)
                    self.assertEqual(list(external.iterdir()), [])
                    self.assertFalse((root / ".codex").exists())

    def test_adr_policy_concurrent_write_is_preserved(self):
        config = self.root / ".codex/config.toml"
        config.parent.mkdir()
        original = b'model = "fixture"\r\n'
        config.write_bytes(original)
        target = self.root / LOCAL
        concurrent = b"Concurrent project policy.\n"
        real_replace = os.replace

        def introduce_policy(source, destination):
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(concurrent)
            real_replace(source, destination)

        with mock.patch.object(starter.os, "replace", side_effect=introduce_policy):
            code, _, errors = self.configure(mode="local", apply=True)
        self.assertEqual(code, 2)
        self.assertIn("changed during preview", errors)
        self.assertEqual(config.read_bytes(), original)
        self.assertEqual(target.read_bytes(), concurrent)
        self.assertFalse((self.root / "AGENTS.skills-first.md").exists())

    def test_adr_policy_failure_rolls_back_outputs(self):
        target = self.root / LOCAL
        real_open = Path.open

        def fail_policy(path, *args, **kwargs):
            if path == target and args == ("xb",):
                raise OSError("fixture policy write failure")
            return real_open(path, *args, **kwargs)

        with mock.patch.object(Path, "open", autospec=True, side_effect=fail_policy):
            code, _, errors = self.configure(mode="local", apply=True)
        self.assertEqual(code, 2)
        self.assertIn("fixture policy write failure", errors)
        self.assertEqual(self.files(), {})

    def test_adr_partial_policy_write_or_close_failure_removes_owned_file(self):
        real_open = Path.open
        for failure, replacement in (("write", False), ("close", False), ("close", True)):
            with (
                self.subTest(failure=failure, replacement=replacement),
                tempfile.TemporaryDirectory() as directory,
            ):
                root = Path(directory).resolve()
                target = root / LOCAL

                class FailingPolicyStream:
                    def __init__(self, stream, failure, replacement, target):
                        self.stream = stream
                        self.failure = failure
                        self.replacement = replacement
                        self.target = target

                    def __enter__(self):
                        return self

                    def fileno(self):
                        return self.stream.fileno()

                    def write(self, data):
                        if self.failure == "write":
                            self.stream.write(data[:19])
                            raise OSError("fixture disk full during policy write")
                        return self.stream.write(data)

                    def __exit__(self, exc_type, exc, traceback):
                        self.stream.close()
                        if self.failure == "close":
                            if self.replacement:
                                self.target.unlink()
                                self.target.write_bytes(b"Concurrent replacement policy.\n")
                            raise OSError("fixture disk full during policy close")

                def open_policy(
                    path, *args, target=target, failure=failure, replacement=replacement, **kwargs
                ):
                    stream = real_open(path, *args, **kwargs)
                    return (
                        FailingPolicyStream(stream, failure, replacement, target)
                        if path == target and args == ("xb",)
                        else stream
                    )

                identity_reuse = (
                    mock.patch.object(starter.os.path, "samestat", return_value=True)
                    if replacement
                    else contextlib.nullcontext()
                )
                with (
                    mock.patch.object(Path, "open", autospec=True, side_effect=open_policy),
                    identity_reuse,
                ):
                    code, _, errors = self.configure(root=root, mode="local", apply=True)
                self.assertEqual(code, 2)
                self.assertIn("fixture disk full", errors)
                if replacement:
                    self.assertTrue(target.is_file(), "Reused file identity deleted a replacement")
                    self.assertEqual(target.read_bytes(), b"Concurrent replacement policy.\n")
                else:
                    self.assertFalse(target.exists(), "Failed creation left an owned policy behind")
                self.assertEqual(
                    [p for p in root.rglob("*") if p.is_file()], [target] if replacement else []
                )

    def test_adr_legacy_lock_requires_reconciliation(self):
        code, _, errors = self.configure(mode="link", apply=True)
        self.assertEqual(code, 0, errors)
        lock = self.lock()
        del lock["adr_policy"]
        (self.root / ".skills-first/bundle.lock.json").write_bytes(json.dumps(lock).encode())
        before = self.files()
        code, _, errors = self.configure(apply=True)
        self.assertEqual(code, 2)
        self.assertIn("reconcile", errors.lower())
        self.assertEqual(self.files(), before)
        with self.assertRaises(starter.AdoptionError):
            starter.status(self.root)

    def test_adr_policy_provenance_is_validated(self):
        code, _, errors = self.configure(mode="local", apply=True)
        self.assertEqual(code, 0, errors)
        original_lock = self.lock()
        for patch in (
            {"mode": "unrecognized"},
            {"source_sha256": "0" * 64},
            {"local_path": "../outside.md"},
            {"source_path": "wrong.md"},
        ):
            with self.subTest(patch=patch):
                lock = {**original_lock, "adr_policy": {**original_lock["adr_policy"], **patch}}
                (self.root / ".skills-first/bundle.lock.json").write_bytes(
                    json.dumps(lock).encode()
                )
                before = self.files()
                code, _, errors = self.configure(apply=True)
                self.assertEqual(code, 2)
                self.assertIn("reconcile", errors.lower())
                self.assertEqual(self.files(), before)
                with self.assertRaises(starter.AdoptionError):
                    starter.status(self.root)

    def test_adr_policy_bytes_and_hash_preserve_utf8_newlines(self):
        real_read = Path.read_bytes
        for policy in ("Café policy.\n", "Café policy.\r\n"):
            with self.subTest(policy=policy), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                source_bytes = policy.encode("utf-8")

                def read_policy(path, source_bytes=source_bytes):
                    return source_bytes if path == starter.HERE / POLICY else real_read(path)

                with mock.patch.object(Path, "read_bytes", autospec=True, side_effect=read_policy):
                    code, _, errors = self.configure(root=root, mode="local", apply=True)
                self.assertEqual(code, 0, errors)
                self.assertEqual((root / LOCAL).read_bytes(), source_bytes)
                self.assertEqual(
                    self.lock(root)["adr_policy"]["source_sha256"],
                    hashlib.sha256(source_bytes).hexdigest(),
                )


if __name__ == "__main__":
    unittest.main()
