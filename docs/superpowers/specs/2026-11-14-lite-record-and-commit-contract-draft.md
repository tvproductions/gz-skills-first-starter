# Starter sidecars following Backplane: minimum contract draft

Status: design-review slice, November 14, 2026. This is not an approved full
implementation specification, identified ADR approval, implemented schema or
activated commit policy. No dependency, hook, companion repository or historical
commit is changed. The existing pending 0.10.0 implementation scope remains
bounded; the future record platform needs its own selected delivery scope.

## Intent and authority

The maintainer selected JSON sidecars for structured facts, Markdown for
narrative/generated views, a hand-written CHANGELOG, Git history and bounded
interrupted-write recovery. SQLite, Dolt, a permanent ledger and event replay
are excluded. Superpowers remains the feature inner loop. This document
proposes the minimum shared meanings and one small JSON record per commit.

The maintainer clarified that this is starter design following Backplane's
cues, not permission for this document to redefine Backplane. The starter MUST
maintain an explicit reviewed correspondence and trail compatible Backplane
evolution. Backplane retains its own semantic design authority. Useful proposed
extensions go through that repository's own design/approval/release process.
Independent components remain independently usable and versioned.

The maintainer subsequently authorized simultaneous design in the local Backplane
repository. Its paired draft is `docs/superpowers-backplane/specs/2026-11-14-lite-record-and-commit-alignment-design.md`.
Read the two candidates together: Backplane proposes the semantic contract and
starter describes its file/commit binding. Both remain local design candidates;
this coordination does not activate the November 7 release-doctrine transfer.

Reviewed Backplane main: `05505f8009989eb7514ec62750e33c78bc40abf9`.
The [governance](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/docs/superpowers-backplane/governance.md),
[native issue contract](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/skills/managing-superpowers-backlog/references/github-issue-contract.md)
and [checkpoint format](https://github.com/tvproductions/superpowers-backplane/blob/05505f8009989eb7514ec62750e33c78bc40abf9/skills/managing-superpowers-backlog/references/checkpoint-format.md)
supply the current design cues. Its checkpoint is a dated capture, not an
editable lite schema. Its November 7 release-doctrine draft is not activated
authority. This document supplies no new Backplane support guarantee.

## Approaches and selected boundaries

The selected storage approach uses current-state JSON, readable Markdown and
committed Git snapshots. A permanent JSONL ledger would add ordering/replay and
projection obligations. A database authority would make the selected sidecars
exports and introduce another persistence contract. Both are excluded.

For commit transport, recommend one custom Git trailer containing a single
compact JSON object. Multiple scalar trailers would require another field
encoding convention; free-form JSON in the body would need custom extraction.
The proposed single-trailer approach uses Git's existing parser and preserves
the small typed record requested by the maintainer. Its exact spelling/encoding
is proposed here for review, not activated policy.

## Common sidecar envelope

Each of the five structured artifacts MUST identify:

| Field | Proposed type and meaning |
| --- | --- |
| `format` | Literal `gz-starter-records/v1`; a format identity independent of product/template/plugin versions |
| `artifact` | One of `requirements`, `backlog`, `roadmap`, `work`, `releases` |
| `namespace` | Nonempty project-owned namespace for stable record identities |
| `records` | Array of typed records valid for that artifact; unique identities |

Each record has a stable `id` and discriminating `type`. IDs are unique within
the project namespace across the five artifacts. Work records separately
use Backplane's `kind`: capability, outcome, gate or external-boundary. IDs do
not encode mutable parentage, release membership or execution priority. Native
GitHub identities are separate mappings, populated only after observation.

Record references MUST distinguish a stable identity from the evaluated version.
Approval/evaluation references identify an actual locator and immutable revision
or exact reviewed content digest, with availability/limitations disclosed.
An unavailable reference is not an empty successful observation. A digest proves
identity, not adequacy or approval. Use these proposed typed references, aligned
with the paired Backplane draft:

| Reference | Exact fields and constraints |
| --- | --- |
| RecordRef | `namespace`: nonempty string; `id`: nonempty stable record ID; both required and no extra fields |
| SourceRef | `locator`: nonempty source location string; `revision`: string or null; `record_id`: string or null; `availability`: available/unavailable/redacted; all four required and no extra fields |

Known revisions use `git-commit:<full-lowercase-oid>`, `git-blob:<full-lowercase-oid>`
or `sha256:<64-lowercase-hex>`. Git OIDs are 40 or 64 hex characters as appropriate
to the repository's object format. The locator supplies the repository/path or
other source location; `record_id` selects a named record when needed. Available
approval/evaluation inputs require a known revision and readable evidence.
Unavailable/redacted inputs may retain known identities, but never support an
accepted claim that depends on unreadable contents. Missing evidence remains
explicit; do not invent revisions. Narrative section binding remains to specify.

Reject unknown formats/fields and invalid references rather than silently
dropping data or coercing types. Extension/version migration rules need explicit
specification. Schema validity alone does not establish semantic acceptance.

## Minimum field ownership and Backplane correspondence

| Sidecar | Required semantic groups | Backplane cues and open boundary |
| --- | --- | --- |
| Requirements | Stable statement keys, required wording/constraints, governing authority/revision, approval references | Requirement/Authority; preserve existing project PRD-equivalent authority |
| Backlog | Work identity/kind, objective, bounded allowed/excluded scope, work acceptance criteria, requirement coverage, parent/dependency relationships, explicit priority, lifecycle and closure reason | Native issue contract, Backplane Record and Coverage; never infer edges from ID spelling |
| Roadmap | Capability progression, milestone identities, forecast/target relationships and explicit deferrals | Capability/outcome graph and target grouping; finalized portable roadmap schema is missing |
| Work | Selected outcome references, approved plan/revision, plan-task progress, concrete blockers/resume targets, evidence/evaluation references and continuation context | Superpowers execution and Backplane handoff/PR/evaluation contracts; do not independently own outcome lifecycle |
| Releases | Published baseline, bounded selected outcome membership, target version/impact rationale, applicable gates/dispositions, publication authority and observed channel identities | Project release policy and native target grouping/publication; shared release-doctrine implementation remains pending |

CHANGELOG.md stays manually curated and has no sidecar in the minimum design.
Markdown generated sections are projections of the structured owner; narrative
remains editable source. File paths and generated-section markers remain open.

The minimum cross-record rules are:

- Distinguish requirement statements from bounded work acceptance criteria;
  maintain many-to-many coverage with contribution scope and combined-result
  ownership where relevant. Do not require redundant decomposition layers.
- BACKLOG owns outcome lifecycle; WORK owns selected execution/task progress.
  Reuse the six Backplane open lifecycle meanings and completed/not-planned
  closure meanings, with explicit eligibility/transition evidence.
- Satisfaction uses SATISFIED, UNSATISFIED or UNKNOWN against exact criteria and
  delivery inputs. Deferred/excluded/unresolved scope is a separate disposition.
  A task checkbox, commit, issue closure or milestone cannot manufacture a pass.
- Immutable project-owned evaluations retain old inputs/results. Current
  pointers and summaries derive from accepted evidence, not duplicate editable
  verdicts. Actual evidence remains in existing project-owned artifacts.
- ROADMAP forecasts; RELEASES selects actual release membership. Changed scope
  requires reconciliation. Published identities and membership remain historical.
- Promotion MUST map local keys/relationships/authority/evidence to observed
  native IDs, verify the transfer and switch each field's authority explicitly.
  Do not retain two mutable masters. Lite may remain permanent.

## Proposed per-commit JSON record

Use exactly one `Starter-Record` trailer in each governed new commit. Its value
is a single-line UTF-8 JSON object, with these required fields:

| Field | Proposed type and meaning |
| --- | --- |
| `format` | Literal `gz-starter-commit/v1` |
| `kind` | `implementation`, `fix`, `documentation`, `maintenance`, `integration` or `revert`; describes the change, not its SemVer impact |
| `records` | Unique RecordRef array, resolved against the committed snapshot and explicit external authorities |
| `evidence` | Unique SourceRef array for evidence/approval; no prospective CI/publication claims |
| `reason` | Nonempty concise explanation, including why empty references are appropriate when none apply |

These five fields and the reference types above are the proposed minimum.
Evidence references must identify the inspected revision; a moving branch URL
alone is not an immutable evidence reference. Affected records resolve through
the containing commit's snapshot or explicitly pinned external authority.

Documentation-only commits with no governed record change may use empty arrays
with an honest reason. Implementation/closure claims need applicable work and
evidence references; empty arrays cannot bypass that obligation. Commit metadata
does not itself approve design, satisfy criteria, select a release or authorize
publication. The containing Git commit already supplies tree/parent/commit
identity; do not embed its future SHA into its message or own tracked contents.

The companion [JSON example](2026-11-14-commit-record-example.json) is an invented
documentation-only record. The [message example](2026-11-14-commit-message-example.txt)
shows the identical object as one trailer. JSON remains in its own file and the
commit-message example, not embedded in management Markdown.

Require one recognized format and one trailer: reject duplicate keys/trailers,
unknown fields/enums, coercion and malformed JSON. Proposed maximum is 8,192 UTF-8
bytes for the JSON value; link large evidence rather than embedding reports.
Recommend deterministic serialization: fixed field order shown above, compact
separators, no multiline payload, and deterministic ordering only for arrays
whose semantics are sets. Preserve meaningful order in source records.

## How Git carries the record

Trailers are `Key: value` footer lines separated from the prose by a blank line.
Git's [interpret-trailers](https://git-scm.com/docs/git-interpret-trailers)
can add/parse them. [git log](https://git-scm.com/docs/git-log) can select a
trailer key and emit its value. Git treats the JSON as a value; the starter's
own schema/semantic validation supplies the additional discipline.

Local read-only demonstration from the repository root:

```bash
git interpret-trailers --parse docs/superpowers/specs/2026-11-14-commit-message-example.txt
```

To inspect a future governed commit, use:

```bash
git log -1 --format='%(trailers:key=Starter-Record,valueonly)'
```

This is ordinary commit-message content carried by Git, not Git notes, a new
tracked receipt per commit or a separate event stream. Amend/rebase/squash or
cherry-pick can change the containing identity/payload: reconcile metadata against
the resulting actual snapshot. Never rewrite published history to add records.

## Validation and unresolved engineering

Preserve exactly the four routine checks: Ruff check, Ruff format, ty and
unittest. Do not install another routine hook as part of this design. The owning
CLI can prepare/validate record content for an ordinary direct Git commit;
integration acceptance must validate actual resulting commits and state, not
trust that authors used the CLI. Decide that acceptance mechanism explicitly
before implementation. A CLI-only convention is not complete enforcement.

Pydantic is a candidate implementation tool for strict models and schema
generation. No dependency or model package is selected/installed by this draft.
Complete JSON parsing/type checks, referential checks and source/evidence
reconciliation are separate from semantic human approval.

Required proof includes: duplicate trailer/key rejection; invalid references;
wrong namespace/format; stale criteria/evidence; copied metadata after changed
payload; staged-versus-unstaged changes; coherent view regeneration; reached-fault
recovery with user edits preserved; merge/squash/revert/automation handling; and
verified lite-to-Backplane mapping without dual authority. Keep applicable
verification proportional and reuse unchanged-input evidence.

Remaining design gaps: narrative binding,
field-level model schemas, Backplane roadmap/release additions and review,
schema upgrades, migration proof, prospective adoption boundary
for every-commit metadata, and enforceable integration acceptance. Current
Backplane requires GitHub/gh. This design defines no additional hosting target.

This slice is ready for discussion, not dependent implementation. Architectural
ownership/persistence/interface choices require their separately identified ADR
edition and explicit approval under the existing policy before implementation.
