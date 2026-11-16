# Roadmap

## Selected 0.11.0 scope — application foundations, November 16, 2026

Published baseline: **0.10.0**, immutable release source
`6b236d87f301f689edae6934dabee9495df726d4`. Pending target: **0.11.0 / minor**,
governed by the maintainer's foundations/house-style design request and
[draft design edition 1](docs/superpowers/specs/2026-11-16-application-foundations-design.md).
Outcome: coherent Python application guidance in both lanes, separate runtime
settings.json, environment/secrets handling, right-sized hexagonal guidance,
operator warnings/overrides and bounded worked verification.

Completed: repository gap review, exact-source GZKit drydock/house-style/hexagonal
comparison, comparison with selected gz-skills criteria, captured settings.json
and operator-authority decisions, draft design and draft ADR-0002 edition 1.
Builder review is complete; its two questions are resolved: keep the broader
Ruff/ty patch deferred, and retain the maintainer-reaffirmed rejection of all
paths containing spaces, including user-selected paths.
Remaining: maintainer design approval, separate identified ADR approval,
policy/instruction/resource reconciliation, applicable starter use and worked
positive/negative verification. Required release freshness and applicable
acceptance remain future gates; cognitive measurement remains deferred/UNKNOWN.

Compatibility: new guidance/default configuration responsibilities require
adopter review; preserve existing settings, interfaces, mandatory engineering
requirements and project choices. No automatic adopter refactoring. Excluded:
GZKit lifecycle/kernel, universal runtime library, upstream edits/releases,
native activation, real-adopter migration, management sidecars and full TUI/web/
desktop qualification. No publication is authorized. Version mirrors are
reconciled to the pending planning target; this does not mark draft behavior
implemented. Reconcile this record at design approval and implementation closeout.

The following 0.10.0 completion record and historical narratives retain their
original dates and are superseded by this new scope where they describe next work.

Reconciled November 15, 2026 for the finite 0.10.0 release, governed by
[#12](https://github.com/tvproductions/gz-starter/issues/12) and approved design
[#13](https://github.com/tvproductions/gz-starter/issues/13). Published baseline
0.9.0 -> 0.10.0 / minor; version mirrors agree. Completed scope includes mandatory
ADR binding and link/local policy access, independently released companion ADR
contributions, targeted both-lane disabled-path qualification, genuine publisher
use/alignment, canonical naming and selected policy/tool maintenance. See the
[release acceptance](docs/evidence/2026-11-15-0.10.0-release.md) and
[combination receipt](docs/evidence/2026-11-15-adr-combination.md).

Compatibility: new mandatory pre-1.0 adoption requirements need reviewed adopter
reconciliation; existing authorities, profiles and Backplane-disabled settings
are preserved. Real-adopter migration/pilot, naming enforcement, management
sidecars, deterministic upgrades, broader platform proof and acceptance automation
remain deferred. Cognitive measurement is UNKNOWN under the standing deferral;
no full strict conformance is claimed. Publication is verified by the immutable
release tag and GitHub record. Historical planning narrative below retains its
original scope/ordering and is superseded by this completion record where stated.

## Delivered baseline

- Immutable bundle, two native marketplace catalogs, independent template
  versioning and exact-SHA adopter provenance. Current selections are SP 7.0.2
  and gz-skills 0.13.0; Backplane 0.3.0 stays pinned and disabled. `bundle.json` owns
  those selections; exact pins do not establish upstream freshness.
- Preview/apply/status configuration, preservation/conflict/symlink/duplicate/gzkit
  checks, unittest coverage and read-only structural backport assessment.
- Python-only lite/full adoption policy, expanded Astral acceptance, explicit
  lane selection, adopter SemVer and new-major PRD rules. These are binding
  review requirements; the helper does not certify conformance.
- One starter-owned `update-gz-template` skill, introduced in 0.6, with canonical
  packaged bytes and protection for adopter edits. Generic engineering and
  maintenance skills remain upstream-owned.
- **0.8.0:** `configure --host codex|claude|opencode`, project-only `localize`
  activation repair, and `run-opencode` for OpenCode 2.2.0's inherited duplicate-ID
  failure. Scope repair preserves adoption records; it is not a version migration.
- macOS CLI/native runtime scope proofs for Codex 0.166.0, Claude Code 2.1.316
  and OpenCode 2.2.0, including inside/outside controls and preserved user
  settings. Claude project installation and OpenCode v2 support are delivered;
  combined-stack Backplane acceptance remains separate and deferred.
- **0.9.0 Windows correction:** normalize discovery identifiers and scope-test
  paths. Public-helper regressions cover all three hosts using Windows path
  semantics; this does not prove fresh-session native discovery on Windows.

See the [0.9.0 release receipt](docs/evidence/2026-11-08-0.9.0-release.md),
[three-host receipt](docs/evidence/2026-10-31-three-host-repo-scope.md),
[changelog](CHANGELOG.md) and [current handoff](docs/handoffs/2026-10-24-session-close.md).
Historical receipts establish their stated inputs and scope, not current
universal acceptance.

## Next work, in recommended order

### House naming and layout — proposal ready for review

The maintainer requested the [dated house-policy draft](docs/engineering/naming-and-layout.md)
and explicitly selected rejection of user-selected paths containing spaces.
The draft supplies all 15 requested naming/layout areas, exact unapplied tool
settings, per-member declaration verification and downstream migration guidance;
see its [bounded evidence](docs/evidence/2026-11-14-naming-layout-proposal.md).
This is minor-level work from published 0.9.0, but its implementation is not yet
selected into pending 0.10.0. Reconcile the bounded scope and obtain required
policy/design/ADR approvals before dependent work. Keep all four routine checks;
remediate findings and prove actual path/declaration/artifact behavior. No
adopter change, chore/skill creation, enforcement activation or release occurs
by saving the draft. The prior sidecar/Backplane review remains pending too.

### Canonical rename selected: gz-starter

November 14 maintainer decision: the canonical project name will be
**gz-starter**, with **GZ Starter** as the display name. Book the coordinated
repository/local-folder and adopter migration as minor-level work in the valid
pending **0.10.0** target from published 0.9.0; do not add a bump per task.
Execution is now authorized and the candidate uses the renamed GitHub repository,
local checkout, distribution and canonical CLI. Compatibility interfaces remain
as documented in `docs/rename-gz-starter.md`. Desktop primary-folder binding is now verified in the current handoff;
downstream adopter propagation remains explicit follow-up work. Keep the earlier ADR/policy
acceptance gates intact; this does not establish release acceptance.

Required completion scope:

- Rename the GitHub repository through `gh`, verify the same repository/history
  and intended new URL, then reconcile local remotes and active source links.
  Preserve immutable tags/releases and historical adoption provenance.
- Coordinate the local folder move and desktop project binding with the
  maintainer. Repair path-dependent environments, launchers and normal hooks;
  verify the managed pinned runtime and clean installed behavior afterward.
- Resolve the package/distribution, Python import, CLI and marketplace identity
  migration explicitly. Prefer consistent canonical naming while defining any
  supported compatibility aliases and retirement boundary before changing them.
  Update owning metadata, locks, catalogs, native project bindings, tests,
  documentation and generated resources coherently; do not edit native caches
  or activate plugins user-wide.
- Record the decision and migration boundary in gz-skills and Backplane. Keep
  their independent names/versions and preserve their existing project policy.
- Inventory authorized downstream adopters and provide a reviewed migration
  path for old source URLs, identifiers/configuration and recorded versions/SHAs.
  Preserve project additions and old immutable source identities. Do not perform
  unrequested blanket changes to downstream repositories.
- Verify preview/migration/recovery, repeat adoption and old-provenance handling,
  both catalogs/resources, source-independent builds, installed commands and
  applicable native project discovery. Observe exact-commit CI and ordinary
  Git alignment. Scope activation, release acceptance and publication separately.

Repository/folder target naming is selected. Exact public identifier/alias
dispositions and the implementation sequence remain to review. This booking
does not implement the rename, publish a release or approve the other draft
record-platform architecture. See the current
[handoff](docs/handoffs/2026-11-14-opinionated-cli-design-discussion.md).

### 1. Establish mandatory ADR practice across the trio

Selected next minor: **0.10.0**, from published 0.9.0. The maintainer agreed
that both lite and heavy adopters must follow this practice, and that this
starter, gz-skills and SP-BP must demonstrate it themselves before propagation.
The [native feature issue](https://github.com/tvproductions/gz-starter/issues/12)
captures the increment's intent, workstreams and acceptance conditions. Detailed
design is tracked as [child issue #13](https://github.com/tvproductions/gz-starter/issues/13).
The maintainer approved the [starter specification](docs/superpowers/specs/2026-11-08-adr-practice-design.md),
the native implementation plan and separately
[ADR-0001-001](docs/decisions/ADR-0001-001-qualify-exact-component-combinations.md).
Starter policy, link/local helper support and packaged-policy verification are
implemented and qualified for the exact released sources and observed Windows
Codex scope in the combination receipt. Each real adopter must reconcile its
authorities and verify its actual installed/discovered sources.
This repository owns the adopter policy
and cross-component contract; gz-skills and SP-BP design their internals in their
own repositories.
Approve each concrete design before dependent implementation; individual new
architectural decisions retain their separate ADR approval checkpoint.
See the [governing scope and discussion record](docs/handoffs/2026-10-24-session-close.md#november-8-agreed-adr-practice-and-next-release-scope)
and the [source proposal's final guidance](https://github.com/wtcis-pvecob/cob_projects/blob/dd1ab883c04e884678ed723959b17c5c364263d1/docs/engineering/proposals/2026-11-07-gz-adr-workflow-discussion.md#final-audience-guidance).

Prevent surprise architectural commitments embedded in implementation. Require
recognition during design, execution and review; reuse applicable approved
choices; obtain separate explicit approval of an identified ADR edition before
implementing a new or replacement choice. Preserve independent record identities,
editorial history and honest approval provenance. Routine details within an
accepted decision need no new ADR. Drafting or indexing does not confer approval.

The starter leads adopted policy for the trio; gz-skills owns portable workflow
and template behavior; SP-BP integrates with its existing planning/tracking
surfaces. Each repository must bind the practice for its own development too.
A central CLI, shared runtime or application core is not a prerequisite. The
starter owns nothing on GZKit's behalf; its drydock and lifecycle remain separate.
Do not introduce a competing planning hierarchy or fork upstream SP workflows.

Completion requires a reviewed concrete design, the three project bindings,
portable workflow and applicable SP-BP integration, plus behavioral positive and
negative controls for missing/conflicting decisions, vague assent, mid-work
choices, accepted-decision reuse and honest backfills. Demonstrate the practice
in all three repositories before adopter propagation. Detailed distribution and
integration remain to be designed; this scope agreement is not implementation
acceptance or approval of an individual ADR.

### 2. Complete an authorized real-adopter pilot

FDAU remains the primary candidate, subject to authorization in that repository.
Exercise adoption and a subsequent template upgrade against real project edits.
Preserve domain code, existing authorities, explicit lane, settings and native
activation scope. Record reviewed source and target versions/SHAs.

Completion requires observed configuration, applicable Python/Astral acceptance,
fresh native discovery, preservation and rollback evidence. Report unresolved
requirements explicitly; successful configuration is insufficient. Feed concrete
pilot findings into the reporting and upgrade proposals below.

### 3. Provide reviewed template upgrade and rollback tooling

The [canonical update workflow](docs/updating.md) exists; deterministic three-way
reconciliation remains proposed. `localize` repairs activation but does not
upgrade adoption provenance or merge changed managed files.

Completion requires original/local/target previews, explicit conflict handling,
coherent reconciliation of managed records/guidance/host settings/update skill,
preserved adopter edits and plugin enablement, and tested rollback. Exercise
public helper seams with invented fixtures and a separately authorized pilot.
Do not install plugins or overwrite user defaults as a migration shortcut.

### 4. Close remaining native/platform proof gaps

Keep completed CLI/runtime scope proofs separate from these open checks:

- Codex desktop picker and model-visible invocation in a fresh project session.
- Windows repository skill-link materialization and fresh native discovery;
  `core.symlinks=false` produced placeholders in the November 1 checkout.
- Other host operating systems and model invocation paths not covered by the
  macOS CLI receipts.

Completion requires exact host/version/source identities, actual invocation or
discovery results, inside/outside controls and preserved user settings for each
claimed target. The [October 18 Windows Codex CLI receipt](docs/evidence/2026-10-18-codex-discovery-verified.md)
proves its published 0.4.0 fixture, not universal current-host readiness.
Test the actual embedded XPPython3 host separately; standalone 3.12 tool probes
do not establish simulator/plugin compatibility.

### 5. Make adoption acceptance independently inspectable

The [strict-adoption design](docs/engineering/strict-adoption-design.md) already
identifies automatic lane/evidence/PRD validation as proposed, not implemented.
Design reporting that distinguishes declared lane, managed configuration,
Python conformance, native discovery and release eligibility. Preserve the
upstream profile schema and existing planning/lifecycle authorities.

Completion requires public-helper positive and negative controls for missing,
failed, stale and inapplicable evidence, explicit exceptions with owner/revisit,
and absence of a lane. Do not infer acceptance from configuration, a profile
string or an installed plugin. Validate major-release PRD requirements without
implementing a competing requirements-tracking system.

The maintainer selected this as the final planned feature before a proper 1.0.0,
after ADR practice, pilot feedback, upgrade/rollback work and platform evidence.
Include applicable architectural-decision approval and alignment evidence;
field presence cannot establish human approval. Existing mandatory adoption
checks remain in force before reporting automation exists. Prepare a newly
written 1.0.0 PRD and finite release scope; this feature alone does not establish
1.0.0 readiness or authorize publication.

## Parallel maintenance: dependency scans and update candidates

The November 7 hosted scans and real update-PR generation passed after the
minimum-only uv correction; the historical failure and recovery evidence is in
the [completed receipt](docs/evidence/2026-11-07-dependabot-uv-compatibility.md#hosted-verification-completed--november-7).
Release 0.9.0 independently refreshed both locks and tested uv 0.13.7; see its
[release receipt](docs/evidence/2026-11-08-0.9.0-release.md). This does not claim
any update PR was merged or all future scan behavior is verified. Preserve the
two Python baselines, exact locks and adopter-owned schedules. Review remaining
PR applicability against the current locks; root build-only updater behavior and
real embedded-host proof remain separate gaps. Plugin/Lizard qualification
follow-ups retain the receipt's explicit ownership and revisit conditions.

## Unscheduled upstream dependencies

### Cognitive engine integration

Tracked as [issue #1](https://github.com/tvproductions/gz-starter/issues/1),
without milestone or promised delivery date. Releases 0.7.1 and 0.8.0 retain the
maintainer's explicit exception. Consumer preparation provides 42 qualification
fixtures, independent source inventory, provenance and ceiling checks; no real
engine is installed or qualified.

On an authorized upstream candidate, qualify the selected CPython AST approach
at ceiling 15, including keyword conditionals and functions under module-level
loops/match. Preserve public contracts, fail-closed discovery, historical failing
evidence and upstream ownership. Complete the issue's corpus/qualification proof
before removing the exception. Leave gzkit untouched; create no extraction
project, private scorer or incidental plugin installation. See the
[integration boundary](docs/engineering/cognitive-integration.md) and
[extraction assessment](docs/evidence/2026-10-24-gzkit-cognitive-extraction.md).

### Backplane readiness

Keep SP-BP disabled until readiness and explicit adoption are established.
Require upstream host/adapter acceptance and reviewed combined-stack evidence
before claiming support. Existing Claude/OpenCode SP + gz-skills support does
not depend on that future acceptance. Backplane owns requirements tracking,
labels, backlog/release monitoring, handoffs and lite/heavy definitions; do not
duplicate those lifecycles here.

The 0.8.0 receipt assigns November 7 revisit dates to the cognitive/reproducer
exceptions and Backplane readiness. That review remains due; this documentation
reconciliation does not renew exceptions or establish upstream availability.

## Python engineering follow-up

Delivered: `src/` packaging with uv_build, centralized configuration, locked
execution, reviewed Ruff selection, ty, unittest and pre-commit; expanded
[Astral acceptance](docs/engineering/astral-acceptance.md) and
[worked migrations](docs/engineering/astral-migrations.md). The approved four
routine hooks remain Ruff check/format, ty and unittest. Deeper analysis stays
outside routine hooks and routine CI.

The 0.8.0 receipt records actual C901/Lizard, coverage, Interrogate, Vulture,
Bandit, dependency audit, deptry and Import Linter results with reviewed findings
and scope limits. Do not continue describing all of those checks as unperformed.
Cosmic Ray has bounded runtime/worker controls, not a production mutation score.
Shared/local analysis-utility ownership remains unresolved; cohesion selection
and verification remain adopter-owned.

Use the settled [lizard-functions-v1 contract](docs/engineering/ccc-contract.md)
at function/module/overall ceilings 20/20/20. Syntax/discovery failures fail
closed. Historical complexipy scores are defect-reproduction evidence only;
they do not establish cognitive acceptance. Preserve the
[earlier remediation record](docs/evidence/2026-10-18-complexity-remediation.md)
without presenting its cognitive result as current qualification.

Reusable Python-version idiom/stdlib review and generic dependency maintenance
belong to gz-skills. The selected Pythonic-pattern workflows are not a complete
version audit; record that coverage gap and review a released upstream workflow
before adding routing. Do not create a local maintenance skill or freshness
reporter. Refresh release-specific evidence for actual candidate inputs rather
than treating old measurements or exact pins as current acceptance.

## Later extensions requiring separate design

- Language/environment and CLI/TUI/web/desktop support matrices. Current template
  support remains Python-only; do not derive another language's policy from it.
- Adopter-selected new-project product templates, without a mandatory framework.
- Optional registration of project-owned operational plugins.

No roadmap entry authorizes implementation in an adopting or upstream repository,
plugin installation, GitHub mutation, tag movement or release publication.
