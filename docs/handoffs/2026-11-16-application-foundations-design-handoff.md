# Application foundations — fresh design handoff, November 16, 2026

## Resume disposition

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
