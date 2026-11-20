---
id: ADR-0004
title: Own Python command discipline in starter development tooling and native host adapters
revision: 1
state:
decision_date:
revision_date: 2026-11-19
approved_by:
approved_revision:
approval_ref:
---

# Python command control — proposal, edition 1

**Withdrawn November 19, 2026. Historical proposal; do not implement or seek
approval of it.** During review, the maintainer identified the enforcement
subsystem as inconsistent with the starter's lightweight role and accepted the
recommendation to withdraw it with “proceed as recommended.” This is an agent
transcription of this conversation; no durable conversation URL is available.
The proposal was never approved or Current, so this is not retirement of an
accepted decision. The original proposal text below is retained unchanged;
its pre-withdrawal SHA-256 is
`ddcccb9922ee69c6f000df8352aaddcea138ca0f6c5da80378ea4b49933e8fe7`.

**Unapproved proposal. No command-control implementation or activation is authorized
by this document.** The maintainer asked to address the implementation corrections
identified by the discipline evaluation. Routine corrections proceeded separately;
this proposed operational boundary needs identified-edition architectural approval.

## Scope and context

The [Python policy](../../engineering/python.md) already requires
`uv run --locked python`. The [evaluation](../../evidence/2026-11-19-discipline-evaluation-results.md)
observes repeated bare Python commands after that rule was available. Its
[correction follow-up](../../evidence/2026-11-19-discipline-corrections.md)
closes the sampled adopter link and declared-verification defects, but neither
provides Python command enforcement. Repeating the instruction is not a proved fix.

ADR-0001 edition 1 preserves independent component ownership and exact-source
qualification. It does not approve a command-control implementation. This proposal
keeps strong Python preferences in the starter; no SP/gz-skills changes follow.
Draft ADR-0003's bootstrap verifier remains independently unapproved; this proposal
does not implement or approve it.

## Alternatives

1. Keep instructions and retrospective command review. This has no added runtime
   dependency or native integration, but detects violations after execution.
2. Use native command-name deny patterns. They can reject common forms with little
   code. Path variants and shell forms need separate handling; the observed rule
   checker and vendor documentation do not establish complete coverage.
3. Add one starter-owned command classifier with small native pre-tool adapters.
   This can reject prohibited submitted forms before execution and keep policy
   identical across adapters. It adds a development dependency, host qualification,
   parser limits and possible false denials. Host failures can limit enforcement.

## Proposed decision and design boundary

Choose alternative 3, conditional on the confirmation gates below. Own the shared
classifier in the installed starter development tooling, exposed as
`gz-starter command-policy --host codex|claude`. Adopters must explicitly add and
lock a released starter development dependency before selecting this integration.
No application runtime dependency, copied upstream skill, generic orchestrator,
approval ledger or user-wide hook is introduced. Keep the base helper's
standard-library contract; do not add a shell-parser dependency without review.

Project-scoped synchronous `PreToolUse` adapters consume the actual tool request
and return the host's supported denial response. Start with the qualified local
Codex and Claude CLI versions only. Do not infer OpenCode, Work cloud, embedded,
Windows or Linux support. Preserve existing native settings and hooks; preview
and review configuration changes before applying them. Leave the four routine
pre-commit categories unchanged.

The classifier must:

- Permit the prescribed `uv run --locked python` form in the owning project,
  including reviewed uv options that preserve its interpreter and lock contract.
- Reject directly submitted bare, versioned, relative-path and absolute-path
  Python executables, including launcher forms, before their effects occur.
- Inspect statically understood compound commands and supported wrappers. Reject
  ambiguous dynamic executable selection or unsupported shell syntax rather than
  guessing it contains no prohibited invocation. Document the accepted grammar.
- Explain the rejected form and the canonical invocation. Do not silently rewrite
  commands, relax permissions, alter locks or substitute another interpreter.
- Launch the classifier itself through the pinned locked environment from the
  owning root. No bare Python bootstrap exception is implied.

This checks submitted tool commands; it does not police every subprocess of
arbitrary application code or establish a security boundary against a hostile
actor. Interactive stdin, alternate code-running tools and host hook failures
must have explicit coverage/dispositions. Do not market a partial guard as
complete execution enforcement.

## Consequences, uncertainty and release scope

Ambiguous shell constructs may require agents to submit simpler separate calls.
Tool requests are processed locally; public evidence must redact private command
data. The installed command's input/output and exit-status contract must be
versioned and tested at its public seam.

Native coverage and failure behavior are consequential unknowns. In particular,
the [Codex hook documentation](https://learn.chatgpt.com/docs/hooks) describes
unsupported paths and responses that can leave execution continuing. A configured
hook therefore supplies no fail-closed guarantee. If an acceptance negative can
execute, do not activate or close this correction; report the unsupported boundary
and return for a revised architectural choice. Approval does not authorize a
fallback execution broker or global policy installation.

This proposed supported development interface is minor scope: published 0.11.3
would advance to the already proposed 0.12.0 target after selection and scope
reconciliation. It is excluded from the selected 0.11.4 duplicate-source patch.
Current mirrors remain 0.11.4. No PRD or major release is selected. No dependent
repository changes, installation, Git sync, tag or publication is implied.

## Confirmation before activation or acceptance

Prove native delivery and actual effects in fresh sessions for each claimed host:

1. Canonical Python, lint/type/unittest and normal direct Git commands proceed
   with their real statuses; nested workspace use resolves the correct root.
2. Bare/versioned Python, direct relative/absolute executables, wrappers, static
   compounds and dynamic selection are blocked before a fixture sentinel writes.
3. Malformed input/output, missing executable, crash, timeout and disabled or
   missing hook cannot become an accepted enforced session. Record actual native
   behavior; do not infer a denial from a hook log or configuration.
4. Interactive stdin and every available alternate execution tool have a tested
   disposition. An uncovered executable path prevents a complete-control claim.
5. Existing adopter authorities/settings/hooks are preserved. Installed-artifact
   checks pass independently of the source checkout. Repeat the original affected
   ADR, maintenance and adopter tasks without reminding actors of the rule.

Implement only after separate approval of this edition and review of the bounded
execution plan. Keep original failures; later passes qualify only their inputs.

## Approval evidence and edition history

Edition 1, November 19, 2026: agent proposal prepared during correction follow-up.
Human architectural approval has not been obtained. Preserve the reviewed bytes
and actual explicit response before administrative approval capture. Blank state
and approval fields confer no authority.
