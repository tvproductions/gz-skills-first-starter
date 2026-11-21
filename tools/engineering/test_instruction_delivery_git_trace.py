"""Replay fixed native events against the Git ordering checker."""

import json
import subprocess
import sys
import unittest
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory

from tools.engineering.instruction_delivery_git_trace import check_git_trace

CONTROLS = Path(__file__).parent / "fixtures" / "instruction-delivery-git-traces-v1.json"


class GitTraceTests(unittest.TestCase):
    def test_fixed_native_controls(self):
        cases = json.loads(CONTROLS.read_text(encoding="utf-8"))
        for case in cases:
            with self.subTest(case=case["name"]):
                verdict = check_git_trace(
                    case["events"], case["host"], PurePosixPath(case["workspace"])
                )
                for key, expected in case["expected"].items():
                    self.assertEqual(verdict[key], expected)

    def test_trace_command_replays_raw_jsonl(self):
        case = json.loads(CONTROLS.read_text(encoding="utf-8"))[2]
        with TemporaryDirectory() as directory:
            path = Path(directory) / "trace.jsonl"
            path.write_text(
                "".join(json.dumps(event) + "\n" for event in case["events"]),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.engineering.evaluate_instruction_delivery",
                    "trace",
                    "git-sync",
                    str(path),
                    "--host",
                    case["host"],
                    "--workspace",
                    case["workspace"],
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )
        self.assertEqual(result.returncode, 1, result.stderr)
        verdict = json.loads(result.stdout)
        self.assertEqual(verdict["status"], "FAIL")
        self.assertEqual(verdict["edit_line"], 3)
        self.assertEqual(verdict["reason"], "edit_before_assertion")
