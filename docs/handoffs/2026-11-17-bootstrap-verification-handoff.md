# Bootstrap verification review — handoff, November 17, 2026

## November 18 reference save point

The maintainer invoked `gzs-git-sync`. Fast-forwarded main from `7dea4b5` to
`de5cdcd`, preserving the local three-page Addy Osmani article PDF in `docs/`.
Reviewed its text and rendered pages; retain it as reference material, without
adopting its recommendations as project instructions. This save point adds no
behavior, dependency selection or release scope. Published version **0.11.2**
and the separately approval-gated proposed **0.12.0** remain unchanged.

Startup freshness reuses the November 18 release-specific official-source receipt:
all **20 candidate input hashes match**, and it records no required updates.
Actual caller uv **0.13.8** satisfies the **>=0.13.5** floor; validation uses
managed CPython **3.14.10** and the current exact lock. Native discovery and
cognitive/embedded/platform limits remain as recorded below. Final sync must
preserve normal hooks, verify remote SHA equality and observe both exact-commit
CI jobs; report their outcome without a receipt-only follow-up commit.

Local integration checks pass: `uv sync --locked --all-groups`, all four hooks
through `uv run --locked pre-commit run --all-files`, `uv run --locked gz-starter
validate`, `uv build --no-sources`, and `uv run --locked python
tools/verify_distribution.py`. No new behavior or analyzer input requires new
tests or deeper-tool replay. Reuse those passes for this result-only prose;
the final exact-commit CI verifies the complete committed candidate.

## Resume point and authority

**November 18 release update:** after completed dependency maintenance, the
maintainer requested “publish 0.11.2”. See the
[release receipt](../evidence/2026-11-18-0.11.2-release.md) for exact source,
CI, tag and publication outcome. This supersedes the earlier publication limits
only for this maintenance patch and its ordinary synchronization. The design
review below remains the resume point; no verifier or ADR approval is inferred.
**Published and verified:** 0.11.2 at immutable source
`1175433c950d47d5330e4a9a36a986f1a0c6ae26`; both exact-source CI jobs, remote
annotated tag and downloaded source contents pass. Proposed 0.12.0 will advance
this published patch. This single publication-result follow-up updates pointers;
its final main/CI alignment is reported in the release response without another
receipt-only commit.

Resume the maintainer's **design review**, at the automatic transition from
bootstrap validation to adopter behavior tests. Read
[design edition 2](../superpowers/specs/2026-11-17-bootstrap-verification-design.md)
and draft [ADR-0003 edition 1](../decisions/ADR-0003-001-own-bootstrap-verification-in-the-starter.md).
Then settle the finite supported CI/command pattern and what observed authored
code/tooling/test assets activate behavioral requirements. Preserve all requested
negative controls and fail closed on uncertainty; do not add a manual phase or
allow-empty selector.

**No verifier implementation or implementation plan exists.** Complete-design
approval and separate explicit approval of identified ADR-0003 edition 1 remain
pending. Do not infer either from agreement on one approach, this handoff, Git
sync or prior release assent. Once approved, preserve exact approval evidence,
invoke the writing-plans workflow, reconcile the selected minor scope/mirrors,
and implement with meaningful reached-fault tests immediately.

Latest request: **“write handoff and git sync”**. This authorizes the ordinary
main commit/push and exact-commit CI observation for the reviewed session scope.
It authorizes no implementation, adopter write, new dependency migration, native
installation/activation, companion change, tag or release publication.

## GitHub operations preference

Maintainer direction, November 17: **both the starter and adopters MUST STRONGLY
PREFER the GitHub CLI (`gh`) for ALL GitHub operations**. Use direct `gh`
commands, including `gh api` where needed, for GitHub service operations and
automation. Keep direct `git` for repository operations such as commits, fetches
and pushes. Carry this preference into starter/adopter instructions and supported
CI/migration examples during the authorized reconciliation; preserve both lanes.

## Selected problem and evidence

The maintainer requested a bounded upstream correction to the v0.9.0 adopter
bootstrap deadlock: authoritative pre-runtime verification, a supported command/
hook/CI pattern, real bootstrap validation, automatic meaningful-test requirements
once code or tooling appears, preservation of discovery/coverage failures,
Windows/macOS proof without Node, and concrete migration of stale requirements
and handoffs. Keep the [roadmap](../../ROADMAP.md#selected-correction--pre-implementation-verification-november-17-2026)
as the existing scope authority.

The adopter's private November 17 verification section and earlier feedback were
read in place, without changes. They identify eight pending paths, zero runtime/
Python tooling/test assets and an unconditional unittest hook. Do not copy private
records into this public scaffold. Use invented fixtures throughout acceptance.
The consumer's runtime-design gate and native-readiness gaps remain separate.

Negative reproduction on managed CPython **3.14.10**: a temporary invented tree
with README and pyproject, no Python implementation/tests, ran
`python -m unittest discover -v`. It reported **Ran 0 tests / NO TESTS RAN**, exit
**5**. The adoption runbook permits configuring before product initialization,
but its hook lacks executable applicability logic. The portable git-sync 1.1.0
policy diagnosis does not itself provide the starter command/migration.

## Review direction and unresolved approval

The agent proposed a starter-owned installed development verifier, separately
pinned/locked by adopters, with a verification extra for explicitly declared YAML
parsing. Keep the base helper's stdlib dependency contract. This avoids copied
verifier/test assets masking an adopter's missing product tests. No such command
or extra has been implemented or delivered yet.

During review the maintainer replied verbatim:

> yes, an implementer is not accounting for the starter's own testing.

Context: this answered the choice between the installed development verifier and
project-owned copies. Record it as direction on that approach plus a mandatory
testing clarification, not complete-design or separately identified ADR approval.
This is an agent transcription of the current conversation; no durable
conversation URL is available. Approval fields remain empty and ADR state Draft.

Design edition 2 now makes three obligations explicit:

1. **Starter/producer:** existing implementation always requires its meaningful
   suite. Add owning verifier regressions and installed-distribution/platform
   qualification immediately. Never classify the starter itself as pre-runtime.
2. **Adopter bootstrap:** run the qualified verifier against the actual adopter
   artifacts; explain any product-test N/A. Exact-version producer evidence may
   be reused; it does not validate the adopter's files/product. Do not rerun the
   complete producer suite on every adopter commit.
3. **Adopter implementation:** automatically require the adopter's own meaningful
   tests and preserve coverage obligations once its code/tool/test assets appear.
   Installed starter tests cannot stand in for adopter tests.

The original [design edition 1](../superpowers/specs/2026-11-17-bootstrap-verification-design-edition-1.md)
is preserved byte-for-byte, SHA256
`edb8c8fdc9ebf0eeff0bf9e0919aaefef5e31c66963e9f3dda327f2e045e4719`.
Its fresh builder check reported **nothing important left**, with conservative
handling of CI logic, discovery omissions, richer gates and actual Windows proof.
That check evaluated edition 1; it supplies neither human approval nor platform
acceptance. Edition 2 records the subsequent maintainer clarification.

## Required delivery and acceptance still ahead

Before calling the correction delivered, complete:

- Approved executable contract and ownership, followed by an implementation plan.
- Meaningful starter-owned helper tests for valid bootstrap, malformed artifacts,
  stale locks/links, code/tooling with missing tests, undiscovered/empty/all-skipped
  suites, import/syntax/load_tests/assertion failures, and the unchanged-hook
  transition when code appears. Preserve runtime coverage failures and thresholds.
- Public CLI and installed-artifact proof; parser dependency explicitly declared
  in the optional verification extra, no transitive-import assumption.
- Reconciled authoritative policy, generated instructions, hook/CI examples,
  greenfield/brownfield/update guidance and reviewed existing-adopter migration.
  Supersede stale requirements/handoffs while preserving failed-history receipts
  and runtime-design approval. Ordinary configure must not overwrite app files.
- Actual Windows and macOS execution of the supported command/hook and substantive
  acceptance cases using direct commands without Node. A configured matrix,
  parser check or mocked platform is not Windows proof. Keep unavailable evidence
  UNKNOWN; do not call full correction acceptance complete.
- Full applicable repository gate, packaged-resource refresh, source-independent
  builds, clean installed behavior and refreshed candidate-specific evidence.

No new helper exists, so its tests are pending implementation. Existing starter
tests remain applicable now; no bootstrap exception is claimed for this sync.

## Tool maintenance included in this save point

**November 18 follow-up:** a new explicit `gzs-update-dependencies` invocation
updates filelock/platformdirs/python-discovery/virtualenv in both locks. Read the
[current maintenance receipt](../evidence/2026-11-18-dependency-maintenance.md)
and its exact candidate inventory before reusing earlier dependency evidence.
Retain pending 0.11.2, the design-review resume point and the separate design/ADR
approvals above. This maintenance invocation grants no additional Git sync or
publication authority. Codex 0.170.0 now observes installed SP 7.0.2, gz-skills
0.13.0 and disabled Backplane 0.3.0 at selected SHAs; the older native drift below
is historical. No installation or activation was performed in this follow-up.

Earlier this session, the maintainer explicitly invoked dependency maintenance.
The [post-release receipt](../evidence/2026-11-17-post-release-maintenance.md) and
[registry record](../evidence/2026-11-17-post-release-dependencies.json) preserve
that completed source/environment pass at its exact inputs:

- uv/uv_build **0.13.8 -> 0.13.9**, ty **0.0.104 -> 0.0.105**, both independent
  locks/environments, root/example backend and CI selection/reference guidance.
  Use `uv tool run --from uv==0.13.9 uv ...` so nested commands resolve the same
  selected binary; machine uv 0.13.8 remains unchanged and supported.
- All **77** registry projects current at the checked time; both locked audits
  cover **75** registry packages with zero known vulnerabilities/skips. Both
  outdated results are empty; repeated upgrade resolutions are byte-stable.
- Actual managed Python **3.14.10** / standalone host reference **3.12.16** remain
  the approved families. Minimum-only uv **>=0.13.5** remains intact.
- Repair of stale pre-rename host-environment shebangs through exact all-group
  reinstall; the actual pip-audit command and standalone 3.12 controls then pass.
- Four routine hooks, catalogs/resources, source-independent builds and isolated
  installed CLI/example typing/preservation checks passed. Final evidence-only
  prose reuses unchanged owning checks under the verification policy.

This handoff adds no further dependency selection. Session-start freshness may
reuse the same-day official-source receipt after checking relevant inputs; an
AGENTS continuation-pointer edit is not a dependency change or a new registry
query. Preserve the receipt's historical hashes rather than rewriting evidence
to match later prose. Release preparation needs its own actual candidate receipt.

## Version accounting and retained limits

The following November 17 accounting is historical: 0.11.2 has now published
as recorded at the top of this handoff. Preserve the unimplemented correction's
proposed 0.12.0 and its separate design/ADR approvals; no current release gate
remains for the completed maintenance patch.

Last published baseline: **0.11.1**, immutable source
`041c1989406c1b9c4978042661c2dd38ff1db160`; [publication is verified](../evidence/2026-11-17-0.11.1-release.md).
Current development checkpoint: **0.11.2 / patch**, governed by completed
compatible maintenance. Bundle, pyproject, root lock, packaged bundle and CLI
must agree. The unimplemented correction's new supported tool/adoption interface
proposes **0.12.0 / minor**, folding in that maintenance after design approval.
Reconcile all mirrors in dependent planning; no complete minor-version or
release-acceptance claim is made now. Neither this sync nor a version string
publishes a release. Preserve immutable tags and earlier receipts.

SP **7.0.2**, selected gz-skills **0.13.0**, disabled Backplane **0.3.0** and both
catalogs/native source bindings are unchanged. Actual macOS Codex **0.169.0**
inventory instead exposes installed gz-skills **0.11.0** and disabled Backplane
**0.2.0**; native installation alignment/fresh-session discovery remain open.
Do not repair with user-wide activation or edit native caches directly.

Retain cognitive **DEFERRED / measurement UNKNOWN**, ceiling 15, adopter-owned
cohesion, actual embedded-host UNKNOWN, desktop/other-host/model limits and all
unselected roadmap work. Existing Linux hosted CI for the starter is distinct
from the correction's required future Windows/macOS acceptance.

## Save-point verification and synchronization

Starting main/remote: `0667b3347bfc98cd26179fdc41f820ce67d2a2d2`
(Save post-0.11.1 handoff). Freshly fetch and inspect divergence before integration.
The intended unit includes prior maintenance, its evidence, draft design/ADR,
review clarification/history and this handoff/continuation-pointer update.
Preserve all unrelated work; work directly on main with normal hooks.

Review the complete staged scope, run the repository's applicable gate and
packaging checks with the selected uv/interpreter, then commit with the
established public identity without changing global settings. Ordinary push
must be followed by local/remote SHA equality and both jobs for that exact SHA.
Report final commit, CI URL/result and remaining worktree in the sync response.
Do not create a CI-receipt-only follow-up chain. No tag or release is authorized.

Observed pre-commit save-point checks on the coherent candidate: root exact
all-group sync; all four routine pre-commit hooks; catalog/resource validation;
`uv build --no-sources`; and isolated installed CLI/example verification **pass**
under uv 0.13.9 / managed Python 3.14.10. Independent host-reference exact sync
and positive/negative standalone controls **pass** on managed Python 3.12.16.
These current checks supersede the earlier maintenance receipt's pending hosted
CI status only when this save point's exact CI is observed in the sync response.
No new behavioral tests or analyzer/platform replay is justified by the draft
and handoff prose; the existing implemented starter suite runs normally.
Final review: all **223 local references** across **14** changed/new Markdown
files resolve, the existing suite contains **95** tests, lock semantics change
only reviewed package/owner metadata, and the diff has no whitespace errors.
