# Dependency-maintenance binding — November 13, 2026

## Authority, source and scope

The maintainer explicitly required the **starter**, for every adopter, to make
dependency maintenance fully migrate to the most current stable versions,
including newer families, rather than review and offer to apply. A product-local
adjustment was rejected. The authorized scope is this bounded starter policy/docs
correction and verification, not a broad starter dependency upgrade, release
publication, external message, plugin/cache change or consumer migration. The
maintainer's follow-up rejects a local-only adjustment: the source correction
is synchronized upstream through the normal main-branch ritual. The final
response records its exact commit, CI and remote alignment. A mandatory callout
at the top of README and maintainer/adopter instructions makes the execution
default visible before the detailed maintenance guidance.

The initial clean development checkout was stale at
`a483e382146c6082e590e31494c07d1812645014`. A live read-only fetch found main seven
commits behind. The complete bounded patch and preliminary receipt were saved
outside the checkout; only that patch was reversed, then main was fast-forwarded
without reset/rebase/force. The correction was reapplied and reconciled against
current base **`dff33ac2f598a1b2f239340318464713df3ad6d3`**, aligned with fetched
origin/main (ahead/behind **0/0**). New ADR work and current 0.10.0 metadata were
preserved. The separate published starter checkout was left untouched.

That base commit identifies the reviewed base only, not the corrected source
commit. The final response identifies the synchronized source; no new template
release or installed-adopter propagation is claimed. The content hashes below identify the policy
candidate; this receipt does not hash itself. The actual last published baseline
is **0.9.0**, immutable tag `v0.9.0` at
**`3f76acf0038b030bf5abd85ce4a419e890d3e420`**.

## Resulting contract

`docs/baseline-policy.md#dependency-maintenance-means-completed-migration` owns
the binding. For the starter and **every adopter, lite and heavy**, maintenance,
update, upgrade and freshen requests fully migrate the requested scope to the
most current stable upstream versions, including newer tool/dependency families,
and complete verification. A bare `gzs-update-dependencies` invocation uses
update mode here, explicitly overriding that portable skill's review-only
default. Do not stop at inventory, recommendation, adopt/defer or an offer to
apply, or seek another permission round for ordinary migration work. Only an
explicit check, freshness review, assessment or no-changes request is review-only.

Migrate affected family constraints, declarations, exact selections, locks,
backends, hooks/CI, commands, configuration and integration together. An old pin
or range, upstream major bump, hypothetical risk or untested compatibility is
not deferral evidence. Preserve required product behavior, Python N-1 and actual
embedded-host limits. A retained older selection requires demonstrated
incompatibility, evidence, accepted-by authority, owner and dated revisit, remains
noncurrent/conditional, and waives no missing/failed/stale acceptance. Preserve
rollback, native installation/activation scope and existing thresholds. A blocked
update or required verification leaves maintenance incomplete.

Reconciled maintainer/adopter instructions, README, baseline and Python policy,
adoption/configuration/structure/architecture guides, workflow mapping, canonical
template-update guide and owned update-skill source. Template-only requests stay
narrow; broader maintenance cannot end after a narrow template assessment.
`tools/package_resources.py` regenerated both changed wheel-resource copies; all
six canonical resources remain consistent. Portable gz-skills/native caches were
not edited or claimed current. No competing maintenance skill/updater was added.
The applicable approved ADR-0001 ownership and independent-version choice is
preserved; no replacement architectural decision or approval event is invented.

## Version and bounded release scope

This changes adopter authorization and completion requirements. It is a policy
change, not a pin refresh or compatible patch-only clarification. Apply the
required version-decision procedure: **published 0.9.0 -> pending 0.10.0 / minor**.
Reuse the valid existing pending target; do not bump once per task. The explicit
maintainer-requested maintenance binding joins the existing mandatory-policy
bundle. The [current handoff](../handoffs/2026-11-08-adr-practice-save-point.md#dependency-maintenance-policy-correction--november-13)
and `docs/versioning.md` record that decision and the source requirement.

Completed added scope: this policy/instruction reconciliation, packaging and
local gate. Remaining scope: the existing ADR companion delivery, shared/targeted
qualification, companion internal use and reviewed distribution. Deferred work
and required release gates remain unchanged. Bundle, package, lock and packaged
bundle keep **0.10.0**; no version-file change is needed. No publication or
adopter propagation follows. Current selected tool/plugin pins, locks and
runtime targets are unchanged from the fetched base; the environment was synced
to that existing lock as required for verification.

## Current candidate verification

Host uv 0.13.6 remains supported. Current-candidate verification explicitly uses
**uv 0.13.8**, resolved through `uv tool run --from uv==0.13.8 uv ...`, as directed.
Inside locked project execution, `shutil.which("uv")` resolves that tool environment
and a nested `uv --version` reports **0.13.8**, so hooks use the same executable.
Managed Python is **3.14.10**, from the checkout's `.venv/bin/python`, matching
`.python-version` and CI. CI's separately tested uv selection is **0.13.7** and
the compatibility floor remains **>=0.13.5**; no project requirement was raised.

Commands below use that uv 0.13.8 prefix; package resources were regenerated with
it. Current policy text/resource and version checks are distinct from the
historical old-base checks below.

| Command after the uv 0.13.8 prefix | Observed result |
| --- | --- |
| `sync --locked --all-groups` | Exit 0; existing 75-package lock synced, including current-base tool refreshes |
| `run --locked pre-commit run --all-files --verbose` | Exit 0; Ruff check, Ruff format, ty and unittest all pass; 72 tests |
| `run --locked skills-first-starter validate` | Exit 0; 0.10.0 bundle and both catalogs valid, Backplane disabled |
| `run --locked python tools/package_resources.py --check` | Exit 0; all six canonical/resource inputs agree |
| `run --locked skills-first-starter version` | Exit 0; 0.10.0 |
| `build --no-sources` | Exit 0; current 0.10.0 source distribution and wheel built |
| `run --locked python tools/verify_distribution.py` | Exit 0; current wheel resources, sdist contents and isolated installed CLI checks pass |
| `git diff --check` (direct git) | Exit 0; no whitespace errors |

Existing adoption/resource/distribution tests cover the changed packaged
instruction surfaces. No new tests mirror this text correction. No analyzer
code/configuration changed; the separate analyzer suite and deeper release
analyses are not rerun for this bounded policy correction.

## Historical checks, not current-candidate acceptance

Before discovering the stale checkout, uv 0.13.6 / managed Python 3.14.10 passed
locked sync, all four hooks, 0.8.0 bundle/catalog validation, source-independent
0.8.0 sdist/wheel build and isolated installed CLI/resource verification. Those
observations apply only to the initial old-base policy candidate. They do not
establish current starter acceptance; the current-base gate above supersedes
them. No old-base artifact is presented as the current candidate.

## Limits and remaining work

This verifies policy/package inputs, not a new dependency freshness inventory,
release acceptance or native adopter behavior. Exact-commit remote CI and
local/remote alignment are reported in the final synchronization response;
release/installed propagation stays separate. Existing adopters consume the
correction through reviewed starter maintenance, not an automatic local override.
Existing cognitive-engine qualification, host/native-readiness and ADR behavioral
qualification gaps remain open. No gate, ceiling or exception is weakened.
No pressure-agent or fresh-session adopter compliance experiment is claimed.

## Reviewed source SHA256 values

| Path | SHA256 |
| --- | --- |
| `AGENTS.md` | `e9432411856b9d4aa82ff843664ed83a335957147bffbb0e69515ef595b0ab0a` |
| `README.md` | `853e28aeb27e422699020f2d6e29cef20a015d0f8e5ee19825404468c3732ec3` |
| `CHANGELOG.md` | `c99b061444ae40a03c9165376cb0b814f7f8729bd077d8610fe7af0f07b95ead` |
| `docs/baseline-policy.md` | `039dcd415a0f09fd5c022106cfd52901dc28ddd18b86ef671eed13de36fbda20` |
| `docs/versioning.md` | `34a3b7b714748d954d931ac4dce72d38183886d41a669cede54a0b7e86812309` |
| `docs/adoption.md` | `747a2c1f69f538d1493a76212bfd295c3964bfbe5ffea342b0d993f5dccdc188` |
| `docs/adoption-workflow.md` | `6d3f122d0e3f23b4d44e17e97918b383beafbb7d10ef1df713ff4ff296eae1e9` |
| `docs/adoption-0.5.md` | `8d06219f1728295017f5805e746a15224f3f6512c5c575b1822db3d24171f8f2` |
| `docs/project-configuration.md` | `82d3195921a9810691a01eb20fc3a12162ddcd1b2c7156b13cb4e3968ff44bdc` |
| `docs/architecture.md` | `de9c9ba95817ae385ac662dd5ab344d56b257c9e641a1ec44024cda30bc742e1` |
| `docs/structure.md` | `c27f70a64ccdb380c0b726ffa587f42103b228a456621263b1b2a0913eb4056c` |
| `docs/updating.md` | `270032bc1669e621d262737be3c1f672ec92cf7c3e109a11f34c1315bfde1f60` |
| `docs/gz-skills-python.md` | `6a599cb8e49189fe743279e062b92d6451e1f5341db89bdc427f09712d3f8c84` |
| `docs/engineering/python.md` | `0831368339d8ae806a03c25e6e4fc94c35509f9b3d69c042fc63eb900bb26316` |
| `docs/engineering/astral-alignment.md` | `cf66a1928aa7f9021cb965ba6dff4dda2a56718aaa93e0d931f4006bd0fba0b3` |
| `docs/handoffs/2026-11-08-adr-practice-save-point.md` | `139a9e9c92a88296fc74b112cb16c03fcd7ed99ea7134fd638dea00add1d1ac8` |
| `templates/AGENTS.skills-first.md` | `e53e9bf8bc46baf4e61696c63796dccc834bd511d2dcc8a68559e2c5be50311b` |
| `templates/skills/update-gz-template/SKILL.md` | `441d9832f65aff0f7d6e3fb6a6a86b2db37069cdbc04a853e25d17b87c598d2e` |
| `src/skills_first_starter/resources/templates/AGENTS.skills-first.md` | `e53e9bf8bc46baf4e61696c63796dccc834bd511d2dcc8a68559e2c5be50311b` |
| `src/skills_first_starter/resources/templates/skills/update-gz-template/SKILL.md` | `441d9832f65aff0f7d6e3fb6a6a86b2db37069cdbc04a853e25d17b87c598d2e` |
