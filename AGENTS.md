# GZ Starter

Read `README.md` and `docs/architecture.md` before making changes. To continue
starter development, start at the current resume point and remaining gates in
`docs/handoffs/2026-11-18-discipline-evaluation-handoff.md` and recheck live
state. To adopt the starter in another project, follow `docs/adoption-workflow.md`
and preserve that project's instructions.

Accept **GZ Starter**, **starter** and **starter template** for `gz-starter`.
Resolve an adopted template by its recorded source, version and exact SHA.
Use canonical repository, package, command and skill identifiers in provenance
and executable instructions.

**Dependency maintenance MUST complete migration to the latest stable versions
of every in-scope dependency and tool, including new families.** A bare
`gzs-update-dependencies` invocation is update mode. Review-only requires an
explicit check, assessment or no-changes request. Apply the Python-family,
product-contract and evidenced-exception rules to this starter and both adopter
lanes. At session start, do one bounded freshness check against official sources,
flag stale or unavailable evidence, and migrate only in separately authorized
maintenance. Read the [completed-migration binding](docs/baseline-policy.md#dependency-maintenance-means-completed-migration)
and [session-start procedure](docs/engineering/verification-policy.md#session-start-freshness-is-a-check).

## Work and verify

Use the native skills selected in `.codex/config.toml`. **Starter is the outer
loop, SP is the inner loop, and gz-skills is supplemental.** Starter frames
objective, scope, requirements and completion. Apply the owning SP development
workflow within that context and use gz-skills for distinct engineering needs.
Keep SP's workflow intact. Follow the [workflow composition](docs/architecture.md#outer-loop-inner-loop-and-supplemental-disciplines)
and [native discovery checks](docs/structure.md#native-development-skills).
Verify actual discovery and report unverified host and Backplane limits.

Adopter instructions are mandatory. Write them with explicit actions, evidence
and completion conditions. Preserve project authorities and settings, report
unmet requirements and evidenced exceptions, and keep failing checks visible.
Use invented fixtures for the public scaffold. Only Python is supported in
lite and heavy. For new product-target guidance, identify the applicable
language/environment, product type and verification. Extend language support
only through its own baseline.

Use direct `git` and `gh` commands for repository and GitHub operations.
Reserve Python for substantive processing and invoke it with
`uv run --locked python` on the exact managed pin and supported uv. Work and
commit on `main` unless the maintainer requests a feature branch. Preserve
unrelated work and normal hooks. Editing grants no authority to install plugins,
mutate GitHub issues, tag or publish.

Follow SP verification-before-completion and the
[verification policy](docs/engineering/verification-policy.md). Run each
selected command in full, freshly, for changed behavior and affected consumers.
Reserve the full gate for broad/uncertain changes and integration/release
checkpoints. Cite dated, input-matched historical results as such and rerun
affected checks when inputs or risk change. Add tests for meaningful defects
at the public seam, including adoption helper behavior. Keep Astral settings
centralized in the root `pyproject.toml`, including workspaces.

- For an integration or release checkpoint, run the
  [starter checkout gates](docs/engineering/verification-policy.md#starter-checkout-gates).
- For analyzer changes, run the [checker CLI suite](docs/engineering/verification-policy.md#starter-checkout-gates)
  explicitly.
- For bundle changes, validate the pins and both catalogs. After changing any of
  the six resource sources, regenerate with
  `uv run --locked python tools/package_resources.py` and check the mirrors.
  See the [resource and catalog checks](docs/engineering/verification-policy.md#starter-checkout-gates).

## Decisions and release scope

During design, execution or review, follow the [ADR policy](docs/engineering/architectural-decisions.md)
in both lanes and reuse applicable approved `docs/decisions/` entries.
Obtain separate explicit approval of the exact new or replacement edition
before dependent implementation. Continue independent authorized work.
Keep approval evidence and edition history with the ADR. General spec, plan,
test or release assent does not approve an ADR. Use the selected gz-skills
procedure/template under the [exact-source qualification](docs/evidence/2026-11-15-adr-combination.md).

At requirements intake, planning and closeout, execute the
[required version decision procedure](docs/versioning.md#required-version-decision-procedure).
Use the existing release-scope authority for the published baseline, proposed
target, governing work, completed/remaining/deferred scope, compatibility and
acceptance evidence. PRDs guide majors, including a newly written PRD for
1.0.0 and every other major. Selected work and requirements drive minors.
Compatible fixes drive patches. Derive routine bumps, reuse a valid pending
target and require a finite first release. Missing required PRD, scope or
version evidence blocks the applicable claim. Report baseline → target,
governing work and verified mirrors. Keep `CHANGELOG.md` current.

`bundle.json` owns the starter's `template_version` and `pyproject.toml`
mirrors it. Record version and exact SHA in new adopter provenance. Keep
template, adopter and component versions independent. Adopters may use
`0.0.0` only for an unpublished bare scaffold. Set `0.1.0` when original
implementation, tests, documentation or configuration is added. Preserve
published versions and immutable tags. For release preparation, read the
[release procedure](docs/versioning.md#preparing-and-publishing-a-release).
For companion policy or release work, run the
[ecosystem consistency check](docs/versioning.md#ecosystem-policy-authority-and-consistency).
This starter is the alignment source for gz-skills and SP-BP. Keep their
workflows tool-agnostic and their release ownership independent.

## Native changes and ownership

Keep installation, version updates and activation separate and project-owned.
Preserve user defaults and installed copies, and suppress inherited duplicates
locally. Use explicit project-scoped operations. Report unsupported repository
scope and leave activation pending. Shared caches grant no activation authority.
For adoption, localize repairs and native updates, follow
[repository-owned installation and brownfield repair](docs/adoption.md#repository-owned-installation-and-brownfield-repair)
and [updates and rollback](docs/adoption.md#updates-and-rollback). Preview,
review and apply `localize` for brownfield activation repair. Verify installed
revisions and enablement separately. Codex 0.166.0 `plugin add` enables
user-wide. Do not use it for project installation, updates or reinstalls.
For OpenCode 2.2.0 project commands, use the
[scoped launcher](docs/adoption.md#opencode)
`uv run --locked gz-starter run-opencode --project <root> -- <args>`.

Read [ownership](docs/structure.md) before changing catalogs, adoption tooling
or skills. The starter owns the catalog, helper, marketplace adapters, guidance
and only the narrow `update-gz-template` skill. Use its
[update contract](docs/updating.md) for adopters. This checkout publishes the
template and never adopts it. Keep generic workflows and skills upstream,
and operational skills and domain code project-owned. FDAU is a design precedent.
Keep Backplane deferred until ready and explicitly adopted. It owns lite/heavy
and the planning, labeling, monitoring and handoff lifecycles. Preserve existing
backlog/handoff authority and avoid a competing ledger or gzkit lifecycle.

## Python baseline and tooling

For Python work, read [Python engineering](docs/engineering/python.md). This
starter and non-gzkit adopters must meet
[Astral alignment](docs/engineering/astral-alignment.md). Use `src/`, uv_build
for pure Python, central metadata and tool settings, locked uv and installed
artifact verification. At adoption or affected reconciliation, complete
[Astral acceptance](docs/engineering/astral-acceptance.md) using the worked
migrations. Reconcile nonconforming adopter layout/settings while preserving
behavior, data and authorities. Record evidence, owner and revisit condition
for exceptions. Keep configuration, Python acceptance and native discovery
separate.

Use uv-managed Python N-1 (currently 3.14.x) and the XPPython3 host exception
(3.12.x). Check exact supported patches against official releases, pin
`.python-version` and CI, and inspect the embedded runtime separately. Follow
[family and patch selection](docs/baseline-policy.md#allowed-python-families).
Use a minimum-only uv requirement, checked in `pyproject.toml`, and record
actual provenance. Allow supported callers independently of CI's selected
version. See [uv executable compatibility](docs/baseline-policy.md#uv-executable-compatibility).
For design or dependency review, assess Python 3.14 opportunities with the
[versioned docs and adoption criteria](docs/engineering/python.md#version-aware-design)
and record concrete benefits, risks and decisions.

Keep the four routine hooks limited to locked Ruff check, Ruff format, ty and
unittest. Never use pytest. Keep C901 (ceiling 20) and deeper tooling outside
routine hooks and CI. For adoption, release acceptance or on-demand analysis, follow
[the deeper-tool requirements](docs/engineering/python.md#adoptionrelease-analysis-and-on-demand-hygiene)
and the [complexity contract](docs/engineering/ccc-contract.md) when measuring
C/C/C. Report required missing, failing or stale evidence explicitly. Keep
cognitive **DEFERRED / measurement UNKNOWN**, ceiling 15 and conditional
acceptance under the [starter-wide deferral](docs/engineering/cognitive-integration.md#starter-wide-qualification-deferral).
Apply it to this starter and both adopter lanes. Missing delivery alone does
not block progress. Adopters own cohesion pins and verification. For mutation work,
inspect structured worker/test outcomes
under [the Python policy](docs/engineering/python.md#complexity-policy-ruff-complexipy-and-lizard).

## Git synchronization ritual

On an authorized Git sync, follow the
[starter Git synchronization procedure](docs/engineering/verification-policy.md#starter-git-synchronization)
even if gz-skills is unavailable. Fetch and review scope before staging. Keep
normal hooks, push ordinarily and verify remote SHA alignment and completed
CI for that exact SHA. Report sync, release acceptance and publication
separately.

## Starter tooling maintenance

Before release preparation, scoped tool upgrades or quarterly maintenance, read
the [starter inventory and receipt procedure](docs/engineering/python.md#periodic-dependency-freshness-review).
Use `gzs-update-dependencies` for maintenance and `gzs-dependency-risk-audit`
for risk review. If unavailable, follow the owning procedure and report the gap.
Check official stable releases across tool families, and retain evidenced
exceptions with an owner and dated revisit. The
[baseline policy](docs/baseline-policy.md) owns adopter ranges. Distinguish
policy changes from checkout pin refreshes in release notes and adopter reviews.
