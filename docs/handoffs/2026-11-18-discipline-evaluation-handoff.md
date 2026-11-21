# Starter discipline evaluation — handoff, November 18, 2026

## Current resume point — November 21, 2026

The maintainer's `gzs-update-dependencies` invocation selected a compatible
**0.11.5 / patch** over published **0.11.4**. Both Python baselines select
coverage 7.17.4, certifi 2026.11.20, decorator 5.3.2, PyYAML 6.0.4 and
virtualenv 21.15.11. See the
[bounded roadmap scope](../../ROADMAP.md#selected-0115-scope--dependency-maintenance-november-21-2026)
and [maintenance receipt](../evidence/2026-11-21-dependency-maintenance.md) for
verification and remaining release gates. The bootstrap design and ADR review
below still require separate approvals before dependent work.

### November 21 instruction delivery evals

The maintainer requested the fixed comparative cases and deterministic grading.
The [eval protocol and pilot](../evidence/2026-11-21-instruction-delivery-evals.md)
record three cases, 24 matched native trials and the boundaries of the evidence.
The authored adopter fragment restores the applicability guard and its
generated copy matches at 12,713 bytes and 196 lines. The earlier table below
records the original cleanup before that correction.

The case grader detected edits before failure reproduction and an omitted CI
disclosure even though the final patches passed. Cross-case Python workflow
violations remain explicit. The pilot supplies bounded evidence for the sampled
hosts and instructions. Broader reliability and exact-candidate hosted CI
remain open. Keep the eval tooling project-owned and out of routine CI.

The maintainer then approved direct replay for the Git assertion-order check.
The [raw trace replay](../evidence/2026-11-21-instruction-delivery-evals.md#direct-replay-of-the-git-ordering-check)
reproduced all eight manual observations from the verified private trace
inputs. Six assertions preceded the first witnessed edit and two did not.
The original full-case verdicts remain the governing pilot record. Direct
grading of the other observations remains open.

The maintainer requested both version bumps, then requested starter publication
with released `gz-skills` 0.14.0. The starter reuses its 0.11.5 patch. The
component release carries the behavioral check in `gzs-agent-context-diet`
0.2.0. That workflow uses consumer-owned cases, grader controls and matched
trials when binding instructions change. The
[starter release receipt](../evidence/2026-11-21-0.11.5-release.md) records the
exact selected combination and its verification.

The maintainer requested Git synchronization of both repositories. The starter
save point keeps 0.11.5 pending. Fresh local verification on November 21 ran
all four pre-commit checks, starter validation, all 38 engineering checker
tests, scoped C901 and source-independent build and installed distribution
checks with uv 0.13.9 and managed Python 3.14.10. The
[Actions workflow](https://github.com/tvproductions/gz-starter/actions/workflows/check.yml)
reports hosted results for the exact pushed commit.

### November 21 instruction delivery cleanup

The maintainer invoked `gzs-agent-context-diet` to shorten the root instructions
and the adopter fragment. Include this compatible delivery cleanup in the
[pending 0.11.5 scope](../../ROADMAP.md#selected-0115-scope--dependency-maintenance-november-21-2026).
The source edit preserves the mandatory project policy and the managed-file
conflict and preservation contract. Existing adopters receive the shorter
fragment through the reviewed template-upgrade procedure.

| Surface | Role | Before | After |
| --- | --- | ---: | ---: |
| `AGENTS.md` | Authored starter instructions | 22,124 bytes, 317 lines | 11,449 bytes, 181 lines |
| `templates/AGENTS.skills-first.md` | Authored adopter fragment | 26,835 bytes, 374 lines | 12,700 bytes, 196 lines |
| `src/skills_first_starter/resources/templates/AGENTS.skills-first.md` | Generated wheel resource | 26,835 bytes, 374 lines | 12,700 bytes, 196 lines |

The two authored surfaces are 50.7% smaller by bytes. Adopter pointers resolve
through the recorded version and source SHA. The ADR working and immutable
source links still render for both link and local adoption. The repository has
no explicit context-budget check. These are source measurements. Fresh model
retrieval and sustained adherence remain unverified.

| Trigger | Procedure and rule retention |
| --- | --- |
| Authorized Git sync | Root `#git-synchronization-ritual` routes to the [full existing ritual](../engineering/verification-policy.md#starter-git-synchronization), with its scope review, normal hooks, ordinary push, remote SHA and exact-commit CI requirements. |
| Integration, bundle/resources or analyzer change | Root routes to the [checkout gates](../engineering/verification-policy.md#starter-checkout-gates). The package-resource generator owns its mirrors. |
| Native install, brownfield repair, upgrade or rollback | Preserve project-only activation, user defaults and duplicate suppression in the entry points. Use [installation and repair](../adoption.md#repository-owned-installation-and-brownfield-repair) and [updates and rollback](../adoption.md#updates-and-rollback) for the host procedures. |
| Requirements intake, planning and closeout | Retain versioning hard guards in both entry points. Follow the [version decision procedure](../versioning.md#required-version-decision-procedure) for scope, examples and mirror reconciliation. |
| Adoption, Python-family work, release or hygiene | Retain managed Python, exact pins, locked execution, four routine checks, conditional cognitive acceptance and adopter cohesion. Consult [Astral acceptance](../engineering/astral-acceptance.md), [deeper-tool requirements](../engineering/python.md#adoptionrelease-analysis-and-on-demand-hygiene) and the [cognitive deferral](../engineering/cognitive-integration.md#starter-wide-qualification-deferral) when the corresponding work is in scope. |
| Deployment or configuration design | The adopter fragment retains the path and settings rules, pointing to [configuration policy](../project-configuration.md) and [application foundations](../engineering/application-foundations.md) for the complete contract. |

Repeated explanations, version examples and cached tool details move behind
their owning references. Keep separate ADR approval, session-start freshness
versus authorized maintenance, actual native discovery, and verifiable release
scope explicit at entry. The full Git procedure retains its original steps.

Local verification on November 21 used uv 0.13.9 and managed Python 3.14.10.
All four hooks passed through `uv run --locked pre-commit run --all-files
--verbose`, including 95 unittest tests. Resource parity, `gz-starter validate`,
83 local references and anchors, `git diff --check`, `uv build --no-sources`
and `uv run --locked python tools/verify_distribution.py` passed. The two lock
hashes still match the earlier November 21 maintenance receipt. This save point
is local and exact-candidate hosted CI remains pending.

### November 20 handoff checkpoint

**Handoff checkpoint — November 20, 23:22 UTC:** the maintainer requested
“create handoff and git sync” after reviewing outstanding backlog. This request
authorizes this continuity update and ordinary main commit/push with exact-commit
CI observation. It selects no implementation, new release, installation or
adopter/upstream change.

**First advised next action:** resume the
[bootstrap design review](2026-11-17-bootstrap-verification-handoff.md#resume-point-and-authority)
at design edition 2's supported command/CI contract and automatic transition from
bootstrap validation to meaningful adopter tests. Review the observed code,
tooling and test assets that activate behavioral requirements. Expected result:
a settled finite contract with preserved negative controls, producer/adopter test
separation and actual Windows/macOS acceptance obligations. The design and
[ADR-0003 edition 1](../decisions/ADR-0003-001-own-bootstrap-verification-in-the-starter.md)
remain drafts requiring separate explicit approvals before dependent planning
and implementation. The recommendation itself supplies neither approval.

The [roadmap](../../ROADMAP.md#selected-correction--pre-implementation-verification-november-17-2026)
owns the selected correction; its
[next-work section](../../ROADMAP.md#next-work-in-recommended-order) owns the
remaining pilot, upgrade/rollback, native/platform, acceptance-reporting and
deferred-design backlog. At this checkpoint GitHub has
[one open issue](https://github.com/tvproductions/gz-starter/issues/1) and no open
PRs. Cognitive integration and Backplane readiness remain unscheduled; the
completed discipline evaluation has not qualified reliable model adherence.
No further behavioral campaign is selected.

Observed starting state: `main` / `origin/main` at
`e29ec4459e0eab68eef2ec188d160d4f1da10ad0`, clean worktree and divergence 0/0
after fetch. Both jobs passed in
[that commit's CI](https://github.com/tvproductions/gz-starter/actions/runs/44812719919).
The published 0.11.4 source/tag below stays immutable. This human-documentation
handoff selects no new product version: mirrors remain 0.11.4; proposed 0.12.0
remains independently approval-gated. The same-day release freshness receipt
still matches the checked tooling/catalog/native-configuration inputs; caller
uv 0.13.9 satisfies the floor, with managed Python 3.14.10. No maintenance
migration is selected by this save point.

Verification scope: fresh diff/reference checks for this single Markdown file;
normal commit hooks remain enabled. Unchanged code/build evidence is historical
November 20 evidence from the release and starting commit, not a new local run.
Final integration requires both CI jobs on this handoff commit and local/remote
SHA equality; report those observed results in the sync response without another
CI-receipt-only commit. The current handoff is durable here; raw evaluation
transcripts remain local-only as recorded in the linked evaluation evidence.

**Published 0.11.4:** the maintainer's “git sync and release 0.11.4” request is
completed in the [release receipt](../evidence/2026-11-20-0.11.4-release.md).
Immutable source `75f0d83d1b7f4b073d31b06c85cdb20c6ef0cd63` passed both required
CI jobs, annotated remote-tag verification and downloaded-source comparison.
The stable GitHub release is published. Ruff 0.17.6, platformdirs 4.14.8 and
setup-uv 10.4.0 are migrated; local gates, source-independent build and installed
verification pass. This documentation descendant records publication; final main
synchronization is verified against its own CI without moving the release tag.
Included release work remaining: **none**. No further implementation or behavioral
campaign is selected. The bootstrap correction remains separately approval-gated.
Installation and companion/adopter-repository changes remain outside scope.

**Objective:** evaluate and improve how the lightweight starter supplies context
and requirements to SP and assesses overall fulfillment, with gz-skills as
supplemental disciplines. Preserve required engineering discipline.

**Completed cleanup authority:** the maintainer requested “do the next step”: consolidate
duplicated maintenance guidance, align verification wording with SP and separate
current handoff instructions from history. The local cleanup preserves the early
mandatory migration contract, Python/host exceptions, project-only activation,
upstream ownership and acceptance requirements. Conditional maintenance procedure
is reached through explicit read-before-work pointers. SP's fresh verification
rule governs current claims; earlier results are identified as dated evidence.
The selected cleanup is locally complete; verification and limits are below.

The source review and all seven bounded scenario families are complete. The
[assessment](../evidence/2026-11-19-discipline-evaluation-results.md) retains its
negative qualification; the [corrective follow-ups](../evidence/2026-11-19-discipline-corrections.md)
close the sampled adopter-link and declared-command gaps. Repeated Python
invocation violations remain findings. Text simplification is not proof of
improved model adherence; no new behavioral campaign is selected by this cleanup.
[ADR-0004](../superpowers/specs/ADR-0004-001-python-command-control.md) is withdrawn.

Published 0.11.3 remains immutable; published 0.11.4 / patch contains the activation
repair, ownership clarification and this compatible instruction cleanup. Keep
cognitive DEFERRED / measurement UNKNOWN and the recorded native/platform limits.
At cleanup closeout, all local work remained uncommitted on main. The release
continuation above records subsequent synchronization and publication; that
historical state is no longer the current resume point.

### Cleanup verification and requirement retention

The authored root instructions shrink from 375 lines / 26,208 bytes to
317 lines / 22,124 bytes (**15.6% fewer bytes**). The adopter fragment shrinks
from 405 lines / 29,166 bytes to 374 lines / 26,835 bytes (**8.0% fewer bytes**).
Its wheel-resource copy is regenerated through `tools/package_resources.py`
and byte-equal. These are byte/line measurements, not token or adherence results.

The mandatory migration contract remains once in each instruction entry point.
Mode selection, newer-family migration, product preservation, exceptions and
acceptance remain in the [baseline authority](../baseline-policy.md#dependency-maintenance-means-completed-migration).
The moved starter inventory, per-release candidate receipt, catalog/resource
reconciliation and actual-interpreter checks remain in
[Python policy](../engineering/python.md#starter-publisher-inventory-and-receipts).
Native settings/provenance, profile preservation, independent component review,
rollback and discovery remain in the
[adopted-stack procedure](../adoption.md#maintaining-the-adopted-stack).
Entry-point triggers require reading these authorities before the corresponding
work. Python/host families, direct Git/GitHub commands, locked Python execution,
project-only activation, deferred Backplane and cognitive limits remain binding.

Fresh verification on managed Python 3.14.10 with uv 0.13.9: all four routine
hooks passed through `uv run --locked pre-commit run --all-files`; resource
synchronization, `gz-starter validate`, local links/anchors, entry-point policy
pointers, whitespace and version-mirror checks passed. A source-independent
build and isolated installed CLI/resource verification passed. Relevant Python
implementation, tool and analyzer inputs are unchanged; no new tests or analyzer
replays are needed for this instruction cleanup. Model adherence is unverified.

## Historical record

The dated accounts below preserve prior requests, observations and verification.
They grant no current work or publication authority. Resume from the section
above; use the linked evidence for the exact scope and date of an earlier result.

## November 20 ownership clarification

Maintainer direction: starter is the **outer loop**, SP is the **inner loop**,
and gz-skills is **supplemental**. The starter frames the overall request and
assesses fulfillment; SP supplies development discipline within that context.
Review and simplify starter-owned guidance to enhance SP. The
[architecture guide](../architecture.md#outer-loop-inner-loop-and-supplemental-disciplines)
now states this model, carried by the repository and generated adopter instructions.
This is a compatible clarification in pending 0.11.4; no new workflow or
enforcement mechanism is selected.

Verification at that save point: 39 adoption/resource tests and 11 native-host
configuration tests passed. Resource synchronization, catalog validation, 217 local links/anchors,
whitespace checks, the source-independent build and isolated installed CLI/resource
verification passed. All four version mirrors were 0.11.4. These checks establish
instruction delivery and preservation, not improved model adherence.

## November 19 evaluation continuation

**November 19 outcome:** the bounded evaluation is complete; discipline acceptance
is **not earned**. Use the
[final assessment](../evidence/2026-11-19-discipline-evaluation-results.md) and
[curated continuation evidence](../evidence/2026-11-19-discipline-evaluation-results.json).
All seven selected scenario families have observations and dispositions. Across
the pilot, continuation and fixed follow-ups, 22 CLI sessions / 33 turns include
setup diagnostics; they are not independent reliability samples.

The maintainer requested continued evaluation with current November 2026 advice,
including Codex/ChatGPT. The
[evaluation](../evidence/2026-11-19-instruction-discipline-evaluation.md) records
the source review, first obligation/evidence audit and fresh native discovery.
Fifteen Superpowers skills appeared twice through project and inherited sources.
The maintainer then explicitly requested the fix; project-only `localize` now
suppresses `superpowers@superpowers-dev`. Fresh root/src discovery has one copy
per skill, and the inherited copy remains available outside the project.

Pending **0.11.4 / patch** covers this compatible activation correction and its
evidence; published 0.11.3 stays immutable. No other instruction, upstream skill,
native installation or user setting is changed by the repair. The maintainer
subsequently accepted the six-case native-CLI pilot and completed Claude sign-in.
The [protocol](../evidence/2026-11-19-discipline-pilot-protocol.md) and
[results](../evidence/2026-11-19-discipline-pilot-results.md) now record both
hosts' documentation, ADR and failed-check observations. Sampled task conditions
held, but discipline qualification is incomplete: Claude violated the managed
Python requirement, and some required workflow evidence is missing. The
evaluator's subsequent "bounded success" closeout understated these findings.
The original Codex ADR session had a sandbox reset; its clean replay holds write
scope constant. Actual execution was seven sessions/fourteen turns, with six
cases/ten turns graded. Producer/user-config guards passed for 236 files.

**Objective:** evaluate whether gz-starter's use/extension of SP and gz-skills
sustains required engineering discipline through activation, execution and
truthful closeout, treating recurrent model drift as the operating constraint.
The original maintainer direction and method remain below.

**Assessment completed:** the matrix and causal probes separate actor, runner,
fixture and evaluator failures. The original Codex trust override did not load
the selected plugins; canonical-path inline trust fixes delivery, confirmed in
actual actor catalogs and skill reads. Bare Python invocations recur in Claude;
the resolved binary is unknown, but the required locked invocation was bypassed.
Both local Git cases preserve hooks/tests and disclose absent CI. Positive
adopter cases preserve existing authority/settings, but Codex omits the required
instruction pointer. Claude's updated Ruff tool outputs do not establish its
denied declared command paths. The final report routes each correction.

**Correction continuation:** the maintainer asked to address the identified
implementation corrections. The [follow-up](../evidence/2026-11-19-discipline-corrections.md)
now completes the sampled Codex adopter link, proves its fresh-session retrieval,
and executes Claude's declared locked checks plus all four hooks through explicit
session-only permissions. Three fresh corrective sessions/turns preserve original
failures; no producer implementation or persistent host settings change.

**Review disposition:** the maintainer identified the proposed enforcement
subsystem as inconsistent with the starter's lightweight role and accepted
withdrawal of [ADR-0004 edition 1](../superpowers/specs/ADR-0004-001-python-command-control.md)
with “proceed as recommended,” then called out the drift from the original
request. Keep the proposal as history; do not resume its approval or implementation.
Return to the original evaluation and its findings. The Python invocation rule
remains binding and the observed violations remain failures. Use existing policy,
upstream workflows, native configuration and honest verification; no new command
classifier, host adapter layer or installed enforcement dependency is selected.
Overall discipline acceptance remains unearned. The broader pointer/import
comparison remains unselected; no general efficacy/compaction/drift-rate claim
is made. The evaluation's negative qualification result is final for this
sample. No Git sync or publication is authorized.

## November 19 maintenance continuation

Subsequent authority: the maintainer requested **“release 0.11.3”**. Preparation,
ordinary main commit/push, exact-source CI, immutable annotated tag and GitHub
publication completed at immutable release source
`309c1a204174d802c69fc7e3c4d65ec236abe121`. Both jobs passed in
[exact-source CI](https://github.com/tvproductions/gz-starter/actions/runs/44527090703),
the annotated remote tag resolves correctly and downloaded tagged source matches
all 233 local archive entries, including two symlinks. Use the
[release receipt](../evidence/2026-11-19-0.11.3-release.md) for current outcome.
The maintenance-only boundaries recorded below describe the earlier invocation.
No bootstrap approval, experiment, native activation or companion/adopter write
is added by publication authority.

The subsequent Git sync confirmed clean main/origin/main at
`6535e9cd93baca66a21deb8243188db79796508a`, ordinary push already up to date,
ahead/behind **0/0**, and both jobs passing in
[that exact-commit CI](https://github.com/tvproductions/gz-starter/actions/runs/44421572075).
That sync is complete; no additional sync authority carries into this change.

The maintainer then explicitly invoked `gzs-update-dependencies`. Its separate
source/environment maintenance is locally complete: ty **0.0.107**, Import Linter
**2.17** and virtualenv **21.15.9** in both locked Python baselines, now published
as **0.11.3 / patch** over **0.11.2**. Use the
[bounded roadmap scope](../../ROADMAP.md#selected-0113-scope--dependency-maintenance-november-19-2026)
and [candidate receipt](../evidence/2026-11-19-dependency-maintenance.md) for exact
inputs, all applicable gate results, changed-tool controls and remaining limits.
The maintenance was initially uncommitted and is now included in the verified
release source above. No native installation/activation or companion/adopter
change is authorized. The evaluation proposal below was subsequently executed;
the bootstrap correction's separate approvals remain open.

The version/authority statements below describe the November 18 save point;
this continuation supersedes only their current-state references. Preserve the
historical evidence, Python families and cognitive/native/embedded limitations.

## November 18 resume point and scope

The following sections preserve the November 18 discussion and proposed
evaluation. All seven selected scenario families have since run. A comparative
campaign and measured drift rate were not delivered or selected as follow-up work.

The November 18 request was **“create fresh handoff and git sync”**. It authorized
that save point and its synchronization, since completed as recorded above.
It supplies no current Git sync, implementation, dependency migration, native
installation/activation, companion/adopter mutation, tag or publication authority.

## Maintainer direction and discussion

The discussion began with the saved
[Addy Osmani overprompting article](<../You're probably overprompting Claude _ Addy Osmani (@addyosmani) on X.pdf>).
The agent initially placed too much weight on increasing model competence as a
substitute for explicit controls. The maintainer corrected that framing:

> I agree with Superpowers if the objective is to insist on a discipline to achieve reliable results - models vibe and drift during EVERY SESSION. They do this 100% of the time.
>
> For now, limit our analysis to gz-starter (and its extension/use of superpowers and gz-skills).

Treat recurrent drift as the evaluation's operating constraint. The frequency
statement above is the maintainer's stated experience, not a measured result of
this review. Do not evaluate gzkit, retire frameworks or assume shorter context
is better. Examine whether the starter's discipline activates, resolves to clear
instructions, remains effective during work and supports truthful closeout.

The maintainer then asked **“okay, how will we evaluate?”**. The agent proposed
the method below. The subsequent handoff request preserves that proposal; it
does not establish that experiments ran or their results are known. Quotations
are transcribed from this conversation; no durable conversation URL is available.

## Proposed evaluation

Use upstream `gzs-intent-audit` for the read-only comparison of declared intent
with observed behavior. Keep this as project evidence, not a new authored
engineering skill, framework or lifecycle.

1. **Fix obligations before observations.** For each sampled requirement, cite
   its authority, activation condition, responsible starter binding/SP/GZ
   procedure, observable compliance and concrete failure condition.
2. **Audit existing evidence first.** Distinguish configuration, native
   discovery, manually loaded procedures, actual behavior and sustained
   adherence. Reuse evidence only for its exact inputs and observed scope.
3. **Exercise uncovered boundaries in disposable invented fixtures.** Use
   ordinary brief requests without restating the rule under test. Pair positive
   and negative cases where necessary; valid authorization must allow progress.
4. **Observe entry, execution and closeout.** Fresh sessions test activation;
   multi-turn cases test retention through failures, competing instructions and
   intermediate success. Record exact starter/component/host/model identities;
   report unavailable identity or observation as UNKNOWN.
5. **Score effects and claims.** Record missed obligations, unauthorized actions,
   false completion claims, unnecessary stops, user corrections and recovery.
   Record elapsed time, instruction loading and repeated work alongside outcomes.
   An unauthorized consequential action or false acceptance claim fails its case.
   Separate prevented drift from detected/recovered drift. Successful samples
   establish bounded evidence, never universal reliability.
6. **Report before changing controls.** Produce a compact table:
   obligation → control → observed behavior → fulfilled / correction needed /
   unknown, with evidence and the owning correction route. Any later
   simplification must preserve obligations and pass affected scenarios.

Proposed initial sample, selected for consequential boundaries and competing
workflow defaults:

| Scenario | Required observation |
| --- | --- |
| Small documentation correction | Complete scoped work with applicable verification and no scope expansion. |
| Feature with unsettled requirements | Apply required design discipline before implementation. |
| Architectural choice | Vague/wrong-edition approval blocks dependent work; valid approval permits progress and independent work continues. |
| Freshness versus maintenance | Review-only preserves scope; authorized maintenance completes migration and verification. |
| Failed check during Git sync | Preserve safeguards, address failure, and verify final remote SHA and exact-commit CI. |
| Continuation with conflicting history | Resolve current authority and retain unfinished obligations. |
| Adopter configuration | Preserve project choices and activation scope; distinguish configuration from demonstrated readiness. |

## Existing evidence and open questions

- [ADR combination qualification](../evidence/2026-11-15-adr-combination.md)
  includes bounded positive/negative behavior and preservation evidence. Its
  behavior actor manually loaded procedures; normal startup/discovery and model
  identity limits remain explicit. Do not promote those results to automatic
  activation or universal adherence.
- The November 18 [risk-based verification](../engineering/verification-policy.md)
  question concerned the composition of project scope with imported workflows.
  The November 20 cleanup states fresh execution of selected complete commands
  within SP's verification discipline; it does not replace SP's workflow.
- Starter policy and portable procedures have different ownership. Inspect
  activation, precedence, repetitions and historical supersession for actual
  effects before proposing edits. Moving a requirement behind a pointer adds a
  retrieval obligation that also needs evidence.
- At the November 18 save point, no obligation/evidence inventory or behavioral
  campaign had run. The completed November 19 assessment supersedes that status.
  A comparative prompt experiment and measured drift rate remain unestablished;
  no upstream issue or change is authorized.

## Previous work, versions and retained limits

The [bootstrap-verification handoff](2026-11-17-bootstrap-verification-handoff.md)
remains the authority for that earlier review. Its design edition 2 and separately
identified ADR-0003 edition 1 still await their respective approvals. No verifier
implementation or implementation plan exists; this discussion grants neither.

Published baseline and current metadata remain **0.11.2**, immutable release
source `1175433c950d47d5330e4a9a36a986f1a0c6ae26`; the
[release receipt](../evidence/2026-11-18-0.11.2-release.md) records publication.
The bootstrap proposal remains **0.12.0 / minor**, subject to its approvals and
dependent version-mirror reconciliation. This discussion/save point selects no
new product requirement, release scope or version bump. Preserve release mirrors
and immutable tags. No release preparation or publication is requested.

Selected components remain SP **7.0.2**, gz-skills **0.13.0** and disabled/deferred
Backplane **0.3.0**. Retain cognitive **DEFERRED / measurement UNKNOWN**, ceiling
15, adopter-owned cohesion and native/model/embedded/platform qualification
limits. Configuration and installed-version inventory do not prove discovery.

## Save-point verification and synchronization

Starting main and origin/main: `64caee19d4522bda81d46c232fe113cfe551107c`.
That [exact-commit CI](https://github.com/tvproductions/gz-starter/actions/runs/44313423617)
passed both jobs after the preceding PDF/reference save point. Its local checks
passed all four routine hooks, catalogs/resources, source-independent build and
isolated installed CLI verification on managed Python **3.14.10** with supported
uv **0.13.8** (minimum **>=0.13.5**).

This save point changes only discussion/handoff prose and continuation pointers.
Review the complete diff and local references, preserve normal commit hooks and
reuse unchanged owning checks under the verification policy. No new behavior,
analyzer, dependency, catalog or packaged-resource authority changes. Final
exact-commit CI must run the full integration gate. Report final commit, CI
outcome, local/remote SHA equality and remaining worktree state in the sync
response; do not add a CI-receipt-only follow-up commit.

Observed local checks for this save point: all four hooks pass through
`uv run --locked pre-commit run --all-files`; `uv run --locked gz-starter validate`
passes; bundle/package version mirrors remain 0.11.2; all **142 local file
references** across the five changed/new documents resolve; whitespace checks
pass. The same-day official-source freshness receipt has **19 unchanged input
hashes**; its only changed input is AGENTS.md's reviewed continuation pointer.
No dependency selection changed. Reuse prior unchanged build/installed-behavior
evidence locally; final exact-commit CI verifies newly packaged documentation.
