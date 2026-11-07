# Python policy authority correction — November 7, 2026

The maintainer explicitly requested fixing alignment in the starter, gz-skills
and SP-BP, then reaffirmed current policy: Python 3.14 unless X-Plane/XPPython3
bound, then supported 3.12. This corrects authority drift already discussed in
October. It does not establish a new global policy for unrelated consumers.

## Source and scope

Starter begins at `4f8bb09633655473cd6aab9e1ddc60963c487bb1`, clean before this
correction. Its existing baseline already declares `>=3.14,<3.15` for ordinary
projects and `>=3.12,<3.13` for XPPython3-bound code. Those family declarations
and exact interpreter selections do not change here.

Canonical gz-skills main starts at `9a7970208207d68cc4a04eff7c3d39bcea664463`.
A new standalone source checkout owns the edits; installed caches and consumer
copies are untouched. Setup/update previously honored explicit adopted policy
but also supplied 3.13 and a fixed tool/package assortment when policy was absent.
The candidate removes that competing standard, preserves authority precedence
and reports missing/unavailable authority. Its own ordinary Python project moves
from 3.13.15 to managed 3.14.10 and declares the 3.14 family. Pending bundle 0.9.0
and skill 0.4.0 reflect changed pre-1.0 fallback/support contracts; no publication
or catalog pin change is authorized by source alignment.

SP-BP at `0aa0cc0` already owns a Python 3.14 decision. Actual initial runtime
and pin agree at managed 3.14.10. Existing release-doctrine changes were present,
and a separate strict-Astral reconciliation is concurrently adding its tooling
project/lock/CI. Preserve those artifacts. This task only clarifies Backplane's
own ordinary-project authority and appends its source binding/scoped receipt.
Its current metadata already says `>=3.14,<3.15`; do not misattribute that work
or claim complete strict acceptance from this narrower correction.

## Behavioral witness

A fresh read-only baseline review exercised five cases: available adopted 3.14
with stale 3.13 pin; unavailable adopted source; approved host 3.12; unrelated
consumer 3.11/custom tools; no policy with heavy selected. The no-policy case
explicitly selected the retired 3.13/tool default. The unavailable-source case
had an ambiguity; the other three already respected explicit policy.

A separate fresh post-change scenario review passes all five: use the available
adopted authority, keep missing/unavailable authority UNKNOWN, preserve host
verification and unrelated consumer policy, and require a project decision when
no baseline exists. This is bounded instruction behavior evidence, not native
host execution or statistical reliability across all future model sessions.

## Distribution and verification boundaries

The starter still selects published gz-skills 0.8.3. A corrected source candidate
is not an installed fix. Publish/review that independent candidate and perform
an explicitly scoped source update before claiming native discovery of the
correction. No installed skill bytes or native activation are changed here.
The starter's release rules still distinguish source edits, Git sync and release.

Record actual per-repository checks and remaining gaps before completion. Keep
gz-skills' backend/resource layout and full Astral migration outside this bounded
Python-policy correction; no broader conformance or freshness claim is made.

## Observed checks and remaining state

- Starter: locked all-group sync, four routine hooks, catalog validation,
  source-independent build and isolated installed-distribution verification
  pass. Regenerated adopter instructions agree with the authoritative fragment.
  Ordinary interpreter remains managed 3.14.10; the separate X-Plane runtime
  probe reports 3.12.16. No analyzer implementation or bundle pin changed.
- gz-skills: 28 tests pass before/after on the actual original 3.13.15 and new
  managed 3.14.10 respectively; Ruff/format/ty, all 20 skill validations,
  source-independent build and installed-wheel catalog/resource proof pass.
  Both artifacts match 44 canonical resources. Below-family 3.13 installation is
  refused. The authority scenario correction passes all 5 bounded cases. Its
  own evidence records the unchanged portable-helper syntax and package scope.
- SP-BP: actual managed 3.14.10, current locked hooks and 9 adapter tests pass.
  Existing strict-Astral acceptance gaps remain unchanged. Its pre-existing
  source-binding contents are preserved byte-for-byte before the appended
  authority section. This does not publish its separate concurrent work.

The three source checkouts are intentionally uncommitted. Canonical starter and
companion bindings agree on current authority; installed gz-skills 0.8.3 still
needs a separately reviewed release/update to expose the corrected source.
No native plugin install, source publication, tag or GitHub mutation occurred.
