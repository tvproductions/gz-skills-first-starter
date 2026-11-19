# Dependency maintenance — November 19, 2026

Mode: **update**, explicitly invoked through selected gz-skills **0.13.0** /
`gzs-update-dependencies` **0.5.0** under the completed-migration binding.
Started from clean main `6535e9cd93baca66a21deb8243188db79796508a`, the rollback
reference. Source/environment maintenance is authorized; commit/push, publication,
native installation/activation and companion/adopter changes are outside this pass.

## Scope, authority and version

Published baseline **0.11.2**, immutable source
`1175433c950d47d5330e4a9a36a986f1a0c6ae26`, is verified through the latest stable
[GitHub release](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.2).
Select **0.11.3 / patch** to restore the existing latest-stable tooling commitment
following new upstream releases. The
[bounded roadmap scope](../../ROADMAP.md#selected-0113-scope--dependency-maintenance-november-19-2026)
owns included work and acceptance. No new policy, product requirement, public
interface or architectural choice is introduced. Reuse approved ADR-0001 edition 1;
component sources and the binding/qualification procedure do not change.
The bootstrap correction's proposed 0.12.0 remains separately approval-gated.
This maintenance does not approve its design, ADR or implementation.

Inventory covers both independent Python projects/locks/environments and runtime
pins, every dev/hygiene/transitive registry package, uv, root/example isolated
build backends, hooks, CI execution and Action pins, bundle/catalogs and native
Codex/Claude/OpenCode source/activation bindings. The root owns the example's
tool settings/environment; the example has no runtime dependencies or separate
lock. There is no other language ecosystem, container, vendored binary or adopted
starter provenance to migrate: this is the canonical starter, not its own adopter.
The project supplies its Python standard; no lite/heavy profile is inferred.
Cohesion remains adopter-owned and the shared cognitive engine is undelivered.

## Current stable selections and compatibility

The [machine-readable receipt](2026-11-19-dependencies.json) records all **77
registry projects**, before/after versions, official source URLs, Python
requirements, selected yank status, exact component/Action identities, both
structured security audits and candidate input hashes.

| Tool | Before | Selected/latest | Consumers |
| --- | --- | --- | --- |
| [ty](https://github.com/astral-sh/ty/releases/tag/0.0.107) | 0.0.105 | 0.0.107 | both dev groups and installed typing consumers |
| [Import Linter](https://github.com/import-linter/import-linter/blob/v2.17/docs/release_notes.md) | 2.16 | 2.17 | both hygiene groups and the starter import-boundary contract |
| [virtualenv](https://github.com/pypa/virtualenv/releases/tag/21.15.9) | 21.15.8 | 21.15.9 | both transitive pre-commit/tool graphs |

Review intervening [ty 0.0.106](https://github.com/astral-sh/ty/releases/tag/0.0.106):
its breaking diagnostic split affects incompatible TypeIs narrowings; the new
version also corrects generic constructor inference and uv-script isolation.
No active project override or assertion depends on the old diagnostic names.
Retain all defaults and verify valid/invalid assignments and disjoint TypeIs
narrowing on both interpreters. The naming-rule proposal remains deferred.

Import Linter 2.17 accepts positional configuration paths, deprecates `--config`
and rejects colon/duplicate contract ids. This project uses auto-discovered TOML
with one id-free forbidden contract; no CLI/configuration migration is needed.
Validate that contract plus kept/broken boundaries and invalid TOML identifiers
in disposable fixtures. The upstream source has moved to the import-linter
organization; PyPI and its exact v2.17 tag/release notes supply release evidence
(the GitHub Releases API has no release record).

virtualenv 21.15.9 fixes symlink-app-data reseeding after pip reinstalls, long
Windows app-data cleanup, yanked seed updates and empty-PATH activators; Python
3.15 lazy-import optimizations are outside the selected families. Test exact
child creation, offline pip reinstall/bytecode/reseed and empty-PATH bash
activation on actual macOS ARM64. These controls do not establish the Windows
long-path fix, online index-yank handling or other shells/platforms.

All other package/tool selections remain current, including uv/uv_build
**0.13.9**, Ruff **0.17.5** and pre-commit **4.7.0**. Preserve minimum-only uv
**>=0.13.5** and CI's reference selection. Execute with
`uv tool run --from uv==0.13.9 uv ...`; nested hooks resolve the same cached binary.
The machine's unrelated supported uv **0.13.8** and user defaults are unchanged.
No preview feature or native plugin manager update is needed.

Official release/tag queries retain SP **7.0.2**, gz-skills **0.13.0**, deferred
Backplane **0.3.0**, checkout **7.0.1** and setup-uv **10.3.3**, with exact source
SHAs unchanged. Both catalogs and Codex/Claude/OpenCode source/activation and
duplicate-source overrides are preserved. Only the bundle's independent template
version changes; regenerate its wheel resource and validate both catalogs.

[Python.org](https://www.python.org/downloads/) confirms approved family patches
**3.14.10 / 3.12.16**; upstream **3.15.2** stays outside deliberate N-1/embedded
policy. No runtime pin or CI selection changes. Review the
[versioned 3.14 opportunity guide](https://docs.python.org/3.14/whatsnew/3.14.html):
this scoped tool migration adds no concurrency, compression, template processing
or annotation-introspection consumer. Defer that machinery; Path.copy/move does
not establish the helper's exclusive-write/preservation semantics. There is no
justified runtime modernization in this pass, and 3.14-only APIs remain unavailable
to independent host-reference code.

## Observed verification

Actual execution: macOS ARM64, **uv 0.13.9**, managed **CPython 3.14.10** and
independent **3.12.16**. Disposable controls/audits remain outside the repository;
no new maintenance reporter, hook or skill is added.

- Both projects: `uv lock --upgrade`, `uv sync --locked --all-groups`, repeat
  `uv lock --upgrade`, `uv lock --check`, and
  `uv pip list --outdated --format json` pass. Repeated resolutions preserve
  both lock hashes exactly; both outdated results are `[]`. Every selected
  registry version matches the latest non-yanked stable release.
- Semantic lock review: only ty, Import Linter and virtualenv versions/artifacts
  change, plus root version and owning direct-requirement metadata. Package sets,
  dependency edges, sources, groups and top-level lock contract are unchanged.
  Exact host sync also corrects a pre-existing environment lag in filelock,
  platformdirs and python-discovery to their already-locked November 18 versions.
- `uv run --locked pre-commit run --all-files --verbose`: all four hooks pass,
  including **95 unittest tests**. No rule, assertion, threshold or selection is
  weakened. Normal pre-commit hook installation remains present.
- `uv run --locked --group hygiene python -m unittest discover -s tools/engineering
  -p "test_*.py" -v` passes all **29 checker CLI tests**, including counting,
  portability, cognitive-qualification and consumer-gate controls. Scoring code
  and contracts remain unchanged; this does not qualify the undelivered engine.
- `uv run --locked gz-starter validate` and `gz-starter version` pass at **0.11.3**;
  both catalogs, exact component SHAs and regenerated bundle resources validate.
- From `baselines/xplane`,
  `uv run --locked python ../../tools/verify_xplane_baseline.py` passes actual
  3.12.16 positive/negative Ruff, ty and unittest controls.
- Each baseline's owning pinned pip-audit audits its separate hash-bearing
  `uv export --locked --all-groups --no-emit-local` requirements with
  `--require-hashes --no-deps --disable-pip` and separate task-local caches:
  **75 root / 75 host registry packages, zero known vulnerabilities, zero skips**.
  Generic redundant-no-deps/hashing advice is emitted; requirements already carry
  hashes and structured outcomes cover every registry package.

- Both exact interpreters pass disposable positive/negative ty assignment and
  TypeIs controls (`disjoint-type-is-narrowing`), positional-config Import Linter
  kept/broken boundaries and colon/duplicate TOML-id rejection. The real starter
  contract reports **1 kept, 0 broken**. The first INI identifier fixture did not
  reach the intended validator because that reader normalizes section names to
  their last colon-separated component; an explicit TOML id reaches the required
  rejection. This was a fixture correction, not a relaxed tool requirement.
- Both interpreters create a real virtualenv at their exact patch, offline
  reinstall embedded **pip 26.3**, compile pip bytecode and successfully reseed
  the same symlink-app-data environment. `python -m pip --version` remains usable.
  Empty-PATH bash activation leaves exactly the absolute environment bin path,
  without an empty/current-directory search entry. The fixture supplies `uname`
  and `basename` through absolute-path shell functions and compares canonical
  macOS temporary paths; the first attempt omitted those fixture requirements.
- `uv build --no-sources` and
  `uv run --locked python tools/verify_distribution.py` pass: source-independent
  sdist-to-wheel build, archive/resource/version inventory, isolated installed
  CLI, extracted-source example rebuild, installed positive/negative typing and
  settings-preservation controls. The verified backend remains uv_build 0.13.9;
  installed typing uses updated ty 0.0.107.

All applicable local maintenance gates pass. Final receipt/scope/handoff prose
reuses these passes under the risk-based verification policy; it changes no
execution, dependency, resource or behavior input. Closeout verifies four static
version mirrors plus installed/runtime 0.11.3, **26 candidate input hashes**, all
**181 local file references** across the six changed/new Markdown files, and
whitespace checks. Both repeat lock hashes and complete audit package sets match
the final selected locks.

## Native observations and retained limits

Read-only `codex plugin list --marketplace skills-first-starter --json` on Codex
**0.170.0** reports installed/enabled SP **7.0.2** and gz-skills **0.13.0** and
installed/disabled Backplane **0.3.0**, at the selected exact SHAs. This pass
performs no installation or activation. The invoked maintenance skill is read
from the selected 0.13.0 cache. Inventory/configuration does not establish broader
fresh-session, desktop, other-host or model behavioral qualification.

Retain cognitive **DEFERRED / measurement UNKNOWN**, ceiling **15**, adopter-owned
cohesion, actual embedded XPPython3 and platform/native qualification limits.
Unchanged deeper analyses retain only their prior exact-input bounded evidence;
this pass is maintenance, not strict release/adoption acceptance. Revisit the
standing cognitive deferral at release preparation/candidate delivery; delivery
alone does not establish qualification. No retained outdated package exception
is needed. Hosted CI for the dirty candidate is **UNKNOWN** until separately
requested synchronization; the base commit's green CI does not verify these
changes. Release acceptance and publication remain separate from maintenance.

Disposition: source/environment migration and local maintenance verification are
complete. **0.11.2 -> pending 0.11.3 / patch**; release mirrors and runtime agree.
No commit, push, tag, release or native activation is performed. Roll back only
this reviewed maintenance diff to the clean starting SHA if needed, then exact
sync each owning environment and rerun affected checks; preserve subsequent work
and published history. The pending patch excludes the proposed bootstrap command,
discipline evaluation and all other backlog work.
