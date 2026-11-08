# Dependabot uv compatibility diagnosis — November 7, 2026

Initial diagnosis below is historical; the authorized minimum-only resolution
later in this record supersedes its exact-pin blocker and updater alternatives.
Fresh hosted verification remains pending the default-branch change.

Initial status: demonstrated upstream execution constraint; hosted repair blocked.
The operator authorized resolving the failures. Do not report this diagnosis or
passing local checks as successful hosted scanning. Preserve exact uv 0.13.6,
standard Python 3.14.10 and separate X-Plane Python 3.12.16 selections.

## Failure and causal boundary

The November 2 [standard job](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/41469195255)
and [X-Plane job](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/41469179882)
report `tool_version_not_supported`: detected requirement `==0.13.6`, running
updater version 0.13.5. Both manifests require exactly 0.13.6. The updater's uv
process rejects that mismatch before lock generation; this is not a dependency
resolution or Python-family failure. The separate
[Actions scan](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/41469217136)
succeeded.

Reviewed upstream source commit:
`05146d8f2a50ea4adf6e00a197c85afae99f7051`, committed November 7, 2026.
Its [uv Dockerfile](https://github.com/dependabot/dependabot-core/blob/05146d8f2a50ea4adf6e00a197c85afae99f7051/uv/Dockerfile)
selects uv 0.13.7. This is upstream source evidence, not evidence of which image
GitHub currently deploys. A newer binary still cannot satisfy an exact 0.13.6
requirement. The [lock updater](https://github.com/dependabot/dependabot-core/blob/05146d8f2a50ea4adf6e00a197c85afae99f7051/uv/lib/dependabot/uv/file_updater/lock_file_updater.rb)
uses preinstalled uv; its [error handler](https://github.com/dependabot/dependabot-core/blob/05146d8f2a50ea4adf6e00a197c85afae99f7051/uv/lib/dependabot/uv/file_updater/lock_file_error_handler.rb)
translates uv's required-version mismatch into the observed error.

GitHub's [documented Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference)
provide no uv executable/version override. The open
[upstream version-field request](https://github.com/dependabot/dependabot-core/issues/14376)
concerns updating the constraint; it does not establish exact-version runtime
selection. Relaxing/removing the requirement or using an older tool would
contradict this repository's exact-execution policy.

## Reproduction and controls

Read-only commands run from the starter checkout, for each baseline `.` and
`baselines/xplane`:

```bash
uv tool run --from uv==0.13.5 uv lock --check --project BASELINE
uv tool run --from uv==0.13.7 uv lock --check --project BASELINE
```

All four probes exit 2 with the expected required-version mismatch. The temporary
tool runs populate normal uv download/tool caches; they do not replace the
project environment, change pins or install native plugins.

Controls using required uv 0.13.6:

```bash
uv lock --check
uv lock --check --project baselines/xplane
```

Both exit zero (75 and 76 packages respectively). Manifests and locks are unchanged.
These controls isolate the uv version check; they do not emulate hosted scanning
or prove a full updater run.

Attempts to retry both failed jobs using `gh run rerun RUN_ID` were rejected:
`This workflow run cannot be retried`. No new run was created. The current hosted
image and a fresh hosted result remain unverified. Docker and Dependabot CLI are
not installed on this machine; no installation or custom image was attempted.

## Resolution boundary

A durable automated path must select each repository-required uv binary rather
than follow the hosted updater's bundled version. A controlled existing updater
is a design option, subject to verification of exact-version selection, separate
baseline resolution, review-only PRs, source provenance and applicable CI. It is
not implemented or enabled by this diagnosis. Keep generic dependency workflow
ownership in gz-skills; add no competing local maintenance skill or reporter.

The maintainer must choose a controlled updater design or retain hosted scans
with an explicit upstream blocker. Do not silently change the automation service,
weaken exact pins, suppress failures, disable scans or claim the problem resolved.
No issue, PR, tag, release or user-wide installation was created by this work.

## Documentation verification

With required uv 0.13.6 and managed Python 3.14.10, locked all-group sync, all
four routine hooks, bundle/catalog validation, source-independent build and
isolated installed-distribution verification pass. All 42 local Markdown link
targets across the five changed documents exist; `git diff --check` passes.
Analyzer code and authoritative wheel-resource inputs are unchanged, so analyzer
regressions and resource regeneration are inapplicable. These results verify the
documentation/package change, not resolution of the hosted updater failure.

## Authorized minimum-only resolution

The maintainer rejected exact uv matching as a repeated impediment and explicitly
chose a minimum-only requirement. Alternatives discussed were a bounded
`>=0.13.5,<0.14` range and an unbounded `>=0.13.5` minimum; the latter was selected
to avoid version-only blockers at minor-family boundaries. Replacing Dependabot
is unnecessary for this causal failure class.

Set both projects to `required-version = ">=0.13.5"`. Keep CI on tested uv
0.13.6 without requiring supported local or hosted executables to match it.
Record actual provenance and behavioral verification. Preserve exact Python
patches, dependency locks and uv_build 0.13.6. This is a prospective adopter
policy change for the next minor release, not a tool upgrade or release.
Astral documents PEP 440 constraints for
[required-version](https://docs.astral.sh/uv/reference/settings/#required-version).

The old exact-pin failures above are the negative control. Before changing the
checkout, a disposable snapshot with a bounded candidate passed lock checks
under uv 0.13.5, 0.13.6 and 0.13.7 in both projects, and all-group sync plus
X-Plane probes under 0.13.5 and 0.13.7. Both exact managed Python versions were
already available in the machine's uv store; this is not clean cold-download
proof for older uv metadata. Admission of later uv releases is a deliberate
policy choice, not a claim of having tested every future version.

Regenerated packaged adopter instructions. Final minimum-only checkout results:

| uv | Standard project | Independent X-Plane project |
| --- | --- | --- |
| 0.13.5 | Lock check, all-group sync, all four hooks, catalogs, source-independent build and installed-artifact verification pass | Lock check, all-group sync and standalone probes pass on managed 3.12.16 |
| 0.13.6 | Same full repository gate passes on managed 3.14.10; actual nested uv path/version recorded | Lock check passes |
| 0.13.7 | Lock check and all-group sync pass | Lock check, all-group sync and standalone probes pass |

Below-floor uv 0.13.4 is rejected with exit 2 and the expected `>=0.13.5`
requirement message in both projects. The pre-change 0.13.5/0.13.7 rejection and post-change
acceptance isolate the configuration fix. Commands use `uv tool run --from
uv==VERSION uv ...` to exercise actual binaries; `uv run` provenance confirms
nested commands resolve each selected uv. Exact locks, CI selections and
interpreter pins remain unchanged. No analyzer implementation changed, so its
separate regressions are inapplicable. Both managed Python patches were already
provisioned; cold provisioning under the older uv remains outside this proof.

Independent review reports no substantive findings in the configuration/policy
change. Final verification matrix and completed plan resolve its documentation
follow-up. Resource-copy and local Markdown-target checks pass; unchanged locks,
Python pins and CI/scan configuration are verified with Git diff.

Do not call hosted scanning repaired until observing fresh jobs on the final
default-branch inputs. No push or scan-service replacement is implied.

## Authorized synchronization and hosted scan request

The maintainer subsequently authorized commit/push, exact-commit CI, fresh
Dependabot checks and review of generated PRs. Commit
`f0f5428c3f9146c4caaab209822b1f5d5fd57daa` reached origin/main with a clean,
aligned worktree. Both [exact-commit CI jobs passed](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/42391923946).
Normal commit hooks and the complete local gate passed using uv 0.13.6.

Hosted scan requests cannot use retry of the old runs. Public GraphQL mutation
discovery exposes no Dependabot update trigger. Browser access is unavailable;
native Chrome and Safari control each timed out. No fresh scan was established
by those attempts.

Add the actual uv minimum/CI distinction as a comment in `.github/dependabot.yml`
and push that configuration-file update to request processing through Git.
Preserve the parsed configuration, weekly schedules, independent projects and
PR limits. GitHub documents checks on configuration-file check-in in its
[version-update guide](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates),
and a configuration update as a trigger in its
[server release notes](https://docs.github.com/en/enterprise-server%403.21/admin/release-notes).
This is a bounded fallback attempt, not proof of a new hosted job. Observe new
job identities and actual manifests/results before accepting the fix; do not
keep making configuration edits if it does not enqueue jobs.

## Hosted verification completed — November 7

The configuration-comment update at
`e918dbbd02353258b697de5f63739a2431d65327` triggered all three fresh jobs.
Both [repository CI jobs](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/42392131270)
passed for that exact SHA. The parsed Dependabot configuration, schedules and
limits are unchanged; the update adds only the actual uv compatibility note.

| Scan | Result | Hosted evidence |
| --- | --- | --- |
| Standard Python | SUCCESS | [run 42392138777](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/42392138777) |
| X-Plane/XPPython3 | SUCCESS | [run 42392138808](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/42392138808) |
| GitHub Actions | SUCCESS | [run 42392138759](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/42392138759) |

Both Python logs report actual uv 0.13.7 on Linux and complete without
`tool_version_not_supported`. Their structured results report dependency-update
requests; the actual open PR inventory is ten PRs, five per Python job. Do not
confuse all update requests in the logs with accepted/open GitHub PRs.

Inspected all ten PRs' changed-file scopes and package/version diffs. At the
recorded head SHAs, all reported `checks` and `xplane-baseline` CI checks passed.
The [PR inventory](2026-11-07-dependabot-prs.json) preserves exact heads, file
lists and CI links. Baseline Python/uv requirements and activation scope remain
intact; changes are confined to each project's own manifest/lock.

| PR | Baseline | Proposed update |
| --- | --- | --- |
| [#2](https://github.com/tvproductions/gz-skills-first-starter/pull/2) | Standard | complexipy 8.1.0 → 8.3.0 |
| [#3](https://github.com/tvproductions/gz-skills-first-starter/pull/3) | X-Plane | virtualenv 21.14.13 → 21.15.5 |
| [#4](https://github.com/tvproductions/gz-skills-first-starter/pull/4) | Standard | pip 26.2.2 → 26.3 |
| [#5](https://github.com/tvproductions/gz-skills-first-starter/pull/5) | X-Plane | coverage 7.17.0 → 7.17.1 |
| [#6](https://github.com/tvproductions/gz-skills-first-starter/pull/6) | X-Plane | complexipy 8.2.0 → 8.3.0 |
| [#7](https://github.com/tvproductions/gz-skills-first-starter/pull/7) | Standard | python-discovery 1.6.4 → 1.9.4 |
| [#8](https://github.com/tvproductions/gz-skills-first-starter/pull/8) | Standard | Lizard 1.24.3 → 1.25.0 |
| [#9](https://github.com/tvproductions/gz-skills-first-starter/pull/9) | X-Plane | SQLAlchemy 2.1.6 → 2.1.8 |
| [#10](https://github.com/tvproductions/gz-skills-first-starter/pull/10) | Standard | virtualenv 21.14.13 → 21.15.5 |
| [#11](https://github.com/tvproductions/gz-skills-first-starter/pull/11) | X-Plane | nodeenv 1.11.0 → 1.12.0 |

This is scan recovery and PR scope/CI review, not permission to merge upgrades.
In particular, complexipy remains a historical defect reproducer; changing its
selection needs explicit consideration of that purpose, not routine green CI.
Lizard needs the counting-contract/analyzer regression gate before acceptance.
Other updates still require applicable compatibility review. No PR is approved,
merged or closed by this work; no release or native plugin is published/installed.
The root build-only uv_build update path and embedded-host behavior remain
unverified by these actual PRs. Future hosted images remain subject to checks.

The following documentation-only evidence commit preserves this completed
verification. Its CI must be observed separately; scan inputs and configuration
are unchanged from e918dbb. Report its final SHA/CI without another receipt-only
follow-up commit.
