"""Read tool-operation records from the fixed Codex and Claude trace formats."""

from collections.abc import Iterator

PASSIVE_CODEX = {"agent_message", "reasoning", "todo_list", "plan", "web_search"}
PASSIVE_CLAUDE = {"Read", "Grep", "Glob", "Skill"}


def codex_records(event: dict) -> Iterator[tuple[str, bool, dict]]:
    """Yield Codex operation IDs, start flags, and payloads."""
    phase = event.get("type")
    if phase in {"item.started", "item.completed"}:
        item = event["item"]
        if item.get("type") not in PASSIVE_CODEX:
            yield item["id"], phase == "item.started", item


def claude_records(event: dict) -> Iterator[tuple[str, bool, dict]]:
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


def boundary_observed(events: list[dict], host: str) -> bool:
    """Require the host's opening marker before grading operation order."""
    if host == "codex":
        return any(event.get("type") == "turn.started" for event in events)
    return any((event.get("type"), event.get("subtype")) == ("system", "init") for event in events)
