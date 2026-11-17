"""Explicit, validated startup configuration for the invented application."""

import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import TypedDict, cast

PREFIX = "EXAMPLE_FOUNDATIONS_"
OWNED = {"schema_version", "message", "repeat", "tags", "output_file", "credential_ref"}


class ConfigurationError(ValueError):
    """Invalid input with a controlled, secret-free diagnostic."""


class Overrides(TypedDict, total=False):
    """Explicit values; omitted keys leave lower-precedence layers intact."""

    message: str
    repeat: int
    tags: tuple[str, ...]
    output_file: str | None


@dataclass(frozen=True)
class Settings:
    """Validated values consumed by the application boundary."""

    message: str
    repeat: int
    tags: tuple[str, ...]
    output_file: Path | None
    credential: str | None = field(repr=False, compare=False, default=None)


@dataclass(frozen=True)
class LoadedSettings:
    """Resolved values and their safe selection/source metadata."""

    settings: Settings
    selected_file: Path | None
    sources: Mapping[str, str]


def checked_path(value: str | Path, base: Path) -> Path:
    """Reject supplied and effective spaced paths before content access."""
    if not str(value) or " " in str(value):
        raise ConfigurationError(
            "path must be nonempty and space-free; select an explicit alternate root"
        )
    path = Path(value)
    if not path.is_absolute():
        path = base / path
    pending = [path.absolute()]
    inspected = set()
    while pending:
        candidate = pending.pop()
        if candidate in inspected:
            continue
        inspected.add(candidate)
        if " " in str(candidate):
            raise ConfigurationError("path contains spaces; select an explicit alternate root")
        for item in (candidate, *candidate.parents):
            if item.is_symlink():
                target = item.readlink()
                pending.append(target if target.is_absolute() else item.parent / target)
    if " " in str(path.absolute()) or " " in str(path.resolve()):
        raise ConfigurationError("resolved path contains spaces; select an explicit alternate root")
    return path.resolve()


def _pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """Reject duplicate JSON keys instead of silently taking the last."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ConfigurationError("duplicate settings key")
        result[key] = value
    return result


def _nonfinite(value: str) -> object:
    """Reject JSON spellings that are outside finite contractual data."""
    raise ConfigurationError("nonfinite JSON number")


def _valid(values: Mapping[str, object]) -> None:
    """Validate each supplied layer without echoing rejected values."""
    message, repeat, tags = values["message"], values["repeat"], values["tags"]
    if not isinstance(message, str) or not 1 <= len(message) <= 1024:
        raise ConfigurationError("message must contain 1 to 1024 characters")
    if type(repeat) is not int or not 1 <= repeat <= 3:
        raise ConfigurationError("repeat must be an integer from 1 to 3")
    if (
        not isinstance(tags, (list, tuple))
        or len(tags) > 8
        or any(not isinstance(tag, str) or not 1 <= len(tag) <= 64 for tag in tags)
    ):
        raise ConfigurationError(
            "tags must contain at most eight nonempty strings of up to 64 characters"
        )
    output = values["output_file"]
    if output is not None and (not isinstance(output, str) or not output):
        raise ConfigurationError("output_file must be null or a nonempty path")
    if values["credential_ref"] not in (None, "env:EXAMPLE_FOUNDATIONS_TOKEN"):
        raise ConfigurationError("credential_ref must name the documented injected credential")


def _selected_file(
    config_path: str | Path | None, config_root: Path, base: Path, environ: Mapping[str, str]
) -> Path | None:
    """Resolve the declared selection without fallback after explicit input."""
    root = checked_path(config_root, base)
    if not root.is_dir():
        raise ConfigurationError("config_root must be an existing directory")
    explicit = config_path is not None or PREFIX + "CONFIG" in environ
    selected = config_path if config_path is not None else environ.get(PREFIX + "CONFIG")
    path = checked_path(selected if selected is not None else root / "settings.json", base)
    return path if explicit or path.exists() else None


def _read_file(path: Path) -> dict[str, object]:
    """Read bounded UTF-8 JSON and validate the file-owned schema."""
    if not path.is_file():
        raise ConfigurationError("selected settings file must be an existing regular file")
    try:
        with path.open("rb") as stream:
            content = stream.read(65537)
        if len(content) > 65536:
            raise ConfigurationError("settings file exceeds 64 KiB")
        data = json.loads(
            content.decode("utf-8"), object_pairs_hook=_pairs, parse_constant=_nonfinite
        )
    except OSError, UnicodeError, ValueError:
        raise ConfigurationError(
            "selected settings file must be accessible, UTF-8 and valid JSON"
        ) from None
    if not isinstance(data, dict) or set(data) - OWNED:
        raise ConfigurationError("settings must be an object containing only owned keys")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ConfigurationError("schema_version must be integer 1")
    data.pop("schema_version")
    return data


def _apply_environment(
    values: dict[str, object], environ: Mapping[str, str], base: Path
) -> dict[str, str]:
    """Parse documented process inputs while preserving absent/empty semantics."""
    sources = {}
    for key in ("message", "repeat", "tags", "output_file"):
        name = PREFIX + key.upper()
        if name not in environ:
            continue
        text = environ[name]
        if not text:
            raise ConfigurationError(f"{name} must not be empty")
        try:
            value = int(text) if key == "repeat" else json.loads(text) if key == "tags" else text
        except ValueError:
            raise ConfigurationError(f"{name} has an invalid documented value") from None
        values[key] = value
        _valid(values)
        sources[key] = "environment"
        if key == "output_file":
            checked_path(text, base)
    return sources


def load_settings(
    *,
    config_path: str | Path | None,
    config_root: Path,
    invocation_base: Path,
    environ: Mapping[str, str],
    overrides: Overrides,
) -> LoadedSettings:
    """Select one file, validate every supplied layer and pass finished values."""
    base = checked_path(invocation_base, Path.cwd())
    path = _selected_file(config_path, config_root, base, environ)
    values: dict[str, object] = {
        "message": "Hello example",
        "repeat": 1,
        "tags": [],
        "output_file": None,
        "credential_ref": None,
    }
    sources = {key: "default" for key in values}
    output_base = base
    if path is not None:
        data = _read_file(path)
        values.update(data)
        _valid(values)
        sources.update({key: "file" for key in data})
        output_base = path.parent if "output_file" in data else base
        if values["output_file"] is not None:
            checked_path(str(values["output_file"]), output_base)
    environment_sources = _apply_environment(values, environ, base)
    sources.update(environment_sources)
    if "output_file" in environment_sources:
        output_base = base
    if set(overrides) - {"message", "repeat", "tags", "output_file"}:
        raise ConfigurationError("unknown explicit setting")
    values.update(overrides)
    _valid(values)
    sources.update({key: "explicit" for key in overrides})
    if "output_file" in overrides:
        output_base = base
    output = (
        checked_path(str(values["output_file"]), output_base)
        if values["output_file"] is not None
        else None
    )
    if output is not None and (output == path or not output.parent.is_dir()):
        raise ConfigurationError(
            "output must have an existing parent and must not replace settings"
        )
    credential = None
    if values["credential_ref"] is not None:
        credential = environ.get(PREFIX + "TOKEN")
        if not credential:
            raise ConfigurationError("required injected credential is missing or empty")
    return LoadedSettings(
        Settings(
            cast(str, values["message"]),
            cast(int, values["repeat"]),
            tuple(cast(Sequence[str], values["tags"])),
            output,
            credential,
        ),
        path,
        sources,
    )


def safe_diagnostics(loaded: LoadedSettings) -> dict[str, object]:
    """Expose only nonsecret values and winning source labels."""
    settings = loaded.settings
    return {
        "values": {
            "message": settings.message,
            "repeat": settings.repeat,
            "tags": settings.tags,
            "output_file": str(settings.output_file) if settings.output_file else None,
        },
        "sources": {k: v for k, v in loaded.sources.items() if k != "credential_ref"},
    }


def child_environment(
    environ: Mapping[str, str], *, forwarded: Sequence[str] = ()
) -> dict[str, str]:
    """Forward only names explicitly selected by the process owner."""
    return {key: environ[key] for key in forwarded if key in environ}
