# Fresh handoff after 0.10.0 publication — November 15, 2026

## Foundations design continuation — November 16, 2026

The maintainer subsequently selected application foundations, house style and
hexagonal guidance as **0.11.0 / minor** work, requesting Superpowers
brainstorming. Continue from the [design draft, edition 1](../superpowers/specs/2026-11-16-application-foundations-design.md)
and [draft ADR-0002 edition 1](../decisions/ADR-0002-001-runtime-configuration-boundary.md),
with release scope in the roadmap. Both await their distinct approvals; no
foundation behavior is implemented or activated by these drafts.

Decisions: settings.json for runtime configuration, separate from pyproject tool/
build settings; right-sized architecture retains principles with fewer components;
agents offer warnings and respect explicit human departures. The maintainer
specifically reaffirmed rejection of all paths containing spaces, including
user-selected paths. Preserve that runtime contract rather than treating it as an
advisory warning. The broader proposed Ruff/ty activation stays deferred.
Independent builder review found those last two scope questions; both are now
resolved. The design includes a complete numbered disposition of GZKit's 108
house-style candidates and links exact drydock/hexagonal sources.

Pending-version mirrors are 0.11.0, with dependency/component pins unchanged.
Five focused version/resource tests, catalog validation, resource-drift and lock
checks passed. Draft prose/reference review follows the risk-based verification
policy; no runtime-foundations, upstream-audit effectiveness or strict acceptance
claim follows. Existing 0.10.0 release evidence below remains historical and valid
for its own exact source. No new publication, native installation, companion
mutation or adopter migration is authorized.

## Resume point

**The requested 0.10.0 release is complete.** The current request is a fresh
handoff and ordinary Git sync of this starter. No further implementation,
maintenance, companion mutation, installation or publication is selected.
Do not resume obsolete release blockers or repeat unchanged qualification.
Start future work from the published 0.10.0 baseline and existing authorities;
derive a new version only when governing work is selected.

## Verified release and source state

- [GZ Starter 0.10.0](https://github.com/tvproductions/gz-starter/releases/tag/v0.10.0)
  was published at **2026-11-15 23:35:00 UTC**, as a normal, nondraft release.
- Release source: `6b236d87f301f689edae6934dabee9495df726d4`.
  Annotated tag object: `b6079417b9e1460ff0ee799655ad587ead40538d`.
  The remote tag peels to that source; never move it.
- [Exact release-source CI](https://github.com/tvproductions/gz-starter/actions/runs/43775495781)
  passed both `checks` and `xplane-baseline`.
- Downloaded tagged source equals `git archive` for all **189 files**.
  Captured ZIP SHA256:
  `e3b3936e69eb96f6792b02a9a57f1ba2ad85bbf9dc71fe2d5e60b0dae647b6ad`.
- Governing issues [#12](https://github.com/tvproductions/gz-starter/issues/12)
  and [#13](https://github.com/tvproductions/gz-starter/issues/13) are closed
  completed. Milestone 0.10.0 is closed with zero open and two closed issues.
- This handoff starts from clean `main`, aligned with freshly fetched origin at
  the release source. Its documentation-only follow-up commit and exact CI result
  are supplied in the sync response; do not create a self-referential receipt chain.
  The existing origin URL redirects successfully to canonical `gz-starter`.

Release acceptance, publication and Git synchronization are separate results.
See the [release receipt](../evidence/2026-11-15-0.10.0-release.md) and
[exact-combination qualification](../evidence/2026-11-15-adr-combination.md).
The approved scope and actual ADR-0001 edition 1 are unchanged.

## Completed evidence and retained limits

The locked release gate passed with managed Python **3.14.10** and uv **0.13.8**:
four routine checks, 72 unittest methods, both catalogs, six-resource drift,
source-independent build and isolated installed CLI/alias/link/local checks.
All twelve targeted publisher/lite/heavy/access/conflict scenarios passed;
all 140 protected inputs remained unchanged. The source-identical shared B01–B16
matrix, active Backplane controls, genuine use/alignment in all three publishers
and completed independent final review are linked from the combination receipt.
Its curated invented-fixture archive is committed; complete local originals and
the unsuccessful permission-limited probe remain under `dist/adr-qualification/`.

Acceptance retains the documented cognitive deferral: ceiling 15, measurement
UNKNOWN, no shared engine installed or qualified. Actual model identity,
normal-profile restart, other native hosts/models, and the stated deeper-tool,
cohesion and embedded-deployment gaps remain explicit. Do not claim full strict
conformance or extend bounded observations to real adopters.

Same-day official freshness/audit evidence remains applicable to unchanged
manifests and locks. This handoff reuses it under the
[documentation-only verification policy](../engineering/verification-policy.md);
no dependency migration or build/model replay is required for these prose edits.
Preserve normal hooks and observe the handoff commit's own CI after pushing.

## Component and workspace preservation

The selected combination is SP **7.0.2**, gz-skills **0.13.0**, and Backplane
**0.3.0 disabled**. Both catalogs agree. Codex/Claude project marketplace refs
use starter catalog `9f0f27791713f735d960e44b18759a9fb63a61ae`; OpenCode
selects matching sources. Activation, duplicate overrides and user defaults stay
unchanged. Configuration does not prove normal-profile skill loading.

Registered companion worktrees remain under
`%TEMP%/gz-adr-prerequisites-20261115/`. Read-only inspection for this handoff found
both clean and equal to their recorded origin/main:

| Worktree | Published source | Evidence descendant |
| --- | --- | --- |
| gz-skills | 0.13.0 `0bdab63fc503c6b36e2dd487932689b4e555e41a` | `36377cb27638194e122f268781557a729c9bdf5c` |
| superpowers-backplane | 0.3.0 `39fbe3065c16ac119c4c10a3c2428fda39d57e61` | `6362be0da9ad9f0eba8889b94bf1047671156f88` |

GZ's four exact tagged channels and Backplane's native arrival/three-platform CI
are verified in their owning receipts. Backplane #37 is closed completed.
Companion synchronization is not part of this documentation-only starter sync.

Original sibling checkouts retain unrelated edits. Preserve gz-skills'
`CHANGELOG.md`, `docs/evidence/2026-11-14-dependency-maintenance.md`, and
`docs/release-policy.md`; preserve Backplane's `docs/release-policy.md`.
Do not reset, stash, remove their worktrees, or sweep those edits into commits.
Keep private OpenCode server stdout and authentication out of public evidence.

## Future work

Naming/layout enforcement, management sidecars/commit metadata, a future CLI,
real-adopter pilot, deterministic upgrades, wider platform proof and acceptance
automation remain deferred under their existing authorities. No next feature
or version has been selected. Preserve separate explicit ADR approval and
Superpowers' **Native** execution term; keep updates plain and bounded.

Earlier history remains in Git through the release source and the linked
[ADR save point](2026-11-08-adr-practice-save-point.md) and
[November 14 design discussion](2026-11-14-opinionated-cli-design-discussion.md).
