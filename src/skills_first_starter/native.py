"""Render repository-owned native settings without invoking global installers."""

import json
from pathlib import Path

from skills_first_starter.native_json import document, replace_fields

HOST_PATHS = {
    "codex": ".codex/config.toml",
    "claude": ".claude/settings.json",
    "opencode": "opencode.json",
}


def configuration_path(root: Path, host: str) -> str:
    """Repair existing JSONC in place rather than shadowing project configuration."""
    if host == "opencode" and (root / "opencode.jsonc").exists():
        if (root / "opencode.json").exists():
            raise ValueError("both OpenCode JSON and JSONC exist; reconcile their precedence first")
        return "opencode.jsonc"
    return HOST_PATHS[host]


def update_skill_path(host: str) -> str:
    """Select the host's native project skill discovery directory."""
    surface = ".claude" if host == "claude" else ".agents"
    return f"{surface}/skills/update-gz-template/SKILL.md"


def _merge_object(data: dict, key: str, additions: dict) -> None:
    """Add absent entries while refusing conflicting project decisions."""
    current = data.setdefault(key, {})
    if not isinstance(current, dict):
        raise ValueError(f"{key} must be an object; reconcile without overwriting")
    for name, value in additions.items():
        if name in current and current[name] != value:
            raise ValueError(f"conflicting {key}.{name}; reconcile without overwriting")
        current[name] = value


def _claude_settings(data: dict, ref: str, parts: list[dict]) -> None:
    """Reconcile Claude's project marketplace and activation maps."""
    _merge_object(
        data,
        "extraKnownMarketplaces",
        {
            "skills-first-starter": {
                "source": {
                    "source": "git",
                    "url": "https://github.com/tvproductions/gz-skills-first-starter.git",
                    "ref": ref,
                },
                "autoUpdate": False,
            }
        },
    )
    enabled = {p["name"] + "@skills-first-starter": p["enabled_by_default"] for p in parts}
    _merge_object(data, "enabledPlugins", enabled)
    names = {p["name"] for p in parts}
    for identity, active in data["enabledPlugins"].items():
        if identity.split("@", 1)[0] in names and identity not in enabled and active:
            raise ValueError(f"duplicate plugin source {identity}; reconcile first")


def _opencode_settings(data: dict, parts: list[dict]) -> None:
    """Preserve unrelated package selections and reconcile the pinned active pair."""
    if "plugin" in data:
        raise ValueError("OpenCode v1 plugin configuration needs explicit v2 reconciliation")
    plugins = data.setdefault("plugins", [])
    if not isinstance(plugins, list) or any(not isinstance(p, str) for p in plugins):
        raise ValueError("OpenCode plugins must be an array of package strings")
    if any("superpowers-backplane" in p and not p.startswith("-") for p in plugins):
        raise ValueError("existing OpenCode Backplane plugin needs explicit readiness review")
    for part in parts:
        if not part["enabled_by_default"]:
            continue
        repository = part["repository"]
        target = f"git+{repository}.git#{part['revision']}"
        if any(repository in p and p != target for p in plugins):
            raise ValueError(f"conflicting OpenCode plugin {part['name']}; reconcile first")
        if target not in plugins:
            plugins.append(target)


def project_json(existing: str, host: str, ref: str, parts: list[dict]) -> str:
    """Preserve unrelated JSON settings and require immutable project sources."""
    data, _ = document(existing)
    before = json.dumps(data, sort_keys=True)
    if host == "claude":
        _claude_settings(data, ref, parts)
    elif host == "opencode":
        _opencode_settings(data, parts)
    else:
        raise ValueError(f"unsupported JSON host: {host}")
    if existing and json.dumps(data, sort_keys=True) == before:
        return existing
    return replace_fields(existing, data)
