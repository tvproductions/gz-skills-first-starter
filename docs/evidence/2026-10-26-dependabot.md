# Dependabot implementation receipt — October 26, 2026

Scope: user-directed Dependabot implementation for standard and X-Plane cases,
building on the same session's approved scheduled-scan policy correction. The
worktree already contained that policy/documentation change. No Git push, remote
configuration mutation, plugin installation, simulator access or publication was
performed. This is not the release-wide freshness receipt.

The operator subsequently authorized Git synchronization using
`gz-skills:gzs-git-sync`. Initial fetch found main/origin aligned at `35ac057`;
the current commit contains the reviewed policy, scanner, independent X-Plane
baseline and verification changes. Normal commit hooks and exact-SHA CI
observation are required. Git sync publishes this configuration to the default
branch; it does not waive the separate hosted-scan and real-PR UNKNOWNs below.

## Candidate inputs

- `.github/dependabot.yml`: independent weekly `uv` jobs for `/` and
  `/baselines/xplane`, plus `github-actions` at `/`; Mondays 09:00 America/Chicago,
  five open version-update PRs per job, direct and transitive package updates.
- Root project: unchanged Python 3.14.9 and uv/uv_build 0.13.5, Ruff 0.17.2,
  ty 0.0.91, pre-commit 4.7.0; hygiene selections complexipy 8.1.0 (defect
  reproducer), Cosmic Ray 8.7.0 and Lizard 1.24.3. Root package pins and lock
  were not refreshed by this work.
- New `baselines/xplane` dependency-only project: managed standalone Python
  3.12.16, uv 0.13.5; dev Ruff 0.17.2, ty 0.0.92, pre-commit 4.7.0,
  uv_build 0.13.5; hygiene complexipy 8.2.0 (unqualified defect reproducer),
  Cosmic Ray 8.7.0 and Lizard 1.24.3. uv generated a separate revision-5 lock
  containing 45 packages including the virtual project. Exact sync installed
  44 distributions. Root and X-Plane locks select distinct Python minor families.
- CI retains checkout v7.0.1 at
  `3d3c42e5aac5ba805825da76410c181273ba90b1` and setup-uv v10.3.2 at
  `07a047e608db84b3d8c06cd9a7c7dcc9c355c18e`. The new job uses those existing
  reviewed actions with Python 3.12.16 and uv 0.13.5. No action freshness claim
  is supplied by adding this job.
- SP v7.0.1, gz-skills v0.8.0 and disabled Backplane remain unchanged in the
  bundle/catalogs. Their latest status/native discovery was not reverified here.

The candidate is the local diff containing these inputs, not a published release
or an observed hosted Dependabot deployment. Recheck the committed candidate and
hosted results before claiming operational coverage.

## Official freshness and compatibility evidence

Official PyPI JSON queries on October 26 returned:

| Tool | Latest registry version | X-Plane selection | Decision |
| --- | --- | --- | --- |
| [uv](https://pypi.org/pypi/uv/json) | 0.13.5 | 0.13.5 execution pin | Retain required resolver |
| [uv_build](https://pypi.org/pypi/uv-build/json) | 0.13.5 | 0.13.5 | Pin as packaging tool in this non-package environment |
| [Ruff](https://pypi.org/pypi/ruff/json) | 0.17.2 | 0.17.2 | Adopt; positive/negative check probes pass |
| [ty](https://pypi.org/pypi/ty/json) | 0.0.92 | 0.0.92 | Adopt latest beta under the existing no-stable-release exception; probes pass |
| [pre-commit](https://pypi.org/pypi/pre-commit/json) | 4.7.0 | 4.7.0 | Adopt; CLI launch passes |
| [complexipy](https://pypi.org/pypi/complexipy/json) | 8.2.0 | 8.2.0 | Track as defect reproducer; no cognitive qualification claimed |
| [Cosmic Ray](https://pypi.org/pypi/cosmic-ray/json) | 8.7.0 | 8.7.0 | Retain selection; X-Plane-runtime mutation qualification UNKNOWN |
| [Lizard](https://pypi.org/pypi/lizard/json) | 1.24.3 | 1.24.3 | Retain selection; no new deeper acceptance claim |

The reported Python requirements permit 3.12 for these tools; Lizard's metadata
does not specify a Python floor. A successful resolution/install establishes
neither analyzer correctness nor full host compatibility. Root ty 0.0.91 and
complexipy 8.1.0 are behind the observed registry releases, not current. Their
root upgrades were outside this bot-configuration change and remain required
review work; this receipt supplies no compatibility exception for them.

[Python 3.12.16](https://www.python.org/downloads/release/python-31216/) is the
October 25 security release and the newest 3.12 CPython listed by required uv
at review. The managed 3.12.16 interpreter was already installed; the new project
uses it without changing any embedded runtime. XPPython3's official
[installation guidance](https://xppython3.readthedocs.io/en/latest/usage/installation_plugin.html)
still documents its Python 3.12 layout. The actual host patch and its support
for these standalone selections remain UNKNOWN; no host acceptance is inferred.

[GitHub's ecosystem table](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories)
lists uv 0.11 and supports tagged SHA Action updates. Current upstream
[uv updater source](https://github.com/dependabot/dependabot-core/blob/f0feb6fa5fd8b4f176de03e7d76e60dd2ff5af17/uv/Dockerfile)
selects uv 0.13.5. The
[lock updater](https://github.com/dependabot/dependabot-core/blob/f0feb6fa5fd8b4f176de03e7d76e60dd2ff5af17/uv/lib/dependabot/uv/file_updater/lock_file_updater.rb)
includes a build-only dependency path. Upstream main resolved through GitHub's
API to `f0feb6fa5fd8b4f176de03e7d76e60dd2ff5af17`. This supports attempting the
configuration without downgrading our resolver; it does not establish which
revision GitHub's hosted service deploys. Actual job/PR behavior remains UNKNOWN.

## Applicability and retained boundaries

The X-Plane project contains no product code, package or simulator entry point.
`package = false` follows uv's documented
[non-package configuration](https://docs.astral.sh/uv/concepts/projects/config/#project-packaging).
Build/installed-artifact acceptance is inapplicable to that dependency-only
project; it remains required for the root helper and adopter products. This is
not permission for an adopter application to omit `src/`, uv_build or installed
proof. Neither baseline is a member of a shared workspace.

The verifier needs portable subprocesses, temporary files and TOML reading,
all available in 3.12. No concrete Python 3.14-only API gain warrants imposing
3.14 on the host-bound probe; retain the root's 3.14 policy separately.

Maintainer ownership/revisit: recheck hosted updater compatibility and the root
build-only update path on the first real Dependabot jobs/PRs after merge. Revisit
ty's beta exception at stable release or next scoped maintenance. Complete
embedded-host verification before accepting a real X-Plane adopter, and retain
the existing deeper-tool acceptance gaps. No new compatibility waiver is created.

## Verification

- PASS: new X-Plane lock generated by uv 0.13.5, exact all-group sync on managed
  Windows CPython 3.12.16, subsequent `uv lock --check` with no lock changes.
- PASS: X-Plane verifier's valid Ruff check/format/type-check inputs, deliberate
  undefined-name/type-assignment failures with required diagnostic IDs and
  exit codes, and one discovered unittest with passing/failing assertion controls.
  pre-commit and uv_build module launches pass on that interpreter.
- PASS: root locked all-group sync; four routine pre-commit hooks (Ruff check,
  Ruff format, ty, unittest). No extra routine hook or hygiene CI gate was added.
- PASS: YAML parsing and one-off cross-check of both scan paths, canonical lock
  Python families, exact interpreter pins, CI uv versions and independent projects.
  This is a local syntax/consistency check, not hosted schema/operation proof.
- PASS: bundle/both catalogs validate; source-independent sdist-to-wheel build;
  wheel resources and isolated installed helper commands; sdist includes the
  scanner and X-Plane declarations/lock/pin/README and excludes `.venv` contents.
  At final verification the machine command resolved uv 0.13.1 and correctly
  failed the required-version check. Repeating build and distribution checks
  through `uv tool run --from uv==0.13.5 uv ...` passed, including nested uv
  commands. No machine-wide uv replacement or relaxed version requirement was used.

Hosted Dependabot runs and update PRs, Linux execution of the new CI job,
embedded-host behavior, absent deeper tools and unperformed deeper analyses
remain UNKNOWN. These gaps prohibit a blanket current/fully verified claim.
Rollback is removal of the new scanner/baseline/CI changes; previous root pins
and lock are preserved. No other repository or global plugin state was modified.
