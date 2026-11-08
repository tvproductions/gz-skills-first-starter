---
id: ADR-0001
title: Qualify exact component combinations for starter releases
revision: 1
state: Current
decision_date: 2026-11-08
revision_date: 2026-11-08
approved_by: "project maintainer in this conversation"
approved_revision: 1
approval_ref: "#approval-evidence"
---

# ADR-0001 — Qualify exact component combinations for starter releases

## Scope

The starter's ADR-practice policy distribution and qualification of its selected
SP, gz-skills and SP-BP combination. Component versions/releases remain independent.
This choice does not select future companion release numbers or activate plugins.

## Context

The starter already owns immutable bundle/catalog selections. Mandatory ADR
practice needs a reliable relationship between starter adopter policy, the
portable gz-skills procedure/template and applicable SP-BP integration. A version
label or configured pin alone cannot prove the selected behavior. Each component
has independent ownership, delivery and native availability.

## Alternatives

- Qualify each exact selected combination with source-bound behavioral evidence.
  This fits current catalogs and keeps claims bounded, with an obligation to
  reassess changed combinations.
- Declare compatible component ranges. This permits broader independent upgrades
  but needs a supported compatibility contract and evidence covering the ranges.
  That evidence is not established.

## Decision and rationale

Qualify an exact component combination for each starter release.
The starter owns mandatory adopter policy and concise entry pointers; gz-skills
owns the portable procedure and ADR template; SP-BP owns its planning/tracking
integration. Keep component versions and releases independent. Record the exact
reviewed source revisions and behavioral evidence in existing starter release
evidence. Use existing immutable bundle/catalog pins and project activation
configuration, without a central CLI, runtime or compatibility service.

This makes the qualification claim match the inputs actually examined and
preserves each component owner's design authority. The maintainer's approach
selection preceded the separate explicit approval recorded below.

## Consequences

- Changed combinations require impact review and affected requalification.
  Preserve applicable unchanged evidence only with explicit justification.
- Starter releases depend on immutable companion deliveries and internal-use
  evidence; versions need not match and releases need not be simultaneous.
- Independent adopter updates remain possible, but their resulting combination
  cannot inherit a starter-qualified claim without assessment.
- Expected pins, actual loaded sources and enablement require separate evidence.
  Disabled Backplane remains disabled; its integration evidence does not establish
  combined-stack readiness.
- Detailed companion design remains in its owning repository. The starter must
  link actual contribution records before claiming delivery or propagation.

## Confirmation

Review the bundle, both catalogs, project source/activation and release receipt
for the exact candidate. Exercise the specification's behavioral matrix and
verify internal use in all three publishing repositories before propagation.
Record actual results in release/evaluation evidence, not in this ADR. This
record claims no behavioral qualification has passed.

## Related design

See [the approved specification](../superpowers/specs/2026-11-08-adr-practice-design.md)
and feature #12 / design #13 linked there. Specification and plan approval are
distinct from the architectural approval below.

## Approval evidence

Source: this project maintainer conversation, November 8, 2026. No durable
conversation URL is available. This is an agent transcription of the actual
approval, not an independently generated approval event.

The agent presented ADR-0001-001 separately from the implementation plan and
requested explicit architectural approval of qualifying exact component
combinations while preserving independent ownership, versions and releases.
The maintainer replied verbatim:

> approve plan (explain native execution), and explicityly approve ADR-0001-001

The reviewed proposal's exact bytes are preserved in
[ADR-0001-001-reviewed.txt](approvals/ADR-0001-001-reviewed.txt), SHA-256
`ea36ce63cb1590263cb3b575f75dd78d4bc05f1e4343142b0f5f95c23512688e`.
That hash identifies the reviewed text; the explicit human response supplies
approval. The role above identifies the actual approving user without inventing
a personal identity or external account.

## Administrative capture

November 8, 2026: recorded Current/approval metadata, relocated the working ADR,
repaired related links and changed proposal wording to approved present tense.
Choice, scope, rationale and constraints are unchanged. The separately preserved
reviewed proposal retains its original draft/status wording and content. This
capture does not advance the approved edition, establish behavioral qualification,
authorize publication or approve companion internals.
