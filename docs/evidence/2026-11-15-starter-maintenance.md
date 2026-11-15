# Starter maintenance — November 15, 2026

Mode: **update**, explicitly invoked through `gzs-update-dependencies` under
the starter's completed-migration binding. The preceding explicit Git-sync
authorization in this conversation covers ordinary main commits/pushes and CI
observation. It does not authorize a tag/release, native installation, user-wide
activation, companion edits or adopter propagation.

## Scope and governing decisions

Started from clean main `fab4dc26d54d4cda0ac39d92608729ba7c8de56d`, also the
rollback reference. Reuse approved ADR-0001-001: review exact component changes
without claiming combined behavior from configuration. No new architecture,
profile choice, tool family, routine hook or permanent maintenance reporter is
introduced. The naming/layout and record-management proposals remain drafts.
This Windows session uses `U:\repos\agents\gz-skills-first-starter`; it does not
move the active checkout or establish the desktop binding described by earlier
handoffs from another environment.

Published baseline is **0.9.0**, immutable release commit
`3f76acf0038b030bf5abd85ce4a419e890d3e420`; pending target stays **0.10.0 / minor**.
The existing #12/#13 ADR/policy bundle, canonical rename and selected maintenance
govern this change. Reuse that valid target; bundle, package, lock, runtime and
packaged-bundle mirrors must agree. Remaining companion/internal-use/behavioral
qualification and adopter propagation are not satisfied by this maintenance.
The broader CLI/naming implementation is excluded until separately selected.
No release publication is authorized or claimed.

Inventory includes both pyprojects/locks, managed runtime pins, resolver/backend,
dev/hygiene groups, four local hooks, CI actions/execution pins, bundle, both
catalogs, six wheel resources and all three native project configurations.
These are two independent Python projects, not a uv workspace. Empty runtime
dependencies, additional tooling and centralized owning pyproject settings are
preserved. No container, other-language manifest, vendored upstream skill or
project-managed standalone binary was found. This publishing starter does not
self-adopt. Native CLI binaries, caches and user settings are outside the source
update; selected sources do not establish installation or active loading.

## Official live selections

The [registry receipt](2026-11-15-dependency-recheck.json) records every selected
version, latest non-yanked stable release, Python constraint, official PyPI URL
and candidate manifest/lock hash for **76 distinct registry projects**, including
uv and uv_build. All selected versions already equal upstream stable; none is
yanked. Queries considered stable releases across families. No registry update
or stale-family exception is needed.

| Project tool | Previous -> selected/latest |
| --- | --- |
| uv / uv_build | 0.13.8 -> 0.13.8 |
| Ruff | 0.17.5 -> 0.17.5 |
| ty | 0.0.104 -> 0.0.104 |
| pre-commit | 4.7.0 -> 4.7.0 |
| Bandit | 1.9.4 -> 1.9.4 |
| Complexipy | 9.0.0 -> 9.0.0 |
| Cosmic Ray | 8.9.0 -> 8.9.0 |
| coverage | 7.17.3 -> 7.17.3 |
| deptry | 0.25.1 -> 0.25.1 |
| Import Linter | 2.16 -> 2.16 |
| Interrogate | 1.7.0 -> 1.7.0 |
| Lizard | 1.26.0 -> 1.26.0 |
| pip-audit | 2.10.1 -> 2.10.1 |
| Vulture | 2.16 -> 2.16 |

[Python.org](https://www.python.org/downloads/) and uv's managed download inventory
agree on **3.14.10** and **3.12.16** as the latest patches in their approved
families. Latest upstream stable is **3.15.2**, outside ordinary N-1/host policy;
3.16 is prerelease. Retain exact runtime/CI pins, `>=3.14,<3.15`, the separate
`>=3.12,<3.13` host-reference range, and uv's minimum-only **>=0.13.5**.
Actual resolver is current [uv 0.13.8](https://github.com/astral-sh/uv/releases/tag/0.13.8)
on Windows x86_64; no machine-wide tool update is needed.

| Component/action | Previous -> selected/latest | Immutable commit |
| --- | --- | --- |
| [gz-skills](https://github.com/tvproductions/gz-skills/releases/tag/v0.12.0) | 0.11.0 -> **0.12.0** | a8f67160475a6995391d2244188d7c38eda65dfb |
| [Superpowers](https://github.com/obra/superpowers/releases/tag/v7.0.2) | 7.0.2 -> 7.0.2 | 22f0b463e7a5e579904dd6211a520321035526f7 |
| [Backplane](https://github.com/tvproductions/superpowers-backplane/releases/tag/v0.2.0) | 0.2.0 -> 0.2.0, disabled | 0b18e34e65379e729d8fece97151a1bb8604b461 |
| [checkout](https://github.com/actions/checkout/releases/tag/v7.0.1) | 7.0.1 -> 7.0.1 | 3d3c42e5aac5ba805825da76410c181273ba90b1 |
| [setup-uv](https://github.com/astral-sh/setup-uv/releases/tag/v10.3.3) | 10.3.3 -> 10.3.3 | 68559e99cc807c1eb7e9238fd43a15bba460eec2 |

The starter's own latest published release remains 0.9.0; do not run template
adoption/upgrades against this publishing repository. Compatibility imports,
legacy CLI alias, marketplace IDs and provenance directories remain intact.

## gz-skills impact and source reconciliation

Resolved the annotated v0.12.0 tag through tag object
`e078a2f7028e0429c8a32b5e878342d2cebec051` to the release commit above. Reviewed
the official release notes, [source comparison](https://github.com/tvproductions/gz-skills/compare/v0.11.0...v0.12.0),
[packaged workflow guidance](https://github.com/tvproductions/gz-skills/blob/a8f67160475a6995391d2244188d7c38eda65dfb/skills/gzs-router/references/workflows.md)
and [owning release evidence](https://github.com/tvproductions/gz-skills/blob/main/docs/evidence/2026-11-14-0.12.0-release.md).
Router 0.6.0 adds task execution/routing guidance for independent gz-skills and
complementary Superpowers use. Dependency update 0.5.0 makes direct invocation
perform scoped updates/verification, agreeing with this starter's existing
binding. The other eighteen skills and native adapter contracts are unchanged;
new packaged guidance is not a new workflow owner. Ordinary Git sync still needs
authority and this starter's release remains separately gated. No new ADR or
portable ADR contribution is supplied by the release.

Bundle, both catalogs, OpenCode source, current guidance and generated resources
select the same new component. Codex/Claude development sources require the
resulting published catalog commit; they cannot refer to a future self SHA.
Publish the verified catalog, then update those two immutable refs in a bounded
binding follow-up, preserving every activation/duplicate-source override. Do not
use `plugin add`, mutate caches or enable Backplane. Fresh-session 0.12.0 loading
and model behavior remain UNKNOWN; the session initially advertises cache 0.10.1.

Python 3.14 opportunity review uses the [versioned release/porting notes](https://docs.python.org/3.14/whatsnew/3.14.html)
and local opportunity guide. Retain existing annotation semantics: no annotation
introspection consumer changed. Bounded executor submission/interpreter pools,
Zstandard and template strings have no new helper consumer. Defer Path.copy/move
replacement because exclusive writes, symlink handling, recovery and concurrent
replacement preservation need the existing tested semantics. No modernization
machinery is justified by this instruction-only update. These 3.14-only APIs are
unavailable to the 3.12 host reference; actual embedded-host behavior stays UNKNOWN.

## Observed verification

In each owning Python project, `uv lock --upgrade`, `uv sync --locked --all-groups`,
`uv lock --check` and `uv pip list --outdated --format json` pass. Both outdated
results are `[]`; both locks remain byte-identical to rollback after resolution
and consistency checks. Root lock SHA-256 is
`67f1fec2c542f6f43ba0652edb73ffa01f53ad3258b0e9c777c96cca8f788323`;
host-reference lock is `9fbd72e70b8bf85cc6927c26d259bd872906f4552b245d868432abc7f51925e8`.
The root environment was already synchronized in the preceding sync. The
standalone environment needed synchronization to the existing lock; this changed
installed tools, not declarations or lock selections.

- `uv run --locked pre-commit run --all-files --verbose`: all four hooks pass,
  including **72 unittest cases**. No new tests or relaxed rules were needed.
- `uv run --locked gz-starter validate`: valid 0.10.0 and both catalogs.
- `uv run --locked python tools/package_resources.py`, then `--check`: all six
  resource copies agree with their owning inputs.
- `uv run --locked python ../../tools/verify_xplane_baseline.py` in the separate
  project: positive/negative tool controls pass on managed Python **3.12.16**;
  real XPPython3/simulator execution remains unverified.
- Root execution is managed CPython **3.14.10 / AMD64**, with Ruff 0.17.5,
  ty 0.0.104 and pre-commit 4.7.0 resolved inside the root `.venv`. Existing
  installed pre-commit hook points at that environment; four hook categories and
  root/member target configuration are unchanged.
- Reuse the **29 analyzer regression passes** observed during the preceding
  sync in this conversation: analyzer code, fixtures, tools, settings and runtimes
  are unchanged. No analyzer-specific update invalidates that evidence.
- Hashed `uv export --locked --all-groups --format requirements.txt --no-emit-project`
  outputs feed the project-pinned auditor with `--requirement <export> --no-deps
  --disable-pip --format json`; audit results and final artifact results are
  recorded below after observation. Unpublished local projects are excluded by
  export, rather than silently skipping registry dependencies.

The auditor emits generic hash advice despite hashed exports. Its root cache
read warning concerns performance only; it still returned a complete result.
No source, resolver or required gate failure is waived.

Both security audits completed: **74 root / 75 standalone registry dependencies**,
**zero known vulnerabilities and zero skipped registry packages**. The standalone
default-cache run was stopped after it consumed CPU without producing a result.
A bounded repeat captured the main thread in Python 3.12 `tempfile._mkstemp_inner`,
called by `NamedTemporaryFile` from pip-audit's cache write. Changing only the
HTTP cache to a new task-local directory completed the same export in three
seconds; a subsequent ordinary pinned CLI run passed in one second. The original
cache-path behavior is unresolved beyond this localized boundary. No default
cache was deleted, machine setting changed or dependency downgraded. Reproduce
with `--cache-dir <task-local-directory>` on this host; the root audit's cache-read
warning and this baseline cache-write stall are environment limitations, not
missing audit results. Temporary instrumentation was outside the repository.

`uv build --no-sources` built the 0.10.0 sdist and wheel; `uv run --locked python
tools/verify_distribution.py` passed resource/archive inventories and isolated
installed CLI checks. Both compatibility command names remain available.
`uv run --locked gz-starter version` reports 0.10.0 and `git diff --check` passes.
Later prose-only evidence updates reuse those applicable artifact results under
the verification policy. Normal commit hooks must pass without bypass, and
exact final-commit CI remains to be observed after source/binding publication.

Astral applicability: A01-A08/A10/A17 have the identity, runtime, tool, source,
lock and export evidence above. A09 local hooks pass; exact final-commit CI must
be observed after sync. A11/A12 have the source-independent build and isolated
installed proof above. A13 is inapplicable to this CLI rather than a typed library;
A14 is inapplicable to independent runtime projects; A15 has only public registry
and immutable Git sources; A16 native/embedded deployment is unverified. A18 keeps
the starter-wide cognitive deferral (ceiling 15, measurement UNKNOWN), remaining
deeper-tool/cohesion and ADR/trio/native-host limits. This is source maintenance,
not strict release/adoption acceptance or engine qualification.

## Published catalog and project binding

Source/catalog commit `1173009eb4484c2dbde2bac672ad4f96b5208438` passed normal
commit hooks and was pushed ordinarily after a fresh fetch found no remote
divergence. Its [CI run](https://github.com/tvproductions/gz-starter/actions/runs/43743537501)
passed both jobs. The binding follow-up changes Codex/Claude project refs to
that exact published catalog and updates this record, changelog, structure guide
and handoff. Existing true/false activation values, duplicate suppression and
Claude `autoUpdate: false` are preserved. OpenCode already selects the same
component. No cache installation, user setting or deferred-plugin activation
was performed. Native installation/discovery remains UNKNOWN.
Parsed before/after TOML/JSON comparison confirms the ref is the only setting
change. Both refs equal the published catalog commit, its catalog bytes agree
with the working catalog, all 0.10.0 mirrors agree, and recorded pyproject/lock
hashes remain unchanged.

Reuse the unchanged-input full gate/build/artifact/audit results. Parse and
compare the binding files and published catalog; retain normal hooks. Observe
CI for the binding follow-up's own exact SHA at closeout, then verify clean
main/origin alignment. Do not add another CI-receipt-only commit.
