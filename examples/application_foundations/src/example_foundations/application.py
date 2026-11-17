"""Orchestration with one injected writer and a small filesystem adapter."""

import os
import tempfile
from collections.abc import Callable
from pathlib import Path

from example_foundations.configuration import Settings, checked_path
from example_foundations.domain import render_message


def atomic_write_text(path: Path, text: str) -> None:
    """Replace through a sibling; preserve prior bytes and clean up on failure."""
    path = checked_path(path, Path.cwd())
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=path.parent, delete=False, mode="w", encoding="utf-8", newline=""
        ) as stream:
            temporary = Path(stream.name)
            stream.write(text)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def run(settings: Settings, *, write_text: Callable[[Path, str], None]) -> str:
    """Pass values to the domain and coordinate the selected output effect."""
    text = render_message(settings.message, settings.repeat, settings.tags)
    if settings.output_file is not None:
        write_text(settings.output_file, text)
    return text
