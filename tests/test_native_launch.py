"""Verify the OpenCode duplicate-ID workaround keeps configuration project-owned."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from skills_first_starter.native_launch import launch


class NativeLaunchTests(unittest.TestCase):
    def test_user_preferences_survive_but_inherited_plugin_sources_do_not(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            project, user = root / "project", root / "user"
            project.mkdir()
            user.mkdir()
            (project / "opencode.json").write_text(json.dumps({"plugins": ["fixture-local"]}))
            (project / ".agents/skills").mkdir(parents=True)
            original = json.dumps(
                {
                    "model": "fixture",
                    "plugins": ["fixture-global"],
                    "permissions": [{"action": "fixture", "effect": "deny"}],
                }
            )
            (user / "opencode.json").write_text(original)
            with (
                mock.patch.dict("os.environ", {"OPENCODE_CONFIG_DIR": str(user)}),
                mock.patch("skills_first_starter.native_launch.subprocess.run") as run,
            ):
                run.return_value.returncode = 0
                self.assertEqual(launch(project, ["api", "plugin.list"]), 0)
            env = run.call_args.kwargs["env"]
            effective = json.loads(env["OPENCODE_CONFIG_CONTENT"])
            self.assertEqual(effective["plugins"], ["fixture-local"])
            self.assertEqual(effective["model"], "fixture")
            self.assertEqual(effective["permissions"][0]["effect"], "deny")
            self.assertIn(str(project / ".agents/skills"), effective["skills"])
            self.assertEqual(env["OPENCODE_CONFIG_PROJECT_DISABLE"], "true")
            self.assertEqual(env["OPENCODE_CONFIG_DIR"], str(project / ".opencode"))
            self.assertIn("--standalone", run.call_args.args[0])
            self.assertEqual((user / "opencode.json").read_text(), original)

    def test_global_mutations_and_shared_server_attachment_are_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "opencode.json").write_text('{"plugins": []}')
            for args in (
                ["plugin", "add", "fixture"],
                ["plugin", "remove", "fixture"],
                ["service", "restart"],
                ["--print-logs", "service", "restart"],
                ["--print-logs", "plugin", "add", "fixture"],
                ["--server", "http://example.invalid"],
            ):
                with self.subTest(args=args), self.assertRaises(ValueError):
                    launch(root, args)


if __name__ == "__main__":
    unittest.main()
