---
name: adopt-skills-stack
description: Configure or assess a project's Superpowers, Superpowers Backplane, and gz-skills bundle from a reviewed gz-skills-first-starter checkout, preserving existing project authorities and installations.
---

# Adopt the skills stack

This skill guides adoption; it does not replace the three upstream workflows.
Read [the adoption guide](../../docs/adoption.md) for native host loading,
compatibility checks, updates, and rollback. The helper is
[starter.py](../../starter.py); use its CLI help for current options.

For structural adoption in an existing project, read
[backport guidance](../../docs/backport.md). Run the read-only assessment, map
existing sources to proposed targets, and implement only useful, authorized
changes with project verification. Configuration adoption does not move code.

Before choosing versions, use the adoption guide's “Getting current SP and
gz-skills” procedure. Check latest published releases, distinguish development
main from a release, and record reviewed full SHAs. The starter pins are a
baseline, not an instruction to keep SP behind because Backplane is deferred.
Also use its “Maintaining the adopted stack” procedure for the starter template,
SP, SP-BP and gz-skills at adoption and scoped maintenance. Compare recorded
provenance with upstream releases/commits, preserve app additions and overrides,
and record independent adopt/defer decisions. Track SP-BP updates without
enabling it while readiness and explicit adoption remain pending.
Generic maintenance routes to gz-skills `gzs-update-dependencies` for authorized
updates and `gzs-dependency-risk-audit` for risk assessments. Keep the starter's
role to policy and adoption bindings; do not add a competing local maintenance
skill or claim proposed upstream freshness-only reporting is implemented.

Establish the exact target project and a reviewed published starter revision.
Read the starter's [versioning contract](../../docs/versioning.md). Record its
declared template version and exact SHA independently of the app version;
confirm published release/tag identity separately. Legacy unversioned locks
require reviewed reconciliation, never an inferred label or silent rewrite.
Read the [project configuration contract](../../docs/project-configuration.md);
inventory app dependencies, locks and settings, preserve additions and reviewed
overrides, and report freshness/adoption gaps. The helper leaves these files
untouched and does not resolve packages or load application settings.
Inspect project instructions, existing plugins and skill discovery, and gzkit
ownership. Keep app rules and existing user changes. Do not make a copy of an
upstream skill tree or install the same skill through two discovery contracts.

Run `uv run --python 3.14.8 starter.py configure --project <root>` from this starter checkout.
Inspect its preview, then apply the already-authorized adoption with `--apply`.
A conflict requires reconciliation of the specific source or file; do not remove
other installations or use a force overwrite to make it pass. Existing AGENTS
stays untouched: review the generated fragment and add a pointer within scope.
Profile choice is separate; do not infer lite/heavy from the components selected.

Native installation is a separate, explicit operation. Follow only the guide for
the active host; preserve project scope and existing upstream versions. For a
configuration-only request, stop after configuration and identify installation
as pending. OpenCode is deferred until Backplane's upstream adapter is ready.

SP-BP is an expected addition to the target stack and is disabled by default. Preserve existing backlog/handoff practice; do not
install or activate Backplane as part of ordinary adoption. Its future activation
requires an explicit readiness review and configuration change.

Verify actual SP and gz-skills discovery in a fresh session. If Backplane is later
explicitly adopted, also verify its compatibility contract. Record exact sources and PASS/FAIL/UNKNOWN; status/configuration is not
proof of loading. GitHub authentication, a real issue preflight, and any mutation
scenario require the corresponding authorized environment. Do not operate on
production issues just to test installation. Backplane's manifest version does
not prove a published release or cross-harness readiness.
