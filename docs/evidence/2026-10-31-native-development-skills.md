# Native development skill discovery — October 31, 2026

Scope: this starter's macOS checkout, Codex CLI/app-server 0.166.0. The user
explicitly requested native development skill use here. This is development
configuration, not template self-adoption or release acceptance.

The checked-in `.codex/config.toml` enables SP/gz-skills from the published
v0.7.1 marketplace at `27594dbaec853e6bde037b0aaf3f0427a3f053f9`.
Direct Git inspection confirms the native marketplace checkout resolves to that
SHA; `git show SHA:.agents/plugins/marketplace.json | cmp -
.agents/plugins/marketplace.json` confirms matching catalogs. Native plugin state
reports SP 7.0.1 and gz-skills 0.8.0 enabled, Backplane disabled.
The installed Git source HEADs match the catalog exactly:

- SP: `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`.
- gz-skills: `75bcd11ee9371ecff1a7b3432d2af29d4bdbb788`.

The repository update-skill directory is a relative symlink to the existing
canonical template source. No upstream skills were copied or authored, no
adoption lock/profile was created, and no global marketplace was registered.
Native resolution used existing caches without manual plugin-add commands.

A fresh native app-server process used the JSONL `initialize` / `initialized`
handshake followed by `skills/list` with `forceReload: true`. Results from the
repository root and `src/` each report zero discovery errors, 15 enabled SP
skills, 20 enabled gz-skills workflows, and the enabled repo-scoped
`update-gz-template` resolving to `templates/skills/update-gz-template/SKILL.md`.
Backplane skills are absent. This tests runtime discovery, not merely manifests.

An independent fresh app-server launched in `/tmp` reports no SP, gz-skills or
update skill. User configuration SHA-256 before/after the runtime checks is
`0d98c4d0799daaf1c93a473e57b213161a0489906520a98403eea45236b20f8a`.
Existing disabled user defaults were preserved. Runtime metadata labels cached
upstream skills `user`; the outside control establishes project enablement scope.

An initial relative local marketplace source (`.`) resolved at the caller's
working directory and failed from `src/`. The final pinned Git source resolves
correctly from both launch directories. It contains no machine-specific path
and needs explicit reconciliation when the development catalog is updated.

Desktop skill-picker refresh and model-visible invocation in a fresh desktop
chat remain UNKNOWN. Restart the client/open a new project chat to check them.
Windows Git symlink materialization and other hosts remain UNKNOWN. No broader
Backplane readiness, workflow correctness or release acceptance is implied.

The operator additionally required repository/project-scoped installation as
the adopter default, prohibiting global/user installation. Internal/adopter
instructions and native guides now require project-owned registration and
activation. Unscoped Codex install and Claude marketplace-add examples were
removed. Codex 0.166.0's install/marketplace-add help exposes no project-scope
option; the verified path uses project configuration and native resolution.
Claude project marketplace registration remains unverified; its guide requires
scope verification and retains explicit `--scope project` plugin installation.

Repository verification passed with required uv 0.13.5 and managed Python
3.14.10: regenerated packaged adopter instructions, locked all-group sync, all
four routine hooks (Ruff check/format, ty, unittest), bundle/both-catalog
validation, source-independent build, isolated installed-distribution checks
and `git diff --check`. Analyzer implementation and pins are unchanged; deeper
release acceptance was not performed. Changes remain uncommitted/unpublished.

## Subsequent live-state correction

The earlier 36-skill/0.8.0 result above is a historical observation. On recheck,
the native installed path has changed to `gz-skills/0.8.3`, whose Git HEAD is
`d6acc26e28ca1c4f43e5bb46d8973021d7d006c3`. Native plugin inventory still
declares source ref `75bcd11ee9371ecff1a7b3432d2af29d4bdbb788` (0.8.0), so
the advertised ref does not establish actual installed content. The scoped
`codex plugin marketplace upgrade skills-first-starter` reports already up to
date and leaves the discrepancy. No manual cache edits or deletions were made.
Final exact-pin discovery is UNKNOWN pending native source reconciliation.
The user configuration hash remains the recorded value above.

An attempted desktop inspection through Computer Use was rejected because that
tool is not allowed to access the Codex app. Desktop picker acceptance remains
UNKNOWN; this restriction is not a reason to change installation scope.

Claude Code 2.1.316 CLI help confirms `--scope project` for marketplace-add and
plugin-install. The guide now provides explicit scoped commands. This is syntax
verification, not end-to-end Claude installation or workflow acceptance.
