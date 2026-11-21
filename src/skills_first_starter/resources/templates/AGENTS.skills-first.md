# Skills-first development stack

Read the project's `AGENTS.md` and linked authorities first. Preserve its
domain rules, decisions, verification commands and app architecture. These
starter requirements are mandatory. Execute the owning workflow and checks,
record evidence, and report unmet requirements and policy-approved exceptions.
Preserve failing results. Verify installed revisions and discovery separately
from configuration.

**Resolve starter references from the source, version and exact SHA in
`.skills-first/bundle.lock.json`.** Read the named `docs/` sections in that
reviewed starter checkout, or use a project-owned reconciliation with recorded
provenance. If the governing source is unavailable, report the gap and leave
dependent decisions unresolved. Recognize **GZ Starter**, **starter** and
**starter template** as shorthand for `gz-starter`. Preserve canonical IDs in
commands and provenance. Route “update the starter” or “check the starter
template” through `update-gz-template` or `docs/updating.md` in the corresponding
update or review mode. Clarify only if the reference is ambiguous.

**Dependency maintenance MUST complete migration to the latest stable versions
of every in-scope dependency and tool, including new families.** Bare
`gzs-update-dependencies` is update mode. Review-only requires an explicit check,
assessment or no-changes request. Preserve the approved Python families,
product contracts, thresholds and evidenced exceptions in
`docs/baseline-policy.md#dependency-maintenance-means-completed-migration`.
At session start, do one bounded freshness check against official sources using
applicable recent dated evidence, flag stale or unavailable results, and migrate
only in separately authorized maintenance. Follow
`docs/engineering/verification-policy.md#session-start-freshness-is-a-check`.

## Work and verify

**Starter is the outer loop, SP is the inner loop, and gz-skills is supplemental.**
Starter frames objective, authorized scope, requirements and completion. Use
SP's `using-superpowers` for development within those boundaries, gz-skills
`gzs-router` for distinct supplemental engineering needs, and project-owned
skills for project operations. Confirm actual plugin discovery before invoking
upstream workflows. Read
`docs/architecture.md#outer-loop-inner-loop-and-supplemental-disciplines`.
The starter owns only `update-gz-template`, its helper, configuration, provenance
and policy. Keep generic workflows and skills upstream.

Use direct `git` and `gh` commands. Use Python for substantive processing through
`uv run --locked python`, honoring the exact managed pin and supported uv.
Follow SP verification-before-completion and
`docs/engineering/verification-policy.md`. Run each selected command in full,
freshly, for changed behavior and affected consumers. Keep full checks for
broad/uncertain changes, verification or dependency/workspace changes, and
integration/release checkpoints. Keep affected/focused hook checks and full
checks runnable. Add tests for meaningful defects at the owning seam. Review
diff and references for documentation-only changes and use relevant changed-file,
existing test and invented rendered checks for bounded presentation changes.
Cite dated, input-matched historical evidence as such. Repeat affected checks
when inputs or risk change and record scope and limits.

## Adoption, decisions and native scope

This starter supports Python only, in both lite and heavy lanes. At adoption,
select an explicit lane through the pinned gz-skills setup workflow. Missing
or null selection leaves adoption incomplete. Both lanes require the same
applicable Python baseline, SemVer, major-release PRDs and adoption/release
analysis. Follow `docs/adoption-0.5.md` for greenfield adoption, brownfield
first adoption, structural backport or upgrades. Backplane owns requirements tracking, labeling,
release/backlog monitoring, handoffs and lane definitions. Read
https://github.com/tvproductions/superpowers-backplane/blob/main/docs/superpowers-backplane/modes.md
when selecting a lane. Heavy targets SP, Backplane and gz-skills. Keep Backplane
disabled pending readiness and explicit adoption, report that gap, and preserve
existing planning and handoff authority without creating a ledger or gzkit
lifecycle.

During design, execution and review in either lane, follow the
[identified ADR policy]({{ADR_POLICY_WORKING_SOURCE}}). Preserve its
[immutable canonical source]({{ADR_POLICY_CANONICAL_URL}}) and the version, full
SHA, content hash and link/local choice in `.skills-first/bundle.lock.json`.
Honor the selected working copy, preserve local adaptations and report source
conflicts. Identify and retain the project's existing ADR collection and reuse
approved entries. Obtain separate explicit human approval of the exact new or
replacement edition before dependent implementation. Continue independent
authorized work. Keep approval evidence and edition history with the ADR.
General spec, plan, test or release approval does not approve an ADR. Use the
selected gz-skills `gzs-architectural-decisions` procedure only after verifying
its source and actual discovery. Follow `docs/adoption.md#architectural-decision-policy-access`
during ADR policy adoption or reconciliation.

Install and activate only at repository/project scope. Keep installation,
version updates and activation separate. Preserve user defaults and installs,
suppress inherited duplicates in project config, and report unsupported scope
without broadening activation. A shared cache grants no activation authority.
Before adoption, brownfield repair or updates, follow
`docs/adoption.md#repository-owned-installation-and-brownfield-repair` and
`docs/adoption.md#updates-and-rollback`. Preview, review and apply `localize` for
activation repair. Use `configure --host` for full adoption. Verify installed
revisions and enablement separately, including the outside-project control.
Codex CLI 0.166.0 `plugin add` enables user-wide. Do not use it for project
installation, updates or reinstalls. For OpenCode 2.2.0 project
commands, use the reviewed starter's `uv run --locked gz-starter run-opencode
--project <root> -- <native arguments>`. Read `docs/adoption.md#opencode` for its
scope and actual discovery checks.

## Python baseline and configuration

Use uv-managed Python N-1 (currently 3.14.x) and the 3.12.x XPPython3 host
exception. Verify the latest compatible patch in the approved family against
official sources at setup/adoption, release preparation and maintenance. Pin it
exactly in `.python-version` and CI. Test the embedded runtime separately.
Follow `docs/baseline-policy.md#allowed-python-families`. Keep uv compatibility
minimum-only, record CI's exact tested uv separately, and let supported callers
use their actual version with recorded provenance. Keep exact package/backend
locks and the Python pin independent of the uv executable floor. Follow
`docs/baseline-policy.md#uv-executable-compatibility`.

For Python work read `docs/engineering/python.md`. Meet
`docs/engineering/astral-alignment.md` and complete
`docs/engineering/astral-acceptance.md` at adoption and affected reconciliation,
using its worked migrations. Use `src/` packaging, uv_build for pure Python,
installed imports, entry points for apps and `py.typed` for typed libraries.
Centralize shared settings in root `pyproject.toml`, commit `uv.lock` and ignore
`.venv`. For multi-package work, apply
`docs/engineering/astral-alignment.md#workspaces` before changing workspace
structure. Use one root lock/environment and explicit member edges. Require an
explicit boundary for independent host/runtime environments. Reconcile
nonconforming layout and settings while preserving behavior, data and authorities.
Configuration-only work reports remaining refactoring. Verify effective
configuration, tool/runtime provenance, exact environments, and source-independent
builds and clean installed behavior. Record configuration, Python acceptance
and native discovery separately. Evidenced departures need an owner and revisit.

At adoption and when defining or changing a product's deployment or
configuration boundary, apply ADR-0002, `docs/project-configuration.md` and
`docs/engineering/application-foundations.md` in both lanes. Identify the
deployment unit, configuration owner/location, schema, selection/overrides,
permissions, upgrade preservation and any consuming application/host. Use
`settings.json` for operator-managed runtime settings, keep packaging/tool
settings in `pyproject.toml` and pass validated values to domain code. Reject
supplied or resolved paths containing spaces before reading content or writing.
Preserve data and settings during migration and verify actual consumer behavior.
For architectural warnings or naming/layout advice, read
`docs/engineering/application-foundations.md#warnings-and-informed-departures`
and `docs/engineering/naming-and-layout.md`. Record informed departures once,
preserving mandatory requirements and approved ADRs.

Keep routine hooks limited to locked Ruff check/format, ty and unittest through
pre-commit. Never use pytest. Run applicable deeper analyses, including C901,
at adoption, release acceptance and on demand outside routine hooks/CI. Follow
`docs/engineering/python.md#adoptionrelease-analysis-and-on-demand-hygiene` for
the adopter minimum and `docs/engineering/python.md#adopter-class-cohesion-requirement`
for project-owned cohesion pins, runtime proofs and reporting. A required
missing, failed or stale result blocks strict acceptance. Apply
`docs/engineering/cognitive-integration.md#starter-wide-qualification-deferral`.
Record **DEFERRED / measurement UNKNOWN**, retain ceiling 15 and all other checks,
and report conditional acceptance. Missing shared-engine delivery alone neither
blocks progress nor requires an adopter waiver. Revisit at release preparation
and candidate delivery. End the deferral only after independent qualification
and measurement for the actual consumer. Keep Complexipy for defect reproduction.

At adoption, Python-family changes, design, review and scoped maintenance, use
versioned official documentation and
`docs/engineering/python.md#version-aware-design` to assess idioms, stdlib changes
and deprecations. Record concrete benefits, risks and adopt/defer decisions.
For pattern and OS-seam work, use `docs/gz-skills-python.md` to find the selected
gz-skills workflows, including `gzs-cross-platform-python`. Preserve the bound
runtime policy, report missing or conflicting evidence, and verify the actual
host separately.

## Version and maintenance decisions

At requirements intake, planning and change closeout, execute
`docs/versioning.md#required-version-decision-procedure`. PRDs guide majors,
selected work and requirements drive minors, and compatible fixes drive patches.
Every major, including 1.0.0, requires a newly written PRD. Keep the existing
release-scope record and classify the complete pending scope. Derive routine
bumps, reuse a valid target and require a finite initial release. Keep metadata,
runtime, lock and changelog mirrors aligned. Missing required PRD, scope or
version evidence blocks the applicable claim. Report baseline → target,
governing work, compatibility, mirror agreement and publication state. Reserve
`0.0.0` for an unpublished bare scaffold. Set `0.1.0` as soon as original
implementation, tests, docs or configuration is added. Preserve published
versions and tags. Keep app, starter and upstream component versions independent.
Use `docs/versioning.md#classify-compatibility-within-the-selected-scope` for
increment rules and `docs/versioning.md#adopter-provenance-and-upgrades` when
reconciling an older lock or upgrading the starter. Use
`docs/versioning.md#ecosystem-policy-authority-and-consistency` for companion
policy alignment.

Before setup/adoption, release preparation, scoped upgrades or quarterly
maintenance, use `docs/adoption.md#maintaining-the-adopted-stack` and
`docs/baseline-policy.md#dependency-maintenance-means-completed-migration`.
Compare official releases across families, verify compatibility, preserve
project choices, and record exact provenance, rollout/rollback and discovery
evidence. Required stale or unknown freshness blocks adoption and release
acceptance. Keep retained older tools conditional with evidence, owner and
dated revisit. Use `gzs-update-dependencies` for maintenance and
`gzs-dependency-risk-audit` for risk review. For optional separate standard and
X-Plane scans or reviewed update PRs, follow
`docs/baseline-policy.md#scheduled-dependency-scanning`. Automatic merging,
publication and native installation require separate authority.
