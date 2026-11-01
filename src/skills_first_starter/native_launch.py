"""Launch OpenCode with project-owned config instead of conflicting inherited plugins."""

import json
import os
import subprocess
from pathlib import Path

from skills_first_starter.native import configuration_path
from skills_first_starter.native_json import document


def _merge(base: dict, override: dict) -> dict:
    """Retain user preferences where the project has not selected another value."""
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = _merge(result[key], value)
        else:
            result[key] = value
    return result


def launch(project: Path, arguments: list[str]) -> int:
    """Isolate config for a private server without editing user settings or installs."""
    root = project.resolve(strict=True)
    path = root / configuration_path(root, "opencode")
    settings, _ = document(path.read_text(encoding="utf-8"))
    config_root = Path(os.environ.get("OPENCODE_CONFIG_DIR", str(Path.home() / ".config/opencode")))
    inherited = {}
    for name in ("opencode.json", "opencode.jsonc"):
        user_file = config_root / name
        if user_file.exists():
            inherited = _merge(inherited, document(user_file.read_text(encoding="utf-8"))[0])
    inherited.pop("plugins", None)
    inherited.pop("plugin", None)
    effective = _merge(inherited, settings)
    skills = list(effective.get("skills", []))
    for surface in (".claude/skills", ".agents/skills", ".opencode/skills"):
        source = root / surface
        if source.is_dir() and str(source) not in skills:
            skills.append(str(source))
    if skills:
        effective["skills"] = skills
    if "--server" in arguments or any(arg.startswith("--server=") for arg in arguments):
        raise ValueError("project OpenCode must use its own server, not a shared server")
    if "service" in arguments:
        raise ValueError("project OpenCode must not change the user's background service")
    if any(
        arguments[i : i + 2] in (["plugin", "add"], ["plugin", "remove"])
        for i in range(len(arguments))
    ):
        raise ValueError("edit project plugin selections; do not use global plugin add/remove")
    env = os.environ.copy()
    env["OPENCODE_CONFIG_DIR"] = str(root / ".opencode")
    env["OPENCODE_CONFIG_PROJECT_DISABLE"] = "true"
    env["OPENCODE_CONFIG"] = str(path)
    env["OPENCODE_CONFIG_CONTENT"] = json.dumps(effective)
    command = ["opencode", *arguments]
    if (not arguments or arguments[0] != "serve") and "--standalone" not in arguments:
        command.append("--standalone")
    return subprocess.run(command, cwd=root, env=env, check=False).returncode
