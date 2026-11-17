# Application Foundations Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan on `main`. Checkboxes track deliverables; follow the repository's risk-based verification policy.

**Goal:** Deliver the approved 0.11.0 application-foundations guidance, a bounded reference fixture, and the selected starter path behavior with observable evidence.

**Architecture:** Keep configuration and effects at a project-owned application boundary. The starter publishes guidance and a small invented example, not a shared loader or framework; its existing helper retains its public seams. Respect explicit informed departures and preserve existing mandatory policy.

**Tech Stack:** Python 3.14, uv, standard library, unittest, existing Ruff/ty/pre-commit configuration.

**Spec:** [Design edition 3](../specs/2026-11-16-application-foundations-design.md), SHA-256 `54b2a94c5be72dfa93abb65101db384f3c2dad61c720e53b095b6bdc191367a6`; maintainer approval recorded in the [handoff](../../handoffs/2026-11-16-application-foundations-design-handoff.md).

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
- `examples/application_foundations/`: invented, independently packaged CLI/library fixture and its unittest suite. This is illustrative and is not a starter runtime dependency.
- `ROADMAP.md`, `CHANGELOG.md`, existing handoff and a dated evidence record: reconcile scope, observed evidence and unresolved limits. Regenerate packaged copies through `tools/package_resources.py` when authoritative resources change.

## Task 1: Starter path contract

**Files:** `src/skills_first_starter/cli.py`, affected native path consumers, `tests/test_starter.py`, `tests/test_native_hosts.py`, `tests/test_native_launch.py`.

**Interfaces:** Preserve `configure`, `localize`, `status`, `backport`, `check_path` and `main` public signatures and existing error/exit conventions. Reuse a single internal path validator if feasible; it must validate original and resolved paths without reading target contents.

- [ ] Inventory every path accepted or derived by the API and CLI, installed resource paths, symlink handling, process paths and existing preflight/write ordering. Record which entry points can cause effects and any platform limitation.
- [ ] Add public-seam unittest cases for API and CLI: supplied spaced project path, a space-free symlink resolving to a spaced target, a spaced parent or managed child, and a valid space-free control. For each rejected write, assert existing sentinel bytes are unchanged and missing parents remain absent. Include a file whose *contents* contain spaces and assert those bytes survive.
- [ ] Run the focused tests and confirm the rejection regressions fail for the intended reason. Implement validation before target content reads or mutation, including all planned targets before the first write. Return an actionable `AdoptionError`/CLI failure without changing the existing API shape.
- [ ] Run `uv run --locked python -m unittest discover -s tests -p 'test_starter.py' -v` and the affected native-host/launch test modules. Inspect behavior for resource paths and unsupported platforms; record evidence rather than generalizing.

## Task 2: Guidance and migration

**Files:** configuration, naming/layout, application foundations and adopter pointers listed above.

**Interfaces:** The configuration contract is the authoritative runtime-settings guidance; `pyproject.toml` remains authoritative for packaging/dependencies/tool configuration. Existing `.gz-skills/settings.json` remains distinct.

- [ ] After ADR approval, replace the current either-TOML-or-JSON runtime recommendation with the approved ownership, scope and location rules, file selection and value precedence, validation, secret handling, explicit host/library responsibility and no-spaces contract. Explain explicit invalid-selection failure and configuration preservation across replacement.
- [ ] Reconcile each of the 15 numbered naming/layout sections against edition 3, including web application classification and paths. Remove claims that the deferred Ruff/ty patch is active. Preserve compatibility names and external schemas.
- [ ] Publish the remaining foundations in a focused engineering page: errors, logging/output, paths, persistence/recovery, external calls, trust, data semantics, operations, privacy and interfaces. Give applicability and observable evidence; distinguish recommendations, mandatory existing requirements and informed overrides.
- [ ] Inventory the starter's actual configuration and effect boundaries; document its applicable choices or explicitly authorized departures without creating an unused settings file. Update adopter migration and update-skill guidance to inventory existing contracts, preview, preserve data and obtain migration authority.
- [ ] Update short pointers and ownership mapping. Regenerate packaged resources with `uv run --locked python tools/package_resources.py` when an authoritative input changes; review the generated diff and run the existing resource drift test. Review the warning/override example for consequence, recorded choice, no repeat challenge and no false conformance claim.

## Task 3: Reference fixture and behavior evidence

**Files:** `examples/application_foundations/pyproject.toml`, `examples/application_foundations/src/example_foundations/`, `examples/application_foundations/tests/`, fixture README and invented settings.

**Interfaces:** Define `load_settings(config_path, environ, overrides)` at the fixture boundary to return validated settings and safe source diagnostics; domain functions receive resolved values and injected dependencies. CLI delegates to the same boundary. Document exact concrete signatures in the fixture README as implemented; do not expose these as a starter API.

- [ ] Build one small packaged CLI/library fixture, with no new runtime dependency. Select an explicit path, then documented config-path environment variable, then one declared default. Resolve relative file paths against the settings file and launch/API paths against the documented invocation base. Support simulated project/user/service/host contexts through explicit roots.
- [ ] Add focused unittest cases proving defaults → one JSON file → documented environment → explicit CLI/API overrides; omitted flags preserve lower layers, empty differs from absent, lists/scalars replace, and diagnostics identify winning sources without secrets.
- [ ] Exercise duplicate keys, malformed JSON, nonfinite numbers, wrong/unknown keys, unsupported schema and an absent or invalid explicitly selected file. Assert errors precede application effects and never fall through to another file. Cover a deliberate extension namespace if the fixture exposes one.
- [ ] Exercise two isolated roots, a different working directory, an installed fixture without source `pyproject.toml`, external settings surviving code replacement, and explicit service/host selection independent of HOME. Verify spaced supplied/resolved/symlink paths reject before effects and input text containing spaces remains intact.
- [ ] Use sentinel secrets in isolated tests to prove stdout, stderr, logs, examples and distribution do not contain them. Test deliberate child environment forwarding. Exercise a domain decision with injected values/fakes and an adapter failure at its owning seam; demonstrate boundary-only construction.
- [ ] Run the fixture's documented locked unittest and isolated build/install commands. Record actual platform and interpreter, failure controls, results and unverified host/platform claims; do not infer TUI, web, desktop, simulator or multi-account qualification.

## Task 4: Crosswalk and integration

**Files:** `docs/engineering/application-foundations.md`, `docs/structure.md`, `ROADMAP.md`, `CHANGELOG.md`, dated evidence and handoff.

- [ ] Map all 108 candidate dispositions and 15 naming topics to the actual delivered guidance or existing authority. Preserve the distinction between GZKit's commissioned, landed and conformant behavior and the pinned upstream audit's demonstrated limits. Do not copy a portable skill or claim an upstream improvement shipped.
- [ ] Record the starter inventory, warnings/override example, fixture and path-test evidence, deferred scanner evaluation, known native/platform limits and cognitive deferral. Reconcile 0.10.0 → 0.11.0 scope and mirrors under `docs/versioning.md`; do not claim release acceptance or publication.
- [ ] Compare completed work to every acceptance item in design edition 3. Record missing evidence as UNKNOWN and repair actual gaps before claiming implementation acceptance. Review the complete diff including resource copies and changed consumers.

## Task 5: Coherent integration verification

**Files:** evidence and handoff updates only after checks.

- [ ] Run `uv run --locked pre-commit run --all-files`, `uv run --locked gz-starter validate`, `uv build --no-sources`, and `uv run --locked python tools/verify_distribution.py`. Run `uv sync --locked --all-groups` if environment state requires it. If analyzer code changed, also run `uv run --locked --group hygiene python -m unittest discover -s tools/engineering -p 'test_*.py' -v`.
- [ ] Verify fixture distribution and examples contain no sentinel; inspect lock/catalog/resource consistency and changed-file diff. Record actual commands, interpreter/tool provenance and outcomes. Re-run affected checks only if relevant inputs change.
- [ ] Report implementation evidence separately from release preparation. Release preparation needs its own authorized complete maintenance pass, scanner evaluation and applicable deeper evidence; no tag or publication is implied.
