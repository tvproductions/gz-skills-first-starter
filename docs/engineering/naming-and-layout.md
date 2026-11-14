# House naming and Python workspace layout

**Draft proposal, edition 1 — November 14, 2026. Not active policy.**
The maintainer requested this proposal and explicitly selected rejection of
user-selected paths containing spaces. Approval of this draft and any separately
identified architectural ADR is still required before dependent implementation.
The imperative requirements below describe the proposed adopted contract.

This is GZ Starter's concrete interpretation of the cited documentation as read
on **2026-11-14**. The uv workspace and init pages display **2026-11-12**;
ty's configuration/rule-level pages display **2026-11-13**. Each Canonical line
records the review date; a page date is recorded where verified, not invented
for undated pages. Astral defaults, permitted alternatives and house choices
are distinguished. This Python-only contract binds the starter and both adopter
lanes after adoption; it does not impose Python preferences on portable skills,
Superpowers or unrelated Backplane consumers.

## Approach and boundaries

Keep one policy page, root-owned configuration, explicit member metadata and
project-owned verification. Prefer the existing deptry tool plus a bounded
unittest declaration check over a new dependency-management service. Keep
Ruff check/format, ty and unittest as the four routine checks. Keep the other
engineering analyzers on demand. No ledger, new skill or maintenance framework
is introduced. Generic engineering and maintenance remain owned by gz-skills;
the starter currently owns only `update-gz-template`.

The alternative of retaining the tools' varied defaults would not express the
operator's selected consistency standard. Per-member copied tool configurations
would create drift; root ownership with verified discovery avoids that. This
proposal follows the operator's role-folder choice instead of imposing a
`packages/` folder because it appears in an upstream example.

## 1. Distribution and project folder names

Name each owned distribution in lowercase kebab-case, for example
`bird-feeder`. Give its project folder the same name. Require ASCII letters,
digits and single internal hyphens, starting with a letter and ending with a
letter or digit. Check normalized distribution names for collisions.

PyPA permits additional spellings and normalizes case and separator runs for
comparison; it does not require every source folder to be kebab-case. The
folder/name identity is a house rule supported by uv's project examples.
Do not rename generated wheel filenames, which follow their own specification.

Canonical: [PyPA names and normalization](https://packaging.python.org/en/latest/specifications/name-normalization/) — checked 2026-11-14.
Canonical: [uv workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) — checked 2026-11-14; page 2026-11-12.
Canonical: [uv init](https://docs.astral.sh/uv/concepts/projects/init/) — checked 2026-11-14; page 2026-11-12.

## 2. Import packages and Python modules

Put each import package under `src/` in snake_case: distribution `bird-feeder`
uses `src/bird_feeder/__init__.py`. Replace hyphens with underscores for the
ordinary mapping. Require the derived name to be a valid Python identifier
that is not a keyword; choose a meaningful distribution name that satisfies
that mapping for a new project. Keep subpackages and modules snake_case. Include `__init__.py`
for these ordinary packages; do not infer namespace-package support from this
example. This house scope uses pure Python and uv_build.

uv_build's default derives the module name by lowercasing and replacing periods
and hyphens with underscores, and permits explicit overrides. The house rule
selects that default over PEP 8's discouragement of underscores in package names;
it is not a claim that PEP 8 forbids them. Ruff N999 checks Python module naming.
Existing public import overrides require a reviewed compatibility migration.
The starter's retained `skills_first_starter` import is such an existing
interface; this draft does not rename it to `gz_starter`.

Canonical: [uv build-backend modules](https://docs.astral.sh/uv/concepts/build-backend/#modules) — checked 2026-11-14.
Canonical: [PEP 8 naming](https://peps.python.org/pep-0008/#naming-conventions) — checked 2026-11-14.
Canonical: [Ruff N999](https://docs.astral.sh/ruff/rules/invalid-module-name/) — checked 2026-11-14.

## 3. Names inside Python code

Use snake_case for functions, methods, parameters, variables and ordinary
attributes; CapWords for classes; SCREAMING_SNAKE_CASE for constants. Give
project-defined error exceptions names ending in `Error`. Preserve Python's
specified special methods and external API spellings at explicit boundaries.
Enable all stable pep8-naming N rules and keep the pinned tool's documented
unittest method handling. Do not broaden ignores merely to silence new findings.

N801–N818 and N999 cover class/function/argument/local/module names, several
mixed-case/import patterns, method parameters and error suffixes. They do not
infer which arbitrary assignment is a constant, or enforce every attribute,
JSON field or command name. Review those remaining conventions explicitly.

Canonical: [PEP 8 naming](https://peps.python.org/pep-0008/#naming-conventions) — checked 2026-11-14.
Canonical: [Ruff pep8-naming rules](https://docs.astral.sh/ruff/rules/#pep8-naming-n) — checked 2026-11-14.

## 4. Commands, subcommands and options

Use lowercase kebab-case for executable and subcommand names and long options.
Organize operational commands as `tool-name area action`, implemented with
nested argparse subparsers. For example, `example-suite report build
--output-dir results`. Use flags for options of an action, rather than encoding
independent actions in mutually exclusive mode flags. Keep conventional
`--help` and `--version` entry points; they need no artificial area/action pair.

The area/action order is the operator's choice. clig.dev discusses both noun/
verb orders; GNU supports consistent long options; argparse provides the parser
mechanism and maps hyphenated options to underscored Python destinations.
None mandates this exact house hierarchy. Do not break existing commands or
aliases silently; inventory and migrate them under the versioning contract.

Canonical: [CLI Guidelines, subcommands](https://clig.dev/#subcommands) — checked 2026-11-14.
Canonical: [GNU command-line interfaces](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html) — checked 2026-11-14; read via direct download after browser timeout.
Canonical: [Python 3.14 argparse](https://docs.python.org/3.14/library/argparse.html#subcommands) — checked 2026-11-14, documentation 3.14.10.

## 5. Environment variables

Use one documented uppercase family prefix for project-defined variables:
`<FAMILY>_<MEMBER>_<THING>`. Use uppercase ASCII letters, digits and underscores;
start each component with a letter. For example, `COB_REPORTS_OUTPUT_DIR`.
Select the family prefix once for the adopter, not independently per member.
Do not rename external variables such as `PATH`, `HOME`, `UV_CACHE_DIR` or
`PYTHONPATH`, or give them unrelated meanings.

POSIX describes the uppercase/digit/underscore spelling of its standard utility
variables and reserves lowercase-containing names for applications. It does
not require uppercase application variables or a family prefix. The requested
uppercase family convention is therefore a house choice; avoid reserved names.

Canonical: [POSIX.1-2024 Base Definitions, chapter 8](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap08.html) — checked 2026-11-14; read via direct download after browser 403.

## 6. Program-owned data keys

Use snake_case for field names in JSON and other project-defined data schemas,
including settings a program writes. Match the Python names that serialize and
consume them. This is a house convention, with no Python or Astral authority
prescribing JSON spelling. Google's JSON guidance instead chooses lower camelCase.

Preserve externally owned schemas, map keys that are data values, protocol
fields and compatibility records according to their actual contracts. Do not
mechanically rewrite native plugin manifests, historical adoption provenance or
third-party JSON. Migrate owned persisted schemas with explicit old/new reading,
conflict handling and versioned evidence before changing their writers.

Canonical: [Google JSON property names](https://google.github.io/styleguide/jsoncguide.html#property-name-format) — checked 2026-11-14; an explicitly different convention, not the authority for snake_case.

## 7. Tool configuration spellings

Use standardized and tool-owned keys exactly as specified. The relevant
pyproject, uv, Ruff and ty compound keys use kebab-case, for example
`requires-python`, `build-backend`, `target-version`, `line-length` and
`python-version`. Tool/table identifiers and project-defined mapping keys are
not subject to a blanket rewrite. In particular, deptry's `known_first_party`
and `package_module_name_map` are its actual snake_case keys. Native schemas
retain their required names. Keep settings centralized in root `pyproject.toml`.

Canonical: [pyproject specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/) — checked 2026-11-14.
Canonical: [uv settings](https://docs.astral.sh/uv/reference/settings/) — checked 2026-11-14.
Canonical: [Ruff configuration](https://docs.astral.sh/ruff/configuration/) — checked 2026-11-14.
Canonical: [ty configuration reference](https://docs.astral.sh/ty/reference/configuration/) — checked 2026-11-14.
Canonical: [deptry configuration](https://deptry.com/usage/) — checked 2026-11-14.

## 8. Reject paths containing spaces

Do not read or write files/folders whose path components contain a space
(U+0020). This includes user-selected paths, project roots, configuration paths,
input files and generated destinations, not only names created by the project.
The maintainer explicitly selected rejection of all such paths in this chat
on 2026-11-14. This is a house restriction, not an OS, Python or Astral limit.

Validate the supplied path before opening it or creating a parent. Resolve
aliases/symlinks and validate the effective target before target I/O; check
existing children encountered during traversal before processing them. Reject
with an actionable path error and leave existing files untouched. Apply the
same behavior through API and CLI seams; quoting the argument does not make it
acceptable. Preserve data contents containing spaces. Do not remove spaces,
rename user files automatically or scan unrelated machine directories.

This deliberately rules out application data under locations such as
`Program Files` or `Application Support`; require an explicitly configured
space-free location. Before activation, audit relevant runtime/resource/cache
paths and existing path contracts on all supported systems. Test supplied and
resolved paths, input/output/parent paths, traversal and no-partial-write cases.
Use invalid path strings as negative controls without writing forbidden paths.
Do not claim this restriction is implemented by Ruff or by this proposal.

Canonical: operator request and explicit follow-up, 2026-11-14; preserved in the
[design intake](../superpowers/specs/2026-11-14-naming-layout-policy-intake.md).
No external standard is claimed as authority for this restriction.

## 9. Skills and their Python code

Give a skill a 1–64 character name using lowercase ASCII letters, digits and
single hyphens, with no leading/trailing hyphen; give its parent directory
exactly that name. Keep the specified `SKILL.md` filename. For Python support,
map hyphens to underscores: skill `report-build` can call module
`report_build` under its documented `scripts/` surface or a project-owned
installed package. If the mapped skill name begins with a digit or is a Python
keyword, prefix the module stem with `skill_`: `3d-layout` maps to
`skill_3d_layout`, and `class` to `skill_class`. Verify the resulting identifier.
The spec governs skill naming, not that Python mapping.
Do not infer a shared runtime dependency or author more starter skills from this
rule. Preserve upstream ownership and identifiers.

Canonical: [Agent Skills specification](https://agentskills.io/specification#name-field) — checked 2026-11-14.
Canonical: [uv module derivation](https://docs.astral.sh/uv/concepts/build-backend/#modules) — checked 2026-11-14.

## 10. Reviewed majority of Ruff and ty rules

Enable more than half of each pinned tool's stable rule inventory, with the
actual enabled set measured after ignores/overrides. Count rules, not families.
Document selected families/rules, justified exclusions and adoption findings.
Move toward more reviewed coverage without enabling incompatible rules or
claiming that rule counts establish code quality. Do not use Ruff `ALL` or ty
`all` as a substitute for review. Keep preview rules separately selected and
exclude deprecated/removed rules from the stable denominator.

Keep tool versions exact in the uv lock/declarations between authorized updates.
At an update, compare the rule inventory and actual selection before accepting
new defaults or new members of selected families. A family selector can expand
on upgrade too. Pinning delays that change until a reviewed tool update; it
cannot remove the need to inspect it. Use unittest, never pytest.

Measured proposal on Python 3.14.10 / uv 0.13.8, Ruff 0.17.5 and ty 0.0.104:

| Tool | Stable denominator | Proposed enabled | Coverage | Current limitation |
| --- | ---: | ---: | ---: | --- |
| Ruff | 815 | 541 | 66.4% | Existing starter selects 227; broader candidate has 14 findings |
| ty | 151 | 134 | 88.7% | Preserve the pinned default active severities explicitly; do not infer consumer acceptance |

Use this reviewed candidate Ruff selection in root `pyproject.toml` after
approval and remediation. N adds all 16 stable naming rules. The complete
[proposed patch](../superpowers/specs/2026-11-14-naming-layout-tool-settings.patch)
also records ty's 151 individual stable severity settings (134 enabled), avoiding
implicit `all`. The patch is not applied to this checkout.

```toml
[tool.ruff]
target-version = "py314"
line-length = 100

[tool.ruff.lint]
select = [
    "E4", "E7", "E9", "F", "I", "UP", "B", "SIM", "RUF", "N",
    "A", "ASYNC", "BLE", "C4", "DTZ", "EXE", "FA", "FLY", "FURB",
    "G", "ICN", "INT", "ISC001", "LOG", "PIE", "PLE", "PLW", "PTH",
    "PYI", "RET", "RSE", "SLOT", "TID", "YTT", "W", "PGH",
]
```

The additions cover shadowing, async hazards, comprehensions, dates, executable
files, annotations/import conventions, logging, Python correctness and safer
filesystem idioms. Stub rules apply where stubs exist. Leave complexity C901
on demand, avoid formatter-conflicting families, and do not select pytest
rules. Documentation/security/deeper tools retain their separate existing
contracts; omitted families are not declared permanently undesirable.
Review the 14 existing findings before activation, especially intentional broad
exception handling at analyzer fail-closed boundaries. Fix or narrowly justify
findings with evidence; do not blindly rewrite boundaries to satisfy a count.

Canonical: [Ruff selection](https://docs.astral.sh/ruff/linter/#rule-selection) — checked 2026-11-14; warns that ALL expands on upgrade.
Canonical: [Ruff rule inventory](https://docs.astral.sh/ruff/rules/) — checked 2026-11-14; actual counts use the pinned executable.
Canonical: [ty rule levels](https://docs.astral.sh/ty/rules/) — checked 2026-11-14; page 2026-11-13.
Canonical: [ty configuration](https://docs.astral.sh/ty/configuration/) — checked 2026-11-14; page 2026-11-13.

## 11. Distinguish uv requirements from the house layout

Document the adopter's member grouping. uv member globs must resolve to projects
with their own pyproject files; its common root-plus-packages example does not
prescribe placement by application/library role. Both roles are supported.
Role or domain grouping is within uv's permitted layouts, not a compatibility
exception. This house policy chooses the role grouping below. Do not nest a
member inside another member's project directory; the cited page does not
establish support for that pattern.

Canonical: [uv workspace membership/layouts](https://docs.astral.sh/uv/concepts/projects/workspaces/) — checked 2026-11-14; page 2026-11-12.

## 12. Packaged root and role folders

Keep the root a real packaged workspace member, with root `src/<root_import>/`.
Put other members exactly one project level under `applications/` or
`libraries/`, spelled out. A member declaring a command in `[project.scripts]`
belongs under applications; a member exposing a reusable API without such a
command belongs under libraries. A command-bearing member remains an application
if it also exposes importable functions. Use subpackages for internal structure,
not nested workspace members. A standalone one-package project needs no empty
role folders or invented workspace members.

```text
example-suite/
  pyproject.toml
  uv.lock
  src/example_suite/__init__.py
  applications/
    example-report/
      pyproject.toml
      src/example_report/__init__.py
  libraries/
    example-shared/
      pyproject.toml
      src/example_shared/__init__.py
      src/example_shared/py.typed
```

```toml
[tool.uv.workspace]
members = ["applications/*", "libraries/*"]

[tool.uv.sources]
example-shared = { workspace = true }
```

Select pure-Python packaged projects using uv_build; do not use extension
modules or bare/no-package projects in this house layout. uv documents other
options, including disabling packaging; they are excluded by this choice,
not unsupported by uv. Existing non-project coordinators in the worked
migrations require explicit reconciliation before policy activation. Preserve
their old evidence as history, not as acceptance of this new contract.

Canonical: [uv workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) — checked 2026-11-14; page 2026-11-12.
Canonical: [uv initialization choices](https://docs.astral.sh/uv/concepts/projects/init/) — checked 2026-11-14; page 2026-11-12.
Canonical: [uv project packaging](https://docs.astral.sh/uv/concepts/projects/config/#project-packaging) — checked 2026-11-14.

## 13. Library typing marker

Ship `py.typed` inside every library's import package and verify that it is in
the built wheel and visible to an installed consumer. uv init --lib provides
this marker; a source file alone is not installed typing evidence. Preserve
public type hints during member moves and validate the actual supported runtime.

Canonical: [uv libraries](https://docs.astral.sh/uv/concepts/projects/init/#libraries) — checked 2026-11-14; page 2026-11-12.

## 14. Shared rules and dependency versions

The workspace shares its lock, resolved Python-requirement intersection and
root uv source definitions (subject to member overrides). It does not inherit
a Cargo-style workspace.package/dependencies/lints table. Give each member its
own metadata and direct dependency declarations. Keep the same declared Python
family and shared external dependency constraints where the family uses them;
review differences intentionally. Update those declarations together, regenerate
one root lock and verify its resolutions. A root uv source maps provenance;
it neither declares a member dependency nor centralizes its version constraint.
Do not use forced overrides to hide incompatible member requirements.

Keep all Ruff and ty settings only in root `pyproject.toml`; do not add member
`[tool.ruff]`/`[tool.ty]` tables or competing tool-specific files. Ruff ignores
pyproject files without its section, then discovers the root configuration.
Ruff otherwise chooses the nearest configuration without implicit parent merge;
its explicit `extend` exists but is not needed in this centralized house layout.
ty continues searching for its configuration above member metadata when its
section is absent. It also merges user-level settings; explicit project rule
severities and recorded effective behavior are needed for reproducibility.
Do not pass pyproject.toml to ty's `--config-file`, which expects ty.toml.

From the root, use the locked environment and installed members:

```text
uv sync --locked --all-packages --all-groups
uv run --locked ruff check --config pyproject.toml .
uv run --locked ruff format --check --config pyproject.toml .
uv run --locked ty check --project .
uv run --locked python -m unittest discover -s tests -v
```

Reconcile the selected dependency groups if the real project has incompatible
ones; do not silently omit a required group. Include every member's test roots
through explicit unittest discovery/aggregation; a root tests directory does
not discover arbitrary member tests automatically. Prove a negative lint/type
control inside an application and a library, including invocation from a member
directory. Verify environment, source roots and installed imports rather than
adding source-path hacks. Inspect Ruff --show-settings for both owners and
observe ty's actual diagnostics; configuration presence alone is insufficient.

Canonical: [uv shared workspace behavior](https://docs.astral.sh/uv/concepts/projects/workspaces/) — checked 2026-11-14; page 2026-11-12.
Canonical: [Ruff discovery/inheritance](https://docs.astral.sh/ruff/configuration/#config-file-discovery) — checked 2026-11-14.
Canonical: [ty discovery/precedence](https://docs.astral.sh/ty/configuration/) — checked 2026-11-14; page 2026-11-13.
Canonical: [ty command-line configuration](https://docs.astral.sh/ty/reference/cli/) — checked 2026-11-14.

## 15. Check each member's declared imports

Every adopter must fail verification when its runtime source imports an external
distribution or sibling member absent from its own `[project.dependencies]`.
Checking only the root dependency union, a shared installation, or successful
imports is insufficient. Check the root package too. Do not mark every sibling
as known_first_party: that would mask a missing member dependency.

Run existing deptry separately against each member's source and metadata,
using root-locked tooling and explicit distribution-to-module mappings where
needed. For example, from the root:

```text
uv run --locked --group hygiene deptry applications/example-report/src --config applications/example-report/pyproject.toml --package-module-name-map example-shared=example_shared
uv run --locked --group hygiene deptry libraries/example-shared/src --config libraries/example-shared/pyproject.toml
```

Keep deptry outside the four routine hooks as already required; run it at
adoption/release acceptance and on demand. Add a project-owned unittest
contract for per-member declarations to the existing routine unittest category,
not a fifth hook. The test must discover root plus the two member globs, parse
all member source imports with stdlib AST (including TYPE_CHECKING branches),
exclude only stdlib and that member's own import package, map external modules
to distributions and sibling modules to their owning member, normalize names,
and compare to that member's direct dependencies. Fail on unmapped/ambiguous
modules, syntax/discovery errors or a zero-member scan; do not treat them as
stdlib or first party. Validate installed metadata and explicit mappings against
member metadata/uv_build overrides. Keep test-only dependencies in a separately
identified test scope, not in runtime allowances. Reject undeclared sibling
imports even when its distribution is installed. Ordinary relative imports
stay within the owning package; cross-package absolute imports need declarations.

Deptry alone does not fully satisfy that literal rule: optional dependencies
can count as declared, and its documented extraction skips some TYPE_CHECKING
imports. Dynamic/plugin imports need an explicit inventory and reached-path
checks. If that evidence is missing, record UNKNOWN and block acceptance of
this declaration-isolation requirement; documenting a gap is not a waiver. Do
not claim arbitrary dynamic-import proof from AST scanning. These are bounded test requirements, not a new CLI,
service, ledger or generic maintenance helper. Their implementation remains
pending in this proposal.

Required acceptance controls: declared external and sibling imports pass;
omitting either fails despite shared installation; an optional/dev-only
allowance cannot authorize a runtime direct dependency; TYPE_CHECKING imports,
unknown mappings, malformed source and missed member discovery cannot silently
pass. On 2026-11-14 the disposable deptry control passed with `packaging` and
`example-shared` declared, and failed with DEP003/DEP001 respectively after
removing both. That proves those two cases, not the additional unittest contract.

Canonical: [uv dependency-isolation limitation](https://docs.astral.sh/uv/concepts/projects/workspaces/#when-not-to-use-workspaces) — checked 2026-11-14; page 2026-11-12.
Canonical: [deptry extraction/configuration](https://deptry.com/usage/) — checked 2026-11-14.
Canonical: [deptry rules](https://deptry.com/rules-violations/) — checked 2026-11-14.
Canonical: [deptry declaration sources](https://deptry.com/supported-dependency-managers/) — checked 2026-11-14.

## Adopter migration proposal

For cob_projects, inventory and propose member-folder moves from snake_case
into `applications/<kebab-name>/` and `libraries/<kebab-name>/`, keeping imports
snake_case under src. Review each distribution name rather than guessing it
from an old folder. Move project-defined environment variables to one COB family
prefix, and migrate owned settings.json fields from camelCase to snake_case.
Update paths, references, scripts, tests and serialized readers/writers together;
handle old/new key conflicts explicitly. Do not rewrite externally specified
schemas or historical evidence. Do not change an adopter as part of this task.

For the starter itself, reconcile retained public import/CLI/native/provenance
compatibility, existing non-project workspace examples, flat legacy commands,
the broader Ruff findings and all path entry points before activation. Replace
inconsistent active guidance coherently only after approval; the existing
published guidance remains in force until then. Refresh instructions/resources
if their authoritative inputs change and run affected consumer/artifact checks.
No downstream conformance follows from publishing this draft.

## Version, acceptance and future maintenance

Published baseline: **0.9.0**. Existing pending candidate: **0.10.0 / minor**.
The naming/layout requirement change is minor-level under the 0.x contract,
including the deliberate path restriction. The current authorization delivers
this proposal only; it does not select its implementation into 0.10.0. The
recommended next scope is the complete bounded contract below alongside the
existing opinionated policy/rename work, subject to the maintainer's scope/design
approval. Reuse a valid pending target rather than bumping per task. Bundle/package mirrors remain 0.10.0; no tag or release is authorized.
The new record-platform architecture is not added to this scope.

For that proposed implementation bundle, include all 15 requirements, starter
policy/instructions/resource reconciliation, tool-setting activation and finding
remediation, path rejection at API/CLI boundaries, root/member declaration tests
and artifact/platform evidence. Exclude downstream adopter edits, the chore
framework, new skills, the cognitive engine and the record-platform design.
The completion gate is the following evidence set for that exact candidate,
not merely merging this proposal.

Before acceptance: approve the policy and any identified architectural ADR,
reconcile existing guidance/instructions, apply reviewed settings, remediate
findings, implement/verify path rejection and member declaration tests, inspect
built typing markers and installed imports, and run the applicable integration
checks on supported platforms. Preserve all four routine checks and existing
cognitive qualification deferral/ceiling; claim no strict cognitive conformance.
The [intake](../superpowers/specs/2026-11-14-naming-layout-policy-intake.md)
preserves the original operator request and superseded preliminary notes.

Future chore hook, guidance only: when an authorized uv/Ruff/ty version update
is detected, re-read the cited Astral pages, compare claims/defaults/rule sets
with this dated policy, and record source dates, differences, adopt/defer calls
and evidence in the existing maintenance authority. How this is tracked and
whether any starter-owned chore skill exists are undecided. Design that boundary
with the current single-owned-skill contract and upstream maintenance ownership;
implement no chore, schedule or new skill from this paragraph.
