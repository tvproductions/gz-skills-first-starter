# Changelog

## 0.3.3 — Unreleased

- Mandate the GitHub CLI for all GitHub handling in starter guidance and adoption
  workflows. Explicitly route repository access, release checks, issue handling,
  and related GitHub operations through `gh` rather than ad hoc browser or API
  usage in the starter docs.
- Prepare patch 0.3.3 as explicitly requested.

Adopter impact: update local workflows to use `gh` for GitHub interactions,
including repository browsing, release inspection, issue mutation, and any other
GitHub-backed handling described by the starter. Existing non-GitHub project
operations are unchanged.

Verification: documentation-only update; no runtime behavior changed.

## 0.3.2 — Unreleased

- Pin refresh: update Superpowers from v6.4.1 to the latest stable v7.0.0,
  published October 10, 2026, at full SHA
  `bb92a77741419a4ab5f06e711a283343f1ada0c3`. Align the bundle and both native
  catalogs. Retain gz-skills, Backplane and Python/tool pins.
- Correct current SP guidance: Backplane's historical compatibility baseline
  does not constrain active SP while Backplane remains deferred and disabled.
11. Prepare patch 0.3.2 as explicitly requested; no adopter baseline policy changes.

Adopter impact: review SP 7's workflow changes and reconcile the recorded bundle,
catalog source and native installation through the host manager when authorized.
Preserve prior pins for rollback, project instructions and profile choices.
Backplane enablement still requires separate readiness and compatibility review.
No installed plugin cache or other project is changed by this update.

See [the scoped update assessment](docs/evidence/2026-10-11-superpowers-7.0.0.md)
for release/manifest evidence, compatibility limits and Python opportunity decisions.
Fresh-session native loading and SP 7/Backplane compatibility remain unverified.

Verification: 28 unittest tests, bundle/both-catalog validation, Ruff 0.15.18
check/format and offline uv lock consistency passed on actual managed Python
3.14.8. The lock refresh changed only template version metadata; no Python code
or development-tool resolution changed.
