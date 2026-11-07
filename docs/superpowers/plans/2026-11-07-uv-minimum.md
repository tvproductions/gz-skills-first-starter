# uv Minimum Compatibility Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for this authorized single-task configuration change. Do not create additional agent work.

**Goal:** Accept uv >=0.13.5 in both baselines without forcing CI's tested version on every caller.

**Architecture:** Separate the executable compatibility floor from CI's exact tested selection. Preserve locked package resolution, pinned Python families/patches and native plugin ownership.

**Tech Stack:** uv, TOML, Python 3.14.10 / standalone 3.12.16, four routine hooks.

**Spec:** The maintainer selected minimum-only compatibility in this session; record the decision and alternatives in `docs/evidence/2026-11-07-dependabot-uv-compatibility.md`.

## Global Constraints

- Set `required-version = ">=0.13.5"` in both pyprojects; impose no upper bound.
- Keep CI uv 0.13.6 as a tested reference, not an exclusive runtime requirement.
- Preserve existing roadmap edits, historical diagnosis, package locks and runtime pins.
- Do not publish, push, install plugins or replace Dependabot.

## Review Focus

Below-floor rejection; accepted floor and newer versions; separate Python projects;
nested hook executable provenance; clean provisioning versus already installed managed runtimes.

## Task 1: Reconcile compatibility, policy and evidence

- [x] Use the observed pre-change failures as the negative control; verify the floor and newer uv against both projects after editing.
- [x] Update both manifests, AGENTS, baseline/Python/adopter/configuration guidance, Dependabot guide, roadmap, changelog and handoff. Preserve earlier diagnosis as historical and append the authorized resolution.
- [x] Regenerate authoritative wheel-resource copies. Verify unchanged locks and CI selections.
- [x] Run the full repository gate, explicit X-Plane probes and actual floor/newer compatibility checks. Record versions, limits and hosted verification still pending publication.
- [x] Review the complete intended diff; leave the result uncommitted for the user's next Git-sync request.
