# Changelog

## 0.1.0 — Unreleased

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

Verification: run the repository checks before publication and attach the exact
release commit's results to its release notes. Native host discovery and
end-to-end installation remain unverified; ty/pre-commit enforcement and other
documented Python tooling gaps remain outstanding. This version does not certify
combined-stack compatibility or SP-BP readiness.
