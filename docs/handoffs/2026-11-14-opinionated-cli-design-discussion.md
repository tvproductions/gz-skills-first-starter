# Opinionated enforcement CLI — design-discussion handoff

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

The maintainer selected structured single-file artifacts in lite, with a standard
schema, update rules and forward translation into SP-BP. The responsibilities are:

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
proposal. If the structured data warrants JSON, use a sidecar. Sidecar granularity,
field ownership, canonical-data versus projection roles, and narrative binding
remain open. Do not independently duplicate mutable facts across Markdown/JSON.

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

## Remaining design questions, in suggested discussion order

1. **Cognitive blocker:** remove/suspend it as a universal blocker until delivery,
   or prioritize producing the shared qualified engine? The maintainer demanded
   that we either skip or make it; no choice was finalized. The agent recommended
   centrally removing unavailable qualification as a blocker, which remains a
   recommendation. [Issue #1](https://github.com/tvproductions/gz-skills-first-starter/issues/1)
   was open/unscheduled. No threshold waiver, private scorer or extension of a
   release-specific/adopter-specific exception is authorized by this handoff.
2. **Enforcement architecture/ownership:** define the CLI boundary, portable
   SP-BP semantics versus starter-specific executable rules, location/versioning
   of Pydantic models, and interfaces that avoid duplicate script implementations.
   Reconcile current prohibitions on competing lifecycle ownership. Which
   existing modules need refactoring, and which helpers are retained/moved/retired?
3. **Record schema and authority:** exact headings, common metadata, stable IDs,
   criterion identities, state vocabularies, approval/evidence references,
   sidecar purpose and binding, and how schema upgrades preserve local content.
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
