# Application foundations and house style — 0.11.0 design

Status: **draft for maintainer review, edition 2, November 16, 2026**.
This is design work, not active adopter policy or implemented behavior. Design
approval and separate approval of an identified architectural ADR edition remain
distinct. No publication, upstream edit, adopter migration or native installation
is authorized by this document.

## Intent and selected scope

Give Python adopters a coherent application foundation alongside the existing
tooling, packaging and engineering baseline. Agents need concrete defaults and
evidence expectations for configuration, secrets, boundaries and operation;
operators retain authority to choose departures. Apply in both lite and heavy
lanes without imposing Backplane activation or its lifecycle.

The maintainer selected this work as minor-level scope, requested Superpowers
brainstorming, agreed that right-sizing reduces components while retaining the
architectural principles, required guidance and operator warnings rather than
universal architectural gates, and selected **settings.json**. These conversation
decisions establish design inputs, not approval of this identified edition or an
architectural ADR. Exact quotations: “let these be guidance for agents and warnings
offered to operators, if the operator/human overrides, so be it”; “settings.json”.
The maintainer subsequently reaffirmed the specific path restriction: “we do not
want paths with spaces, it is sloppy.” Retain rejection as the default behavior,
including user-selected paths; the general architectural warning posture does
not weaken that explicit input contract.
The maintainer also specified: “we'll always have some deployment/config aspect
with any adopter.” Edition 2 makes the deployment/configuration contract universal
and separates that obligation from the location chosen for each deployment.

Published baseline: **0.10.0**, tag v0.10.0 at
`6b236d87f301f689edae6934dabee9495df726d4`; publication was verified through
`gh release view`. Target: **0.11.0 / minor**. New adopter guidance and an explicit
configuration/architecture contract change the pre-1.0 adoption contract. Reuse
this target for the coherent bundle, not a bump per topic. The existing roadmap
owns release accounting. Implementation and release acceptance remain incomplete.

## Approaches

1. **Written standards alone.** Smaller delivery, but adopters must infer how to
   demonstrate precedence, isolation and warning/override behavior.
2. **Guidance with bounded worked verification — proposed approach.** Publish
   clear defaults, explicit applicability, a small invented reference application,
   and tests of consequential observable behavior. Keep real application loaders
   and checks project-owned. This expresses the selected agent-guidance posture
   without a new runtime framework.
3. **A shared runtime framework and compulsory architecture gates.** Not selected:
   the maintainer chose operator-overridable guidance, and this starter owns
   policy/adoption tooling rather than a shared application framework. GZKit's
   kernel, registers, work packages and drydock are not imported.

The worked-verification delivery is a design recommendation for approval, not a
claim that the maintainer separately selected every implementation detail.

## Authority, warnings and overrides

Distinguish four things throughout prose, examples and reports:

- Existing mandatory engineering requirements remain in force, including Python
  policy, locked tools, four routine checks, packaging, ADR practice and truthful
  acceptance. This feature does not silently waive them.
- New house-style and architectural recommendations are strong defaults for
  agents. Agents follow them, or explain a relevant departure and its consequence
  before making the departure. They do not invent permission to depart.
- A human may accept a different design. Record the choice and its scope briefly
  in the existing design, project instructions or applicable ADR; proceed and do
  not repeatedly ask or warn about the same unchanged choice. No waiver database,
  acceptance service or recurring reminder is introduced.
- Runtime errors are a different dimension. Malformed JSON, invalid supplied
  settings, absent required credentials or failed writes must follow the product's
  error contract. An architectural override does not make an unsuccessful runtime
  operation successful or authorize bypassing a failed required check.

The specifically selected no-spaces path contract is a rejection rule, not an
advisory architecture finding. Human authority still permits a later explicit
change to that contract; agents must not infer one from general warning guidance.

A useful warning names the affected boundary, concrete consequence, recommended
alternative and proposed action. Emit it at a meaningful design/review point;
repeat only when scope or evidence materially changes. Optional architecture
checks report findings by default. A project may explicitly promote a selection
to its own gates. Approved ADR changes still use the existing ADR policy; ordinary
guidance departures need no ADR unless they actually change an architectural
decision. No numeric architecture score or automatic conformance claim is added.

## Configuration contract

### Responsibilities

| Home | Owns | Does not own |
| --- | --- | --- |
| pyproject.toml | Packaging, dependency groups, workspace declarations and supported tool settings; any future code-design checker settings under its actual owned namespace | Mutable deployment settings or secret values |
| settings.json | Application runtime settings, in a project-owned schema | Python dependency declarations, native host configuration or secret material |
| Environment variables | Explicitly documented process inputs and overrides | An undocumented second settings schema or arbitrary executable expressions |
| Secret source | Credentials and other sensitive values resolved at the application boundary | Committed values in examples, metadata, evidence or build artifacts |

Every adopter must identify its deployment and configuration contract, including
libraries, plugins, command-line tools and hosted applications. Do not label the
whole concern inapplicable because a project has few settings or no standalone
process. Identify what is installed/deployed, who configures it, the settings and
secret inputs, the loading boundary, the selected location, upgrade ownership and
verification. This requirement to identify the contract is universal; the runtime
mechanism follows the actual consuming application and host.

settings.json is the house default for operator-managed runtime files. A library's
consumer may supply validated arguments; the contract then identifies that
consumer and its deployment/configuration responsibilities. The library must not
silently search the user's filesystem or environment. A host may own loading and
pass settings into its plugin. Document even an empty operator-settings surface
and how deployment inputs are supplied; do not invent a second loader merely to
create a file. Existing adopter formats need an inventory and reviewed migration
or an operator-selected departure; adoption must not overwrite them. There is no
generic settings loader in the starter helper and this design adds none.

### Configuration ownership and location

The common rule is **one selected settings file at a documented configuration
root, owned by the deploying operator or consuming host**. Mutable settings live
outside the installed code by default, so code replacement does not replace
operator settings. The installation may contain immutable defaults and an
example; installation, code, data, cache and configuration are distinct roles.
The same directory may serve multiple roles only through an explicitly selected
deployment contract, such as a portable application. Do not assume a site-packages
directory, executable directory, repository root or current directory is the
universal configuration home.

| Configuration owner/scope | Location selection and proof |
| --- | --- |
| Project-owned operation | settings.json under the explicitly selected project/workspace root, or an explicit external path; prove that two projects do not read each other's settings |
| Per-user installed application | A documented application-specific directory under the selected user configuration root; resolve the OS directory through its supported mechanism where applicable; prove separate-user isolation and survival across code replacement |
| Service/container/deployment | An explicitly supplied absolute file, commonly mounted or provisioned by deployment tooling; document the process identity, access permissions and whether the mount is read-only; do not infer the interactive user's home |
| Host/plugin/library consumer | The host/consumer owns its file and passes the selected settings or explicit values across the boundary; document the host initialization and precedence contract |
| Portable deployment | An explicitly selected writable deployment/configuration root; settings may be beside the executable when that contract preserves them on update and the no-spaces rule holds; no automatic portable mode merely because a nearby file exists |

File selection is distinct from value precedence. Proposed application rule:
**explicit API/launch --config path → documented APP_CONFIG file-path variable →
the application's one declared scope-specific default**. A host-supplied explicit
path/value contract uses the first branch without inventing a CLI. Select one
file, not an implicit merge across project, user and system scopes. An explicitly
supplied invalid, empty, inaccessible or missing selection fails; do not quietly
fall through to another file. Relative explicit paths resolve once against the
invocation's documented base and become absolute; do not let later directory
changes affect them. Diagnose the selected location without secret contents.

For the current Python CLI baseline, XDG_CONFIG_HOME with HOME/.config fallback
is an available Linux default; uv also documents .config on macOS, an appropriate
CLI precedent rather than a universal desktop rule. Windows selection must state
whether settings are local or roaming and use the corresponding configured known
folder rather than synthesizing a username path. Native macOS Application Support
contains a space: our strict path contract requires an explicit space-free
configuration root. The same applies to any spaced home/redirected directory on
any platform. Reject with actionable guidance; do not rename an OS directory,
strip spaces or switch locations silently. Services and hosts select their own
roots through the deployment contract. These are location recommendations;
TUI/web/desktop/embedded qualification remains separate from Python CLI proof.

Official location context, checked November 16:
[XDG](https://specifications.freedesktop.org/basedir/latest/),
[uv](https://docs.astral.sh/uv/concepts/configuration-files/),
[Windows known folders](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid),
[macOS directories](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html).
Platform conventions inform the selected profile; they do not override the
maintainer's explicit no-spaces rule or establish qualification of an untested host.

### Proposed loading semantics

At the application's declared configuration boundary, use one configuration
adapter at startup and pass the resolved settings inward as values. Keep environment/file
reads and concrete adapter selection out of domain logic. In services or hosted
plugins, startup means the owning application/host initialization boundary, not
each request. Explicit reload is a separately designed capability.

Proposed precedence, lowest to highest: **built-in defaults → one selected
settings.json → documented environment overrides → explicitly supplied CLI/API
overrides**. Omitted CLI values must not overwrite lower layers. The application
selects a settings file by an explicit argument or a documented application
location, never an uncontrolled walk through the current working directory and
its parents. An explicitly selected missing/unreadable file is an error. Absence
at an optional default location permits defaults only when the contract says so.
Do not edit installed packages or require a source checkout at runtime.

Use UTF-8 JSON with an integer schema_version when a persistent external schema
exists. Reject malformed JSON, duplicate keys, nonfinite numbers, wrong types,
unknown owned keys and unsupported versions with actionable messages that omit
secret values. Validate the resolved settings before application effects. Preserve
deliberate application extension namespaces; reject unknown keys within the
owned schema rather than blocking explicitly supported extensions.

Merge only documented object fields; scalars and arrays replace rather than
concatenate. No recursive merge or interpolation by accident. Define null,
empty-string and absent semantics per setting. Resolve relative paths from the
selected file's directory; environment/CLI/API paths use their documented base,
and the resolved result must not depend on an incidental later working directory.
Require explicit migration handling for an older schema instead of rewriting
an operator's file while reading it.

Expose configuration validation and redacted effective-source diagnostics when
useful: key, winning source and safe value, with sensitive values always omitted.
This is an application contract, not a new starter CLI command.

### Environment variables

Adopt the existing draft's documented uppercase project-family convention,
preserving real external names such as PATH, HOME and UV_CACHE_DIR. Single-member
applications may use FAMILY_THING; workspaces use FAMILY_MEMBER_THING. Inventory
each supported variable's type, default, requiredness, sensitivity, precedence,
path base and reload behavior. Environment values remain strings until explicitly
parsed. Parse booleans from a documented closed set, numbers with bounds, lists
with one documented encoding, and paths with explicit resolution. Never use eval,
shell expansion or truthiness of a nonempty string as a boolean parser.

An absent value permits fallback; an empty supplied value is validated according
to that setting's declared contract and does not silently become absent. Bad
values report the variable name and expected form without exposing sensitive
contents. Ignore unrelated environment names. Tests isolate relevant variables,
including developer UV/PYTHON settings when they affect the tested process.

No automatic dotenv discovery. If a project needs a local .env workflow, document
the explicit loading mechanism, selected file, syntax and precedence; the real
process environment wins over local dotenv values. .env is plaintext local input,
not a secret manager. Commit placeholders only in .env.example; review ignore and
artifact-exclusion patterns without hiding unrelated files. Child-process
environments inherit deliberately: preserve required platform variables, remove
unneeded sensitive entries, and document necessary forwarding. Do not break child
startup with a universal empty-environment rule.

## Secrets and trust

Keep real credentials out of committed settings, URLs, command arguments,
examples, test fixtures, logs, errors, transcripts and distributions. Committed
settings may name a credential reference; resolution belongs to the config/secret
adapter. Use an existing OS/service credential facility or CI secret injection
where applicable; select no universal secret backend or new dependency here.
Environment injection is supported but is not treated as inherently confidential
storage. Avoid environment dumps and indiscriminate child forwarding.

Use least-privilege credentials, separate development/test/production identities
where those environments exist, and document rotation/revocation and incident
ownership. On suspected exposure, prevent further disclosure, revoke/rotate the
credential and identify affected locations with redacted evidence. History
rewrites and external incident actions require their actual authorization;
deleting a committed value does not resolve a leaked credential.

Evaluate a repository secret scanner during the release's authorized maintenance
pass. Select and verify it before adding a pin or claiming coverage. Keep the
four routine pre-commit categories unchanged; a scanner would use an explicit
on-demand or separately approved CI surface. Scanner negatives never prove no
secrets exist, and a selected scanner is not a substitute for artifact inspection.

## Architecture and house-style comparison

Prior art is pinned to GZKit `04d901b7f594de50f908f66cc1d0ce54210828e8`:
[house-style record](https://github.com/tvproductions/gzkit/blob/04d901b7f594de50f908f66cc1d0ce54210828e8/docs/rnd/house-style.md),
[review](https://github.com/tvproductions/gzkit/blob/04d901b7f594de50f908f66cc1d0ce54210828e8/docs/rnd/house-style/review.md),
[hexagonal specification](https://github.com/tvproductions/gzkit/blob/04d901b7f594de50f908f66cc1d0ce54210828e8/docs/governance/hexagonal-architecture.md),
[review](https://github.com/tvproductions/gzkit/blob/04d901b7f594de50f908f66cc1d0ce54210828e8/docs/rnd/hexagonal-specification/review.md),
[RP-15](https://github.com/tvproductions/gzkit/blob/04d901b7f594de50f908f66cc1d0ce54210828e8/docs/governance/harbor-ro15-project-structure.md),
[RP-7](https://github.com/tvproductions/gzkit/blob/04d901b7f594de50f908f66cc1d0ce54210828e8/docs/governance/harbor-ro7-placement.md).
These distinguish commissioned work, landed structures and actual application
conformance. Do not claim GZKit's target is fully implemented.

| GZKit idea | Starter disposition proposed for approval |
| --- | --- |
| Each fact declared once where its consumer reads it | Adopt the principle; retain genuinely necessary standard metadata mirrors and generated resources under their existing contracts |
| Whole-system architectural responsibilities, rather than one core import test | Adopt; document domain, orchestration, ports, adapters and wiring for the actual system |
| Pure domain; handlers orchestrate effects | Adopt as agent guidance; domain decisions receive values, including time/configuration/randomness; orchestration coordinates external calls |
| Configurator loads once and passes finished dependencies/settings | Adopt as guidance; no DI framework, mandatory bus or kernel dependency |
| Mechanical enforcement plus review judgment and adopter delivery proof | Adapt to existing checks/workflows and warning/override posture; no register or chore lifecycle |
| Python Protocol ports | Prefer where an explicit Python interface earns its place; functions and modules may supply a small application's boundary |
| Frozen Pydantic entities, validating factories, value-return errors, command/query buses | Consider per domain; do not mandate a modeling library, storage model or bus for every adopter |
| Ledger/event model and drydock/work-package semantics | Exclude from this feature; retain Backplane and project ownership |
| Mandatory hexagon structure at every size | Adapt: retain the principles while reducing components and honoring explicit human departures |
| Ruff ALL, complete rule/threshold choices, five-year dependency age | Do not import; existing reviewed starter selections and dependency policy remain authoritative |
| 108 candidates, 13 families and recorded contradictions | Use the complete numbered crosswalk below; do not equate examining a candidate with adopting it |

### Complete candidate disposition crosswalk

Numbers refer to the pinned [November 8 inventory](https://github.com/tvproductions/gzkit/blob/04d901b7f594de50f908f66cc1d0ce54210828e8/docs/rnd/house-style/sources/candidate-inventory-2026-11-08.md).
That inventory is a historical snapshot, not the final decision set. Later
house-style and hexagonal rulings supersede it where explicitly stated. Every
number 1–108 is covered below; dispositions are proposed starter choices, not
adoption of GZKit's decisions or claims about its current runtime.

| Candidates | Proposed disposition and reason |
| --- | --- |
| 1–10 | Adopt responsibility/ownership, plain injection and domain guidance; adapt structural detail to size. Read the earlier no-folder-partition and second-adapter rules against their later reversals; do not preserve stale rules. Separate DDD, architecture, BDD and TDD by the actual change/risk. |
| 11–14 | Retain existing stdlib-first, dependency justification and Pydantic permission. Exclude five-year aging and a GZKit exception register; current dependency-risk and maintenance policy owns evaluation. |
| 15–19 | Prefer explicit validated models and current annotations; allow stdlib types/dataclasses and TypedDict where suitable. No mandatory Pydantic conversion or universal frozen/forbid-extra class policy. Settings schemas have their own explicit unknown-key rule. |
| 20–21 | Preserve unittest and stdlib-first; recommend argparse for a new Python CLI. Preserve existing interface/library choices through explicit review rather than incidental replacement. No extra pytest-ban hook beyond existing routine categories. |
| 22–28 | Reuse existing Astral, selected-family, idiom-review and maintenance requirements. Keep legitimate metadata mirrors; no blanket future-annotation removal without a consumer/semantics review. |
| 29–30 | Keep reviewed starter lint/type selections and evaluate the existing proposed expansion on its own evidence. No imported ALL/preview activation or broad per-directory exemptions. |
| 31–36 | Retain uv_build, locked execution, dependency groups, project-owned tools and minimum-only uv policy. Retain documented requirements exports and isolated installation probes where current verification needs them; no blanket prohibition that breaks those checks. |
| 37–40 | Preserve authoritative audits, immutable actions and version ownership. Review new supply-chain features during authorized maintenance. No new publishing service, package-registry release or runtime/tool pin change from this feature. |
| 41–43 | Reuse src/packaging/workspace and evidence policy. Document app/library applicability. Keep legacy baselines shrinking where they already exist; add neither a registry nor a mandatory deadline mechanism. |
| 44–47 | Preserve reviewed suppressions with reasons and current strict typing; improve boundary errors. Do not require one custom exception per raise or import GZKit-specific suppression syntax without exact tool verification. |
| 48–58 | Adopt clear ownership, context-managed resources, explicit state and safe error boundaries as guidance. Review tool-enforceable rules with the existing selection. No blanket no-lazy-import, docstring-style or extra-keyword-parameter refactor. |
| 59–63 | Preserve existing complexity contracts, on-demand placement, ceilings and cognitive deferral. No imported 50/600/300 line limits, 40% coverage floor or GZKit threshold-table ownership. |
| 64–74 | Adopt platform-conscious paths, UTF-8, temporary cleanup, deliberate executable/environment resolution, argument vectors, CSV newline handling and portable delivered text. Use strict decoding for contractual data; replacement may be appropriate for diagnostic text. Verify platform claims; no blanket replacement-decoding rule. |
| 75–85 | Adapt CLI grammar/help/output/verbosity guidance and stable exit semantics. Preserve actual published command/exit contracts. No mandatory new --json on every existing leaf, GZKit four-code table or seven-obligation lifecycle. |
| 86–90 | Adopt selected runtime settings.json and boundary loading. Keep code-design/tool configuration distinct; machine settings in files/code, explanatory policy in prose. Do not require Rich. Read the early data-only-model statement against the later domain-method decisions; DTOs and domain objects have different jobs. |
| 91–95 | Use actual behavior plus targeted architecture checks. No universal AST-only/no-import policy for tests. Packaging follows the real deliverable; no generic binary build. Adopt actionable warning/recovery explanations; exclude GZKit's operational-mode contract. |
| 96–104 | Preserve meaningful semantic tests, deterministic local unit tests, isolation and truthful mutation/exit outcomes. Keep reached-fault tests for consequential behavior and the risk-based scope policy. Do not import one test per result variant, mandatory labels, fixed per-test/smoke budgets or a new receipt mechanism. |
| 105–108 | Preserve simplicity, bounded edits, behavior-matched docs and generated-resource ownership. Existing project authorities own canonical inputs; do not introduce GZKit rule/skill mirrors. |

The 14 borderline process items stay with existing project/SP/Backplane authority;
their useful configuration, isolation and behavior principles are covered above.
The inventory's 13 contradictions are reasons to consult the subsequent rulings,
not 13 fixes to reproduce in this repository. Examples include the overturned
folder restriction, model-versus-service responsibility, scaffold rule delivery
gaps and tool/dependency configuration drift. No current GZKit conformance claim
is inferred from that historical inventory.

The selected gz-skills 0.13.0 audit at
`0bdab63fc503c6b36e2dd487932689b4e555e41a` has ten meaningful failure classes,
but its broad domain/application grouping and applicability exits do not define
this stronger contract. Portable work belongs upstream: recognize the consuming
project's chosen profile and human departures; assess domain/orchestration
separation, configuration/effect placement, whole-system coverage, wiring and
boundary evidence explicitly. No Python, Pydantic, package layout, error model
or starter policy becomes a universal gz-skills requirement.

Before claiming that an upstream audit verifies these recommendations, evaluate
it with invented good/bad examples: environment reads inside domain logic,
business rules in adapters, hidden concrete construction, external types through
ports, a clean import graph with effectful callbacks, omitted/unmapped code,
and an operator-selected departure. Report what it misses. This is a contribution
design, not authorization to edit or release the companion repository. The
starter can ship honest project-owned review guidance without inventing a local
copy of that skill or claiming an unreleased upstream improvement is available.

The November 14 naming/layout proposal remains a source input, not silently
activated by this design. For 0.11.0, reconcile and publish guidance for all 15
areas, but keep its broader Ruff selection and explicit ty activation patch
deferred. Existing routine selection and four hook categories remain unchanged;
this release does not add its 14-finding remediation or enforce a majority-rule
quota. This scope follows the selected guidance/warning posture, rather than
silently promoting additional recommendations into mandatory tool gates.
Preserve compatibility names and external schemas. The maintainer reaffirmed
the earlier explicit rejection of all paths containing U+0020, including
user-selected paths. Retain that contract across the API and CLI: validate
supplied and resolved paths, including relevant parent/child paths and symlink
targets, before target content access, writes or parent creation. Fail with an
actionable error and leave existing data unchanged. Do not rename or strip spaces
automatically; quoting does not change acceptance. Audit resource/runtime paths
and platform implications during implementation, preserving the original draft's
scope. This is a selected runtime rejection, not a warning-only convention.
No tool patch or path-rejection implementation is applied during design.

## Remaining foundations

These are concrete guidance defaults, with project-specific applicability and
operator departures handled as above. They are not new mandatory services.

| Foundation | Agent guidance and observable evidence |
| --- | --- |
| Errors | Distinguish expected invalid input, unavailable dependencies and unexpected faults; translate at the boundary, preserve useful causes without secret values; test representative failures and partial-effect behavior |
| Logging and diagnostics | Standard-library logging by default; diagnostics on stderr for CLIs, machine results on stdout; explicit levels and redaction, stable event names where consumed; assert output remains parseable under failure/verbosity |
| Paths and files | Separate code, config, mutable data, cache and temporary files; explicit path bases, platform permissions and symlink/overwrite behavior; test relocation, changed working directory and a reached write failure |
| Persistence/recovery | Preserve existing migration/recovery requirements; document transactions, atomic replacement where applicable, concurrent-writer policy and restore verification; test an interrupted/failed operation without losing prior data |
| External calls/subprocesses | Explicit timeout and cancellation, bounded retries only for safe/idempotent operations, deliberate environments, argument vectors and cleanup; fake failures/timeout tests at owning boundaries |
| Input/trust boundaries | Validate type, size, allowed structure and resource use at entry; keep untrusted paths/commands out of unchecked filesystem/shell effects; reached-fault tests for actual consumers rather than speculative attack inventories |
| Data semantics | UTF-8 text, documented aware timestamps/UTC interchange where time exists, explicit units and serialization versions, stable ordering when contractual; examples and round-trip/boundary tests |
| Operation/delivery | Startup validation, graceful shutdown and cleanup, upgrade/rollback and troubleshooting for applicable targets; installed execution outside the checkout and operator-readable recovery instructions |
| Privacy/security response | Minimum necessary data, explicit retention/deletion and telemetry choice, vulnerability-reporting contact and redacted incident handling; invented data only in evidence |
| Interface contracts | Python CLI: help/version, errors/exit codes, output channels and noninteractive behavior. TUI/web/desktop: document their relevant unresolved requirements; do not claim those targets qualified from CLI proof |

## Delivery, migration and verification

Use existing authorities: update the configuration contract, focused engineering
pages, baseline/adoption pointers, generated instructions, ownership/coverage
mapping and the single update skill's migration guidance where relevant. Keep
AGENTS pointers short; distribute depth through linked policies. Regenerate the
six wheel resources when their authoritative inputs change. Do not create a
generic local skill, maintenance framework, policy registry or new helper command.

The starter itself is a consumer: inventory its relevant configuration, process
and filesystem behavior and either apply the approved guidance within scope or
record an operator-selected departure. Do not introduce settings.json for a
helper that has no runtime settings consumer. Adopter review inventories existing
schemas, variable names, path contracts, data and automation, previews changes,
preserves existing working behavior and obtains the actual migration authority.
No adopter or companion edit is incidental to this release.

Implement one small invented, project-owned Python CLI/library reference fixture
with settings.json and isolated unittest examples. Simulate project/user/service/
host launch contexts within that fixture; do not build four new products or claim
native GUI, simulator or real multi-account permission qualification from those
examples. Exercise actual behavior rather than freezing policy wording. The
bounded acceptance matrix is:

1. Precedence including omitted CLI options, missing versus empty environment
   input, scalar/list replacement and configuration-source diagnostics.
2. Invalid/duplicate/unknown keys, unsupported schemas and absent explicit file:
   actionable errors before application effects.
3. Execution from another working directory and an installed artifact without a
   source pyproject; deterministic path resolution, isolation of two selected
   project/user roots, explicit-file selection with no fallback after invalid
   input, and preservation of external settings across code replacement. Exercise
   explicit service/host selection without relying on an interactive home.
4. Secret-like sentinels absent from stdout, stderr, logs, committed examples and
   distribution contents; explicit child forwarding controls.
5. Domain decisions exercised with values and fakes, an adapter failure reaching
   its intended seam, and concrete construction only at the selected boundary.
6. Architecture warning explains the consequence; an explicit human departure
   proceeds, is recorded once and is not repeatedly challenged. Missing evidence
   remains unknown; an accepted departure is not reported as conformance.
7. Applicable existing preservation, API/CLI, metadata/catalog, resource-drift,
   source-independent build and clean installed-artifact checks remain passing.
8. A spaced path supplied through API or CLI is rejected before target content
   access, file changes or parent creation; resolved/symlink/parent paths receive
   the same validation, valid space-free paths work, and input contents containing
   spaces are preserved. Use bounded invented controls and verify no partial write.

Run meaningful owning tests during implementation and the existing full gate
once for the coherent integration candidate. Use managed pinned Python and locked
uv, preserve the four routine hooks and routine CI; changed analyzers also require
their explicit checker tests. Release preparation still requires its authorized
freshness/migration pass and applicable deeper evidence, separately from this
design task. Preserve cognitive DEFERRED / measurement UNKNOWN. Verify the
reference on supported execution platforms before claiming those platforms;
document unavailable platform/embedded-host proof rather than generalizing.

## Completion, decisions and exclusions

Builder review of edition 1, November 16: the independent reviewer identified two consequential
questions. Naming-tool activation was resolved by the explicit guidance-only
scope above, keeping the broader Ruff/ty patch deferred. The spaced-path question
was put to the maintainer and resolved by the actual reaffirmation quoted above.
No important builder question remains unanswered from that review. Edition 2
adds the maintainer-directed universal deployment/configuration concern and the
proposed scope-specific location/selection contract. The same independent reviewer
performed the focused check of that changed scope and returned “Nothing important
left in the changed scope.” Fixture/directory names, documented relative-path
bases and platform-test decomposition remain builder-owned; unavailable native
proof stays explicitly unverified. Design and architectural approval remain
pending. This records the actual scope of each review.

Design acceptance requires a complete source crosswalk, resolved consequential
questions, a finite 0.11.0 release scope, builder review and maintainer approval
of this exact design edition. Dependent implementation additionally requires
separate approval of ADR-0002 edition 2 for runtime configuration ownership and
boundary loading. Reuse ADR-0001 for unchanged component ownership/qualification;
this design does not alter that decision or promise a new combination.

Implementation acceptance requires reconciled policy/instructions/resources,
worked positive/negative behavior, starter internal-use review and recorded
exceptions/unknowns. Missing checks are not passed checks. Publication is outside
this design authorization. Exclude a universal loader/kernel, GZKit lifecycle,
real-adopter migration, companion edits/releases, native activation, full TUI/web/
desktop support and the deferred cognitive engine.

Builder may choose ordinary file/module organization, fixture names and focused
test decomposition within these boundaries. Changes to default behavior, scope,
operator authority or new runtime dependencies return to design review.
