# Starter discipline evaluation — handoff, November 18, 2026

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
change is authorized. The prior discussion below selects no implementation; its evaluation
proposal and the bootstrap correction's separate approvals remain open.

The version/authority statements below describe the November 18 save point;
this continuation supersedes only their current-state references. Preserve the
historical evidence, Python families and cognitive/native/embedded limitations.

## Resume point and scope

Resume the discussion of how to evaluate **gz-starter and its extension/use of
Superpowers and gz-skills**. Start with a read-only audit of existing intent and
evidence. The proposed behavioral evaluation below has not been executed or
approved as a complete experiment protocol. Establish its concrete fixtures,
host/session mechanism and bounded run scope before execution; preserve current
engineering requirements throughout.

The maintainer's latest request is **“create fresh handoff and git sync”**.
It authorizes this handoff, continuation-pointer reconciliation, applicable
verification, ordinary main commit/push and exact-commit CI observation. It
supplies no implementation, policy relaxation, dependency migration, native
installation/activation, companion/adopter mutation, tag or release authority.

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
- [Risk-based verification](../engineering/verification-policy.md) already
  overrides imported demands for a new plan, full suite, independent review or
  build replay on every small change. Evaluate whether that precedence works.
- Starter policy and portable procedures have different ownership. Inspect
  activation, precedence, repetitions and historical supersession for actual
  effects before proposing edits. Moving a requirement behind a pointer adds a
  retrieval obligation that also needs evidence.
- No completed obligation/evidence inventory, behavioral campaign, comparative prompt experiment,
  measured drift rate or simplification result has been delivered in this
  discussion. No upstream issue or change has been requested.

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
