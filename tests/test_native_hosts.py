"""Exercise native host selection through the public adoption helper."""

import json
import tempfile
import unittest
from pathlib import Path, PureWindowsPath
from unittest import mock

from skills_first_starter import cli as starter
from skills_first_starter.native import HOST_PATHS, update_skill_path

REF = "a" * 40


class NativeHostTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        inherited = mock.patch.object(starter, "_inherited_plugins", return_value={})
        inherited.start()
        self.addCleanup(inherited.stop)

    def test_owned_discovery_surface_uses_portable_identifiers(self):
        for host in HOST_PATHS:
            with self.subTest(host=host), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                starter.configure(root, REF, host=host, apply=True)
                with mock.patch.object(starter, "Path", PureWindowsPath):
                    self.assertEqual(starter.configure(root, REF, host=host)["writes"], [])

    def test_each_host_previews_then_applies_only_project_files_without_native_commands(self):
        for host, config in HOST_PATHS.items():
            with self.subTest(host=host), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                with mock.patch.object(starter.subprocess, "run") as native:
                    preview = starter.configure(root, REF, host=host)
                    self.assertFalse(list(root.iterdir()))
                    self.assertIn(config, preview["writes"])
                    self.assertIn(update_skill_path(host), preview["writes"])
                    starter.configure(root, REF, host=host, apply=True)
                    self.assertEqual(starter.configure(root, REF, host=host)["writes"], [])
                    self.assertEqual(starter.status(root)["status"], "configured")
                    native.assert_not_called()
                self.assertTrue((root / config).is_file())
                for other in set(HOST_PATHS.values()) - {config}:
                    self.assertFalse((root / other).exists())

    def test_claude_uses_project_settings_and_keeps_explicit_backplane_disable(self):
        starter.configure(self.root, REF, host="claude", apply=True)
        settings = json.loads((self.root / ".claude/settings.json").read_bytes())
        source = settings["extraKnownMarketplaces"]["skills-first-starter"]["source"]
        self.assertEqual(source["ref"], REF)
        self.assertEqual(source["source"], "git")
        self.assertIs(settings["enabledPlugins"]["gz-skills@skills-first-starter"], True)
        self.assertIs(
            settings["enabledPlugins"]["superpowers-backplane@skills-first-starter"], False
        )

    def test_opencode_pins_both_upstream_adapters_and_omits_deferred_backplane(self):
        starter.configure(self.root, REF, host="opencode", apply=True)
        config = json.loads((self.root / "opencode.json").read_bytes())
        expected = [
            f"git+{p['repository']}.git#{p['revision']}"
            for p in starter.bundle()["components"]
            if p["enabled_by_default"]
        ]
        self.assertEqual(
            config["plugins"], ["-" + p["name"] for p in starter.bundle()["components"]] + expected
        )
        self.assertNotIn("plugin", config)

    def test_json_hosts_preserve_unrelated_settings_and_idempotent_bytes(self):
        for host in ("claude", "opencode"):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                path = root / HOST_PATHS[host]
                path.parent.mkdir(parents=True, exist_ok=True)
                original = {"fixture": {"label": "café"}}
                if host == "opencode":
                    original["plugins"] = ["fixture-plugin@1.0.0"]
                path.write_text(json.dumps(original), encoding="utf-8")
                starter.configure(root, REF, host=host, apply=True)
                first = path.read_bytes()
                config = json.loads(first)
                self.assertEqual(config["fixture"], original["fixture"])
                if host == "opencode":
                    self.assertIn("fixture-plugin@1.0.0", config["plugins"])
                starter.configure(root, REF, host=host, apply=True)
                self.assertEqual(path.read_bytes(), first)

    def test_conflicting_native_state_blocks_all_writes(self):
        cases = (
            ("claude", {"enabledPlugins": {"gz-skills@skills-first-starter": False}}),
            ("claude", {"enabledPlugins": {"gz-skills@other": True}}),
            ("opencode", {"plugin": ["fixture-legacy"]}),
            ("opencode", {"plugins": ["git+https://github.com/obra/superpowers.git#old"]}),
        )
        for host, config in cases:
            with self.subTest(config=config), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                path = root / HOST_PATHS[host]
                path.parent.mkdir(parents=True, exist_ok=True)
                original = json.dumps(config).encode()
                path.write_bytes(original)
                with self.assertRaises(ValueError):
                    starter.configure(root, REF, host=host, apply=True)
                self.assertEqual(path.read_bytes(), original)
                self.assertFalse((root / ".skills-first").exists())
                self.assertFalse((root / "AGENTS.md").exists())

    def test_opencode_jsonc_is_preserved_instead_of_shadowed(self):
        path = self.root / "opencode.jsonc"
        path.write_text('{ // Project authority\n "plugins": []\n}\n')
        starter.configure(self.root, REF, host="opencode", apply=True)
        self.assertIn("// Project authority", path.read_text())
        self.assertEqual(starter.configure(self.root, REF, host="opencode")["writes"], [])
        self.assertFalse((self.root / "opencode.json").exists())

    def test_claude_local_override_is_preserved_and_blocks_activation_conflict(self):
        path = self.root / ".claude/settings.local.json"
        path.parent.mkdir()
        original = b'{"enabledPlugins":{"gz-skills@skills-first-starter":false}}'
        path.write_bytes(original)
        with self.assertRaisesRegex(ValueError, "enabledPlugins"):
            starter.configure(self.root, REF, host="claude", apply=True)
        self.assertEqual(path.read_bytes(), original)
        self.assertFalse((self.root / ".claude/settings.json").exists())
        self.assertFalse((self.root / ".skills-first").exists())

    def test_host_switch_requires_reconciliation_before_writing_other_host_settings(self):
        starter.configure(self.root, REF, host="claude", apply=True)
        with self.assertRaises(starter.AdoptionError):
            starter.configure(self.root, REF, host="opencode", apply=True)
        self.assertFalse((self.root / "opencode.json").exists())

    def test_new_host_symlink_destinations_cannot_escape_the_repository(self):
        for host in ("claude", "opencode"):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                destination = root / HOST_PATHS[host]
                destination.parent.mkdir(exist_ok=True)
                destination.symlink_to(self.root / "outside.json")
                with self.assertRaises(starter.AdoptionError):
                    starter.configure(root, REF, host=host, apply=True)
                self.assertFalse((self.root / "outside.json").exists())

    def test_cli_host_selection_reaches_the_public_configuration(self):
        with mock.patch("builtins.print") as output:
            result = starter.main(
                [
                    "configure",
                    "--project",
                    str(self.root),
                    "--starter-ref",
                    REF,
                    "--host",
                    "claude",
                    "--apply",
                ]
            )
        self.assertEqual(result, 0)
        self.assertEqual(json.loads(output.call_args.args[0])["host"], "claude")
        self.assertTrue((self.root / ".claude/settings.json").is_file())


if __name__ == "__main__":
    unittest.main()
