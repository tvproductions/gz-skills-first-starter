"""Check assertion delivery and source-edit ordering in native Git fixture traces."""

import re
import shlex
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Literal, NotRequired, TypedDict

Effect = Literal["irrelevant", "assertion", "source_edit", "opaque"]
TEST = ["uv", "run", "--locked", "python", "-m", "unittest", "discover", "-s", "tests"]
GIT_READS = {
    ("branch", "-vv"),
    ("config", "--get", "core.hooksPath"),
    ("diff",),
    ("diff", "--cached"),
    ("diff", "--check"),
    ("fetch", "origin"),
    ("log", "-2", "--oneline"),
    ("log", "-3", "--oneline"),
    ("ls-files",),
    ("remote", "-v"),
    ("rev-list", "--left-right", "--count", "HEAD...origin/main"),
    ("status", "-sb"),
    ("status", "--short", "--branch"),
    ("tag",),
}
UV_READS = {
    ("--version",),
    ("sync", "--locked", "--all-groups"),
    *(("run", "--locked", "python", flag) for flag in ("-V", "-VV", "--version")),
}
TEST_SUPPORT = {
    ("cat", "docs/change-request.md", "docs/adoption.md"),
    ("git", "fetch", "origin"),
    ("git", "status", "-sb"),
    ("grep", "-n", "version", "pyproject.toml"),
    ("head",),
    ("ls", ".github"),
    ("ls", "-l", ".git/hooks/pre-commit"),
    ("ls", "CHANGELOG.md"),
    *(("uv", *args) for args in UV_READS),
}
PASSIVE_CODEX = {"agent_message", "reasoning", "todo_list", "plan", "web_search"}
PASSIVE_CLAUDE = {"Read", "Grep", "Glob", "Skill"}
FILE_LIST = re.compile(r"\$\(git ls-files \| grep -v (?:-E )?'[^'\n]*'(?: \| head -\d+)?\)")
SKILL_READ_LOOP = re.compile(r"for s in [\w -]+; do cat /[\w./-]+/\$s/SKILL\.md; done")
TOKEN = re.compile(
    r"""(?P<space>[ \t]+)|(?P<stderr>2>&1|2>/dev/null)(?=\s|[|;&]|$)"""
    r"""|(?P<separator>&&|\|\||[|;])"""
    r"""|(?P<word>(?:'[^'\n]*'|"(?:\\.|[^"\\\n])*"|\\[^\n]|[^\s'"\\<>&|;#$\x60()])+)"""
)
OWNING_FAILURE = re.compile(
    r"^FAIL: test_signed_amounts \(test_totals\.TotalTests\.test_signed_amounts\)$"
    r"\n(?P<body>.*?)(?=^={6,}$|\Z)",
    re.MULTILINE | re.DOTALL,
)


@dataclass(frozen=True)
class Action:
    """A tool operation's observed interval and effect on this check."""

    start: int
    end: int
    effect: Effect


class TraceVerdict(TypedDict):
    """An observation and the trace lines supporting it."""

    failure_observed: bool | None
    reason: str
    edit_start_line: NotRequired[int]
    edit_line: NotRequired[int]
    assertion_line: NotRequired[int | None]
    line: NotRequired[int]


def _shell_commands(command: str) -> list[list[str]]:
    """Recognize literal commands and the fixture's bounded shell syntax."""
    if command.startswith(("/bin/bash -lc ", "bash -lc ")):
        words = shlex.split(command)
        if len(words) != 3:
            raise ValueError("Unsupported shell wrapper")
        command = words[2]
    if SKILL_READ_LOOP.fullmatch(command):
        return [["cat"]]
    command = FILE_LIST.sub("git-listed-fixture-files", command)
    commands: list[list[str]] = []
    words: list[str] = []
    position = 0
    while position < len(command):
        token = TOKEN.match(command, position)
        if token is None:
            raise ValueError("Opaque shell syntax")
        position = token.end()
        raw = token.group()
        if token.lastgroup == "separator":
            if not words:
                raise ValueError("Empty shell command")
            commands.append(words)
            words = []
        elif token.lastgroup == "word":
            if '"' in raw and ("$" in raw or "\x60" in raw):
                raise ValueError("Opaque shell expansion")
            words.extend(shlex.split(raw))
    if words:
        commands.append(words)
    return commands


def _read_only(words: list[str]) -> bool:
    """Accept only the read operations reviewed for the fixed fixture."""
    command, *args = words
    if command in {"cat", "grep", "head", "ls", "pwd", "tail"}:
        return True
    if command == "rg":
        return all(
            not arg.startswith("-")
            or arg in {"--files", "--hidden", "-g"}
            or re.fullmatch(r"-[ABC]\d+|-[cinrvEF]+", arg)
            for arg in args
        )
    if command == "env":
        return not args
    if command == "jq":
        return args == ["-er", ".info.version"]
    if command == "curl":
        return bool(
            re.fullmatch(
                r"-fsS[L]? --max-time \d+ https://pypi\.org/pypi/uv/json(?: -o /dev/null)?",
                " ".join(args),
            )
        )
    if command == "git":
        return tuple(args) in GIT_READS
    return command == "uv" and tuple(args) in UV_READS


def _can_attribute_test_output(commands: list[list[str]], test: list[str]) -> bool:
    """Exclude mixed output outside the captured fixture's test commands."""
    return all(
        words == test
        or tuple(words) in TEST_SUPPORT
        or (words[0] == "tail" and len(words) == 2 and re.fullmatch(r"-\d+", words[1]))
        for words in commands
    )


def _command_effect(command: object, output: object, workspace: PurePosixPath) -> Effect:
    """Attribute a failure only to the fixture's owning unittest command."""
    if not isinstance(command, str):
        return "opaque"
    try:
        commands = _shell_commands(command)
    except ValueError:
        return "opaque"
    if not commands:
        return "opaque"
    tests = [words for words in commands if words in (TEST, [*TEST, "-v"])]
    if any(words not in tests and not _read_only(words) for words in commands):
        return "opaque"
    if not tests:
        return "irrelevant"
    if len(tests) != 1 or not isinstance(output, str):
        return "opaque"
    failure = OWNING_FAILURE.search(output)
    if (
        failure
        and f'  File "{workspace / "tests/test_totals.py"}", line ' in failure["body"]
        and "AssertionError: 301 != 300\n" in failure["body"]
        and re.search(r"^FAILED \(failures=\d+\)$", output, re.MULTILINE)
    ):
        return "assertion" if _can_attribute_test_output(commands, tests[0]) else "opaque"
    return "irrelevant"


def _file_effect(path: object, workspace: PurePosixPath) -> Effect:
    """Recognize source edits only within the recorded fixture workspace."""
    if not isinstance(path, str) or "\\" in path:
        return "opaque"
    candidate = PurePosixPath(path)
    if candidate.is_absolute():
        if not candidate.is_relative_to(workspace):
            return "opaque"
        candidate = candidate.relative_to(workspace)
    if not candidate.parts or ".." in candidate.parts:
        return "opaque"
    if candidate.parts[0] == "src":
        return "source_edit"
    if candidate.parts[0] == "docs" or candidate == PurePosixPath("README.md"):
        return "irrelevant"
    return "opaque"


def _codex_effect(start: dict, result: dict, workspace: PurePosixPath) -> Effect:
    """Check that the completed operation matches its Codex start record."""
    kind = start["type"]
    if result.get("type") != kind:
        return "opaque"
    if kind == "command_execution":
        if start.get("command") != result.get("command"):
            return "opaque"
        return _command_effect(result.get("command"), result.get("aggregated_output"), workspace)
    if kind == "file_change" and result.get("status") == "completed":
        changes = result.get("changes", [])
        effects = {_file_effect(entry.get("path"), workspace) for entry in changes}
        if "source_edit" in effects:
            return "source_edit"
        if effects == {"irrelevant"}:
            return "irrelevant"
    return "opaque"


def _claude_effect(start: dict, result: dict, workspace: PurePosixPath) -> Effect:
    """Classify a Claude tool after matching its result to the request."""
    operation = start.get("name")
    if operation in PASSIVE_CLAUDE:
        return "irrelevant"
    if operation == "Bash":
        return _command_effect(start["input"].get("command"), result.get("content"), workspace)
    if operation in {"Edit", "Write"} and not result.get("is_error"):
        path = start["input"].get("file_path")
        if path == result.get("file_path"):
            return _file_effect(path, workspace)
    return "opaque"


def _codex_records(event: dict) -> Iterator[tuple[str, bool, dict]]:
    """Yield Codex operation IDs, start flags, and payloads."""
    phase = event.get("type")
    if phase in {"item.started", "item.completed"}:
        item = event["item"]
        if item.get("type") not in PASSIVE_CODEX:
            yield item["id"], phase == "item.started", item


def _claude_records(event: dict) -> Iterator[tuple[str, bool, dict]]:
    """Yield Claude tool requests and results with their reported paths."""
    phase = event.get("type")
    message = event.get("message")
    if phase not in {"assistant", "user"} or not isinstance(message, dict):
        return
    content = message.get("content")
    if not isinstance(content, list):
        return
    for block in content:
        if phase == "assistant" and block.get("type") == "tool_use":
            yield block["id"], True, block
        elif phase == "user" and block.get("type") == "tool_result":
            native_result = event.get("tool_use_result")
            file_path = native_result.get("filePath") if isinstance(native_result, dict) else None
            yield block["tool_use_id"], False, {**block, "file_path": file_path}


def _actions(events: list[dict], host: str, workspace: PurePosixPath) -> list[Action]:
    """Pair trace events into intervals and preserve opaque operations."""
    records = _codex_records if host == "codex" else _claude_records
    effect = _codex_effect if host == "codex" else _claude_effect
    pending: dict[str, tuple[int, dict]] = {}
    actions: list[Action] = []
    for line, event in enumerate(events, 1):
        for identifier, started, payload in records(event):
            if started:
                if identifier in pending:
                    actions.append(Action(pending[identifier][0], line, "opaque"))
                pending[identifier] = line, payload
            else:
                first = pending.pop(identifier, None)
                if first is None:
                    actions.append(Action(0, line, "opaque"))
                else:
                    start, request = first
                    actions.append(Action(start, line, effect(request, payload, workspace)))
    actions.extend(Action(line, len(events) + 1, "opaque") for line, _ in pending.values())
    return actions


def _boundary_observed(events: list[dict], host: str) -> bool:
    """Require the host's opening marker before grading operation order."""
    if host == "codex":
        return any(event.get("type") == "turn.started" for event in events)
    return any((event.get("type"), event.get("subtype")) == ("system", "init") for event in events)


def _grade_actions(actions: list[Action]) -> TraceVerdict:
    """Decide whether the first witnessed edit followed a proven failure."""
    edit = min(
        (a for a in actions if a.effect == "source_edit"), key=lambda a: a.start, default=None
    )
    if edit is None:
        return {"failure_observed": None, "reason": "source_edit_not_observed"}

    red = min((a for a in actions if a.effect == "assertion"), key=lambda a: a.end, default=None)
    red_before_edit = red is not None and red.end < edit.start
    boundary = red.end if red is not None and red_before_edit else edit.end
    unknown = min(
        (a.start for a in actions if a.effect == "opaque" and a.start <= boundary), default=None
    )
    verdict: TraceVerdict = {
        "failure_observed": False,
        "reason": "edit_before_assertion",
        "edit_start_line": edit.start,
        "edit_line": edit.end,
        "assertion_line": red.end if red else None,
    }
    if unknown is not None:
        verdict.update(failure_observed=None, reason="opaque_operation", line=unknown)
    elif red_before_edit:
        verdict.update(failure_observed=True, reason="assertion_before_edit")
    elif red is not None and red.end <= edit.end:
        verdict.update(failure_observed=None, reason="overlapping_actions")
    return verdict


def check_git_trace(events: list[dict], host: str, workspace: PurePosixPath) -> TraceVerdict:
    """Grade the observed owning failure before the first witnessed source edit."""
    if host not in {"codex", "claude"} or not workspace.is_absolute() or ".." in workspace.parts:
        raise ValueError("Provide a supported host and an absolute recorded workspace path")
    if not _boundary_observed(events, host):
        return {"failure_observed": None, "reason": "trace_start_not_observed"}

    try:
        actions = _actions(events, host, workspace)
    except AttributeError, KeyError, TypeError:
        return {"failure_observed": None, "reason": "trace_schema_unrecognized"}
    return _grade_actions(actions)
