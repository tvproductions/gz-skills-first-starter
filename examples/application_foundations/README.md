# Application-foundations reference

This invented Python CLI/library demonstrates the
[configuration contract](../../docs/project-configuration.md) and
[application foundations](../../docs/engineering/application-foundations.md).
It is a local editable dev dependency in the root lock/environment, not a
starter runtime dependency or a reusable shared settings framework. Its version
starts at 0.1.0. Run all development commands from the starter root.

```bash
uv sync --locked --all-groups
uv run --locked example-foundations --config-root /tmp/example-project
uv run --locked python -m unittest discover -s tests -p 'test_application_foundations.py' -v
```

The config root must exist and be space-free; create a task-owned directory
first. Copy settings.example.json to settings.json there when desired. An absent
default file permits built-in defaults; --config and EXAMPLE_FOUNDATIONS_CONFIG
select one file and fail without fallback if invalid/empty/missing. --config-root
is explicit even for service, user and host examples, keeping the demonstration
independent of HOME and native account conventions.

Values: defaults → selected file → documented environment → explicit CLI/API
overrides. Omitted flags preserve lower layers. File-relative paths use that
file's parent; environment/CLI/API paths use the captured invocation base.
No dotenv discovery, interpolation or parent-directory search occurs.

| Setting | Contract |
| --- | --- |
| schema_version | Required integer 1 in a file; bool is invalid |
| message | 1–1024 characters; default Hello example |
| repeat | Integer 1–3; default 1 |
| tags | Array of at most eight nonempty strings, up to 64 characters each; default empty |
| output_file | Null disables output; otherwise a nonempty space-free path with existing parent |
| credential_ref | Null or env:EXAMPLE_FOUNDATIONS_TOKEN; never a literal credential |

Reject duplicate/unknown keys, wrong types, malformed/nonfinite JSON and files
over 64 KiB. Arrays/scalars replace. Empty values are invalid except the explicitly
documented null cases. No extension namespace is supported. A selected credential
reference requires nonempty environment injection; resolved values never enter
the result or diagnostics. This illustrates injection without inventing a
network service. Test sentinels are generated in tests, never committed examples.

Supported environment inputs: EXAMPLE_FOUNDATIONS_CONFIG selects a file;
EXAMPLE_FOUNDATIONS_MESSAGE, EXAMPLE_FOUNDATIONS_REPEAT,
EXAMPLE_FOUNDATIONS_TAGS (JSON array) and EXAMPLE_FOUNDATIONS_OUTPUT_FILE
override values. Empty input fails; unrelated variables are ignored.
EXAMPLE_FOUNDATIONS_TOKEN is a sensitive required input only when referenced.
Configuration is loaded once; reload is unsupported. child_environment forwards
only explicitly named keys, including secrets only when deliberately selected.

CLI: --config-root PATH, --config PATH, --message TEXT, --repeat INTEGER,
--tags JSON, --output-file PATH or --no-output, and --check-config. Rendering
returns one JSON object on stdout; diagnostics use stderr. Help/version exit 0,
invalid usage/config exits 2, output failure exits 1. There is no interactive
prompt. --check-config prints safe effective values/source labels without writing.
Content spaces are preserved; spaced supplied/resolved paths, parents and
symlink targets reject before content access/effects.

Library consumers call load_settings with explicit config_path, config_root,
invocation_base, environ and overrides. The exported Settings type holds finished
values. domain.render_message receives values only; application.run receives
an injected writer; cli.main selects the concrete writer once. configuration.py
owns external inputs, application.py the filesystem adapter, and domain.py pure
rendering. Importing the package does not load settings. The complete typed
contract is in the [implementation plan](../../docs/superpowers/plans/2026-11-16-application-foundations.md#modules-and-typed-interfaces).

Output uses a temporary sibling and atomic replacement, cleaning up after a
failure. The prior file survives a reached failed replace. Settings cannot be
an output target. Concurrent writers are last successful replacement wins;
there is no transaction/retry or power-loss durability promise. Shutdown closes
resources synchronously. Output failure reports recovery guidance: inspect the
unchanged prior output, correct permissions/destination and retry explicitly.

Deploy the built wheel with configuration external to installed code. Upgrades
or reinstalls replace code, not settings. Preserve the prior wheel and external
settings for rollback; schema migration is explicit, never performed on read.
No telemetry, background service, retained personal records, clock or networking
is present. Output files are operator-owned; operators choose retention/deletion.
Report scaffold vulnerabilities through the canonical starter repository's
private GitHub vulnerability reporting when available, otherwise request a
private reporting channel without posting credentials or sensitive details.

Source and example ship in the starter sdist; the starter wheel carries no
example runtime. For independent packaging use:

```bash
uv build --no-sources --project examples/application_foundations --out-dir /tmp/example-foundations-artifacts
uv build --no-sources
uv run --locked python tools/verify_distribution.py
```

Use a fresh task-owned artifact directory. The final checker extracts the root
sdist, builds this package there, installs its wheel into a clean environment,
then exercises CLI/API behavior outside the checkout, configuration preservation
across reinstall and an invalid explicit selection. Normal unit tests simulate
project/user/service/host roots. Neither establishes real native-account
permissions, embedded runtime, GUI/web/TUI delivery, or all-platform acceptance.
