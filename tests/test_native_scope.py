"""Verify brownfield scope repair preserves global state and project authorities."""

import json
import tempfile
import tomllib
import unittest
from pathlib import Path
from unittest import mock

from skills_first_starter import cli as starter
from skills_first_starter.native import HOST_PATHS

REF = "b" * 40


class NativeScopeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def test_codex_suppresses_inherited_duplicates_only_in_project(self):
        inherited = {"plugins": {"gz-skills@gz-skills": {"enabled": True}}}
        snapshot = json.dumps(inherited)
        path = self.root / ".codex/config.toml"
        path.parent.mkdir()
        path.write_bytes(b'# Keep caf\xc3\xa9\r\nmodel = "fixture"\r\n')
        with mock.patch.object(starter, "_inherited_plugins", return_value=inherited):
            preview = starter.localize(self.root, REF, host="codex")
            self.assertEqual(preview["writes"], [".codex/config.toml"])
            self.assertNotIn("gz-skills", path.read_text())
            starter.localize(self.root, REF, host="codex", apply=True)
            after = path.read_bytes()
            self.assertTrue(after.startswith(b'# Keep caf\xc3\xa9\r\nmodel = "fixture"\r\n'))
            plugins = tomllib.loads(after.decode())["plugins"]
            self.assertIs(plugins["gz-skills@gz-skills"]["enabled"], False)
            self.assertIs(plugins["gz-skills@skills-first-starter"]["enabled"], True)
            self.assertEqual(starter.localize(self.root, REF, host="codex")["writes"], [])
        self.assertEqual(json.dumps(inherited), snapshot)
        self.assertFalse((self.root / ".skills-first/bundle.lock.json").exists())

    def test_codex_repairs_local_boolean_without_losing_other_tables_or_pin(self):
        path = self.root / ".codex/config.toml"
        path.parent.mkdir()
        path.write_text(
            '[plugins."gz-skills@skills-first-starter"]\nenabled = false # Repair me\n'
            '[marketplaces.skills-first-starter]\nsource_type = "git"\n'
            'source = "https://example.invalid/reviewed.git"\nref = "old-selection"\n'
            "[fixture]\nkeep = true\n"
        )
        with mock.patch.object(starter, "_inherited_plugins", return_value={}):
            starter.localize(self.root, REF, host="codex", apply=True)
        data = tomllib.loads(path.read_text())
        self.assertTrue(data["plugins"]["gz-skills@skills-first-starter"]["enabled"])
        self.assertEqual(data["marketplaces"]["skills-first-starter"]["ref"], "old-selection")
        self.assertTrue(data["fixture"]["keep"])
        self.assertIn("# Repair me", path.read_text())

    def test_codex_missing_newline_and_multiline_values_do_not_corrupt_repair(self):
        for original in (
            '[plugins."gz-skills@skills-first-starter"]',
            '[plugins."gz-skills@skills-first-starter"]\nnotes = """\nenabled = false\n"""\nenabled = false',
        ):
            with self.subTest(original=original):
                path = self.root / ".codex/config.toml"
                path.parent.mkdir(exist_ok=True)
                path.write_text(original)
                before = tomllib.loads(original)["plugins"]["gz-skills@skills-first-starter"]
                with mock.patch.object(starter, "_inherited_plugins", return_value={}):
                    starter.localize(self.root, REF, host="codex", apply=True)
                after = tomllib.loads(path.read_text())["plugins"]["gz-skills@skills-first-starter"]
                self.assertIs(after["enabled"], True)
                if "notes" in before:
                    self.assertEqual(after["notes"], before["notes"])

    def test_claude_repairs_both_project_layers_without_altering_user_state(self):
        inherited = {"enabledPlugins": {"gz-skills@gz-skills": True}}
        for name in ("settings.json", "settings.local.json"):
            path = self.root / ".claude" / name
            path.parent.mkdir(exist_ok=True)
            path.write_text(
                json.dumps(
                    {
                        "fixture": name,
                        "enabledPlugins": {
                            "gz-skills@gz-skills": True,
                            "gz-skills@skills-first-starter": False,
                        },
                    }
                )
            )
        with mock.patch.object(starter, "_inherited_plugins", return_value=inherited):
            starter.localize(self.root, REF, host="claude", apply=True)
            self.assertEqual(starter.localize(self.root, REF, host="claude")["writes"], [])
        for name in ("settings.json", "settings.local.json"):
            data = json.loads((self.root / ".claude" / name).read_bytes())
            self.assertEqual(data["fixture"], name)
            self.assertIs(data["enabledPlugins"]["gz-skills@gz-skills"], False)
            self.assertIs(data["enabledPlugins"]["gz-skills@skills-first-starter"], True)
        self.assertIs(inherited["enabledPlugins"]["gz-skills@gz-skills"], True)

    def test_scope_repair_preserves_adopted_component_versions_and_lock_bytes(self):
        starter.configure(self.root, REF, host="opencode", apply=True)
        path = self.root / ".skills-first/bundle.lock.json"
        lock = json.loads(path.read_bytes())
        part = next(p for p in lock["components"] if p["name"] == "gz-skills")
        part["revision"] = "c" * 40
        path.write_text(json.dumps(lock, indent=2) + "\n")
        original = path.read_bytes()
        starter.localize(self.root, REF, host="opencode", apply=True)
        config = json.loads((self.root / "opencode.json").read_bytes())
        self.assertIn(
            "git+https://github.com/tvproductions/gz-skills.git#" + "c" * 40, config["plugins"]
        )
        self.assertEqual(path.read_bytes(), original)

    def test_opencode_preserves_unrelated_plugins_and_orders_local_overrides(self):
        path = self.root / "opencode.json"
        path.write_text(json.dumps({"plugins": ["superpowers-helper@1.0.0"], "fixture": True}))
        starter.localize(self.root, REF, host="opencode", apply=True)
        config = json.loads(path.read_bytes())
        self.assertTrue(config["fixture"])
        self.assertEqual(config["plugins"][0], "superpowers-helper@1.0.0")
        self.assertIn("-gz-skills", config["plugins"])
        self.assertTrue(config["plugins"][-1].startswith("git+https://github.com/tvproductions/"))

    def test_each_scope_repair_stays_within_the_selected_project(self):
        for host in HOST_PATHS:
            with self.subTest(host=host), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                with (
                    mock.patch.object(starter, "_inherited_plugins", return_value={}),
                    mock.patch.object(starter.subprocess, "run") as commands,
                ):
                    starter.localize(root, REF, host=host, apply=True)
                    commands.assert_not_called()
                files = [str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()]
                self.assertEqual(files, [HOST_PATHS[host]])

    def test_jsonc_scope_repair_keeps_comments_strings_and_nested_fields(self):
        path = self.root / "opencode.jsonc"
        original = (
            "{ // Keep project rationale\n"
            ' "fixture": {"plugins": ["unrelated"], "text": "https://example.invalid/a,}//b"},\n'
            ' "plugins": [], /* Keep this explanation */\n}\n'
        )
        path.write_text(original)
        starter.localize(self.root, REF, host="opencode", apply=True)
        after = path.read_text()
        self.assertIn("// Keep project rationale", after)
        self.assertIn("/* Keep this explanation */", after)
        self.assertIn(
            '"fixture": {"plugins": ["unrelated"], "text": "https://example.invalid/a,}//b"}', after
        )
        self.assertEqual(starter.localize(self.root, REF, host="opencode")["writes"], [])
        self.assertFalse((self.root / "opencode.json").exists())


if __name__ == "__main__":
    unittest.main()
