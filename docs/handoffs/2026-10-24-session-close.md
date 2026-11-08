# Session handoff — October 24, 2026

## November 8 branch preference — commit directly on main

The maintainer directed: “please don't create feature branches, just commit to
main”. This supersedes the execution isolation ruling below. Returned the
uncommitted reviewed changes to `main` and removed `feature/adr-practice` only
after verifying that both branch tips were identical and no distinct commits
would be lost. Recorded the direct-main preference in AGENTS for future work.
The requested scope is a normal local commit with hooks; no push, tag, release,
plugin installation or companion edit is implied. Preserve the outstanding
qualification work in the receipt. The commit identity belongs in Git history;
do not create a self-referential receipt commit chain.

## November 8 native implementation — starter complete, trio qualification pending

The maintainer approved the plan for native execution and separately explicitly
approved ADR-0001-001: “approve plan (explain native execution), and explicityly
approve ADR-0001-001”. Native means the primary agent implements tasks in this
session and a fresh reviewer checks the whole change. No per-task implementation
agents, commits/pushes, plugin installs, companion writes or publication follow.
The approved ADR now lives in `docs/decisions/`, with self-contained approval
evidence and the exact reviewed proposal preserved/hash-verified under
`docs/decisions/approvals/`. Earlier draft/approval-pending entries below are
historical checkpoints superseded by this capture.

Implementation branch: `feature/adr-practice`, based on
`1dd24b2a52249e22170a102bb0c363daae3e243b`. Preserve the local uncommitted design
and implementation artifacts. Starter policy and its own agent binding now
route design/execution/review to applicable ADRs. `configure --adr-policy
link|local` supports immutable links or an exact repository-local policy copy;
omission preserves a recorded selection and defaults to link only on new
projects. The existing lock records original source/hash/path; old locks, mode
changes, adaptations and conflicts require reviewed reconciliation. The sixth
packaged input is the ordinary ADR policy. No new ledger/capability or generic
starter skill is added; component pins, activation and version remain unchanged.

Verification on uv 0.13.7 / managed Python 3.14.10: baseline 60 tests passed;
11 new policy test methods failed before implementation; the final review
regression adds a twelfth policy method and the full suite now passes 72 tests.
Covered both modes/all three helper hosts, exact UTF-8 LF/CRLF
bytes/hashes, no-write previews, repeated selection, edits/legacy/malformed
records, symlinked destination/parents, concurrency and failed-write rollback.
The pre-change wheel failed the new missing-policy check. Final locked all-group
sync, all four routine hooks, bundle/both-catalog validation, six-resource drift
check, source-independent build and isolated installed helper checks pass.
Portability audit reports no findings on Windows. macOS/Linux execution, actual
native discovery and exact-candidate remote CI remain unverified. No analyzer
changed; no analyzer-regression suite is triggered.

The [qualification receipt](../evidence/2026-11-08-adr-practice-qualification.md)
keeps the whole feature INCOMPLETE. Shared B01-B16 and targeted behavioral checks,
released owning companion contributions and companion internal-use/alignment
records remain outstanding. Both live companion trees/releases were inventoried
read-only without qualifying or changing them. Initial starter internal use is
this actual separately approved ADR and its application; independent alignment
review is complete, with its sole medium finding fixed and verified below.

Execution rulings: preserve the approved dirty checkout on a feature branch while
the optional separate-worktree preference is unanswered (transfer if requested);
use native PowerShell plan-scoped scratch bookkeeping rather than Bash helpers;
put focused public-seam tests in `tests/test_adr_policy.py`; retain existing
`update-gz-template` text because its fresh application baseline preserved local
mode/provenance and routed to canonical target guidance. Put target details in
adoption/updating docs; add no duplicate skill procedure. Incorrect rulings would
require workspace/progress reconciliation, focused-command correction or renewed
skill evaluation respectively, without authorizing wider product scope.

Published baseline -> pending target remains **0.9.0 -> 0.10.0 / minor**, governed
by #12/#13. Included starter policy/helper/docs/artifact work is locally verified;
companion delivery and feature qualification remain included unfinished work.
Existing pilot, deterministic upgrade/rollback, remaining platform and reporting
deferrals remain unchanged. Final review found one medium defect: partial writes
or close failures could leave a newly created policy after earlier outputs rolled
back. A real-file regression failed for both cases; the fix removes the owned
failed file while preserving a concurrent replacement. Full 72-test suite,
routine hooks, catalogs, resource check, no-sources rebuild, isolated installed
verification and portability audit pass after the fix. No unresolved important
findings or deferred minors remain. The receipt records every declined review
boundary and its disposition; no whole-feature acceptance follows.

## November 8 specification approved — starter implementation plan prepared

After the complete section review and a satisfaction check, the maintainer said
“ok, proceed”. Captured that as approval of the revised starter specification
for implementation planning; its approval section records the exact pre-capture
content hash and actual conversation context. This does not approve
ADR-0001-001. That architectural proposal remains unchanged and unapproved.

Created the [starter implementation plan](../superpowers/plans/2026-11-08-adr-starter-binding.md)
with four task units: policy/approval, public helper plus packaged policy,
adopter/update reconciliation, and source-bound qualification evidence. It uses
the existing provenance lock for link/local selection and adds no new ledger,
generic workflow skill or companion-internal implementation. Companion owning
designs/releases/evidence remain separate dependencies; the whole feature is not
implementation-ready from this starter plan alone.

The [plan alignment audit](../evidence/2026-11-08-adr-starter-plan-audit.md)
passes intent-to-scope and scope-to-plan comparison for the bounded starter plan.
Live published baseline/tag resolution still supports **0.9.0 -> 0.10.0 / minor**;
all four version mirrors agree. No product code, runtime/pin, packaged input,
native installation or companion file changed. Existing executable checks are
unchanged; planning whitespace/local-link checks apply to these artifacts.
Everything remains local and uncommitted. Next: review the implementation plan,
confirm native execution (recommended), and obtain separate explicit approval
of ADR-0001-001 before dependent implementation. Do not infer ADR approval from
the specification approval or a general instruction to proceed.

## November 8 design resumed — exact component qualification selected

Resumed issue #13 from clean main `1dd24b2a52249e22170a102bb0c363daae3e243b`;
direct `git ls-remote` confirmed origin/main matched. Read the pinned COB
discussion and live issues #12/#13 through direct `gh`. The maintainer selected
qualifying an exact component combination for each starter release: starter
mandatory policy/entry pointers, gz-skills portable procedure/template and
SP-BP planning/tracking integration, with independent component versions/releases
and exact reviewed sources plus behavioral evidence.

The [draft specification](../superpowers/specs/2026-11-08-adr-practice-design.md)
records this selection and proposes policy/distribution touchpoints, approval
provenance, preservation, owning companion obligations and a behavioral matrix.
The separately identified
[ADR-0001-001 record](../decisions/ADR-0001-001-qualify-exact-component-combinations.md)
is preparatory design material, not an authoritative Current decision. Approach
selection does not supply approval of either newly written document. Obtain
explicit specification approval and separate exact-edition ADR approval before
dependent implementation. The fresh SP builder check reported “nothing important
left” for material planning questions; this does not supply human approval.

During section-by-section review the maintainer accepted the propagation gate
and directed support for both immutable source links and repository-local policy
copies. Updated the draft with local-copy provenance, explicit working-source
routing, preservation/reconciliation and affected packaging/helper-test and
behavioral obligations. The initial builder check predates this addition; recheck
the affected design before final approval. Whole-specification and separate ADR
approval remain pending; continue reviewing the next sections with the maintainer.
The maintainer also accepted the proposed lightweight Markdown approval receipt
for otherwise unaddressable conversations, preserving actual approval text and
context plus the exact reviewed edition. This accepts the mechanism; it does
not approve the draft specification or ADR-0001-001.
The maintainer then selected the full shared B01-B16 matrix plus targeted checks
for each publishing repository and lite/heavy adopter fixture, replacing the
proposed full matrix in every binding. Every binding must demonstrate a missing-
approval stop and an approved-decision continuation. Preserve actual SP-BP
integration checks, both policy-access forms, policy precedence and genuine
internal use in all three publishers. Expand to affected matrix cases when a
binding changes shared behavior or a targeted check reveals a discrepancy.
The affected builder recheck remains due after section review is complete.

The maintainer directed keeping the decision and approval metadata/history in
the ADR, with approval evidence embedded or durably referenced and an optional
lookup-only README. Do not introduce a new ledger or other Backplane capability.
Live Backplane main `05505f8009989eb7514ec62750e33c78bc40abf9` defines heavy
participation without a transaction-ledger guarantee; its governance describes
checkpoint pairs and checkpoint installation/recovery receipts. The draft now
links those exact sources and requires integration through existing supported
records. This is a section decision, not whole-specification or ADR approval.
A fresh affected SP builder recheck of local-policy distribution, qualification
coverage and existing-record-only integration again reported “nothing important
left”. Local design links resolve and diff whitespace checks pass after these
revisions. Complete revised-specification approval and separate ADR approval
remain the next checkpoints; no implementation plan or product code was added.

Documentation verification: uv 0.13.7, pinned managed Python 3.14.10; all four
routine hooks passed, as did the read-only packaged-resource drift check and
diff whitespace check. No authoritative packaged input, code or analyzer changed;
build/install and behavioral qualification are not claimed for this design work.

Published baseline -> pending target remains **0.9.0 -> 0.10.0 / minor**, governed
by #12 and the existing bounded release record below. Bundle, package, lock and
packaged bundle still declare 0.10.0; no pin or runtime change is needed for this
design. Remaining scope includes approvals, companion designs/delivery, bindings,
behavioral qualification, internal use in all three repositories and distribution.
Existing deferrals remain unchanged. No companion files, native installations,
GitHub issues, commits, remote branches, tags or releases are changed by this
design work. Drafts are local and uncommitted; no implementation plan exists.

## November 8 save point — resume detailed design at issue #13

The maintainer requested a handoff and Git sync, then a return to detailed
design. Created [design issue #13](https://github.com/tvproductions/gz-skills-first-starter/issues/13)
as a native child of [feature #12](https://github.com/tvproductions/gz-skills-first-starter/issues/12),
both targeting [milestone 0.10.0](https://github.com/tvproductions/gz-skills-first-starter/milestone/2).
This books the design explicitly. Neither a concrete specification nor its
approval nor an implementation plan exists yet. Do not mark the feature ready
or complete from this booking or the save point.

There is enough accepted input to begin design without repeating settled
questions. Read the whole COB discussion through direct `gh`, pinned to
`dd1ab883c04e884678ed723959b17c5c364263d1` (live main rechecked unchanged):

```powershell
gh api 'repos/wtcis-pvecob/cob_projects/contents/docs/engineering/proposals/2026-11-07-gz-adr-workflow-discussion.md?ref=dd1ab883c04e884678ed723959b17c5c364263d1' -H 'Accept: application/vnd.github.raw+json'
```

The roughly 1,600-line document is a chronological discussion with explicit
acceptances. Later operator decisions and **Final audience guidance** govern
earlier candidate/open text. Use its standalone lightweight guidance and accepted
sample/edition rules; separate its GZKit reconciliation, drydock, ledger, order,
identity crossover and `g0` conventions. Preserve source identity and distinguish
source design acceptance from a real architectural ADR's explicit approval.

Start from this conversation's accepted boundaries recorded below: mandatory
both lanes; trio internal use first; no centralized CLI/core prerequisite; starter
leads its adopting stack and owns nothing for GZKit; acceptance reporting is the
last planned feature before a separately scoped 1.0.0. Starter design owns its
adopter policy and cross-component obligations. gz-skills and SP-BP design their
internals in their own repositories; coordinate and link their records rather
than silently deciding or duplicating their implementation here. The initial
design must resolve distribution/version references and behavioral evaluation
contracts. Reuse the source's accepted ADR semantics and ask only about actual
remaining decisions. Follow SP design review before implementation planning;
separate ADR approval still applies to new architectural choices.

Sync scope: the eight reviewed starter planning/version/resource files, from
published 0.9.0 commit `3f76acf0038b030bf5abd85ce4a419e890d3e420` to pending
0.10.0. A fresh origin fetch confirms no main divergence; remote Dependabot
branch refreshes do not alter this scope. No helper/analyzer implementation,
component pin, native installation or companion repository changes are included.
Keep normal hooks, run the documented local gate, push main normally and observe
CI for that exact final SHA. Report the result without a receipt-only commit
chain. This save point publishes no tag or release and starts no design work.

Pre-sync verification passed again on uv 0.13.7 / managed Python 3.14.10:
locked all-group sync, all four routine hooks, bundle/both-catalog validation,
source-independent build and isolated installed-distribution checks. Analyzer
regressions are not triggered by this documentation/version-only scope. Verify
the final commit's own CI after push; prior release CI does not cover this change.

## November 8 agreed ADR practice and next release scope

Published baseline: **0.9.0**, immutable annotated `v0.9.0` tag
`4e4a66d222488194b599de4f2ccef9ba291ea881`, release commit
`3f76acf0038b030bf5abd85ce4a419e890d3e420`. Both exact-commit CI jobs passed
in [run 42501660044](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/42501660044).
GitHub reports a published stable release; downloaded wheel/sdist/update-skill
ZIP hashes match SHA256SUMS. The downloaded wheel installs outside the checkout
on managed Python 3.14.10, reports 0.9.0 and validates both catalogs. The earlier
release-preparation entry below is historical; publication is complete.

Pending target / kind: **0.10.0 / minor**. Governing work: the maintainer's
agreement in this conversation to mandatory architectural decision practice in
both lite and heavy lanes, informed by the
[COB proposal's final lightweight guidance](https://github.com/wtcis-pvecob/cob_projects/blob/dd1ab883c04e884678ed723959b17c5c364263d1/docs/engineering/proposals/2026-11-07-gz-adr-workflow-discussion.md#final-audience-guidance).
The new mandatory adoption/workflow requirement determines the minor increment.
Bundle, package, generated resources and owning-tool lock metadata must agree.

Release outcome: agents recognize consequential architectural choices before
implementation embeds them, reuse applicable approved decisions, and obtain
separate explicit approval of the identified edition for new or replacement
decisions before dependent work. Check alignment during design, execution and
review. Preserve honest approval provenance, editorial history and independent
decision/requirement/design/work/evidence/release identities. An ADR is not a
feature, task or release container. A successful test or general plan/release
approval is not architectural approval. Existing authority to act remains intact.

Initial rollout covers this starter, gz-skills and SP-BP before propagation to
adopting projects. The starter leads policy for projects adopting/using this
trio; it owns nothing on GZKit's behalf. GZKit drydock/ledger/order/crossover work
remains under GZKit's own authority. The practice applies to these publishing
repositories themselves as well as their adopters. No central CLI, shared
runtime, application core or new planning hierarchy is a prerequisite.

Included completed work: this agreed scope, ownership boundaries and reordered
roadmap. Included remaining work: concrete design of the starter policy binding,
portable gz-skills workflow/template and applicable SP-BP integration; reconcile
each repository's own instructions; verify recognition/approval/alignment with
invented positive and negative behavioral scenarios. Demonstrate use in all
three repositories before adopter propagation. Missing approvals, vague assent,
mid-implementation choices, existing-decision reuse, conflicting direction and
honest backfills must be covered. The accepted conceptual direction does not
constitute approval of an unwritten implementation design or a real ADR edition.

Deferred/excluded from 0.10.0: real-adopter pilot execution, deterministic template
upgrade/rollback tooling, remaining native-platform qualification and adoption-
acceptance automation, except references needed to keep their future integration
coherent. Acceptance reporting is the final planned feature before a proper
1.0.0; existing adoption requirements remain mandatory throughout. The future
1.0.0 needs its own new PRD and finite scope, not an automatic tag after reporting.
Generic maintenance and cognitive integration retain their existing ownership.

Compatibility/migration: a newly mandatory workflow changes the pre-1.0 adoption
contract; preserve existing suitable ADR identities/history and explicit authority.
Do not silently migrate collections or claim a native hook/approval writer exists.
Publication: 0.10.0 is unpublished. No companion edits, plugin installation,
issue mutation, commit/push or publication is performed by this discussion record.
Detailed distribution/version binding and SP-BP integration remain design work;
claim neither implementation readiness nor ADR-practice acceptance yet.

Discussion-record verification: uv 0.13.7 and managed Python 3.14.10; owning-tool
lock refresh changed only the starter version. Regenerated resources, locked
all-group sync, all four routine hooks, bundle/both-catalog validation,
source-independent build and isolated installed-distribution checks pass for
0.10.0. Reviewed the complete eight-file diff and whitespace checks. No analyzer
or helper behavior changed; deeper release acceptance and behavioral ADR
evaluations remain outstanding. Changes are local and uncommitted.

The maintainer subsequently requested a tracked feature increment. Created
[feature #12](https://github.com/tvproductions/gz-skills-first-starter/issues/12)
in [milestone 0.10.0](https://github.com/tvproductions/gz-skills-first-starter/milestone/2)
using the existing enhancement classification. The issue captures bounded
workstreams, acceptance criteria, exclusions and verification; detailed design
is pending, not approved or implementation-ready. Starter design owns adopter
policy/cross-component obligations. Each companion owns its detailed design and
implementation in its own repository; link its records rather than duplicating
task state here. Concrete specifications need maintainer approval before dependent
implementation, and architectural ADR approval remains a separate checkpoint.
No Backplane lifecycle labels, plugin activation or companion issues were created.

## November 8 authorized 0.9.0 release

The maintainer requested publication and queried whether the version was 0.9.1.
Live GitHub release/tag inventory confirms published 0.8.0 is the baseline,
with no 0.9.x tag or release. The complete pending policy bundle requires 0.9.0;
do not invent an intervening 0.9.0 to justify 0.9.1. The preceding save point
`8870cc53b941ab1e40704d72e1b6144715c04c9b` matches origin/main with green
[exact-commit CI](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/42500761358).

The release outcome/scope below remains governing. Publication authority now
includes the ordinary release commits/pushes, immutable annotated v0.9.0 tag,
GitHub release and the four declared distribution assets. No plugin/native-cache
installation or dependent-repository update is authorized. Freshness review
precedes the release-scoped tool refresh; both locks and CI are reconciled.
See the [candidate-specific receipt](../evidence/2026-11-08-0.9.0-release.md)
and its JSON companion for actual input hashes, deeper checks and explicit
retentions/limitations. Remaining work is exact-release-commit CI, remote tag,
published stable status and downloaded asset/install verification. Record final
results after publication without a chain of receipt-only commits.

## November 8 Git synchronization and release scope

The maintainer invoked `gzs-git-sync` for this checkout. Initial main was
`8d090f88bf45b9a755808a62c1445beeb005daff` with the twelve reviewed policy,
version-mirror, generated-resource and audit files pending. A fresh origin fetch
found four newer commits through `a483e38`; preserve their minimum-only uv
compatibility, roadmap, hosted-scan evidence and Python authority clarification.
The local policy unit was committed with normal hooks as `a112d8e`, then merged
with origin/main. Resolve the overlapping changelog by retaining both units.

Published baseline: **0.8.0**, immutable `v0.8.0` commit
`e0b752fcc13b87ec7868fe0b0f85badefdb6bf52`; GitHub confirms publication.
Pending target / kind: **0.9.0 / minor**, superseding the November 1 patch-only
0.8.1 target because the combined scope includes an adopter policy change.
Governing work: the approved minimum-only uv compatibility requirement in the
[November 7 plan](../superpowers/plans/2026-11-07-uv-minimum.md), the existing
Windows idempotence defect, and release-planning/Python-authority corrections.
Release outcome: admit supported uv >=0.13.5 while preserving locked packages,
exact managed Python pins, native configuration behavior and policy ownership.
Included completed work: those changes, roadmap reconciliation and hosted-scan
evidence; the November 1 audit remains historical evidence for local adopters.
Included remaining work: candidate-specific freshness review and applicable
release acceptance before any separately authorized publication.
Deferred/excluded: cognitive-engine integration, Backplane readiness, native
desktop/embedded-host proof, dependency PR merges and dependent-repository edits.
Compatibility/migration: adopter uv policy changes from exact execution to a
minimum; package/backend and plugin pins remain unchanged. Bundle, package,
lock, installed CLI and generated-resource version mirrors must agree at 0.9.0.
No unresolved product decision blocks this save point. Release acceptance is
separate and remains pending; no tag or publication is authorized by Git sync.

The pre-merge local gate passed with uv 0.13.6 and managed Python 3.14.10:
locked all-group sync, four routine hooks, bundle/both-catalog validation,
source-independent build and isolated installed-distribution verification.
After reconciliation, the complete gate passed again with supported machine uv
0.13.7 and managed Python 3.14.10; the installed CLI reports 0.9.0. The independent
X-Plane locked sync and verifier also passed on managed Python 3.12.16.
Observe CI for the final pushed SHA and report remote alignment without another
receipt-only commit. No analyzer implementation changed; analyzer-specific
regressions are not triggered. Existing acceptance exceptions remain explicit.

## November 1 release-planning correction (unreleased)

The maintainer clarified the governing hierarchy: PRDs guide majors, selected
work/requirements drive minors, and fixes drive patches, then requested an audit
and correction of adopting projects under agents/ and xp/. The
[audit and verification receipt](../evidence/2026-11-01-release-planning-audit.md)
records inventory, local binding edits, published-release evidence and unresolved
scope decisions. Six project AGENTS files and both companions' release-policy
bindings were corrected; existing changelogs were reconciled where applicable.
Health's published 0.1.0 was incorrectly labeled unreleased. WebAPI's pending
Python support removal needs a major/PRD or preservation decision before release.

Starter pending version is 0.8.1 for compatible host fixes and clarification of
existing release commitments. Metadata/lock/resources agree; the required local
gate passed. Product versions, adoption records, plugin pins and approved scopes
remain unchanged. No commits, pushes, tags or releases were requested or made.
The maintainer then requested a reliable policy. Versioning now includes a
mandatory decision procedure at requirements intake, planning and closeout,
worked arithmetic, a bounded release record and failing completion conditions.
All eight local bindings carry those checks and current source hashes; agents
derive routine numbers and ask only for unresolved product-scope decisions.
Backplane's release bundle, Ortho4XP's distributed baseline and WebAPI's support
removal remain explicit decisions; do not manufacture them from this audit.

Read this entry first, then the
[0.7 tooling handoff](2026-10-24-0.7-latest-tooling.md) and
[acceptance/synchronization record](../evidence/2026-10-24-git-sync.md).
Recheck Git and remote CI before continuing; this is a dated checkpoint.

## Python policy authority aligned in source — November 7

The maintainer subsequently requested Git synchronization of this correction.
Fetch confirms all three local main branches align with their remotes before
committing. Publish the reviewed starter authority first, then reconcile the
companions to its exact committed source. Stage only the narrow SP-BP authority
paragraph/binding/receipt; preserve its separate strict-Astral and release-scope
work. Keep hooks and project gates intact. Observe final exact-commit CI where
configured, report absent project CI explicitly and avoid receipt-only loops.
This authorizes ordinary commits/pushes, not release or installed propagation.

The maintainer explicitly directed fixing all three repositories and reaffirmed:
current ordinary projects use Python 3.14; X-Plane/XPPython3-bound code uses
supported 3.12. The starter already declares those ranges. Updated workflow
mapping, shared ownership guidance and generated adopter instructions to prevent
a supporting skill's fallback from becoming a competing standard.

A new standalone `../gz-skills` canonical checkout starts at `9a79702`.
Its candidate 0.9.0 reconciles its own ordinary runtime/support to 3.14 and managed
3.14.10, and setup/update 0.4.0 remove the old fallback runtime/tool/package
assortment. They consume the governing project/adopted source and keep unavailable
authority UNKNOWN. Five bounded baseline/green cases and all 28 tests pass;
Ruff/format/ty, all 20 skill validations and source-independent/installed artifact
proof pass. Source/sdist/wheel preserve all 44 canonical skill resources.

SP-BP independently already selected 3.14.10. Preserve its concurrent strict-
Astral and release-doctrine work; only a narrow runtime-authority paragraph,
appended binding and scoped receipt belong to this correction. Its current
locked hooks and nine adapter tests pass. No wider acceptance gap is waived.

The [cross-repository receipt](../evidence/2026-11-07-python-policy-alignment.md)
records source identities and limitations. The starter still selects released
gz-skills 0.8.3; the corrected source is unpublished/uninstalled. No native cache
or consumer copy was edited, and no plugin install, commit, push or publication
occurred. Per-repository independent review found no concrete correction defect.
Run a separately authorized release/update path before claiming installed skill
alignment. Full engineering migrations remain independently scoped.

## Hosted Dependabot recovery verified — November 7

The authorized policy/roadmap commit `f0f5428` reached main with both exact-commit
CI jobs passing. A comment documenting the uv minimum in `.github/dependabot.yml`
at `e918dbb` triggered fresh hosted jobs, preserving parsed settings/schedules.
Both Python scans and Actions passed; actual Python updater uv is 0.13.7 and
the old version-rejection error is absent. Both repository CI jobs pass on
e918dbb too. CLI retry and browser-control attempts had failed; the Git-based
configuration update supplied the successful trigger.

Inspected all ten generated PRs (#2–#11): five per Python baseline, limited to
their own manifests/locks, with green reported CI. Exact heads/files/check links
are in the [PR inventory](../evidence/2026-11-07-dependabot-prs.json); the
[completed receipt](../evidence/2026-11-07-dependabot-uv-compatibility.md#hosted-verification-completed--november-7)
records scan links and scope. No PR was merged or approved. Complexipy updates
need review of historical-reproducer intent; Lizard needs its analyzer/contract
checks. Routine CI does not establish those deeper results. Root build-only
uv_build PR behavior and embedded-host acceptance remain unverified.

This final documentation update closes stale pending-scan statements in the
roadmap/guide and preserves material verification. Observe its own exact-commit
CI after normal hooked commit/push; make no further receipt-only commit just to
record that result. Scan inputs remain unchanged from e918dbb. No tag/release,
plugin installation or dependent-repository change is authorized by this sync.

## Minimum-only uv compatibility — November 7

The maintainer subsequently authorized committing/pushing this reviewed unit,
exact-commit CI verification, fresh Dependabot checks for both Python projects
and inspection of generated PRs. Pre-sync fetch finds main/origin aligned at
`8d090f88bf45b9a755808a62c1445beeb005daff`, with only the reviewed roadmap,
minimum-only uv policy/configuration, generated instructions and evidence edits.
Keep normal hooks enabled. Report final remote/CI/scan identities after push
without a chain of receipt-only commits. Release publication remains separate.

The maintainer identified repeated exact-pin impediments and explicitly approved
minimum-only uv compatibility. This supersedes the exact-execution constraint
and pending updater choice in the initial diagnosis below. Both projects now
declare `required-version = ">=0.13.5"` without an upper bound. CI 0.13.6 remains
the tested reference, not the only permitted executable. No replacement bot is
needed for the demonstrated version rejection.

AGENTS, adopter instructions, baseline/Python/configuration guidance, the
Dependabot guide and generated wheel instructions distinguish compatibility
from tested selections and freshness. Supported uv versions need not be replaced
solely to match CI. Exact managed Python patches, package locks and uv_build pins
remain unchanged. Future uv admission is a policy choice, not blanket proof;
record actual provenance and investigate behavioral failures. Older uv may need
the exact managed Python already available or reviewed download metadata.

The [diagnosis/resolution receipt](../evidence/2026-11-07-dependabot-uv-compatibility.md)
preserves failing controls and the accepted alternatives. The change remains
unreleased and needs the next minor policy release under the 0.x contract; no
tag, release, push, plugin installation or dependent-repository change follows.
Fresh hosted scans need final default-branch inputs; real update PRs remain
UNKNOWN. Earlier roadmap edits remain in this worktree.

Verification: actual uv 0.13.5 and 0.13.6 each pass the complete repository gate
with managed Python 3.14.10; lock checks pass in both projects under 0.13.5,
0.13.6 and 0.13.7. All-group sync and standalone X-Plane probes also pass under
0.13.5 and 0.13.7 on managed 3.12.16. uv 0.13.4 is rejected below the floor.
Nested uv provenance is recorded; locks, CI pins and interpreter pins are
unchanged. Managed interpreters were already provisioned; no cold-download or
embedded-host acceptance is inferred. Generated resource copies agree.

## Dependabot compatibility diagnosis — November 7 (superseded constraint)

The operator next requested resolving both uv scan failures. The
[dated diagnosis](../evidence/2026-11-07-dependabot-uv-compatibility.md) proves
the causal boundary: each project requires exactly uv 0.13.6, hosted November 2
jobs ran 0.13.5, and current upstream Dockerfile source selects 0.13.7. Both
nonmatching versions fail read-only lock checks in both projects; 0.13.6 passes.
The Dockerfile does not establish GitHub's currently deployed image. CLI retries
of both jobs were rejected as not retryable; no new hosted run exists.

The guide now corrects obsolete pin/metadata descriptions and links the evidence.
Pins, locks, project environments and scan configuration remain unchanged. No
policy-compliant hosted uv-version override was found. A maintainer choice is
pending between designing a controlled updater that honors exact pins and
retaining the explicit upstream blocker. Do not claim hosted scanning repaired
or silently replace the service, relax pins, install tools or publish changes.
The earlier roadmap edits remain in the same uncommitted worktree.

## Roadmap reconciliation — November 7

The operator authorized the next recommended step: reconcile ROADMAP.md, not
implement its proposed features or create GitHub issues. The roadmap now
separates delivered 0.8.0 three-host support and the unreleased Windows fix
from open work, updates the selected gz-skills version to 0.8.3 and replaces
blanket deeper-analysis UNKNOWNs with the bounded 0.8.0 receipt results.
Historical evidence remains intact; cognitive qualification, production mutation
score, desktop/other-platform proofs and embedded-host acceptance remain open.

Live GitHub inspection confirms that November 2 Actions scanning passed but
both uv jobs failed with required 0.13.6 versus updater-supported 0.13.5.
The roadmap links those runs and prioritizes resolving or explicitly tracking
the limitation, then an authorized adopter pilot, acceptance reporting, reviewed
upgrade/rollback tooling and remaining platform proofs. Each entry defines
completion evidence. The dependency guide's older pin/metadata descriptions
remain for reconciliation during the scan repair; no tool pin was weakened.
The November 7 upstream exception/readiness revisits remain due, not renewed.

This is documentation reconciliation only. No runtime, catalogs, resources,
adopter repository, native installation, issue, commit, push or release changed.
Verification with required uv 0.13.6 and managed Python 3.14.10 passed: locked
all-group sync, four routine hooks, bundle/catalog validation, source-independent
build and isolated installed-distribution checks. All 37 local Markdown link
targets across the three changed files exist; whitespace checks pass. No analyzer
implementation or authoritative wheel-resource input changed, so analyzer
regressions and resource regeneration are inapplicable to this documentation edit.

## Git synchronization and Windows correction — November 1

Fast-forwarded main from `ec0d3c4` to published 0.8.0 commit `e0b752f`.
Its Linux CI passed, but the local Windows gate found discovery identifiers
compared against native backslash paths: repeated configuration rejected its
own update skill for all three hosts. Normalize that identifier to POSIX form
and normalize relative paths in the scope-repair test. A regression exercises
the public configure preview with Windows path semantics on every platform;
it fails before the correction and passes afterwards.

Verification uses uv 0.13.6 and managed Python 3.14.10: locked all-group sync,
all four routine hooks (60 helper tests), bundle/catalog validation,
source-independent build and isolated installed-distribution checks pass.
The unchanged analyzer suite passes all 29 tests. The independent X-Plane
baseline sync and verifier pass on managed Python 3.12.16. The portability
audit reports no findings in the helper and test directories.

This is an unreleased compatible fix; published tags remain unchanged. Native
fresh-session discovery on this Windows checkout remains unverified:
`core.symlinks=false` produces placeholder files for the repository skill links.
Git synchronization and exact-commit CI are verified separately during the push;
no new release acceptance or publication is implied.

## 0.8.0 authorized release — October 31

The maintainer explicitly directed publication; no additional approval is needed.
The reviewed preparation commit is `f176c5e29e61fad0b792d9cd6012f3ab8d95f5c5`,
pushed to main with green CI run 41256392928. Final release metadata and native
development bindings follow in the release commit. The immutable v0.8.0 tag and
GitHub release identify the final SHA; verify them live before further work.

The [release receipt](../evidence/2026-10-31-0.8.0-release.md) supersedes earlier
same-day input observations: uv/uv_build 0.13.6, ty 0.0.95, setup-uv v10.3.3,
gz-skills v0.8.3 in both catalogs, existing Python patches retained. Both locked
baselines, 59 helper tests, 29 analyzer tests, distribution verification,
complexity, dependency audits and documented deeper checks pass within their
stated limits. Cognitive qualification remains under the standing maintainer
exception; complexipy is historical reproduction only. Backplane stays disabled.

Fresh native discovery and canonical skill bytes match the new selections.
Codex's earlier requested-0.8.0/cache-0.8.3 mismatch is resolved by explicitly
selecting published 0.8.3; this does not relabel the earlier failure. Claude's
project-only update resolves 0.8.3. OpenCode uses the required scoped launcher.
User settings/global installations remain unchanged. Desktop picker and other
native-host/embedded-runtime limitations remain explicit. The separate upstream
dependency-skill candidate remains unpublished; no dependent release is implied.

## Three-host local ownership and brownfield repair — October 31 (unreleased 0.8.0)

The final inherited-source test exposed OpenCode 2.2.0's duplicate-ID failure:
its earlier source wins despite a later project pin. Added `run-opencode`, a
scoped native launcher using versioned native environment options, not a host
rewrite. It reconciles ordinary preferences in memory, excludes inherited plugin
declarations/ancestor config, preserves explicit repo skill paths and starts a
private server. It blocks global add/remove and shared-server attachment. The
same fixture now reports the correct project targets active. Use this required
route on 2.2.0; clean-project success alone did not establish brownfield behavior.
User settings and installations remain unchanged. See the receipt's correction.
Final change verification passes: locked all-group sync, four routine hooks with
59 unittests, bundle/both catalogs, source-independent build, installed-wheel
host/repair checks and explicit Ruff C901. uv 0.13.5 and managed Python 3.14.10
were used. Temporary native test servers are stopped. No tag/release or Git
synchronization was performed; the 0.8.0 candidate remains in the worktree.

Latest operator direction: all three target hosts must obey repository-owned
selection, activation and commands. Existing global/user copies may remain;
do not uninstall them or rewrite user defaults to repair a project. The starter
is an emphatic engineering standard: mandatory steps, prescribed commands and
actual evidence; no convenient substitute or configuration-only acceptance.

Implemented `configure --host codex|claude|opencode` with matching native project
settings and update-skill discovery; default remains Codex for compatibility.
Non-Codex adoption records carry additive `host`; old records retain Codex.
Implemented `localize --host` as independent preview/apply scope repair. It reads
inherited Codex/Claude identities, suppresses duplicate sources in repo settings,
repairs Claude's local override layer, and places OpenCode ID exclusions before
its full-SHA package targets. It preserves adoption records, existing project
marketplace selections, adopted component pins and unrelated settings. JSONC
updates preserve comments and source bytes outside changed native fields.
Simultaneous JSON/JSONC files and OpenCode v1 adapter migration need explicit
reconciliation. No native installer is called by the helper.

Template/pyproject/uv lock now identify development 0.8.0, a coherent minor for
this capability/policy bundle. No component/tool/runtime pins were refreshed and
no release/tag is published. Existing earlier policy edits remain in the worktree.
The update skill and wheel resources are reconciled. Starter development now has
Codex, Claude and OpenCode project settings; both repo skill links resolve to the
single canonical update skill. No starter self-adoption lock/profile is created.

Native macOS checks: Codex 0.166.0 discovers 36 starter entries in a trusted
fixture and none outside. Claude 2.1.316 native installs succeed at project scope
for fixtures and this starter; inventory reports enabled inside/disabled outside.
OpenCode 2.2.0's persistent server loads both upstream v2 adapters at exact SHAs,
discovers 15 SP + 20 gz-skills + update skill and none outside. Initial short-lived
OpenCode queries can finish before background package installation; wait for real
server state. User settings snapshots remain unchanged. See the
[three-host receipt](../evidence/2026-10-31-three-host-repo-scope.md).

Codex's gz-skills cache still contains 0.8.3 despite the requested 0.8.0 ref.
Scope proof does not close exact-pin acceptance; that failure remains explicit.
Desktop selectors/model invocation and other operating systems remain UNKNOWN.
The upstream dependency-skill candidate described below remains uncommitted and
unpublished in its separate source checkout. No cache surgery or global install
was used. Full release acceptance, cognitive qualification and Backplane readiness
remain separate from this change's repository/native-scope verification.

## October 31 native development skills and repository scope (unreleased)

The operator clarified the 0.1.0 rationale: the first substantive release is
the first versioned public-contract commitment, without claiming 1.0 stability.
They also supplied a specific Codex CLI 0.166.0 observation: `plugin add`
unconditionally enables a plugin user-wide even from a project with a local
marketplace. Native install/update guidance now prohibits that shortcut and
separates installation, version changes and enablement. Preserve project
activation, user defaults and duplicate-source overrides, and verify actual
revisions and outside-project scope. This clarification uses the operator's
observation; no user-wide install was run to reproduce it here.

Subsequent operator direction makes freshness review completion actionable:
strongly recommend a concrete supported upgrade batch and explicitly offer to
apply it; carry out already-authorized updates without repeating permission.
The internal/adopter instructions, Python policy and maintenance guide bind this
behavior now. The upstream skill correction is prepared in the clean checkout
`/tmp/gz-skills-maintenance-20261031` (base
`9a7970208207d68cc4a04eff7c3d39bcea664463`), with pending skill 0.3.1/bundle
0.8.4 and synchronized metadata/uv lock. Its 28 unittests and source/wheel
builds pass. It is uncommitted/unpublished and is not installed or selected by
this starter's unchanged gz-skills 0.8.0 pin.

The versioning policy and adopter workflow now allow `0.0.0` only as an
unpublished bare-scaffold placeholder. Once original implementation, tests,
documentation or configuration is added, use initial project version `0.1.0`;
do not release that original work as `0.0.0`. Preserve published history.
Claude Code 2.1.316 help confirms `--scope project` for both marketplace-add
and plugin-install; the native guide now gives those exact commands.

Live cache state subsequently changed: the gz-skills installation under the
starter marketplace now resolves to 0.8.3 / Git HEAD
`d6acc26e28ca1c4f43e5bb46d8973021d7d006c3` despite native inventory declaring
the requested 0.8.0 source ref. A scoped native marketplace upgrade reports
already current and does not repair this mismatch. Treat final exact-pin
discovery as UNKNOWN; retain the earlier passing observation as historical.
Do not patch/delete native caches to force agreement. Desktop Computer Use
inspection is blocked by the tool's app-access restriction. User config hash
remains unchanged. See the updated discovery receipt for limits.

The operator explicitly requested native skill use in this starter and requires
repo/project-scoped installation, registration and activation for adopters too.
Do not use global/user-level installation or unscoped install/marketplace-add
commands as a fallback. Shared native download caches are storage, not user-wide
activation. The adopter fragment, native installation guides and starter AGENTS
now make that rule explicit; generated wheel instructions must stay in sync.

Development `.codex/config.toml` selects the published v0.7.1 Git catalog, enables
SP/gz-skills here, suppresses the duplicate gz-skills source and keeps Backplane
disabled. A relative repository skill symlink exposes canonical
`update-gz-template` for explicitly identified adopter work. No self-adoption
lock/profile is created. A fresh macOS CLI 0.166.0 app-server discovers 15 SP,
20 gz-skills and the update skill from both root and `src/`, with no discovery
errors. An independent `/tmp` runtime discovers none of these. User config
remains byte-identical. See the
[native receipt](../evidence/2026-10-31-native-development-skills.md).
Desktop picker/model invocation, Windows symlink checkout and other hosts remain
UNKNOWN; refresh the desktop client and start a fresh project chat to inspect
its native selector. Repository checks and final results are recorded in the
receipt; this work does not publish a release or synchronize Git.

## October 31 direct CLI guidance (unreleased)

The maintainer requires direct `gh` commands for GitHub operations and direct
`git` commands for repository operations, both internally and in adopter
instructions. Routine CLI calls must not be wrapped in Python. Reserve Python
for substantive processing through the prescribed locked, uv-managed environment,
honoring the exact interpreter pin and required uv version. Updated starter
AGENTS.md, the adopter fragment, Python policy and generated wheel-resource copy;
the changelog records this as unreleased guidance.

Verification with uv 0.13.5 and managed Python 3.14.10: locked all-group sync,
all four routine hooks, bundle/catalog validation, source-independent build and
isolated installed-distribution checks passed. No analyzer behavior changed.
Native skill discovery remains separate; this session does not expose SP or
gz-skills, and no plugin configuration or installation was changed.

The operator requested Git synchronization of this guidance. A fresh origin
fetch confirmed `main` and `origin/main` aligned at
`ec0d3c43d4d70445adbb58d03c06adbf076004a2` before committing the six reviewed
files. The required local gate passed again with uv 0.13.5 and managed Python
3.14.10; nested hooks resolve the same uv. Push normally and observe CI for the
final commit, reporting the remote identity and result without another
receipt-only commit. Existing cognitive and host-readiness limitations remain;
this sync does not prepare or publish a release.

## October 26 policy alignment

The operator designated this template as the authoritative shared policy
alignment source for gz-skills and Backplane. The source contract is
`docs/versioning.md#ecosystem-policy-authority-and-consistency`. Both companion
repositories now have local `docs/release-policy.md` bindings and AGENTS pointers:
check this source before release preparation, at scoped policy/tooling maintenance
and when notified of relevant changes; record source identity, applicability,
decisions and approved exceptions. SemVer and the newly written major-release PRD
rule apply prospectively, including independently versioned skill majors.

Backplane owns requirements tracking, labels, backlog/release monitoring,
handoffs and lite/heavy mode definitions. Its local
`docs/superpowers-backplane/modes.md` records this authority and separates intended
scope from implemented readiness. The template references it and retains shared
engineering/release policy, configuration and provenance; it supplies no competing
lifecycle. Keep existing profile values and the setup schema. Companion policy
alignment does not require circular template adoption, synchronized versions or
imposing starter requirements on unrelated consumers.

Reviewed clean starting commits: starter `eef2e858bba709988eb859b17739d2989d8825ab`,
gz-skills `dca86e61bed3aa610555ef30a9ecccf4bd380f2a`, and Backplane
`15b04adbdd01033087d31d8ade6ab98504669e8c`. The source bindings record the starter
base SHA plus hashes of the edited working-tree policy inputs. Reconcile final
committed revisions before claiming published alignment; the new cross-repository
links have been verified against local files, not published remote content.

Validation on Windows with required uv 0.13.5 and managed Python 3.14.9: locked
all-group sync, regenerated wheel-resource instructions, all four routine hooks,
bundle/catalog validation, source-independent build and isolated installed
distribution checks pass. Cross-repository link targets, source hash receipts
and whitespace checks pass. Companion changes are repository documentation only;
no shipped skill tree, runtime pin, plugin installation or native issue changed.
This task does not close the prior deeper-analysis or Backplane readiness gaps.
The operator subsequently requested Git synchronization of all three repositories.
Publish this reviewed source first, then bind the companions to its exact commit
and push their reviewed documentation. Reuse the passing checks for unchanged
inputs and retain normal commit hooks. Verify final remote identities and any
configured CI; report final results without another receipt-only commit. This
does not authorize a tag or release, or complete the deferred acceptance work.

## Current state

Published **v0.7.1** at `27594dbaec853e6bde037b0aaf3f0427a3f053f9` without
waiting for the upstream engine, as explicitly directed. Remote annotated tag
`0562a205f918007aaee53b3dce49d24e30bd3c6f` peels to that commit.
[Both exact-commit CI jobs passed](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/40428666883).
The stable release has four verified asset digests; its downloaded wheel installs
separately, reports 0.7.1 and validates catalogs. The release receipt records
publication details. Earlier preparation/hold statuses below are historical.

Issue #1 is open as **Integrate and qualify the gzkit cognitive engine when
available**, with its milestone cleared and no promised date. Milestone 0.7.1
is closed for the delivered consumer preparation/Ruff patch. Do not reintroduce
an upstream delivery-date hold or claim actual engine qualification. The
following documentation commit records publication/backlog state; verify its
own CI when syncing, without moving the release tag or adding receipt-only loops.

Latest direction supersedes the engine release hold: the maintainer cannot
promise when the gzkit-owned engine will arrive and explicitly directed release
of 0.7.1 without waiting. Ship the prepared consumer checks and Ruff 0.17.3 patch;
retain the cognitive exception. Issue #1 stays open as unscheduled engine
integration, outside the 0.7.1 deadline. No private engine, extraction project,
gzkit mutation or plugin installation is authorized. The candidate-specific
receipt is `docs/evidence/2026-10-26-0.7.1-release.md`; require exact-commit CI,
immutable annotated tag, published stable status and verified assets.
Local release checks pass with managed Python 3.14.10 / 3.12.16, required uv
0.13.5 and Ruff 0.17.3: four routine hooks, 39 adoption tests, all 29 analyzer
regressions, X-Plane probes, C901/Lizard, exact-lock audits and runtime dependency/
import checks. The receipt records limits; real engine scoring remains unperformed.

The operator resumed issue #1, then clarified that the shared cognitive engine
will come from gzkit soon. Consumer preparation for unreleased 0.7.1 now includes
42 fixtures, installed-engine qualification/provenance, independent corpus
inventory and ceiling enforcement. It contains no scorer, private fork or
extraction project. Read `docs/engineering/cognitive-integration.md` and
`docs/evidence/2026-10-26-cognitive-consumer-preparation.md` before continuing.
No engine is installed or qualified; actual corpus scores and eventual
exact-commit CI remain pending. Keep issue #1 open and the 0.7.0 exception in
place until the real upstream candidate is pinned, qualified and measured.
Local preparation passes the complete routine/artifact gate and all 29 explicit
analyzer regressions on managed Python 3.14.10 / uv 0.13.5. The project .venv is
3.14.10; the uv package-manager pin is not a Python 3.13 selector. The lock only
changes the starter version to 0.7.1; dependency pins are preserved. No commit,
push, issue closure, plugin installation or release occurred in this preparation.

Published **v0.7.0** on October 26 at
`a02635dad451f8f89c7801c2cbc02e2ec453d369`; remote annotated tag object
`b13299760c3ccdd33696fcbf13fff6f749397ee0` dereferences to that commit.
[Both exact-commit Linux CI jobs passed](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/40409167397).
GitHub reports a published stable release with all four asset digests matching;
the downloaded wheel installs separately, reports 0.7.0 and validates catalogs.
The user-directed cognitive exception remains explicit in the release notes.

After publication, cognitive qualification was booked as
[issue #1](https://github.com/tvproductions/gz-skills-first-starter/issues/1) in
[milestone 0.7.1](https://github.com/tvproductions/gz-skills-first-starter/milestone/1).
The follow-up documentation commit records that booking/publication proof; it
does not implement cognitive scoring, publish 0.7.1, change code-version metadata
or move the release tag. Observe CI for the final documentation SHA as part of
sync; do not create another receipt-only follow-up. See the release receipt's
publication confirmation for final source/asset identities.

The maintainer subsequently authorized publishing 0.7.0 without waiting for the
cognitive qualification correction, then booking that correction as 0.7.1.
Read `docs/evidence/2026-10-26-0.7.0-release.md` and its JSON companion for the
candidate-specific freshness/acceptance review. Python 3.14.10 and ty 0.0.92 are
now selected; both hygiene groups declare the previously required deeper tools.
Actual deeper checks, reviewed low-severity/static findings and bounded
actual-package mutation samples are recorded without weakening thresholds.
Cognitive acceptance remains explicitly deferred, not passed; gz-skills 0.8.0
is a retained noncurrent selection with owned revisit. Require final exact-SHA
CI, annotated tag, asset digests and published GitHub status before reporting
release completion. Do not publish 0.7.1 or start the cognitive implementation.

Follow-up: the operator selected Dependabot exploration/implementation. Weekly
uv jobs now target `/` and `/baselines/xplane`, with a GitHub Actions job.
The separate dependency-only X-Plane project selects Python 3.12.16 and its own
uv lock; a CI job runs bounded standalone tool probes. No simulator package or
embedded runtime was installed. See `docs/engineering/dependabot.md` and the
dated `docs/evidence/2026-10-26-dependabot.md` receipt for current results.
The operator permits scheduled scans and reviewed update PRs here; adopters
choose starter updates, direct upstream updates or both, and their own timing.
The blanket schedule ban was corrected in AGENTS/current policy; historical
evidence is unchanged. Embedded-host compatibility remains separate from
standalone tests. Auto-merge, publication, plugin installation and dependent-repo
edits remain outside this work.

The operator then invoked `gz-skills:gzs-git-sync` for this complete change.
Pre-sync origin fetch: main and origin/main aligned at
`35ac057`, with only this session's policy, Dependabot and X-Plane baseline work
pending. Required uv 0.13.5 gates and the separate managed Python 3.12.16 probes
pass; the receipt records details. Commit/push this reviewed unit with hooks,
then observe both CI jobs for its exact SHA. Final sync/CI results are reported
after push without creating a CI-receipt-only commit. Hosted Dependabot scan and
real update-PR behavior remain separate proof, not established by CI alone.

Initial save point `a53a5db` reached origin/main. Standard CI passed; X-Plane
failed before sync because required uv 0.13.5's embedded download metadata did
not supply 3.12.16 on the clean Linux runner. The correction pins Astral's newer
official metadata in the X-Plane project's uv settings, preserving exact Python
and uv requirements. All three initial hosted scans completed successfully;
actual update PRs remain unobserved. The receipt records run links, the source
manifest SHA/checksum and the local-project lookup exclusions. Push the corrective
commit normally and verify its own CI; no earlier green job covers that SHA.

At the earlier October 24 session recheck, a fresh origin fetch confirmed main and
origin/main aligned at `731495876ef131c1a0795d38ad69116b77a594ca`, with a clean
worktree and no divergence.
[Exact-commit Ubuntu CI passed](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/40137030752).
This handoff refresh is a subsequent documentation change; verify its containing
commit with Git and its own CI rather than assuming the preceding run covers it.

Latest published release: **v0.7.1**, with the explicit cognitive exception and
retained component/host limitations. Engine integration is open and unscheduled.
No adopter migration or upstream-project change was performed.

## Published-release verification

An adopter reported that 0.6.0 was unpublished. Live GitHub CLI and remote-tag
queries on October 24 confirmed that
[v0.6.0 is published](https://github.com/tvproductions/gz-skills-first-starter/releases/tag/v0.6.0):
`publishedAt` is `2026-10-24T15:35:45Z`, with both draft and prerelease false.
The annotated remote tag object is
`1e33e51cd696eafd90db52d14b89b2f079160336`; its release commit is
`c0a6945b2170e1cf5bee3e80738916f5b62d13a5`. The wheel, source distribution,
portable update-skill ZIP and checksum assets are present. The report conflicts
with the observed canonical release state; the adopter's cause was not diagnosed
and no adopter files were changed. No republication or tag change was needed.

The user then requested handoff and Git synchronization. Scope is this existing
handoff's verification update only; reuse the passing checks for unchanged
code/tool/catalog inputs, run the normal commit hooks with required uv 0.13.5,
push main normally and observe CI for the final SHA. Report that result after
the push without creating another CI-receipt-only commit. Version 0.7.0 remains
unreleased, with the acceptance work below still open.

## Decisions to preserve

- Ordinary GZ projects use the stable Python minor one behind the newest
  stable minor (N-1): currently 3.14, with the latest verified patch. Current
  execution pin is 3.14.9. The documented XPPython3 host exception is separate.
- Baseline tools must use the latest verified stable releases across families;
  exact pins ensure reproducibility, not evergreen freshness. Follow the
  dated toolchain receipt rather than assuming installed versions are current.
- Cognitive scoring retains ceiling 15. Complexipy is a defect reproducer,
  not qualified acceptance authority. The user selected gzkit's scoring approach
  and intends a small external GitHub/PyPI project later. That work is deferred:
  **leave gzkit untouched on this machine**, create no extraction project and
  introduce no private starter fork as an incidental continuation.
- Gz-skills maintenance skills were unavailable in this session. Follow the
  documented direct fallback without requiring plugin installation. Availability
  in a catalog does not prove installation or discovery. Backplane stays disabled.
- The user identified weak internal maintenance discipline in dependency projects
  as a concern. This session did not audit or repair those repositories. Providing
  a maintenance skill alone does not prove that a supplying project uses it.

## Verified and unfinished work

The local routine gate passes, including 39 adoption tests. Thirteen analyzer
regressions, C901/Lizard checks, bundle/catalog/resource validation,
source-independent builds and isolated installed-artifact checks also pass.
Cosmic Ray has a bounded synthetic compatibility proof, not a measured mutation
result for this starter's actual production code. CI passes the routine and
artifact gate; it does not run the full deeper-analysis suite.

Open acceptance items must remain explicit:

1. **Known cognitive qualification failure:** complexipy misses keyword-value
   conditionals. The candidate gzkit scorer fixes that fixture but omits
   functions under module-level loops/match. The proposed shared engine is
   neither integrated nor qualified. See the
   [extraction assessment](../evidence/2026-10-24-gzkit-cognitive-extraction.md).
2. **Unperformed deeper analysis:** Interrogate, Vulture, Bandit, branch/statement
   coverage, deptry, pip-audit and applicable Import Linter contracts/results;
   actual-project mutation analysis is also unperformed. Missing results are
   UNKNOWN, not demonstrated code defects. Cohesion is explicitly an adopter-owned
   requirement; do not invent a helper-validation failure from its absence here.
3. **Incomplete effective-configuration proof:** project settings, tool paths and
   Ruff discovery were inspected, but applicable ancestor/user/system configuration
   precedence was not fully verified.
4. **Separate host-readiness gap:** native skill discovery was not verified for
   this checkout/session. Do not equate it with a Python build failure or require
   installing gz-skills here simply to validate the package.

Next release-preparation work should complete the nondeferred applicable analysis,
review findings, close configuration proof and refresh candidate-specific evidence.
Keep the cognitive dependency explicitly deferred until the user resumes it.
Do not describe Git sync as completion of this acceptance work or waive the gates.

## Git sync and future handoffs

AGENTS.md now owns a Git synchronization ritual independent of installed skills:
review scoped changes, use the required uv/interpreter, run applicable checks,
commit with hooks, push normally, verify the final remote SHA and its CI, then
report the worktree and remaining blockers. Keep sync, acceptance and publication
separate. No plugin, dependency-repository change or release is incidental to sync.

Handoffs are ordinary dated files in `docs/handoffs/`; AGENTS.md and README link
to the current entry. There is no automated handoff manager or enforced schema.
Keep material decisions, observed checks and unfinished work here, with links to
evidence; inspect live state on resume. Do not create repeated commits merely to
record CI for each preceding documentation-only receipt commit.
