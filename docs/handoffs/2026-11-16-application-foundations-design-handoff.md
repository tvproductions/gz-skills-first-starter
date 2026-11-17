# Application foundations — fresh design handoff, November 16, 2026

## Continuation: roadmap reconciliation

**0.11.1 is published and verified**, source
`041c1989406c1b9c4978042661c2dd38ff1db160`, annotated tag object
`1aa29e6fe24214a7ce85073fc599da84169cea82`. Both jobs passed in
[exact-release-source CI](https://github.com/tvproductions/gz-starter/actions/runs/44054657062);
downloaded tagged source matches all 216 Git entries, including both symlinks.
The [release receipt](../evidence/2026-11-17-0.11.1-release.md) records publication,
freshness/security checks, preserved limits and recovery from the initial
email-privacy push rejection using only an unpublished-commit identity correction.
Resume from released 0.11.1 with the next explicitly selected work. No pending
release target or new feature is selected; do not reopen completed release gates.
This publication-result follow-up is synchronized ordinarily and its exact CI
is observed in the sync response; do not add a receipt-only commit chain.

**November 17 roadmap reconciliation:** the maintainer requested correction of
obsolete rename/ADR backlog entries. The roadmap now records their completed
0.10.0 delivery and the 0.11.0 guidance/path-rejection delivery, preserving the
remaining Ruff/ty enforcement, real-adopter, upgrade/rollback, native/platform,
acceptance-reporting and management-record work. Rename guidance and active
README continuation/release pointers are reconciled. Historical release and
approval records retain their identities; do not reopen their completed gates.

Published baseline **0.11.0 -> 0.11.1 / patch**, governed solely by this compatible
documentation correction. The maintainer subsequently requested “commit, push,
publish”. This authorizes ordinary main sync and 0.11.1 publication after the
required gates; it supersedes the earlier uncommitted/unpublished disposition.
No new feature or architecture is selected. Exact-source CI and immutable
publication verification are complete as recorded above.

Verification on uv **0.13.8** / managed CPython **3.14.10**: reviewed the complete
diff against both release receipts and the exact ADR-combination evidence;
all **153** local references/anchors in the six changed Markdown files resolve.
`uv run --locked pre-commit run --all-files` passes all four hooks;
`uv run --locked gz-starter validate`, resource drift and offline lock checks pass.
`uv build --no-sources` and `uv run --locked python tools/verify_distribution.py`
pass for 0.11.1, including isolated installed CLI checks. Bundle, pyproject, local
lock entry, runtime output and generated bundle copy agree on **0.11.1**; the
lock diff changes only this project's version. No dependency/component selection
changed. The final evidence-only prose updates reuse these passes under the
verification policy. No new behavioral test or analyzer/platform replay is
needed; existing release limits remain. The
[0.11.1 release receipt](../evidence/2026-11-17-0.11.1-release.md) adds fresh
official registry/runtime/component/Action checks and clean exact-lock security
audits for this candidate. Normal hooks remained enabled; local/remote release
alignment and exact-source CI were verified before tagging. Publication identities
are recorded above; verify this follow-up's CI without another receipt-only commit.

**Published November 17:** [GZ Starter 0.11.0](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.0),
source ccac3b5e1ac03f2cf5642d7766aed6e68001997c, annotated tag object
7040c90aa86feecf5cd2367d81cd41fe9f69d697. Exact-source CI run 44050428855
passed both jobs before tagging. The downloaded tagged source matches all 212
files of local git archive. The release receipt records observed identities and
retained conditional engineering limits.

The completed release is the baseline for the documentation correction above;
no next feature scope is selected. Design edition 3, ADR-0002 edition 2, implementation,
maintenance, scoped acceptance and publication are complete. Do not request
those approvals again or reopen completed plan tasks. Cognitive qualification
remains DEFERRED / measurement UNKNOWN; documented native/embedded and broader
interface limits remain. This publication record supersedes earlier checkpoint
statements below. The final documentation follow-up is synchronized ordinarily,
with its own exact-commit CI observed; do not add a receipt-only commit chain.

### Historical execution checkpoints — superseded by publication above

November 17 release checkpoint: the maintainer requested “git sync and
do release”. The 0.11.0 release scope and version are reconciled, official
freshness/deeper analysis/typing evidence is complete, and the independent
release-delta review found no material defects. See the
[release receipt](../evidence/2026-11-17-0.11.0-release.md). Synchronize this exact
candidate, observe both CI jobs for its SHA, then tag/publish under that explicit
authorization. Preserve immutable 0.10.0 and all existing deferred work.
This request supersedes earlier statements withholding Git/release authority;
native installations, companion edits and real-adopter migration remain outside
scope. Publication identities are recorded after actual observation.

Current November 17 execution: the maintainer explicitly replied
“approve ADR-0002 edition 2”. Approval metadata and the exact reviewed draft are
preserved with [ADR-0002](../decisions/ADR-0002-002-runtime-configuration-boundary.md).
Implementation of the revised plan is complete locally on main: foundation policy,
both-lane pointers, generated resources, starter path rejection and a local dev
CLI/library fixture are delivered in the working tree. Initial four-hook gate,
95 owning tests and extracted-sdist installed/reinstall artifact checks pass.
Independent review returned four Important findings; the single correction pass
fixed them and verified CLI redaction, empty-root rejection, poisoned-parent
environment isolation and missing path/bounds/preservation controls. Use the
[implementation evidence](../evidence/2026-11-17-application-foundations.md).
Preserve the separate maintenance work. No commit, push, native plugin action or
release publication is authorized by this implementation. Earlier pending-approval
and no-implementation dispositions below are historical and superseded here.
Resume with Git synchronization if requested, or separately authorized release
preparation and its candidate-specific freshness/deeper acceptance. Do not
request design or ADR approval again. Cognitive qualification remains DEFERRED /
measurement UNKNOWN; native/embedded and broader interface limits stay explicit.

November 17 planning continuation: the maintainer returned to the pending plan
refinements and ADR approval. The implementation plan now addresses all three
recorded findings: root-owned tests/type checks and source-distribution/installed
verification; target-content read guards with a deliberate-read positive control;
and an explicit fixture schema, modules, typed interfaces, CLI contract and
build/install commands. A reached atomic-replacement failure must preserve prior
bytes and remove its temporary sibling. The revised plan awaits maintainer
review. ADR-0002 edition 2 remains unapproved; both reviewed design/ADR hashes
remain unchanged. No dependent implementation has begun. Preserve the separate
uncommitted maintenance changes. Earlier open-refinement statements below are
historical and superseded by this continuation.

November 17 maintenance continuation: the explicit `gzs-update-dependencies`
invocation completed the five-package migration in both Python baselines.
Use the [new maintenance receipt](../evidence/2026-11-17-starter-maintenance.md)
and registry/candidate hashes for current evidence. Lizard's existing contract
is requalified; all routine hooks, checker regressions, artifact checks and
standalone baseline checks pass, and both security audits find no known
vulnerabilities or skipped packages. Changes remain local pending Git sync.
This supersedes the freshness limitation below without approving the plan or ADR.

On November 16, 2026, the maintainer replied “approve” in the main
conversation immediately after being asked to approve the complete design
edition 3 identified below. This approves those exact draft bytes; it does not
approve ADR-0002 edition 2. The original disposition below is preserved as
the historical handoff. The implementation plan is
[application foundations](../superpowers/plans/2026-11-16-application-foundations.md).
Separate explicit ADR approval remains necessary before dependent implementation.

November 17 continuation: the maintainer requested review of the plan in the
main conversation, then Git synchronization. The plan is a draft save point,
not accepted for execution. Review identified three refinements before execution:
explicit fixture test/type/build integration and distribution delivery;
an observable guard proving rejected paths are not read, beyond unchanged-file
assertions; and a concrete fixture schema, typed interfaces, module boundaries
and build/install commands. Preserve these open findings and complete the plan
before dependent implementation. ADR-0002 edition 2 remains unapproved, with its
reviewed bytes unchanged. Design approval does not need to be requested again.
The pending release target remains 0.11.0; no implementation or release acceptance
is claimed. The earlier bounded freshness check did not establish newer targets;
the November 15 maintenance receipt remains the latest complete review.

Sync validation on November 17 used uv 0.13.8 and managed CPython 3.14.10 on
macOS ARM64. The full pre-commit run passed Ruff check/format and unittest;
ty initially found missing hygiene imports in the newly created environment.
`uv sync --locked --all-groups` restored the declared locked environment, then
`uv run --locked pre-commit run ty --all-files` passed. Catalog validation,
`uv build --no-sources` and `uv run --locked python tools/verify_distribution.py`
passed, including isolated installed CLI checks. No pins, locks, catalogs,
analyzers or runtime behavior changed. Exact-commit remote CI is observed after
push and reported with the sync result, without a CI-receipt-only commit chain.

## Original resume disposition (historical; superseded above)

**Resume with maintainer review of design edition 3. Design approval is pending;
do not begin implementation.** The latest request is to preserve this disposition
in a fresh handoff and perform ordinary Git synchronization. “good, what next?”
acknowledged the discussion; it did not explicitly approve the complete identified
design or architectural ADR. This handoff/sync request supplies no such approval.

Current artifacts:

- [Application-foundations design, edition 3](../superpowers/specs/2026-11-16-application-foundations-design.md).
  SHA-256: `54b2a94c5be72dfa93abb65101db384f3c2dad61c720e53b095b6bdc191367a6`.
- [ADR-0002, draft edition 2](../decisions/ADR-0002-002-runtime-configuration-boundary.md):
  resolve runtime configuration at the application boundary.
  SHA-256: `94b414de72d191ab9d3cd7c7fcc968e6beb708eeb93e9d24fea09d341212758b`.
- [0.11.0 scope](../../ROADMAP.md#selected-0110-scope--application-foundations-november-16-2026)
  remains the release-planning authority. The earlier
  [release/design handoff](2026-11-15-adr-release-session-handoff.md) is history.

These hashes identify reviewed draft bytes, not acceptance. Design approval,
architectural approval, implementation acceptance, Git sync and publication are
different results. Record the actual explicit approvals when given; preserve
the reviewed bytes and edition history. Do not infer them from this save point.

## Decisions supplied by the maintainer

- Use **settings.json** for application runtime settings. Separate that concern
  from pyproject packaging/dependencies/workspace and supported tool settings.
- Right-sized hexagonal architecture retains the principles with fewer
  components. Give agents strong guidance and offer operators actionable
  warnings; respect explicit informed human departures without repeated
  questioning. Existing mandatory engineering policy and approved decisions
  retain their authority.
- **Reject paths containing spaces, including user-selected paths.** The
  maintainer reaffirmed “we do not want paths with spaces, it is sloppy.” Keep
  validation of supplied/resolved paths and no-partial-write behavior in scope;
  do not reinterpret this explicit input contract as a warning-only convention.
- Every adopter has a deployment/configuration concern. Identify its deployment
  unit, configuration owner, location, loading/override behavior and evidence.
  Libraries/plugins identify the configuring consumer/host rather than silently
  reading global settings or declaring the whole concern inapplicable.
- Incorporate Astral's guidance on project types. uv's application/library roles,
  packaging and workspace organization are separate from interface and
  deployment/configuration scopes. A Python web server is an application even
  without its own project.scripts entry. Web does not imply portable delivery;
  portable operation needs an explicit relocation/preservation contract.

## Draft scope and proposed defaults to review

The design proposes foundations for settings, environment variables, secrets,
errors/logging, paths/data, persistence/recovery, external calls, input/trust,
data semantics, operation, privacy and interface contracts, in both lanes.
Settings live outside replaceable installed code by default, with explicit
project/user/service/host/portable ownership. File selection is explicit launch/
API path, then documented application config-path variable, then one declared
scope-specific default. Select one file and fail an invalid explicit selection.
Value precedence is defaults → settings.json → documented environment values →
explicit CLI/API overrides. Boundary validation precedes application effects;
domain logic receives values. Secrets use external references/injection, with
redacted diagnostics and deliberate process forwarding. No automatic dotenv
discovery or arbitrary working-directory settings search is proposed.

Deliver guidance with one small invented CLI/library reference fixture and
meaningful positive/negative behavior evidence, not a shared application runtime.
Keep the existing four routine hooks. The broader November 14 Ruff/ty patch,
majority-rule quota and its 14-finding remediation remain deferred. Reconcile all
15 naming/layout topics as guidance, including the earlier draft's erroneous
command-only application classification. No active rule patch or path-rejection
implementation has been delivered by this design work.

Source comparison is explicit: GZKit main was read at
`04d901b7f594de50f908f66cc1d0ce54210828e8`, including its house-style inventory
(108 candidates), R&D rulings, hexagonal specification and RP-7/RP-15 drydock
plans. The design has a complete numbered disposition crosswalk. Distinguish
GZKit's commissioned, landed and actually conformant behavior; import none of its
ledger, kernel dependency, lifecycle or blanket tool selections. Selected
gz-skills 0.13.0's audit was inspected at
`0bdab63fc503c6b36e2dd487932689b4e555e41a`: it is a useful general coupling
audit, not demonstrated verification of this stronger chosen contract.
Portable audit improvements stay upstream-owned and need their own authorized
work; no companion mutation or unreleased capability is claimed here.

## Review and exact next steps

The independent builder check of edition 1 found two consequential questions:
lint activation and the path rule. Their dispositions are recorded above. A
focused independent check of edition 2's universal deployment/configuration and
location changes returned “Nothing important left in the changed scope.”
Edition 3 adds official-source Astral classification and web/portable
clarifications; it has source/diff review, not a new whole-design independent
review or native web qualification. Do not relabel the earlier check's scope.

1. Present the concrete design edition 3 for main-conversation review and obtain
   explicit approval of that design. Preserve these accepted inputs rather than
   asking the same questions again. Handle genuine requested changes first.
2. After design approval, use Superpowers writing-plans to produce the bounded
   implementation plan. Keep project main/worktree and verification policy.
3. Obtain separate explicit approval of **ADR-0002 edition 2** before its dependent
   implementation. Plan/design/release assent is not architectural approval.
4. Execute only the subsequently authorized plan, with scoped owning tests and
   existing integration checks. Release preparation additionally needs its own
   dependency-maintenance/freshness and acceptance evidence. No release is
   authorized by the present handoff or Git sync.

## Version, verification and synchronization

Published baseline: **0.10.0**, immutable tag source
`6b236d87f301f689edae6934dabee9495df726d4`. Pending target: **0.11.0 / minor**.
Bundle, pyproject, uv.lock project version, runtime output and packaged bundle
agree. Only local-project version metadata changed in the lock; dependencies,
interpreter/tool selections and component pins remain unchanged. No additional
per-topic bump. Preserve published tags and the existing 0.10.0 release.

Pre-handoff main is `78c059d`, three unpublished local commits above origin's
`f8e5200584ad66b9afc991bb5d8879186f426513`; a fresh fetch found **3 ahead / 0 behind**.
The worktree was clean. Those commits contain the reviewed design/ADR/scope and
planning-version reconciliation; the handoff commit adds only this record and
continuation pointers. Preserve main and normal hooks; push ordinarily without
rewriting history. The final sync response must identify the handoff commit,
prove main/origin alignment and observe CI for that exact SHA. Do not append a
self-referential CI-receipt commit chain.

Actual tools are uv **0.13.8** and managed Python **3.14.10**. This session's
five focused version/resource tests passed, as did catalog validation, six-resource
drift, lock consistency, the 0.11.0 source-independent build and isolated installed
CLI checks. At the sync integration checkpoint,
`uv run --locked pre-commit run --all-files` passed all four hooks; catalog,
resource-drift and lock checks also passed. Reuse unchanged analyzer/platform
inputs appropriately; no analyzer implementation changed. The actual web/host
runtime examples and proposed foundation behaviors are not implemented or
qualified. Freshness uses this session's bounded official checks and applicable
dated evidence; no dependency migration is authorized by the sync.

Cognitive qualification remains **DEFERRED / measurement UNKNOWN**, ceiling 15.
Keep recorded deeper-tool, cohesion, native-host and embedded-deployment limits.
No strict release/adopter conformance, plugin installation, Backplane activation,
upstream edit, real-adopter migration, tag or publication follows from Git sync.
