# Post-release dependency maintenance — November 17, 2026

Mode: **update**, explicitly invoked through `gzs-update-dependencies` under the
starter's completed-migration binding. Started from clean main
`0667b3347bfc98cd26179fdc41f820ce67d2a2d2`, the rollback reference. This source
and environment maintenance does not authorize commit/push, publication, native
installation/activation or companion/adopter changes.

## Scope and version decision

Published baseline **0.11.1** at immutable source
`041c1989406c1b9c4978042661c2dd38ff1db160` -> pending **0.11.2 / patch**.
The governing correction restores the existing latest-stable tooling commitment
after new same-day releases. Reuse ADR-0001 edition 1: component sources and ADR
procedure/bindings are unchanged, so its source-bound qualification retains only
the previously observed scope. No new ADR or major PRD applies. The
[roadmap scope](../../ROADMAP.md#selected-0112-scope--post-release-dependency-maintenance-november-17-2026)
excludes all unrelated backlog work. Published tags and earlier evidence remain
immutable; these development version mirrors do not establish publication.

Inventory: root and independent X-Plane pyprojects/locks, the root-managed
example's build backend, both runtime pins/environments, uv, every dev/hygiene
and transitive registry dependency, hooks, CI Actions/execution pins,
bundle/catalogs and Codex/Claude/OpenCode source/activation bindings. There is
no other language ecosystem, container or repository-owned binary. The example
has no runtime dependencies or independent environment/lock. Cohesion remains
adopter-owned; the shared cognitive engine is not delivered. Preserve retired
Radon/Xenon and the four routine hooks.

## Live selections and compatibility

The [registry receipt](2026-11-17-post-release-dependencies.json) records all
77 registry projects, before/after selections, source URLs, Python requirements,
yank status and candidate hashes. Official release queries independently retain
SP 7.0.2, gz-skills 0.13.0, disabled Backplane 0.3.0, checkout 7.0.1 and setup-uv
10.3.3 at their existing exact SHAs. Both catalogs and native bindings remain
unchanged apart from the bundle's independent template version.

| Tool | Before | Selected/latest | Consumers |
| --- | --- | --- | --- |
| [uv](https://github.com/astral-sh/uv/releases/tag/0.13.9) | 0.13.8 | 0.13.9 | resolver, locked execution, CI selection |
| [uv_build](https://pypi.org/project/uv-build/0.13.9/) | 0.13.8 | 0.13.9 | root/example isolated builds; host-reference dev group |
| [ty](https://github.com/astral-sh/ty/releases/tag/0.0.105) | 0.0.104 | 0.0.105 | both dev groups and locked type-check consumers |

uv 0.13.9 fixes wheel package-identity validation and equivalent lock-marker
handling and factors repeated markers. Its Rust floor concerns building uv from
source; this pass uses the published macOS ARM64 binary. Defer new preview-only
venv redirect and HTTP/2 keepalive features: neither has a project consumer.
Keep minimum-only caller compatibility >=0.13.5. Execute through
`uv tool run --from uv==0.13.9 uv ...`; nested hook/build commands resolve that
same binary, without changing a global executable or user defaults.

ty 0.0.105 splits missing module members, invalid dataclass post-init signatures
and single-constraint TypeVars into more precise diagnostics. No active rule
override or diagnostic-name assertion relies on the old classifications. Keep
all defaults/thresholds; verify the actual package and installed typed example.
The unapplied naming-rule proposal explicitly records its older ty inventory;
it remains deferred and requires refresh before any future application.

[Python.org](https://www.python.org/downloads/) retains current approved patches
3.14.10 and host-reference 3.12.16. Latest stable 3.15.2 is outside the approved
N-1/embedded-host families. Keep both pins and CI Python selections unchanged.
Review the [versioned 3.14 opportunity guide](https://docs.python.org/3.14/whatsnew/3.14.html)
and existing project opportunity analysis: no runtime consumer needs new
concurrency, compression, template or annotation-introspection machinery.
Path.copy/move does not establish the helper's exclusive-write/preservation
contract. Retain existing behavior; defer those APIs rather than introducing
unrelated modernization or requiring them in the 3.12 host reference.

## Verification and remaining limits

Observed on macOS ARM64 with managed CPython **3.14.10** / **3.12.16** and
uv **0.13.9** (`6b2d39dcc`); nested commands resolve that same cached executable.
The machine's unrelated uv 0.13.8 remains unchanged and supported.

- Both projects: `uv lock --upgrade`, `uv sync --locked --all-groups`, a second
  `uv lock --upgrade`, `uv lock --check`, and `uv pip list --outdated --format json`
  pass. Second resolutions preserve both lock hashes exactly; outdated results
  are `[]`. Semantic lock review finds only ty/root project-version changes in
  the root and ty/backend/owner metadata changes in the host-reference lock.
  No package set, source, group membership or top-level lock contract changes.
- `uv run --locked pre-commit run --all-files`: all four hooks pass. Normal
  pre-commit hook installation is present. Ruff and pre-commit remain 0.17.5 /
  4.7.0; ty is 0.0.105. Representative example Ruff settings still resolve from
  root pyproject. No lint rule, type-check default or numeric threshold is relaxed.
- `uv run --locked gz-starter validate`: **0.11.2**, unchanged exact component
  SHAs and both catalogs valid. `tools/package_resources.py` refreshes the bundle
  resource; routine tests and archive verification detect resource/version drift.
- `uv build --no-sources` and `uv run --locked python tools/verify_distribution.py`:
  source-independent sdist-to-wheel build, archive/resource inventory, isolated
  installed CLI, extracted-source example rebuild, installed positive/negative
  typing and settings preservation all pass with uv_build 0.13.9 / ty 0.0.105.
- From `baselines/xplane`, `uv run --locked python ../../tools/verify_xplane_baseline.py`:
  positive/negative Ruff, ty and unittest controls pass on actual Python 3.12.16.
  This is standalone tooling evidence, not simulator/XPPython3 execution proof.
- Both exact-lock hash-bearing `uv export --locked --all-groups --no-emit-local`
  requirements are audited by each owning environment's pinned pip-audit with
  `--require-hashes --no-deps --disable-pip` and separate task-local caches.
  **75 root / 75 host-reference registry dependencies, zero known vulnerabilities,
  zero skipped packages.** pip-audit emits redundant-no-deps/generic hashing
  advice; hashes are required and every registry dependency has a structured
  outcome. Local distributions are verified by source/installed checks.

The first host audit exposed pre-existing executable shebangs pointing to the
obsolete pre-rename folder. Module inspection proved pip-audit was installed in
the correct 3.12 environment; its wrapper referenced a missing interpreter.
`uv sync --locked --all-groups --reinstall` in that independent environment
regenerated wrappers without deleting the environment or changing its lock.
The real pip-audit command and standalone controls then passed; final inspection
finds no missing shebang interpreter. Other pre-existing unsynced host packages
were reconciled to the already-selected lock by exact sync.

### Native source selection versus installation

Read-only `codex plugin list --marketplace skills-first-starter --json` on
Codex **0.169.0** observes installed SP **7.0.2** at the selected SHA, enabled
gz-skills **0.11.0** at `62622aee80ce27d4a39efe3554a583b844f38876`, and disabled
Backplane **0.2.0** at `0b18e34e65379e729d8fece97151a1bb8604b461`.
This session's invoked skill also comes from the 0.11.0 cache. Those latter two
installed versions differ from current repository selections **0.13.0 / 0.3.0**.
The native CLI advertises no project-scoped installed-version updater; marketplace
refresh is not installed-revision proof, and `plugin add` is prohibited as a
scope-preserving update substitute. Preserve user settings and existing caches.
**Native installation alignment and fresh-session discovery remain unverified;
the full installed stack cannot be called current.** No cache is edited directly
and no installation/activation is attempted. Revisit with an evidenced native
project-scoped update/resolution operation; the maintainer owns that follow-up.

### Acceptance mapping and closeout

Reuse unchanged [Astral acceptance](../engineering/astral-acceptance.md) evidence
from the source-bound 0.11.0/0.11.1 records only for unaffected rows:

| Rows | Actual maintenance result |
| --- | --- |
| A01 | PASS: clean starting SHA, source/environment scope, rollback and version decision above. |
| A02–A03 | PASS: existing src layouts and declared pure-Python backend preserved; new backend builds and clean installs verified. |
| A04 | PASS for affected configuration: root settings own the example; independent host-reference settings remain separate; declarations/hooks/default rules preserved. |
| A05–A08 | PASS: actual pinned interpreters, official latest targets, stable locks, exact all-group sync, current tool provenance and owning controls. |
| A09 | Local hooks PASS; hosted CI for this uncommitted candidate UNKNOWN. Prior commit's CI is not candidate proof. |
| A10–A12 | PASS: reviewed semantic lock/source intent, no runtime dependencies added, source-independent artifacts and clean installed behavior. |
| A13 | PASS for the existing example's py.typed and installed typing controls; no new library support claim. |
| A14–A16 | No new workspace/private/native-deployment trigger; retain earlier applicability and actual embedded-host UNKNOWN. |
| A17 | PASS for this pass's hash-required audit exports and pinned temporary uv execution; uv.lock remains authoritative. |
| A18 | CONDITIONAL: cognitive DEFERRED / measurement UNKNOWN, ceiling 15; cohesion adopter-owned; native/embedded/platform gaps retained. |

Completed: requested repository source/environment migration and full applicable
local verification. Version mirrors (bundle, pyproject, root lock, packaged bundle
and runtime output) agree on **0.11.2**; baseline **0.11.1 -> 0.11.2 / patch**
matches the bounded roadmap and changelog. No included source migration remains.
Acceptance is conditional, never full strict engineering/native-stack acceptance.
Final diff/evidence review resolves all **202 local Markdown references** across
the ten changed Markdown files, verifies all **20 candidate input hashes** and
finds no whitespace errors. Eighteen tracked paths plus the two new evidence
files are the intended uncommitted scope. Final evidence/pointer wording reuses
the passed gates on unchanged owning implementation/tool inputs under the
verification policy.
Unchanged Lizard/cognitive consumers and deeper analyses retain same-day bounded
evidence; no scoring contract changes or redundant analyzer requalification.
Release preparation must refresh candidate evidence and run remaining applicable
release checks. This uncommitted pass has no exact-candidate hosted CI, tag or
release publication; those require their own authorization and evidence.
