# Template versioning

The initial template version is **0.1.0**. It is recorded in
`bundle.json` as `template_version`, independently of SP, SP-BP and gz-skills
versions and the adopter's application version. `pyproject.toml` mirrors the
version for this starter's helper project; the repository tests check agreement.
An adopter may change its app metadata without changing the starter's identity.

```bash
uv run --python 3.14.8 starter.py version
```

This reports the checkout's declared version, not proof of a published release.
The initial release is
[v0.1.0](https://github.com/tvproductions/gz-skills-first-starter/releases/tag/v0.1.0),
dated October 11, 2026. Its annotated tag identifies the verified release commit.
Earlier development commits were untagged; do not label them as a released
v0.1.0 retroactively. Future publication remains a separately authorized operation.

## Version contract

Use [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for the template's
public adoption contract: CLI commands and outputs, managed-file formats,
preservation/conflict behavior, baseline requirements and project guidance.
During 0.x development, bump the minor version for additions, requirement changes
or adoption changes requiring reconciliation; bump the patch for compatible
fixes and clarifications. Release 1.0.0 only when the intended public contract
and its compatibility guarantees are established. After 1.0, incompatible
contract changes require a major bump, compatible additions a minor bump and
compatible fixes a patch bump. Explain adopter impact even for small changes.

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

1. Select the next version according to the adoption contract. Update
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
