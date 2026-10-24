# Session handoff — October 24, 2026

Read this entry first, then the
[0.7 tooling handoff](2026-10-24-0.7-latest-tooling.md) and
[acceptance/synchronization record](../evidence/2026-10-24-git-sync.md).
Recheck Git and remote CI before continuing; this is a dated checkpoint.

## Current state

At preparation, main and origin/main were aligned at
`d752e37865684d444029731a36c0d844746950f7`, with a clean worktree.
[Exact-commit Ubuntu CI passed](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/40135547065).
This handoff and its entry-point links are the subsequent documentation change;
verify their containing commit with Git and its own CI rather than assuming
the preceding run covers it.

Latest published release: **v0.6.0**. Development version: **0.7.0, unreleased**.
The work is pushed, but strict release acceptance is incomplete. No new tag,
release, adopter migration or upstream-project change was performed.

## Decisions to preserve

- Ordinary GZ projects use the stable Python minor one behind the newest
  stable minor (N-1): currently 3.14, with the latest verified patch. Current
  execution pin is 3.14.9. The documented XPPython3 host exception is separate.
- Baseline tools must use the latest verified stable releases across families;
  exact pins ensure reproducibility, not evergreen freshness. Follow the
  dated toolchain receipt rather than assuming installed versions are current.
- Cognitive scoring retains ceiling 15. Complexipy is a defect reproducer,
  not qualified acceptance authority. The user selected gzkit's scoring approach
  and intends a small external GitHub/PyPI project later. That work is deferred:
  **leave gzkit untouched on this machine**, create no extraction project and
  introduce no private starter fork as an incidental continuation.
- Gz-skills maintenance skills were unavailable in this session. Follow the
  documented direct fallback without requiring plugin installation. Availability
  in a catalog does not prove installation or discovery. Backplane stays disabled.
- The user identified weak internal maintenance discipline in dependency projects
  as a concern. This session did not audit or repair those repositories. Providing
  a maintenance skill alone does not prove that a supplying project uses it.

## Verified and unfinished work

The local routine gate passes, including 39 adoption tests. Thirteen analyzer
regressions, C901/Lizard checks, bundle/catalog/resource validation,
source-independent builds and isolated installed-artifact checks also pass.
Cosmic Ray has a bounded synthetic compatibility proof, not a measured mutation
result for this starter's actual production code. CI passes the routine and
artifact gate; it does not run the full deeper-analysis suite.

Open acceptance items must remain explicit:

1. **Known cognitive qualification failure:** complexipy misses keyword-value
   conditionals. The candidate gzkit scorer fixes that fixture but omits
   functions under module-level loops/match. The proposed shared engine is
   neither integrated nor qualified. See the
   [extraction assessment](../evidence/2026-10-24-gzkit-cognitive-extraction.md).
2. **Unperformed deeper analysis:** Interrogate, Vulture, Bandit, branch/statement
   coverage, deptry, pip-audit and applicable Import Linter contracts/results;
   actual-project mutation analysis is also unperformed. Missing results are
   UNKNOWN, not demonstrated code defects. Cohesion is explicitly an adopter-owned
   requirement; do not invent a helper-validation failure from its absence here.
3. **Incomplete effective-configuration proof:** project settings, tool paths and
   Ruff discovery were inspected, but applicable ancestor/user/system configuration
   precedence was not fully verified.
4. **Separate host-readiness gap:** native skill discovery was not verified for
   this checkout/session. Do not equate it with a Python build failure or require
   installing gz-skills here simply to validate the package.

Next release-preparation work should complete the nondeferred applicable analysis,
review findings, close configuration proof and refresh candidate-specific evidence.
Keep the cognitive dependency explicitly deferred until the user resumes it.
Do not describe Git sync as completion of this acceptance work or waive the gates.

## Git sync and future handoffs

AGENTS.md now owns a Git synchronization ritual independent of installed skills:
review scoped changes, use the required uv/interpreter, run applicable checks,
commit with hooks, push normally, verify the final remote SHA and its CI, then
report the worktree and remaining blockers. Keep sync, acceptance and publication
separate. No plugin, dependency-repository change or release is incidental to sync.

Handoffs are ordinary dated files in `docs/handoffs/`; AGENTS.md and README link
to the current entry. There is no automated handoff manager or enforced schema.
Keep material decisions, observed checks and unfinished work here, with links to
evidence; inspect live state on resume. Do not create repeated commits merely to
record CI for each preceding documentation-only receipt commit.
