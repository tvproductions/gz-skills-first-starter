"""Repair native activation in project files while preserving user installations."""

import json
import re
import tomllib

from skills_first_starter.native import project_json
from skills_first_starter.native_json import document, replace_fields


def _plugin_states(parts: list[dict], sources: list[dict]) -> dict[str, bool]:
    """Select the project source and suppress inherited duplicate identities."""
    names = {p["name"] for p in parts}
    desired = {p["name"] + "@skills-first-starter": p["enabled_by_default"] for p in parts}
    for plugins in sources:
        for identity in plugins:
            if identity.split("@", 1)[0] in names and identity not in desired:
                desired[identity] = False
    return desired


def _table_identity(line: str) -> str | None:
    """Recognize quoted native plugin table names using the TOML parser."""
    if not line.lstrip().startswith("["):
        return None
    try:
        plugins = tomllib.loads(line).get("plugins", {})
    except tomllib.TOMLDecodeError:
        return None
    return next(iter(plugins), None)


def _set_plugin_state(text: str, identity: str, active: bool) -> str:
    """Change one enabled boolean while retaining unrelated TOML bytes."""
    lines = text.splitlines(keepends=True)
    newline = "\r\n" if "\r\n" in text else "\n"
    value = str(active).lower()
    expected = tomllib.loads(text)
    expected.setdefault("plugins", {}).setdefault(identity, {})["enabled"] = active
    for start, line in enumerate(lines):
        if _table_identity(line) != identity:
            continue
        if not lines[start].endswith("\n"):
            lines[start] += newline
        end = next(
            (i for i in range(start + 1, len(lines)) if lines[i].lstrip().startswith("[")),
            len(lines),
        )
        for i in range(start + 1, end):
            if re.match(r"\s*enabled\s*=", lines[i]):
                comment = " #" + lines[i].split("#", 1)[1].rstrip("\r\n") if "#" in lines[i] else ""
                candidate = lines.copy()
                candidate[i] = f"enabled = {value}{comment}{newline}"
                rendered = "".join(candidate)
                if tomllib.loads(rendered) == expected:
                    return rendered
        lines.insert(start + 1, f"enabled = {value}{newline}")
        return "".join(lines)
    return text + f"{newline}[plugins.{json.dumps(identity)}]{newline}enabled = {value}{newline}"


def codex_scope(existing: str, inherited: dict, ref: str, parts: list[dict]) -> str:
    """Install project overrides without changing inherited user settings."""
    data = tomllib.loads(existing)
    states = _plugin_states(parts, [inherited.get("plugins", {}), data.get("plugins", {})])
    text = existing
    for identity, active in states.items():
        current = data.get("plugins", {}).get(identity, {}).get("enabled")
        if current is not active:
            text = _set_plugin_state(text, identity, active)
    if "skills-first-starter" not in data.get("marketplaces", {}):
        text += (
            '\n[marketplaces.skills-first-starter]\nsource_type = "git"\n'
            'source = "https://github.com/tvproductions/gz-skills-first-starter.git"\n'
            f'ref = "{ref}"\n'
        )
    return text


def claude_scope(existing: str, inherited: dict, ref: str, parts: list[dict]) -> str:
    """Make project settings authoritative over user-level duplicate sources."""
    data, _ = document(existing)
    data.setdefault("enabledPlugins", {}).update(
        _plugin_states(parts, [inherited.get("enabledPlugins", {}), data.get("enabledPlugins", {})])
    )
    baseline = json.loads(project_json("", "claude", ref, parts))
    # An existing project source retains its reviewed version selection.
    data.setdefault("extraKnownMarketplaces", {}).setdefault(
        "skills-first-starter", baseline["extraKnownMarketplaces"]["skills-first-starter"]
    )
    return replace_fields(existing, data)


def _managed_target(target: str, parts: list[dict]) -> bool:
    """Recognize only the selected identities and their upstream package sources."""
    return any(
        target in (p["name"], "-" + p["name"])
        or target.startswith(p["name"] + "@")
        or p["repository"] in target
        for p in parts
    )


def opencode_scope(existing: str, parts: list[dict]) -> str:
    """Override inherited plugin IDs before loading the project's pinned adapters."""
    data, _ = document(existing)
    if "plugin" in data:
        raise ValueError("OpenCode v1 adapter migration requires review; no files changed")
    plugins = data.get("plugins", [])
    if not isinstance(plugins, list) or any(not isinstance(p, str) for p in plugins):
        raise ValueError("OpenCode plugins must be package strings for scope repair")
    unrelated = [p for p in plugins if not _managed_target(p, parts)]
    targets = [
        f"git+{p['repository']}.git#{p['revision']}" for p in parts if p["enabled_by_default"]
    ]
    data["plugins"] = unrelated + ["-" + p["name"] for p in parts] + targets
    return replace_fields(existing, data)
