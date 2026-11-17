"""Launch boundary: load once, wire dependencies and translate safe errors."""

import argparse
import json
import os
import sys
from collections.abc import Sequence
from pathlib import Path

from example_foundations.application import atomic_write_text, run
from example_foundations.configuration import (
    ConfigurationError,
    Overrides,
    load_settings,
    safe_diagnostics,
)


def main(argv: Sequence[str] | None = None) -> int:
    """Render one JSON result without interactive prompts or secret diagnostics."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version="0.1.0")
    parser.add_argument("--config-root", required=True)
    parser.add_argument("--config")
    parser.add_argument("--message", default=argparse.SUPPRESS)
    parser.add_argument("--repeat", default=argparse.SUPPRESS)
    parser.add_argument("--tags", default=argparse.SUPPRESS)
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--output-file", default=argparse.SUPPRESS)
    output.add_argument("--no-output", action="store_true")
    parser.add_argument("--check-config", action="store_true")
    args = parser.parse_args(argv)
    overrides: Overrides = {}
    for key in ("message", "output_file"):
        if hasattr(args, key):
            overrides[key] = getattr(args, key)
    try:
        if not args.config_root:
            raise ConfigurationError("--config-root must be a nonempty explicit path")
        if hasattr(args, "repeat"):
            try:
                overrides["repeat"] = int(args.repeat)
            except ValueError:
                raise ConfigurationError("--repeat must be an integer from 1 to 3") from None
        if hasattr(args, "tags"):
            tags = json.loads(args.tags)
            if not isinstance(tags, list):
                raise ValueError("tags must be a JSON string array")
            overrides["tags"] = tuple(tags)
        if args.no_output:
            overrides["output_file"] = None
        loaded = load_settings(
            config_path=args.config,
            config_root=Path(args.config_root),
            invocation_base=Path.cwd(),
            environ=dict(os.environ),
            overrides=overrides,
        )
    except (ValueError, OSError) as error:
        detail = (
            str(error)
            if isinstance(error, ConfigurationError)
            else "check selected file, schema, paths and documented values"
        )
        print(f"invalid configuration: {detail}", file=sys.stderr)
        return 2
    if args.check_config:
        print(json.dumps(safe_diagnostics(loaded)))
        return 0
    try:
        text = run(loaded.settings, write_text=atomic_write_text)
    except OSError:
        print(
            "output failed; prior data was preserved where replacement did not complete",
            file=sys.stderr,
        )
        return 1
    print(json.dumps({"text": text}))
    return 0
