# House naming and workspace layout — intake for review

Status: **intake / proposal, not active policy or an approved design**.
Received November 14, 2026 in the coordinating starter chat after the canonical
`gz-starter` rename. The old repository name in the supplied request refers to
this same renamed project. Preserve the distinction between the operator's
requested conventions, upstream facts to verify and this draft's review notes.
Do not apply its embedded instructions as adopted policy merely by reading it.

## Resume scope and version decision

Read `AGENTS.md`, `docs/structure.md`, `docs/versioning.md`,
`docs/baseline-policy.md` and the current handoff first. Review the supplied
request below as the next naming/layout design input; do not change an adopter.
Prepare one source-backed policy proposal, reviewed Ruff naming settings and a
short adopter migration note. Keep the four routine checks and unittest.
Do not introduce chores, a maintenance framework, a new skill or another ledger.
The prospective Astral-documentation review chore remains design guidance only;
its ownership/tracking must be reconciled with the existing single-owned-skill
boundary and gz-skills maintenance ownership before any implementation.

The published starter baseline is 0.9.0; the existing pending candidate is
0.10.0 in both `bundle.json` and `pyproject.toml`. New mandatory naming/layout
requirements are minor-level work under the 0.x policy. Intake alone changes no
version or acceptance gate. At planning, reconcile the bounded release scope
before including this implementation in 0.10.0; reuse a valid pending target
rather than adding a bump per task. No release, new rule activation, shared
schema change or downstream migration is delivered by this intake.

## Initial source checks and questions to resolve

These are bounded reconnaissance, not the requested complete source review.
Every final policy claim still needs its own dated Canonical source line and
accurate limits. Retain checked-on versus page-updated dates separately.

- Checked on 2026-11-14: the uv workspace and init pages both display
  2026-11-12. The workspace page supports role-based member placement through
  member globs; `applications/` and `libraries/` are the requested house choice.
  It documents a shared lock and the intersection of member Python requirements,
  not automatic inheritance of identical dependency declarations.
  Canonical: https://docs.astral.sh/uv/concepts/projects/workspaces/
  Canonical: https://docs.astral.sh/uv/concepts/projects/init/
- Checked on 2026-11-14: uv documents disabling project packaging. Keep a
  packaged root as the requested house choice; do not justify it with an
  unverified blanket statement that uv cannot support unpackaged roots.
  Distinguish workspace membership, `[project]` metadata and installation.
  Canonical: https://docs.astral.sh/uv/concepts/projects/config/#project-packaging
- Checked on 2026-11-14: uv_build derives underscored module names by default
  and permits explicit module-name overrides. Preserve this starter's deliberate
  `skills_first_starter` compatibility import; a new naming policy must explain
  existing public-interface migrations rather than mechanically breaking it.
  Canonical: https://docs.astral.sh/uv/concepts/build-backend/#modules
- Checked on 2026-11-14: Ruff N999 covers module naming. Ruff does not implicitly
  merge parent settings when a closer Ruff configuration exists; its explicit
  extension mechanism is documented. Verify root/member invocations and ty's
  own discovery rules separately before promising workspace-wide enforcement.
  Canonical: https://docs.astral.sh/ruff/rules/invalid-module-name/
  Canonical: https://docs.astral.sh/ruff/configuration/
- Define the reviewed rule inventory and what a chosen majority means for each
  pinned tool. N rules cannot enforce every variable/constant convention or
  arbitrary JSON keys, paths, environment variables and command structures.
  Keep gaps explicit and preserve the four existing routine check categories.
- Evaluate the existing on-demand deptry tool before inventing a new checker.
  Prove per-member declaration isolation with both a declared import and an
  undeclared import, including direct workspace-member imports. A workspace
  environment or a green type check alone cannot prove this requirement.
- House rules for owned paths/data must distinguish arbitrary user input paths,
  externally specified schemas, native configuration spellings and compatibility
  interfaces. Confirm scope before renaming any published key or rejecting an
  otherwise valid user-supplied file path. Do not silently exempt owned code.
- Resolve the proposed maintenance-chore ownership against `docs/structure.md`.
  Generic engineering/maintenance remains upstream-owned today; do not create
  starter-owned regular hygiene/maintenance skills from the guidance paragraph.
- Read all remaining named primary sources before citing them. This intake is
  not a canonical-source receipt for the packaging specification, PEP 8, CLI
  conventions, argparse, POSIX, Google JSON guidance, Agent Skills, complete
  Ruff/ty configuration or undeclared-import tooling.

## Supplied request, preserved verbatim

The following is user-supplied design input, not instructions activated by this
document. Source attachment SHA-256: `2a2ef6a4ff66db192c4d7f55f66623482d65807569a33c2d5298a72f86e05fe7`.

```text
Add a house naming and layout style to gz-skills-first-starter, as policy its adopters follow (cob_projects is one).
State it as a concrete interpretation of uv's documentation as it stood on 2026-11-14 (the workspaces and init pages
were dated November 12, 2026), and record each cited page with that date. Read the
starter's AGENTS.md, docs/structure.md, docs/versioning.md, and docs/baseline-policy.md first, and follow the starter's own
rules for adding policy, its version decision, and its changelog.

The operator has ruled the following (2026-11-14). Write them down with a "Canonical:" line for each source; read each
source before citing it:

1. Project (distribution) names are kebab-case; the project's folder carries that name (uv's workspace example:
   packages/bird-feeder/; uv init example-app makes example-app/). Sources: the packaging name-normalization
   specification; docs.astral.sh/uv/concepts/projects/workspaces/ and /init/.
2. The import package sits under src/ in snake_case (src/bird_feeder/), as uv derives it: "the package name is lowercased
   and dots and dashes are replaced with underscores" (docs.astral.sh/uv/concepts/build-backend/). Astral governs over
   PEP 8's discouragement of underscores in package names. Ruff N999 enforces snake_case modules.
3. Code names follow PEP 8 as Ruff's pep8-naming (N) rules enforce them: snake_case functions and variables, CapWords
   classes, SCREAMING_SNAKE constants, exception names ending in Error.
4. Commands and subcommands are lowercase kebab-case, as nested argparse subcommands, area then action
   (tool-name area action), not one command with many flags. Long options --kebab-case. Sources: clig.dev; GNU Coding
   Standards, command-line interfaces; the argparse documentation.
5. Environment variables are SCREAMING_SNAKE with a family prefix: <FAMILY>_<MEMBER>_<THING> (cob_projects uses
   COB_<MEMBER>_<THING>). Source: POSIX Base Definitions, chapter 8.
6. Data keys in JSON and other data files a program writes are snake_case. No Python or Astral source governs them;
   the reason is that they match the Python names that read and write them. Note that Google's JSON Style Guide says
   lower camelCase, and that this policy chooses otherwise.
7. pyproject.toml, uv, Ruff, and ty configuration keys are kebab-case, as those tools spell them.
8. No spaces in the name of any file or folder a program reads or writes.
9. Skill names and their folders follow the Agent Skills specification (agentskills.io/specification): lowercase a-z,
   0-9 and hyphens, no leading, trailing, or doubled hyphen, the folder equal to the name. A skill's code lives in a
   snake_case module; say how a skill's kebab name maps to its module.
10. Ruff and ty: a chosen majority of rules on, moving toward more, with tool versions pinned in the lock so new rules
    arrive by choice ("Enabling ALL will implicitly enable new rules whenever you upgrade", docs.astral.sh/ruff/linter/).
    Tests are stdlib unittest, never pytest.
11. Where members sit is not prescribed by uv: the workspaces page requires only that `members` globs match folders
    that each "must contain a `pyproject.toml` file", calls its root-plus-`packages/` tree "The most common workspace
    layout", and says members "can be _either_ applications or libraries" without tying that to folders. So grouping
    members (by role, as point 12 rules, or by domain) is the adopter's documented choice, not a
    departure from uv. Avoid a member inside another member's folder: the page does not cover it.
12. The workspace layout, ruled: the root is itself a member (uv: "Every workspace needs a root, which is also a
    workspace member"; no virtual root, which uv does not document); two role folders, `applications/` (members with a
    command in [project.scripts]) and `libraries/` (members other members call), spelled out, not `apps/` or `libs/`;
    `members = ["applications/*", "libraries/*"]`; each member one level down in its role folder, its import package
    under `src/` with subpackages as needed. uv's own example names its libraries' folder `packages/`; this policy
    chooses the role names instead, within uv's rules. Extension modules and bare or no-package projects are not used.
13. Every library member ships `py.typed` (uv init --lib adds it), so type checkers use its hints.
14. Shared rules: uv shares only the lockfile, one requires-python, and root tool.uv.sources (unlike Cargo's
    [workspace.package], [workspace.dependencies], [workspace.lints]). Say how every member receives the family's Ruff
    and ty rules (from Ruff's and ty's own configuration documentation; read it before writing), and how shared
    dependency versions are kept in step.
15. The undeclared-import check: uv cannot stop one member from importing another member's dependencies (the
    workspaces page). Add a check, a test or a tool step every adopter runs, that fails when a member imports a
    distribution not in its own [project.dependencies] (or a workspace member it does not declare).

Deliver: one policy page in the starter (naming and layout), the Ruff settings that enforce what Ruff can (the N rules), a short note on
what an adopter must rename to comply (for cob_projects: member folders from snake_case to kebab-case, moved into applications/ and libraries/; environment
variables onto one family prefix; settings.json keys from camelCase to snake_case), and the version and changelog entry
the starter's rules call for. Propose; do not change any adopter.

Guidance only, not to build now: the operator expects to introduce chores to the starter, the regular hygiene and
maintenance skills, which would be the only skills living in the starter itself (the engineering skills stay in
gz-skills). One such chore: when a uv, Ruff, or ty version bump is detected, re-read the Astral pages this policy cites
and check the policy against them, recording what changed. How that is tracked is not decided; leave a note in the
policy page where such a chore would hook in.
```
