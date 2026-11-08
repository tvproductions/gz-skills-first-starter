# Roadmap

Reconciled November 8, 2026 against the 0.9.0 release and agreed ADR priority,
current bundle, Windows correction and hosted scan results. This is the starter's
project roadmap, not a replacement for Backplane's backlog/lifecycle authority.
The ADR increment is tracked as [feature #12](https://github.com/tvproductions/gz-skills-first-starter/issues/12)
in [milestone 0.10.0](https://github.com/tvproductions/gz-skills-first-starter/milestone/2).
Cognitive integration remains issue #1. Other entries remain roadmap work
without assigned versions or newly created issues.

## Delivered baseline

- Immutable bundle, two native marketplace catalogs, independent template
  versioning and exact-SHA adopter provenance. Current selections are SP 7.0.1
  and gz-skills 0.8.3; Backplane stays pinned and disabled. `bundle.json` owns
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

### 1. Establish mandatory ADR practice across the trio

Selected next minor: **0.10.0**, from published 0.9.0. The maintainer agreed
that both lite and heavy adopters must follow this practice, and that this
starter, gz-skills and SP-BP must demonstrate it themselves before propagation.
The [native feature issue](https://github.com/tvproductions/gz-skills-first-starter/issues/12)
captures the increment's intent, workstreams and acceptance conditions. Detailed
design is booked as [child issue #13](https://github.com/tvproductions/gz-skills-first-starter/issues/13)
and resumes after the handoff/Git sync. This repository owns the adopter policy
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

Tracked as [issue #1](https://github.com/tvproductions/gz-skills-first-starter/issues/1),
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
