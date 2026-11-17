# Canonical rename to gz-starter

The maintainer selected **gz-starter** as the canonical repository, distribution
and command name on November 14, 2026, and explicitly authorized executing the
GitHub/local-folder migration. Display name is **GZ Starter**; **starter** and
**starter template** remain valid shorthand. This is minor-level work in the
completed **0.9.0 -> 0.10.0** scope, not a second increment per task.
The rename shipped in [0.10.0](evidence/2026-11-15-0.10.0-release.md);
the latest published baseline is [0.11.0](evidence/2026-11-17-0.11.0-release.md).
Starter checkout relocation, desktop binding, environment repair and installed
aliases are complete. The checkout procedure below is retained as migration
guidance; it is not pending starter work. Downstream migrations remain explicit.

## Canonical identities and retained compatibility

| Surface | Canonical/current selection |
| --- | --- |
| GitHub repository | `tvproductions/gz-starter` |
| Local checkout folder | `gz-starter` under the existing project parent |
| Python distribution | `gz-starter`, shipped in 0.10.0 |
| CLI | `gz-starter`; `skills-first-starter` remains an equivalent alias |
| Python import | `skills_first_starter` is retained for compatibility |
| Native marketplace identity | `skills-first-starter` is retained to preserve configured plugin IDs and overrides; display name is GZ Starter |
| Adopter record directory | `.skills-first/` remains stable |
| Owned update skill | `update-gz-template` remains stable |

Do not mechanically rename compatibility keys, import paths, existing adopted
records or all historical URLs. These retained interfaces are intentional, not
unreconciled new branding. New helper configuration, policy links and provenance
use the new canonical source. Source detection accepts the new HTTPS/SSH origins
and both historical repository names. Existing adopter files remain protected by
the helper's preservation/conflict rules.

## Starter checkout and development environment

Rename the existing GitHub repository with the owning `gh repo rename` command,
verify repository identity/history and its new URL, and update this checkout's
origin. Preserve published tags/releases. Coordinate the folder move with the
desktop project; update its primary folder to the relocated checkout. Do not
create an unrelated replacement repository or discard local work.

Python virtual-environment scripts and installed Git hooks can contain absolute
paths. Recreate the repository-owned `.venv` using the exact managed interpreter,
sync the unchanged dependency selections from the lock, and reinstall the same
four pre-commit hooks after relocation. This is environment repair, not a tool
freshness update. Preserve native user settings and caches.

Verify `uv run --locked gz-starter version`, its legacy alias, bundle/catalog
validation, normal hooks, `uv build --no-sources` and clean installed behavior.
The installed-artifact verifier exercises both command names. Observe CI for the
final pushed commit; report desktop discovery separately.

## Downstream adopter migration

Update adopters only under their authorized project scope. First inspect their
recorded template version/full SHA, native source/activation configuration,
project instructions and local modifications. Record a rollback point and
preview the intended source/configuration changes through `update-gz-template`.

For a separate starter checkout, update its origin to the new repository.
**Do not change an application's own origin to the starter repository.** For
adopters, reconcile canonical starter-source links and project marketplace
source URLs while retaining the selected immutable revisions and compatibility
marketplace/plugin IDs. Keep project overrides and user defaults intact.

Historical `.skills-first/bundle.lock.json` source/version/SHA records describe
the actual adopted source. Preserve those records as provenance; do not pretend
the adopter already adopted 0.10.0 or later, or rewrite old exact sources merely
to modernize the name. An actual upgrade records its reviewed target and exact
SHA through the owning workflow. Verify required project behavior and fresh
native discovery before accepting each migration.

Published **0.9.0** retains its old distribution/command contract. Releases
**0.10.0 and later** use the canonical distribution/command with the compatibility
interfaces above. Select a verified published version/full SHA through the
owning update workflow; the completed starter rename and ADR/trio qualification
do not authorize mass adopter edits or certify an individual adopter's migration.

## Coordinated companions

gz-skills and Superpowers Backplane retain their own names, versions and remote
origins. Their active starter policy/source links and handoffs follow the new
canonical repository. Historical receipts and immutable approval/specification
bytes remain intact. No companion release, plugin installation, workflow
implementation or GZKit change is implied.
