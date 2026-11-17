# Roadmap

## Selected 0.11.1 scope — roadmap reconciliation, November 17, 2026

Published baseline: **0.11.0**, immutable tag source
`ccac3b5e1ac03f2cf5642d7766aed6e68001997c`. Pending target: **0.11.1 / patch**.
Governing correction: the maintainer requested reconciliation of obsolete
rename/ADR backlog entries after their verified publication. Correct the active
roadmap and continuation pointers without changing the released adoption contract.

Included work: distinguish completed 0.10.0/0.11.0 delivery from remaining
enforcement, real-adopter and platform work; link exact release/qualification
evidence; reconcile changelog and version mirrors. Acceptance requires reviewed
diff/references, consistent version mirrors, catalog/resource checks and the
applicable packaging checks. Record observed results in the current handoff.
No new feature, policy requirement or architectural choice is selected.

Completed locally: reconciliation and version mirrors; reviewed references and
diff; all four routine hooks, catalog/resource/lock checks, source-independent
build and isolated installed-artifact verification. Included implementation work
remaining: **none**. The maintainer subsequently requested “commit, push,
publish”. Candidate-specific freshness/security evidence is refreshed; unchanged
source analysis is retained in the [release receipt](docs/evidence/2026-11-17-0.11.1-release.md).
Complete ordinary sync, exact-commit CI and immutable tag/release verification.

Deferred/excluded: all implementation in the next-work sections, companion or
adopter edits and native activation. Compatibility: prose correction only; no
adopter migration is required. Publication: **authorized, not yet observed**;
no unresolved product decision. No next feature release scope is selected.

## Selected 0.11.0 scope — application foundations, November 16, 2026

**Published November 17:** [0.11.0](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.0),
source ccac3b5e1ac03f2cf5642d7766aed6e68001997c. Exact-source CI passed both
jobs; the annotated remote tag and downloaded source are verified in the release
receipt. The baseline/target accounting below describes this completed increment.

Published baseline: **0.10.0**, immutable release source
`6b236d87f301f689edae6934dabee9495df726d4`. Released target: **0.11.0 / minor**,
governed by the maintainer's foundations/house-style design request and
[approved design edition 3](docs/superpowers/specs/2026-11-16-application-foundations-design.md).
Outcome: coherent Python application guidance in both lanes, separate runtime
settings.json, environment/secrets handling, right-sized hexagonal guidance,
operator warnings/overrides and bounded worked verification.

Completed: repository gap review, exact-source GZKit drydock/house-style/hexagonal
comparison, comparison with selected gz-skills criteria, settings.json and
operator-authority decisions, approved design edition 3 and ADR-0002 edition 2.
Every adopter must identify its deployment/configuration contract; the selected
file location follows project, user, service, host or explicit portable scope.
Edition 1's builder review is complete; its two questions are resolved: keep the broader
Ruff/ty patch deferred, and retain the maintainer-reaffirmed rejection of all
paths containing spaces, including user-selected paths.
Edition 2's focused location/selection builder check found nothing important left.
Edition 3 incorporates Astral's application/library model, packaging and workspace
guidance, distinguishing these from interface and deployment/configuration scope.
A Python web service is an application and normally service/container scope;
portable operation requires a separately explicit relocation contract.
Design edition 3 was approved in the main conversation; the exact draft bytes
and approval context are preserved in the
[continuation handoff](docs/handoffs/2026-11-16-application-foundations-design-handoff.md).
The [implementation plan](docs/superpowers/plans/2026-11-16-application-foundations.md)
is revised with root-owned fixture verification/distribution integration,
pre-read rejection guards and concrete fixture schema/interfaces/commands.
November 17 [dependency maintenance](docs/evidence/2026-11-17-starter-maintenance.md)
updated both baselines; candidate-specific freshness and compatibility evidence
is recorded in the release acceptance receipt below.
The maintainer separately approved ADR-0002 edition 2 on November 17; its exact
reviewed draft and approval context are preserved with that decision. The revised
plan is implemented. Guidance/instructions/resources, starter path rejection
and the worked CLI/library fixture are delivered with **95 owning tests**,
the full gate and clean installed-artifact checks passing. Independent review's
four Important findings were corrected with reached-fault/negative controls;
see the [implementation evidence](docs/evidence/2026-11-17-application-foundations.md).
November 17: the maintainer explicitly requested Git synchronization and release.
Release-specific freshness, deeper analyses, installed typing and the bounded
release-delta review are complete; see the
[0.11.0 acceptance receipt](docs/evidence/2026-11-17-0.11.0-release.md).
Completed: synchronized source, exact-commit CI and verified annotated tag/
GitHub release. No included implementation or publication gate remains.
Cognitive measurement remains
deferred/UNKNOWN under the standing policy.

Compatibility: new guidance/default configuration responsibilities require
adopter review; preserve existing settings, interfaces, mandatory engineering
requirements and project choices. No automatic adopter refactoring. Excluded:
GZKit lifecycle/kernel, universal runtime library, upstream edits/releases,
native activation, real-adopter migration, management sidecars and full TUI/web/
desktop qualification. Publication completed under the November 17 request
after the documented source/CI gates. The receipt records version-mirror checks
for that immutable release.

## Completed 0.10.0 scope — ADR practice and canonical rename

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
release tag and GitHub record. Historical planning/approval narratives remain
in their dated handoffs; they do not reopen completed release gates.

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
[changelog](CHANGELOG.md) and [current handoff](docs/handoffs/2026-11-16-application-foundations-design-handoff.md).
Historical receipts establish their stated inputs and scope, not current
universal acceptance.

### Canonical rename selected: gz-starter

**Completed and published in 0.10.0.** The November 14 decision was executed:
canonical repository/local folder, distribution and CLI are **gz-starter**;
the display name is **GZ Starter**. Desktop primary-folder binding, relocated
environment/hooks, installed command/alias behavior and release-source CI are
recorded in the [release handoff](docs/handoffs/2026-11-15-adr-release-session-handoff.md)
and [release receipt](docs/evidence/2026-11-15-0.10.0-release.md).
The legacy CLI alias, Python import, marketplace identity, record directory and
update-skill ID remain intentional compatibility interfaces; see the
[migration guide](docs/rename-gz-starter.md).

Remaining work is downstream propagation under each adopter's authorization:
inventory its source/version/SHA and local changes, preview reconciliation,
preserve immutable provenance and verify preservation, rollback and discovery.
Include this in the real-adopter pilot below; do not repeat the starter rename
or assume publication migrated existing adopters.

### Mandatory ADR practice across the trio

**Completed and published in 0.10.0.** Governing issues
[#12](https://github.com/tvproductions/gz-starter/issues/12) and
[#13](https://github.com/tvproductions/gz-starter/issues/13) are closed completed.
The approved specification/plan and separately approved ADR-0001 edition 1 led
to mandatory both-lane policy, link/local policy access, preservation/conflict
behavior, independently released gz-skills procedure/template and Backplane
checkpoint integration. Genuine use/alignment in all three publishers and the
source-bound behavioral controls are recorded in the
[exact-combination receipt](docs/evidence/2026-11-15-adr-combination.md).

This completes the bounded trio delivery, not universal adopter/native-host
acceptance or Backplane enablement. Each adopter must reconcile its authorities
and verify actual installed/discovered sources. Reuse applicable approved ADRs;
obtain separate explicit approval of an identified new/replacement edition before
dependent implementation. Do not request completed design/ADR approvals again.

## Next work, in recommended order

These items remain unselected implementation work; the 0.11.1 documentation
correction does not select a feature release or authorize implementation.

### House naming and layout — deferred enforcement

**Guidance and starter path rejection shipped in 0.11.0.** All 15 topics in the
[house policy](docs/engineering/naming-and-layout.md) were reconciled with the
approved foundations design. The helper rejects supplied/resolved spaced paths
before target content access or changes; the CLI/library reference and installed
preservation controls are delivered. See the
[implementation evidence](docs/evidence/2026-11-17-application-foundations.md).

Remaining: the broader November 14 Ruff/ty activation proposal, majority-rule
quota and 14-finding remediation, plus separately reviewed adopter enforcement
and migration. The [original proposal evidence](docs/evidence/2026-11-14-naming-layout-proposal.md)
is historical input, not evidence that these remaining changes are active.
Select a bounded scope before implementation, reuse existing design/ADR approvals
where applicable and obtain approval only for actual new/replacement decisions.
Keep all four routine checks and prove affected declaration/artifact behavior.

### Complete an authorized real-adopter pilot

FDAU remains the primary candidate, subject to authorization in that repository.
Exercise adoption and a subsequent template upgrade against real project edits.
Preserve domain code, existing authorities, explicit lane, settings and native
activation scope. Record reviewed source and target versions/SHAs.

Completion requires observed configuration, applicable Python/Astral acceptance,
fresh native discovery, preservation and rollback evidence. Report unresolved
requirements explicitly; successful configuration is insufficient. Feed concrete
pilot findings into the reporting and upgrade proposals below.

### Provide reviewed template upgrade and rollback tooling

The [canonical update workflow](docs/updating.md) exists; deterministic three-way
reconciliation remains proposed. `localize` repairs activation but does not
upgrade adoption provenance or merge changed managed files.

Completion requires original/local/target previews, explicit conflict handling,
coherent reconciliation of managed records/guidance/host settings/update skill,
preserved adopter edits and plugin enablement, and tested rollback. Exercise
public helper seams with invented fixtures and a separately authorized pilot.
Do not install plugins or overwrite user defaults as a migration shortcut.

### Close remaining native/platform proof gaps

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
The 0.10.0 ADR combination receipt adds its exact Windows Codex observations;
it does not close the broader normal-profile/other-host gaps.
Test the actual embedded XPPython3 host separately; standalone 3.12 tool probes
do not establish simulator/plugin compatibility.

### Make adoption acceptance independently inspectable

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

### Management records and commit metadata — deferred design

The selected JSON-sidecar/Markdown split and minimum commit-contract draft remain
design work in the [November 14 discussion handoff](docs/handoffs/2026-11-14-opinionated-cli-design-discussion.md).
Schema, Backplane mapping, update/recovery behavior and applicable ADR approval
remain unresolved. No sidecar manager, commit schema or hook is implemented by
the rename, ADR-practice or application-foundations releases. Continue through
the existing design authority before dependent implementation; preserve
Backplane's lifecycle ownership.

## Parallel maintenance: dependency scans and update candidates

The November 7 hosted scans and real update-PR generation passed after the
minimum-only uv correction; the historical failure and recovery evidence is in
the [completed receipt](docs/evidence/2026-11-07-dependabot-uv-compatibility.md#hosted-verification-completed--november-7).
The latest completed maintenance and candidate-specific review are recorded in
the [0.11.0 release receipt](docs/evidence/2026-11-17-0.11.0-release.md), including
both locks, Lizard 1.26.1 requalification and actual uv 0.13.8. This does not claim
any update PR was merged or all future scan behavior is verified. Preserve the
two Python baselines, exact locks and adopter-owned schedules. Review remaining
PR applicability against the current locks; root build-only updater behavior and
real embedded-host proof remain separate gaps. Native/plugin qualification
retains the release receipt's explicit scope limits; do not reopen the completed
Lizard scoring-contract requalification as an unperformed check.

## Unscheduled upstream dependencies

### Cognitive engine integration

Tracked as [issue #1](https://github.com/tvproductions/gz-starter/issues/1),
without milestone or promised delivery date. The current starter-wide deferral
applies to this checkout and both adopter lanes: **DEFERRED / measurement UNKNOWN**,
ceiling 15, conditional acceptance without strict-conformance claims. Consumer
preparation provides 42 qualification
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

The current release receipt rechecked component selections and retained the
cognitive deferral and disabled Backplane. Historical revisit dates do not
establish availability or readiness; revisit at release preparation and candidate
delivery, with independent qualification before removing the cognitive deferral.
This reconciliation neither qualifies an engine nor enables Backplane.

## Python engineering policy follow-up

Delivered: `src/` packaging with uv_build, centralized configuration, locked
execution, reviewed Ruff selection, ty, unittest and pre-commit; expanded
[Astral acceptance](docs/engineering/astral-acceptance.md) and
[worked migrations](docs/engineering/astral-migrations.md). The approved four
routine hooks remain Ruff check/format, ty and unittest. Deeper analysis stays
outside routine hooks and routine CI.

The [0.11.0 receipt](docs/evidence/2026-11-17-0.11.0-release.md) records the latest
candidate's C901/Lizard, coverage, Interrogate, Vulture, Bandit, dependency audit,
deptry, Import Linter and installed-typing results with findings and scope limits.
Do not continue describing those completed checks as unperformed.
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
