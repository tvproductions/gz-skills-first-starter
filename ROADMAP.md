# Roadmap

## Selected 0.11.5 scope — dependency maintenance, November 21, 2026

Published baseline **0.11.4**, immutable source
`75f0d83d1b7f4b073d31b06c85cdb20c6ef0cd63` → pending **0.11.5 / patch**.
The maintainer invoked `gzs-update-dependencies` from clean main
`ec5b2f1379c0bcfe46d8850c0b02dcf4ef297dad`. Restore the existing latest-stable
tooling commitment in both baselines with a compatible development-tool refresh.
The scope preserves the public adoption contract, Python families, component
selections and routine hooks. The proposed **0.12.0** bootstrap correction
remains separately approval-gated.

Included: update coverage, certifi, decorator, PyYAML and virtualenv, verify both
locked environments and changed-tool consumers, and reconcile starter version
mirrors and packaged resources. Local acceptance requires repeatable locks,
complete locked security audits and the full integration gate. Record results
and remaining host limits in the
[maintenance receipt](docs/evidence/2026-11-21-dependency-maintenance.md).
Local maintenance is complete. Both exact environments, full gates and
changed-tool controls passed. Each locked audit covered 75 packages with zero
known vulnerabilities and zero skips. Exact-candidate hosted CI and release
acceptance remain pending.
Release acceptance and publication require separate authorization.

The maintainer's `gzs-agent-context-diet` invocation also selects instruction
delivery cleanup for 0.11.5. Shorten the root and generated adopter instructions,
retain the binding requirements, and move conditional details to their owning
policies. Preserve the helper's managed-file contract and regenerate its resource
copy. See the [instruction delivery handoff](docs/handoffs/2026-11-18-discipline-evaluation-handoff.md#november-21-instruction-delivery-cleanup).

The [instruction delivery eval](docs/evidence/2026-11-21-instruction-delivery-evals.md)
adds project-owned evidence for the same patch. It restores the applicability
guard and records fixed comparative cases, deterministic grading and a
bounded native pilot. Broader reliability assessment and exact-candidate hosted
CI remain open.

The Git assertion-order check now replays the saved native traces directly.
Keep this bounded evidence in the same patch and report the unaffected
manual observations separately.

The maintainer requested version bumps for the starter and its upstream context
diet skill. Retain the pending starter patch for the compatible instruction
delivery and evaluation changes. The independently versioned skill and bundle
candidates are `gzs-agent-context-diet` 0.2.0 and `gz-skills` 0.14.0. The
starter patch selects the published `gz-skills` v0.13.0 source. A future
component update requires the upstream release and its own qualification.

## Current review — starter discipline evaluation, November 18, 2026

Completed bounded review of gz-starter and its use/extension of SP and gz-skills against the
maintainer's operating constraint of recurrent model drift. Preserve required
discipline; assess activation, precedence, sustained adherence and truthful
closeout before proposing changes. The
[current handoff](docs/handoffs/2026-11-18-discipline-evaluation-handoff.md)
records the discussion and proposed obligation/evidence audit followed by bounded
behavioral scenarios. The [November 19 evaluation](docs/evidence/2026-11-19-instruction-discipline-evaluation.md)
completes the first source/evidence audit and fresh native discovery checks,
including a separately requested duplicate-source repair. The authorized
[pilot](docs/evidence/2026-11-19-discipline-pilot-results.md) now covers three
cases in each host. The [completed assessment](docs/evidence/2026-11-19-discipline-evaluation-results.md)
adds the five remaining scenario families and fixed positive follow-ups. The
stack has not earned discipline acceptance: repeated locked-Python invocation
violations remain. The runner's trust/delivery, resume-scope and cache preflight errors
are diagnosed and corrected in disposable controls. Functional task results,
violations and setup diagnostics remain separate. The subsequent
[correction follow-up](docs/evidence/2026-11-19-discipline-corrections.md)
completes the sampled adopter link and declared-verification gaps with three
fresh corrective sessions. The maintainer accepted withdrawal of
[ADR-0004 edition 1](docs/superpowers/specs/ADR-0004-001-python-command-control.md):
the proposed enforcement subsystem exceeds the starter's lightweight scope.
The Python invocation requirement and observed failures remain; automatic
enforcement is not selected work. Continue from the evaluation findings through
existing policy, upstream workflows and native capabilities. The maintainer
subsequently selected bounded instruction cleanup: consolidate repeated maintenance
guidance, bind verification scope to SP's fresh-command discipline and separate
current handoff authority from history. This compatible correction is part of
released 0.11.4 below. No new tooling subsystem or broader comparative campaign is
selected. The November 19 maintenance below was published as
0.11.3; the current development target is 0.11.5. The separately approval-gated
bootstrap correction/proposed 0.12.0 below remains open.

## Selected 0.11.4 scope — Codex duplicate-source repair, November 19, 2026

Published baseline **0.11.3**, immutable source
`309c1a204174d802c69fc7e3c4d65ec236abe121` -> released **0.11.4 / patch**.
Governing work: the maintainer's request to fix duplicate Superpowers discovery
found during the continued instruction evaluation. Restore the existing
project-owned activation and inherited-duplicate suppression commitment. The
existing approved native binding and ADR-0001 apply; no new ADR or PRD is needed.
The maintainer's November 20 clarification also requires explicit composition:
starter outer loop, SP inner loop, gz-skills supplemental. Reconcile repository
guidance, the adopter instruction source and its packaged copy under the
[ownership model](docs/architecture.md#outer-loop-inner-loop-and-supplemental-disciplines).
This clarifies existing responsibilities and adds no workflow or public interface;
retain the pending patch target and existing version mirrors.
The maintainer then requested the concrete cleanup identified by the review.
Preserve the prominent maintenance contract in each instruction entry point;
use the existing baseline, Python policy and adopted-stack procedure as the
authoritative detail. Align verification wording with SP and make the current
handoff resume point unambiguous. This is a compatible clarification of existing
requirements and source ownership, not a new workflow or supported interface.

Included: preview/review/apply the project-only `localize --host codex` repair,
preserve selected pins and user defaults, verify fresh discovery from root/src
with an outside cwd control, reconcile metadata/lock/resource mirrors and record
the research/audit and subsequent bounded pilot results. Current official advice informs the evaluation; it
does not change engineering requirements. Completed: the override, idempotent
preview, 15 duplicate pairs removed in fresh native discovery and unchanged user/
other-host settings. The original activation repair passed the full applicable
local gate: all four routine
checks, **95 unittest tests**, catalog/resource/version validation,
source-independent build and isolated installed verification. The November 20
ownership clarification passes 50 affected adoption/native-host tests, resource/
catalog/link checks, a fresh source-independent build and isolated installed
verification. These are dated results for those inputs. The subsequent cleanup
passed a fresh four-hook gate, resource/catalog/reference checks,
source-independent build and isolated installed verification. Root instructions
are 15.6% smaller by bytes and the adopter fragment 8.0% smaller, with requirements
retained through explicit pointers to existing authorities. Included local work
remaining at cleanup closeout: **none**. Model adherence remains unqualified.
The release continuation below records subsequent exact-source hosted CI.
The evaluation retains historical and untested behavior separately from the
actual native discovery evidence. Compatibility: local activation correction;
no component, public interface or adopter policy change.

Excluded: upstream changes, extra hooks,
global activation/uninstallation, comparative behavioral campaign, companion/adopter changes,
and native plugin installation. The subsequent maintainer request “git sync and release 0.11.4”
authorizes ordinary synchronization and publication after the release gates.
Release preparation migrates fresh Ruff 0.17.6/platformdirs 4.14.8 releases in both
Python baselines and setup-uv 10.4.0 in both CI jobs. The
[release receipt](docs/evidence/2026-11-20-0.11.4-release.md) records actual candidate
freshness, compatibility, security, verification and publication state.
**Published and verified November 20:** [0.11.4](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.4)
at immutable source `75f0d83d1b7f4b073d31b06c85cdb20c6ef0cd63`. Both exact-source
CI jobs, annotated remote tag and downloaded tagged-source identity pass.
Included release work remaining: **none**. Conditional engineering limits and the
evaluation's negative discipline result remain; publication does not qualify model adherence.
The proposed bootstrap 0.12.0 remains separately
approval-gated. The [evaluation](docs/evidence/2026-11-19-instruction-discipline-evaluation.md)
owns observed results and the distinction between discovery and model behavior.

## Selected 0.11.3 scope — dependency maintenance, November 19, 2026

Published baseline **0.11.2**, immutable source
`1175433c950d47d5330e4a9a36a986f1a0c6ae26` -> released **0.11.3 / patch**.
**Published and verified November 19:** [0.11.3](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.3)
at immutable source `309c1a204174d802c69fc7e3c4d65ec236abe121`. Both exact-source
CI jobs, annotated remote tag and downloaded tagged-source identity pass.
Included release work remaining: **none**; all excluded work remains open.
The subsequent maintainer request **“release 0.11.3”** authorizes release-specific
preparation, ordinary main commit/push, exact-source CI, immutable annotated tag
and GitHub publication. The
[release receipt](docs/evidence/2026-11-19-0.11.3-release.md) records those gates
and their actual outcome separately from the completed maintenance below.
Governing work: the maintainer's explicit `gzs-update-dependencies` invocation
from clean main `6535e9cd93baca66a21deb8243188db79796508a`. Restore the existing
latest-stable tooling commitment after new upstream releases; add no new product
requirement, policy, supported interface or architectural choice. The proposed
0.12.0 correction remains independently approval-gated, not a selected maintenance
target. Reuse ADR-0001's unchanged component-binding decision.

Included: inventory both Python baselines and all registry dependencies, runtimes,
uv/backend, root-managed example, Actions, components, catalogs and native source
bindings; migrate ty 0.0.105 -> 0.0.107, Import Linter 2.16 -> 2.17 and virtualenv
21.15.8 -> 21.15.9; reconcile locks, version mirrors and packaged bundle.
Acceptance: current official-source evidence, stable repeat resolution, exact
environment sync, empty outdated results, complete locked security audits, the
full repository gate and affected tool positive/negative controls on managed
Python 3.14.10 and independent 3.12.16. Record outcomes and remaining work in the
[candidate receipt](docs/evidence/2026-11-19-dependency-maintenance.md).

Completed locally: both migrations, stable repeat locks, exact environment sync,
empty outdated results, all four routine hooks (**95 unittest tests**) and
**29 checker CLI tests**, complete
75-package security audits per baseline with zero vulnerabilities/skips, catalog/
resource/version checks, source-independent build, isolated installed behavior/
typing and changed-tool positive/negative controls on both exact interpreters.
The [candidate receipt](docs/evidence/2026-11-19-dependency-maintenance.md) and its
machine-readable companion retain inputs, results and bounded platform claims.
Included local maintenance work remaining: **none**. Both exact-candidate hosted
CI jobs passed; current release-specific evidence and conditional acceptance are
recorded in the receipt above. Excluded:
bootstrap implementation/approvals, discipline experiments, unrelated backlog,
policy changes, native installation/activation and companion/adopter writes.
Git sync and publication were excluded from maintenance and are now separately
authorized by the release request. Retain cognitive DEFERRED / measurement UNKNOWN, ceiling
15, adopter-owned cohesion and embedded/platform/native qualification limits.
Compatibility impact: development-tool pin refresh; preserve application behavior,
Python families, routine hooks and project/user activation scope. Release
acceptance/publication requires the current candidate evidence and exact-source
verification recorded above.

## Selected correction — pre-implementation verification, November 17, 2026

The maintainer selected correction of the v0.9.0 adopter bootstrap deadlock:
authoritative pre-runtime verification, a supported executable hook/CI path,
automatic real-test requirements when implementation/tooling appears, concrete
existing-adopter migration and actual Windows/macOS evidence without Node.
Preserve genuine discovery/coverage failures and separate runtime-design approval.

Diagnosis reproduced: managed Python 3.14.10 exits 5 for empty discovery in an
invented documentation/configuration-only checkout. The runbook permits this
stage, but the worked hook runs discovery unconditionally. The
[design edition 2](docs/superpowers/specs/2026-11-17-bootstrap-verification-design.md)
and [ADR-0003 edition 1](docs/decisions/ADR-0003-001-own-bootstrap-verification-in-the-starter.md)
are **drafts awaiting separate approvals**; no dependent implementation exists.
The proposal adds an installed development verification command/extra with owning
tests and reviewed migration, rather than an allow-empty mode or copied helper.
The maintainer endorsed that delivery direction and emphasized the starter's
existing and new owning tests. Preserve producer qualification, adopter artifact
validation and adopter behavior/coverage as distinct obligations. This review
direction does not approve the complete design or separately identified ADR.
Resume that review from the [bootstrap handoff](docs/handoffs/2026-11-17-bootstrap-verification-handoff.md),
including the still-open transition-rule review and actual platform gates.

Version decision at intake: published **0.11.1** -> proposed **0.12.0 / minor**
for the new supported command/dependency/adoption interface. The maintainer has
since selected publication of the completed maintenance as **0.11.2** below;
the proposed minor therefore advances that patch, rather than folding in an
unpublished maintenance checkpoint. Development metadata now records **0.11.3**
for the independent November 19 maintenance;
planning acceptance MUST reconcile all mirrors after design approval, before
implementation/closeout. No completed version reconciliation is claimed yet.

Completed: read-only consumer diagnosis, negative reproduction and reviewable
design/ADR drafts. Remaining: separate approvals, implementation plan, helper/
consumer regression tests, policy/examples/migration reconciliation, installed
proof and actual Windows/macOS execution. Excluded: consumer runtime/adopter
writes, native activation, companion changes, unrelated backlog, Git sync and
publication. Existing cognitive/native/embedded limits remain explicit.
The subsequent “write handoff and git sync” request authorizes saving this
review/maintenance checkpoint on main; it grants no design/ADR approval,
dependent implementation or publication authority.

## Selected 0.11.2 scope — post-release dependency maintenance, November 17, 2026

**Published November 18:** [0.11.2](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.2)
at immutable source `1175433c950d47d5330e4a9a36a986f1a0c6ae26`.
Both exact-source CI jobs, remote annotated tag and downloaded tagged-source
contents are verified in the release receipt below. Included release work
remaining: **none**. The draft correction and all other deferred work stay open.

**Publication authorized November 18:** the maintainer requested “publish 0.11.2”.
This selects ordinary main synchronization, immutable annotated tag and GitHub
release after the required exact-candidate gates. The
[release receipt](docs/evidence/2026-11-18-0.11.2-release.md) records final
acceptance and publication separately. No bootstrap-verifier implementation,
design/ADR approval, native installation or companion/adopter write is selected.

November 18 authorized maintenance follow-through: include the newly released
transitive fixes filelock 4.2.12, platformdirs 4.14.7, python-discovery 1.9.6 and
virtualenv 21.15.8 in both locks under this same compatible patch. The
[new candidate receipt](docs/evidence/2026-11-18-dependency-maintenance.md) records
fresh official inventory, exact environments, security audits and changed-package
controls. Direct tool/backend/runtime/component/Action selections remain current
and unchanged. Native Codex 0.170.0 now reports the selected component revisions;
that observation supersedes the earlier installed-version drift for this host,
without proving all-host discovery or Backplane readiness. No native mutation
was performed. Retain the draft correction's separate approvals/proposed minor,
conditional engineering limits and separate publication authority.

Published baseline: **0.11.1**, immutable source
`041c1989406c1b9c4978042661c2dd38ff1db160`. Released target: **0.11.2 / patch**.
Governing work: the maintainer's explicit `gzs-update-dependencies` invocation
after the clean post-release sync at `0667b3347bfc98cd26179fdc41f820ce67d2a2d2`.
Restore the existing latest-stable tooling commitment after new same-day releases;
introduce no new capability, adoption obligation or architectural choice.

Included: live inventory of both Python baselines, all registry dependencies,
uv/backend, example build backend, Actions, components and native source bindings;
migrate uv/uv_build 0.13.8 -> 0.13.9 and ty 0.0.104 -> 0.0.105; reconcile locks,
CI/reference guidance, version mirrors and packaged bundle. Acceptance requires
stable repeat resolution, exact-environment sync, empty outdated results,
security audits, the full repository gate and affected ty/backend controls.
Record actual results and remaining gates in the
[maintenance receipt](docs/evidence/2026-11-17-post-release-maintenance.md).

Completed locally: all three tool selections, both locked environments,
byte-stable repeat resolution, empty outdated results, 75-package security
audits per baseline with zero known vulnerabilities/skips, all four routine
hooks, catalog/resource/version checks, source-independent build and clean
installed CLI/example typing/preservation checks. Included source/environment
work remaining: **none**. November 18 native inventory matches selected sources;
broader discovery/readiness remains unverified. Exact-candidate hosted CI and
publication verification now pass; no included release gate remains.

Compatibility: execution-pin refresh only; preserve public behavior and uv's
>=0.13.5 caller minimum. No runtime-family migration or new ADR is needed.
Excluded/deferred: native installation/activation, companion/adopter changes,
the broader draft naming-rule patch and all existing roadmap work. Cognitive
DEFERRED / measurement UNKNOWN and native/embedded limits remain explicit.
Maintenance alone did not authorize publication; the later explicit request above
now supplies release authority. Historical receipts retain their original scope.

## Selected 0.11.1 scope — roadmap reconciliation, November 17, 2026

**Published November 17:** [0.11.1](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.1),
source `041c1989406c1b9c4978042661c2dd38ff1db160`. Both exact-source CI jobs,
annotated remote tag and downloaded tagged-source contents are verified in the
[release receipt](docs/evidence/2026-11-17-0.11.1-release.md). The subsequent
maintenance target is recorded above; this section preserves the released scope.

Previous published baseline: **0.11.0**, immutable tag source
`ccac3b5e1ac03f2cf5642d7766aed6e68001997c`. Released target: **0.11.1 / patch**.
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
Ordinary sync, exact-commit CI and immutable tag/release verification completed.

Deferred/excluded: all implementation in the next-work sections, companion or
adopter edits and native activation. Compatibility: prose correction only; no
adopter migration is required. Publication: **verified**;
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
[changelog](CHANGELOG.md) and [current handoff](docs/handoffs/2026-11-18-discipline-evaluation-handoff.md).
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
The [0.11.1 release receipt](docs/evidence/2026-11-17-0.11.1-release.md) refreshes
candidate-specific freshness/security evidence and retains the same-day 0.11.0
maintenance/analysis, including both locks, Lizard 1.26.1 requalification and
actual uv 0.13.8. This does not claim
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
