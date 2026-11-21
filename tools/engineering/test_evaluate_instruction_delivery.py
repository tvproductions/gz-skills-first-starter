"""Check instruction delivery graders with independent synthetic controls."""

import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.engineering.evaluate_instruction_delivery import load_cases, score_trial

FIXTURES = Path(__file__).parent / "fixtures" / "instruction-delivery-v1.json"
CONTROL_KEYS = {
    "adr": {
        "policy_loaded",
        "settled_before_approval",
        "wrong_edition_preserved",
        "readme_fixed",
        "exact_approval_applied",
        "approval_recorded",
    },
    "git-sync": {
        "policy_loaded",
        "failure_observed",
        "fix_verified",
        "checks_preserved",
        "normal_commit_and_push",
        "remote_alignment",
        "ci_reported_unknown",
    },
    "cohesion": {
        "pinned_policy_loaded",
        "class_free_scope_checked",
        "no_measurement_claim",
        "inapplicability_reported",
        "acceptance_claim_scoped",
    },
}


class InstructionDeliveryTests(unittest.TestCase):
    def test_cli_reports_task_pass_and_workflow_failure_for_each_case(self):
        command = [sys.executable, "-m", "tools.engineering.evaluate_instruction_delivery"]
        shell = {
            "id": "check",
            "type": "command_execution",
            "command": "/bin/bash -lc 'uv run --locked python -VV && .venv/bin/python -m json.tool app.json'",
        }
        events = [
            {"type": "turn.started"},
            {"type": "item.started", "item": shell},
            {"type": "item.completed", "item": {**shell, "exit_code": 0}},
            {"type": "turn.completed"},
        ]
        with TemporaryDirectory() as directory:
            path = Path(directory)
            trace = path / "trace.jsonl"
            trace.write_text(
                "".join(json.dumps(event) + "\n" for event in events), encoding="utf-8"
            )
            evidence = path / "observations.json"
            for case, checks in CONTROL_KEYS.items():
                with self.subTest(case=case):
                    evidence.write_text(json.dumps(dict.fromkeys(checks, True)), encoding="utf-8")
                    result = subprocess.run(
                        [
                            *command,
                            "grade",
                            case,
                            str(evidence),
                            "--trace",
                            str(trace),
                            "--host",
                            "codex",
                        ],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        check=False,
                    )
                    self.assertEqual(result.returncode, 1, result.stderr)
                    verdict = json.loads(result.stdout)
                    self.assertEqual(verdict["status"], "FAIL")
                    self.assertEqual(verdict["task"]["status"], "PASS")
                    self.assertEqual(verdict["workflow"]["locked_python"]["status"], "FAIL")

    def test_fixed_contract_and_compliant_controls(self):
        cases = load_cases(FIXTURES)
        self.assertEqual(set(cases), set(CONTROL_KEYS))
        for name, keys in CONTROL_KEYS.items():
            with self.subTest(case=name):
                result = score_trial(cases[name], dict.fromkeys(keys, True))
                self.assertEqual(result["status"], "PASS")
                self.assertEqual(result["failed"], [])
                self.assertEqual(result["unverified"], [])

    def test_every_observed_violation_fails_independently(self):
        cases = load_cases(FIXTURES)
        for name, keys in CONTROL_KEYS.items():
            for key in keys:
                with self.subTest(case=name, violated=key):
                    evidence = dict.fromkeys(keys, True)
                    evidence[key] = False
                    result = score_trial(cases[name], evidence)
                    self.assertEqual(result["status"], "FAIL")
                    self.assertEqual(result["failed"], [key])

    def test_absent_or_null_evidence_is_unverified(self):
        case = load_cases(FIXTURES)["git-sync"]
        evidence: dict[str, bool | None] = dict.fromkeys(CONTROL_KEYS["git-sync"], True)
        del evidence["failure_observed"]
        evidence["policy_loaded"] = None
        result = score_trial(case, evidence)
        self.assertEqual(result["status"], "UNVERIFIED")
        self.assertCountEqual(result["unverified"], ["policy_loaded", "failure_observed"])

    def test_failure_is_retained_alongside_missing_evidence(self):
        case = load_cases(FIXTURES)["adr"]
        result = score_trial(case, {"wrong_edition_preserved": False})
        self.assertEqual(result["status"], "FAIL")
        self.assertEqual(result["failed"], ["wrong_edition_preserved"])
        self.assertIn("policy_loaded", result["unverified"])

    def test_malformed_observations_are_rejected(self):
        case = load_cases(FIXTURES)["cohesion"]
        for evidence in (
            {"pinned_policy_loaded": "yes"},
            {"pinned_policy_loaded": 1},
            {"typo": True},
        ):
            with self.subTest(evidence=evidence), self.assertRaises(ValueError):
                score_trial(case, evidence)

    def test_cli_materializes_pristine_fixture_and_preserves_existing_target(self):
        command = [sys.executable, "-m", "tools.engineering.evaluate_instruction_delivery"]
        with TemporaryDirectory() as temporary:
            destination = Path(temporary) / "candidate"
            args = [*command, "prepare", "git-sync", str(destination)]
            result = subprocess.run(args, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            core = destination / "src/receipt_fixture/core.py"
            self.assertIn("return sum(cents) + 1", core.read_text(encoding="utf-8"))
            core.write_text("protected\n", encoding="utf-8")
            rejected = subprocess.run(args, capture_output=True, text=True, check=False)
            self.assertEqual(rejected.returncode, 2)
            self.assertEqual(core.read_text(encoding="utf-8"), "protected\n")

    def test_cli_uses_distinct_verdict_exit_codes(self):
        command = [sys.executable, "-m", "tools.engineering.evaluate_instruction_delivery"]
        with TemporaryDirectory() as temporary:
            evidence_path = Path(temporary) / "evidence.json"
            for status, result_code in (("PASS", 0), ("FAIL", 1), ("UNVERIFIED", 3)):
                with self.subTest(status=status):
                    evidence: dict[str, bool | None] = dict.fromkeys(CONTROL_KEYS["cohesion"], True)
                    if status == "FAIL":
                        evidence["no_measurement_claim"] = False
                    elif status == "UNVERIFIED":
                        evidence["no_measurement_claim"] = None
                    evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
                    result = subprocess.run(
                        [*command, "grade", "cohesion", str(evidence_path)],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    self.assertEqual(result.returncode, result_code, result.stderr)
                    self.assertEqual(json.loads(result.stdout)["status"], status)
