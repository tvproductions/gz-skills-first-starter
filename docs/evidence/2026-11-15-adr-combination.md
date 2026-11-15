# Starter 0.10.0 exact-source ADR qualification

Status: **PASS within the stated observed scope**. Approved ADR-0001 edition 1
is reused; no replacement decision or waiver changes the release scope.
Final pre-publication independent review is recorded below. The final published
starter source is the immutable v0.10.0 tag; these inputs are identified by
catalog commit plus exact resource hashes, avoiding a self-referential SHA.

## Exact released sources and bindings

| Component | Release / immutable source |
| --- | --- |
| Starter catalog/policy/bindings | 0.10.0 candidate `9f0f27791713f735d960e44b18759a9fb63a61ae` |
| SP | 7.0.2 `22f0b463e7a5e579904dd6211a520321035526f7` |
| gz-skills | [0.13.0](https://github.com/tvproductions/gz-skills/releases/tag/v0.13.0) `0bdab63fc503c6b36e2dd487932689b4e555e41a` |
| Backplane | [0.3.0](https://github.com/tvproductions/superpowers-backplane/releases/tag/v0.3.0) `39fbe3065c16ac119c4c10a3c2428fda39d57e61`, disabled here |

Both catalogs agree with bundle.json. Codex/Claude project marketplace refs bind
the published starter catalog above; OpenCode selects matching component sources.
Parsed comparison confirms the ref is the only activation setting changed:
SP/gz-skills enabled, Backplane disabled, alternate gz-skills source suppressed,
Claude autoUpdate false. No user settings, native cache activation or adopters
were changed. Latest official GitHub releases were rechecked as SP7.0.2/GZ0.13.0/
BP0.3.0. Same-day maintained package/runtime/Action manifests and locks retain
exact recorded hashes; their freshness/audit/compatibility receipt remains valid.

Policy path is docs/engineering/architectural-decisions.md; canonical bytes at
that catalog SHA hash `a01343789f3cb1c2164073908ad6465e28651fe6fd16b2aaf37f3baca21e37b7`. Generated locks preserve
starter version/full SHA/path/hash and link/local mode. Link fixtures use the
pre-resolved exact immutable Git blob; local fixtures use their generated working
copy. This is available-source behavior, not proof of network retrieval.

Portable sources are skills/gzs-architectural-decisions/SKILL.md (skill0.1.0,
SHA256 a85b8a48fc700da52d65b5b61fa4ee525a1c0b7ffd303f02f753a26d5cf2339a)
and references/adr-template.md (SHA256
88fcf67e431e4df013b6c52b342361e9370adf15fc3f39b521d41f7aad706916).
Actual fixture reads match the delivered bytes; no upstream procedure is copied
into this product. Fresh separate native app-server inventory observes the enabled
ADR procedure and SP execution skill at recorded hashes; bounded native details
and the original inventory hash are in the adjacent JSON. Behavior actor manually
loads these sources. Native discovery and behavior are distinct observations;
normal-profile startup/loading, other hosts and actual model identity remain
UNKNOWN. Native catalog scope is Windows Codex0.169.0; actual behavior uses the
available Windows Codex test actor and PowerShell tools.

## Shared matrix reuse and targeted applicability

The full source-identical [B01–B16 record](https://github.com/tvproductions/gz-skills/blob/0bdab63fc503c6b36e2dd487932689b4e555e41a/docs/evidence/2026-11-15-adr-canonical.json),
[qualified inputs](https://github.com/tvproductions/gz-skills/blob/0bdab63fc503c6b36e2dd487932689b4e555e41a/docs/evidence/2026-11-15-adr-qualified-inputs.json)
and [complete canonical archive](https://github.com/tvproductions/gz-skills/blob/0bdab63fc503c6b36e2dd487932689b4e555e41a/docs/evidence/2026-11-15-adr-canonical.zip)
preserve actual prompts, fixtures, actions, failures/corrections and all sixteen
PASS verdicts. Canonical archive SHA256 is
62594620cd8fb993fcc9c5216ac79942a28562db28035e28d12a14e29873b2e8.
Exact procedure/template hashes above are unchanged. Starter changes distribution,
source-availability description and project binding; it does not change portable
semantics. Therefore reuse is limited to those unchanged procedures/declared
fixture-policy cases, supplemented by actual binding/access/precedence controls:

| Shared cases | Applicability / affected control |
| --- | --- |
| B01 recognition/drafting; B04 vague assent; B05 exact approval; B06 edition mismatch | Same approval/edition rules; targeted publisher/lite/heavy stops use wrong-edition approval, which supplies no applicable approval (B01 gate/B06 variant). Full choice recognition/drafting remains the shared B01 observation. |
| B02 reuse | Five actual binding continuations reuse matching reviewed edition-1 approval without duplicate ADR or approval request. |
| B03 conflict; B14 access/unavailable evidence | Both modes/provenance exercised; two adapted local copies require missing migration-owner approval. Local choice/edits win working-source selection, conflicts are surfaced, dependent changes stop and independent corrections continue. Shared unavailable-content cases retain their original scope. |
| B07 mid-work; B12 review drift | Same portable rules; active Backplane owner exercises five checkpoints and actual review drift. |
| B08 editorial; B09 material replacement; B10 backfill; B11 independent evolution | Same portable procedure/template and project semantic requirements; no new revision/lifecycle mechanism. Backplane typed records preserve these relationships. |
| B13 permission; B15 human initiation; B16 weak justification | Same portable authority/initiator/evidence semantics; local fixtures perform only authorized local work, with no publication inferred from fictional approval. |

The [Backplane owning integration](https://github.com/tvproductions/superpowers-backplane/blob/39fbe3065c16ac119c4c10a3c2428fda39d57e61/tests/scenarios/2026-11-15-adr-integration.md)
provides its sixteen-case applicability mapping, stop/continue at five affected
checkpoints, typed-record positive/missing/wrong-edition/stale controls, actual
complete-pair Git/file observations, review drift and neutral-consumer behavior.
Its product resources remain source-identical through the released SHA. Native
HTTPS installation, catalog observation and separate active controls are recorded
in [the owning publication receipt](https://github.com/tvproductions/superpowers-backplane/blob/cc0910aeb2d190aefeb04f15533ab82cc29a137e/tests/scenarios/2026-11-15-adr-publication.md).
[Exact tagged-source CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/43772211920)
passes Linux/macOS/Windows; downloaded source archive equals Git archive.
GZ's tagged Codex/Claude/OpenCode/uvx channels and assets are verified in its
[release receipt](https://github.com/tvproductions/gz-skills/blob/36377cb27638194e122f268781557a729c9bdf5c/docs/evidence/2026-11-15-0.13.0-release.md).
GZ has no configured hosted workflow; no CI pass is invented.

## Actual starter publisher and disabled adopter results

All twelve cases use invented approvals, never actual publisher authorization.
Existing ADR collection and BACKLOG/HANDOFF authority, explicit profiles and
Backplane-disabled configuration are preserved. Actual results independently
checked against file contents and all **140 protected input hashes**:

| Case | Final source authority | README / preservation |
| --- | --- | --- |
| lite-link-stop | local | PASS |
| lite-link-continue | remote | PASS |
| lite-local-stop | local | PASS |
| lite-local-continue | remote | PASS |
| heavy-link-stop | local | PASS |
| heavy-link-continue | remote | PASS |
| heavy-local-stop | local | PASS |
| heavy-local-continue | remote | PASS |
| publisher-local-stop | local | PASS |
| publisher-local-continue | remote | PASS |
| lite-local-conflict | local | PASS |
| heavy-local-conflict | local | PASS |

Five covered changes proceed; five wrong-edition and two local-adaptation changes
stop. All twelve independent spelling corrections complete. Both lite/heavy
exercise link/local stop and continuation, local provenance, existing collection
mapping, source conflicts and project precedence. Heavy does not imply Backplane
activation. Targeted GZ publisher controls are in its canonical record; Backplane
publisher/active controls are in its owning record. Active integration does not
qualify disabled paths; these are separately exercised here.

The first nested CLI attempt inherited read-only permissions and made no reads or
changes. It is preserved locally as an environment failure, not a behavioral
verdict. The available test actor then completes the cases; its harmless path/
parsing/line-ending precondition errors precede writes and are disclosed. No
product correction or additional shared-matrix replay was required.

[Curated fixture archive](2026-11-15-adr-combination.zip), SHA256 `400c7edc70dd76e3ee9e1008aabc5c6b3023bd687d4e256bb011d6cf18df8fd6`,
contains 335 text entries: original/final invented fixtures,
exact prompt, input manifest, actor results and tool-action transcript. Machine
metadata/absolute paths are redacted with original/public hashes recorded;
complete originals and failed CLI records remain local. Raw CLI events/stderr,
profiles, authentication and install metadata are excluded. This bounded content
was inspected before publication. Adjacent JSON records independently observed
file outcomes and native/source hashes; exit status/keywords alone are not verdicts.

## Genuine internal use, review and release boundary

Each publisher used its own separately approved actual ADR-0001 edition1 before
dependent implementation, retaining original reviewed bytes and actual human
response. Fictional fixtures do not establish these approvals:

- Starter: [actual decision](../decisions/ADR-0001-001-qualify-exact-component-combinations.md)
  and [implementation/alignment review](2026-11-08-adr-practice-qualification.md).
  This release follows that decision by waiting for independently delivered
  companions and source-bound qualification. The current final review checks
  source/configuration/approval alignment without changing the choice.
- [GZ actual decision](https://github.com/tvproductions/gz-skills/blob/0bdab63fc503c6b36e2dd487932689b4e555e41a/docs/decisions/ADR-0001-001-standalone-architectural-decision-procedure.md)
  and [independent alignment review](https://github.com/tvproductions/gz-skills/blob/0bdab63fc503c6b36e2dd487932689b4e555e41a/docs/review/architectural-decisions-2026-11-15-final.md).
- [Backplane actual decision](https://github.com/tvproductions/superpowers-backplane/blob/39fbe3065c16ac119c4c10a3c2428fda39d57e61/docs/decisions/ADR-0001-001-reference-decisions-through-existing-checkpoints.md)
  and [independent alignment review](https://github.com/tvproductions/superpowers-backplane/blob/39fbe3065c16ac119c4c10a3c2428fda39d57e61/tests/scenarios/2026-11-15-adr-final-review.md).

Final starter review: focused independent review found two stale current-source
references, corrected in adoption/structure guidance. Source/configuration,
actual targeted results and protected hashes have no unresolved findings; final
receipt/archive/plan reconciliation is the remaining review closeout. No new
architecture approval or repeated case run is required.

Full locked starter gate, 72 tests, catalogs/resources, source-independent build
and isolated installed verification pass. Selection-source CI at catalog9f0f277
passes [both jobs](https://github.com/tvproductions/gz-starter/actions/runs/43774043523).
Final publication waits for its own exact committed-source CI, then immutable
annotated v0.10.0/GitHub release verification. Broader native/model/adopter and
cognitive/deeper-tool limitations remain explicit in the release acceptance;
this is conditional engineering acceptance, never full strict conformance.
