---
id: ADR-0002
title: Resolve runtime configuration at the application boundary
revision: 2
state: Current
decision_date: 2026-11-17
revision_date: 2026-11-16
approved_by: "project maintainer in this conversation"
approved_revision: 2
approval_ref: "#approval-evidence"
---

# ADR-0002 — Resolve runtime configuration at the application boundary

**Current edition 2. Explicit architectural approval recorded November 17, 2026.**
The reviewed draft bytes and actual approval context are preserved below.

## Context and scope

The starter's configuration guidance presently presents a pyproject tool namespace
and settings.json as alternative application settings homes. This conflates
development/project-tool settings with deployment/runtime settings and leaves
agents to invent loading and external-access boundaries. Scope is the starter's
guidance to Python adopters in both lanes, and its own applicable behavior.
Every adopter has a deployment/configuration concern, including libraries and
hosted plugins. The contract identifies the actual configuring consumer; this
does not require a library to introduce independent global settings discovery.

## Decision

Use settings.json as the house default for application runtime configuration.
Keep packaging, dependencies and supported development-tool configuration in
pyproject.toml, with any code-design checker configuration in its legitimate
tool namespace. Keep secret values outside committed configuration.

Every adopter identifies its deployment unit, configuration owner/scope, selected
location, precedence, permissions, startup/reload and upgrade responsibilities.
Use one selected settings file under the application's documented configuration
root, outside installed code by default. Select an explicit launch/API path first,
then a documented application config-path variable, then the declared default for
that deployment scope. Do not merge scopes or fall back after an invalid explicit
selection. Project, per-user, service, host and explicitly portable deployments
have different roots; no directory is universal. Libraries receive configuration
through their consumers. A portable install may co-locate code and settings only
through its explicit preservation contract. All selected paths honor the
maintainer-reaffirmed rejection of spaces, with explicit alternate roots when a
normal OS path is incompatible.

An application configuration adapter resolves defaults, a selected settings file
and documented environment/explicit overrides once at startup, validates the
result and supplies settings as values to consumers. One outer configurator wires
concrete dependencies; domain logic reads no files, environment, clock or other
hidden process inputs for itself. No shared runtime loader, kernel, model library,
DI framework or mandatory package layout is introduced.

These are strong agent defaults. Agents surface consequential departures and
respect an explicit informed human override, recorded in existing project
authority. Project-specific decisions can adopt stricter requirements. Existing
approved decisions and mandatory engineering gates retain their own authority;
an override is not permission to misreport runtime errors or bypass failed checks.

## Alternatives

- Keep arbitrary runtime settings under a pyproject tool table. Useful for
  project-local tools, but requires an explicit runtime deployment/discovery
  contract and can couple an installed application to a source checkout.
- Leave every runtime format and loading boundary unspecified. Preserves latitude
  but does not supply the consistent guidance requested by the maintainer.
- Ship a common loader/kernel and compulsory architecture gates. Adds a runtime
  dependency and enforcement owner that the selected guidance approach does not
  require.

## Consequences and confirmation

Existing adopter formats require reviewed migration or an operator-selected
departure, not overwrite. JSON needs explicit validation and documented values;
it has no comments or built-in merge/override semantics. Small applications may
use functions/modules for the boundary; libraries can receive explicit arguments.

Confirm with worked precedence, invalid-input, redaction, isolated environment,
relocation and installed-execution examples, plus an architecture-warning and
human-override example. These observations belong in implementation evidence,
not invented approval fields. Related design:
[application foundations](../superpowers/specs/2026-11-16-application-foundations-design.md).

## Approval and edition history

Edition 1 was proposed November 16, 2026 and is preserved in commit `ed2417d`.
Edition 2, also November 16, adds the universal deployment/configuration concern
and scope-specific location/selection contract following the maintainer's
clarification. Edition 1 remains historical; edition 2 was separately approved
November 17. The original design-input conversation selected
“settings.json” and “we'll always have some deployment/config aspect with any
adopter”; that earlier input did not itself approve this ADR edition.

## Approval evidence

Source: the main project maintainer conversation, November 17, 2026. This is
an agent transcription; no durable conversation URL is available. After the
agent presented the refined plan and separately requested approval of the
identified ADR edition, the maintainer replied verbatim:

> approve ADR-0002 edition 2

The exact reviewed draft is preserved in
[ADR-0002-002-reviewed.txt](approvals/ADR-0002-002-reviewed.txt), SHA-256
`94b414de72d191ab9d3cd7c7fcc968e6beb708eeb93e9d24fea09d341212758b`.
The hash identifies content; the actual human response establishes approval.

## Administrative capture

November 17: preserved the reviewed draft, recorded Current/approval metadata
and replaced pending/proposal status wording. Decision, scope and constraints
are unchanged. This administrative capture does not advance the edition or
establish implementation acceptance, host qualification or release authority.
