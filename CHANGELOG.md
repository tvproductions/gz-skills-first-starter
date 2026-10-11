# Changelog

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
