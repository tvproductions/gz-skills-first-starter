# Fresh ADR/release session handoff — November 15, 2026

## Resume point

The original request to complete the pending starter release is **unfinished**.
The latest request is **“fresh handoff and git sync”**. This save point resumes
neither implementation nor release publication. Preserve the approved release
scope; do not present a checkpoint or passing engineering checks as release
acceptance. The separately proposed enforcement CLI has not been implemented;
its name has not been settled. Keep that work out of scope.

First read the [release assessment](../evidence/2026-11-15-0.10.0-release.md), then
reconcile the owning gz-skills release procedure with its approved Task 3 and
[unverified OpenCode observation](https://github.com/tvproductions/gz-skills/blob/77ad2c792e0df39782271639c317e2c812b5a48e/docs/evidence/2026-11-15-0.13.0-opencode.json).
The owner procedure places exact tagged-channel checks after tagging/publication;
do not promote the previous agent's sequencing assumptions into new policy.
Determine the next required gate from that authority before another experiment.
If diagnosing native loading, establish a source-backed, falsifiable cause before
changing configuration. Expected result: one explained next action and its actual
observable outcome, not another collection of guesses. Stop dependent work if it
requires an unapproved architectural change or an explicit scope revision.
Continue independent work already authorized; do not request settled approvals again.

## Observed source and publication state

Observed 2026-11-15 21:12:48 UTC. Fresh fetches show all three saved checkpoints
clean and ahead/behind 0/0 in the workspaces below. The starter row is the starting
SHA for this documentation-only save point; the final sync response supplies the
new handoff commit and exact CI result without a self-referential receipt commit.

| Repository | Saved source / workspace | Published -> pending |
| --- | --- | --- |
| Starter | `main` at `1478a0bfc03ae34353f44f642bf24ec8a3e23395`; `U:\repos\agents\gz-skills-first-starter` | 0.9.0 -> 0.10.0 |
| gz-skills | Registered detached worktree at `77ad2c792e0df39782271639c317e2c812b5a48e`, equal to remote main | 0.12.0 -> unreleased 0.13.0 |
| Backplane | Registered detached worktree at `5904713f47fae21e94813327b4e2daa9878605e3`, equal to remote main | 0.2.0 -> planned 0.3.0; package still 0.2.0 |

Latest published releases above were rechecked through `gh release list`. No
0.10.0/0.13.0/0.3.0 tag or release was published by this work. Starter selections
remain SP 7.0.2, gz-skills 0.12.0 and disabled Backplane 0.2.0. Do not advance pins
or assert installed portable ADR availability from unreleased main-branch source.
Reuse the finite pending versions under their existing governing work.

## Completed work and trustworthy evidence

- gz-skills adds `gzs-architectural-decisions` 0.1.0, its template and router 0.7.0.
  This is Markdown instruction/catalog work, not a new CLI implementation.
  [Canonical qualification](https://github.com/tvproductions/gz-skills/blob/77ad2c792e0df39782271639c317e2c812b5a48e/docs/evidence/2026-11-15-adr-canonical.json)
  preserves B01-B16, availability/legacy/overflow supplements, publisher stop/continue,
  source hashes and raw ZIP evidence. Fictional approvals are labeled evaluation
  input. Actual model identity is UNKNOWN; observed behavior scope is Windows Codex.
- The [independent final review](https://github.com/tvproductions/gz-skills/blob/77ad2c792e0df39782271639c317e2c812b5a48e/docs/review/architectural-decisions-2026-11-15-final.md)
  found no defects and confirms genuine approved ADR-0001 reuse/alignment. The
  actual separate architectural approval and original reviewed bytes remain linked
  from each owning ADR; do not replace them with design/plan/release assent.
- Clean prepared gz-skills source `1af1b81001451eabc62133e6d48867d2ec6c9c13`
  passed 32 unittest checks, Ruff/format/ty, 21 skill validators, native Claude
  validators and reproducible/source-independent/installed package checks.
  Candidate Codex/Claude installs matched 21 skills/48 resources. Artifacts belong
  to that prepared SHA, not automatically to a later changed release commit.
- Backplane preserves partial tool updates, the frozen probe contract and 20 raw
  unscored captures. Four routine checks and nine adapter tests pass. Read its
  [partial-maintenance receipt](https://github.com/tvproductions/superpowers-backplane/blob/5904713f47fae21e94813327b4e2daa9878605e3/tests/scenarios/2026-11-15-adr-release-tooling.md).
  Product ADR integration is unwritten. Do not infer strict A01-A18/deeper-tool,
  installed-hook, SP conformance or native-install acceptance from this checkpoint.
- Exact previous CI is green for [starter 1478a0b](https://github.com/tvproductions/gz-starter/actions/runs/43758173997)
  and [Backplane 5904713, all three platforms](https://github.com/tvproductions/superpowers-backplane/actions/runs/43758071447).
  gz-skills has no configured hosted workflows. New starter handoff CI must be
  observed on the final pushed SHA. Current documentation-only verification uses
  [the repository policy](../engineering/verification-policy.md): review diff/links,
  preserve normal hooks, reuse unchanged source checks; add no behavioral tests.

## Remaining work and authority

1. Resolve required gz-skills native-channel evidence through its owning
   [approved plan](https://github.com/tvproductions/gz-skills/blob/77ad2c792e0df39782271639c317e2c812b5a48e/docs/superpowers/plans/2026-11-15-architectural-decisions.md)
   and release procedure. OpenCode 2.3.0 reads the selected fixture config but exposes
   zero candidate skills; root cause is **not established**, and no adapter defect
   or fix is proved. The attempted URI/directory/env/project-identity variants and
   short-lived private server did not establish acceptance. Do not repeat them.
2. Continue the [Backplane plan](https://github.com/tvproductions/superpowers-backplane/blob/5904713f47fae21e94813327b4e2daa9878605e3/docs/superpowers-backplane/plans/2026-11-15-architectural-decision-integration.md)
   from incomplete T1/T2 prerequisites, then baseline before T3 authorship. Required
   deeper changed-tool checks, scored conformance/native selection, actual integration,
   checkpoint preservation, genuine internal use/review and release remain open.
   Owner [issue #37](https://github.com/tvproductions/superpowers-backplane/issues/37)
   was created from the approved intake and last had one designing label. Re-read
   the full native intake/revision/blockers before any lifecycle transition.
3. Complete starter [Task 4](../superpowers/plans/2026-11-08-adr-starter-binding.md#task-4-assemble-behavioral-and-exact-combination-evidence):
   immutable companion deliveries, targeted publisher/lite/heavy controls, supported
   active Backplane integration, all three genuine internal uses and exact-combination
   qualification. Keep unrelated deeper/platform gaps explicit. Only then complete
   the original 0.10.0 release through its documented gates.

Prior explicit authorization covers the approved prerequisite plans and release
work; this handoff creates no new authority. Review substantive decisions in the
main conversation, never through side-question approval prompts. Preserve the
approved remote GZKit H5 naming precedent and Superpowers' **Native** execution
term. Do not reopen approved ADR editions or invent a replacement architecture.

The user challenged the elapsed time, repeated verification and whether work was
“vibe coding.” The prior OpenCode investigation made configuration guesses before
establishing a cause; that was acknowledged. Keep future work bounded and evidence
based. Do not build a new verification framework, repeat the unchanged complete
model matrix, launch extra maintenance threads or start the proposed CLI.

## Local-only material and preservation

Registered companion roots are
`C:\Users\Jeff\AppData\Local\Temp\gz-adr-prerequisites-20261115\gz-skills` and
`C:\Users\Jeff\AppData\Local\Temp\gz-adr-prerequisites-20261115\superpowers-backplane`.
Their shared Git directories are the respective original repositories under
`U:\repos\agents\`. Preserve these worktrees and ignored scratch until evidence
and continuation needs are met; do not reset original branches to align them.

- gz-skills scratch: `.superpowers/sdd/2026-11-15-architectural-decisions/`.
  Existing complete-tree hashes and canonical archives own replay identities.
- Backplane scratch: `.sp-bp/work/adr-integration/`; use this owner-approved area,
  not `.superpowers`, for Backplane execution artifacts.
- OpenCode fixture/binary: `C:\Users\Jeff\AppData\Local\Temp\g13o\p` and
  `...\g13o\bin\opencode.exe`; installed machine 2.1.4 was unchanged. Raw server
  stdout contains a temporary server password: keep it private and out of public
  evidence. No authentication/profile files should be copied. The owned test
  server was stopped; recheck current processes before reusing a recorded port.
- Original gz-skills checkout still has unrelated changes in `CHANGELOG.md`,
  `docs/evidence/2026-11-14-dependency-maintenance.md`, and `docs/release-policy.md`.
  Original Backplane still has its unrelated `docs/release-policy.md` edit.
  Preserve them; do not stash, sweep into commits, reset or force-push.

No implementation, dependency/native install, cleanup, tag, release, issue mutation
or additional experiment is part of this fresh handoff/Git-sync request.

Earlier context: [November 14 design discussion](2026-11-14-opinionated-cli-design-discussion.md) and [November 8 ADR save point](2026-11-08-adr-practice-save-point.md).
