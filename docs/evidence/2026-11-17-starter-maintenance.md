# Starter dependency maintenance — November 17, 2026

Mode: **update**, explicitly invoked through `gzs-update-dependencies` under
the repository's completed-migration binding. Started from clean main
`21406c4e9a629f07763ca96e9fa2476e1be9fb72`, the rollback reference. Work remains
in the checkout for review; this maintenance request does not publish a release
or activate plugins. Reuse the valid pending **0.11.0 / minor** target over
published **0.10.0**, governed by the existing application-foundations scope.
No additional bump, design approval or ADR approval follows from maintenance.

## Inventory and official selections

Includes both independent pyprojects and locks, ordinary 3.14 and host-reference
3.12 runtime pins, uv/backend, all dev/hygiene and transitive dependencies,
local hooks, CI execution pins/actions, bundle/catalogs and native project
bindings. No other language manifest, container or repository-owned binary was
found. Existing mandatory tool selection overrides upstream generic profile
defaults; retired Radon/Xenon remain retired. Cohesion remains adopter-owned;
the undelivered cognitive engine remains DEFERRED / measurement UNKNOWN.
Native manager/cache updates, user settings, real adopters and companion source
changes are outside this pass. The starter is not its own template adopter.

The [registry receipt](2026-11-17-dependency-recheck.json) records all **76**
distinct PyPI projects, before/after selections, latest non-yanked stable releases
across families, official registry URLs, Python requirements and candidate
manifest/lock/binding hashes. Five updates were resolved in **both** projects:

| Dependency | Previous | Selected/latest | Consumer |
| --- | --- | --- | --- |
| Lizard | 1.26.0 | 1.26.1 | on-demand complexity checker |
| CacheControl | 0.14.4 | 0.15.0 | pip-audit HTTP cache |
| filelock | 4.2.10 | 4.2.11 | tooling/cache synchronization |
| SQLAlchemy | 2.1.8 | 2.1.9 | Cosmic Ray persistence dependency |
| virtualenv | 21.15.6 | 21.15.7 | pre-commit environment dependency |

All other registry selections already match latest stable; none is yanked.
Actual resolver **uv 0.13.8** and backend **uv_build 0.13.8** remain current.
Preserve minimum-only uv **>=0.13.5**, exact locks and independent environments.
[Python.org](https://www.python.org/downloads/) and uv's managed inventory agree
on **3.14.10**, **3.12.16** and latest stable **3.15.2**. Retain the approved
3.14 N-1 and 3.12 embedded-host families rather than adopting 3.15; no stale
patch exception is needed. Actual verification runs on managed CPython 3.14.10
and 3.12.16, macOS ARM64. The latter is a tooling reference, not simulator proof.

Official GitHub latest-release queries and dereferenced tag objects retain:

| Component | Latest stable | Immutable source |
| --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers/releases/tag/v7.0.2) | 7.0.2 | `22f0b463e7a5e579904dd6211a520321035526f7` |
| [gz-skills](https://github.com/tvproductions/gz-skills/releases/tag/v0.13.0) | 0.13.0 | `0bdab63fc503c6b36e2dd487932689b4e555e41a` |
| [Backplane](https://github.com/tvproductions/superpowers-backplane/releases/tag/v0.3.0) | 0.3.0; disabled/deferred | `39fbe3065c16ac119c4c10a3c2428fda39d57e61` |
| [checkout](https://github.com/actions/checkout/releases/tag/v7.0.1) | 7.0.1 | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| [setup-uv](https://github.com/astral-sh/setup-uv/releases/tag/v10.3.3) | 10.3.3 | `68559e99cc807c1eb7e9238fd43a15bba460eec2` |

Catalog validation confirms both catalogs agree with the unchanged bundle.
Codex/Claude immutable catalog refs and OpenCode component sources stay intact,
as do enablement and inherited-duplicate suppression. This pass adds no native
discovery/model or combined-stack qualification claim.

## Compatibility and qualification

Reviewed the [Lizard patch comparison](https://github.com/terryyin/lizard/compare/1.26.0...1.26.1),
including Python prefixed-string/NLOC fixes, and
[CacheControl 0.15.0 notes](https://github.com/psf/cachecontrol/releases/tag/v0.15.0).
The latter corrects expiration, headers, cached response handling and resource
cleanup. Both real pip-audit consumers complete with the new cache library.
Resolution accepts the other patch updates under existing consumer constraints;
no dependency override or compatibility downgrade was required.

Lizard 1.26.0 and 1.26.1 were run in isolated temporary environments on the same
**24 Python files / 220 functions**. Names, start/end locations and cyclomatic
scores match exactly; the receipt records the corpus result hash. All **29**
checker CLI/counting/portability/cognitive-qualification regressions pass on
3.14.10, preserving boundary 20/21, aggregation, discovery and fail-closed errors.
Update the exact-version guard and current engineering guidance to 1.26.1.
Retain `lizard-functions-v1`: these observations show no scoring-contract change.
This does not qualify Lizard cognitive scoring or replace the selected deferred
shared cognitive engine.

Python 3.14 opportunity review reuses the versioned
[what's-new/porting guide](https://docs.python.org/3.14/whatsnew/3.14.html).
No new runtime consumer justifies template strings, interpreter pools, Zstandard,
annotation changes or replacing the helper's exclusive-write/recovery semantics
with Path.copy/move. Retain existing behavior and defer those APIs; they also
cannot become requirements of the 3.12 host-reference environment.

## Observed verification and limits

- In each owning project: `uv lock --upgrade`, `uv sync --locked --all-groups`,
  `uv lock --check`, and `uv pip list --outdated --format json` pass. Outdated
  results are `[]`; a second upgrade resolution leaves candidate hashes unchanged.
- `uv run --locked pre-commit run --all-files`: all four hooks pass.
- `uv run --locked --group hygiene python -m unittest discover -s tools/engineering -p 'test_*.py' -v`:
  29 pass on the selected analyzer candidate.
- `uv run --locked gz-starter validate`: 0.11.0 and both catalogs valid.
- `uv build --no-sources` and `uv run --locked python tools/verify_distribution.py`:
  archive/resource checks and isolated installed CLI checks pass.
- From `baselines/xplane`, `uv run --locked python ../../tools/verify_xplane_baseline.py`:
  positive/negative controls pass on managed Python 3.12.16. Embedded host remains
  unverified. No claim of new Windows/Linux acceptance follows from macOS proof.
- Hashed `uv export --locked --all-groups --format requirements.txt --no-emit-project`
  outputs were audited with the pinned `pip-audit --requirement <export> --no-deps
  --disable-pip --cache-dir <task-local-cache> --format json`. Results: **74 root /
  75 host-reference registry dependencies**, **zero known vulnerabilities**,
  **zero skipped packages**. Empty runtime projects are deliberately excluded
  from the export. Task-local caches preserve the earlier documented host-cache
  workaround; no user cache or setting was deleted or changed.

No authoritative wheel-resource input changed, so regeneration is unnecessary;
existing drift/archive checks pass. Four routine hook categories, selected lint
rules, numeric thresholds and acceptance authority remain unchanged. No new
behavioral test is needed for an exact-version guard: existing owning negative
and threshold tests plus the corpus comparison cover its consequences.

This completes the scoped source/environment migration. Release preparation
must reference these actual candidate inputs and refresh evidence when inputs
change. Current native loading, real XPPython3 operation, cohesion and remaining
deeper release qualification retain their existing limits. Cognitive status is
DEFERRED / measurement UNKNOWN; no strict release/adopter acceptance is claimed.
