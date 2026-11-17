# Bootstrap verification correction — design edition 1

Date: November 17, 2026. Status: **DRAFT; not approved or implemented**.
Governing request: correct the pre-implementation verification deadlock reported
by the maintainer from GZYoke's v0.9.0 adoption. This design concerns starter
verification/adoption, not permission to implement that consumer's runtime.

## Problem and observed cause

The adoption runbook explicitly permits configuring the stack before product
initialization. Its worked hook instead runs unconditional unittest discovery.
The consumer reports documentation, metadata, locks and CI, with no runtime
package, authored Python tooling or Python test assets. The November 17 report
identifies eight unsaved paths and conflicting current instructions/handoffs.
Its native-loading and runtime-design gates remain independent.

An invented temporary checkout with only README and pyproject reproduces the
mechanism on this starter's managed Python 3.14.10:
`python -m unittest discover -v` reports `Ran 0 tests` / `NO TESTS RAN` and exits
**5**. Nothing demonstrates a failed behavioral assertion. Treating that exit
as success globally would also hide genuinely broken implementation discovery.
Portable git-sync guidance now diagnoses applicability but does not supply a
command, adopted hook or migrated instruction contract.

Private consumer reports were inspected read-only. Public fixtures MUST use
invented names/content; do not copy its private handoff or operational material.

## Intended result and boundaries

An ordinary Python implementation project MUST be able to save preparatory
work before its runtime-design approval, after real bootstrap validation.
Report product behavioral testing as **not applicable: pre-implementation**
with the observed artifact inventory and reason. Do not call it a passing
product suite, completed adoption, runtime approval or release acceptance.

Once runtime code, authored executable tooling or test assets exist, meaningful
unittest verification is mandatory. Fail on missing tests, zero discovery,
import/syntax/load failures, assertion failures and wholly skipped suites.
Preserve each project's existing coverage commands, source scope, numeric
thresholds and cadence. Nonempty discovery alone does not establish relevance
or coverage; those remain reviewed evidence and existing owning gates.

No placeholder tests, manual phase flag, allow-empty option, skipped hook,
shell exit suppression, research-only reclassification, Node tooling, product
runtime implementation, native installation or unrelated dependency migration.
Do not introduce a generic lifecycle, acceptance ledger or conformance framework.

## Approaches and proposed choice

1. **Starter-owned installed development verifier — recommended.** Extend the
   existing packaged helper with one command and test it in the starter. Adopters
   pin the verification extra as a development dependency through uv. This keeps
   verifier implementation/tests out of the adopter source tree: its own tests
   cannot accidentally stand in for the adopter's missing runtime tests.
2. **Copy a verifier and its tests into each adopter.** It runs with locked
   Python, but adds separately maintained executable copies, requires migrating
   them together, and needs special treatment to stop verifier tests masking
   missing product tests. Reject this additional ownership/distribution surface.
3. **Document a conditional shell discovery command.** It is easy to copy but
   splits platform semantics and artifact classification across hook/CI/prose;
   it leaves the already-observed drift and Windows behavior insufficiently
   tested. Reject as the supported shared implementation.

The recommendation is an agent proposal, not a recorded human choice.
[ADR-0003 edition 1](../../decisions/ADR-0003-001-own-bootstrap-verification-in-the-starter.md)
identifies the consequential ownership/dependency choice separately.

## Supported executable contract

Add `gz-starter verify --project <root>`. Run it in the adopter's exact managed,
locked Python environment. Its common hook entry is:

```yaml
- id: unittest
  name: unittest and bootstrap verification
  entry: uv run --locked gz-starter verify --project .
  language: system
  pass_filenames: false
  always_run: true
```

Keep the other three hook categories Ruff check, Ruff format and ty. CI executes
`uv sync --locked` and `uv run --locked pre-commit run --all-files`, plus any
existing required project checks. Do not replace a project's richer discovery,
workspace aggregation or coverage checks with a weaker default.

Distribute the verifier through an optional `verification` extra. Declare its
YAML parser explicitly there; use safe parsing, not regex YAML interpretation
or an undeclared transitive import. Retain the base helper's standard-library
runtime. The consumer adds an immutable reviewed released Git source for
`gz-starter[verification]` to its dev group with `uv add --dev`, then commits its
own generated lock. Do not advertise a PyPI release that has not been published,
use a moving branch, install globally, or fabricate adoption provenance. Existing
recorded template adoption and this independently pinned verification tool are
distinct until a full reviewed template migration reconciles them.

Initial support is the ordinary pinned CPython 3.14 project on Windows/macOS,
in either lane. This does not establish support for running the starter's 3.14
distribution inside an embedded 3.12 host. Preserve the separate host exception
and its current verification path; do not broaden compatibility metadata without
actual evidence. Workspaces retain their explicit per-owner discovery and
coverage obligations; unsupported selection/aggregation fails with a diagnostic
rather than silently using one root suite.

## Artifact validation and classification

Before deciding test applicability, inspect the actual repository tree,
including untracked source/test files. Exclude only documented VCS, managed
environment and generated-cache/build directories; do not treat .gitignore as
authority to hide authored implementation. Reject unreadable/ambiguous/symlinked
inputs rather than declaring an empty project. Honor the existing path policy.

Validate the artifacts that actually exist: required project metadata/lock and
exact Python pin, supported centralized tool configuration, native/profile/
bundle JSON/TOML, hook and workflow YAML, declared readme, and local Markdown
references. Run owning lock consistency validation; do not infer consistency
from TOML parse alone. Report checked paths/counts and applicable limitations,
without dumping settings contents or reading operational data/credential stores.
Absent native setup is an adoption gap, not invented proof of native readiness.

Supported bootstrap CI is declarative orchestration of direct `gh`, `git`, uv
and check commands. Migrate the consumer-style inline Python subprocess wrappers
to the tested direct-command example. Arbitrary authored scripts and inline
program logic are executable tooling and MUST have owning meaningful tests;
parsing workflow YAML does not qualify that logic. Hosted CI behavior requires
actual execution, separate from local artifact parsing.

Product modules, standalone scripts, tool modules, extensionless executable
scripts and test assets activate behavioral requirements automatically. A
package=false flag or a stale handoff cannot override observed implementation.
Include a new source file outside the conventional src directory in negative
fixtures. Do not provide user-configurable source exclusions or a manual
pre-implementation selector.

The command has two observable outcomes, neither derived from a manually chosen
stage:

- **Bootstrap PASS:** artifact checks pass and no implementation/tool/test
  trigger exists. Print the inventory and explicit product-test N/A reason.
- **Behavior required:** discover/run the actual configured unittest selection
  with the project interpreter. Require a nonzero executed suite with at least
  one non-skipped successful test and no discovery errors/failures. Preserve
  failure diagnostics/status; never map exit 5 to zero after running discovery.

Allow a documented test start/pattern/top-level selection under root pyproject
for existing valid layouts. Invalid paths, undiscovered test assets, empty custom
load_tests results and unsupported aggregation MUST fail. No arbitrary command
override can turn an echo/no-op into a behavioral result. Preserve existing
coverage enforcement outside or alongside this command at its original cadence.

Static inventory cannot prove test relevance. State that limit; keep coverage
requirements and review of owning assertions explicit. The installed verifier's
tests/dependencies are outside adopter inventory and cannot satisfy its suite.

## Adoption and migration deliverables

Update authoritative verification/Python policy, the generated instructions,
greenfield and brownfield runbooks, worked hook/CI examples and canonical update
guidance together. Explain conditional bootstrap acceptance, pending product
build/installed/coverage checks, and automatic transition to full requirements.
Do not alter upstream portable skills or the user's runtime-design gate.

Give existing v0.9.0 and later adopters executable instructions to:

1. Record the old template/tool sources, current diff, pending paths and rollback.
2. Add the exact reviewed verification development source and regenerate/sync
   the project lock with uv; retain all app dependencies and selected lane.
3. Replace the unconditional unittest hook with the supported entry; preserve
   the other categories and richer existing tests/coverage commands.
4. Reconcile CI with direct commands and the same entry, including private-repo
   authentication before raw git fetch. Preserve exact event-SHA checkout.
5. Reconcile stale AGENTS, generated fragment, requirements and handoffs in one
   reviewed change: supersede the deadlock, preserve historical failed receipts
   and unauthorized-skip history, explicitly retain runtime-design approval and
   other outstanding acceptance gaps. Do not infer an exception from git sync.
6. Run the real hook gate, review the result and diff, then use the separately
   authorized ordinary sync procedure. A local bootstrap PASS is not hosted CI
   success or release/adoption acceptance.

Provide preview/preservation/idempotence and installed-artifact acceptance through
the existing helper's public CLI seam. Do not silently rewrite existing adopter
hooks, CI, pyproject or handoffs during ordinary configure. An explicit migration
uses the documented reviewed changes; do not create a force-adoption path.

## Required acceptance cases

Test the new helper immediately through its public command, using invented
temporary projects and substantive negative controls. No placeholder suite.

| Case | Required observation |
| --- | --- |
| Docs/config/lock/CI only | Real artifact checks PASS; explicit behavioral N/A; no product test claimed. |
| Malformed TOML, JSON or YAML; stale lock; broken local link | Fail before applicability can produce PASS. |
| Runtime package or standalone tooling; no tests | Fail with the triggering path and missing-test reason. |
| Ignored/untracked or unconventional-location source | Behavioral requirements still activate. |
| New verification helper | Its own starter tests exercise validation/classification/discovery failures before shipping. |
| Good code with reached-behavior assertions | Actual owning suite runs and succeeds. |
| Failed assertion, syntax/import error, load_tests exception | Nonzero result and original failure diagnostics. |
| Test file with no tests, empty load_tests, wrong discovery selection | Fail; never bootstrap N/A. |
| Every test skipped / expected failure only | Fail to establish a successful behavioral suite. |
| Bootstrap followed by adding implementation | Same unchanged hook automatically rejects absent tests. |
| Existing runtime coverage failure | Existing coverage gate continues to fail; no scope/threshold/cadence weakening. |
| Unreadable/symlinked input or unsupported workspace | Fail closed; do not hide source/discovery errors. |
| Installed verifier in an adopter | Its own installed tests cannot satisfy missing adopter tests. |
| Existing local configuration/provenance | Preserve additions, lane, native settings, prior evidence and runtime approval gate. |

Execute the acceptance cases and exact supported command/hook on actual macOS
and Windows with pinned managed Python, using a shell-only hosted example and
no Node actions/tooling. Use direct gh/git commands and versioned uv provisioning;
do not wrap routine CLI in Python. Include private-checkout authentication and
exact-event-revision controls. A configured matrix or mocked platform is not
Windows evidence. If no actual Windows runner is available, report that required
acceptance UNKNOWN; do not call the complete correction verified.

Run the repository's full applicable gate, build from sdist without development
sources, and exercise the installed verifier including its YAML dependency.
Refresh packaged authorities and exact-candidate freshness evidence after
implementation. Retain cognitive DEFERRED / measurement UNKNOWN and all unrelated
native/embedded/platform limits.

## Release scope and approvals

Proposed published baseline **0.11.1 -> 0.12.0 / minor**: the correction introduces
a supported verification command/dependency and adoption interface, beyond a
pin-only patch. Fold already-completed, uncommitted 0.11.2 tool maintenance into
this bounded minor; preserve its historical receipt. Do not bump per task.
Reconcile roadmap, metadata, lock, runtime/resource mirrors and changelog after
design acceptance. Current development metadata still records the maintenance
checkpoint 0.11.2; no 0.12.0 implementation/closeout claim is made here.

Included work is this executable bootstrap contract, tests, adopted examples,
migration and actual Windows/macOS proof, plus the existing maintenance batch.
Exclude GZYoke runtime/adopter edits, unrelated roadmap work, native activation,
companion changes and release publication. Publication and Git sync require their
own authority; no design or ADR approval authorizes them.

Before dependent implementation, obtain approval of this design edition 1 and
separate explicit approval of ADR-0003 edition 1. Then write the implementation
plan and implement with reached-fault tests. Preserve actual approval evidence;
do not label this proposal accepted based on the request to correct the defect.

Fresh builder check, November 17: **nothing important left**. The reviewer could
plan the correction without reopening user requirements. Settle the finite
direct-command CI pattern conservatively, reject discovery that omits observed
test assets, preserve richer coverage/aggregation gates and require actual
Windows execution. This is design-review evidence, not human design/ADR approval
or an implementation/platform verification result.
