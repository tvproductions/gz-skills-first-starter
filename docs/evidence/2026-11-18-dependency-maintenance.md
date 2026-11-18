# Dependency maintenance — November 18, 2026

Mode: **update**, explicitly requested through `gzs-update-dependencies` 0.5.0
from selected gz-skills 0.13.0. Started on clean main at
`7dea4b5ad2104b424dfc0f471090182f195f3812`, the rollback reference. The preceding
Git sync was complete; this invocation authorizes source/environment migration,
not another commit/push, tag, release or native installation/activation.

## Scope and version decision

Published baseline **0.11.1**, immutable source
`041c1989406c1b9c4978042661c2dd38ff1db160`, remains the latest nondraft stable
[GitHub release](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.1).
Reuse pending **0.11.2 / patch** and its
[bounded maintenance scope](../../ROADMAP.md#selected-0112-scope--post-release-dependency-maintenance-november-17-2026).
These transitive fixes restore the existing latest-stable commitment; no new
public capability, requirement or architectural choice is introduced. The
bootstrap-verification design/ADR remain drafts with separate approval gates and
proposed 0.12.0; do not infer approval or implementation from this maintenance.

Inventory includes both independent Python pyprojects/locks/environments,
runtime pins, root/example build backends, uv, all dev/hygiene/transitive registry
packages, pre-commit hooks, CI execution/Actions pins, components, both catalogs
and Codex/Claude/OpenCode source/activation configuration. The root owns the
example's tool settings and environment. There is no additional language,
container, vendored binary or adopted-template record to migrate: this is the
canonical starter, not its own adopter. Cohesion remains adopter-owned; the
shared cognitive engine is undelivered. No profile is inferred or created.

## Current stable migration and compatibility

The [machine-readable receipt](2026-11-18-dependencies.json) records every one
of **77 registry projects**, selected before/after versions, official evidence,
unchanged component/Action SHAs, candidate hashes and security/control results.

| Package | Before | Selected/latest | Consumers |
| --- | --- | --- | --- |
| [filelock](https://github.com/tox-dev/filelock/releases/tag/4.2.12) | 4.2.11 | 4.2.12 | both transitive tool graphs |
| [platformdirs](https://github.com/tox-dev/platformdirs/releases/tag/4.14.7) | 4.14.5 | 4.14.7 | both transitive tool graphs |
| [python-discovery](https://github.com/tox-dev/python-discovery/releases/tag/1.9.6) | 1.9.5 | 1.9.6 | virtualenv in both environments |
| [virtualenv](https://github.com/pypa/virtualenv/releases/tag/21.15.8) | 21.15.7 | 21.15.8 | both pre-commit/tool environments |

Official notes describe sticky-directory lock ownership protection, directory
parsing/root-path fixes (including intervening
[platformdirs 4.14.6](https://github.com/tox-dev/platformdirs/releases/tag/4.14.6)),
interpreter discovery fixes and environment seeding/activation fixes. All support
the selected Python families. Accept the fixes without changing project rules or
consumer APIs. The new filelock restriction rejects another account's lock in a
sticky directory; project-owned caches and disposable owned directories need no
exception. Actual controls below establish the bounded macOS workflow, not every
upstream fix or platform.

Retain current uv/uv_build **0.13.9**, Ruff **0.17.5**, ty **0.0.105**,
pre-commit **4.7.0** and all other dev/hygiene selections. Preserve uv minimum-only
**>=0.13.5**, exact package/backend pins and all four routine hooks. No newer
stable tooling family was omitted in favor of an old constraint. The owning uv
resolver updates both locks; no lock is edited manually and no package/group,
source or dependency-edge change is introduced beyond the four versions/artifacts.

[Python.org](https://www.python.org/downloads/) confirms current approved patches
**3.14.10 / 3.12.16**; upstream 3.15.2 stays outside the deliberate N-1/embedded
families. Preserve both pins/CI selections. Review the
[versioned 3.14 opportunity guide](https://docs.python.org/3.14/whatsnew/3.14.html)
and existing project analysis: the helper has no new concurrency, compression,
template-processing or annotation-introspection need. Defer those APIs; Path
copy/move does not replace the exclusive-write/preservation contract. No source
modernization is justified by these transitive updates; 3.14-only APIs remain
unavailable to the independent 3.12 host-reference code.

## Observed verification

Actual execution: macOS ARM64, **uv 0.13.9**, managed **CPython 3.14.10** and
independent **3.12.16**. Temporary compatibility probes and audit caches stay
outside the repository; no reusable updater or maintenance hook is added.

- Both baselines: `uv lock --upgrade`, `uv sync --locked --all-groups`, repeat
  `uv lock --upgrade`, `uv lock --check`, and
  `uv pip list --outdated --format json` pass. Second resolutions are byte-stable;
  both outdated results are `[]`. All selected registry versions match current
  non-yanked stable releases; direct declarations remain unchanged.
- `uv run --locked pre-commit run --all-files --verbose`: all four hooks pass,
  including **95 unittest tests**. No assertions, thresholds or selections change.
- On each exact interpreter, disposable controls pass for independent file-lock
  contention/release, absolute cache-path selection without user-directory
  creation, virtualenv interpreter discovery, offline seeded creation, child
  exact-version execution, seeded pip and bash/zsh activation with a pydoc alias.
  Seeded pip reports 26.3. These controls exercise actual changed packages;
  no mock or installation metadata is used as compatibility proof.
- Independent host reference:
  `uv run --locked python ../../tools/verify_xplane_baseline.py` passes its
  positive/negative Ruff, ty and unittest controls on actual 3.12.16.
- Each owning environment's pinned pip-audit audits its separate
  `uv export --locked --all-groups --no-emit-local` hash-bearing requirements,
  using `--require-hashes --no-deps --disable-pip` with task-local caches.
  **75 root / 75 host registry packages, zero known vulnerabilities, zero skips.**
  Generic redundant-no-deps/hashing advice is emitted; exports require hashes,
  no second resolver runs, and structured outcomes cover every registry package.
- `uv run --locked gz-starter validate`, `uv run --locked gz-starter version`,
  `uv build --no-sources`, and
  `uv run --locked python tools/verify_distribution.py` pass: both catalogs,
  wheel resources, source-independent sdist-to-wheel build, isolated installed
  CLI and extracted-source example/typing/preservation controls are verified.
  None of the six authoritative wheel-resource inputs changed, so resource
  regeneration is unnecessary; the tests/archive checks prove they still match.
- Final review verifies **20 candidate input hashes**, all **four static version
  mirrors** plus actual CLI 0.11.2, and **114 local Markdown references** across
  the five changed/new Markdown files. Semantic lock comparison confirms exactly
  four package/version/artifact changes per baseline, with all package sets,
  dependency edges, groups, sources and lock contract unchanged. Final receipt
  prose reuses these unchanged-input passes under the verification policy.

## Native state, remaining limits and disposition

Read-only native Codex **0.170.0** inventory now reports installed/enabled
SP **7.0.2** and gz-skills **0.13.0**, plus installed/disabled Backplane **0.3.0**,
at the selected exact SHAs. This supersedes November 17's observed installed
revision drift for this host; this pass performed no installation or activation.
Both catalogs and all native source/activation/duplicate-source overrides are
unchanged. Actual invocation of this maintenance skill comes from the 0.13.0
cache. Broader fresh-session/desktop/other-host discovery and combined-stack
readiness remain separate, unverified dimensions.
The native CLI warns that its PATH-alias setup is sandbox-restricted; the
read-only inventory succeeds, and no installation or settings repair is attempted.

Retain cognitive **DEFERRED / measurement UNKNOWN**, ceiling 15, adopter-owned
cohesion and actual embedded XPPython3/Windows/other-host limits. No analyzer
selection or scoring contract changes; unchanged deeper analyses retain only
their prior bounded evidence under the verification policy. This is maintenance,
not strict release/adoption acceptance. Backplane stays disabled.

Version mirrors remain 0.11.2; no per-task bump or publication is warranted.
Source/environment migration and all applicable local maintenance checks are
complete. Intended worktree scope: two updated locks, four existing documentation
files and these two new dated receipts; no unrelated changes are included.
Hosted CI for the modified candidate is UNKNOWN until a separately requested
sync; the base commit's green CI does not verify these changed locks. Release
preparation requires fresh actual-candidate evidence and its remaining gates.
