"""Calibrate the locked Python check with fixed native trace controls."""

import unittest

from tools.engineering.instruction_delivery_python_trace import check_locked_python


def codex(command, exit_code=0):
    """Record a single tool operation in a complete Codex turn."""
    item = {"id": "shell", "type": "command_execution", "command": command}
    return [
        {"type": "turn.started"},
        {"type": "item.started", "item": item},
        {"type": "item.completed", "item": {**item, "exit_code": exit_code}},
        {"type": "turn.completed"},
    ]


def claude(command, *, is_error=False, content=""):
    """Record one Bash request and its native result in a Claude turn."""
    return [
        {"type": "system", "subtype": "init"},
        {
            "type": "assistant",
            "message": {
                "content": [
                    {
                        "type": "tool_use",
                        "name": "Bash",
                        "id": "shell",
                        "input": {"command": command},
                    },
                ]
            },
        },
        {
            "type": "user",
            "message": {
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": "shell",
                        "is_error": is_error,
                        "content": content,
                    },
                ]
            },
        },
        {"type": "result", "subtype": "success"},
    ]


class LockedPythonTraceTests(unittest.TestCase):
    def test_literal_invocations_and_file_inspection(self):
        controls = (
            ("uv run --locked python -m json.tool app.json", "PASS"),
            ('UV_CACHE_DIR="$PWD/.cache" uv run --locked --no-sync python -VV', "PASS"),
            ("uv --no-cache run --offline --locked python - <<'PY'\nprint('fixture')\nPY", "PASS"),
            (".venv/bin/python -m json.tool app.json", "FAIL"),
            (r'"C:\Fixture\.venv\Scripts\python.exe" -VV', "FAIL"),
            ("PYTHONPATH=src python3 -m unittest", "FAIL"),
            ("uv run --offline python -m unittest", "FAIL"),
            ("ls .venv/bin/python", "NOT_APPLICABLE"),
            ("grep '&&' .venv/bin/python", "NOT_APPLICABLE"),
            ("env", "NOT_APPLICABLE"),
            ('"$INTERPRETER" -VV', "UNVERIFIED"),
            ("bash check.sh", "UNVERIFIED"),
            ("find . -exec python3 {} +", "UNVERIFIED"),
            ("cat <<'END'\ntext\nEND\npreview.sh\nEND", "UNVERIFIED"),
        )
        for host, trace in (("codex", codex), ("claude", claude)):
            for command, expected in controls:
                with self.subTest(host=host, command=command):
                    self.assertEqual(
                        check_locked_python([trace(command)], host)["status"], expected
                    )

    def test_unwitnessed_branch_is_unverified(self):
        for command, code in (
            ("git status && .venv/bin/python -VV", 1),
            ("git status || .venv/bin/python -VV", 0),
            ("git status && .venv/bin/python -VV; git status", 0),
            ("if false; then cat README.md; .venv/bin/python -VV; fi", 0),
            ("exit 0; .venv/bin/python -VV", 0),
        ):
            with self.subTest(command=command):
                verdict = check_locked_python([codex(command, code)], "codex")
                self.assertEqual(verdict["status"], "UNVERIFIED")
                self.assertEqual(verdict["violations"], [])

    def test_truncated_turns_and_failures_across_turns(self):
        complete = codex("uv run --locked python -VV")
        truncated = codex("uv run --locked python -VV")[:2]
        incomplete = check_locked_python([complete, truncated], "codex")
        self.assertEqual(incomplete["status"], "UNVERIFIED")
        violation = codex("uv run --locked python -VV && .venv/bin/python -VV")
        failed = check_locked_python([complete, truncated, violation], "codex")
        self.assertEqual(failed["status"], "FAIL")
        self.assertEqual(failed["violations"], [{"trace": 3, "line": 3}])
        self.assertTrue(failed["unverified"])

    def test_native_tool_denial_does_not_prove_execution(self):
        trace = claude(
            "python3 -VV",
            is_error=True,
            content="Permission to use Bash has been denied.",
        )
        self.assertEqual(check_locked_python([trace], "claude")["status"], "UNVERIFIED")
