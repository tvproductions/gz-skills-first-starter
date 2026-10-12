# Changelog

## 0.3.2 — Unreleased

- Pin refresh: update Superpowers from v6.4.1 to the latest stable v7.0.0,
  published October 10, 2026, at full SHA
  `bb92a77741419a4ab5f06e711a283343f1ada0c3`. Align the bundle and both native
  catalogs. Retain gz-skills, Backplane and Python/tool pins.
- Correct current SP guidance: Backplane's historical compatibility baseline
  does not constrain active SP while Backplane remains deferred and disabled.
  Prepare patch 0.3.2 as explicitly requested; no adopter baseline policy changes.

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

## 0.3.1 — Unreleased

- Policy change: require cohesion in the adopter minimum on-demand Python tool
  standard. Clarify that downstream tool requirements are independent of the
  starter helper's own needs; adopters own tool pins, runtime verification and
  interpretation of class scores. Pass the requirement through the generated
  instructions fragment and linked baseline/engineering guidance.
- Prepare patch version 0.3.1 as explicitly requested by the user for this
  requirement clarification. Runtime, analyzer and upstream component pins are
  retained; no cohesion dependency is added to the starter environment.

Adopter impact: reconcile project instructions and the selected development tools
against the reviewed policy. Verify cohesion on the selected runtime with invented
class fixtures, preserve project thresholds and record inapplicable scopes or
compatibility gaps. Keep the tool outside hooks and CI gates. Selection does not
establish installation or Python 3.14 compatibility; this starter has no cohesion
compatibility receipt. Existing adopters are not automatically migrated.

Verification: 28 unittest tests, bundle/both-catalog validation and Ruff 0.15.18
check/format passed on Python 3.14.8. The offline uv lock refresh changed only
the starter's version metadata. This policy/documentation change requires no
Python 3.14 API changes; no cohesion execution or compatibility claim is made.

## 0.3.0 — 2026-10-11

- Establish the zero-skill ownership contract: this template authors and
  distributes no agent skills. SP + SP-BP + gz-skills remains the intended stack,
  with SP and gz-skills active and SP-BP deferred/disabled pending readiness and
  explicit adoption. Project operational skills remain project-owned.
- Move adoption instructions into `docs/adoption-workflow.md`, Python policy and
  references into `docs/engineering/`, and on-demand analysis utilities and their
  CLI tests into `tools/engineering/`. Preserve the existing Python/tool policy
  and analyzer semantics. Remove all starter `SKILL.md` packages.
- Configure now writes host configuration, provenance and project instructions
  without installing a front-door skill or creating skill discovery directories.
  Instructions route directly to upstream/project workflows and require review
  of template releases, dependency updates and baseline-policy changes.
- Add the structure/ownership contract, supporting design precedents and an
  explicit migration guide. Correct stale copied guidance about gz-skills v0.6.0
  maintenance and setup capabilities without invoking setup or selecting a profile.
- Clarify that adopters stay current within Python 3.14.x, or host-compatible
  3.12.x for XPPython3-bound projects. Exact execution pins are refreshed verified
  selections rather than permanent adopter patch requirements. XPPython3's
  embedded runtime remains host-controlled and requires separate validation.
- Add `docs/baseline-policy.md` as the adopter version-range/selection authority,
  separate from checkout-specific execution pins. Release guidance distinguishes
  policy changes from pin refreshes; unsettled tool families remain explicit gaps.
- Require relevant code to observe the selected Python family's idioms, stdlib
  advances and deprecations through bounded evidence-backed review. Delegate
  reusable workflows to SP/gz-skills while keeping runtime policy starter-owned;
  the pinned Pythonic-pattern skills do not prove complete version-audit coverage.
- Inspect seven relevant gz-skills instruction bodies and verify their Git blob
  hashes against the pinned release; document Python pattern, portability,
  environment/maintenance and debt/change-review coverage and its limits.
- Reinforce upstream runtime/engineering-policy obedience while leaving runtime
  discovery in gz-skills. Record the separately authorized neighboring-source
  reinforcement as released v0.7.0 at `6ebf803e4a2775d3742c84984a03548275b7c926`,
  selected consistently by the bundle and both native catalogs. Tagged installs
  passed in disposable Codex/Claude configuration and the uvx snapshot installer.
- Correct the relocated analyzer test fixture to write Python source as UTF-8;
  Windows' legacy locale encoding otherwise invalidates its Unicode cases.

Adopter impact: reconcile older managed records and project instructions; retire
legacy starter skills only after reviewing and preserving project edits. Configure
blocks legacy starter skill names in all four inspected discovery surfaces before
any writes and preserves their contents. It never performs an automatic migration.
Keep prior pins/configuration for rollback and preserve application skills,
dependencies, overrides, profiles and native manager state.

Verification: 28 routine unittest tests, bundle/both-catalog validation and pinned
Ruff lint/format checks on Python 3.14.8, plus the relocated analyzer's ten public
CLI tests. Template metadata/lock changes select 0.3.0; SP/SP-BP and runtime/tool
pins are retained. The independent gz-skills update is recorded above.
The relocation requires no new Python 3.14 APIs; concurrency, annotation,
compression and template-string opportunities are deferred as unnecessary here.
Historical evidence retains its original paths/hashes and failures. Fresh-session
host loading, ty/pre-commit enforcement and the other documented gaps remain
unverified or pending. The GitHub release identifies the full verified template
commit and CI outcome; native loading evidence remains separate.

## 0.2.0 — 2026-10-11

- Adopt gz-skills v0.6.0 at exact commit
  `e722e808647481c4c9d2feab61f1843aa8e0b19a` in the bundle and both native catalogs.
  Its nineteen-skill catalog adds project setup and Pythonic pattern review/apply;
  maintenance now supports freshness-only review and starter/plugin inventory.
- Update guidance that previously described these released capabilities as
  proposals. Preserve approved starter Python 3.14 and retired-tool policy over
  upstream profile defaults. SP and deferred/disabled SP-BP pins are unchanged.

Adopter impact: existing managed locks and front-door skills require reviewed
reconciliation; configure refuses to overwrite older records. Keep prior pins
for rollback, preserve app files and explicit profiles, and use the native host
manager only when its update is authorized. This release does not invoke project
setup, select lite/heavy, install plugins or migrate other projects.

Compatibility review: gz-skills' Python CLI now requires >=3.13, compatible with
the starter's pinned 3.14.8. Native plugin consumption does not require that CLI.
The pin change needs no new Python APIs; concurrency, annotation introspection,
compression and template-string machinery are deferred as unnecessary here.
See [the update assessment](docs/evidence/2026-10-11-gz-skills-0.6.0.md).

Verification: 25 unittest tests, bundle/both-catalog validation and Ruff 0.15.18
check/format passed on Python 3.14.8. uv lock refresh changed only the starter
version; a subsequent lock check passed. Release notes identify the full release
commit and its GitHub CI result. Starter-specific fresh-session loading remains unverified;
upstream installation evidence does not prove this combined bundle loads.
ty/pre-commit and the other documented tooling gaps remain outstanding.

## 0.1.0 — 2026-10-11

Initial versioned template baseline; earlier untagged development commits did not
establish a published release.

- Immutable native catalogs for independent SP and gz-skills sources; SP-BP
  remains pinned, pre-release, deferred and disabled.
- Preview/apply/status adoption with conflict preservation, idempotence and a
  starter-owned front door; read-only structural backport assessment.
- Python 3.14 family policy with exact patch 3.14.8, baseline configuration
  guidance permitting project additions/extensions/overrides, and maintenance
  routing to gz-skills.
- Explicit UTF-8 reads and preservation of existing host TOML line endings.
- Starter version and exact revision in new adopter records, plus a read-only
  `version` command and version-bearing configure/status/validate output.

Adopter impact: reconcile older managed files from a reviewed starter checkout.
Unversioned starter records retain their existing SHA and require review; the
helper does not overwrite them or invent version provenance. App dependencies,
settings and explicit profiles remain project-owned.

Verification: 25 unittest tests, bundle validation (including both native
catalogs), Ruff 0.15.18 check and format check passed on Python 3.14.8.
The GitHub release notes identify the exact verified release commit.
gz-skills v0.5.0 remains its latest published release as checked October 11;
newer upstream main changes are not included in this baseline.
Native host discovery and
end-to-end installation remain unverified; ty/pre-commit enforcement and other
documented Python tooling gaps remain outstanding. This version does not certify
combined-stack compatibility or SP-BP readiness.
