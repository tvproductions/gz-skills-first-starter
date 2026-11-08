# ADR Starter Binding Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for native execution
> after plan review and the separate ADR approval below. Steps use checkbox
> (`- [ ]`) syntax. Do not start companion implementation through this plan.

**Goal:** Implement the starter's approved ADR policy binding and both policy
access forms, then prepare source-bound qualification without claiming unavailable
companion delivery or adopter readiness.

**Architecture:** Starter policy and concise pointers bind independently owned
portable procedures and existing Backplane tracking. Extend the existing
preview/apply/status helper and provenance lock for optional repository-local
policy content; retain immutable links in both modes. Qualify exact selected
sources through existing release evidence, with no new ledger or central service.

**Tech Stack:** Managed Python 3.14.10, uv >=0.13.5 (actual planning host 0.13.7),
stdlib, uv_build 0.13.7, unittest, Ruff, ty and the existing four pre-commit hooks.

**Spec:** [Approved starter design](../specs/2026-11-08-adr-practice-design.md),
governed by [#13](https://github.com/tvproductions/gz-skills-first-starter/issues/13)
under [#12](https://github.com/tvproductions/gz-skills-first-starter/issues/12).

## Global Constraints

- Published baseline 0.9.0 at `3f76acf0038b030bf5abd85ce4a419e890d3e420` ->
  pending 0.10.0, minor. Reuse this target; preserve version mirrors.
- Require separate explicit approval of
  [ADR-0001-001](../../decisions/ADR-0001-001-qualify-exact-component-combinations.md)
  before dependent implementation. Spec/plan approval does not supply it.
- Preserve both lanes, project authority, suitable existing ADR collections,
  profile settings, native activation and unrelated edits. Infer no profile.
- Keep decisions self-contained. Use Current/Retired and positive integer
  editions; preserve exact approval provenance, editorial history and independent
  evolution. Indexes are optional lookup aids.
- Add no generic starter workflow skill, ledger, Backplane capability, central
  CLI/core/runtime, upstream skill copy or fork. Integrate existing workflows.
- Keep companion designs, skill names, APIs and implementation in their owning
  repositories. No companion edits or issue mutations are authorized here.
- Install/activate no plugins. Change no component pins until owning contributions
  are released, reviewed and separately scoped for selection. Publish nothing.
- Use direct git/gh and locked uv execution. Keep Python family, dependency pins
  and hooks unchanged. Do not run pytest or introduce network access in configure.
- Implement no automatic migration/merge/rollback product. Preserve conflicts
  using the existing review/reconciliation route and transactional file writes.

## Review Focus

1. A repeated configure with no policy flag must preserve a recorded local choice.
   Task 2 tests omission, explicit repetition and rejected mode changes.
2. A local policy edit, symlink or concurrent write must survive failed adoption.
   Task 2 tests all-write rejection, containment and rollback at the public seam.
3. An installed wheel must supply exact policy bytes without a source checkout or
   network. Task 2 tests UTF-8/newline hashes and source-independent installation.
4. A legacy lock must not acquire an implicit approval or silent migration.
   Tasks 2 and 3 preserve old bytes and require reviewed reconciliation.
5. A configuration success must not imply available ADR skills or qualified
   behavior. Tasks 1 and 4 check explicit gaps and stop/continue controls.

## Execution boundaries and interfaces

Execution approval: the maintainer explicitly approved this plan for the
recommended native method and separately approved ADR-0001-001 in the same
conversation on November 8, 2026. Actual approval text and reviewed ADR content
are preserved in the decision record. Native execution means one implementer
in this session and one fresh whole-change reviewer; no per-task implementer
subagents. Commit/push, publication, installation and companion edits remain
outside this authorization.

This plan implements only the starter subsystem. gz-skills portable delivery and
SP-BP existing-record integration require their own approved designs/plans and
release evidence. Task 4 consumes those owning outputs; if unavailable, report
the dependency and keep qualification/propagation incomplete. Do not implement
substitutes or shrink feature #12's gates.

Implementation choices below resolve builder details within the approved design:

- Public CLI: `configure --adr-policy {link,local}`; omitted means preserve the
  recorded choice, otherwise use `link` for a new project.
- Python seam: extend `configure(project: Path, ref: str, *, apply: bool = False,
  host: str = "codex", adr_policy: str | None = None) -> dict`.
- Source policy: `docs/engineering/architectural-decisions.md`.
- Managed local destination: `.skills-first/architectural-decisions.md`, avoiding
  collisions with project-authored policy at the source document's conventional
  path. Both modes retain the canonical immutable URL.
- Extend the existing `.skills-first/bundle.lock.json` with `adr_policy`, holding
  `mode`, `source_path`, `source_sha256`, and `local_path` only in local mode.
  Reuse `starter.repository`, `starter.version` and `starter.revision` for source
  identity. This is provenance, not approval or a new manifest authority.
- Canonical URL:
  `https://github.com/tvproductions/gz-skills-first-starter/blob/<full-sha>/docs/engineering/architectural-decisions.md`.
- Keep existing lock schema version 1 with the additive policy record. Explicit
  mode changes and older locks still require the existing manual reconciliation;
  do not teach configure to overwrite them or remove a former local copy.
- `status` resolves the recorded mode and remains read-only. Missing, malformed
  or conflicting policy provenance must never produce a configured/readiness claim.

### Task 1: Bind starter policy and capture the architectural approval

**Files:** Create `docs/engineering/architectural-decisions.md`; modify `AGENTS.md`,
`docs/architecture.md`, `docs/structure.md`, `docs/gz-skills-python.md`; after ADR
approval, move its working file from `docs/superpowers/specs/` to
`docs/decisions/ADR-0001-001-qualify-exact-component-combinations.md` and repair
references in this plan/spec/handoff. No index is required initially.

**Interfaces:** Consume approved spec and actual separate human ADR approval.
Produce concise canonical policy and a self-contained approved decision with
recoverable reviewed content and actual approval evidence.

- [x] Read the identified ADR edition with the maintainer and obtain explicit
  approval of ADR-0001-001. Preserve its reviewed bytes/hash and actual approval
  text/context; do not interpret the design approval as this approval.
- [x] Record approval metadata and evidence in the ADR, with administrative
  capture distinguished from reviewed decision text. Use the actual approval
  date and the maintainer's project-authorized identity, not a fabricated name.
  Preserve the reviewed proposal through retrievable history or an exact copy
  embedded/referenced in the approval evidence before relocating the working file.
- [x] Write the policy from the spec's required behavior and exact COB source:
  recognition/reuse, separate edition approval, independent work, provenance,
  amendments/retirement, backfills, independent evolution and authority boundaries.
  State that detailed portable procedures remain gz-skills-owned and their new
  delivery is unverified until actual owning references are available.
- [x] Add concise starter routing to AGENTS and reconcile ownership documents.
  Do not invent a delivered skill name or claim existing 0.8.3 supplies it.
- [x] Review the policy against each normative spec paragraph and the source's
  final lightweight guidance. Verify local references and immutable source links.
  This documentation review is not behavioral qualification.
- [x] Review the exact diff for this task. Commit with normal hooks only if Git
  synchronization/commit authority has been established; otherwise retain the
  reviewed task changes without committing.

### Task 2: Support preserved link/local policy selection in the public helper

**Files:** Modify `src/skills_first_starter/cli.py`,
`templates/AGENTS.skills-first.md`; create focused `tests/test_adr_policy.py`
(execution ruling: keep the existing `tests/test_starter.py` regression suite);
package the policy
and regenerate resources in the continuation below before final task acceptance.

**Interfaces:** Consume Task 1 policy bytes. Produce the extended configure seam,
CLI flag and additive lock record defined above, with matching read-only status.
Reuse `check_path`, `_plan_writes` and `_apply_writes` for all managed writes.
Use `hashlib.sha256` on original source bytes; preserve those exact UTF-8 bytes
when creating a local copy. Normalize no newlines before hashing/copying.

- [x] Add unittest public-seam cases, using `starter.main(...)` for CLI dispatch
  and `starter.configure(...)` for preservation/failure fixtures:
  `test_adr_link_preview_and_apply`, `test_adr_local_preview_and_apply`,
  `test_adr_policy_choice_survives_omitted_flag`,
  `test_adr_mode_change_requires_reconciliation`,
  `test_adr_local_edits_block_all_writes`,
  `test_adr_policy_symlinks_are_rejected`,
  `test_adr_policy_concurrent_write_is_preserved`,
  `test_adr_policy_failure_rolls_back_outputs`,
  `test_adr_legacy_lock_requires_reconciliation`,
  `test_adr_policy_provenance_is_validated`, and
  `test_adr_policy_bytes_and_hash_preserve_utf8_newlines`.
- [x] Assert link mode emits the exact canonical URL and matching source hash,
  emits no local file, and preview leaves the project untouched. Assert local
  mode previews the local file, writes identical source bytes only on apply,
  records source identity/hash/path and points instructions to the local working
  source while retaining the immutable URL. Parameterize both modes over Codex,
  Claude and OpenCode; assert Backplane stays disabled and profiles unchanged.
  A representative assertion for the local-mode preservation contract is:

  ```python
  def test_adr_policy_choice_survives_omitted_flag(self):
      starter.configure(self.root, REF, apply=True, adr_policy="local")
      policy = self.root / ".skills-first/architectural-decisions.md"
      before = policy.read_bytes()
      result = starter.configure(self.root, REF, apply=True)
      self.assertEqual(result["writes"], [])
      self.assertEqual(policy.read_bytes(), before)
      lock = json.loads((self.root / ".skills-first/bundle.lock.json").read_bytes())
      self.assertEqual(lock["adr_policy"]["mode"], "local")
  ```
- [x] Assert a second application is a no-op; omission preserves local mode;
  explicit repetition succeeds. Reject a changed mode, malformed record, unknown
  mode, inconsistent hash/path or unreconciled legacy lock before any writes.
  Assert edited files and existing instructions survive every rejected attempt.
  Cover a symlinked destination and parent using the suite's supported Windows
  fixture method; retain explicit host limitations if link creation is unavailable.
- [x] Inject a local-copy write failure and a concurrent destination edit using
  existing mock patterns. Assert prior writes roll back and unrelated/concurrent
  content remains intact. Use both non-ASCII text and CRLF/LF source fixtures to
  show that the recorded SHA-256 describes the actual copied bytes.
- [x] Run `uv run --locked python -m unittest discover -s tests -p test_adr_policy.py -v`
  and observe assertion-level failures for the unsupported new behavior. Do not
  use resource drift or an unrelated fixture failure as the negative control.
- [x] Implement mode resolution, candidate/lock generation and CLI/status plumbing
  in the existing helper. Render two explicit instruction placeholders,
  `{{ADR_POLICY_WORKING_SOURCE}}` and `{{ADR_POLICY_CANONICAL_URL}}`, by literal
  replacement; do not format the whole template. The working source is the local
  relative path in local mode and the canonical URL in link mode. Register the
  local destination with `check_path` only when selected; all candidates must be
  checked before writing. Raise `AdoptionError` for policy reconciliation failures.
- [x] Re-run the focused unittest command after resource regeneration below;
  require all cases to pass, including existing adoption/rollback regressions.
  Do not add a readiness certificate or network fetch to configure/status.
#### Task 2 continuation: Package the policy and verify clean installed behavior

**Files:** Modify `tools/package_resources.py`, `tools/verify_distribution.py`,
`tests/test_starter.py`; generate
`src/skills_first_starter/resources/docs/engineering/architectural-decisions.md`
and changed existing resource copies. Update source-inventory descriptions in
`AGENTS.md` and relevant documentation from five inputs to six.

**Interfaces:** Add the canonical policy path as the sixth `RESOURCE_PATHS` input;
the installed helper reads it through existing `HERE` resource selection.
The policy remains ordinary starter documentation, not another skill.

- [x] Extend archive/installed verification assertions before adding the resource:
  require exact canonical policy bytes/hash in the wheel, preserve exactly one
  owned update skill, and require both link/local public CLI behavior outside the
  checkout. Observe the missing-policy assertion fail on a pre-change artifact.
- [x] Add the sixth authoritative input and matching wheel archive check. Extend
  installed native-host verification to run preview/apply/status and repeated
  configure for both modes in separate temporary adopter roots. Assert link mode
  creates no copy; local mode needs no network/source checkout and preserves
  source bytes. Verify the ordinary missing-`--starter-ref` wheel rejection remains.
- [x] Run `uv run --locked python tools/package_resources.py`, then the Task 2
  focused tests. Run `uv build --no-sources` followed by
  `uv run --locked python tools/verify_distribution.py`. Require archive-byte,
  clean-environment import/CLI and installed-resource checks to pass.
- [x] Record actual interpreter/uv provenance and installed scope. Preserve the
  one-update-skill ownership rule and separate both policy access forms from
  installed portable-skill/native-discovery qualification.
- [x] Review/commit this task only under actual Git authority as in Task 1.

### Task 3: Reconcile adopter instructions and update guidance

**Files:** Modify `docs/adoption-workflow.md`, `docs/adoption.md`,
`docs/adoption-0.5.md`, `docs/updating.md`,
`templates/skills/update-gz-template/SKILL.md`, `README.md`, `ROADMAP.md`,
`CHANGELOG.md`, and the existing handoff; regenerate changed resource copies.

**Interfaces:** Consume the policy and configure flag/provenance from Tasks 1-2.
Produce canonical adoption/update instructions for both lanes and policy modes.

- [x] Document exact preview/apply commands for both `--adr-policy link` and
  `--adr-policy local`; show omission preserving an existing selection. State
  that local copies still reference source version/SHA/hash and require reviewed
  reconciliation when project edits or source policy differ.
- [x] Explain existing-lock/mode-change reconciliation through old/current/target
  review, preserving original bytes and rollback evidence. Add no automatic
  overwrite or deterministic upgrade product. Keep suitable existing ADR paths,
  identity/history and project-approved adaptations; identify unresolved gaps.
- [x] Bind both lanes to policy and portable workflow through the existing update
  skill; do not add generic ADR procedure text or another starter-owned skill.
  Preserve architectural approval versus ordinary documentation review, and
  self-contained ADRs with embedded/referenced evidence and optional lookup index.
- [x] Check examples against Task 2's public CLI tests. Re-run the resource
  generator/check after changing the fragment or update skill. Update release
  scope with completed versus still-dependent work; retain 0.10.0 and all deferrals.
- [x] Review/commit this task only under actual Git authority as in Task 1.

### Task 4: Assemble behavioral and exact-combination evidence

**Files:** Create `docs/evidence/2026-11-08-adr-practice-qualification.md` for the
first actual run (use its actual execution date if different); update roadmap,
changelog and existing handoff. This is a project evidence record, not a new
tracker, reporting engine or workflow skill.

**Interfaces:** Consume approved owning companion designs, immutable released
contributions, source/path/version mapping, their evaluation evidence and all
three real internal-use records. Produce a source-bound qualification result or
an explicit incomplete assessment. No companion implementation is part of this task.

- [x] Inventory actual owning records and delivery sources. If missing, list the
  missing records/owners and stop the affected qualification/propagation steps;
  continue independent starter checks. Do not invent future versions or skill names.
- [ ] Once selection is separately authorized, reconcile bundle pins, both catalogs
  and development host marketplace refs together, preserving project activation,
  user defaults and disabled Backplane. Validate source revisions separately from
  loaded sources. Follow native project-only qualification; install nothing through
  this plan without separate authorization.
- [ ] Run or inspect source-identical full shared B01-B16 evaluation evidence.
  Preserve exact prompts/fixtures, loaded sources, environment/model metadata,
  full transcripts/actions and verdicts. Record missing metadata as UNKNOWN.
- [ ] Run the targeted checks from the spec for all three repository bindings,
  lite/heavy fixtures and owner-supported active SP-BP integration, coordinating
  owning repository execution under its own authority. Every binding needs B01
  stopping and B02 continuation controls. Verify both policy-access forms and
  project precedence; an active-integration result does not qualify disabled paths.
- [ ] Expand to affected matrix cases on behavior changes/discrepancies. Preserve
  failures, fixes and reruns, and justify every reused shared result by unchanged
  inputs/applicability. Require genuine internal use plus alignment review in all
  three publishing repositories. Do not substitute fictional approvals for real use.
- [x] Run the documented starter gate: `uv sync --locked --all-groups`,
  `uv run --locked pre-commit run --all-files`,
  `uv run --locked skills-first-starter validate`, `uv build --no-sources`,
  `uv run --locked python tools/verify_distribution.py` and resource drift check.
  Analyzer regressions are required only if analyzer inputs change. Record deeper
  release/platform gaps separately; these checks do not establish all release acceptance.
- [x] Review the full intended diff and record exact source hashes, actual
  provenance, coverage, limitations and remaining dependencies. Claim feature
  acceptance/propagation only when all its gates pass; publish/install/migrate
  nothing from a passing assessment. Follow the separate user-authorized Git sync
  ritual when synchronization is requested.

## Self-review and execution handoff

Coverage: Task 1 owns policy/ADR provenance; Task 2 owns mode/preservation behavior
and installed distribution; Task 3 owns adoption/reconciliation; Task 4 owns
behavioral/internal-use/exact-combination evidence and final scope accounting.
Companion internals remain separate owning plans, not omitted starter work.

Commands use unittest and the actual managed interpreter; existing interfaces are
`configure`, `status`, `check_path`, `_plan_writes`, `_apply_writes` and `HERE`.
The new external parameter/flag, lock fields, file paths and template placeholders
are defined above; implementation may choose private helper boundaries without
changing those contracts. No new dependency or Python 3.14-specific mechanism is
needed beyond hashlib/pathlib/stdlib handling; retain current runtime policy.

Recommended execution: native, because Tasks 1-3 share helper/provenance/resource
interfaces and the overall feature still awaits independent companion deliveries.
Run one fresh whole-change review after implementation. Preserve existing local
design/handoff work when selecting execution isolation; create no worktree merely
to write this plan. Review this plan and obtain separate ADR approval before
dependent implementation. No product implementation has been performed by planning.

Execution disposition: Tasks 1-3 are complete. Verification used an uncommitted
feature branch; the maintainer subsequently directed a normal local commit on
main and no feature branches. The reviewed work was returned to main and the
temporary branch removed after verifying it held no distinct commits.
The existing update skill remained unchanged after its application baseline
preserved local-mode/provenance requirements; target-specific guidance lives in
the canonical adoption/update documents it already routes to. Task 4's local
inventory, gate and review/evidence steps are complete; companion delivery,
shared/targeted behavioral evaluation and companion internal use remain pending.
The fresh whole-change reviewer found one medium partial-write cleanup defect;
its regression failed before the fix and all 72 tests plus the full gate pass
afterward. See the [qualification receipt](../../evidence/2026-11-08-adr-practice-qualification.md)
for source hashes, review dispositions and remaining UNKNOWNs. Do not mark the
whole feature accepted or propagate this candidate.
