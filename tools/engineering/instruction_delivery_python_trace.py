"""Check observable locked Python invocations in saved instruction-delivery traces."""

import re
import shlex
from collections.abc import Iterator
from pathlib import PureWindowsPath
from typing import Literal, TypedDict

if __package__:
    from tools.engineering.instruction_delivery_native_trace import (
        PASSIVE_CLAUDE,
        boundary_observed,
        claude_records,
        codex_records,
    )
else:
    from instruction_delivery_native_trace import (
        PASSIVE_CLAUDE,
        boundary_observed,
        claude_records,
        codex_records,
    )

Effect = Literal["locked", "violation", "opaque", "irrelevant"]
PYTHON = re.compile(r"(?:pythonw?(?:3(?:\.\d+)?)?|py)(?:\.exe)?", re.IGNORECASE)
ASSIGNMENT = re.compile(r"[A-Za-z_]\w*=")
HEREDOC = re.compile(r"<<'(?P<end>[A-Za-z_]\w*)'[ \t]*\n(?:.*?\n)?(?P=end)(?=\n|$)", re.DOTALL)
TOKEN = re.compile(
    r"""(?P<space>[ \t]+)|(?P<stderr>2>&1|2>/dev/null)(?=\s|[|;&]|$)"""
    r"""|(?P<separator>&&|\|\||[|;\n])"""
    r"""|(?P<word>(?:'[^']*'|"(?:\\.|[^"\\])*"|\\[^\n]|[^\s'"\\<>&|;#$`(){\}])+)"""
)
READS = {
    "cat",
    "cmp",
    "curl",
    "grep",
    "head",
    "jq",
    "ls",
    "nl",
    "pwd",
    "rg",
    "shasum",
    "tail",
    "wc",
    "which",
}
UV_FLAGS = {"--locked", "--frozen", "--no-sync", "--offline", "--no-python-downloads", "--no-cache"}
UV_TOOLS = {"cohesion", "ruff", "ty"}
SHELL_CONTROL = {
    "if",
    "then",
    "elif",
    "else",
    "fi",
    "for",
    "while",
    "until",
    "do",
    "done",
    "case",
    "esac",
    "function",
    "select",
    "exit",
    "return",
    "exec",
    "source",
    ".",
    "eval",
    "set",
    "trap",
    "break",
    "continue",
}


class Observation(TypedDict):
    """A trace index and native event line, without command contents."""

    trace: int
    line: int


class PythonVerdict(TypedDict):
    """The status of the bounded observation and its supporting locations."""

    status: str
    locked: list[Observation]
    violations: list[Observation]
    unverified: list[Observation]


def _shell_steps(command: str) -> list[tuple[str, list[str]]]:
    """Recognize separate literal commands and retain their execution separators."""
    if command.startswith(("/bin/bash -lc ", "bash -lc ")):
        wrapper = shlex.split(command)
        if len(wrapper) != 3:
            raise ValueError("Unknown shell wrapper")
        command = wrapper[2]
    command = command.strip()
    heredoc = HEREDOC.search(command)
    if heredoc is not None and heredoc.end() == len(command):
        command = command[: heredoc.start()]
    steps: list[tuple[str, list[str]]] = []
    words: list[str] = []
    separator = ""
    position = 0
    while position < len(command):
        token = TOKEN.match(command, position)
        if not token:
            raise ValueError("Unknown shell syntax")
        position = token.end()
        if token.lastgroup == "word":
            raw = token.group()
            if '"' in raw and any(mark in raw for mark in ("$(", "`")):
                raise ValueError("Command substitution")
            words.extend(shlex.split(raw))
        elif token.lastgroup == "separator" and words:
            steps.append((separator, words))
            separator, words = token.group(), []
        elif token.lastgroup == "separator" and token.group() != "\n":
            raise ValueError("Empty shell command")
    if words:
        steps.append((separator, words))
    elif separator in {"&&", "||", "|"}:
        raise ValueError("Incomplete shell command")
    return steps


def _uv_effect(args: list[str]) -> Effect:
    """Grade the supported uv invocation forms without assuming a resolved runtime."""
    start = 1 if args[:1] == ["--no-cache"] else 0
    if args[start : start + 1] != ["run"]:
        return "irrelevant" if args[:1] in (["--version"], ["sync"]) else "opaque"
    index = start + 1
    flags = set()
    while index < len(args) and args[index] in UV_FLAGS:
        flags.add(args[index])
        index += 1
    if index == len(args):
        return "opaque"
    name = args[index]
    if name == "python" and "--locked" in flags and "--frozen" not in flags:
        return "locked"
    if PYTHON.fullmatch(PureWindowsPath(name).name):
        return "violation"
    return "irrelevant" if name in UV_TOOLS else "opaque"


def _effect(words: list[str]) -> Effect:
    """Distinguish an executable position from arguments such as inspected paths."""
    index = 1 if words[0] == "env" else 0
    while index < len(words) and ASSIGNMENT.match(words[index]):
        index += 1
    if index == len(words):
        return "irrelevant"
    command, *args = words[index:]
    if PYTHON.fullmatch(PureWindowsPath(command).name):
        return "violation"
    if command == "uv":
        return _uv_effect(args)
    if command == "rg" and any(arg.startswith("--pre") for arg in args):
        return "opaque"
    if command in READS or (command == "command" and args[:1] in (["-v"], ["-V"])):
        return "irrelevant"
    if command == "git" and args[:1] in (["status"], ["diff"], ["log"], ["rev-parse"]):
        return "irrelevant"
    return "opaque"


def _command_effects(command: object, succeeded: bool) -> Iterator[Effect]:
    """Keep conditional invocations unknown unless the chain proves they ran."""
    try:
        steps = _shell_steps(command) if isinstance(command, str) else []
    except ValueError:
        steps = []
    if not steps or any(words[0] in SHELL_CONTROL for _, words in steps):
        yield "opaque"
        return
    chain_completed = succeeded and all(sep in {"", "&&", "|"} for sep, _ in steps)
    conditional = False
    for separator, words in steps:
        if separator in {";", "\n"}:
            conditional = False
        elif separator in {"&&", "||"}:
            conditional = not chain_completed
        effect = _effect(words)
        yield "opaque" if conditional and effect in {"locked", "violation"} else effect


def _completed_effects(host: str, request: dict, result: dict) -> Iterator[Effect]:
    """Identify shell operations at the native trace boundary."""
    if host == "codex":
        if request.get("type") == "file_change" and result.get("type") == "file_change":
            return
        if request.get("type") == result.get("type") == "command_execution":
            code = result.get("exit_code")
            if request.get("command") == result.get("command") and type(code) is int:
                yield from _command_effects(result.get("command"), code == 0)
                return
    else:
        name = request.get("name")
        if name in PASSIVE_CLAUDE or name in {"Edit", "Write", "MultiEdit", "TodoWrite"}:
            return
        if name == "Bash":
            content = result.get("content")
            denied = isinstance(content, str) and content.startswith(
                (
                    "Permission for this tool use was denied.",
                    "Permission to use Bash has been denied.",
                )
            )
            if not (result.get("is_error") and denied):
                yield from _command_effects(
                    request["input"].get("command"), result.get("is_error") is False
                )
                return
    yield "opaque"


def _observations(events: list[dict], host: str) -> Iterator[tuple[int, Effect]]:
    """Pair requests and completions, retaining gaps from missing or opaque events."""
    records = codex_records if host == "codex" else claude_records
    terminal = "turn.completed" if host == "codex" else "result"
    if not boundary_observed(events, host) or not any(e.get("type") == terminal for e in events):
        yield 0, "opaque"
    pending: dict[str, tuple[int, dict]] = {}
    for line, event in enumerate(events, 1):
        try:
            for identifier, started, payload in records(event):
                if started:
                    if identifier in pending:
                        yield pending[identifier][0], "opaque"
                    pending[identifier] = line, payload
                elif (request := pending.pop(identifier, None)) is None:
                    yield line, "opaque"
                else:
                    for effect in _completed_effects(host, request[1], payload):
                        yield line, effect
        except AttributeError, KeyError, TypeError:
            yield line, "opaque"
    for line, _ in pending.values():
        yield line, "opaque"


def check_locked_python(traces: list[list[dict]], host: str) -> PythonVerdict:
    """Grade only recorded invocations and retain violations alongside unknowns."""
    grouped: dict[Effect, list[Observation]] = {
        "locked": [],
        "violation": [],
        "opaque": [],
        "irrelevant": [],
    }
    for trace, events in enumerate(traces, 1):
        for line, effect in dict.fromkeys(_observations(events, host)):
            if effect != "irrelevant":
                grouped[effect].append({"trace": trace, "line": line})
    status = "NOT_APPLICABLE"
    if grouped["violation"]:
        status = "FAIL"
    elif grouped["opaque"] or not traces:
        status = "UNVERIFIED"
    elif grouped["locked"]:
        status = "PASS"
    return {
        "status": status,
        "locked": grouped["locked"],
        "violations": grouped["violation"],
        "unverified": grouped["opaque"],
    }
