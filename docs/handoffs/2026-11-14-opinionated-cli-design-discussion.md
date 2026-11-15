# Opinionated enforcement CLI — design-discussion handoff

Current continuation: [fresh ADR/release session handoff](2026-11-15-adr-release-session-handoff.md).
Use that resume point; the discussion and checkpoints below remain history.

## Reviewed ADR guidance checkpoint — November 15

The companion plans were approved for Superpowers Native execution. Keep the
upstream term and main-conversation review preference. The maintainer questioned
elapsed time and whether the separately planned CLI had started; it has not.
No CLI naming/design decision or new CLI behavior was added. Avoid another
verification framework, repeated unchanged model matrix or extra maintenance thread.

Reviewed gz-skills source is pushed at `77ad2c792e0df39782271639c317e2c812b5a48e`:
ADR skill/template/router, complete canonical instruction evidence and genuine
approved-decision use/alignment review with no findings. Source/package gates
pass; 0.13.0 is still unreleased because current OpenCode native acceptance is
UNVERIFIED. Catalog refs stay on published 0.12.0; no tag/release or propagation.
Backplane `5904713f47fae21e94813327b4e2daa9878605e3` preserves partial prerequisite
tooling/probe work and owner issue #37; ADR integration/0.3.0 remain pending.

The [release record](../evidence/2026-11-15-0.10.0-release.md#reviewed-guidance-implementation-checkpoint--november-15)
contains exact sources, actual results, remaining gates and registered worktree
paths. Preserve originals and scratch. Starter 0.10.0 remains blocked under the
approved scope; do not claim completion or start the planned CLI. Resume owning
plans from recorded checkpoints, not from the older pre-implementation note below.

## Approved design, plans ready for review — November 15

The maintainer said **“proceed with that design”** after main-thread review of
the remote GZKit naming precedent. Both companion designs and actual separate
ADR approvals are now captured with exact original proposal bytes/provenance.
The [release assessment](../evidence/2026-11-15-0.10.0-release.md#approved-design-continuation-and-implementation-plan-review)
links immutable owner commits, Current decisions, reviewable implementation plans
and the proposed Backplane native intake body. No new work item is posted and no
product skill/integration is implemented yet. Review plans in the main conversation,
using native execution as the recommendation; do not repeat architectural approval
already supplied or infer implementation evidence from the administrative capture.
Then execute the approved plans, independently release both contributions and
complete starter Task 4 qualification before the authorized 0.10.0 publication.
Original dirty companion checkouts and all release/qualification gates remain.

## Review correction — remote naming precedent, November 15

Review designs and architectural decisions in the main conversation; the
maintainer rejected side-question prompts as the place for that review. The
main thread accepted the responsibility split and original gz-skills design,
then requested checking the remote GZKit drydock ADR naming plan. The
[readiness assessment](../evidence/2026-11-15-0.10.0-release.md#main-conversation-review-and-naming-precedent)
records the exact source and comparison. GZKit's ratified H5 uses the same
sequential decision/edition form with minimum-width numbers and its stated slug
grammar. The companion drafts now cite this precedent and propose those precise
details. Continue review here before implementation; do not infer approval of
changed proposal bytes or skip the requested review based on side-question replies.

## Release request checked — November 15, 2026

The maintainer requested publishing the pending release. The
[0.10.0 readiness assessment](../evidence/2026-11-15-0.10.0-release.md) records
the actual candidate, live publication inventory, prepared release-note content
and binding blockers. Current ADR-0001 and the approved #12 scope still require
owning companion ADR deliveries, shared/targeted behavior and internal-use
evidence. Current helper/dependency checks do not supply them. No 0.10.0 tag or
release exists; keep versions/changelog pending. The maintainer explicitly chose
**“Keep approved scope; complete prerequisites.”** Owning companion designs and
ADR proposals are being prepared in clean registered worktrees identified in
the assessment, preserving both original dirty checkouts. Publication authority
is established; missing acceptance and approval of unwritten companion designs/
ADR editions are not inferred from it. No narrower release exception is selected.

## Dependency maintenance follow-up — November 15, 2026

The maintainer invoked `gzs-update-dependencies` after an ordinary Git sync in
this conversation. Update mode selects released gz-skills **0.12.0**, exact
commit `a8f67160475a6995391d2244188d7c38eda65dfb`, replacing 0.11.0. The
[maintenance receipt](../evidence/2026-11-15-starter-maintenance.md) records
live registry/runtime/action checks, compatibility review and verification.
All 76 registry projects are current; Python 3.14.10/3.12.16, uv/uv_build 0.13.8,
SP 7.0.2 and disabled Backplane 0.2.0 stay selected. Both locks are unchanged.
The separate local host-reference environment was synchronized to its existing
lock. Catalog/resource/OpenCode update `1173009eb4484c2dbde2bac672ad4f96b5208438`
is published with both CI jobs passing in
[run 43743537501](https://github.com/tvproductions/gz-starter/actions/runs/43743537501).
Codex/Claude development sources now bind to that exact catalog, preserving
activation/duplicate overrides. Native 0.12.0 installation/loading is not claimed.

Reuse pending **0.10.0 / minor** from published **0.9.0**, under existing #12/#13
scope and ADR-0001-001. Ordinary source sync remains separate from publication;
no tag/release, adopter/companion edit, new profile or native installation is
implied. The naming/layout and record-management proposals below remain drafts,
and their next design-review step is unchanged. Cognitive measurement, ADR/trio
qualification and fresh-session native loading remain unverified/deferred as
recorded. Observe exact final-commit CI and report it in the sync response;
do not create a receipt-only commit chain.

## End-of-day handoff — November 14, 2026

The maintainer requested this handoff and ordinary Git sync, then stopping for
the night. Canonical GitHub repository/local checkout is **gz-starter**. Codex's
project primary path and direct Git top-level were verified to select the same
renamed checkout. Origin is `https://github.com/tvproductions/gz-starter.git`.
The rename, environment repair and desktop binding are complete; the earlier
pending-binding notes below are historical. Retain the compatibility command,
import, marketplace IDs and `.skills-first/` provenance described in the migration
guide. The old directory is only a relocation notice, not another checkout;
clean it up only when no active runtime still needs its original directory.

### First work next session

1. Read this entry, `AGENTS.md` and live Git state. Review the
   [naming/layout policy draft, edition 1](../engineering/naming-and-layout.md),
   [exact unapplied settings patch](../superpowers/specs/2026-11-14-naming-layout-tool-settings.patch)
   and [bounded evidence](../evidence/2026-11-14-naming-layout-proposal.md).
2. Discuss the proposed contract and select its bounded implementation/release
   scope. The maintainer requested preparing a proposal, not activating it.
   Strict rejection of all paths containing spaces, including user-selected
   paths, is an explicit selected requirement for that proposal. Preserve it.
3. Obtain any separately identified architectural ADR approvals before dependent
   implementation. Then plan the selected work. Keep the 14 broader-lint findings,
   declaration-test implementation and real path/platform/artifact checks open;
   measurement and configuration alone are not acceptance.
4. Continue the existing paired starter/Backplane sidecar and commit-record
   design review afterward. Keep all new designs drafts until actually approved.
   Preserve JSON/Git with no SQLite, Dolt or permanent ledger; Backplane owns
   management semantics and Superpowers remains the feature inner loop.

Starter-wide cognitive qualification remains deferred, ceiling 15 retained,
measurement UNKNOWN and eventual shared-engine delivery/qualification required.
The small API/CLI extraction is future work; MCP/plugins stay deferred. Keep four
routine checks, local execution and existing skill ownership. Create no chore,
new skill, ledger, downstream migration, cloud environment, tag or release from
this handoff. The supplied attachment is preserved design input, not active
policy. No adopter or companion source was changed during the proposal work.

### Verified save point and release accounting

Fresh fetch on all three repositories found clean main and 0 ahead / 0 behind:

- Starter: `1a82a026eb337f024508133d28b70396136c000c`; both jobs passed in
  [exact-commit CI](https://github.com/tvproductions/gz-starter/actions/runs/43650651825).
  This is the full saved proposal before the present handoff-only commit.
- gz-skills: `4a7abd79f483c6c9abfc8f9470694be847f1347d`; documented local
  checks pass; hosted CI is not configured. No further edits need a commit.
- Backplane: `c1b63d8f72fba9996f0857120f8c97e9e8d5700d`; previously observed
  [three-platform CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/43647870548)
  passes; no further edits need a commit.

Published 0.9.0 -> pending 0.10.0 / minor is unchanged in bundle/package mirrors.
The proposal's implementation has not been silently added to that release's
approved scope. Reuse a valid pending target when the coherent bundle is selected;
do not bump per pending task. No release has been published by this session.
Current draft SHA-256: policy 7b23a16cffc45053046a1f626949933a4ac44b27a77695738d07dea7fddea301; settings patch a5f1564f2c23cf50d19d2c954f0881cd74432d8a0749e12f00adab8400c05618.
These hashes identify draft bytes and imply no approval.

Verification for this final checkpoint is handoff diff/reference review, version
mirror checks, unchanged unapplied-patch validation and normal hooks. Reuse the
same-input proposal/runtime evidence; observe CI for this handoff commit through
completion after ordinary push. The final sync response records that SHA/result;
avoid another CI-receipt-only commit. Companion repositories remain unchanged.

## Extended session — naming/layout proposal prepared

After the readiness save point, the maintainer answered **“Prepare the proposal
now”** and continued the session. Read the
[draft policy, edition 1](../engineering/naming-and-layout.md),
[exact unapplied tool-settings patch](../superpowers/specs/2026-11-14-naming-layout-tool-settings.patch)
and [bounded source/tool evidence](../evidence/2026-11-14-naming-layout-proposal.md).
The original 15-point attachment remains verbatim in the linked intake. These
artifacts supersede the earlier next-session-only handling, not the current
active engineering policy. No root tool settings, tests, helpers or adopter
files were changed; no release or dependency/native update was performed.

The maintainer explicitly chose **“Reject all paths containing spaces”**,
including user-selected paths, in response to the scope clarification. The
draft requires rejection before target I/O and review of actual path/platform
contracts; do not silently narrow it to project-generated names. This is a
house restriction, not a claimed Python/OS/Astral requirement. Owned schema keys
stay snake_case while external tool/protocol keys keep their real spellings.

The source-backed proposal covers all 15 requested areas. uv workspace/init
pages display November 12, 2026; all Canonical lines record the November 14
review. Root-only Ruff/ty discovery passed positive and negative controls in
both application and library fixtures. The proposed Ruff selection enables
541/815 stable rules, including all 16 naming rules; it finds 14 existing issues,
with zero naming-only findings. ty's explicit proposed stable severities enable
134/151 rules. Per-member deptry passes declared external/sibling imports and
fails when omitted. Its extraction limits require the additional project-owned
unittest contract specified in section 15; that test is not implemented.
Unknown dynamic-import coverage blocks that requirement's acceptance.

A fresh builder review exposed the release-scope decision and an acceptance
ambiguity. The latter is resolved above. The former stays a maintainer choice:
this task authorizes a proposal, not implementation or silently expanding
0.10.0. Recommended bounded implementation scope is all 15 requirements plus
starter policy/resource reconciliation, tool findings, strict paths, declaration
tests and artifact/platform evidence. Downstream edits, chores/new skills,
engine extraction and record-platform implementation are excluded.
Published 0.9.0 -> pending 0.10.0 / minor remains mirrored and unpublished;
reuse that target if the proposed coherent scope is selected. No task-count bump.

Resume by reviewing this policy proposal and selecting its implementation scope,
then any required architectural ADR editions separately. The paired sidecar/
Backplane drafts, cognitive deferral and remaining shared-engine work remain as
recorded, not approved or replaced. The desktop primary path is now verified;
its earlier pending note below is historical. The preceding readiness commit
`54cf1001ba1d7064639575561fe19d83adb79158` has
[passing exact-commit CI](https://github.com/tvproductions/gz-starter/actions/runs/43648751233).
Observe CI for the eventual proposal commit separately, without a receipt-only
commit loop. Only starter docs were edited during this extension; companion
repositories retain the verified migration commits recorded below.

## Ready to resume — primary folder verified November 14

After the maintainer updated the desktop project, `list_projects` reports its
`gz-starter` primary path as the renamed checkout. Direct `pwd` and
`git rev-parse --show-toplevel` agree; origin is the canonical
`https://github.com/tvproductions/gz-starter.git`. Main was clean at
`5845e8fb488f0674636a6c1748e3f0a97e1d8c08`, and a fresh fetch confirmed
0 ahead / 0 behind before this documentation follow-up. This resolves the
primary-folder action left pending in the earlier migration entry. It does not
prove fresh-session plugin discovery. The old path contains only a relocation
notice; remove it only after confirming no active chat/runtime needs its
original working directory.

Verified final migration sync identities, before this resume-note commit:

- Starter `5845e8fb488f0674636a6c1748e3f0a97e1d8c08`:
  [exact-commit CI](https://github.com/tvproductions/gz-starter/actions/runs/43647770059)
  passed both jobs, including the four routine checks, catalogs, build and
  isolated installed aliases, plus the separate X-Plane baseline.
- Backplane `c1b63d8f72fba9996f0857120f8c97e9e8d5700d`:
  [exact-commit CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/43647870548)
  passed on Linux, macOS and Windows; all four normal hooks passed.
- gz-skills `4a7abd79f483c6c9abfc8f9470694be847f1347d`: 32 repository tests
  passed after its final documentation changes; unchanged-source Ruff/format/ty
  and 20-skill validations remain applicable. No hosted workflow is configured.

All three were pushed with matching local/remote main and clean worktrees.
This follow-up changes starter documentation only; do not infer new companion
implementation, native activation, release acceptance or publication.

### Newly supplied naming/layout request

Read the [preserved intake](../superpowers/specs/2026-11-14-naming-layout-policy-intake.md)
before the next design review. It contains the exact 15-point attachment,
its hash, bounded official-source checks, review gaps and its guidance-only
chore idea. Its embedded instructions are proposed work, not activated policy.
Do not treat the supplied old starter name as another repository.

Next session: review the proposed house naming/layout contract and source
attributions; define Ruff/ty configuration propagation and the per-member
undeclared-import check; reconcile existing interface compatibility, path/data
scope, rule inventory and skill ownership. Read every cited primary source and
record checked-on/page dates accurately. Prepare the policy/configuration and
adopter-migration proposal before dependent implementation; obtain an identified
ADR approval separately for any new architectural choice. No adopter changes,
chores, new skill, new hook, expanded rule selection or dependency migration
were performed by this intake. The existing paired sidecar/Backplane designs
remain drafts for subsequent review, not displaced or approved by the new input.

Version decision at intake: new mandatory naming/layout requirements are minor
work under 0.x. Published 0.9.0 -> existing pending 0.10.0 stays unchanged in
bundle/package mirrors. This documentation checkpoint does not expand the
approved implementation bundle; reconcile bounded release scope at planning,
reuse a valid pending target and never bump once per pending task. All earlier
ADR/qualification/maintenance gates and no-release instruction remain intact.

Verification scope: human documentation/intake only; review the diff, original
attachment identity, local references, version mirrors and saved remote/CI
identities. Existing runtime/build evidence is unchanged. Normal hooks remain
enabled; configured hosted CI will verify the final pushed documentation SHA.
Keep Git synchronization distinct from release acceptance/publication.

## Canonical gz-starter migration — November 14 follow-up

The maintainer explicitly chose execution of the rename/migration tonight.
GitHub is now `tvproductions/gz-starter`, verified to retain the same repository
ID and history. The checkout is relocated to `gz-starter`. GZ Starter is the
display name. Pending distribution/CLI is `gz-starter` at **0.10.0**, from
published 0.9.0; no extra per-task version bump or release publication occurs.

The old `skills-first-starter` command remains an equivalent alias. The Python
import `skills_first_starter`, marketplace/plugin IDs and `.skills-first/`
provenance directory remain intentional compatibility interfaces. New source
URLs/provenance use the canonical repository; historical adoption records and
immutable receipts remain intact. Source detection accepts old and new origins.
The update skill remains `update-gz-template`. See the starter's
`docs/rename-gz-starter.md` for reviewed downstream migration guidance; no blanket
downstream edits or native cache/user-scope activation were performed.

The paired designs remain drafts. Their format examples now use
`gz-starter-records/v1` and `gz-starter-commit/v1`, not activated schemas.
Current draft SHA-256: starter 951a78aa9ddfdce7bfe88b38888deafaa0f0bf32d968142e180a47c3029aea61; Backplane f680c70202138c77d34a881f0e081c32f17847b1bf34c9390ad6d0ddd9b8e0e6.
Earlier hashes below identify the pre-rename drafts and remain historical.
No sidecar/ledger/Backplane workflow implementation is authorized by naming work.

The relocated starter environment and four normal hooks were rebuilt from the
same locked dependency selections on Python 3.14.10; the new and legacy commands
both report 0.10.0. The desktop app's primary-folder binding requires the user:
Computer Use cannot control the app, and no project-folder edit API is exposed.
The old folder contains only a temporary relocation notice for the active chat,
not a second checkout. Remove that placeholder after the desktop task/project
has been rebound and no active runtime depends on it.

Companion names, versions and remotes are unchanged. All three repositories must
receive follow-up commits/sync and exact-final CI observation where configured.
No tag/release is authorized. The original wrap-up commits below remain valid
save points, not the final renamed-candidate identities.

Observed rename verification: the existing canonical-source tests first failed
against the old URL/accepted-origin list, then all 72 helper tests passed with
new HTTPS/SSH origins and retained historical origins. GitHub repository ID is
unchanged after `gh repo rename`. Canonical and legacy CLI version output agrees.
All external locked package records are byte-equivalent as parsed; only the
root distribution identity changed. The rebuilt relocated environment uses
managed Python 3.14.10 and the existing lock. Renamed wheel/sdist builds and
isolated installed CLI/resource checks pass. All 207 concrete relative Markdown
targets in the reviewed migration files exist. Normal hooks and exact-final CI
remain required; desktop native discovery is not inferred from these results.

## Evening wrap-up — resume the paired drafts

Latest maintainer authority, November 14: update handoffs and Git sync **all
three** repositories (GZ Starter, gz-skills and Superpowers Backplane), with
normal verification/hooks. Preserve draft status; implement no new design and
publish no release. This supersedes earlier sibling-edit/commit limitations in
the historical entries below. Work remains local; no cloud environment change.

**Canonical naming decision, superseding the earlier short-name-only choice:**
the maintainer explicitly accepted **gz-starter**, requested the GitHub/local
folder rename and coordination across all three projects/downstream adopters,
and asked to get that work booked at least in the starter. **GZ Starter** is the
display name; **starter** and **starter template** remain shorthand. Actual
repository/package/command identities remain unchanged until migration executes.
The [roadmap](../../ROADMAP.md#canonical-rename-selected-gz-starter) books the
required migration and compatibility proof as minor work in pending 0.10.0.
The previously unnamed final item is now this canonical rename decision.

Tonight's original save points are pushed: starter
`454c59643013bd9aea4c5e3f4760ab873b86934e`, Backplane
`5822c6b78acd08d7f90faefaf984f257c625d7a4`, gz-skills
`5fc6cc330e45f40f1b904b6bb2d1ae7214b3dcc5`. Starter exact CI passes in
[run 43645889085](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/43645889085)
and Backplane all-three-platform CI passes in
[run 43646001240](https://github.com/tvproductions/superpowers-backplane/actions/runs/43646001240).
gz-skills has no configured hosted Actions workflows; its documented local
checks pass. A meaningful follow-up save point records the newly selected rename;
its final remote/CI results must be observed separately. Designs remain drafts
and no release has been published. Execution of the actual rename is a separate
scope clarification while booking/synchronization continues.

Resume by reading the
[starter contract draft](../superpowers/specs/2026-11-14-lite-record-and-commit-contract-draft.md)
and the paired Backplane draft at repository `tvproductions/superpowers-backplane`,
`docs/superpowers-backplane/specs/2026-11-14-lite-record-and-commit-alignment-design.md`.
They are draft design slices, not approved implementation specs, plans or ADRs.
The next review is narrative binding, field-level schemas, Backplane mapping
gaps, schema upgrades, migration proof and prospective commit-policy enforcement.
Obtain separate approval of identified ADR editions before dependent work.

Settled direction: JSON sidecars own structured facts; Markdown owns narrative
and generated views; CHANGELOG stays hand-written. Use Git history and bounded
local recovery, with no SQLite, Dolt or permanent ledger. Keep lite and Backplane
semantics aligned, explicit promotion and one owner per field. A typed JSON
commit record is selected direction; the `Starter-Record` spelling, exact model
and integration mechanism remain proposed. Preserve four routine checks.
Superpowers remains the feature inner loop; do no gzkit integration/work.

Cognitive qualification is now a starter-wide documented deferral for both
lanes, with ceiling 15 and eventual qualification intact, measurement UNKNOWN
and no strict-conformance claim. The separate maintained engine project is
selected for future design: small Python API plus CLI, eventual PyPI/uv
distribution, MCP/plugin integration deferred. No engine project is created.

Release accounting remains **0.9.0 -> pending 0.10.0 / minor** for existing
starter policy work; new record-platform behavior is not silently added to that
implementation scope. Backplane stays at published 0.2.0 and gz-skills at
published 0.12.0; their documentation-only save points require no new versions.
Current startup gaps remain explicit: starter selects gz-skills 0.11.0 while
0.12.0 is published; installed/loaded sources differ. Backplane records SP 7.0.1
and older tested tools. Maintenance and native scope repair remain separate.

Verification and exact-commit CI results are recorded with the completed sync;
do not substitute historical green runs or this draft record for actual remote
arrival. Keep final normal hook results and CI links in the sync response rather
than making an endless chain of receipt-only commits.

Observed pre-commit save-point checks: uv 0.13.8 with managed Python 3.14.10;
fresh fetch gives 0/0 main divergence; bundle/catalog and generated-resource
checks pass; `uv build --no-sources` and isolated installed-helper verification
pass. New source-independent artifacts are ignored local outputs, not published
releases. Implementation, analyzer and tool inputs remain unchanged; earlier
Ruff/format/ty passes cover those same inputs. Normal commit hooks and exact-final
CI still supply their required checks. No deeper release acceptance is claimed.

## Resume here: review the design evolution before implementation

The maintainer requested this handoff and ordinary Git synchronization so the
nuanced discussion can continue by voice. Resume with a **design review of where
we have come from**, then resolve the questions below one at a time. Keep
responses short enough to discuss; the maintainer explicitly rejected walls of
text during the adopter review.

First permissible action: read this record, inspect current Git/component state,
and review the existing ownership, architecture and release-design authorities
linked below. Present the direction, material conflicts and next decision without
restarting settled preference questions. Expected result: a reconciled design
boundary and an ordered set of remaining decisions. Then develop the concrete
specification and identified ADR proposal(s). Obtain separate explicit approval
of each identified new/replacement ADR edition before dependent implementation.

This record preserves **user-selected direction**, observations and proposals.
It is not an approved implementation specification, execution plan or ADR.
No new enforcement command, record schema, sidecar, Pydantic dependency, adopter
migration or upstream helper removal has been implemented by this discussion.

## Observed repository and authorization

Observed November 14, 2026, approximately 20:48 UTC. Repository:
`tvproductions/gz-skills-first-starter`; branch `main`, tracking `origin/main`.
Starting HEAD: `1c633f869ad3757961a4f734b0203eb558aaf718`; clean worktree and,
after fetch, ahead/behind 0/0. Work and commit directly on main, preserving hooks.

The current request authorizes this durable handoff, necessary entry-point and
changelog updates, verification, normal commit/push and final-commit CI
observation. It does not authorize implementing the proposed architecture,
editing sibling projects, changing plugin installations, or publishing a release.
The sibling inspections in this session were read-only. Their dirty work and
project authorities were preserved. Private operational material is not copied
into this public scaffold; adopter examples below are generalized audit findings.

Predecessors:

- [ADR-practice save point](2026-11-08-adr-practice-save-point.md): implemented
  link/local policy access, exact-component decisions and outstanding trio proof.
- [Chronological handoff and governing release scope](2026-10-24-session-close.md).
- [November 14 maintenance receipt](../evidence/2026-11-14-starter-maintenance.md):
  actual dependency selections, compatibility results and source/binding commits.

## Why the discussion changed direction

The maintainer reported that many sibling adopters fail to apply the starter's
imperatives. An initial intent audit traced instructions through helper behavior
and acceptance; a subsequent read-only sibling review was conducted one project
at a time at the maintainer's request.

The observations exposed several distinct problems:

1. **Instructions ignored:** one adopter's own feedback recorded direct-CLI
   violations, an agent-granted hook waiver and acknowledged corrections left
   unfinished. Its workflow still wrapped routine Git/GitHub commands in Python.
   The historical waiver was reported by its durable record, not independently
   reconstructed from the original transcript. It correctly declared adoption
   incomplete. More emphatic wording alone does not solve this case.
2. **Policy delivery and unfinished adoption:** another adopter linked to a
   missing former starter engineering skill and had not configured tools its
   own instructions required. The maintainer clarified that expecting the
   standard from the starter is correct: the starter must deliver accessible,
   mandatory policy, and the adopter must implement and verify it.
3. **Unavailable shared infrastructure:** a public adopter, gz-mcp-lsp, correctly
   stopped its G5/T12 acceptance on missing qualified cognitive measurement.
   Its record explicitly forbids substitute scorers and premature T13 acceptance.
   This is compliant behavior exposing a starter-owned dependency gap.
4. **Maintenance/propagation drift:** another adopter had substantial engineering
   evidence and an explicit owner-approved cognitive exception, but remained on
   older adopted policy/tool selections. Distinguish migration work from an
   allegation that the agent ignored requirements introduced after that adoption.

Disposable public-helper probes separately showed `configured` with an unlinked
existing root instructions file, absent lane selection and a nonconforming Python
pin. This fulfills today's configuration-only helper boundary; it does not
establish adoption acceptance. A Claude fixture also retained an existing
CLAUDE.md without importing the starter fragment. Current Claude documentation
describes conditional AGENTS.md loading when CLAUDE.md exists. No actual native
session loading or model behavior was qualified by those file probes.

## User-selected direction to preserve

### Independent procedures; firm starter enforcement

Keep Superpowers, gz-skills, SP-BP and the starter independently owned. The
maintainer favored integration in the starter rather than merging the products.
Superpowers supplies feature methodology. gz-skills supplies the additional
best-practice intent, shape, procedures and evidence expectations. SP-BP supplies
management semantics and heavy capabilities. The starter is the opinionated
integration and deterministic enforcement layer for its adopters.

The maintainer emphasized **total relinquishment of agent preference** on adopting
the starter: its strict architectural and engineering choices must be implemented,
including refactoring nonconforming existing code. Preserve required product
behavior and data during migration; preservation of files is not an exemption.
Lite and heavy both operate **under unapologetic opinion**. The correction from
"until" to "under" was explicit; heavy does not escape starter requirements.

The desired direction is a comprehensive installed starter CLI with focused,
strict enforcement. Its executable rules must be explicit and versioned; do not
have a model interpret skill prose into enforcement at runtime. Deterministic
checks establish the mechanical conditions they actually inspect. Approval and
semantic adequacy still need authentic source evidence and review.

The maintainer favors eschewing consumer-facing enforcement scripts in gz-skills:
keep intent/procedure in the skills and enforcement in the owning installed
tooling. Existing helpers need an inventory, ownership/disposition decision and
compatibility migration before removal. Packaging/distribution tooling is a
separate category. Do not silently delete upstream helpers, create copied
implementations or require the starter for unrelated standalone skill consumers.

Implementation is **100% Python for now**. Go is distant future scope. Introduce
no parallel Go implementation, tooling or speculative abstraction for it. Preserve
the existing approved Python-family/embedded-host distinctions. Do not propagate
starter-specific runtime preferences into unrelated portable consumers.

### Six separate management artifacts

The maintainer selected six readable management artifacts in lite, with a standard
schema, update rules and forward translation into SP-BP. The later sidecar choice
below places structured facts in JSON and narrative/generated views in Markdown.
The responsibilities are:

| Artifact | Owns |
| --- | --- |
| REQUIREMENTS.md | Required outcomes, constraints, stable requirement identities and acceptance criteria |
| BACKLOG.md | Identified work, priority, dependencies and governing requirement/defect references |
| ROADMAP.md | Product direction, capability progression, milestones and explicit deferrals |
| WORK.md | Selected current work, execution progress, blockers, verification and continuation |
| RELEASES.md | Published baseline, bounded next-release scope, target version, SemVer reasoning, acceptance and publication facts |
| CHANGELOG.md | Human-facing, categorized history of notable changes and unreleased changes |

Each fact needs one authoritative home and an explicit update trigger. Keep
requirements approval, work lifecycle, criterion satisfaction, release readiness,
publication authority and actual publication distinct. A completed task, milestone
or green CI run does not itself select a new version or authorize publication.
Trace requirements through work/contributions into bounded release commitments.
The user liked this direction; the exact field schema is not yet settled.

The agent proposed capability-oriented durable requirements with release targeting
owned in RELEASES.md. The maintainer positively received the proposal and asked
for external validation; do not invent a finalized requirement hierarchy or PRD
storage/edition rule from that assent.

**No JSON blocks embedded in Markdown.** The maintainer explicitly rejected that
proposal. The subsequent selected split makes JSON sidecars authoritative for
structured facts and Markdown authoritative for narrative, with generated views
of those facts. CHANGELOG.md remains hand-written. Sidecar granularity, exact
field schemas and narrative binding remain open. Do not independently duplicate
mutable facts across Markdown/JSON.

Pydantic was evaluated as a promising Python schema/validation tool. The
maintainer explicitly accepts Python-centric tooling and wants the best tools
for the job. Exact dependencies, typed-model ownership, parser, supported schema
versions and migration implementation remain design choices, not installed facts.

### Starter-controlled lite-to-heavy and template upgrades

The maintainer favored **approach 1**: lite Markdown authorities migrate explicitly
into SP-BP's native GitHub work identities, lifecycle and relationships in heavy.
Retain Markdown files where useful; archive superseded authorities and leave
clear pointers. Preserve old identities, issue mappings, history, evidence and
unresolved obligations. Verify transfer before retiring the old authority.

The starter must fully manage the adopter-facing transition: reviewed preview,
execution, verification, provenance, record disposition and recovery. This does
not imply competing mutable issue state in the starter. Design the delegation
to SP-BP's existing authorities explicitly.

Ordinary starter sophistication/refinement also needs a supported adopter upgrade
path: recorded adopted source/schema, reviewed target, semantic and file diff,
preserved project additions, coherent reconciliation, verification and recovery.
Starter, application, component and schema identities must remain distinct.

### Lightweight skills, heavy tools; proportionate verification

The maintainer emphasized that adopters bog down in endless repeated tests/QC.
The starter must enforce appropriate scope and avoid growing into gzkit. Preserve
the phrase **lightweight skills, heavy tools**: powerful focused tooling without
an agent runtime, scheduler, new governance lifecycle or per-edit bureaucracy.

Working terminology discussed:

- **Focused:** changed behavior, owning tests and directly affected callers.
- **Member:** a uv workspace member (application or library) plus affected consumers.
- **Integration:** cross-member behavior and the complete applicable workspace/
  repository gate. Deliberately independent uv projects retain their boundaries.

Treat **scope**, **execution occasion** and **isolation** as separate dimensions.
Local edit/debug, member change, PR/main integration, adoption/release/migration
acceptance and on-demand investigation need defined selections. Selecting a
workspace member does not establish dependency isolation; independent installed
artifact proof remains necessary at relevant boundaries.

Proposed enforcement uses declared ownership, dependency relationships, changed
inputs and policy triggers; explain why the chosen checks apply. Unknown ownership
broadens verification. Invalid/empty discovery cannot silently pass; legitimate
pre-implementation applicability needs evidence rather than placeholder tests.
Reuse results while relevant inputs are unchanged, rerun invalidated checks only,
and avoid manually repeating the gate immediately before identical hook work.
Keep the four routine categories and expensive acceptance analysis separate.
Exact selection rules, configuration and CI/on-demand routing remain to design.

## Existing authorities and design review targets

Read these before proposing implementation; reconcile their constraints explicitly:

- [Starter architecture/ownership](../architecture.md),
  [structure](../structure.md), [updating](../updating.md),
  [strict-adoption design](../engineering/strict-adoption-design.md), and
  [verification policy](../engineering/verification-policy.md).
- [Current versioning/release authority](../versioning.md) and
  [approved ADR-0001-001](../decisions/ADR-0001-001-qualify-exact-component-combinations.md).
  Reuse its exact-combination principle where applicable; it is not approval
  of the new enforcement-platform architecture.
- SP-BP's inspected local/current main was
  `05505f8009989eb7514ec62750e33c78bc40abf9`; its published 0.2.0 release is
  `0b18e34e65379e729d8fece97151a1bb8604b461`. The release establishes its
  engineering baseline; broader adoption, external pilot and remaining
  OpenCode work are not qualified by it.
- [SP-BP current governance](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/docs/superpowers-backplane/governance.md)
  and [modes](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/docs/superpowers-backplane/modes.md):
  native issue identity/state/relationships; separate coverage, eligibility,
  acceptance and publication; existing approved project records remain valid.
- [SP-BP November 7 release-doctrine discussion 3](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/docs/superpowers-backplane/specs/2026-11-07-release-doctrine-alignment-design.md):
  relevant existing design, explicitly pending reappraisal/approval/implementation.
  It proposes a portable release-doctrine ownership transfer and starter
  enforcement. Current starter policy still owns the shared release rules;
  no transfer has occurred merely because the draft exists.

The starter CLI currently implements configure, localize, run-opencode, status,
backport, bundle/catalog validate and version. It does **not** implement these
six-file schemas, record-management commands, acceptance enforcement or complete
mode/schema upgrade tooling. Do not present a proposed CLI as already delivered.

## November 14 continuation: cognitive policy decision

The maintainer explicitly instructed in the continuation chat: “Make cognitive
qualification a starter-wide documented deferral until the shared engine is
delivered. Keep the ceiling and eventual qualification requirement, and don’t
claim strict conformance. Then continue the design review.” The maintainer also
identified the near-term need for a new maintained project extracting the engine
from gzkit, ultimately published on PyPI and installable with uv. This paragraph
is an agent transcription of the actual instruction, not ADR approval.

The [current policy](../engineering/cognitive-integration.md#starter-wide-qualification-deferral)
now applies to the starter and both adopter lanes: DEFERRED / measurement UNKNOWN,
ceiling 15 retained, conditional progression without another adopter waiver for
missing shared-engine delivery alone, and no strict-conformance claim. Other
checks and known findings remain mandatory. Delivery triggers independent
qualification and consumer corpus measurement, not automatic acceptance. The
starter maintainer owns the deferral and revisits it at release preparation and
candidate delivery. Existing adopter records require explicit reconciliation.
This supersedes the unresolved cognitive choice below, not historical evidence.

The independent engine is selected direction, not a created repository or an
approved package/API design. Resolve its API/CLI boundary, extraction provenance,
discovery correction, runtime support, maintenance and release contract before
implementation. Preserve the existing independent qualification fixtures. Keep
consumer ceilings, baselines, scope selection and release rules in consumers;
do not pull gzkit lifecycle dependencies into the engine. Inspect live gzkit
source before extraction; the October source observations are historical.

The adopter's release-readiness report adds design inputs: fresh consumer
resolution/installation, separately provisioned tools, actual host use,
distribution-content review, onboarding/support and declared-channel publication
verification. Its PyPI/RTD/Pages choices are product-specific examples, not a
universal hosting mandate or publication authorization here. Distinguish runtime,
consumer, candidate and publication readiness. Reassess versions at work closeout;
do not mechanically increment per backlog item. Concrete shared release schema
and gz-skills contribution changes remain to be designed.

## Remaining design questions, in suggested discussion order

### Continuation constraint: small tool and plugin investigation

The maintainer compared the proposed engine with gz-mcp-lsp: a small, doable
project filling an identified gap. Keep its first scope to extraction, proven
discovery corrections, a usable interface, qualification and distribution; do
not make the broader starter enforcement design a prerequisite. Library plus a
thin CLI was initially the agent's recommendation. The maintainer subsequently
directed: “API plus CLI is sufficient for the first release. Keep the extraction
small and maintainable, defer MCP/plugin integration, and continue the design
review.” This is an agent transcription; it selects the first-release boundary,
not an unwritten API specification or ADR. Leave
thresholds, baselines and release/lifecycle rules with consumers. A plugin, if
selected, must call the same maintained tool rather than duplicate scoring.

Official documentation checked November 14, 2026:

- [Build skills](https://learn.chatgpt.com/docs/build-skills) still supports
  standalone repository/user skills, while recommending plugins for reusable
  distribution. This is a distribution direction, not evidence that all local
  skills were migrated or retired.
- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
  documents root Agent Plugins `plugin.json`/`mcp.json`, OpenAI extensions and
  continued `.codex-plugin/plugin.json` compatibility. gz-skills already has a
  Codex plugin; no new plugin is needed merely to retain its skill packaging.
- [GPT migration](https://learn.chatgpt.com/docs/migrate-custom-gpts#step-1-convert-your-gpt)
  explicitly converts custom GPT instructions into plugin skills. The
  [September 11 release notice](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
  announces that migration direction. These are possible explanations of the
  remembered notice, not confirmation of an account-specific migration.
- [Plugin hooks](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks)
  are documented for manually installed Codex desktop plugins; hook-bearing
  plugins are excluded from the public plugin directory. Do not equate PyPI,
  repository-marketplace availability and public-directory eligibility.
- [Hook coverage](https://learn.chatgpt.com/docs/hooks#tool-coverage) includes
  shell/unified exec, apply_patch, MCP and most local function tools, but excludes
  hosted paths and permits specialized opt-outs. It is not complete enforcement.
  [PreToolUse](https://learn.chatgpt.com/docs/hooks#pretooluse) supports explicit
  denial/exit 2; unsupported decision shapes may report an error and continue.
  Any starter hook adapter therefore needs actual supported-host positive and
  negative tests; installation or skill activation alone cannot prove enforcement.

Local read-only observation: Codex CLI 0.169.0 exposes plugin management. Its
local listing reports enabled starter-marketplace gz-skills 0.10.1 despite the
checkout's selected 0.11.0; the separate 0.12.0 copy is disabled here. It also
reports two enabled Superpowers sources. The remote catalog query failed in the
sandbox, so the listing is local evidence only. Loaded session guidance, desired
configuration, installed revisions and scope remain distinct. No installation,
activation repair or maintenance was performed by this investigation.

Selected engine boundary: independently usable PyPI library/CLI, with MCP and
plugin integration excluded from its first release. A future project-scoped
Codex adapter remains deferred. Plugin schema migration, hook adapters and
public-directory submission remain proposals. This does not defer the broader
starter CLI ownership/record design discussion.

Observed verification for the policy slice: uv 0.13.8 with managed Python
3.14.10; all four existing pre-commit hooks pass (Ruff check/format, ty,
unittest). Bundle/catalog validation and generated-resource parity pass. All
182 concrete relative Markdown file targets across the changed authoritative
documents exist; the two existing ADR template variables remain intentionally
unrendered. Bundle/package/lock/packaged-bundle versions agree at 0.10.0.
No analyzer implementation or threshold changed; no new tests, build/install
replay or cognitive qualification result is claimed. Later handoff-only prose
uses those unchanged-input checks plus diff/reference review. Changes remain
local and uncommitted; no Git sync, release or companion edit was requested.

### Selected structured-record and narrative split

The maintainer explicitly directed: “That split makes sense. Let's use JSON
sidecars for structured facts and Markdown for narrative and generated views.
Keep CHANGELOG hand-written, and continue the design review.” This is an agent
transcription of the continuation chat and selection of the approach, not approval
of a completed specification or an identified ADR edition.

Use sidecars as the authority for structured records associated with
REQUIREMENTS.md, BACKLOG.md, ROADMAP.md, WORK.md and RELEASES.md. Markdown owns
explanatory prose and presents generated views of those records. Each mutable
fact has one authoritative home. Keep CHANGELOG.md manually curated; it does not
need its own sidecar in the initial design. Generated content does not confer
approval, evidence sufficiency or publication authority.

The selected split must preserve the six responsibilities above and avoid
multiple editable copies of status, criteria or release membership. Exact field
ownership, filenames/location, schemas, generated-section markers, editing and
conflict/recovery behavior remain design work. The earlier walkthrough proposed
one sidecar per structured artifact and clearly marked generated sections, but
the maintainer's response does not establish an unwritten storage/API contract.

Continue review with how a normal authorized update changes structured facts
and refreshes their views, how manual edits are reconciled, and how a release
decision is distinguished from task completion. Keep the design independent of
cloud execution; the maintainer selected local work for now. GitHub/local/cloud
coordination was discussed as a possible future Git workflow, with no cloud
environment or settings change authorized.

This continuation records design only. It does not implement schemas, record
commands, rendering or migration and does not expand the pending 0.10.0 release
into the future enforcement platform. Reuse the prior unchanged-input checks;
review this prose diff and references under the verification policy.

### Ledger/storage sidebar and Backplane alignment review

The maintainer raised JSONL event history and SQLite as alternatives to the
selected JSON sidecars, emphasizing a small framework operating in gzkit's
spirit without reproducing its ledger/lifecycle architecture. This was a design
question, not selection of JSONL, SQLite or an event ledger. The maintainer then
clarified that lite may remain a permanent choice and heavy means adopting
Backplane; both representations must stay aligned. Backplane may receive useful
requirement-structure improvements from this joint design. These are agent
summaries of the actual continuation chat, not approval of a specification or
identified ADR edition. Do not label installed plugin presence a mode transition.

Read-only review covered Backplane main
`05505f8009989eb7514ec62750e33c78bc40abf9`; its local worktree was clean and a
direct `gh api repos/tvproductions/superpowers-backplane/commits/main` query
confirmed the same remote revision. Reviewed its AGENTS/session-entry material,
bootstrap design/plan, modes, governance, native issue contract, repository
checkpoint/recovery and checkpoint format. The November 7 release-doctrine
discussion remains a proposal; do not present its authority transfer or new
release-check schema as implemented. No Backplane files, state, issues or native
installation were changed. Recorded SP 7.0.1 there differs from current SP 7.0.2;
this review performs no dependency maintenance or compatibility qualification.

#### Observed Backplane contract

- [Governance ownership](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/docs/superpowers-backplane/governance.md#ownership-and-authority)
  assigns live work scope/state/relationships to native GitHub issues, design and
  execution to approved artifacts, and satisfaction to immutable accepted
  evidence. Heavy is GitHub plus project documents/evidence, not exclusively
  GitHub issue fields.
- Stable requirement/criterion keys carry governing identity, revision and
  wording. Coverage is many-to-many. SATISFIED/UNSATISFIED/UNKNOWN describe
  satisfaction; deferred/excluded describe scope disposition separately. Native
  lifecycle has six open states and distinct completed/not-planned closure.
  Parentage, dependency order and priority have different meanings.
- [Portable checkpoint](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/docs/superpowers-backplane/governance.md#portable-repository-record-and-working-state)
  pairs `.sp-bp/state.md` with `.sp-bp/github-state.json` under
  `sp-bp-checkpoint/v1`. It is a dated read-only capture, not an editable offline
  backlog or event ledger. Do not reuse its capture/pagination schema unchanged
  as the lite source-of-truth schema.
- Capture stages candidate files and a recovery receipt in ignored local work.
  One verified Git commit accepts the exact pair. Filesystem replacement and
  remote capture are explicitly not atomic. Recovery checks ownership and stops
  on intervening edits. This is a directly relevant precedent for bounded
  recovery without an authoritative permanent transaction ledger.
- [Current modes](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/docs/superpowers-backplane/modes.md)
  preserve existing lite authorities and reserve ongoing Backplane management
  for heavy. Turning the starter's six-file proposal into a shared supported
  contract requires explicit reconciliation in Backplane's mode/governance
  authority; today's prose does not already ship that lite implementation.

#### Common meaning and storage boundary — design target

Design a Backplane-owned semantic contract with an explicit lite representation: stable
identities, criterion definitions/revisions, typed relationships, lifecycle
meaning, scope dispositions, exact-input evaluation references and release
scope/authority distinctions. The starter implements its opinionated file-based
binding and enforcement. Keep native GitHub IDs and capture metadata in their
adapters; do not invent native IDs before migration or require a speculative
shared runtime package merely to publish the contract.

| Lite artifact | Heavy correspondent to preserve |
| --- | --- |
| REQUIREMENTS.md + structured records | Approved governing docs/issues, stable statement/criterion keys, revisions and coverage |
| BACKLOG.md + structured records | Native issues, issue-owned bounded scope, parent/dependency relationships and lifecycle |
| ROADMAP.md + structured records | Capability/outcome decomposition, target groupings/milestones and derived views; not inferred execution order |
| WORK.md + structured records | Approved issue-bound plans, actual execution/PR state, evidence and continuation artifacts |
| RELEASES.md + structured records | Selected scope and project-owned release authority, native target grouping and actual release publication; full shared release-doctrine implementation remains pending |
| Hand-written CHANGELOG.md | Remains a repository document with human-facing history |

At explicit promotion, preview the local-to-native identity/relationship mapping,
preserve wording/revisions/approvals/evidence and unresolved scope, verify the
actual transfer, then retire local authority for fields now owned by GitHub.
Remaining Markdown/JSON views become projections/captures where appropriate.
No permanent dual-master synchronization or local ledger is implied. Keep the
mapping/history inspectable. No one-to-one mapping from every Markdown file to
one GitHub object is necessary or desirable.

#### Storage alternatives and evidence

1. **Current-state JSON + Markdown, Git history and bounded local recovery**
   was recommended and subsequently selected below. Validate schemas, cross-record references,
   criterion/evidence applicability and generated views directly. Stage a
   coherent candidate, guard concurrent changes, and use an operation-local
   recovery receipt only as needed. Refuse acceptance of interrupted/partial
   updates; recovery must not overwrite independent edits. Agree exact
   durability, reader/writer and acceptance semantics before implementation.
   Do not require one Git commit or full quality gate for every field edit.
2. **Permanent JSONL event ledger** adds ordering/history if events become the
   authority, but then needs event schemas, replay, projections, evolution and
   merge semantics. If sidecars remain authoritative, a ledger adds another
   representation to reconcile. Events generated from the same asserted facts
   are not independent evidence of semantic truth or human approval. Calling
   the file `.log` does not reduce those responsibilities.
3. **SQLite authority** provides database transactions, but makes the selected
   JSON records exports/projections and changes the source-of-truth decision.
   Database-to-files/GitHub publication still needs its own recovery/reconciliation.
   A disposable rebuilt query index could be considered only for demonstrated
   need; none is established. Do not add one in anticipation.

SQLite is not intrinsically unsuitable for a local tool. Its default is a
rollback journal; WAL is optional and adds associated files and checkpointing,
with same-host shared-memory constraints. Those are separate from Git's lack of
semantic merging of a binary database. See the
[official WAL documentation](https://sqlite.org/wal.html) and
[atomic-commit explanation](https://sqlite.org/atomiccommit.html).
Yegge's [Beads 0.57.0 announcement](https://github.com/gastownhall/beads/discussions/2228)
identifies Dolt replacing SQLite and JSONL primary storage. It does not establish
that ordinary SQLite WAL alone caused that choice; do not turn remembered
motivation into an asserted historical fact or adopt Beads' storage stack here.

The recommended distinction is observable behavior: temporary recovery material
for one incomplete write, Git history for committed changes, and canonical
records/evidence for product state. There is no permanent append-only event
authority or replay engine in that recommendation. Local locks do not coordinate
separate machines; branches/clones integrate through Git, followed by semantic
validation. Finish/recover a local incomplete write before normal synchronization;
never rely on ignored scratch as cross-machine continuation authority.

#### Selected storage boundary and proposed interrupted-update recovery

The maintainer explicitly instructed: “Let's stick with JSON sidecars and Git
history, no SQLite, Dolt, or permanent ledger. Keep it aligned with Backplane
and walk me through how we'd recover an interrupted update without making this
too heavy.” The maintainer reaffirmed philosophical alignment with gzkit only,
no work across that boundary, and retention of Superpowers as the lightweight
feature-development inner loop beneath the starter's outer loop. This is an
agent transcription/summary of the continuation, not separate ADR approval.

**Selected:** canonical JSON sidecars, Markdown narrative/generated views,
hand-written changelog and committed Git history. Exclude SQLite, Dolt and a
permanent operation/event ledger from the management-record design. A local
temporary recovery record for an incomplete file update is permitted by the
selected bounded-recovery direction; its exact schema and behavior remain a
proposal. It must not grow into authoritative product history or a replay engine.
Git preserves committed snapshots; it does not record every uncommitted operation
or provide proof of semantic approval. No claim about gzkit ledger redundancy or
changes to that separate project is made.

**Alignment target:** lite and heavy preserve the same applicable management
meanings, identities, criteria/revisions, relationships, dispositions and
evidence. The six artifacts must have explicit Backplane correspondents without
silent loss of requirements or unresolved obligations. Lite may remain permanent;
heavy explicitly adopts verified Backplane management. Heavy-only hosting and
monitoring capabilities need not be implemented locally to preserve the model.
The crosswalk above grounds this design in existing Backplane contracts, but
exact lite schemas, shared contract additions and migration have not been
specified, reconciled or tested. Do not claim complete shape conformity or a
delivered mode transition from conceptual alignment. Improve Backplane's owning
contract deliberately where necessary rather than freeze a deficient local fork.

**Proposed minimal file-update protocol:**

1. Establish the actual worktree, affected paths, current source revisions and
   starting bytes, including legitimate uncommitted edits. Serialize cooperating
   writers in that worktree and detect changes to expected inputs. A local lock
   does not coordinate other clones/machines or prevent an independent editor.
2. Prepare and validate the complete affected JSON/view candidate before changing
   authoritative files. Preserve narrative and test referential/semantic rules.
   Durably prepare one bounded recovery bundle containing exact affected paths,
   starting bytes/absence, proposed bytes and their identities before replacement.
   Keep it in an ignored, confined local working area, not a permanent JSONL file.
3. Recheck inputs and install the prepared files. Recheck final bytes and affected
   invariants before reporting success. Cooperating commands refuse to accept an
   unfinished update. Multiple replacements are not an atomic filesystem batch;
   exact interruption/durability behavior requires reached-fault testing.
4. On restart, inspect the pending bundle before further mutations. If every
   output matches the proposed bytes, revalidate applicable inputs/invariants and
   finalize the completed update. If every output matches the starting bytes,
   discard the uninstalled candidate after verifying ownership. If outputs are a
   mix of starting/proposed states, default to restoring the exact recorded
   starting state only when inputs/ownership still match and applicable authority
   permits recovery. Any third-party edit or unexplained revision change stops
   automatic recovery; preserve files and explain the conflict. An unchanged
   file may legitimately match both identities. Never reset the whole repository
   or restore from HEAD over legitimate starting uncommitted work.
5. Remove successful recovery material after verification; preserve unresolved
   material until recovery/reconciliation is complete. Normal project commits
   capture coherent changes at the existing cadence, without a commit or full
   gate for each field update. Durable approval/evaluation/handoff evidence stays
   in its existing tracked authority, not solely in disposable scratch. Finish
   or explicitly reconcile interrupted updates before normal Git synchronization.

This recovery protocol covers local record/view writes. It cannot make GitHub
API calls, Git pushes, publication or arbitrary tool effects transactional; those
retain their own observed-state and retry contracts. Promotion uses Backplane's
authorized native operations and verified transfer, not replay of this scratch.

This records selected design direction and a recovery proposal, not an approved
identified ADR, implemented migration or Backplane conformance result. Preserve
the pending 0.10.0 scope boundary. No behavior or tests change; diff/reference
review and reuse of unchanged-input evidence are the applicable verification.

### Shared field ownership and disciplined Git commits — design review

The maintainer accepted the bounded recovery approach and requested continued
review of the shared record contract. The maintainer proposed strict,
deterministic typed metadata in commits as a way to strengthen Git discipline,
potentially using Pydantic models, without introducing a separate permanent
ledger. This is a proposed strategy, not an approved commit schema, new hook or
permission to rewrite historical commits. Current storage/recovery selections
remain intact; the exact recovery protocol still needs specification and tests.

The following is the agent's field-ownership proposal, grounded in the reviewed
Backplane governance/native-issue/checkpoint contracts, not a delivered schema:

| Authority in lite | Fields owned there | Backplane correspondence |
| --- | --- | --- |
| Requirements sidecar | Stable requirement/statement keys, required wording, constraints, governing revision and approval references; requirement-level acceptance definitions where applicable | Requirement and Authority records; approved project document/issue statement and revision |
| Backlog sidecar | Stable work/outcome keys, kind, bounded objective/scope, work-specific acceptance criterion keys/definitions, parent/dependency links, explicit priority and outcome lifecycle; links to governing requirements | Native issue contract plus Backplane Record; native hierarchy/dependencies/lifecycle; work criteria and Coverage map to requirements |
| Roadmap sidecar | Capability progression, milestone identities and forecast/target relationships | Capability/outcome decomposition and native target grouping/views; exact shared roadmap schema is not delivered |
| Work sidecar | Selected work references, plan identity/revision, task-level execution progress, blockers/resume context and evaluation/evidence references | Approved issue-bound Superpowers plan, execution/PR contributions, immutable evaluation pointers and handoff context |
| Releases sidecar | Published baseline, bounded selected membership, pending version/classification rationale, release-specific gates/dispositions, publication authority and observed channel identities | Project-owned release scope/authority, native target grouping and actual release records; shared release-doctrine schema/ownership transfer remains pending |
| CHANGELOG.md | Manually curated explanation of notable user-facing changes | Remains a repository document; references release identity without becoming publication authority |

Do not independently store outcome lifecycle in WORK when BACKLOG owns it.
WORK references that state and owns finer plan-task progress. Likewise, parent
completion and release summaries derive from governed outcomes/evaluations,
not separately editable satisfaction booleans. Requirement criteria and bounded
work acceptance criteria need explicit identities/mappings; do not collapse
them or mandate a redundant requirement hierarchy. Roadmap targets are forecasts;
RELEASES owns actual selected membership. Historical published membership remains
immutable. Current evidence pointers do not overwrite historical evaluations.

Each structured artifact needs an identified format/schema version, project/
namespace context and stable record keys. Exact common headers, source-revision
binding, file locations, extension rules and model implementation are unresolved.
Keep native issue IDs, Project fields, pagination and capture times out of the
portable record core. An unobserved native ID is unavailable, not a fabricated
issue number. The existing checkpoint types supply semantic precedent, not an
editable lite source schema ready to adopt unchanged.

Promotion preserves stable local/semantic keys, maps them to native GitHub issue
identities, transfers relationships/criteria/authority/evidence and verifies
arrival before switching field ownership. Current Backplane has no delivered
lite-to-heavy converter for these five sidecars. It also lacks the finalized
shared roadmap/release schema proposed here. Its existing checkpoint remains a
read-only capture, not a general offline mutation/synchronization API. These are
explicit design/implementation gaps, not permission to infer compatibility.

#### Commit metadata proposal

The agent supports examining a small typed change record carried by the commit
message itself. Git owns the containing commit/tree/parents; sidecars remain
the authority for product state. Metadata links a coherent change to governing
work/requirement/criterion revisions and existing evidence, rather than requiring
event replay or maintaining another mutable state log. Pydantic is a plausible
validator, not a selected/installed dependency or semantic approval authority.

Candidate meanings: format version, change category, affected stable record
identities, governing authority revisions, evidence references and verification
scope/reuse rationale where applicable. A documentation-only/no-tracked-work
commit must have a truthful representation rather than invented issue/criterion
links or unsupported completion claims. Keep readable human commit subjects.

Exact JSON-in-message versus Git-trailer encoding is still open. Git's official
[trailer mechanism](https://git-scm.com/docs/git-interpret-trailers) supplies a
parseable message convention, not application-schema validation. A format marker
and JSON payload could preserve the user's desired typed records; alternatively
trailers could encode a bounded schema. Select one unambiguous authoritative
encoding before implementation. Validate against the actual staged/committed
paths and record references, not only against JSON types. The enclosing commit
supplies its own identity: do not embed its future SHA into its message or a
tracked receipt in that same commit. Post-publication CI/channel results arrive
later and cannot be claimed prospectively.

Required design cases include merge/squash, amend/rebase, cherry-pick and revert,
automation commits, interrupted commit/hook failures and staged versus unstaged
inputs. Changed payloads require reconciliation of metadata/evidence. Do not
replay state changes from a copied message or rewrite published history to add
records. Require no fresh full suite for a metadata/prose-only change when valid
unchanged-input evidence suffices under the verification policy.

Current routine hooks are explicitly limited to Ruff check/format, ty and
unittest. A new commit-message hook changes that approved binding; do not install
one silently. Git documents that
[commit-msg may reject a message and can be bypassed](https://git-scm.com/docs/githooks#_commit_msg),
so CLI preparation/local checks alone cannot establish integration enforcement.
Determine the local/integration enforcement and adoption contract explicitly,
without weakening the four existing checks or silently adding a fifth routine
analysis category. Existing direct git/gh requirements remain in force.

Git snapshots and commit metadata can travel through another Git host. Current
Backplane deliberately requires GitHub/gh and native issue features; another
host is a future adapter/conformance undertaking, not existing portable-host
support. No alternate backend, GZKit change or Superpowers replacement is part
of this discussion. This records architectural input only and leaves exact
schema/ADR approval, implementation, release scope and publication separate.

### Remaining detailed decisions

#### Simultaneous design checkpoint

The maintainer explicitly authorized dual design in the local starter and
Backplane folders. The new
[starter minimum-contract draft](../superpowers/specs/2026-11-14-lite-record-and-commit-contract-draft.md)
defines the proposed file envelope, RecordRef/SourceRef types, field ownership
and a compact JSON `Starter-Record` trailer. The paired Backplane draft is at
`docs/superpowers-backplane/specs/2026-11-14-lite-record-and-commit-alignment-design.md`
in `tvproductions/superpowers-backplane`; its HANDOFF and CHANGELOG now point to
the shared design work. These are local, uncommitted design candidates, not
approved ADRs, schema/commit-policy activation or published alignment.

The maintainer selected a minimum typed JSON record for every governed new
commit and preservation of the four routine checks. The proposed encoding is
one `Starter-Record` Git trailer carrying format, kind, records, evidence and
reason. Its exact spelling, strict models, 8,192-byte cap and acceptance mechanism
remain draft choices. The standalone JSON and text message examples accompany
the starter draft, respecting the no-embedded-JSON-in-management-Markdown rule.
Direct `git interpret-trailers --parse` extracts the example successfully without
a commit or configuration change. Git parses the footer; application validation
must establish types/references and cannot manufacture human approval.

Review the two drafts together before proposing identified ADR editions or
dependent implementation. Starter follows reviewed Backplane design cues and
maintains the mapping; this paired work permits improvements in Backplane's
owning contract without making starter prose Backplane authority. Retain current
lite/heavy definitions and make no prospective hosting or mode-convergence
commitment from the broader conversation.

Paired draft identities after the joint edits: starter minimum-contract SHA-256
`e2f2fc7816d807d1eaa287a3747ad1dc4d830781632cd6aa61e3ab15c190ae3a`;
Backplane counterpart SHA-256
`b046c843e8b9980814256a8890b97982bc7c23537966d95204853f4f25079439`.
The full starter base is `8c8ff4b113fa5ec8bd01d5ec3f09ba95c15f5574`;
Backplane remains based on `05505f8009989eb7514ec62750e33c78bc40abf9`.
Both are uncommitted candidates; hashes establish content identity, not approval.
Observed checks: both diff whitespace checks pass; draft relative references
exist; exact draft hashes match Backplane's handoff; Git extracts exactly one
example trailer whose JSON equals the standalone five-field example. Root and
Backplane hook/tool configuration is unchanged. No new behavior or model test,
native qualification, hosted CI, Git sync or publication is claimed.

1. **Cognitive delivery:** the universal-blocker choice is resolved by the
   continuation above; API plus CLI is selected and MCP/plugins deferred for
   the first release. Design the exact contract, independent maintained
   extraction and qualification/release plan. No implementation date,
   package name, new repository or actual engine acceptance is established.
2. **Enforcement architecture/ownership:** define the CLI boundary, portable
   SP-BP semantics versus starter-specific executable rules, location/versioning
   of Pydantic models, and interfaces that avoid duplicate script implementations.
   Reconcile current prohibitions on competing lifecycle ownership. Which
   existing modules need refactoring, and which helpers are retained/moved/retired?
3. **Record schema and authority:** exact headings, common metadata, stable IDs,
   criterion identities, state vocabularies, approval/evidence references,
   sidecar granularity and binding, and how schema upgrades preserve local content.
   JSON structured authority versus Markdown narrative/generated views and the
   hand-written changelog are selected; do not reopen that split.
   Keep malformed records, unmet conditions and unknown evidence distinct.
4. **Management and SemVer:** requirements versus backlog versus selected work;
   roadmap commitments versus forecasts; bounded release membership; classification
   at intake/design/closeout; version-mirror reconciliation and publication
   authority. Where do newly written major PRDs and their edition history live?
   How does the first unpublished 0.1.0 remain finite rather than accumulate
   unrelated work indefinitely?
5. **Verification selection:** smallest reliable ownership/consumer mapping,
   focused/member/integration triggers, pre-implementation checks, isolated
   environments, local/hooks/CI/on-demand responsibilities and evidence reuse.
   Prevent both bypasses and needless repeated full runs. Keep Astral settings
   centralized in root pyproject.toml and independent runtime baselines explicit.
6. **Migration contract:** supported initial/brownfield/legacy paths; conflict and
   recovery behavior; explicit heavy authority transfer and native verification;
   retained/archived records; upgrade compatibility across starter/schema/component
   versions; supported hosts and scope-preserving plugin resolution.
7. **Bounded delivery/release plan:** separate specification and ADR approval,
   implementation slices, starter self-use and real-adopter pilot evidence.
   Determine what belongs in a subsequent release without silently expanding or
   shrinking the existing approved 0.10.0 scope. A first 1.0.0 requires its own
   newly written PRD and finite scope; do not infer that version from ambition.

Review for missing requirements, conflicting authorities, accidental gzkit-like
machinery, unverifiable guarantees and duplication. Include concrete positive/
negative cases for the observed adopter failures. Human/model behavior tests
complement structural checks; hashes and schemas cannot manufacture approval.

## External validation already performed

Primary sources support the concepts, not a universal six-file convention:

- [NASA requirements guidance](https://www.nasa.gov/reference/system-engineering-handbook-appendix/):
  identifiable sources, unique requirement IDs and defined verification.
- [Scrum Guide artifacts](https://scrumguides.org/scrum-guide.html#scrum-artifacts):
  distinguish ordered backlog from selected work and execution planning; no
  Scrum ceremony adoption is implied.
- [Atlassian roadmaps](https://www.atlassian.com/agile/product-management/roadmaps):
  evolving direction connecting everyday work and longer-term outcomes.
- [SemVer](https://semver.org/spec/v2.0.0.html): public-contract impact governs
  increments. The starter's major-PRD and stricter 0.x rules are its own policy.
- [Keep a Changelog](https://keepachangelog.com/en/1.1.0/): human-readable,
  categorized changes, unreleased entries, versions and release dates.
- [GitHub best practices](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects#have-a-single-source-of-truth):
  one authoritative location per fact to prevent drift.
- [Pydantic configuration](https://pydantic.dev/docs/validation/latest/api/pydantic/config/),
  [validators](https://pydantic.dev/docs/validation/latest/concepts/validators/),
  and [JSON Schema](https://pydantic.dev/docs/validation/latest/concepts/json_schema/):
  typed contracts, explicit strictness/extra-field rules and schema generation;
  document parsing, cross-record checks and approval truth remain separate work.
- [Astral workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/):
  workspace-member terminology, shared resolution and dependency-isolation limits.

## Release accounting, freshness and verification boundary

Published baseline remains **0.9.0**, immutable release commit
`3f76acf0038b030bf5abd85ce4a419e890d3e420`. Pending **0.10.0 / minor** remains
governed by the existing ADR/policy bundle and #12/#13. Bundle, package and
packaged-bundle mirrors were observed at 0.10.0. This save point delivers a
discussion handoff and routing documentation only. The future CLI/schema work
is not implemented, added to that release's acceptance scope or assigned another
version by this record. Existing companion/cognitive/native-host gaps persist.

The checkout still selects gz-skills **0.11.0**. A bounded check at this handoff
observed [gz-skills 0.12.0](https://github.com/tvproductions/gz-skills/releases/tag/v0.12.0),
published November 14 at 19:14 UTC, after the earlier authorized update. Flag it
for separately scoped maintenance; this documentation sync leaves pins, locks,
environments and native activation unchanged. Do not call the entire stack
current from the earlier 0.11.0 receipt. The supplied session skill catalog still
advertises the prior 0.10.1 cache; selected refs and loaded skills are distinct.

Execution uses uv 0.13.8 and the existing managed Python 3.14.10 environment.
The earlier full four-hook, catalog, resource, source-independent build and clean
installed-helper checks passed for unchanged implementation/configuration inputs;
both final-commit CI jobs at base 1c633f8 passed in
[run 43627937607](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/43627937607).
For this prose-only change, review the complete diff and references, retain normal
hooks, and reuse applicable source checks under the verification policy. No new
tests or analyzer regressions are required. Final-commit CI will run the actual
candidate's complete configured gate/build/installed checks. Report its exact SHA
and result in the sync response; do not create a CI-receipt-only commit chain.

Local handoff checks observed: `git diff --check` passed; all 113 relative Markdown
link targets across the six intended files exist; package/bundle/packaged-bundle
version mirrors agree at 0.10.0; actual locked interpreter is managed 3.14.10.
Normal commit hooks remain enabled. Final remote alignment and new-commit CI
must be observed after this record's commit; the result belongs in the response.

Suggested next-session skills: brainstorming for the voice design discussion;
intent/plan audit when comparing proposals with adopted commitments; writing-plans
only after the concrete design is approved. Keep the handoff separate from a
formal new design, ADR approval, implementation and release acceptance.
