# Roadmap

## Implemented initial scaffold

- Immutable SP + SP-BP + gz-skills bundle with independent sources.
- Codex and Claude native marketplace catalogs.
- Preview/apply/status Codex project configuration for empty and existing projects.
- Preservation/conflict/symlink/duplicate/gzkit checks and unittest coverage.
- Zero starter-authored skills; documented adoption workflow and direct workflow
  routing in adopter instructions. Analysis utilities live in ordinary tooling.
- Default SP + gz-skills activation with SP-BP pinned but disabled.
- Read-only structural assessment and guidance for incremental backporting.
- Documented native loading/verification boundaries.
- Independent template version metadata and CLI reporting, version/SHA adopter
  provenance, changelog and release policy. Initial v0.1.0 is published.

## Next adoption proofs

1. Fresh Codex session: install from the published marketplace, verify project
   enablement scope, exact loaded revisions, SP and gz-skills entry identities. Backplane
   participation waits for its upstream readiness and explicit adoption.
2. An authorized adopting repository pilot (FDAU is the primary candidate).
   Map existing configuration and adapters; do not replace project authorities.
3. Claude project-scope installation, lifecycle, and combined-stack conformance
   after upstream Backplane Claude acceptance.
4. OpenCode support after upstream Backplane V1/V2 adapter and verification.

## Later extensions

- Reviewed update/rollback automation that preserves existing native installs.
- Generic maintenance remains owned by gz-skills; no local maintenance skill or
  generic freshness reporter is planned. The pinned gz-skills v0.7.0 now supplies
  freshness-only assessment and template/plugin source inventory through its
  existing maintenance skill. The starter retains policy, catalog consistency and
  preservation bindings; current tests prove preservation, not dependency
  resolution or settings loading. See the
  [configuration contract](docs/project-configuration.md).
- New-project product templates selected by the adopter, not a mandatory framework.
- Optional app-owned plugin registration alongside the three engineering plugins.
- Synchronize bundle compatibility evidence as SP-BP completes its release and
  broader proposed capabilities mature.

No milestone above implies a release, current installed stack, or a completed
upstream capability. Requirements/traceability expansion belongs to Backplane,
not a duplicate lifecycle in this starter.

## Python engineering policy follow-up

Reusable Python-version idiom/stdlib review belongs upstream in gz-skills.
The starter's [baseline policy](docs/baseline-policy.md) requires assessing code
currency, but the pinned Pythonic-pattern skills are not a complete version audit.
Record that coverage gap and review a future released workflow before routing
to it. gz-skills v0.7.0 reinforces runtime discovery and scoped version-aware practices
in its existing Python workflows; a comprehensive version audit remains a gap.

The required Python 3.14 engineering policy documents the
routine standards and on-demand hygiene selections, including Cosmic Ray,
deptry, pip-audit and Import Linter. The approved routine pre-commit selection
remains Ruff check/format, ty and unittest.
Still pending: project-locked ty and routine pre-commit checks; agreement on
expanded strict Ruff rules; shared/local utility ownership and existing-project
policy adoption; a pinned Cosmic Ray Python 3.14
synthetic unittest compatibility proof; pinned Python 3.14 verification of the
selected deeper analyzers. Deeper analyzers remain outside hooks
and CI gates. SP-BP remains an expected addition, deferred pending readiness.

Complexity evaluation completed: Ruff 0.15.18 C901 (20) plus complexipy 8.0.1
cognitive complexity (15) replaces Xenon in the starter's on-demand policy.
Python 3.14.8 synthetic compatibility and threshold checks passed. Two existing
functions exceed cognitive limits; configure also exceeds cyclomatic 20. Keep
those findings visible and ratchet down in separately scoped source changes.
The routine pre-commit selection and CI remain unchanged; C901 is not enabled
in ordinary Ruff lint selection. The latest user decision adds Lizard 1.24.1 and retires Radon too. Recover
individual/module/overall aggregation with Lizard; counting policy, corpus
comparison and final C/C/C approximation enforcement remain pending. Keep
periodic dependency freshness review on demand, and tool preferences starter-owned.

## Settled C/C/C implementation — October 9, 2026

This supersedes earlier pending-contract statements. The explicit on-demand
Lizard checker implements `lizard-functions-v1`: function/module/overall
ceilings 20/20/20, nested functions counted independently, no synthetic class
scores, native assertion semantics, undefined empty means, and fail-closed
syntax/discovery errors. Use native Lizard measurements without syntax adapters; unsupported inline
suites fail discovery instead of disappearing from the measurement. Read `docs/engineering/ccc-contract.md` and run its CLI explicitly. Ruff and complexipy remain independent
checks; routine pre-commit and CI selection are unchanged. SP-BP remains expected,
deferred and disabled. No cob_reports tool configuration or app code changed.
The source-only cob_reports receipt reports 649 functions, maximum 100, overall
mean 7.14946, 42 function and 12 module failures, zero tool errors; this is
verified enforcement with visible legacy debt, not a clean corpus.
