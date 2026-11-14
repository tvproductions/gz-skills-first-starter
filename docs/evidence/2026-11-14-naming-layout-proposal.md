# Naming/layout proposal — bounded verification

Observed November 14, 2026. Source base before this proposal:
`54cf1001ba1d7064639575561fe19d83adb79158`, canonical `tvproductions/gz-starter`.
The [policy](../engineering/naming-and-layout.md) and
[tool-settings patch](../superpowers/specs/2026-11-14-naming-layout-tool-settings.patch)
are draft working-tree artifacts, not activated settings or delivered behavior.
The final sync commit containing them identifies the saved candidate.

## Provenance and actual selection

Host uv 0.13.8; uv-managed CPython 3.14.10; locked Ruff 0.17.5, ty 0.0.104
and deptry 0.25.1. No dependencies, root tool settings or native installations
were changed. Temporary configurations and disposable fixture trees were used.
Tools ran from this checkout's locked environment. These are macOS checks,
not three-platform or downstream-adopter acceptance.

- `ruff rule --all --output-format json` reported 815 stable coded rules,
  excluding preview/deprecated/removed entries. Effective `ruff check
  --show-settings` reported 227 current rules and 541 proposed stable rules:
  66.4% of the stable inventory, no unexpected nonstable rule and all 16 N rules.
- `ty explain rule --output-format json` reported 151 stable rules plus one
  preview rule. The pinned stable defaults enable 134 (88.7%); the proposed
  patch explicitly records each of the 151 stable rule severities. No `all`
  selector is used. Warn/error behavior remains failing by default.
- `git apply --check` accepts the proposed pyproject patch without applying it.
  Root version mirrors and lock remain at pending 0.10.0.

## Read-only lint evaluation

`uv run --locked ruff check --select N --output-format json src tests tools
starter.py` reports zero naming findings. Evaluating all proposed rules through
an explicit temporary Ruff config reports 14 findings, listed below. None was
suppressed or fixed in the product to manufacture proposal readiness.

| Location at source base | Rule | Observed finding |
| --- | --- | --- |
| `src/skills_first_starter/cli.py:1` | EXE001 | Shebang is present but file is not executable |
| `src/skills_first_starter/cli.py:358` | PTH101 | `os.chmod()` should be replaced by `Path.chmod()` |
| `src/skills_first_starter/cli.py:359` | PTH105 | `os.replace()` should be replaced by `Path.replace()` |
| `tools/engineering/cognitive_check.py:88` | BLE001 | Do not catch blind exception: `Exception` |
| `tools/engineering/cognitive_check.py:114` | BLE001 | Do not catch blind exception: `Exception` |
| `tools/engineering/cognitive_qualification.py:50` | BLE001 | Do not catch blind exception: `Exception` |
| `tools/engineering/cognitive_qualification.py:101` | BLE001 | Do not catch blind exception: `Exception` |
| `tools/engineering/complexity_check.py:148` | BLE001 | Do not catch blind exception: `Exception` |
| `tools/engineering/evaluate_complexity.py:95` | PLW1510 | `subprocess.run` without explicit `check` argument |
| `tools/engineering/evaluate_complexity.py:124` | PLW1510 | `subprocess.run` without explicit `check` argument |
| `tools/engineering/evaluate_complexity.py:181` | PLW1510 | `subprocess.run` without explicit `check` argument |
| `tools/engineering/evaluate_complexity.py:261` | DTZ011 | `datetime.date.today()` used |
| `tools/engineering/evaluate_cosmic_ray.py:184` | DTZ011 | `datetime.date.today()` used |
| `tools/engineering/test_complexity_check.py:38` | PLW1510 | `subprocess.run` without explicit `check` argument |

Remediate or narrowly justify these during authorized implementation. Review
broad catches as analyzer fail-closed boundaries before altering them. This is a
measured remediation list, not an instruction to blindly accept lint suggestions.

## Configuration discovery controls

Disposable root metadata declared `applications/*` and `libraries/*`. Only the
root held the proposed Ruff/ty settings; member pyprojects contained metadata
without tool overrides. Invocations from each member used the locked tools:

| Owner | Invalid control | Valid correction |
| --- | --- | --- |
| application | N802 and ty invalid-assignment both exit 1 | corrected function/assignment: both exit 0 |
| library | N802 and ty invalid-assignment both exit 1 | corrected function/assignment: both exit 0 |

The type check used the actual managed environment explicitly. The controls
prove configuration discovery for these cases, not installed sibling typing,
all possible user-level overrides, virtual-root conformance or workspace release
acceptance. Real acceptance must repeat owning controls on actual member inputs.

## Per-member dependency controls

The pinned deptry ran on a disposable application's `src` with that member's
own metadata via `--config`, and explicit mapping
`example-shared=example_shared`. Its source imported `packaging` and
`example_shared`. With both distributions declared, it exited 0. Removing both
from the member declaration caused exit 1 with DEP003 for packaging (available
transitively in the shared environment) and DEP001 for the sibling import.
The fixture was removed automatically; no adopter project was edited.

This proves external/sibling positive and negative cases. Deptry's documented
TYPE_CHECKING and optional-dependency behavior requires the additional bounded
project-owned unittest contract proposed in policy section 15. That test is not
implemented. Dynamic-import coverage, strict path rejection, metadata/layout
migration, built typing markers and cross-platform acceptance remain pending.

## Source review and builder review

Each policy Canonical line identifies a primary source read on 2026-11-14.
The uv workspace/init pages show 2026-11-12 and ty configuration/rule-level pages
show 2026-11-13. GNU and POSIX canonical pages were read via successful direct
downloads after browser timeout/403 respectively; Google's current JSON guide
is jsoncguide.html, not the obsolete XML URL. Checked dates are not asserted
as publication dates for pages without a verified update date.

A fresh read-only builder reviewer compared the policy, original 15-point intake
and exact patch. It found two planning questions: whether the proposed new scope
is selected into 0.10.0, and whether an unresolved dynamic-import gap could pass.
The draft now explicitly makes scope selection a future maintainer decision and
sets missing declaration evidence to UNKNOWN/blocking for that requirement.
No human approval, active ADR, implemented enforcement or release is inferred.

## Python 3.14 opportunity assessment

Read the starter's versioned opportunity guide and the official Python 3.14
argparse reference during proposal review. Nested subparsers, AST import walks
and tomllib do not need a new 3.14-only subsystem. The concrete 3.14 gain is
argparse `suggest_on_error` for mistyped area/action choices; propose evaluating
it when the actual CLI hierarchy is implemented, with unchanged exit/failure
semantics and negative controls. Defer enabling it or changing colored help in
this documentation task. No concurrency, compression, template-string or broad
filesystem refactor is justified by these naming rules. Parse declaration-test
fixtures on the actual pinned interpreter and fail closed on unsupported syntax.
Canonical: [Python 3.14 argparse](https://docs.python.org/3.14/library/argparse.html#suggest-on-error) — checked 2026-11-14, docs 3.14.10.
