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
