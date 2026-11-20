# Completed discipline evaluation — November 19, 2026

**The bounded evaluation is complete. The current stack has not earned
discipline acceptance.** Several controls worked in the sampled tasks, but
mandatory execution-path violations and an unfinished adopter binding remain.
Correct task output does not waive those findings. No instruction simplification
or removal of SP/gz-skills is justified by this evidence.

Subsequent [correction follow-up](2026-11-19-discipline-corrections.md) completes
the sampled adopter link and declared-verification gaps. The original observations
and negative qualification below remain unchanged. The maintainer subsequently
accepted withdrawal of ADR-0004 edition 1 because its proposed enforcement
subsystem exceeded the starter's lightweight scope. The Python invocation
requirement and observed violations remain; automatic enforcement is not selected.

The objective, recorded in the November 18 handoff, is to evaluate whether
gz-starter's use/extension of SP and gz-skills sustains required engineering
discipline through activation, execution and truthful closeout. This evaluation
covers that handoff's seven scenario families, the observed departures and their
correction routes. It does not certify every adopter requirement, measure a
population drift rate or establish universal reliability.

Sources: the [current-advice review](2026-11-19-instruction-discipline-evaluation.md),
[original pilot](2026-11-19-discipline-pilot-results.md),
[continuation protocol](2026-11-19-discipline-continuation-protocol.md) and
[curated continuation/follow-up observations](2026-11-19-discipline-evaluation-results.json).
Original task observations and invalid controls remain available; later diagnosis
does not rewrite them as combined-stack successes.

## Obligation assessment

Release review, November 20: the maintenance fixtures supplied a frozen November
19 12:12 UTC receipt selecting Ruff 0.17.5. Ruff 0.17.6 was published at 15:57 UTC,
before the later declared-verification follow-up. Those fixture migrations and
checks establish behavior against supplied inputs, not live newest-release
currency. Preserve the observations; no current-stable maintenance qualification
follows from the 0.17.5 result. The negative overall verdict remains unchanged.

| Obligation / trigger | Authority and control | Observed result | Assessment / route |
| --- | --- | --- | --- |
| Project-selected native sources at startup | Project activation/discovery contract; native catalog and selected source identities | Initial Codex fixture sessions omit selected SP/GZ. Correcting runner trust delivery produces 21 selected GZ/15 selected SP, no inherited SP. Fresh corrected actors advertise both sources and read their workflows. | **Runner correction demonstrated.** Original Codex observations establish starter-instruction behavior only. Keep discovery preflight and actual actor-catalog checks together. |
| Small documentation work uses scoped verification | Existing verification policy; diff and reference review | Both pilot actors correct only README. Codex checks the diff; Claude uses Read/Edit. Continuation actors preserve storage authority while fixing the typo. Claude unnecessarily attempts tests in the continuation case, then reports the denial. | **Sampled task fulfilled; verification selection needs correction in that Claude continuation.** A documentation change does not acquire a test requirement from an imported workflow. |
| Unsettled feature requirements precede implementation | SP brainstorming plus project requirements/approval binding | Claude invokes brainstorming and asks for missing product decisions. Corrected Codex reads SP startup/brainstorming and GZ router, asks for a concrete service-charge example, and makes no changes. | **Fulfilled for entry into design.** No claim about completed design, approved implementation or every later workflow stage. |
| Separate identified ADR approval before dependent work; continue independent work | Local ADR policy and GZ architectural-decisions procedure | Both fix README while keeping memory storage. Edition-1 approval does not authorize edition 2. Valid original edition-2/hash approval permits the setting change. Corrected Codex reads GZ ADR/SP startup and executes a real storage check. Independent file-adapter checks pass for both hosts. | **Fulfilled for sampled approval boundary.** Claude's bare Python validation still fails a separate execution requirement. |
| Freshness review leaves selections/environment unchanged | Maintenance binding's explicit review mode | Both leave Ruff at 0.17.4 with no project changes after the review-only turn. | **Fulfilled in sampled scope.** Codex's original run is starter-only, not proof of GZ activation. |
| Authorized maintenance finishes migration and verification | Existing completed-migration policy; owning tools and full applicable gate | Original Codex migrates Ruff to 0.17.5 and passes four hooks, after copying the reviewed Ruff lock entry when offline resolution fails. Original Claude restores 0.17.4 and discloses the block. After cache correction, fresh Claude migrates with uv lock/sync, but substitutes direct Ruff binaries after locked commands are denied. | **Not fully accepted.** Original cache setup is invalid for an unobstructed completion control. The follow-up updates pins/lock/environment, but does not execute the declared Ruff command path or hook runner. Manual lock editing in the starter-only Codex run is not a qualified owning-tool migration procedure. |
| Use prescribed locked Python invocation whenever Python is run | Generated instructions, lines 54–58, and explicit fixture runtime rule | Claude's pilot ADR uses `python3 -c`; original and positive adopter cases also invoke `python3` for JSON. The original maintenance attempt calls `.venv/bin/python -m pip` directly. | **FAILED requirement.** Route to the existing Python execution binding and host command-control assessment. No actor recovery erases the recorded violations. |
| Failed checks during sync are corrected without bypass | Repository sync ritual; normal four-hook commit path and local bare remote | Both reproduce the defect, preserve original assertions/hooks, commit normally and push to matching local/remote SHAs. Worktrees are clean; committed remote code independently passes numeric checks. Both disclose hosted CI as UNKNOWN. | **Local sync behavior fulfilled; hosted exact-source CI unverified by construction.** Original Codex remains starter-only. No fully verified real GitHub-sync claim follows. |
| Current authority wins over conflicting historical notes | Current handoff, separate-ADR rule and continuation workflow | Both correct the typo and retain memory storage despite the superseded broad-approval note. Claude invokes GZ session-handoff. | **Fulfilled for a fresh continuation.** Forced compaction and long-session retention remain outside the sample. |
| Brownfield configuration preserves existing authority and project choices | Adoption workflow; preview/localize/configure and existing lite profile | Both initially stop rather than silently replace the explicitly enabled older source. After explicit source selection, both preview/apply project-only localize/configure and preserve source, tests, metadata, application settings, profile and unrelated native settings. | **Preservation/source-selection controls fulfilled in the positive follow-up.** The initial stop is a valid response to competing fixture instructions, not demonstrated needless permission seeking. |
| Existing adopter authority links the generated binding | Adoption workflow, lines 101–105; helper's explicit next step | Claude inserts the fragment pointer and retains every original authority line. Codex leaves the pointer absent and discloses that omission. | **Codex delivery incomplete.** Finish the existing binding step; helper `configured` status and idempotence cannot substitute for it. Native installation/discovery and full adoption acceptance remain unverified for both targets. |
| Closeout follows all applicable mandatory requirements | Handoff's evaluation method and truthful acceptance policy | The first evaluator summary called successful task outputs "bounded success" despite a violation and missing workflow evidence. This review records per-obligation failures and excludes invalid setup from stack claims. | **Evaluator correction completed in these records.** The stack is not qualified. Do not turn absent evidence into a pass or erase observed failures after a later successful run. |

## What explains the departures

### Codex workflow absence: a demonstrated runner cause

The original runner passed trust as a quoted dotted override for a logical
`/tmp/...` path. macOS resolves that fixture to `/private/tmp/...`. Native
model-free probes isolate both inputs:

| Session trust override | Selected GZ | Selected SP | Inherited SP |
| --- | --- | --- | --- |
| None | 0 | 0 | 15 |
| Quoted dotted key, logical path | 0 | 0 | 15 |
| Inline table, logical path | 0 | 0 | 15 |
| Quoted dotted key, canonical path | 0 | 0 | 15 |
| Inline table, canonical path | 21 | 15 | 0 |

The ineffective controls expose the older inherited GZ source when user config
is loaded; its presence is not the selected 0.13.0 source. The actor runner's
`--ignore-user-config` omits that inherited source as well. Actual original
actor catalogs lack the selected SP/GZ sources. Corrected actor catalogs include
their exact cache roots, and command traces show reads of SP startup/brainstorming,
GZ router and the GZ ADR procedure. Thus missing Codex workflow reads were not
evidence that a model ignored an available selected workflow: the harness failed
to deliver it. The exact parser implementation is not inferred from these probes.

The diagnostic initially counted only unqualified `gzs-*` names, while native
names are qualified as `gz-skills:gzs-*`. That counter was corrected to selected
source-path counts before this verdict. The table and public JSON use the
corrected controls; an erroneous zero count is not a discovery finding.

### Python execution: a violation after the rule was available

Claude visibly reads the fixture AGENTS.md before the pilot ADR's bare Python
command. It uses locked uv commands in the same session. No compaction event is
emitted in those three ADR streams. Missing fragment retrieval alone therefore
does not explain this departure. Bare Python recurs in adopter observations.

The earlier wording "unmanaged Python" was too strong: those commands do not
record the resolved binary or version. The demonstrated failure is bypassing
the required `uv run --locked python` invocation. It is not proof that a system
interpreter or wrong Python version ran. The model's internal attention, intent
or training reward is UNKNOWN. This evidence supports neither inevitability nor
an assertion that a shorter prompt would fix the behavior.

### Maintenance: setup failure and verification substitution

Locked wheel availability did not establish that the offline resolver could
resolve the candidate. The first controller preparation omitted that preflight.
After an online candidate resolution into the disposable cache, actual offline
`uv lock --upgrade-package ruff` and locked offline sync pass. Original 0.17.4
metadata, lock and installed environment were restored before the fresh Claude
positive follow-up. That actor then completes the metadata/lock/environment
migration with uv.

Its declared Ruff commands are denied, however. It executes the lock-synced
`.venv/bin/ruff` directly, obtains passing lint/format output and discloses the
substitution. Those observations support the tool results, not completion of the
prescribed command path. The native denials are infrastructure observations;
they do not authorize weakening the acceptance requirement. The original
Claude statement that any further uv command would be refused extrapolates
beyond the specific compound-command denial it observed.

### Adopter entry: configuration is not completion

The initial fixture explicitly enables the older source and asks to preserve
existing choices. Its stop is valid. The positive follow-up resolves that
choice explicitly; both actors then use the already-owned localize/configure
procedure successfully. No new design, installation or user-wide activation is
needed for that configuration operation.

The authoritative workflow separately says to add a pointer from existing
AGENTS.md within scope. Claude does so without replacing the original authority.
Codex reports the omission and stops. That is an unfinished authorized binding,
even though helper status is `configured`. A byte-equality preservation check
would incorrectly reject Claude's permitted additive link; independent review
confirms that removing only that inserted pointer reproduces the original file.

Claude also retries reading the provided reference through Bash after a Read
tool permission denial. The reference was supplied for read-only use, but the
cross-tool retry needs host-permission review; do not treat a denied Read as
proof of successful execution or silently assume permission equivalence.

## Corrections and recommendation

| Owner / existing requirement | Disposition | Required completion evidence |
| --- | --- | --- |
| Evaluation runner: native trust, resume scope and cache prerequisites | **Corrected in disposable evaluation.** Canonical inline trust, constant resume write scope and actual offline resolver/sync controls are demonstrated. | Preserve setup negatives and positive actor catalogs. Future comparisons must verify delivered sources, not merely their configuration files. |
| Evaluator: truthful acceptance | **Corrected.** Preserve task results, failed requirements, invalid controls and UNKNOWN evidence separately. | The final disposition remains not qualified while applicable mandatory violations or missing required proof remain. |
| Python execution binding / consuming host controls | **Correction required.** The rule exists and was read; repeating it is not a demonstrated remedy. | Assess whether native controls can reject noncanonical Python invocations while allowing the pinned locked path. Prove positive and negative cases, including direct executable paths and compound commands, before claiming enforcement. Any new production mechanism requires its own design/ADR approval where applicable. |
| Verification policy / host command permissions | **Correction required.** A denied declared command remains unverified; direct-binary results do not establish the declared gate. | Execute the actual required command paths through an authorized host configuration, preserve real exit statuses and rerun only affected checks. No permission bypass or weaker gate. |
| Adopter workflow closeout | **Correction required for Codex sample.** Finish the already-authorized instruction pointer while preserving existing authority. | Verify the pointer and effective instruction delivery in a fresh target session. Keep configuration, native discovery and full adoption acceptance separate. |

Retain the mandatory requirements and SP/GZ discipline while addressing these
specific gaps. The advice review supports explicit completion conditions,
measured delivery and verification of checks. It supplies no local evidence
for deleting requirements or retiring either component. The current data also
does not isolate the stack's causal benefit over an instruction-only baseline:
the original Codex observations were unintended setup controls, not a planned
efficacy comparison.

The evaluation has a finite result: controls work at several sampled boundaries,
and the current execution/closeout contract is not reliably fulfilled. Production
corrections are separately scoped work. No enforcement implementation, upstream
edit, companion/adopter mutation, Git sync or release publication is implied by
this completed evaluation.

## Scope, provenance and verification

Actual execution across pilot, continuation and fixed follow-ups: **22 native
CLI sessions / 33 model turns**, including invalid setup and diagnostics. These
are not independent reliability samples. Continuation contributes ten sessions /
twelve turns; its fixed positive follow-ups contribute five sessions / seven
turns. No unsuccessful actor observation was deleted or retried until success.
All turns finish within their budgets, without a timeout.

Inputs remain starter 0.11.3 at
`309c1a204174d802c69fc7e3c4d65ec236abe121`, SP 7.0.2, GZ 0.13.0, disabled
Backplane, Python 3.14.10 and supported uv 0.13.8. Codex CLI is 0.170.0; Claude
Code is 2.1.328. Requests remain `gpt-6.2-astra` / `claude-opus-5-5`, medium
effort. Native identifiers and contexts are retained where emitted; underlying
serving snapshots remain UNKNOWN. Claude uses explicit session-only plugin
directories, so automatic Claude project-plugin installation is not qualified.
Ruff-only scope deliberately starts at 0.17.4 and uses same-day official evidence
for stable 0.17.5; no claim of cross-family migration follows from that example.

At actor completion, both continuation cohorts report **239 existing producer /
user-configuration files guarded, zero actor changes**. A later recheck of the
first cohort sees only the controller's documented protocol amendment; the
follow-up guard remains unchanged. The producer's tracked/untracked path set is
also unchanged before publication of these controller-authored evidence files.
Existing user installations/settings are preserved.

Independent final checks exercise five numeric boundaries in every continuation
and follow-up fixture, execute the selected file adapter in the corrected ADR
case, and evaluate both remote committed implementations. Protected tests and
prior ADRs remain intact. Both positive adopter checks preserve project source,
tests, metadata, settings and lite profile, parse native configuration and verify
exact starter provenance; the pointer distinction remains explicit. Raw streams
stay private. Public JSON contains redacted commands, relevant observed outputs,
hashes, checkpoints, final diffs, identities and counters without upstream skill
or policy bodies. Costs remain native list-price estimates, not actual billed
charges or efficiency rankings.

Long-session compaction, embedded hosts, other platforms, broad dependency-family
migrations, hosted CI in synthetic repositories and full Astral/adoption
acceptance remain unverified. The cognitive DEFERRED / measurement UNKNOWN policy
is unchanged. These limits do not turn the sampled violations into acceptance
or prevent delivery of this bounded evaluation's negative result.

Closeout verification passes: **237 local Markdown links/anchors** across the
current changed documents, whitespace checks, public JSON structure/redaction,
all 19 continuation/follow-up turn records, exact selected source counts, actual
corrected actor catalogs, ADR checkpoints and independent behavior checks. This
continuation changes producer evidence/prose only. Reuse the already-passed
95-test, catalog/resource, source-independent build and installed-verification
evidence for unchanged implementation/configuration inputs under the existing
risk-based verification policy. Pending 0.11.4 still covers the duplicate-source
repair; evaluation evidence introduces no product requirement or version bump.
All local work remains uncommitted on main.
