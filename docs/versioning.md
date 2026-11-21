# Template versioning

Current published release **0.11.5 / patch** at immutable source
`0d3be366bc3048ed123d36dd6af93ad4d8850b80` restores latest-stable development-tool selections
in both Python baselines after the November 21 maintenance invocation. It also
covers the compatible instruction delivery cleanup and
[deterministic eval evidence](evidence/2026-11-21-instruction-delivery-evals.md).
The maintainer authorized publication with the gz-skills 0.14.0 pin refresh.
The [release receipt](evidence/2026-11-21-0.11.5-release.md) records the
exact combination, completed CI, annotated tag and downloaded-source checks. The
[roadmap scope](../ROADMAP.md#selected-0115-scope--dependency-maintenance-november-21-2026)
and [maintenance receipt](evidence/2026-11-21-dependency-maintenance.md) record
the governing commitment, checks and publication status.

Release **0.11.4 / patch** over published 0.11.3 restores this checkout's existing
project-owned, duplicate-free skill selection by suppressing inherited `superpowers-dev`.
The maintainer explicitly requested the repair during the instruction evaluation.
This is a compatible configuration correction; no new policy, component version,
public interface or architecture is selected. The November 20 ownership
clarification and selected instruction cleanup also belong
to this patch: preserve requirements while consolidating maintenance guidance,
aligning verification wording with SP and identifying current handoff authority.
The [bounded scope](../ROADMAP.md#selected-0114-scope--codex-duplicate-source-repair-november-19-2026)
and [evaluation](evidence/2026-11-19-instruction-discipline-evaluation.md) record
acceptance and remaining work. Release mirrors aligned at 0.11.4;
published v0.11.3 is immutable. The maintainer subsequently requested “git sync
and release 0.11.4,” authorizing ordinary synchronization, exact-source CI,
immutable tagging and GitHub publication after acceptance. The
[release receipt](evidence/2026-11-20-0.11.4-release.md) records actual progress,
including the mandatory release-time Ruff/platformdirs/setup-uv migration.
Included release work remaining: **none**; conditional engineering limits remain.

The following 0.11.3 paragraphs record the completed preceding release.
Release **0.11.3 / patch**, selected by the November 19 maintenance invocation,
restores the existing latest-stable tooling commitment with ty 0.0.107, Import
Linter 2.17 and virtualenv 21.15.9 in both Python baselines. Reconcile all version
mirrors at 0.11.3 and preserve both immutable published sources. The
[bounded roadmap scope](../ROADMAP.md#selected-0113-scope--dependency-maintenance-november-19-2026)
and [candidate receipt](evidence/2026-11-19-dependency-maintenance.md) own its
verification and remaining limits. The subsequent maintainer request **“release
0.11.3”** authorizes preparation, ordinary main synchronization, immutable
annotated tag and GitHub publication after the required exact-candidate checks.
The [release receipt](evidence/2026-11-19-0.11.3-release.md) records verified
publication. Included release work remaining: **none**. No next implementation
release is approved; the draft correction below remains independently gated.

The [bootstrap-verification correction](../ROADMAP.md#selected-correction--pre-implementation-verification-november-17-2026)
is in design review. Its proposed supported command/dependency/adoption interface
would select **0.12.0 / minor** after design approval. The maintainer separately
requested publication of the completed maintenance as **0.11.2**; the proposed
minor follows the pending maintenance patch; development metadata is **0.11.5**.
Reconcile the minor's mirrors only after its design approval.
No correction implementation, approved
architecture, completed minor-version reconciliation or release acceptance is
claimed. The [current handoff](handoffs/2026-11-17-bootstrap-verification-handoff.md)
distinguishes review direction from required complete-design/ADR approvals.

Release **0.11.2 / patch** over published **0.11.1** is selected for the
maintainer-invoked post-release dependency maintenance. New same-day uv/backend
and ty releases require a compatible pin/lock refresh under the existing
latest-stable commitment. No new requirement, runtime behavior, architectural
decision or adopter migration is introduced. The
[bounded roadmap scope](../ROADMAP.md#selected-0112-scope--post-release-dependency-maintenance-november-17-2026)
and [maintenance receipt](evidence/2026-11-17-post-release-maintenance.md)
own included work, acceptance evidence and remaining limits. The subsequent
November 18 “publish 0.11.2” request authorizes publication; follow the
[release receipt](evidence/2026-11-18-0.11.2-release.md) for actual outcome and
preserve all immutable published tags.

The November 18 maintenance invocation also refreshes four transitive packages
in both locks within that same patch. Use its
[candidate-specific receipt](evidence/2026-11-18-dependency-maintenance.md) for the
current inputs; preserve the November 17 receipt as historical evidence. This
compatible refresh adds no supported interface or adoption obligation and does
not select another per-task version bump.

Previous status, November 17, 2026: published **0.11.1** at immutable source
`041c1989406c1b9c4978042661c2dd38ff1db160` advances **0.11.0** by a compatible
documentation patch for the bounded
[roadmap reconciliation](../ROADMAP.md#selected-0111-scope--roadmap-reconciliation-november-17-2026).
Its release mirrors agree; the subsequent maintenance target is recorded above.
The [0.11.1 receipt](evidence/2026-11-17-0.11.1-release.md) records refreshed
freshness/security evidence, retained conditional engineering limits and verified
exact-source CI, annotated tag, GitHub release and tagged-source contents.

Previously published **0.11.0** at immutable source
`ccac3b5e1ac03f2cf5642d7766aed6e68001997c` advances **0.10.0**
(`6b236d87f301f689edae6934dabee9495df726d4`) by a minor release for the finite application-foundations/house-style
scope in the [roadmap](../ROADMAP.md#selected-0110-scope--application-foundations-november-16-2026).
Design edition 3 and ADR-0002 edition 2 are explicitly approved; implementation
and independent-review corrections are complete. The maintainer requested Git
sync and release publication on November 17. The
[0.11.0 receipt](evidence/2026-11-17-0.11.0-release.md) records release acceptance,
retained limits and verified exact-source CI, annotated tag and GitHub publication.
The maintainer subsequently requested correction of stale completed-work backlog
entries, then explicitly requested “commit, push, publish”. That completed patch
produced the 0.11.1 release above; it adds no adoption requirement or runtime
behavior. Preserve both immutable releases and their distinct acceptance evidence.
A version string alone is not publication evidence. The initial release was 0.1.0.

The following development narrative records the preceding 0.10.0 work; its
unpublished/next-target statements are historical and superseded by the current
status above and the [published release handoff](handoffs/2026-11-15-adr-release-session-handoff.md).
The then-selected minor was **0.10.0**: mandatory ADR practice for
the trio and its adopters, plus the maintainer-directed completed dependency-
migration binding recorded in the
[current handoff](handoffs/2026-11-08-adr-practice-save-point.md#dependency-maintenance-policy-correction--november-13).
It also includes the November 14
[starter-wide cognitive qualification deferral](engineering/cognitive-integration.md#starter-wide-qualification-deferral).
This changes acceptance policy, not the ceiling or qualification requirement;
it does not implement or publish the planned independent engine.
The maintainer's November 14 canonical **gz-starter** rename/migration decision
is booked as additional minor-level work in this valid pending 0.10.0 target;
see [the roadmap](../ROADMAP.md#canonical-rename-selected-gz-starter). The repository/local-folder and distribution/CLI rename are implemented in the
candidate with compatibility interfaces retained; downstream propagation and
remaining acceptance are explicit gates, not publication. Preserve the existing ADR/policy scope.
The November 14 [naming/layout proposal](engineering/naming-and-layout.md)
is new minor-level policy work, including explicit spaced-path rejection.
It remains a draft: preparing it neither activates the requirements nor selects
its implementation into 0.10.0. Reconcile the proposed bounded bundle at planning
and reuse this valid pending target if that scope is selected; do not increment
per pending task. Version mirrors remain unchanged and no release is authorized.
The [governing release-scope record](handoffs/2026-10-24-session-close.md#november-8-agreed-adr-practice-and-next-release-scope)
distinguishes this accepted direction from unfinished design, implementation and
acceptance. Adoption-acceptance reporting remains the final planned feature
before a separately scoped 1.0.0 with its newly written PRD.
Release 0.9.0's minimum-only uv policy
change governs the minor increment, alongside compatible corrections recorded
in the [release-planning audit](evidence/2026-11-01-release-planning-audit.md).
The [current release-scope record](handoffs/2026-10-24-session-close.md#november-8-git-synchronization-and-release-scope)
supersedes the audit's earlier patch-only target after upstream reconciliation.
The [0.9.0 receipt](evidence/2026-11-08-0.9.0-release.md) records the authorized
publication and acceptance inputs. Verify its immutable tag and GitHub release
before treating this metadata as publication evidence.
The 0.3 adoption contract removes starter-authored skills; see [migration](migration-0.3.md).
Release 0.8.0 bundles three-host repository configuration, brownfield scope repair
and mandatory adopter discipline. Its [release receipt](evidence/2026-10-31-0.8.0-release.md)
records independent execution-pin refreshes and retained acceptance limitations.
Release 0.7.1 ships the consumer-side preparation and a compatible Ruff patch.
The maintainer explicitly directed publication without waiting for the engine.
Actual cognitive integration remains open and unscheduled in
[issue #1](https://github.com/tvproductions/gz-starter/issues/1).
The incoming shared gzkit-derived engine must still be selected, qualified and
measured before the current deferral can end. Historical releases retain their
recorded exceptions and do not claim the cognitive defect is fixed; see the
[release receipt](evidence/2026-10-26-0.7.1-release.md).
The current version is recorded in
`bundle.json` as `template_version`, independently of SP, SP-BP and gz-skills
versions and the adopter's application version. `pyproject.toml` mirrors the
version for this starter's helper project; the repository tests check agreement.
An adopter may change its app metadata without changing the starter's identity.

```bash
uv run --locked gz-starter version
```

This reports the checkout's declared version, not proof of a published release.
The initial release is
[v0.1.0](https://github.com/tvproductions/gz-starter/releases/tag/v0.1.0),
dated October 11, 2026. Its annotated tag identifies the verified release commit.
Earlier development commits were untagged; do not label them as a released
v0.1.0 retroactively. Release
[v0.7.0](https://github.com/tvproductions/gz-starter/releases/tag/v0.7.0)
adds independently locked X-Plane tooling, Dependabot scans, current execution
tooling and shared policy alignment. The maintainer explicitly authorized its
publication with cognitive qualification deferred to planned 0.7.1; this is a
release-specific exception, not a passing cognitive result or an adopter waiver.
See [release evidence](evidence/2026-10-26-0.7.0-release.md).
Release 0.6.0 added the single template-native update skill and
[canonical update/bootstrap method](updating.md). It retains 0.5's expanded
Astral acceptance, lane/analysis policy, adopter SemVer and major-release PRDs,
and [greenfield/brownfield migration runbook](adoption-0.5.md). It retains the runtime,
tool and independent SP 7.0.0/gz-skills 0.8.0 pins. Automatic conformance/PRD
validation remains unimplemented; release notes disclose acceptance gaps.
Future publication remains a separately authorized operation.

## Ecosystem policy authority and consistency

### Initial adopter project version

The first substantive release is the first versioned commitment to the project's
public contract. Declare that contract and issue the release as **0.1.0**.
This establishes a versioned baseline; the contract may evolve under the required
0.x compatibility rules. It does not assert the stability required for 1.0.0.

Permit `0.0.0` only as an unpublished placeholder for a bare scaffold. As soon
as any original implementation, tests, documentation or configuration is added,
set the initial adopter project version to **0.1.0**. Do not release project-owned
work as `0.0.0`. Align package metadata, runtime version output and release
records, and verify agreement before accepting adoption. Correct an unpublished
`0.0.0` project containing original work to `0.1.0`; preserve published versions
and immutable tags, and
advance an existing released project from its actual current version. Never
reset a released project to `0.1.0` or rewrite a published `0.0.0` release.

This is a mandatory starter policy. SemVer permits zero-valued components, but
its [initial-development guidance](https://semver.org/spec/v2.0.0.html#how-should-i-deal-with-revisions-in-the-0yz-initial-development-phase)
recommends starting at `0.1.0`. Do not mistake syntax validity for acceptance
under this template. The adopter's initial version is independent of the
starter and upstream plugin versions.

### Shared authority

This repository is the authoritative alignment source for the maintainer's
shared engineering and release policy. This document owns the SemVer and
release-planning rules for this template, its adopters, and the maintainer's
`gz-skills` and `superpowers-backplane` repositories. The companion repositories
bind these rules in their own instructions and release documents; they do not
formally adopt this template or bootstrap its bundle into themselves.

Policy flows from this template to those repository bindings. Workflow ownership
is separate: [Backplane](https://github.com/tvproductions/superpowers-backplane)
owns requirements tracking, issue classification/lifecycle labels, backlog and
release monitoring, handoffs, and the definitions of lite and heavy modes.
Refer to its [mode authority](https://github.com/tvproductions/superpowers-backplane/blob/main/docs/superpowers-backplane/modes.md)
and governance instead of defining a second lifecycle here. gz-skills supplies
portable procedures such as `gzs-release`; Superpowers owns feature development.
Upstream Superpowers is independently owned and is not bound by this policy.

The companion repositories must check this source before release preparation,
during scoped policy/tooling maintenance, and when notified of a relevant source
change. Read this document, the changelog, and applicable baseline/engineering
guidance from the canonical repository. Compare with the last reviewed source;
record the date, full source SHA, paths, applicability, differences, and the
adopted decisions in the companion's existing release or handoff authority.
Record development guidance as unreleased; for authorized working-tree review,
also record content hashes and do not present the base SHA as the edited source.
Recheck the final source revision before claiming published alignment.

An unavailable source or unresolved applicable difference is an explicit gap,
not evidence of consistency. A departure needs evidence, the maintainer's
approval, an owner and a dated revisit condition. A local binding may specify
project details but must not silently redefine this shared policy. No automatic
schedule, plugin update, runtime upgrade or synchronized release is implied.

The major-release PRD rule below also applies prospectively to independently
versioned gz-skills skills, including their first 1.0.0. Each affected major
needs newly written requirements identifying that component and major; a new
coordinated PRD may cover several explicitly identified majors. Published
releases and historical acceptance evidence are not retroactively relabeled.

Repository governance is distinct from shipped workflow policy. gz-skills and
Backplane must continue to respect each consumer's own adopted policy; this
alignment does not impose starter tooling or PRDs on unrelated consumers.
Backplane's unfinished capabilities remain unfinished, and both mode intent
and policy alignment remain separate from installed readiness or full starter
conformance. Keep existing project authorities until the relevant Backplane
workflow is ready and explicitly adopted.

Each companion owns the explicit binding for its own development environment.
The maintainer's current Python rule is 3.14 for ordinary projects and supported
3.12 for X-Plane/XPPython3-bound code; the starter owns that rule for its adopters.
gz-skills workflows consume the governing project's policy instead of maintaining
a competing family/tool/package baseline. Publisher-side choices do not become
blanket constraints for unrelated skill or Backplane consumers. A corrected
source candidate must still be released and explicitly selected before installed
alignment can be claimed; source bindings are not native installation evidence.

## Version contract

### Plan releases from their governing work

Use this hierarchy for this starter, adopting projects and the bound companion
repositories: **PRDs guide major releases; selected work and requirements drive
minor releases; fixes drive patch releases.** Apply compatibility analysis to
that scope before selecting the number. A version bump alone is not a release
plan, and an individual task, commit or completed issue is not a release unit.

| Release | Governing scope | Required planning evidence |
| --- | --- | --- |
| Major, including 1.0.0 | A newly written PRD defines the intended product outcomes, requirements and boundaries for that major. | Link the new PRD, acceptance criteria and migration/compatibility decisions. Do not reuse an earlier major's PRD. |
| Minor | A coherent selected bundle of work and requirements advances the product within its governing direction. | Link the included requirements/work items, exclusions, dependencies and acceptance criteria in the existing backlog/release authority. |
| Patch | Corrections restore existing commitments, including compatible clarifications. | Link the defects or incorrect commitments, expected corrected behavior and verification. New capability or obligations do not become fixes by labeling them maintenance. |

Before implementation planning, identify which release scope the work serves.
Before accepting a completed change, reconcile its disposition into that scope:
included, deferred or excluded, with evidence. Keep a current release-scope record
in the project's existing backlog, roadmap or release authority; do not create a
parallel lifecycle. Record all of the following:

1. The actual last published version/tag and exact revision, or explicit evidence
   that this is the first unpublished release. Distinguish that baseline from
   current development metadata and the adopted starter/plugin versions.
2. The proposed next version and governing PRD, selected requirements/work or
   fixes. State why that scope requires major, minor or patch. Review the complete
   scope since the published baseline; the largest required increment wins.
3. Included completed work, included remaining work, deferred work and measurable
   release acceptance gates. Do not treat the whole future backlog as one release
   or require unrelated future work to finish before every release.
4. Compatibility impact and required migration, plus outstanding decisions and
   the evidence needed to resolve them. Unresolved scope/version decisions remain
   explicit; agents MUST NOT silently shrink an approved release to publish sooner.

Maintain the pending version, metadata/runtime mirrors, lock metadata where
affected, and changelog together once the release scope is selected. Multiple
changes in one planned release share its pending version; do not increment once
per task. Before release preparation passes, verify that the selected work and
actual diff agree, all required evidence exists, and the version matches that
scope. Missing scope or classification evidence blocks that claim.

For example, after released `0.4.2`, selected new reporting requirements drive
`0.5.0`; a correction to an existing report drives `0.4.3`. After `1.4.2`, a
compatible new reporting bundle drives `1.5.0`; its compatible defect correction
drives `1.4.3`. A new PRD guiding `2.0.0` must identify that major's outcomes and
requirements; incompatible changes cannot be hidden in `1.5.0`. A PRD does not
automatically make every implementation task a major release. During 0.x,
requirements and incompatible changes advance minor under the rules below;
the first stable `1.0.0` still needs its own newly written PRD.

An unpublished initial `0.1.0` may cover an explicitly selected first-release
scope. It is not evidence of a versioning defect merely because many tasks are
complete. Conversely, "unreleased" is not permission to accumulate unrelated
requirements indefinitely: review scope growth and record whether it belongs
in the first release or a later minor. Preserve existing approved release gates
until a scope change is approved. Published tags and release history stay immutable.

These are planning and acceptance obligations, not publication authorization.
Backplane retains workflow ownership; until ready and explicitly adopted, each
project's existing authorities execute them. Both lite and heavy follow this rule.

### Required version decision procedure

Agents MUST perform this procedure when accepting requirements, planning work,
and closing a change. Do not defer it until someone asks to publish a release.

1. **Establish the baseline.** Read project metadata, runtime version output,
   changelog, published tags/releases and current release scope. Verify their
   identities. Record missing publication evidence as UNKNOWN; do not infer it
   from a version string or silently assume there were no previous releases.
2. **Identify the governing commitment.** Link the new major's PRD, the selected
   minor requirements/work bundle, or the existing commitment being corrected.
   A patch needs an identifiable defect or compatible clarification. New required
   behavior is minor work even when its ticket or commit says "fix".
3. **Classify the complete pending scope.** Use the highest required increment,
   with compatibility constraints below. A stable breaking change requires a
   major and its newly written PRD before implementation planning can pass.
   Never suppress that consequence to avoid writing the PRD. A new PRD can guide
   several minor bundles within its major; it does not make each task a major.
4. **Select one target and reconcile it now.** Calculate it from the last
   published baseline, resetting lower components as shown below. Reuse a valid
   existing pending target. If new work exceeds it, revise the target and scope
   together; do not increment once per pending task. Update metadata/runtime
   mirrors, affected lock metadata and the unreleased changelog in the same
   change. Routine classification and version-file reconciliation are part of
   authorized work; do not ask the maintainer to choose a number agents can
   derive from this policy.
5. **Keep the bundle bounded.** State the release outcome, included requirement
   IDs, exclusions and measurable completion gate. An initial 0.1.0 needs that
   finite scope too. Assign unrelated/new future requirements to later minor
   bundles; do not append the whole roadmap to the active release. Changing an
   approved product outcome or gate requires a scope decision, not a guessed
   version. Ask only for the unresolved product decision and record the blocker.
6. **Verify and report.** Review the actual change against the governing work,
   check all version mirrors and prove the relevant acceptance criteria. Report
   `published baseline -> pending target`, release kind, source requirements or
   defects, included/remaining/deferred work and publication status. A closeout
   MUST NOT claim versioning complete without that evidence. Missing PRDs,
   scope, classification or inconsistent versions fail the applicable planning,
   closeout and release-preparation checks; configuration is not acceptance.

| Published baseline | Selected scope | Pending target |
| --- | --- | --- |
| No previous release, verified | Bounded first usable scope | 0.1.0 |
| 0.4.2 | Compatible fixes only | 0.4.3 |
| 0.4.2 | New requirements, including a bundle also containing fixes | 0.5.0 |
| 1.4.2 | Compatible fixes only | 1.4.3 |
| 1.4.2 | Compatible new requirements or public deprecations | 1.5.0 |
| 1.4.2 | Incompatible public contract, guided by a newly written PRD | 2.0.0 |

Use this compact decision record in the existing release/backlog authority;
equivalent existing fields are sufficient. Do not introduce a second tracker.

```text
Published baseline: version, tag and exact revision; or verified first release
Pending target / kind: version / major | minor | patch
Governing source: new major PRD | selected requirements/work | corrected defects
Release outcome and acceptance gate:
Included completed work / evidence:
Included remaining work:
Deferred or excluded work:
Compatibility / migration / version-mirror checks:
Unresolved product decisions: none, or decision owner and blocked action
Publication: unpublished | published with immutable identity
```

Selecting a version does not assert readiness or authorize publishing it. Tool
updates and refactors are classified by their effect on the public contract;
commit prefixes, effort, elapsed time and the upstream dependency's own version
do not determine this project's bump. Preserve published identities and approved
scope. Do not manufacture past releases to make development progress look older.

### Classify compatibility within the selected scope

Use [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for the template's
public adoption contract: CLI commands and outputs, managed-file formats,
preservation/conflict behavior, baseline requirements and project guidance.
During 0.x development, bump the minor version for additions, requirement changes
or adoption changes requiring reconciliation; bump the patch for compatible
fixes and clarifications. Release 1.0.0 only when the intended public contract
and its compatibility guarantees are established. After 1.0, incompatible
contract changes require a major bump, compatible additions a minor bump and
compatible fixes a patch bump. Explain adopter impact even for small changes.

The unreleased [completed dependency-migration binding](baseline-policy.md#dependency-maintenance-means-completed-migration)
changes adopter authorization and completion requirements: ordinary maintenance
and bare dependency-skill invocations now execute and verify the current stable
migration across families; only explicit review requests are read-only. This is
a policy change requiring **minor** reconciliation under the 0.x contract,
not a patch clarification or pin refresh. Reuse the valid existing pending
**0.10.0** target from published **0.9.0**, adding this maintainer-directed binding
to its existing policy bundle without another per-task bump. Bundle, package,
lock and packaged version mirrors remain 0.10.0; the ADR feature's remaining
qualification gates are unchanged. Preserve immutable published history; no
publication or adopter propagation is authorized by correcting documentation.

Version 0.6.0 adds a native template-update skill and a managed adopter
file, changing the supported adoption capability and ownership contract. It
therefore increments minor from 0.5.0. A compatible correction to an existing
capability would increment patch (for example 0.5.1) and get its own new tag;
neither case moves or reuses v0.5.0.

The following release-planning rules bind this starter and each adopting
project's own releases. App, template and upstream component versions remain
independent; an adopter's PRD describes its own product and major release.

Adopting projects also use `MAJOR.MINOR.PATCH` for their own public product
contract. Apply the same 0.x and stable-release classification above to that
contract, independently of the template's version. Document the supported public
surface, such as Python APIs, CLI behavior, file/data formats and configuration
contracts. A breaking change to that surface requires major after 1.0 even when
it changes no Python function signature. Compatible additions require minor;
compatible fixes require patch. Public deprecations require minor, with removal
reserved for a subsequent major after 1.0. Incrementing major still requires
the newly written PRD below; the PRD does not replace compatibility analysis.

Every major release, including 1.0.0, **always requires a newly written PRD**
for that major release. Reference that PRD in release preparation and evidence;
reusing an earlier major's PRD or changing the version number alone does not
satisfy this requirement. Compatibility impact still determines when a major
bump is needed; the new PRD is a mandatory part of preparing that release.

Minor releases bundle a coherent selected set of related changes. A completed
feature does not automatically trigger its own minor release; record the bundle
in the project's existing backlog and handoff authorities. SP-BP is intended to
help coordinate this bundling when ready and explicitly adopted. While it is
deferred, use the existing authorities without inventing a replacement lifecycle.
The compatibility rules above still bound what belongs in a minor release.

Patch releases remain compatible fixes and clarifications, including bounded
verification of existing commitments; they do not introduce new baseline
obligations. These release-planning rules supplement the version classification
above and do not retroactively relabel published releases.

The user explicitly selected patch versions 0.3.1 for the adopter cohesion
requirement clarification and 0.3.2 for the independent SP update. Their changelog
entries distinguish policy from pin changes; these scoped choices do not change
the general rule above. SP's upstream major version is independent of the
template version.

Release notes distinguish changes to [adopter range/selection policy](baseline-policy.md)
from refreshes of tested exact pins within that policy. Adopters review constraints
and their reasons rather than treating every checkout pin as a permanent requirement.

The current manifest accepts numeric `MAJOR.MINOR.PATCH` versions. Development
snapshots carry the next intended version plus their exact commit SHA; they are
not stable releases until published. Prerelease suffixes would require a scoped
manifest/CLI change. Stable Git tags use `vMAJOR.MINOR.PATCH` and must never be
moved or reused after publication. Subsequent changes receive a new version.

Template version, bundle/lock `schema_version` and upstream component versions
are separate. A template bump does not enable SP-BP, update a plugin or alter a
file schema automatically. A metadata-only additive field does not imply a new
schema; a breaking interpretation of a managed format requires its own reviewed
schema/migration decision.

## Adopter provenance and upgrades

New adoption records the starter's repository, manifest version and full commit
SHA in `.skills-first/bundle.lock.json`. Configure preview/apply and status expose
that starter record. Keep the SHA: multiple development commits may share the
next intended version, and a label alone cannot identify their contents.
The helper records the supplied/default SHA and manifest label; it does not prove
that they match a published tag. Verify the checkout, tag and full commit before
adoption. Native catalogs continue to pin upstream components by full SHA.

Legacy records without a starter version have unknown version provenance.
Do not infer their version from today's metadata or edit their recorded SHA.
Compare the original revision with the desired reviewed release, preview the
full managed-file diff and reconcile the lock, configuration and guidance
together. The helper deliberately refuses different managed records instead of
silently adding a version or migrating an adopter. Preserve app additions,
settings, overrides and profile choices and retain prior pins for rollback.
Until reconciled, configure/status may report the managed-record conflict.

Use the existing [stack maintenance binding](adoption.md#maintaining-the-adopted-stack)
and gz-skills workflows to assess upgrades. Check published starter releases
alongside SP, SP-BP and gz-skills independently; generic freshness tooling remains
upstream-owned. A newer starter does not automatically migrate a generated
repository or prove fresh-session skill discovery.

## Preparing and publishing a release

1. Select the next version according to the adoption contract. For every major,
   including 1.0.0, write a new PRD and reference it in the release evidence.
   For a minor, identify the coherent change bundle in the existing backlog;
   SP-BP may assist only after readiness and explicit adoption. Update
   `bundle.json` and the starter's `pyproject.toml` together, then refresh `uv.lock`
   with uv if its project metadata changed. Preserve independent plugin pins
   unless their upgrade was explicitly scoped.
2. Add a changelog entry describing behavior, baseline/pin changes, adopter
   reconciliation steps, verification evidence and remaining limitations. Mark
   the entry unreleased while preparing it. Preserve historical evidence as-is.
3. Run the documented repository checks on the exact Python pin and review the
   clean committed release candidate. For bundle changes, validate both native
   catalogs. Native loading/readiness evidence remains separate.
4. When publication is authorized, mark the changelog entry released, commit the
   final release metadata, tag that exact verified commit with an annotated
   `vMAJOR.MINOR.PATCH` tag and publish the GitHub release with those notes. The
   release must identify the full commit SHA and remaining host/Backplane gaps.
   Verify the remote tag resolves to the intended commit; do not move it to fix
   a release. Do not conflate an ordinary Git sync with release publication.

The template's GitHub release is the adopter-facing distribution record. No
package-registry upload, plugin installation or new release automation is
required by this policy.
