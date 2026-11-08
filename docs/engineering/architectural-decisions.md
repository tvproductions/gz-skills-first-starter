# Architectural decision policy

This starter policy applies to both lite and heavy adopters and to the starter's
own development. Use the project's existing authorities and suitable ADR
conventions. The starter owns this mandatory binding; gz-skills owns the portable
procedure/template, SP owns feature workflows and Backplane owns its existing
planning/tracking integration. Adopt no GZKit ledger or lifecycle through it.

Source: the [operator-accepted lightweight guidance and sample](https://github.com/wtcis-pvecob/cob_projects/blob/dd1ab883c04e884678ed723959b17c5c364263d1/docs/engineering/proposals/2026-11-07-gz-adr-workflow-discussion.md#final-audience-guidance),
as bound by the approved starter design. Starter distribution follows ADR-0001
(`docs/decisions/ADR-0001-001-qualify-exact-component-combinations.md` in the
canonical starter source identified by the recorded revision):
qualify exact reviewed component combinations; keep independent versions/releases.

## Recognize, reuse and align

During design, implementation and review, inspect applicable decisions and
accepted constraints before introducing consequential choices about ownership,
dependencies, interfaces, persistence, recovery, trust, deployment or operation.
Reuse applicable approved decisions and cite them; do not demand another ADR or
approval for routine work within their scope.

For a new, conflicting or materially replacement choice, explain the choice,
credible alternatives, consequences and material uncertainty. Draft the ADR and
obtain separate explicit human approval of its identified edition before
dependent implementation. A design, plan, green test or release approval does
not substitute. Pause only dependent work, including for choices discovered
mid-implementation; continue independent authorized work. Surface conflicting
authorities rather than selecting an undocumented winner.

Recover existing justification first. Investigate important gaps proportionately;
require neither a new research artifact nor external precedent for every ADR.
Code shows what exists, not necessarily why it was chosen or approved. Disclose
inference and unknown history. Correct implementation drift against an approved
choice; do not rewrite the choice to bless conflicting code.

## Keep the decision and its approval together

Keep the choice, scope, context, credible alternatives, rationale, consequences,
approval metadata and amendment history in the ADR. Include a Confirmation
approach when useful; keep test output, progress and delivery claims in existing
verification/planning records. An optional index only helps locate decisions.

For a new collection, use `ADR-0001-001-title-in-kebab-case.md`: stable unique
decision identity, positive integer edition and descriptive title. Never reuse
an id. Preserve suitable existing conventions through an explicit semantic
mapping, not blanket renaming. The starter's own collection is `docs/decisions/`.
Project instructions must identify the project's actual collection.

Authoritative records use Current or Retired and carry `id`, `title`, `revision`,
`state`, `decision_date`, `revision_date`, `approved_by`, `approved_revision` and
`approval_ref`. Use actual YYYY-MM-DD dates and the authorized human's project
identity. Drafts confer no authority; do not fill approval fields with invented
values or mark an unapproved record Current.

Approval evidence must preserve the actual explicit approval of the identified
edition and its reviewed content. Use a retrievable conversation/review reference
and immutable content reference, or preserve the actual interaction with its
source context, date, identity and exact reviewed bytes/hash. Evidence may be
embedded in the ADR or durably referenced from it; no separate receipt file is
mandatory. Label an agent transcription honestly. A hash/commit identifies
content, while only the actual human response establishes approval. Preserve
the proposal before administrative approval capture and disclose that transition.

## Preserve history and independent evolution

Keep earlier editions retrievable by version history or an existing preserved-
document mechanism. Keep the latest filename as the working ADR and repair
affected links after renames. Approval references retain the reviewed edition.

For editorial changes that preserve the choice, scope and constraints, increment
the edition, update its date/filename and record the previous edition, edit,
editor and existing review/change reference. Preserve the original decision
date and approved revision. Use ordinary documentation review; no architectural
reapproval or additional reviewer is required for a typo. Surface uncertain
meaning rather than calling it editorial. A materially changed choice receives
a new, separately approved ADR.

Retirement requires explicit authority, date, reason and a replacement reference
where applicable. Preserve the record and approval history. Do not disguise
retirement as an editorial amendment. Backfill honestly: distinguish documented
approval, observed code, inferred rationale and unknowns. Disclose unsupported
historical dates as unknown; obtain missing approval now without backdating it.
No blanket historical backfill is required by this binding.

Decisions, requirements, features, designs/plans, evidence, instructions and
releases evolve independently. Links express applicability and constraints,
not one-to-one containment, matching versions or automatic revision cascades.
Recheck affected relationships after changes; amend a record only when its own
meaning/applicability changes. ADR approval adds no data, migration, deployment
or publication permission. Preserve and use existing authority without redundant
requests.

## Access, workflow availability and qualification

Project instructions may identify an immutable source link, a repository-local
policy copy, or both. Record starter version/full SHA, source path and original
content hash for local copies; preserve and review project adaptations. When a
local copy is selected, use it as the identified working policy and retain the
canonical link for comparison. Surface applicable local/source conflicts;
do not silently switch sources or overwrite project changes. If required policy,
procedure or approval content is unreadable, report the gap and withhold affected
completion claims while continuing independent authorized work.

Consult the exact selected gz-skills portable procedure/template when its owning
delivery is verified. The selected gz-skills 0.8.3 is not claimed to deliver the
new ADR contribution. Until owning designs/releases and qualification evidence
exist, use this explicit project binding without claiming the portable workflow
is installed, discoverable or qualified. Heavy mode uses existing supported
Backplane records; no new approval ledger/service is introduced. When Backplane
is disabled, retain existing planning/review/handoff tools in either lane.

Before adopter propagation, require immutable released companion contributions,
full shared behavioral evaluation plus targeted binding checks (including both
missing-approval stopping and approved-decision continuation), and genuine
internal use/alignment review in all three publishers. Expand affected evaluation
when bindings change shared behavior or expose discrepancies. Record exact
sources, loaded configuration, actual observations and limitations in existing
release evidence. Configuration, metadata and passing helper tests alone prove
none of behavioral compliance, native discovery or approval.
