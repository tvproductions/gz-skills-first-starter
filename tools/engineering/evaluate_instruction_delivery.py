"""Grade fixed instruction delivery cases from observed trial evidence."""

import argparse
import json
from collections.abc import Mapping
from pathlib import Path, PurePosixPath

if __package__:
    from tools.engineering.instruction_delivery_git_trace import check_git_trace
else:
    from instruction_delivery_git_trace import check_git_trace

FIXTURES = Path(__file__).parent / "fixtures" / "instruction-delivery-v1.json"


def load_cases(path: Path) -> dict[str, tuple[str, ...]]:
    """Load the required, ordered check names for each fixed case."""
    data = json.loads(path.read_text(encoding="utf-8"))
    cases = {name: tuple(case["checks"]) for name, case in data.items()}
    if not cases or any(not checks for checks in cases.values()):
        raise ValueError("Each case must have at least one check")
    return cases


def score_trial(
    checks: tuple[str, ...], evidence: Mapping[str, object]
) -> dict[str, str | list[str]]:
    """Return a verdict without inferring a pass from missing evidence."""
    extra = sorted(evidence.keys() - set(checks))
    if extra:
        raise ValueError(f"Unknown observation keys: {', '.join(extra)}")
    for name, value in evidence.items():
        if value is not None and not isinstance(value, bool):
            raise ValueError(f"{name} must be true, false, or null")

    failed = [name for name in checks if evidence.get(name) is False]
    unverified = [name for name in checks if evidence.get(name) is None]
    status = "PASS"
    if failed:
        status = "FAIL"
    elif unverified:
        status = "UNVERIFIED"
    return {"status": status, "failed": failed, "unverified": unverified}


def main() -> int:
    """Prepare or grade one case without launching an agent."""
    cases = load_cases(FIXTURES)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "grade", "trace"))
    parser.add_argument("case", choices=cases)
    parser.add_argument("path", type=Path, help="fixture directory, JSON evidence, or native JSONL")
    parser.add_argument("--host", choices=("codex", "claude"))
    parser.add_argument(
        "--workspace", type=PurePosixPath, help="recorded fixture workspace for trace"
    )
    args = parser.parse_args()
    try:
        if args.action == "trace":
            if args.case != "git-sync" or args.host is None or args.workspace is None:
                parser.error("trace requires git-sync, --host and --workspace")
            events = [
                json.loads(line)
                for line in args.path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            if not all(isinstance(event, dict) for event in events):
                raise ValueError("Trace must contain JSON objects")
            result = check_git_trace(events, args.host, args.workspace)
            status, code = {True: ("PASS", 0), False: ("FAIL", 1), None: ("UNVERIFIED", 3)}[
                result["failure_observed"]
            ]
            print(json.dumps({"case": args.case, "status": status, **result}, indent=2))
            return code

        if args.action == "prepare":
            data = json.loads(FIXTURES.read_text(encoding="utf-8"))
            files = data[args.case]["files"]
            relative_paths = [PurePosixPath(name) for name in files]
            if not files or any(
                not path.parts
                or path.is_absolute()
                or ".." in path.parts
                or "\\" in path.as_posix()
                or ":" in path.as_posix()
                for path in relative_paths
            ):
                raise ValueError("Fixture must contain only relative file paths")
            args.path.mkdir()
            for name, content in files.items():
                target = args.path / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8", newline="\n")
            return 0

        evidence = json.loads(args.path.read_text(encoding="utf-8"))
        if not isinstance(evidence, dict):
            raise ValueError("Evidence must be a JSON object")
        result = score_trial(cases[args.case], evidence)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps({"case": args.case, **result}, indent=2))
    return {"PASS": 0, "FAIL": 1, "UNVERIFIED": 3}[str(result["status"])]


if __name__ == "__main__":
    raise SystemExit(main())
