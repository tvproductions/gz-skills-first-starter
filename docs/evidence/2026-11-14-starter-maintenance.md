# Starter maintenance — November 14, 2026

The maintainer explicitly authorized this separate dependency/component update,
ordinary main Git sync and CI verification. This follows the freshness-only
policy pass at c8f286e32dff54164b5c80c91133fee2f1f8ec7d. Existing
ADR-0001-001 applies. Published baseline remains 0.9.0; reuse pending 0.10.0
for the existing policy/ADR feature bundle. No release/tag, adopter propagation,
global installation or Backplane activation.

## Stable selections

Checked official PyPI release metadata and GitHub stable releases on November 14.
Both project locks were regenerated with task-local uv 0.13.8, using
`uv lock --upgrade` and `uv sync --locked --all-groups`. The machine-wide uv
installation was not changed. Python.org and uv's managed-runtime index agree
that 3.14.10 and the standalone host baseline's 3.12.16 are current patches in
the approved families. Python 3.15 is outside the ordinary N-1 policy.

| Tool | Previous | Selected stable |
| --- | --- | --- |
| uv / uv_build | 0.13.7 | 0.13.8 |
| Ruff | 0.17.4 | 0.17.5 |
| ty | 0.0.99 | 0.0.104 |
| Complexipy | 8.1.0 / standalone 8.2.0 | 9.0.0 |
| Cosmic Ray | 8.8.0 | 8.9.0 |
| coverage | 7.17.2 | 7.17.3 |
| Lizard | 1.24.3 | 1.26.0 |
| pre-commit | 4.7.0 | 4.7.0 |
| Bandit | 1.9.4 | 1.9.4 |
| deptry | 0.25.1 | 0.25.1 |
| Import Linter | 2.16 | 2.16 |
| Interrogate | 1.7.0 | 1.7.0 |
| pip-audit | 2.10.1 | 2.10.1 |
| Vulture | 2.16 | 2.16 |

Direct tool versions match the current non-yanked stable PyPI releases, including
new families. Both locks also refresh filelock, grimp, markdown-it-py and
stevedore transitives. After synchronization, both `uv pip list --outdated
--format json` results are empty. Both `uv lock --check` calls pass without
changing lock hashes. Keep uv's minimum support >=0.13.5 distinct from the tested
0.13.8 execution choice. No separate Ruff/ty/uv configuration was introduced;
Astral settings remain in the owning pyproject.toml. The host baseline remains
an intentionally separate project/environment, not a workspace member.

| Component | Previous | Selected immutable release |
| --- | --- | --- |
| SP | v7.0.1 | v7.0.2, 22f0b463e7a5e579904dd6211a520321035526f7 |
| gz-skills | v0.8.3 | v0.10.1, 4c836e3db6d43c495863a2090daaea56585a6ea9 |
| Backplane | unreleased d0eeee829c491da02351e793544aa16ad96461bf | v0.2.0, 0b18e34e65379e729d8fece97151a1bb8604b461; disabled |

Both native catalogs and packaged resources use these exact sources. OpenCode's
project URLs follow the same pins. Codex/Claude development marketplace refs must
point to the resulting immutable catalog commit, preserving activation settings.
Native cache installation/discovery and ADR contribution qualification are
separate from pin consistency; neither is certified by this maintenance pass.
Backplane's first release does not close its adoption/host acceptance gaps.

CI action releases are already current: checkout v7.0.1 at
3d3c42e5aac5ba805825da76410c181273ba90b1 and setup-uv v10.3.3 at
68559e99cc807c1eb7e9238fd43a15bba460eec2. Retain both immutable SHAs; refresh
only CI's uv version. Weekly Dependabot scope/schedule is preserved.

## Compatibility and verification

- Full four-check integration gate passes: Ruff check/format, ty and unittest.
- All 29 existing on-demand analyzer regressions pass. The old Lizard guard
  first rejected 1.26.0; after advancing the reviewed version, its existing
  boundary/discovery/weighted-aggregate/error tests pass with unchanged ceilings
  and lizard-functions-v1 counting semantics. No new tests or abstractions added.
- Complexipy 9's existing canaries pass, including the fixed keyword-conditional
  blind spot (both equivalent forms score nine). Upstream documents major scoring
  changes; do not equate historical scores. No thresholds/snapshots were lowered,
  no historical evidence rewritten, and no shared cognitive-engine acceptance
  claimed. Existing source complexity findings remain visible.
- Cosmic Ray 8.9.0's bounded real fixture passes: two killed and two survived
  mutants, structured outcomes checked and original source restored.
- Standalone 3.12.16 baseline verifier passes positive/negative Ruff, ty and
  unittest controls plus pre-commit/backend probes. Embedded XPPython3 host
  execution remains unverified.
- pip-audit reports no known vulnerabilities: 74 registry dependencies in the
  root environment and 75 in the standalone baseline. The unpublished local
  starter is explicitly skipped as absent from PyPI. The root backend selection
  is also audited through its identical standalone dependency.
- Bundle/both-catalog validation and generated-resource drift checks pass.
- Source-independent wheel/sdist build and isolated installed-helper verification
  pass using the owning verifier with only external artifact paths redirected.
  Exact-commit CI is required for final sync completion; report its observed
  result at closeout without a receipt-only follow-up commit.

Sources: [PyPI metadata](https://pypi.org/),
[Python 3.14.10](https://www.python.org/downloads/release/python-31410/),
[Python 3.12.16](https://www.python.org/downloads/release/python-31216/),
[uv 0.13.8](https://github.com/astral-sh/uv/releases/tag/0.13.8),
[Complexipy 9 migration](https://complexipy.com/migration/),
[Lizard 1.26.0](https://github.com/terryyin/lizard/releases/tag/1.26.0),
[SP 7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2),
[gz-skills 0.10.1](https://github.com/tvproductions/gz-skills/releases/tag/v0.10.1),
[Backplane 0.2.0](https://github.com/tvproductions/superpowers-backplane/releases/tag/v0.2.0).

## Later explicit maintenance invocation

Mode: **update**, explicitly invoked through `gzs-update-dependencies` under this
repository's completed-migration binding on November 14, 2026. Candidate starts
at clean main `0d60d0dc6b6a4a695135a9e1bbcc4e7830171dd2`; that commit is the
rollback reference. No pre-existing changes, new dependency ecosystem, missing
project-required package or profile change was found. This is the publishing
starter, not a self-adopter. Reuse approved ADR-0001-001 and pending **0.10.0**
from published **0.9.0** / `3f76acf0038b030bf5abd85ce4a419e890d3e420`.
The existing #12 policy/ADR release scope and remaining/deferred gates still
govern; this component refresh does not establish release acceptance.

Live PyPI metadata covers **76 distinct registry projects**, including every
registry package in both locks, all direct dev/hygiene/backend pins and the uv
resolver. Every selected version equals its latest non-yanked stable upstream
release; no selected release is yanked. The earlier table's Python tools remain
unchanged. Full package results and authoritative metadata URLs are in the
[registry recheck](2026-11-14-dependency-recheck.json). The initial urllib query
failed on system DNS; curl retrieved the same official PyPI JSON successfully.
Neither source availability nor package freshness is inferred from cached locks.

Official [Python releases](https://www.python.org/downloads/) and uv's managed
runtime inventory still select **3.14.10** and **3.12.16**. Python **3.15.2** is
newest upstream, outside the ordinary N-1 and embedded-host families. Preserve
`>=3.14,<3.15` and `>=3.12,<3.13`, exact runtime/CI pins and uv **>=0.13.5**.
Actual resolver is uv **0.13.8**, current upstream; no machine-wide update needed.

Live GitHub releases and resolved commits confirm SP 7.0.2, Backplane 0.2.0,
checkout 7.0.1 and setup-uv 10.3.3 remain current at the exact SHAs above.
The starter's latest published release remains 0.9.0. **gz-skills 0.11.0** was
published at 18:05 UTC after the earlier pass. Its annotated tag resolves to
`62622aee80ce27d4a39efe3554a583b844f38876`, replacing 0.10.1 /
`4c836e3db6d43c495863a2090daaea56585a6ea9` in the bundle, both catalogs,
OpenCode source and current guidance. Generated resource copies are refreshed.
Reviewed official [release notes](https://github.com/tvproductions/gz-skills/releases/tag/v0.11.0),
[source comparison](https://github.com/tvproductions/gz-skills/compare/v0.10.1...v0.11.0)
and [release receipt](https://github.com/tvproductions/gz-skills/blob/62622aee80ce27d4a39efe3554a583b844f38876/docs/evidence/2026-11-14-0.11.0-release.md).

Compatibility review: only three skill bodies change: Git sync 1.1.0, quality
gate 0.1.3 and dependency update 0.4.2. The other seventeen, installer, lock,
runtime and twenty-skill catalog contracts are unchanged. Stage-aware checks
preserve required tests for this implemented helper. Dependency mode now honors
established user/project authority explicitly. Git sync publication follow-through
requires the consuming project's publication authority; it does not authorize
publishing this starter's pending 0.10.0 or close its ADR feature. No new
architecture, workflow lifecycle or gate waiver is adopted.

Python 3.14 opportunity review against the versioned
[release/porting notes](https://docs.python.org/3.14/whatsnew/3.14.html) and local
opportunity guide: retain current annotation semantics; no runtime introspection
consumer changed. Bounded executor submission and interpreter pools provide no
helper benefit because its workflow remains sequential. Zstandard and structured
templates have no storage/processor consumer. Defer Path.copy/move replacement:
the helper's exclusive creation, rollback and concurrent-file preservation need
their current tested semantics. No broad modernization is warranted by this
instruction-only component refresh. These 3.14 APIs remain unavailable to the
separate 3.12 host baseline; actual embedded-host execution remains UNKNOWN.

Scope includes both pyprojects/locks, exact Python pins, backend, resolver,
pre-commit's four local hooks, CI execution/action pins, bundle, both catalogs,
packaged copies and all three project source configurations. No container,
additional language manifest, separately managed binary or vendored skill tree
exists. Native host CLI installations, user settings and plugin cache updates
are outside this source-maintenance scope. Deferred cognitive/cohesion and ADR
qualification obligations are unchanged, not satisfied by manifest validation.

`uv lock --upgrade`, `uv sync --locked --all-groups`, `uv lock --check` and
`uv pip list --outdated --format json` completed in each owning project. Both
locks are byte-unchanged and both outdated results are `[]`. Dev/hygiene group
placement and empty runtime dependency sets are preserved.

Verification for the coherent candidate:

- `uv run --locked pre-commit run --all-files`: all four hooks pass (Ruff
  check/format, ty and unittest). No behavioral test additions or gate changes.
- `uv run --locked skills-first-starter validate`: valid 0.10.0 bundle and both
  catalogs with gz-skills 0.11.0. `tools/package_resources.py` refreshed affected
  copies; the existing resource-drift tests pass. All version mirrors stay 0.10.0.
- Root and standalone `uv export --locked --all-groups --format requirements.txt
  --no-emit-project` retain hashes; the project-pinned `pip-audit --requirement
  <export> --no-deps --disable-pip --format json` reports zero known
  vulnerabilities across **74** and **75** registry dependencies respectively,
  with no skipped registry packages. The unpublished projects are excluded by
  the export. Exports contain 584/404 SHA-256 entries. The auditor emits generic
  hash advice despite those hashes; the standalone run also reports ignored
  cache-deserialization warnings, then successfully returns complete results.
- `uv run --locked python ../../tools/verify_xplane_baseline.py` from the
  standalone project passes on managed **3.12.16**; real host remains unverified.
- `uv build --no-sources` builds sdist then wheel successfully with uv_build
  **0.13.8**. `uv run --locked python tools/verify_distribution.py` passes archive
  resources/metadata and isolated installed CLI/configuration proof for all
  helper hosts and both policy modes outside the checkout.
- Actual root execution is managed CPython **3.14.10**, arm64; Ruff, ty,
  pre-commit and hygiene executables resolve within the project `.venv` at the
  selected versions. Effective Ruff settings resolve root pyproject.toml,
  target 3.14, line length 100 and the reviewed rule set; verbose ty passes.
  No relevant UV/Ruff/ty/Python override flags or competing ancestor tool
  configuration was present. The existing native pre-commit hook is installed.
- Both lock hashes stay byte-identical to rollback: root
  `e462d598bc66b8f8f1402510a73adcb846287192ee6549de2f45943fcecf3467`;
  standalone `9fbd72e70b8bf85cc6927c26d259bd872906f4552b245d868432abc7f51925e8`.
  Existing 29 analyzer regressions and bounded Cosmic Ray/Complexipy compatibility
  results from the earlier pass remain applicable: their code, fixtures, tools,
  configs and runtimes are unchanged. No analyzer-specific repeat is triggered.

Astral acceptance applicability: A01-A08, A10-A12 and A17 have the scope,
provenance, exact-environment, metadata, package/export and installed-artifact
evidence above. A09 local hooks pass; final candidate CI is pending the authorized
sync below. A13 is not applicable to this CLI rather than a published typed
library. A14 is not applicable: two deliberately independent incompatible runtime
families, no uv workspace. A15 has public PyPI and immutable public Git sources,
no private index/auth integration. A16 has ordinary pure Python distribution
proof; embedded XPPython3/native host deployment is outside the standalone
reference and remains UNKNOWN. A18 retains the existing owned cognitive and
ADR/native-host gaps; this is not strict release/adoption acceptance.

The earlier explicit main-sync authorization is carried through after local
verification. Source/catalog commit
`d874ef0a68b2892e79db37e27385f2026dc9793a` was committed with normal hooks
(unittest passes; Python-only hooks correctly have no changed Python inputs,
after the full all-file run above), fetched and pushed ordinarily without
remote divergence or reconciliation. A following binding commit changes only
Codex/Claude marketplace refs and their documentation to that now-published
catalog SHA. Both source-commit CI jobs passed in
[run 43627842207](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/43627842207).
Parsed Codex/Claude settings confirm both refs and all activation/duplicate
overrides; project activation and duplicate-source overrides are unchanged;
no `plugin add`, cache installation or user-scope change was used. OpenCode
already selects the same exact component source. Native 0.11.0 discovery,
combined-stack behavior and final candidate CI remain UNKNOWN until observed.
Observe both `Check starter` jobs for the final binding commit and report the
result at closeout without a receipt-only commit. This receipt records source
selection and local verification, not native installation or starter publication.
