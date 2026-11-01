# Session handoff — October 24, 2026

Read this entry first, then the
[0.7 tooling handoff](2026-10-24-0.7-latest-tooling.md) and
[acceptance/synchronization record](../evidence/2026-10-24-git-sync.md).
Recheck Git and remote CI before continuing; this is a dated checkpoint.

## Git synchronization and Windows correction — November 1

Fast-forwarded main from `ec0d3c4` to published 0.8.0 commit `e0b752f`.
Its Linux CI passed, but the local Windows gate found discovery identifiers
compared against native backslash paths: repeated configuration rejected its
own update skill for all three hosts. Normalize that identifier to POSIX form
and normalize relative paths in the scope-repair test. A regression exercises
the public configure preview with Windows path semantics on every platform;
it fails before the correction and passes afterwards.

Verification uses uv 0.13.6 and managed Python 3.14.10: locked all-group sync,
all four routine hooks (60 helper tests), bundle/catalog validation,
source-independent build and isolated installed-distribution checks pass.
The unchanged analyzer suite passes all 29 tests. The independent X-Plane
baseline sync and verifier pass on managed Python 3.12.16. The portability
audit reports no findings in the helper and test directories.

This is an unreleased compatible fix; published tags remain unchanged. Native
fresh-session discovery on this Windows checkout remains unverified:
`core.symlinks=false` produces placeholder files for the repository skill links.
Git synchronization and exact-commit CI are verified separately during the push;
no new release acceptance or publication is implied.

## 0.8.0 authorized release — October 31

The maintainer explicitly directed publication; no additional approval is needed.
The reviewed preparation commit is `f176c5e29e61fad0b792d9cd6012f3ab8d95f5c5`,
pushed to main with green CI run 41256392928. Final release metadata and native
development bindings follow in the release commit. The immutable v0.8.0 tag and
GitHub release identify the final SHA; verify them live before further work.

The [release receipt](../evidence/2026-10-31-0.8.0-release.md) supersedes earlier
same-day input observations: uv/uv_build 0.13.6, ty 0.0.95, setup-uv v10.3.3,
gz-skills v0.8.3 in both catalogs, existing Python patches retained. Both locked
baselines, 59 helper tests, 29 analyzer tests, distribution verification,
complexity, dependency audits and documented deeper checks pass within their
stated limits. Cognitive qualification remains under the standing maintainer
exception; complexipy is historical reproduction only. Backplane stays disabled.

Fresh native discovery and canonical skill bytes match the new selections.
Codex's earlier requested-0.8.0/cache-0.8.3 mismatch is resolved by explicitly
selecting published 0.8.3; this does not relabel the earlier failure. Claude's
project-only update resolves 0.8.3. OpenCode uses the required scoped launcher.
User settings/global installations remain unchanged. Desktop picker and other
native-host/embedded-runtime limitations remain explicit. The separate upstream
dependency-skill candidate remains unpublished; no dependent release is implied.

## Three-host local ownership and brownfield repair — October 31 (unreleased 0.8.0)

The final inherited-source test exposed OpenCode 2.2.0's duplicate-ID failure:
its earlier source wins despite a later project pin. Added `run-opencode`, a
scoped native launcher using versioned native environment options, not a host
rewrite. It reconciles ordinary preferences in memory, excludes inherited plugin
declarations/ancestor config, preserves explicit repo skill paths and starts a
private server. It blocks global add/remove and shared-server attachment. The
same fixture now reports the correct project targets active. Use this required
route on 2.2.0; clean-project success alone did not establish brownfield behavior.
User settings and installations remain unchanged. See the receipt's correction.
Final change verification passes: locked all-group sync, four routine hooks with
59 unittests, bundle/both catalogs, source-independent build, installed-wheel
host/repair checks and explicit Ruff C901. uv 0.13.5 and managed Python 3.14.10
were used. Temporary native test servers are stopped. No tag/release or Git
synchronization was performed; the 0.8.0 candidate remains in the worktree.

Latest operator direction: all three target hosts must obey repository-owned
selection, activation and commands. Existing global/user copies may remain;
do not uninstall them or rewrite user defaults to repair a project. The starter
is an emphatic engineering standard: mandatory steps, prescribed commands and
actual evidence; no convenient substitute or configuration-only acceptance.

Implemented `configure --host codex|claude|opencode` with matching native project
settings and update-skill discovery; default remains Codex for compatibility.
Non-Codex adoption records carry additive `host`; old records retain Codex.
Implemented `localize --host` as independent preview/apply scope repair. It reads
inherited Codex/Claude identities, suppresses duplicate sources in repo settings,
repairs Claude's local override layer, and places OpenCode ID exclusions before
its full-SHA package targets. It preserves adoption records, existing project
marketplace selections, adopted component pins and unrelated settings. JSONC
updates preserve comments and source bytes outside changed native fields.
Simultaneous JSON/JSONC files and OpenCode v1 adapter migration need explicit
reconciliation. No native installer is called by the helper.

Template/pyproject/uv lock now identify development 0.8.0, a coherent minor for
this capability/policy bundle. No component/tool/runtime pins were refreshed and
no release/tag is published. Existing earlier policy edits remain in the worktree.
The update skill and wheel resources are reconciled. Starter development now has
Codex, Claude and OpenCode project settings; both repo skill links resolve to the
single canonical update skill. No starter self-adoption lock/profile is created.

Native macOS checks: Codex 0.166.0 discovers 36 starter entries in a trusted
fixture and none outside. Claude 2.1.316 native installs succeed at project scope
for fixtures and this starter; inventory reports enabled inside/disabled outside.
OpenCode 2.2.0's persistent server loads both upstream v2 adapters at exact SHAs,
discovers 15 SP + 20 gz-skills + update skill and none outside. Initial short-lived
OpenCode queries can finish before background package installation; wait for real
server state. User settings snapshots remain unchanged. See the
[three-host receipt](../evidence/2026-10-31-three-host-repo-scope.md).

Codex's gz-skills cache still contains 0.8.3 despite the requested 0.8.0 ref.
Scope proof does not close exact-pin acceptance; that failure remains explicit.
Desktop selectors/model invocation and other operating systems remain UNKNOWN.
The upstream dependency-skill candidate described below remains uncommitted and
unpublished in its separate source checkout. No cache surgery or global install
was used. Full release acceptance, cognitive qualification and Backplane readiness
remain separate from this change's repository/native-scope verification.

## October 31 native development skills and repository scope (unreleased)

The operator clarified the 0.1.0 rationale: the first substantive release is
the first versioned public-contract commitment, without claiming 1.0 stability.
They also supplied a specific Codex CLI 0.166.0 observation: `plugin add`
unconditionally enables a plugin user-wide even from a project with a local
marketplace. Native install/update guidance now prohibits that shortcut and
separates installation, version changes and enablement. Preserve project
activation, user defaults and duplicate-source overrides, and verify actual
revisions and outside-project scope. This clarification uses the operator's
observation; no user-wide install was run to reproduce it here.

Subsequent operator direction makes freshness review completion actionable:
strongly recommend a concrete supported upgrade batch and explicitly offer to
apply it; carry out already-authorized updates without repeating permission.
The internal/adopter instructions, Python policy and maintenance guide bind this
behavior now. The upstream skill correction is prepared in the clean checkout
`/tmp/gz-skills-maintenance-20261031` (base
`9a7970208207d68cc4a04eff7c3d39bcea664463`), with pending skill 0.3.1/bundle
0.8.4 and synchronized metadata/uv lock. Its 28 unittests and source/wheel
builds pass. It is uncommitted/unpublished and is not installed or selected by
this starter's unchanged gz-skills 0.8.0 pin.

The versioning policy and adopter workflow now allow `0.0.0` only as an
unpublished bare-scaffold placeholder. Once original implementation, tests,
documentation or configuration is added, use initial project version `0.1.0`;
do not release that original work as `0.0.0`. Preserve published history.
Claude Code 2.1.316 help confirms `--scope project` for both marketplace-add
and plugin-install; the native guide now gives those exact commands.

Live cache state subsequently changed: the gz-skills installation under the
starter marketplace now resolves to 0.8.3 / Git HEAD
`d6acc26e28ca1c4f43e5bb46d8973021d7d006c3` despite native inventory declaring
the requested 0.8.0 source ref. A scoped native marketplace upgrade reports
already current and does not repair this mismatch. Treat final exact-pin
discovery as UNKNOWN; retain the earlier passing observation as historical.
Do not patch/delete native caches to force agreement. Desktop Computer Use
inspection is blocked by the tool's app-access restriction. User config hash
remains unchanged. See the updated discovery receipt for limits.

The operator explicitly requested native skill use in this starter and requires
repo/project-scoped installation, registration and activation for adopters too.
Do not use global/user-level installation or unscoped install/marketplace-add
commands as a fallback. Shared native download caches are storage, not user-wide
activation. The adopter fragment, native installation guides and starter AGENTS
now make that rule explicit; generated wheel instructions must stay in sync.

Development `.codex/config.toml` selects the published v0.7.1 Git catalog, enables
SP/gz-skills here, suppresses the duplicate gz-skills source and keeps Backplane
disabled. A relative repository skill symlink exposes canonical
`update-gz-template` for explicitly identified adopter work. No self-adoption
lock/profile is created. A fresh macOS CLI 0.166.0 app-server discovers 15 SP,
20 gz-skills and the update skill from both root and `src/`, with no discovery
errors. An independent `/tmp` runtime discovers none of these. User config
remains byte-identical. See the
[native receipt](../evidence/2026-10-31-native-development-skills.md).
Desktop picker/model invocation, Windows symlink checkout and other hosts remain
UNKNOWN; refresh the desktop client and start a fresh project chat to inspect
its native selector. Repository checks and final results are recorded in the
receipt; this work does not publish a release or synchronize Git.

## October 31 direct CLI guidance (unreleased)

The maintainer requires direct `gh` commands for GitHub operations and direct
`git` commands for repository operations, both internally and in adopter
instructions. Routine CLI calls must not be wrapped in Python. Reserve Python
for substantive processing through the prescribed locked, uv-managed environment,
honoring the exact interpreter pin and required uv version. Updated starter
AGENTS.md, the adopter fragment, Python policy and generated wheel-resource copy;
the changelog records this as unreleased guidance.

Verification with uv 0.13.5 and managed Python 3.14.10: locked all-group sync,
all four routine hooks, bundle/catalog validation, source-independent build and
isolated installed-distribution checks passed. No analyzer behavior changed.
Native skill discovery remains separate; this session does not expose SP or
gz-skills, and no plugin configuration or installation was changed.

The operator requested Git synchronization of this guidance. A fresh origin
fetch confirmed `main` and `origin/main` aligned at
`ec0d3c43d4d70445adbb58d03c06adbf076004a2` before committing the six reviewed
files. The required local gate passed again with uv 0.13.5 and managed Python
3.14.10; nested hooks resolve the same uv. Push normally and observe CI for the
final commit, reporting the remote identity and result without another
receipt-only commit. Existing cognitive and host-readiness limitations remain;
this sync does not prepare or publish a release.

## October 26 policy alignment

The operator designated this template as the authoritative shared policy
alignment source for gz-skills and Backplane. The source contract is
`docs/versioning.md#ecosystem-policy-authority-and-consistency`. Both companion
repositories now have local `docs/release-policy.md` bindings and AGENTS pointers:
check this source before release preparation, at scoped policy/tooling maintenance
and when notified of relevant changes; record source identity, applicability,
decisions and approved exceptions. SemVer and the newly written major-release PRD
rule apply prospectively, including independently versioned skill majors.

Backplane owns requirements tracking, labels, backlog/release monitoring,
handoffs and lite/heavy mode definitions. Its local
`docs/superpowers-backplane/modes.md` records this authority and separates intended
scope from implemented readiness. The template references it and retains shared
engineering/release policy, configuration and provenance; it supplies no competing
lifecycle. Keep existing profile values and the setup schema. Companion policy
alignment does not require circular template adoption, synchronized versions or
imposing starter requirements on unrelated consumers.

Reviewed clean starting commits: starter `eef2e858bba709988eb859b17739d2989d8825ab`,
gz-skills `dca86e61bed3aa610555ef30a9ecccf4bd380f2a`, and Backplane
`15b04adbdd01033087d31d8ade6ab98504669e8c`. The source bindings record the starter
base SHA plus hashes of the edited working-tree policy inputs. Reconcile final
committed revisions before claiming published alignment; the new cross-repository
links have been verified against local files, not published remote content.

Validation on Windows with required uv 0.13.5 and managed Python 3.14.9: locked
all-group sync, regenerated wheel-resource instructions, all four routine hooks,
bundle/catalog validation, source-independent build and isolated installed
distribution checks pass. Cross-repository link targets, source hash receipts
and whitespace checks pass. Companion changes are repository documentation only;
no shipped skill tree, runtime pin, plugin installation or native issue changed.
This task does not close the prior deeper-analysis or Backplane readiness gaps.
The operator subsequently requested Git synchronization of all three repositories.
Publish this reviewed source first, then bind the companions to its exact commit
and push their reviewed documentation. Reuse the passing checks for unchanged
inputs and retain normal commit hooks. Verify final remote identities and any
configured CI; report final results without another receipt-only commit. This
does not authorize a tag or release, or complete the deferred acceptance work.

## Current state

Published **v0.7.1** at `27594dbaec853e6bde037b0aaf3f0427a3f053f9` without
waiting for the upstream engine, as explicitly directed. Remote annotated tag
`0562a205f918007aaee53b3dce49d24e30bd3c6f` peels to that commit.
[Both exact-commit CI jobs passed](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/40428666883).
The stable release has four verified asset digests; its downloaded wheel installs
separately, reports 0.7.1 and validates catalogs. The release receipt records
publication details. Earlier preparation/hold statuses below are historical.

Issue #1 is open as **Integrate and qualify the gzkit cognitive engine when
available**, with its milestone cleared and no promised date. Milestone 0.7.1
is closed for the delivered consumer preparation/Ruff patch. Do not reintroduce
an upstream delivery-date hold or claim actual engine qualification. The
following documentation commit records publication/backlog state; verify its
own CI when syncing, without moving the release tag or adding receipt-only loops.

Latest direction supersedes the engine release hold: the maintainer cannot
promise when the gzkit-owned engine will arrive and explicitly directed release
of 0.7.1 without waiting. Ship the prepared consumer checks and Ruff 0.17.3 patch;
retain the cognitive exception. Issue #1 stays open as unscheduled engine
integration, outside the 0.7.1 deadline. No private engine, extraction project,
gzkit mutation or plugin installation is authorized. The candidate-specific
receipt is `docs/evidence/2026-10-26-0.7.1-release.md`; require exact-commit CI,
immutable annotated tag, published stable status and verified assets.
Local release checks pass with managed Python 3.14.10 / 3.12.16, required uv
0.13.5 and Ruff 0.17.3: four routine hooks, 39 adoption tests, all 29 analyzer
regressions, X-Plane probes, C901/Lizard, exact-lock audits and runtime dependency/
import checks. The receipt records limits; real engine scoring remains unperformed.

The operator resumed issue #1, then clarified that the shared cognitive engine
will come from gzkit soon. Consumer preparation for unreleased 0.7.1 now includes
42 fixtures, installed-engine qualification/provenance, independent corpus
inventory and ceiling enforcement. It contains no scorer, private fork or
extraction project. Read `docs/engineering/cognitive-integration.md` and
`docs/evidence/2026-10-26-cognitive-consumer-preparation.md` before continuing.
No engine is installed or qualified; actual corpus scores and eventual
exact-commit CI remain pending. Keep issue #1 open and the 0.7.0 exception in
place until the real upstream candidate is pinned, qualified and measured.
Local preparation passes the complete routine/artifact gate and all 29 explicit
analyzer regressions on managed Python 3.14.10 / uv 0.13.5. The project .venv is
3.14.10; the uv package-manager pin is not a Python 3.13 selector. The lock only
changes the starter version to 0.7.1; dependency pins are preserved. No commit,
push, issue closure, plugin installation or release occurred in this preparation.

Published **v0.7.0** on October 26 at
`a02635dad451f8f89c7801c2cbc02e2ec453d369`; remote annotated tag object
`b13299760c3ccdd33696fcbf13fff6f749397ee0` dereferences to that commit.
[Both exact-commit Linux CI jobs passed](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/40409167397).
GitHub reports a published stable release with all four asset digests matching;
the downloaded wheel installs separately, reports 0.7.0 and validates catalogs.
The user-directed cognitive exception remains explicit in the release notes.

After publication, cognitive qualification was booked as
[issue #1](https://github.com/tvproductions/gz-skills-first-starter/issues/1) in
[milestone 0.7.1](https://github.com/tvproductions/gz-skills-first-starter/milestone/1).
The follow-up documentation commit records that booking/publication proof; it
does not implement cognitive scoring, publish 0.7.1, change code-version metadata
or move the release tag. Observe CI for the final documentation SHA as part of
sync; do not create another receipt-only follow-up. See the release receipt's
publication confirmation for final source/asset identities.

The maintainer subsequently authorized publishing 0.7.0 without waiting for the
cognitive qualification correction, then booking that correction as 0.7.1.
Read `docs/evidence/2026-10-26-0.7.0-release.md` and its JSON companion for the
candidate-specific freshness/acceptance review. Python 3.14.10 and ty 0.0.92 are
now selected; both hygiene groups declare the previously required deeper tools.
Actual deeper checks, reviewed low-severity/static findings and bounded
actual-package mutation samples are recorded without weakening thresholds.
Cognitive acceptance remains explicitly deferred, not passed; gz-skills 0.8.0
is a retained noncurrent selection with owned revisit. Require final exact-SHA
CI, annotated tag, asset digests and published GitHub status before reporting
release completion. Do not publish 0.7.1 or start the cognitive implementation.

Follow-up: the operator selected Dependabot exploration/implementation. Weekly
uv jobs now target `/` and `/baselines/xplane`, with a GitHub Actions job.
The separate dependency-only X-Plane project selects Python 3.12.16 and its own
uv lock; a CI job runs bounded standalone tool probes. No simulator package or
embedded runtime was installed. See `docs/engineering/dependabot.md` and the
dated `docs/evidence/2026-10-26-dependabot.md` receipt for current results.
The operator permits scheduled scans and reviewed update PRs here; adopters
choose starter updates, direct upstream updates or both, and their own timing.
The blanket schedule ban was corrected in AGENTS/current policy; historical
evidence is unchanged. Embedded-host compatibility remains separate from
standalone tests. Auto-merge, publication, plugin installation and dependent-repo
edits remain outside this work.

The operator then invoked `gz-skills:gzs-git-sync` for this complete change.
Pre-sync origin fetch: main and origin/main aligned at
`35ac057`, with only this session's policy, Dependabot and X-Plane baseline work
pending. Required uv 0.13.5 gates and the separate managed Python 3.12.16 probes
pass; the receipt records details. Commit/push this reviewed unit with hooks,
then observe both CI jobs for its exact SHA. Final sync/CI results are reported
after push without creating a CI-receipt-only commit. Hosted Dependabot scan and
real update-PR behavior remain separate proof, not established by CI alone.

Initial save point `a53a5db` reached origin/main. Standard CI passed; X-Plane
failed before sync because required uv 0.13.5's embedded download metadata did
not supply 3.12.16 on the clean Linux runner. The correction pins Astral's newer
official metadata in the X-Plane project's uv settings, preserving exact Python
and uv requirements. All three initial hosted scans completed successfully;
actual update PRs remain unobserved. The receipt records run links, the source
manifest SHA/checksum and the local-project lookup exclusions. Push the corrective
commit normally and verify its own CI; no earlier green job covers that SHA.

At the earlier October 24 session recheck, a fresh origin fetch confirmed main and
origin/main aligned at `731495876ef131c1a0795d38ad69116b77a594ca`, with a clean
worktree and no divergence.
[Exact-commit Ubuntu CI passed](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/40137030752).
This handoff refresh is a subsequent documentation change; verify its containing
commit with Git and its own CI rather than assuming the preceding run covers it.

Latest published release: **v0.7.1**, with the explicit cognitive exception and
retained component/host limitations. Engine integration is open and unscheduled.
No adopter migration or upstream-project change was performed.

## Published-release verification

An adopter reported that 0.6.0 was unpublished. Live GitHub CLI and remote-tag
queries on October 24 confirmed that
[v0.6.0 is published](https://github.com/tvproductions/gz-skills-first-starter/releases/tag/v0.6.0):
`publishedAt` is `2026-10-24T15:35:45Z`, with both draft and prerelease false.
The annotated remote tag object is
`1e33e51cd696eafd90db52d14b89b2f079160336`; its release commit is
`c0a6945b2170e1cf5bee3e80738916f5b62d13a5`. The wheel, source distribution,
portable update-skill ZIP and checksum assets are present. The report conflicts
with the observed canonical release state; the adopter's cause was not diagnosed
and no adopter files were changed. No republication or tag change was needed.

The user then requested handoff and Git synchronization. Scope is this existing
handoff's verification update only; reuse the passing checks for unchanged
code/tool/catalog inputs, run the normal commit hooks with required uv 0.13.5,
push main normally and observe CI for the final SHA. Report that result after
the push without creating another CI-receipt-only commit. Version 0.7.0 remains
unreleased, with the acceptance work below still open.

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
