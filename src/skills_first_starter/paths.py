"""Validate supplied and effective filesystem paths before content access."""

from pathlib import Path


def space_free(path: Path) -> Path:
    """Keep the caller's spelling while rejecting spaced aliases and targets."""
    pending = [path.absolute()]
    inspected = set()
    while pending:
        candidate = pending.pop()
        if candidate in inspected:
            continue
        inspected.add(candidate)
        if " " in str(candidate):
            raise ValueError(
                "paths containing spaces are unsupported; select an explicit space-free path"
            )
        for item in (candidate, *candidate.parents):
            if item.is_symlink():
                target = item.readlink()
                pending.append(target if target.is_absolute() else item.parent / target)
    if " " in str(path.resolve()):
        raise ValueError("resolved path contains spaces; select an explicit space-free path")
    return path
