# Instruction delivery evals implementation plan

**Goal** Compare the long and shortened starter instructions against the same
three observable policy contracts.

**Scope** Reuse the authorized design from the November 21 discussion and the
[November 19 pilot](../../evidence/2026-11-19-discipline-pilot-protocol.md).
This is a project-owned evaluation, outside routine CI and native tool
configuration. Keep upstream skills, adopter repositories and external remotes
outside fixture writes. Treat this as verification for pending 0.11.5. Preserve
the immutable 0.11.4 baseline and keep bootstrap design approval separate.

**Comparison** Use the original instruction sources at
`ec5b2f1379c0bcfe46d8850c0b02dcf4ef297dad` and the corrected short sources in
the candidate. Supply both arms with the same applicable policy, matching task
files and the same host/model/configuration per pair. Measure the root and
adopter entry points in their respective cases. Retain each run and disclose
unavailable trace evidence or infrastructure failures. A small pilot diagnoses
defects and supplies bounded behavioral evidence.

## Tasks

- [x] Define exact ADR approval, Git sync with a failing test, and class-free
  adoption acceptance. Pin the task and observation definitions before live
  runs. Use `tools/engineering/fixtures/instruction-delivery-v1.json` for the
  fixed case contract and `tools/engineering/evaluate_instruction_delivery.py`
  to grade normalized evidence. Keep task state, tool trace and final claim
  distinct. Validate the grader first using known compliant, violating and
  missing-observation controls in `tools/engineering/test_evaluate_instruction_delivery.py`.
- [x] Confirm the known wording defect, restore the applicability guard in the
  authored adopter fragment and regenerate the resource. Freeze the candidate
  before fresh comparative runs.
- [x] Run a paired native pilot in disposable fixtures. Capture per-turn Git
  and filesystem state, actual tool evidence and closeout claims. Keep original
  trials including failures. Report which host/case pairs were actually run
  and graded. Control false positives with independent pristine-state and
  failing-test checks. Do not give agents the grader or expected results.
- [x] Run the checker suite, full starter gate and build/installed proof for
  the changed resource. Record exact evidence and limits in the handoff or an
  evaluation receipt. Proven mandatory violations fail their trial. Missing
  required observations remain unverified. Git sync and publication are
  separate actions.

## Raw Git trace verification

The maintainer approved the first direct-evidence checker. Grade only the
existing `failure_observed` check. Use the saved native JSONL, a declared
fixture workspace and the receipt test's specific owning assertion. Preserve
the earlier manual receipt. The fixed controls exercise failure-before-edit,
edit-before-failure, unrelated errors and insufficient evidence in the native
record formats. An opaque operation cannot establish an ordering.

- [x] Add and run failing controls before the checker.
- [x] Implement the bounded Codex and Claude trace adapters and expose the
  verdict through the existing eval CLI. Preserve the normalized-grade command.
- [x] Replay all eight saved Git traces against the original manual result.
  Record agreements, differences and limits, then run the affected checker and
  starter gates and verify the packaged sources.

The [replay receipt](../../evidence/2026-11-21-instruction-delivery-git-trace-replay.json)
records eight matching observations and their witness lines. The 17 raw
controls, 38 checker tests, 95 routine unit tests, catalog and installed
verification passed. The changed Python files also passed the on-demand
C901 check. Raw traces were replayed on managed Python 3.14.10 on macOS ARM64.
