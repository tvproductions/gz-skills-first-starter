---
id: ADR-0002
title: Resolve runtime configuration at the application boundary
revision: 1
state: Draft
decision_date: null
revision_date: 2026-11-16
approved_by: null
approved_revision: null
approval_ref: null
---

# ADR-0002 — Resolve runtime configuration at the application boundary

**Draft edition 1. Separate explicit architectural approval is pending.**
The maintainer's selection of settings.json and approval of general direction
do not approve this identified edition. No dependent implementation is authorized
by this draft.

## Context and scope

The starter's configuration guidance presently presents a pyproject tool namespace
and settings.json as alternative application settings homes. This conflates
development/project-tool settings with deployment/runtime settings and leaves
agents to invent loading and external-access boundaries. Scope is the starter's
guidance to Python applications in both lanes, and its own applicable behavior.
Libraries and applications with no process settings do not need a new loader.

## Proposed decision

Use settings.json as the house default for application runtime configuration.
Keep packaging, dependencies and supported development-tool configuration in
pyproject.toml, with any code-design checker configuration in its legitimate
tool namespace. Keep secret values outside committed configuration.

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

Edition 1 proposed November 16, 2026. Approval: **pending**. Preserve exact reviewed
content and actual approval provenance under the existing ADR policy before
marking this record Current. The actual design-input conversation selected
“settings.json”; it supplied no approval of this ADR edition.
