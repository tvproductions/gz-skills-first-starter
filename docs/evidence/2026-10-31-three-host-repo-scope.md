# Three-host repository scope — October 31, 2026

The operator requires project-owned selection, activation and commands on
Codex, Claude Code and OpenCode. Existing global/user installations may remain.
No global uninstall or user-wide activation is authorized as a repair shortcut.
This receipt covers native macOS CLI scope, not desktop UI or workflow correctness.

The candidate is unreleased template 0.8.0, based on starter commit
`fc9cdd2b671f7af7e45fddaa1ac2739c75bb2281` plus the reviewed working-tree changes. Component/runtime/tool pins
are unchanged. The fixture catalog is published 0.7.1 at
`27594dbaec853e6bde037b0aaf3f0427a3f053f9`. Initial fixtures were configured
before the candidate metadata bump; they are scope probes, not published 0.8.0
adoption receipts. Tests exercise the final candidate independently.

## Implemented contract

- `configure --host codex|claude|opencode` writes the selected host's project
  settings and native update-skill discovery path. Omitted host retains Codex.
  Non-Codex locks record additive `host`; legacy locks retain Codex semantics.
- `localize --host` previews/applies project-only activation repair. It reads
  inherited Codex/Claude plugin identities, suppresses duplicate sources locally,
  repairs Claude project/local layers and adds OpenCode local ID controls before
  exact package targets. It preserves user settings/installations and adoption
  records, uses adopted component pins when recorded, and preserves unrelated
  settings. JSONC comments and unrelated source bytes are retained.
- The helper never invokes native installers. Native installation, version
  updates and enablement remain separate. Codex `plugin add` and OpenCode
  `plugin add/remove` are not project repair commands. Claude installs use
  explicit `--scope project`. Backplane remains disabled/omitted.

## Native observations

Disposable Git projects under a task-specific temporary directory selected
each host, plus an outside control. The starter itself also carries scoped
development settings for all three hosts without a self-adoption lock/profile.

| Host | Inside project | Outside control | Limits |
| --- | --- | --- | --- |
| Codex CLI/app-server 0.166.0 | Fresh JSONL initialize/initialized then forceReload skills/list: 36 starter entries, no errors | Zero starter entries | Fixture trust supplied only as a session override using the canonical `/private/tmp` path; user config unchanged. Actual gz-skills cache is 0.8.3 despite declared 0.8.0; exact-pin acceptance fails separately. |
| Claude Code 2.1.316 | Both native `plugin install ... --scope project --json` commands succeed. Inventory reports project scope, enabled inside, SP 7.0.1 and gz-skills 0.8.0. Starter checkout also installed at project scope. | Same scoped install records report disabled outside | Cache/installation registry is user-owned storage; effective activation is project-owned. Fresh desktop/model skill invocation remains unverified. |
| OpenCode 2.2.0 | Persistent native server reports active SP/gz-skills package targets at the exact pinned SHAs; skill API reports 15 SP, 20 gz-skills and the project update skill | Zero starter entries; user config has no plugin additions | Initial short-lived standalone list returned empty while missing packages installed in background. Persistent server plus subsequent state establishes loading. Desktop UI remains unverified. |

The Codex session trust override was tested as a full `projects={...}` object;
an earlier dotted override with `/tmp` was ignored and left project settings
disabled. That failed attempt is not discovery acceptance. No persisted trust
entry was added for disposable fixtures.

OpenCode source targets:

- SP: `git+https://github.com/obra/superpowers.git#2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`.
- gz-skills: `git+https://github.com/tvproductions/gz-skills.git#75bcd11ee9371ecff1a7b3432d2af29d4bdbb788`.

Native API `/api/plugin` reports both active; `/api/skill` resolves their actual
package paths. The starter's project-local exclusion/target ordering also loads
both adapters. No copied upstream skill tree or custom OpenCode adapter was added.

## OpenCode brownfield correction

A second fixture inherited a local gz-skills 0.8.3 plugin from an ancestor's
configuration and selected the pinned 0.8.0 adapter in the child project.
OpenCode 2.2.0 loaded the inherited source first and marked the project package
`failed` with `Duplicate plugin ID: gz-skills`. The skill path resolved to 0.8.3.
ID exclusion followed by a new target does not fix this: the versioned native
[supervisor source](https://github.com/anomalyco/opencode/blob/v2.2.0/packages/core/src/plugin/supervisor.ts)
keys package generations by source target but activation by ID, retaining the
first duplicate. Plain project configuration is therefore insufficient for this
brownfield case; the earlier clean-project result does not prove it.

`run-opencode` uses native environment options from the versioned
[server startup](https://github.com/anomalyco/opencode/blob/v2.2.0/packages/cli/src/server-process.ts):
project config directory, explicit repo file, disabled ancestor config discovery,
in-memory user preferences without inherited plugin declarations, and a private
server. Project skill directories are restored as explicit native skill sources.
It changes no host application code, writes no user settings, and stores no
copied preferences or secrets. Global plugin copies remain installed.

The isolated native server reports both project package targets `active`, at the
requested full SHAs, in the same inherited-source fixture. No duplicate failure
remains. The native source was inspected read-only; no OpenCode rewrite or fork
was performed. Ordinary user preferences survive where not overridden by project
settings; system-managed policy remains native authority. Agents MUST use the
scoped launcher on 2.2.0 instead of asserting plain startup has correct precedence.

## Preservation

User configuration snapshots remain unchanged through project repair and native
inside/outside checks:

| User file | SHA-256 |
| --- | --- |
| Codex config | `0d98c4d0799daaf1c93a473e57b213161a0489906520a98403eea45236b20f8a` |
| Claude settings | `73edc9d05922855bb96ab8b3d92755277c8ad9a6f450c5d445d8997576db8cb8` |
| OpenCode config | `35add636ad16ebb8d27a80ac80a546d3f2d29939b967cca94af88971edcb5979` |

The OpenCode snapshot was taken after initial read-only native inventory and
before scope repair; Codex/Claude snapshots predate installation. Native caches
and Claude's install registry gained project installation records as expected.
No user settings were rewritten and no existing installation was removed.

## Acceptance boundaries

Final repository gate passed with required uv 0.13.5 and managed Python 3.14.10:
locked all-group sync, all four routine hooks (59 unittests), bundle/both-catalog
validation, source-independent build and isolated installed-wheel checks for
all host configurations and scope repair. Explicit Ruff C901 passes. Generated
resources match their authorities. The owning `uv lock` update changes the
candidate's own version and adds registry wheel metadata for the existing Grimp
3.18 pin; no dependency versions were refreshed. The Python implementation uses
the existing stdlib JSON/TOML facilities; no new runtime machinery was needed.

The final scoped OpenCode launch in this starter resolves both exact package
targets and the project update skill. Temporary private test servers were
stopped. User-setting hashes remain the recorded values. Changes are uncommitted
and unpublished; this is change verification, not full release acceptance.

Local scope is established for the tested native clients. Codex's actual
gz-skills cache revision mismatch remains an explicit failure of exact-pin
acceptance; an advertised ref cannot prove installed bytes. This work does not
waive that failure, Backplane readiness, cognitive qualification or broader
release/adoption requirements. Desktop UI, Windows/Linux hosts, paid model turns
and combined-stack workflows remain unverified. No tag/release was published.
