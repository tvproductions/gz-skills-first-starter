# Application Foundations Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan on `main`. Checkboxes track deliverables; follow the repository's risk-based verification policy.

**Goal:** Deliver the approved 0.11.0 application-foundations guidance, a bounded reference fixture, and the selected starter path behavior with observable evidence.

**Architecture:** Keep configuration and effects at a project-owned application boundary. The starter publishes guidance and a small invented example, not a shared loader or framework; its existing helper retains its public seams. Respect explicit informed departures and preserve existing mandatory policy.

**Tech Stack:** Python 3.14, uv, standard library, unittest, existing Ruff/ty/pre-commit configuration.

**Spec:** [Design edition 3](../specs/2026-11-16-application-foundations-design.md), SHA-256 `54b2a94c5be72dfa93abb65101db384f3c2dad61c720e53b095b6bdc191367a6`; maintainer approval recorded in the [handoff](../../handoffs/2026-11-16-application-foundations-design-handoff.md).

**Plan revision:** November 17, 2026; the three main-conversation review findings
are addressed below. ADR-0002 edition 2 was separately approved November 17; implementation and the
independent-review correction pass are complete locally. Final evidence is in
[the implementation receipt](../../evidence/2026-11-17-application-foundations.md). Preserve the completed, currently
uncommitted dependency maintenance when executing; do not roll back those locks.

## Global Constraints

- **Gate:** Obtain separate explicit approval of [ADR-0002 edition 2](../../decisions/ADR-0002-002-runtime-configuration-boundary.md), SHA-256 `94b414de72d191ab9d3cd7c7fcc968e6beb708eeb93e9d24fea09d341212758b`, before configuration-boundary implementation. Capture actual approval and preserve reviewed bytes under the ADR policy. This plan is not approval.
- Work directly on `main`; preserve unrelated changes, published tags, normal hooks, Python N-1 policy, four routine hook categories and the 0.11.0 pending target. No publication, plugin activation, real-adopter or companion-repository changes.
- Use `uv run --locked` and unittest, not pytest. Keep the broader Ruff/ty patch, 14-finding remediation and quota deferred. Cognitive qualification remains DEFERRED / measurement UNKNOWN.
- Reject U+0020 in supplied and resolved paths, including parents and symlink targets, before target content access, writes or parent creation. Preserve contents containing spaces and leave existing data unchanged on rejection.
- Both adopter lanes receive the guidance. Every adopter identifies deployment/configuration ownership; library and plugin consumers may supply values. Do not introduce a generic loader, GZKit lifecycle, new local workflow skill or new helper command.
- Maintain privacy: invented fixtures only, no real secrets, no implicit dotenv discovery; identify platform/host and release evidence that remains unknown.

## Review Focus

1. A relative path or symlink resolves to a spaced parent: reject before access or creation (Task 1).
2. An explicit missing or invalid configuration file would otherwise fall back: fail before effects (Task 3).
3. Empty environment input differs from an absent variable; omitted CLI flags do not mask lower layers (Task 3).
4. A secret sentinel appears in an error, diagnostic, child environment or distribution (Tasks 3 and 5).
5. A human departure is repeated or described as conformant despite missing evidence (Tasks 2 and 4).

## File map and sequencing

- `src/skills_first_starter/cli.py`, `native_launch.py` and affected path consumers: validate public and derived paths before effects; do not weaken existing preservation checks.
- `tests/test_starter.py`, `tests/test_native_hosts.py`, `tests/test_native_launch.py`: public seam regressions appropriate to affected entry points.
- `docs/project-configuration.md`, `docs/engineering/naming-and-layout.md`, new `docs/engineering/application-foundations.md`: configuration, all 15 naming/layout topics, and remaining foundations respectively.
- `docs/adoption.md`, `docs/adoption-workflow.md`, `docs/baseline-policy.md`, `docs/structure.md`, `templates/AGENTS.skills-first.md`, `templates/skills/update-gz-template/SKILL.md`: concise pointers, applicability, ownership and migration; modify only where needed.
- `examples/application_foundations/`: invented CLI/library fixture with its own packaging metadata, sharing the root lock, environment and tool settings. This is illustrative and is not a starter runtime dependency.
- `pyproject.toml`, `uv.lock`, `.pre-commit-config.yaml`, `tests/test_application_foundations.py`, `tools/verify_distribution.py`: install the local fixture in the dev group, include its source in ty and distribution checks, and run its unittest cases through existing discovery. Keep exactly four routine hook categories.
- `ROADMAP.md`, `CHANGELOG.md`, existing handoff and a dated evidence record: reconcile scope, observed evidence and unresolved limits. Regenerate packaged copies through `tools/package_resources.py` when authoritative resources change.

## Task 1: Starter path contract

**Files:** `src/skills_first_starter/cli.py`, affected native path consumers, `tests/test_starter.py`, `tests/test_native_hosts.py`, `tests/test_native_launch.py`.

**Interfaces:** Preserve `configure`, `localize`, `status`, `backport`, `check_path` and `main` public signatures and existing error/exit conventions. Reuse a single internal path validator if feasible; it must validate original and resolved paths without reading target contents.

- [x] Inventory every path accepted or derived by the API and CLI, installed resource paths, symlink handling, process paths and existing preflight/write ordering. Record which entry points can cause effects and any platform limitation.
- [x] Add public-seam unittest cases for API and CLI: supplied spaced project path, a space-free symlink resolving to a spaced target, a spaced parent or managed child, and a valid space-free control. For each rejected write, assert existing sentinel bytes are unchanged and missing parents remain absent. Include a file whose *contents* contain spaces and assert those bytes survive.
- [x] Prove the pre-read requirement with `unittest.mock`: wrap `Path.open` and `builtins.open`, retaining their real functions for unrelated reads, and raise `AssertionError` if the path is the protected input or resolves beneath its protected root. Call `configure`, `localize`, `status`, `backport` and `main` through their public seams with spaced supplied/resolved paths. Require the normal rejection rather than the guard's assertion; instrument mutation/process entry points to assert no writes, parent creation or launch. Add a positive control that deliberately reads the protected file and trips the guard, so a wrongly targeted guard cannot pass silently. Scope guards to target content, permitting metadata resolution (`stat`/`readlink`) and unrelated packaged-resource reads. Use separate subprocess CLI controls for exit/output and unchanged bytes; those controls alone do not prove no reads.
- [x] Run the focused tests and confirm the rejection regressions fail for the intended reason. Implement validation before target content reads or mutation, including all planned targets before the first write. Return an actionable `AdoptionError`/CLI failure without changing the existing API shape.
- [x] Run `uv run --locked python -m unittest discover -s tests -p 'test_starter.py' -v` and the affected native-host/launch test modules. Inspect behavior for resource paths and unsupported platforms; record evidence rather than generalizing.

## Task 2: Guidance and migration

**Files:** configuration, naming/layout, application foundations and adopter pointers listed above.

**Interfaces:** The configuration contract is the authoritative runtime-settings guidance; `pyproject.toml` remains authoritative for packaging/dependencies/tool configuration. Existing `.gz-skills/settings.json` remains distinct.

- [x] After ADR approval, replace the current either-TOML-or-JSON runtime recommendation with the approved ownership, scope and location rules, file selection and value precedence, validation, secret handling, explicit host/library responsibility and no-spaces contract. Explain explicit invalid-selection failure and configuration preservation across replacement.
- [x] Reconcile each of the 15 numbered naming/layout sections against edition 3, including web application classification and paths. Remove claims that the deferred Ruff/ty patch is active. Preserve compatibility names and external schemas.
- [x] Publish the remaining foundations in a focused engineering page: errors, logging/output, paths, persistence/recovery, external calls, trust, data semantics, operations, privacy and interfaces. Give applicability and observable evidence; distinguish recommendations, mandatory existing requirements and informed overrides.
- [x] Inventory the starter's actual configuration and effect boundaries; document its applicable choices or explicitly authorized departures without creating an unused settings file. Update adopter migration and update-skill guidance to inventory existing contracts, preview, preserve data and obtain migration authority.
- [x] Update short pointers and ownership mapping. Regenerate packaged resources with `uv run --locked python tools/package_resources.py` when an authoritative input changes; review the generated diff and run the existing resource drift test. Review the warning/override example for consequence, recorded choice, no repeat challenge and no false conformance claim.

## Task 3: Reference fixture and behavior evidence

**Files:** `examples/application_foundations/pyproject.toml`,
`examples/application_foundations/README.md`,
`examples/application_foundations/settings.example.json`,
`examples/application_foundations/src/example_foundations/{__init__,__main__,configuration,domain,application,cli}.py`,
`tests/test_application_foundations.py`, root `pyproject.toml`, root `uv.lock`,
`.pre-commit-config.yaml` and `tools/verify_distribution.py`.

**Interfaces and exact fixture contract:** Use the schema, module boundaries,
typed signatures and commands below. They are fixture implementation choices
within design edition 3, not a universal adopter schema or new starter API.

### Fixture schema and behavior

The invented application renders a greeting and can explicitly save the result.
The example is UTF-8 JSON:

```json
{
  "schema_version": 1,
  "message": "Hello example",
  "repeat": 1,
  "tags": ["demo"],
  "output_file": null,
  "credential_ref": null
}
```

Owned keys are exactly these six. Defaults are message `Hello example`, repeat
`1`, empty tags, no output and no credential. A file must contain integer
`schema_version: 1`; bool is not an integer here. Message is a nonempty string
up to 1024 characters, repeat is integer 1–3, tags are at most eight nonempty
strings of at most 64 characters each. No extension namespace is exposed by
this bounded fixture. Reject duplicate/unknown keys, malformed or nonfinite
JSON and files over 64 KiB before effects. Paths and credential references are
not interpolated. `output_file` is null or a nonempty space-free path; null
explicitly disables output, while empty is invalid. `credential_ref` is null or
the literal `env:EXAMPLE_FOUNDATIONS_TOKEN`; a selected reference requires a
nonempty injected token. The credential is a fixture boundary demonstration and
is never needed by domain rendering or persisted with results.

File selection is an explicit config argument, then
`EXAMPLE_FOUNDATIONS_CONFIG`, then `<config_root>/settings.json`. An empty
explicit/env selection fails, as does a missing, inaccessible or invalid selected
file. Only absence of the declared default permits defaults. The caller supplies
`config_root` and `invocation_base` explicitly; the CLI requires `--config-root`
to identify the default scope. Host/library callers use the same function with
their explicitly selected root. There is no HOME lookup or parent-directory walk.

Value precedence is defaults → selected file → environment → explicit overrides.
Supported value variables are `EXAMPLE_FOUNDATIONS_MESSAGE`,
`EXAMPLE_FOUNDATIONS_REPEAT`, `EXAMPLE_FOUNDATIONS_TAGS` (JSON string array), and
`EXAMPLE_FOUNDATIONS_OUTPUT_FILE`. Empty supplied values fail; unrelated names
are ignored. CLI flags are `--message`, `--repeat`, `--tags` (same JSON encoding),
`--output-file`, and `--no-output`; use suppressed argparse defaults so omitted
flags do not enter overrides. The two output flags are mutually exclusive.
Relative file-owned paths use the selected file's parent; env/API/CLI paths use
the invocation base captured once. Validate supplied and resolved paths and
symlink targets before content reads or effects. Optional output requires an
existing parent directory; no implicit directory creation occurs.

Render `message` on `repeat` lines, prefixing each line with the bracketed tags
when present, in supplied order. Emit one JSON object `{"text": "..."}` on
stdout; diagnostics go to stderr. `--help`/`--version` exit 0, invalid config or
usage exits 2, output failure exits 1. `--check-config` emits only redacted safe
values and winning-source labels and exits without application output effects.
No interactivity, reload, network service or automatic dotenv loading is added.

### Modules and typed interfaces

`configuration.py` owns JSON/environment parsing, validation, selection,
path resolution and credential injection; use stdlib dataclasses/TypedDict.
Its value types and function are:

```python
class Overrides(TypedDict, total=False):
    message: str
    repeat: int
    tags: tuple[str, ...]
    output_file: str | None

@dataclass(frozen=True)
class Settings:
    message: str
    repeat: int
    tags: tuple[str, ...]
    output_file: Path | None
    credential: str | None = field(repr=False, compare=False, default=None)

@dataclass(frozen=True)
class LoadedSettings:
    settings: Settings
    selected_file: Path | None
    sources: Mapping[str, str]

class ConfigurationError(ValueError):
    pass

def load_settings(
    *, config_path: str | Path | None, config_root: Path,
    invocation_base: Path, environ: Mapping[str, str], overrides: Overrides,
) -> LoadedSettings: ...

def safe_diagnostics(loaded: LoadedSettings) -> dict[str, object]: ...
def child_environment(
    environ: Mapping[str, str], *, forwarded: Sequence[str] = (),
) -> dict[str, str]: ...
```

Imports are `dataclass, field` from dataclasses, `Path` from pathlib,
`TypedDict` from typing and `Mapping, Sequence` from collections.abc. The
signatures define the planned API; ellipses here denote function bodies to be
implemented in the owning task, not omitted acceptance decisions. Sources use
`default`, `file`, `environment` and `explicit` labels; include only safe setting
names, with no credential value/reference in diagnostic values or exception
text. `child_environment` copies only explicitly named keys. Demonstrate default
token omission and deliberate token forwarding in tests; do not forward the
whole environment or print the resulting mapping.

`domain.py` defines the pure function
`render_message(message: str, repeat: int, tags: tuple[str, ...]) -> str`.
`application.py` defines
`run(settings: Settings, *, write_text: Callable[[Path, str], None]) -> str`,
which calls the pure function and invokes the injected writer only for a selected
output. It also owns the outer filesystem adapter
`atomic_write_text(path: Path, text: str) -> None`: write UTF-8 to a temporary
sibling, close, replace, and clean up on failure. The existing destination must
survive a reached `os.replace` failure. Reject a resolved output that equals the
selected settings file before application effects; test that settings bytes
survive. Configuration failures use `ConfigurationError` with safe actionable
messages. An absent optional default gives `selected_file=None`; an explicitly
missing selection raises instead.
`cli.py` defines `main(argv: Sequence[str] | None = None) -> int`, builds the
parser, captures launch context and environment once, translates failures with
safe messages, and wires the concrete writer. `__main__.py` calls `main`;
`__init__.py` exports `load_settings`, `Settings`, and `Overrides`. No module
performs reads or configuration during import.

### Root-owned verification and packaging

Create fixture package `example-foundations` at version `0.1.0`, with
`requires-python = ">=3.14,<3.15"`, empty runtime dependencies, a pinned
`uv_build` backend matching the root's verified backend, src package
`example_foundations`, and `example-foundations = "example_foundations.cli:main"`.
The fixture pyproject contains package/build metadata only. Do not create a
fixture lock, `.venv`, interpreter override or tool table.

Install the example as a local editable **development** dependency under the
root's existing dev group, with its root `[tool.uv.sources]` entry pointing to
`examples/application_foundations`. Regenerate the root lock using uv. Add
`examples` to root ty source inclusion; editable installation supplies import
resolution. Extend the existing unittest hook's file selector to `examples/`;
Ruff's existing Python hooks already select those source files. Keep tests in
`tests/test_application_foundations.py`, where normal root unittest discovery
collects them. No wrapper that silently accepts zero tests is needed.

Use a root source declaration:

```toml
[tool.uv.sources]
example-foundations = { path = "examples/application_foundations", editable = true }
```

Add `"example-foundations==0.1.0"` to the existing root dev group, preserving
its other entries and the empty runtime dependency list. This local dev dependency
is the reference package under test, not a new external application framework.

Add `examples/application_foundations/**` to the root sdist's source inputs,
excluding generated build output and environments. The starter wheel keeps its
existing six resource inputs; the example is independently built from the
source distribution rather than bundled as a runtime package in that wheel.
Extend `tools/verify_distribution.py` to require the fixture metadata, source,
README and sample in the root sdist, extract into a temporary directory and
build the fixture from that extracted source, then install only its wheel with
`uv pip install --python <temporary-env-python> --no-deps <fixture-wheel>`.
Create the temporary environment via `uv venv --python sys.executable <env>`
from the root verification process so it uses the actual pinned interpreter.
Run the installed fixture outside both checkouts with `PYTHONPATH` unset and
without a source pyproject. Verify version, CLI/library behavior, redaction,
external-settings preservation across reinstall and a representative invalid
selection. Do not install the editable source into the installed probe.

Owning commands, run from the repository root after metadata reconciliation:

```bash
uv lock
uv sync --locked --all-groups
uv run --locked python -m unittest discover -s tests -p 'test_application_foundations.py' -v
uv run --locked ruff check examples/application_foundations tests/test_application_foundations.py
uv run --locked ruff format --check examples/application_foundations tests/test_application_foundations.py
uv run --locked ty check examples/application_foundations/src tests/test_application_foundations.py
uv build --no-sources --project examples/application_foundations --out-dir /tmp/gz-foundations-build
```

Use a fresh task-owned artifact directory if that final output directory already
exists; do not delete someone else's artifacts. The integrated root commands in
Task 5 run all owning tests and the extracted-source installed probe. Routine CI
already invokes those commands, so no fifth hook or separate routine job is added.

- [x] Build one small packaged CLI/library fixture, with no new runtime dependency. Select an explicit path, then documented config-path environment variable, then one declared default. Resolve relative file paths against the settings file and launch/API paths against the documented invocation base. Support simulated project/user/service/host contexts through explicit roots.
- [x] Add focused unittest cases proving defaults → one JSON file → documented environment → explicit CLI/API overrides; omitted flags preserve lower layers, empty differs from absent, lists/scalars replace, and diagnostics identify winning sources without secrets.
- [x] Exercise duplicate keys, malformed JSON, nonfinite numbers, wrong/unknown keys, unsupported schema, size/type bounds and an absent or invalid explicitly selected file. Assert errors precede application effects and never fall through to another file. This fixture has no extension namespace.
- [x] Exercise the actual output adapter's failed replacement with prior bytes intact and temporary sibling cleanup. At the application seam, inject a writer raising `OSError` and require CLI exit 1, parseable/empty result output as specified, safe stderr and no secret sentinel. Exercise the pre-read guard from Task 1 on selected settings and output paths, plus its deliberate-read positive control.
- [x] Exercise two isolated roots, a different working directory, an installed fixture without source `pyproject.toml`, external settings surviving code replacement, and explicit service/host selection independent of HOME. Verify spaced supplied/resolved/symlink paths reject before effects and input text containing spaces remains intact.
- [x] Use sentinel secrets in isolated tests to prove stdout, stderr, logs, examples and distribution do not contain them. Test deliberate child environment forwarding. Exercise a domain decision with injected values/fakes and an adapter failure at its owning seam; demonstrate boundary-only construction.
- [x] Run the fixture's documented locked unittest and isolated build/install commands. Record actual platform and interpreter, failure controls, results and unverified host/platform claims; do not infer TUI, web, desktop, simulator or multi-account qualification.

## Task 4: Crosswalk and integration

**Files:** `docs/engineering/application-foundations.md`, `docs/structure.md`, `ROADMAP.md`, `CHANGELOG.md`, dated evidence and handoff.

- [x] Map all 108 candidate dispositions and 15 naming topics to the actual delivered guidance or existing authority. Preserve the distinction between GZKit's commissioned, landed and conformant behavior and the pinned upstream audit's demonstrated limits. Do not copy a portable skill or claim an upstream improvement shipped.
- [x] Record the starter inventory, warnings/override example, fixture and path-test evidence, deferred scanner evaluation, known native/platform limits and cognitive deferral. Reconcile 0.10.0 → 0.11.0 scope and mirrors under `docs/versioning.md`; do not claim release acceptance or publication.
- [x] Compare completed work to every acceptance item in design edition 3. Record missing evidence as UNKNOWN and repair actual gaps before claiming implementation acceptance. Review the complete diff including resource copies and changed consumers.

## Task 5: Coherent integration verification

**Files:** evidence and handoff updates only after checks.

- [x] Run `uv run --locked pre-commit run --all-files`, `uv run --locked gz-starter validate`, `uv build --no-sources`, and `uv run --locked python tools/verify_distribution.py`. Run `uv sync --locked --all-groups` if environment state requires it. If analyzer code changed, also run `uv run --locked --group hygiene python -m unittest discover -s tools/engineering -p 'test_*.py' -v`.
- [x] Verify fixture distribution and examples contain no sentinel; inspect lock/catalog/resource consistency and changed-file diff. Record actual commands, interpreter/tool provenance and outcomes. Re-run affected checks only if relevant inputs change.
- [x] Report implementation evidence separately from release preparation. Release preparation needs its own authorized complete maintenance pass, scanner evaluation and applicable deeper evidence; no tag or publication is implied.
