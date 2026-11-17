# Python application foundations

Apply in both adopter lanes under [ADR-0002 edition 2](../decisions/ADR-0002-002-runtime-configuration-boundary.md)
and the [configuration contract](../project-configuration.md). These are strong
agent defaults with actionable warnings and informed human departures. Existing
mandatory engineering requirements and approved decisions keep their authority;
the explicit no-spaces input rule rejects invalid paths at runtime. An override
does not turn an operation failure or missing evidence into success.

## Classify the actual product and deployment

Record uv application/library role, packaging, repository/workspace organization,
interface and deployment/configuration scope separately. Applications include
scripts, CLIs and web servers; a missing scripts entry does not imply a library.
Keep the starter's packaged-src/uv_build baseline even though uv permits other
forms. Python-only support does not certify a non-Python frontend or extension
backend. Identify installation/config/data/cache/temp ownership and permissions.
Every adopter MUST identify its configuring operator or host/consumer, including
an empty operator-settings surface when applicable. A library receives explicit
values instead of discovering global settings; a plugin follows host startup.
Portable means a documented relocation/preservation contract, not simply an
application folder or transferable container.

Official classification and OS-location sources and their November 16 review
dates are preserved in the [approved design](../superpowers/specs/2026-11-16-application-foundations-design.md#astral-project-model-application-interface-and-deployment).
The [naming/layout guidance](naming-and-layout.md) covers all 15 related topics.

## Right-sized architecture and whole-system coverage

Keep domain decisions pure: receive values for configuration, time, randomness
and external results. Application handlers coordinate effects; ports express
needed behavior; adapters translate external types and failures. One outer
configurator selects concrete implementations at initialization. A small product
may use functions/modules instead of classes, buses, containers or a kernel.
Use Protocol only when an explicit interface earns its place. Models may be
stdlib types, dataclasses or justified dependencies; no universal Pydantic model,
error-return style or package-layer count is required.

Map actual source to responsibilities, including commands, callbacks, plugins,
scripts and startup code. Inspect configuration/effect placement, dependency
construction, external types crossing ports and business rules in adapters.
A clean import graph alone misses effectful callbacks and omitted modules.
Use behavior tests at real consumers with fakes; optional architectural checks
warn by default unless a project explicitly promotes them to a gate.

The complete disposition of GZKit's 108 candidates is in the approved design.
Reuse the selected gz-skills audit as a general coupling audit, without claiming
that it verifies this stronger contract. Before claiming stronger coverage,
exercise good/bad examples for hidden environment reads, adapter business rules,
concrete construction, external port types, effectful callbacks, omitted code and
accepted departures. Portable improvements remain upstream-owned. Do not import
GZKit's ledger, kernel, lifecycle, blanket tool selections or numeric rules.

## Warnings and informed departures

At design/review, name the boundary, consequence, alternative and next action.
For example: “Domain rendering reads EXAMPLE_FOUNDATIONS_MESSAGE directly.
Tests and library callers can then receive process-dependent results. Resolve
it at startup and pass message as a value.” Record an informed operator choice
once in the existing design, instructions or applicable ADR and continue within
that scope. Revisit only for materially changed inputs/evidence. Do not add a
warning registry, recurring challenge or runtime approval prompt.

Worked review, invented: an operator accepts one combined startup/orchestration
module for a small CLI instead of separate layer packages. Record “combined
module selected; initialization owns effects; domain functions still receive
values.” A later review reuses that choice without another challenge. If the
operator also accepts hidden domain input, record the concrete departure rather
than reporting pure-domain conformance. No actual adopter exception is granted
by this invented example; changing an approved architectural decision still
requires the ADR procedure.

## Secrets, environment and trust

Resolve credential references or injected values at the boundary. Use an existing
OS/service facility or CI secret injection suitable for the deployment; select
no universal backend. Keep real values out of settings, URLs, arguments, logs,
errors, evidence and artifacts. Environment injection is an input mechanism,
not inherently confidential storage. Forward only explicitly selected variables
to child processes. No implicit dotenv loading; an explicitly selected local
dotenv file is plaintext and needs documented syntax/precedence. Commit examples
with placeholders and review ignore/artifact exclusions without hiding unrelated
files. Document least privilege, separate environment identities, credential
rotation/revocation and incident ownership where applicable.

Validate input type, size, structure and resource bounds before effects. Do not
turn untrusted paths or commands into unchecked filesystem/shell actions. Keep
diagnostics actionable without echoing rejected sensitive values. On suspected
exposure, stop further disclosure, revoke/rotate and identify affected locations
with redacted evidence; removing a value is not revocation. External response or
history rewriting requires its actual authority. The starter selects
detect-secrets 1.5.0 in root hygiene for explicit repository scans, outside the
four routine hook categories. Use relative paths from the reviewed repository
root, include intended tracked/new sources, disable network verification when
reviewing possible credentials, and qualify positive/negative canaries. Triage
every finding; a negative scan cannot prove absence of secrets. This does not
impose a new adopter scanner or qualify external trees. See the 0.11.0 receipt.

## Errors, logging and interfaces

Distinguish expected invalid input, unavailable dependencies and unexpected
faults. Translate at the boundary and preserve useful causes internally without
printing secret-bearing exceptions. Standard-library logging is the default;
use explicit levels, redaction and stable event names where consumed.
For CLIs, stdout carries machine results and stderr diagnostics; test JSON
parseability under verbosity/failure, help/version, exits and noninteractive use.
Preserve existing published commands/exits. TUI/web/desktop requirements need
their own interaction, lifecycle, authentication, accessibility and platform
evidence; CLI proof does not qualify them.

## Files, persistence and recovery

Resolve declared path bases once and keep code/config/data/cache/temp distinct.
Reject supplied and resolved U+0020 paths, parents and symlink targets before
content access or creation, with no partial writes; preserve text containing
spaces. Document symlink/overwrite and permission behavior. Use context managers
and cleanup; choose transactions or atomic replacement where appropriate.
Document migrations, concurrent-writer behavior, backup/restore and interrupted
operation recovery. Exercise a reached failure that preserves prior data rather
than claiming recovery from a happy-path write.

For the reference fixture, output uses a temporary sibling and replace; existing
parents are required, failed replacement preserves prior bytes, and concurrent
writes are last successful replacement wins. This is bounded single-file output,
not database transactions or a power-loss durability guarantee.

## External calls, semantics and operations

For actual external consumers, choose explicit timeouts/cancellation, bounded
retries only for safe/idempotent work, argument vectors, deliberate executable/
environment resolution and cleanup. Exercise failures/timeouts at the owning
adapter. Do not add a network client or subprocess solely to illustrate guidance.
Use UTF-8 contractual text, documented units, aware timestamps/UTC interchange
where time exists, schema versions and contractual ordering. Test round trips
and boundary values; diagnostic replacement decoding is separate from strict
contractual decoding.

Validate at startup; document shutdown, cleanup, configuration ownership,
upgrade/rollback and troubleshooting for the actual delivered target. Prove
installed execution outside the source checkout and settings preservation during
code replacement. Minimize retained personal data; document retention/deletion,
telemetry choice and a vulnerability-reporting contact appropriate to the product.
Use invented data in tests and evidence. Missing host/native evidence is UNKNOWN.

## Starter internal use and evidence ownership

The starter is a configuration/adoption CLI, with no application runtime settings
consumer; it therefore adds no unused settings.json. bundle/catalogs and packaged
resources are immutable desired composition; adopter files and inherited native
settings have their existing schemas. cli.py owns preview, validation, provenance,
configuration orchestration and writes; native modules own host translation,
scope and launch; paths.py owns path validation. These functions form a small
boundary, not a claim that the mixed CLI module is a universal domain layer.
No business-domain model, database or external service is introduced.

Retain exclusive-create/rollback behavior and its reached-fault tests; preserve
native user settings and disabled Backplane. Inventory relevant resource,
inherited-config and managed paths before effects. run-opencode intentionally
forwards the launching operator's environment because native providers/plugins
may consume their own authentication and startup inputs; the helper overrides
its selected project configuration variables. This preserves the inherited
interactive-host interface, not sensitive-variable isolation or a general
application-child default. Operators must remove unrelated sensitive inputs
before launching that host. Narrower forwarding requires host/provider evidence;
do not silently strip unknown credentials or claim third-party qualification.
The interactive process has operator-controlled lifetime/cancellation rather
than an automatic short timeout. Do not scan unrelated paths.

The [reference fixture](../../examples/application_foundations/README.md) and
owning unittest/installed-artifact checks demonstrate bounded settings precedence,
isolation, redaction, pure rendering, injected failure, relocation and preservation.
The starter's existing tests own its public adoption/host/preservation behavior.
Both lanes must supply equivalent evidence for their actual consumer; configuration
alone never establishes acceptance. Keep platform and cognitive DEFERRED /
measurement UNKNOWN limits explicit in the existing evidence, not a new registry.
