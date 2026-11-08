# ADR practice implementation and qualification — November 8, 2026

Overall ADR-feature qualification: **INCOMPLETE**. Starter policy/helper
implementation is locally verified; companion-owned delivery, full shared and
targeted behavioral evaluation, and all three genuine internal-use records are
not established. Do not propagate to adopters or claim feature #12 accepted.

## Candidate and authority

Base checkout: `1dd24b2a52249e22170a102bb0c363daae3e243b`; verification ran on
the uncommitted `feature/adr-practice` candidate. The maintainer subsequently
directed committing on `main` and forbade feature branches. Returned the reviewed
changes to main and removed the temporary branch after verifying identical tips.
Actual commit identity is recorded in Git history. No push, publication, remote
CI, plugin installation or native-discovery result is asserted.

The maintainer approved the revised starter specification and native plan, then
separately explicitly approved ADR-0001-001. The authoritative
[ADR](../decisions/ADR-0001-001-qualify-exact-component-combinations.md) preserves
actual conversation approval and exact reviewed proposal bytes/hash. Reusing
that approved choice for the implementation is genuine starter internal use;
the final independent alignment review and its test-proven fix are recorded
below. This use does not stand in for either companion's internal-use record.

Published baseline: 0.9.0 at `3f76acf0038b030bf5abd85ce4a419e890d3e420`;
pending 0.10.0, minor, governed by #12/#13. Version mirrors remain aligned.
The implementation adds no runtime/dependency/tool refresh. uv 0.13.7 and managed
Python 3.14.10 are the actual execution selections. Preserve existing deeper
release/cognitive/native-host exceptions; this receipt grants no release waiver.

## Expected sources and observed boundaries

| Component | Selected source / state |
| --- | --- |
| Starter | Local uncommitted 0.10.0 candidate based on the SHA above; source hashes must be refreshed for any later candidate/release. |
| SP | Unchanged bundle revision `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` (7.0.1); no new discovery claim. |
| gz-skills | Unchanged bundle revision `d6acc26e28ca1c4f43e5bb46d8973021d7d006c3` (0.8.3); new portable ADR contribution is not qualified. |
| SP-BP | Unchanged bundle revision `d0eeee829c491da02351e793544aa16ad96461bf`; disabled, no activation or combined-stack claim. |

Read-only live inventory: gz-skills main was
[`cfb34f8d2b6e6eebb268581ac07664a6b8074ebf`](https://github.com/tvproductions/gz-skills/tree/cfb34f8d2b6e6eebb268581ac07664a6b8074ebf),
latest stable v0.10.1; SP-BP main was
[`05505f8009989eb7514ec62750e33c78bc40abf9`](https://github.com/tvproductions/superpowers-backplane/tree/05505f8009989eb7514ec62750e33c78bc40abf9),
latest stable v0.2.0. Recursive source-tree listings were complete and returned
no ADR/decision-named paths. This filename inventory does not establish absence
of all architectural content, delivery or approval; no owning ADR-feature
design/release/evaluation references were supplied by this plan or established
by the inventory. Obtain those owning records before qualifying their contribution.
Do not infer alignment or update installed pins from newer release numbers.

## Deterministic starter verification

Baseline: all 60 existing unittest cases passed before helper implementation.
The new policy CLI tests first failed with unsupported `--adr-policy`; after
implementation all 11 new methods and the full 71-test suite passed. The
pre-change wheel failed the new archive assertion for a missing canonical
policy. After packaging the sixth authoritative input, the source-independent
build and clean installed-wheel verifier passed.

New coverage exercises both modes for all three helper hosts, no-write preview,
idempotence and selection preservation, exact source identity/hash and UTF-8
LF/CRLF bytes, local edit conflicts, malformed/legacy provenance, mode-change
reconciliation, symlinked destination/parent rejection, concurrent writes and
rollback after injected write failure. Installed checks exercise both modes,
preview/apply/status and repeated selection outside the checkout. They run
helper configuration only, not real native host discovery.

Native Windows was exercised. The read-only portability audit returned no
findings before implementation. Actual macOS/Linux execution and CI for these
uncommitted changes remain unverified; no cross-host proof is inferred.

The final repository gate passed: `uv sync --locked --all-groups`, all four
routine pre-commit hooks, `skills-first-starter validate`, the six-resource drift
check, `uv build --no-sources`, and isolated installed-distribution verification.
The post-change portability audit again returned `[]`. Local links resolve in
all 21 changed/new Markdown documents, and `git diff --check` passes. These
checks do not supply the missing behavioral/native/companion evidence below.
The independent whole-change review found one medium transactional defect:
a write/close failure after exclusive file creation could leave a partial
policy behind. A real-file regression failed for both failure points before
the fix. Cleanup now identifies the exclusively created file and removes it
after failure only if the path still identifies that file; a concurrent
replacement is preserved. This uses the existing stdlib
[file-descriptor stat](https://docs.python.org/3.14/library/os.html#os.fstat) and
[stat-identity comparison](https://docs.python.org/3.14/library/os.path.html#os.path.samestat),
not a new runtime mechanism. Reviewed on the actual pinned interpreter.

The fix passed all 12 policy methods and the full **72-test** suite. Final
Ruff/format/ty/unittest hooks, catalogs, resource drift, no-sources rebuild,
isolated installed verifier and portability audit all passed again. Ruff's
loop-binding finding in the regression fixture was corrected; no rule was
suppressed. No unresolved critical/important findings or deferred minors remain
from the independent review. No second reviewer pass is claimed after the
test-proven fix.

Verified executable/distribution inputs, SHA-256 (uncommitted candidate):

| Input | SHA-256 |
| --- | --- |
| `src/skills_first_starter/cli.py` | `d8dc2ba63b313076a10e717ab7f066c592d6ebec22274791d0e5970009f73af3` |
| `tests/test_adr_policy.py` | `64d84eeaeb6c0f5a8d95f1b00c5ca5bf7305cc9771ad531c30d5b178449bb7f9` |
| `tools/package_resources.py` | `22fe2d6ac68a9e174b004be2c4ad7c91a38c647cfaa160479983a15ad6ac422d` |
| `tools/verify_distribution.py` | `06f2d37b3786bac79db9cb6491308478749e1402847faa6adb1f569a99f81a76` |
| `docs/engineering/architectural-decisions.md` | `b0272acf8cecee53885579dadcdbfe3703d07a00f3168bad5449c20a9b1634b7` |
| `templates/AGENTS.skills-first.md` | `03a95b633a8fa499a7d481af04d0b5123ba94b6a516cee2b03ef92c36b01141d` |

## Update-skill application check

The approved plan anticipated updating `update-gz-template`. A fresh read-only
application scenario used its existing text with an invented local-policy
adopter and empty target candidate directory. The evaluator explicitly selected
`--adr-policy local`, compared original/current/target policy and mode/path/hash
provenance, preserved adaptations and withheld workflow qualification claims.
It correctly identified that complete CLI details come from the target runbook.

Ruling: retain the current narrow skill, which already routes to canonical
target instructions; add target-specific policy details in adoption/updating
guidance instead of duplicating procedure in the skill. No baseline behavior
failure justified a skill-text change. This one application check is narrower
than the ADR behavioral matrix and is not evidence of general skill discovery
or the portable ADR workflow's qualification.

## Required behavioral and delivery evidence still outstanding

| Requirement | Status / owner |
| --- | --- |
| Approved owning portable procedure/template design and immutable released delivery | UNKNOWN; gz-skills maintainer supplies actual records. |
| Approved integration through existing supported tracking records and released delivery | UNKNOWN; SP-BP maintainer supplies actual records; add no new ledger capability. |
| Full shared B01-B16 scenario transcripts and exact-source verdicts | NOT RUN against a delivered portable ADR contribution. |
| Targeted publishing-repository and lite/heavy binding checks, including stop/continue controls | NOT RUN as the approved ADR behavioral evaluation. Unit/helper tests are distinct. |
| Owner-supported active SP-BP integration and disabled-consumer behavioral controls | NOT VERIFIED for this ADR contribution. |
| Genuine internal use and alignment review in gz-skills and SP-BP | UNKNOWN; cannot be supplied by this starter implementation. |
| Starter internal use and alignment review | Actual explicit ADR approval/reuse recorded; independent whole-change alignment review complete, transactional finding fixed RED-to-GREEN with the final suite/gate passing. |
| Exact released combination, observed loaded sources/native discovery and propagation decision | INCOMPLETE; require owning deliveries, source-identical evidence and separately scoped selection/authorization. |

Keep all applicable B01-B16 requirements, targeted controls and expansion rules
from the approved spec. Failures must be preserved and affected tests rerun on
changed inputs; do not average them away or substitute metadata for behavior.
No companion write, GitHub issue mutation, tag, release or adopter migration
was performed to create this receipt.

## Review boundaries and execution rulings

The final reviewer considered but declined to certify the following behaviors.
The executor retains each boundary rather than treating it as passing evidence:

- Companion delivery/shared-targeted behavior/internal use: remain owning
  dependencies. Cost if wrong: propagation stays blocked until actual records
  establish coverage; starter prose cannot discharge them.
- Native discovery and macOS/Linux execution: remain unverified. Cost if wrong:
  add actual host proof before claiming those platforms or combined readiness.
- Authenticating a supplied starter SHA against the executing artifact: retain
  the existing caller-reviewed source/publication contract; no new network
  authentication feature is added. Cost if wrong: an incorrectly selected SHA
  can misidentify source until the caller/release checks detect it.
- Independent authenticity of the conversation: the receipt is an honest agent
  transcription with preserved reviewed content, not external attestation.
  Cost if wrong: resolve approval provenance before depending on disputed authority.
- Broader inherited filesystem races/junctions: no adversarial concurrency
  certification is claimed. The demonstrated partial-write bug is fixed and
  replacement-preservation controls pass. Cost if wrong: qualify/fix an observed
  additional race before broadening filesystem-safety claims.

Execution rulings preserved in the handoff: use the existing checkout on a feature
branch to retain approved dirty artifacts (subsequently superseded by the
maintainer's direct-main instruction); native PowerShell progress bookkeeping (reconcile progress if its
semantics diverge); focused tests in `test_adr_policy.py` (correct focused commands
if needed); existing update skill retained because its application baseline
passed (extend it only after a demonstrated gap). No deferred review minors.
