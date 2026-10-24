# GZ skills-first starter

This template currently supports Python projects only, in both lite and
full/heavy lanes. Other languages, likely including Go, are future scope;
do not claim their support or invent their baseline from Python policy.
This is the maintainer's opinionated consistency standard. Future CLI, TUI,
web-app and desktop-app guidance must identify language/environment applicability
and verification; do not generalize one target's proof to all product types.

For adoption into another project, start at
`docs/adoption-workflow.md` and preserve that project's instructions.
For continuation of starter development, read
`docs/handoffs/2026-10-24-0.6.0-release.md`; recheck live state before work.

This repository owns the bundle catalog, adoption helper, native marketplace
adapters, and guidance. Read README.md and docs/architecture.md before changes.
The starter owns one narrowly scoped skill, `update-gz-template`, for canonical
template updates. This user-directed exception replaces the zero-authored-skills
rule; generic engineering and dependency maintenance remain upstream-owned.
Keep all other workflow skills upstream- or project-owned; read
`docs/structure.md` and `docs/updating.md` for the ownership/update contract.
`docs/baseline-policy.md` owns adopter version-range and selection policy;
checkout pins record tested execution choices. Distinguish policy changes from
pin refreshes in release notes and adopter reviews.
This is a public scaffold; use invented fixtures and preserve upstream ownership.

Version the template independently of its upstream components and adopter apps.
Read `docs/versioning.md`; `bundle.json` owns `template_version`, mirrored by
the starter's `pyproject.toml`. New adoption records version plus exact SHA.
For this starter and adopters, every major release, including 1.0.0, requires a
newly written PRD. Bundle related changes into minor releases using existing
backlog authority; SP-BP is intended
to assist after readiness and explicit adoption. Patches remain compatible fixes
and clarifications. See the versioning policy for the 0.x compatibility rules.
Keep `CHANGELOG.md` current for release preparation, preserve historical evidence
and never move published tags. Template edits or ordinary Git sync do not imply
tag or release publication.

SP, SP-BP, and gz-skills are independent components. FDAU is the primary design
precedent. SP-BP is an expected addition to the target stack, currently deferred
until readiness and explicit adoption are established. Keep existing backlog
and handoff authority. Do not vendor upstream skills, introduce a gzkit lifecycle,
or infer app domain rules from another adopting project. App operational skills and
supporting domain code remain project-owned.

For Python work, read `docs/engineering/python.md`. Non-gzkit projects
must follow `docs/engineering/astral-alignment.md`: maximal Astral conformance,
`src/` packaging, uv_build for pure Python, centralized pyproject configuration,
locked uv execution and installed-artifact verification. Adopters must refactor
nonconforming structure/configuration; preservation during configuration is not
an exemption. Keep behavior and authorities intact. Compatibility exceptions
need evidence, an owner and revisit condition. Apply this to the starter itself.
Complete `docs/engineering/astral-acceptance.md`, using the worked migrations.
Verify effective configuration, runtime/tool provenance, selected exact environments,
source-independent release builds and clean installed behavior. Track configuration,
Python acceptance and native discovery separately; adopt applicable Astral
recommendations and record evidenced departures. Preserve the routine hook set.
Projects started from this starter require uv-managed, pinned Python 3.14, current clear
Python idioms and suitable stdlib APIs. Consult versioned official documentation
for behavior changes, deprecations and removals; configuration alone does not
supply engineering policy. Keep metadata and tool targets aligned and validate
on the actual pinned interpreter. The documented XPPython3 host exception pins
its supported version and explains the difference.

Baseline Python tooling must use the latest stable release within each explicitly
selected release family, verified at setup/adoption and scoped maintenance. Python's
family is 3.14.x normally and 3.12.x for XPPython3-bound projects; record the
verified patch exactly in `.python-version` and CI, refreshing it during authorized
maintenance. The starter's exact patch is not a permanent adopter requirement.
Inspect/test XPPython3's embedded runtime separately; host limitations require
evidence and a revisit condition rather than an independent runtime replacement.
An installed interpreter satisfying `3.14` is not evidence of freshness. Keep
exact tool pins/locks after verification; family changes require separate review.
Record compatibility exceptions with evidence and a revisit condition. Pass this
rule to adopters through the instructions fragment and Python engineering policy.

Generic dependency maintenance belongs in gz-skills. Route authorized updates to
`gzs-update-dependencies` and dependency-risk reviews to
`gzs-dependency-risk-audit`; keep this starter's material as policy and binding
guidance. Do not add a competing local maintenance skill or generic freshness
reporter. The pinned gz-skills v0.8.0 supplies freshness-only review and
starter/template/plugin inventory through `gzs-update-dependencies`; review mode
leaves pins and environments unchanged. Preserve this starter's approved Python
family and retired-tool decisions over upstream profile defaults.

The routine standard is Ruff check/format, ty, unittest (never pytest), and
pre-commit running those checks. Favor strict, reviewed lint rules. On-demand
hygiene selects Ruff C901 (cyclomatic ceiling 20), complexipy (cognitive ceiling
15), Lizard (cyclomatic scores and aggregates), Interrogate, Vulture, Bandit, branch/statement
coverage through unittest, Cosmic Ray mutation testing, deptry, pip-audit and
Import Linter, plus cohesion as a downstream class-analysis requirement. The
selected on-demand tools form an adopter minimum independent of the helper's
needs; cohesion pins and runtime verification remain adopter-owned. No starter
installation or cohesion compatibility proof is implied. Run applicable deeper
analysis at adoption/release acceptance and on demand, outside routine hooks
and routine CI. Record gaps as UNKNOWN; do not claim strict acceptance with
required missing/failed/stale evidence. Keep the approved routine
pre-commit set limited to Ruff check/format, ty and unittest. C901 is enabled only
in explicit hygiene commands, not routine Ruff selection. The new complexity
policy retires Xenon and Radon. The on-demand `tools/engineering/complexity_check.py` implements
function/module/overall ceilings of 20 under the reviewed `lizard-functions-v1`
contract. Read `docs/engineering/ccc-contract.md`; this is an explicit rebaseline, not exact
Radon equivalence. Syntax/discovery errors fail closed.
Record legacy baselines that may only shrink. Cosmic Ray 8.7.0 has a bounded
Windows/Python 3.14.8 unittest proof; read
`docs/evidence/2026-10-18-cosmic-ray.md` for its baseline exit-code limitation.
Inspect structured worker/test outcomes; exit zero alone is insufficient. The reviewed
routine Ruff selection is E4/E7/E9/F/I/UP/B/SIM/RUF. Ruff, ty and pre-commit are
pinned in dev; complexipy/Lizard/Cosmic Ray remain in hygiene. Utility ownership and
remaining deeper-tool verification remain open. Preserve existing project
authorities while completing required Astral reconciliation.

Validate pins and both catalogs after a bundle change. Use unittest, not pytest.
Test consequential adoption behavior at the public helper seam. Preserve existing
project files, explicit profile choices, and native manager state. A config file
or successful manifest validation cannot prove fresh-session skill discovery.
Report unverified host behavior and Backplane pre-release limitations explicitly.

Checks: `uv sync --locked --all-groups`, `uv run --locked pre-commit run --all-files`,
`uv run --locked skills-first-starter validate`, `uv build`, and
`uv run --locked python tools/verify_distribution.py`. The routine hooks run only
Ruff check/format, ty and unittest. Run the checker CLI tests explicitly after
analyzer changes: `uv run --locked --group hygiene python -m unittest discover -s tools/engineering -p "test_*.py" -v` (eleven contract tests plus the portability regression).
Refresh wheel resource copies with `uv run --locked python tools/package_resources.py`
after changing their five authoritative inputs, including the update skill;
unittest detects drift.
No plugin installation, GitHub issue mutation, tag, or release publication is
implied by editing this repository. Follow the user's actual authorization.

Strong Python/tool preferences belong to this starter and its project binding.
Keep gz-skills and SP agnostic; SP-BP should remain agnostic as well. Do not
propagate these choices into upstream plugins. Review dependency freshness
periodically on demand (at adoption, tool upgrades, and quarterly maintenance),
including runtime/dev tools, the adopted starter revision and pinned SP, SP-BP
and gz-skills releases; distinguish release age
from abandonment. See the Python policy. Do not add review hooks or automatic
schedules, or upgrade dependencies without a scoped request.

When designing features or reviewing dependencies, assess concrete Python 3.14
gains over 3.13 using the Python policy's versioned opportunity guide. Record
benefits, compatibility risks and adopt/defer decisions; do not treat a runtime
pin as sufficient guidance or add machinery without a project need.
