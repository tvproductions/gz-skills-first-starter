# Release-planning audit and correction — November 1, 2026

## Direction and source

The maintainer clarified: PRDs guide majors, selected work and requirements drive
minors, and fixes drive patches. The maintainer requested inspection and correction
of adopting projects, primarily under `agents/` and `xp/`. Local binding changes
are authorized; Git sync, publication, plugin changes and new product scopes are
not implied.

Source: starter base `8d090f88bf45b9a755808a62c1445beeb005daff` plus these
authorized uncommitted corrections. Pending **0.8.1** is not published. Each local
binding records the base plus exact development content, not a false claim that
the base commit contains these edits:

| Source | SHA-256 |
| --- | --- |
| `docs/versioning.md` | `7a3010f2fb6cb7c541485f7415fb0520e26a6cfc84f47b075c623cb3ebecd530` |
| `templates/AGENTS.skills-first.md` | `69ada3ed423076ebbe8f9dba2c29be965b0a834f6046dd42ea27c6682fa52cd1` |

## Root cause and observed behavior

The previous canonical policy contained SemVer classification, new major PRDs,
coherent minor bundles and compatible fixes. It did not explicitly require the
PRD/work/defect hierarchy or current release-scope accounting at planning and
closeout. Older installed adopter fragments had no product-release rule at all.
Copying the starter's template-oriented versioning document also left product
release history unclear, notably in gz-mcp-lsp.

Task counts alone do not prove a versioning defect. FDAU has an explicit first
release vertical-slice/G1 gate; gz-mcp-lsp has an approved initial implementation
and acceptance scope. Tasks within those scopes are not independent releases.
Conversely, unpublished status must not defer release accounting indefinitely.
Backplane's latest handoff explicitly leaves that accounting unresolved and
records that no smaller first release was approved.

Two concrete defects were found. Health's changelog still said 0.1.0 was
unreleased, although GitHub confirms publication at `2026-10-25T18:18:25Z` and
its local tag resolves to `38afff129e236b8b581a42b97525e732568a94bb`.
WebAPI's published v4.0.0 supports `>=3.12,<3.14`; pending adoption changes
narrow support to `>=3.12,<3.13` while retaining version 4.0.0. Shipping that
removal needs a new PRD guiding 5.0.0, or a scope correction retaining support.
The existing runtime decision and dirty work are preserved, not silently reversed.

## Inventory and local dispositions

Inspected all direct project directories under `U:/repos/agents` and `U:/repos/xp`:
Git status, local tags, metadata, instructions, adoption records and relevant
release/planning/handoff material. Used direct `git` and `gh`. Release queries
succeeded after read-only network escalation; initial proxy failures are not
treated as evidence of absent releases.

| Project | Observed state | Correction and next disposition |
| --- | --- | --- |
| starter | Published 0.8.0; Windows host fix pending | Select 0.8.1 for compatible host and existing-policy corrections; reconcile metadata/lock/resources. No publication. |
| gz-mcp-lsp | Development 0.1.0; no local tags or GitHub releases found | Add local binding. Preserve approved reference-parity scope and remaining acceptance; inherited starter history is not product history. |
| gz-skills | Published v0.8.3, tag commit `d6acc26e28ca1c4f43e5bb46d8973021d7d006c3` | Extend existing release-policy binding. Repository-only policy clarification changes no shipped skill; select next shipped bundle separately and retain independent skill versions/reviews. |
| Backplane | Plugin metadata 0.1.0; no local tags or GitHub releases found | Extend existing binding. Keep unresolved first-release accounting and unfinished #4/OpenCode acceptance explicit; preserve approved scope. |
| Ortho4XP | Legacy metadata 1.4; no local tags or fork GitHub releases found | Add local binding. Establish actual upstream/distributed baseline before a three-component successor. Do not reset history or bundle the entire roadmap. |
| q4xpcc | Development 0.1.0; no local tags or GitHub releases found | Add local binding. Separate selected first-release requirements from future minors; retain phase identities and external FDAU gates. |
| FDAU | Development 0.1.0; no local tags or GitHub releases found | Add local binding. Preserve selected vertical-slice/G1 gate, completed children and deferred work. No invented earlier release. |
| Health | Published v0.1.0 | Add language-independent binding and correct stale changelog. A selected capability bundle would drive 0.2.0; fixes alone 0.1.1. No bundle selected or Python-baseline adoption claimed. |
| WebAPI | Published v4.0.0; substantial dirty adoption work | Add binding with support-removal classification. Compatible requirements would drive 4.1.0; fixes alone 4.0.1. Resolve support removal before release; preserve unrelated edits. |

Five other directories are not represented as current starter adopters:
landingmon has no root repository/adoption evidence; md80companion, xpcl and
xpclp have no inspected starter adoption record; xplane-windows-toolkit is an
explicitly frozen migration donor whose canonical product is Health. No policy
or adoption was installed into these projects. Coverage does not extend beyond
these two directory roots or establish undocumented distribution history.

Observed HEADs: gz-mcp-lsp `05aa14b9885e511f04340e422298d784e8a74174`,
gz-skills `9a7970208207d68cc4a04eff7c3d39bcea664463`, Backplane
`0aa0cc007db63449455a1c4f9b6d92cb60c5d29a`, Ortho4XP
`6f0bb4e290d4d651e9e6f85f8020e6eaa1294030`, q4xpcc
`9270f5ad511f4a06ec365f2eb40511d6078b3043`, FDAU
`bf852356550096d281438b19b54f4342b2906eb4`, Health
`ed98645a13bdd34f12fb139a2a740c6d782aa030`, WebAPI
`a855b8d885c75f8dda54daec1f54eb48f111b105`. FDAU advanced during inventory;
its later required audit observed C2.2 verified. No progress was overwritten.

## Changes and limits

Corrected canonical versioning, root instructions, adopter fragment and runbook;
regenerated wheel copies. Pending 0.8.1 restores execution of existing commitments
and fixes the existing host defect; no new capability or tooling baseline is
introduced. Both catalogs keep their independent component pins.

Applied complete local bindings to six project AGENTS files and the companions'
two existing release-policy documents. Updated existing unreleased changelogs in
gz-mcp-lsp, gz-skills, FDAU and WebAPI; corrected Health's release status and added
its pending policy entry. Product versions, locks, plugin activation, approved
plans and backlog states are unchanged. This is a targeted policy correction,
not a full starter upgrade.

Unresolved scopes remain unresolved. Backplane's first-release bundle,
Ortho4XP's distributed baseline and WebAPI's support-removal disposition still
need governing decisions. The instructions now require explicit reconciliation
in existing authorities before release preparation can pass; this audit does
not invent approval or claim every project has complete release accounting.

## Verification

Starter: uv 0.13.6, managed Python pin 3.14.10. Locked all-group sync, all four
pre-commit hooks (Ruff check/format, ty, unittest), bundle/both-catalog validation,
source-independent build and isolated installed-distribution checks passed for
pending 0.8.1 and regenerated guidance. No analyzer changed; analyzer CLI tests
are not triggered. No new tests mirror documentation wording.

Project corrections: reviewed scoped diffs and whitespace checks. FDAU's required
backlog audit reported no findings and retained `wait child=C2.2`; its 15
documentation tests and 10 project-skill tests passed. WebAPI's 23 documentation
tests passed with unrelated pending adoption work preserved. q4xpcc's required
full hygiene command completed with exit zero: all 1,997 unittests passed, and
its required lint, metrics, cohesion and available native checks completed.
That project's retained legacy analyzers are not proof of the starter's current
retired-tool policy conformance; this correction did not change tooling.
Runtime/installed acceptance
for other products was not rerun for these documentation-only changes. No native
discovery, complete product acceptance, CI, sync or publication is claimed.

Final starter artifact verification after adding the audit/handoff also passed:
actual interpreter `Python 3.14.10`, `uv build --no-sources`, installed CLI/wheel
and sdist checks, generated-resource drift check, and `git diff --check`.
Documentation-only receipt edits reuse the passing routine checks on unchanged
implementation inputs. All local corrections remain uncommitted.

## Follow-up: reliable decision procedure

The maintainer requested a reliable policy after the initial correction.
Expanded the canonical policy with a mandatory six-step procedure: establish
baseline, identify governing commitment, classify the entire pending scope,
select/reconcile one target, bound the release, and verify/report the decision.
Added explicit version arithmetic and a compact record for existing authorities.
Apply it at requirements intake, planning and closeout, not only publication.
Agents derive routine version changes within authorized work; only unresolved
product decisions require maintainer input. Missing required PRD/scope/version
evidence blocks the applicable completion claim. This is a mandatory agent
procedure; no automatic semantic classifier or new lifecycle was implemented.

Updated all eight local bindings with those checks. Their current source hashes
supersede the initial snapshot above; both snapshots remain unreleased development
guidance based on the recorded starter commit:

| Source | Current SHA-256 |
| --- | --- |
| `docs/versioning.md` | `960cc4052cb87696980be23a393553079f254ac8105240dbcbac5244a52c4460` |
| `templates/AGENTS.skills-first.md` | `0383bc3330756600b2d9e0ae2393af0143836b7e6bc3b5b8d407e39f361b51b4` |

The selected pending patch remains 0.8.1: this completes the existing
release-planning correction without adding product capability or tooling policy.
Earlier product checks remain applicable to unchanged implementation inputs;
the only follow-up project edits extend the same documentation bindings.

Follow-up verification passed: locked all-group sync, regenerated resources,
all four pre-commit hooks, bundle/both-catalog validation, source-independent
build and isolated installed-distribution checks. All eight local bindings
contain the required decision checks and match the current two source hashes;
scoped whitespace checks pass. Changes remain local and uncommitted.
