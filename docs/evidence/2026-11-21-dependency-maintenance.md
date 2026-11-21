# Dependency maintenance — November 21, 2026

The maintainer invoked `gzs-update-dependencies` in update mode from clean
`main` at `ec5b2f1379c0bcfe46d8850c0b02dcf4ef297dad`, the rollback reference.
Published **0.11.4** (`75f0d83d1b7f4b073d31b06c85cdb20c6ef0cd63`) → pending
**0.11.5 / patch**. The [roadmap](../../ROADMAP.md#selected-0115-scope--dependency-maintenance-november-21-2026)
records the bounded refresh of the existing latest-stable tooling commitment.
The helper and example still declare no runtime dependencies. Both baselines
keep their supported Python ranges, dependency groups, routine checks and
activation decisions. The proposed 0.12.0 bootstrap change remains separately
approval-gated.

## Official sources and selections

At 14:12 UTC the live PyPI JSON inventory covered the 76 unique registry
projects in the two locks (75 per lock), comparing stable, non-yanked releases
with published artifacts. Five projects advanced in both baselines. The other
71 registry selections match the November 20
[inventory](2026-11-20-0.11.4-release.json), which records each pin, registry
URL and Python requirement. The uv executable was checked separately through
its official release. The publication timestamp for coverage 7.17.4 precedes
the November 20 receipt's recorded check time, so the previous receipt's
currency claim for coverage is superseded by this live query.

| Package | Previous → selected and latest | Python requirement | Scope and upstream change |
| --- | --- | --- | --- |
| coverage | 7.17.3 → 7.17.4 | ≥3.11 | Exact hygiene pin. More reliable parallel data and support for a UTF-8 BOM in config. [Release notes](https://coverage.readthedocs.io/en/7.17.4/changes.html#version-7-17-4-2026-11-20) |
| certifi | 2026.10.23 → 2026.11.20 | ≥3.7 | Transitive TLS trust bundle used by requests and dependency audit. The source comparison shows CA bundle removals. [Upstream comparison](https://github.com/certifi/python-certifi/compare/2026.10.23...2026.11.20) |
| decorator | 5.3.1 → 5.3.2 | ≥3.8 | Transitive Cosmic Ray dependency. Preserves the wrapper chain and accepts generated signatures with return annotations. [Upstream changelog](https://github.com/micheles/decorator/blob/5.3.2/CHANGES.md) |
| PyYAML | 6.0.3 → 6.0.4 | ≥3.10 | Transitive tooling dependency, including pre-commit. Fixes merge-key expansion and updates libyaml in wheels. [Release notes](https://github.com/yaml/pyyaml/releases/tag/6.0.4) |
| virtualenv | 21.15.9 → 21.15.11 | ≥3.9 | Transitive pre-commit dependency. Includes 21.15.10's POSIX creator/cache changes and restores the copied-CPython path check before clearing. [Release notes](https://virtualenv.pypa.io/en/21.15.11/changelog.html#release-21-15-11) |

Retained the latest patches in the approved families, CPython **3.14.10** for
`>=3.14,<3.15` and standalone **3.12.16** for XPPython3's `>=3.12,<3.13`
reference. Upstream **3.15.2** is outside both selections. The actual simulator
owns its interpreter. [Python release index](https://www.python.org/downloads/)

Retained uv **0.13.9** (CI and observed local execution, floor **>=0.13.5**)
and uv_build **0.13.9** (root and example isolated builds and the standalone
baseline tooling group). Retained Ruff **0.17.6**, ty **0.0.107** and pre-commit
**4.7.0**. Development tools and the local example remain in their existing
groups. Reviewed the owning lock/exact sync and isolated backend boundaries.
[uv release](https://github.com/astral-sh/uv/releases/tag/0.13.9) ·
[uv lock and sync documentation](https://docs.astral.sh/uv/concepts/projects/sync/) ·
[uv build backend documentation](https://docs.astral.sh/uv/concepts/build-backend/)

The latest released Actions and bundled components match the checked exact
source pins. The project's Codex/Claude catalog source and OpenCode pins still
select the same component revisions. Backplane remains disabled. The checkout
publishes the starter and has no adopter template to migrate. Native host
executables are host-managed. No installed component refresh was due.

| Surface | Retained release | Exact source |
| --- | --- | --- |
| [actions/checkout](https://github.com/actions/checkout/releases/tag/v7.0.1) | v7.0.1 | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| [astral-sh/setup-uv](https://github.com/astral-sh/setup-uv/releases/tag/v10.4.0) | v10.4.0 | `1db35dd8eee11c5894872e0b383ae6c406cf738d` |
| [Superpowers](https://github.com/obra/superpowers/releases/tag/v7.0.2) | v7.0.2 | `22f0b463e7a5e579904dd6211a520321035526f7` |
| [gz-skills](https://github.com/tvproductions/gz-skills/releases/tag/v0.13.0) | v0.13.0 | `0bdab63fc503c6b36e2dd487932689b4e555e41a` |
| [Backplane](https://github.com/tvproductions/superpowers-backplane/releases/tag/v0.3.0) | v0.3.0 | `39fbe3065c16ac119c4c10a3c2428fda39d57e61` |

Python 3.14's deferred annotations let a wrapper survive definition-time type
references that resolve later. The decorator update makes that behavior relevant
to compatibility checking. Source annotation conventions and runtime policy
stay in place. No application source change is needed for this tool-only update.
[Python 3.14 annotation changes](https://docs.python.org/3.14/whatsnew/3.14.html#pep-649-pep-749-deferred-evaluation-of-annotations)

## Local results

- In each baseline, `uv lock --upgrade`, `uv sync --locked --all-groups`, a
  second `uv lock --upgrade` and `uv lock --check` succeeded. Repeat lockfile
  hashes matched and `uv pip list --outdated --format json` returned `[]`.
  Sources, dependency edges, group placement and package sets were preserved.
  Lock changes comprise the five package resolutions and local metadata for
  coverage and the starter version mirror.
  Final SHA-256 values are `4e0437213e3869d8cae36558cce02323d32558a9a0bba4b45a4a9ea0665c8f4f`
  for root `uv.lock` and `59603d9e68274ce50dc26b28da0a33228fb3d02cefaaea78651bb0587ee3586c`
  for `baselines/xplane/uv.lock`.
- Both `pip-audit` runs passed on separate fully hashed exports from
  `uv export --locked --all-groups --no-emit-local`. Each audited 75 registry
  packages with zero known vulnerabilities and zero skips. The auditor used
  `--require-hashes --no-deps --disable-pip` and reported its generic flag advice.
- All four routine hooks and 29 checker CLI tests passed on macOS arm64. The
  branch-enabled coverage run passed all 95 tests and reported 90% combined
  statement and branch coverage for `src/skills_first_starter`. Standalone
  X-Plane Ruff, ty and unittest controls passed under managed Python 3.12.16.
- `uv run --locked gz-starter validate` verified both catalogs and component
  pins. `gz-starter version`, the source and packaged bundle, `pyproject.toml`
  and root lock agree at 0.11.5. `uv build --no-sources` and
  `uv run --locked python tools/verify_distribution.py` passed the isolated
  sdist-to-wheel build, archive/resource checks and installed CLI and example
  verification. Diff whitespace and added local references passed.

### Changed-tool controls

Disposable fixtures passed on both exact managed interpreters. Coverage loaded
a BOM-prefixed config, measured a unittest's partial branch, combined the
parallel data and reported the exact covered/missing counts. The decorator
fixture exercised stacked wrappers, a callable generated from an annotated
signature and preservation of annotations on an existing function. The 3.14
fixture also checked deferred annotations. Cosmic Ray listed 213 operators
under both interpreters. Both PyYAML safe loaders applied a mapping merge and
rejected an unknown tag. Requests resolved certifi's bundle and Python loaded
it into a hostname-checking TLS context. Both virtualenv's default creator and
its copied stdlib `venv` creator seeded pip 26.3 offline. A missing option
value returned an error and created no environment.

The initial disposable assertions expected generated return-annotation
introspection and older coverage CLI wording. The final checks exercise the
upstream callable fix and verify coverage data files and JSON branch counts.
Repository tests, rules and thresholds remain intact.

## Verification boundaries

The candidate remains unpublished. Exact-candidate hosted CI and release
acceptance are pending. Local testing covers macOS arm64 and the standalone
X-Plane environment. Qualification remains open for the actual XPPython3
runtime, other platforms and fresh native discovery. Cognitive integration
remains **DEFERRED / measurement UNKNOWN**, with ceiling 15 and adopter-owned
cohesion. Revisit those evidence boundaries during the applicable release,
host or shared-engine qualification work.
