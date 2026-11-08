# ADR practice save point — November 8, 2026

## Resume here

Work directly on `main`; do not create feature branches unless the maintainer
explicitly requests one. The maintainer approved the starter specification,
native implementation plan and, separately, ADR-0001-001. Do not reopen those
approvals merely to resume. Recheck Git/GitHub state and applicable source
revisions before new work. This handoff supersedes earlier draft/uncommitted
resume statements in the [chronological handoff](2026-10-24-session-close.md).

Committed implementation: `e373f89cfed10dabd9311d16b3e1daea16930967`,
`Implement starter ADR policy and preserved policy access`, committed directly
on main with normal Ruff/format/ty/unittest hooks. The temporary feature branch
was removed after verifying it held no distinct commits. The worktree was clean
when this fresh handoff was requested.

The maintainer then explicitly requested this handoff and `gzs-git-sync`,
authorizing the normal handoff commit and push to origin/main. Initial origin
fetch confirmed main ahead 1 / behind 0, with no remote work to integrate.
Preserve published history and hooks. No release, tag, installation, companion
write or adopter propagation is authorized by this save point.

## Governing records and accepted design

- [Feature #12](https://github.com/tvproductions/gz-skills-first-starter/issues/12)
  owns the bounded 0.10.0 outcome; [design #13](https://github.com/tvproductions/gz-skills-first-starter/issues/13)
  tracks the starter design. No issue mutation was part of this session.
- [Approved specification](../superpowers/specs/2026-11-08-adr-practice-design.md)
  and [approved native plan](../superpowers/plans/2026-11-08-adr-starter-binding.md)
  retain approval context and task disposition.
- [ADR-0001-001](../decisions/ADR-0001-001-qualify-exact-component-combinations.md)
  is Current and explicitly approved. Exact reviewed proposal bytes/hash and
  actual conversation approval are preserved with it. A hash identifies content;
  the human's explicit response supplies approval.
- [Starter policy](../engineering/architectural-decisions.md) binds both lanes
  and the publishing repository; [qualification receipt](../evidence/2026-11-08-adr-practice-qualification.md)
  records actual checks, source hashes and remaining UNKNOWNs.

Qualify an exact component combination for each starter release. The starter
owns mandatory adopter policy and concise pointers; gz-skills owns the portable
procedure/template; SP-BP owns integration with its existing planning/tracking
records. Keep independent ownership, versions, releases and record histories.
Add no central CLI/core, ledger or other new Backplane capability. Preserve
suitable existing ADR conventions. Decisions remain self-contained, with
approval evidence embedded or durably referenced; indexes are optional lookup.

Both immutable policy links and repository-local copies are supported. Run the
full shared B01-B16 behavior matrix plus targeted repository/adopter binding
checks. Every binding needs missing-approval stopping and approved-decision
continuation controls; expand testing for behavior changes/discrepancies. Genuine
internal use in all three publishing repositories and released owning companion
contributions are required before adopter propagation.

## Completed starter work

Plan Tasks 1-3 are implemented. `configure --adr-policy link|local` and read-only
status preserve a recorded policy selection when the flag is omitted; only a
new project defaults to link. Local mode copies exact packaged UTF-8 bytes to
`.skills-first/architectural-decisions.md`. The existing lock records source
identity/path/hash. Legacy provenance, mode changes and local adaptations require
reviewed reconciliation rather than overwrite. Generated instructions identify
both the working policy and immutable canonical source.

The policy is the sixth authoritative wheel resource. Public-helper tests cover
all three hosts, both modes, preview/idempotence, UTF-8 LF/CRLF bytes/hashes,
conflicts, legacy/malformed records, symlinks, concurrent files and rollback.
The isolated installed-wheel verifier covers both policy modes across all three
helper hosts without a starter checkout. This is configuration/artifact proof,
not actual native skill discovery or model-behavior qualification.

Independent whole-change review found one medium inherited rollback defect:
failure after exclusive creation could leave a partial policy behind. A real-file
write/close regression failed before the fix. Cleanup now removes the owned
failed file and preserves a concurrent replacement. The final 72-test suite and
full gate passed after the fix; no unresolved important findings or deferred
minors remain. The receipt records every declined review boundary/disposition.

The narrow update skill remains unchanged: its fresh application baseline
preserved local mode/provenance and routed to canonical target guidance. Put
target-specific reconciliation details in adoption/updating docs; add no
duplicate skill procedure. Plan-scoped scratch progress remains ignored under
`.superpowers/sdd/2026-11-08-adr-starter-binding/`; authoritative results and
remaining work are in tracked plan/evidence/handoff records, not scratch alone.

## Remaining work and next useful step

Plan Task 4 and feature #12 remain **INCOMPLETE**. The starter's actual approved
ADR use/alignment review is recorded; companion use cannot be inferred from it.
Obtain/link actual owning gz-skills and SP-BP design/approval/delivery records
under their own authority. Their internal implementations belong in their own
repositories; this save point does not authorize those writes or invent them.

Then assess the exact immutable released contributions, run/inspect source-bound
shared and targeted behavior evidence, collect genuine companion internal-use
and alignment records, and verify the actual selected/loaded combination before
claiming feature acceptance or permitting separately authorized propagation.
Keep explicit approval, source identity, configuration, discovery, behavioral
compliance, delivery and publication separate.

Current selections/activation are unchanged: SP 7.0.1, gz-skills 0.8.3 and
pre-release SP-BP snapshot disabled. Read-only live inventory saw gz-skills
main `cfb34f8d2b6e6eebb268581ac07664a6b8074ebf` / stable 0.10.1 and SP-BP
main `05505f8009989eb7514ec62750e33c78bc40abf9` / stable 0.2.0. That inventory
establishes neither ADR contribution readiness nor permission to change pins.
Recheck sources on resume. Native discovery and other-host execution claims
remain limited to actual evidence; the sync CI result must be evaluated for its
own exact SHA and scope.

## Release accounting and synchronization evidence

Published baseline: **0.9.0**, immutable tag `v0.9.0`, release commit
`3f76acf0038b030bf5abd85ce4a419e890d3e420`. Pending target: **0.10.0 / minor**,
governed by #12 and its newly mandatory pre-1.0 adoption obligation. Bundle,
package, lock and packaged bundle agree. Reuse this target, not another bump.
Included completed scope: approved starter design/ADR, policy/helper/docs and
installed-artifact verification. Included remaining scope: owning companion
delivery, shared/targeted qualification, companion internal use and reviewed
distribution. Deferred: real-adopter pilot, deterministic upgrade/rollback,
remaining platform qualification and acceptance-reporting automation. A future
1.0.0 still needs its own newly written PRD and finite scope. Release acceptance
and publication remain separate from Git synchronization.

Local execution is uv 0.13.7 / managed Python 3.14.10. This save point changes
handoff/routing documentation only; it adds no analyzer, helper, package input,
catalog or pin change. The implementation's prior gate passed 72 tests and all
declared checks. For this sync, locked all-group sync, all four routine hooks,
bundle/both-catalog validation, six-resource drift, source-independent build
and isolated installed verification passed again. Normal handoff commit hooks
must also pass. Preserve existing deeper-release/cognitive gaps;
no analyzer-specific regression suite is triggered by this scope.

This handoff precedes its own commit and push. Verify the final main SHA equals
origin/main, ahead/behind is 0/0 and the worktree is clean; observe both jobs in
the `Check starter` workflow for that exact SHA. Use `gh run list --commit <SHA>`
and `gh run view <run-id>` to recover the final CI link/result on resume. Record
the result in the sync response rather than creating CI-receipt-only commits.
