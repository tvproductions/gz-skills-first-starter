# Application foundations implementation — November 17, 2026

Candidate: working tree based on main 21406c4; no publication or Git sync is
claimed. Governing work is approved design edition 3 and separately approved
ADR-0002 edition 2. The ADR preserves exact reviewed bytes and verbatim approval.
Published 0.10.0 → pending 0.11.0 / minor remains the coherent release target;
bundle, package and project-lock mirrors retain 0.11.0.

The preceding [maintenance pass](2026-11-17-starter-maintenance.md) completed
both baseline migrations. This implementation adds only a local editable
example-foundations 0.1.0 dev package to the root lock; no external registry
dependency selection changes. The maintenance receipt's candidate hashes name
its earlier inputs, not this later implementation. Release preparation must
refresh the actual candidate and applicable deeper acceptance.

## Delivery and ownership

Runtime guidance lives in project-configuration.md and
engineering/application-foundations.md. The naming/layout page reconciles all
15 topics with the approved guidance scope, including web application roles and
portable delivery. The full numbered 1–108 GZKit disposition remains canonical
in the approved design; this implementation links it rather than duplicating a
second candidate inventory. Both-lane baseline/adoption instructions, update-skill
migration guidance and regenerated wheel copies point to the same authorities.
The broader Ruff/ty proposal, quota and 14-finding remediation remain deferred.

| Dispositions | Delivered authority |
| --- | --- |
| 1–10, 15–19, 48–58, 86–90 | Foundation boundaries, models, settings and operator authority |
| 11–14, 22–43 | Existing Python/Astral/dependency/packaging policy; naming topics 1–3, 7, 10–15 |
| 20–21, 44–47, 75–85 | Existing unittest/typing and foundation error/interface guidance |
| 59–63 | Existing on-demand complexity policy and cognitive deferral |
| 64–74 | Path rejection, portable text/files/process guidance and owning controls |
| 91–104 | Real consumer/installed evidence and risk-based verification |
| 105–108 | Source ownership, generated-resource drift and bounded delivery |

The starter inventory identifies actual CLI/native/path responsibilities with no
unused application settings loader. The example is project-owned, src-packaged,
root-dev-installed, independently built from delivered source and absent from the
starter's runtime dependency list. The root sdist owns its source delivery;
the starter wheel retains the existing six resource inputs.

## Observed behavior and scope

| Design acceptance item | Owning evidence |
| --- | --- |
| 1: precedence, omission, replacement, sources | test_application_foundations: precedence/omission, empty env and source diagnostics |
| 2: malformed/duplicate/nonfinite JSON, wrong/unknown keys, schema, explicit absence | Fixture negative cases; no implicit fallback or application writes |
| 3: roots, path bases, service/host, code replacement | Two-root/cwd controls plus extracted-sdist installed CLI/API/reinstall probe |
| 4: redaction and deliberate forwarding | Runtime-generated sentinel tests, safe diagnostics/repr/output and child environment selection; installed wheel and diagnostic checks |
| 5: values, fakes, reached adapter failure, wiring | Pure render test, injected writer fault and actual failed os.replace preserving prior bytes/cleanup |
| 6: actionable warning and informed departure | Worked review in application-foundations.md; accepted project posture is guidance with retained mandatory/ADR authority |
| 7: existing preservation/metadata/catalog/resources/artifacts | Full four-hook gate, validate, source-independent build and isolated distribution checker |
| 8: supplied/resolved/parent/symlink paths, contents, no partial writes | test_path_contract plus fixture pre-read guards, deliberate-read guard control and space-free/content controls |

Path tests were observed failing on the former behavior, including a symlink
target spelling whose spaced component disappeared after parent normalization.
The corrected helper checks supplied, resolved and symlink-target spellings
before target content access. Fixture tests likewise reached invalid-root and
symlink failures before their fixes, and a redacted-but-unhelpful environment
diagnostic was corrected after its CLI regression failed.

Warnings are a design/review workflow, demonstrated with an explicitly invented
operator review. This is not fresh-session model/host behavior qualification.
The helper/fixture do not automate architecture approval or enforce conformance
scores. Missing evidence remains UNKNOWN; accepted departures are not conformance.

## Verification

Actual tools: uv 0.13.8, managed CPython 3.14.10 on macOS ARM64. Locked commands:

- pre-commit run --all-files: Ruff check, Ruff format, ty and unittest pass.
- gz-starter validate: bundle and both catalogs valid.
- build --no-sources: 0.11.0 wheel and sdist build.
- python tools/verify_distribution.py: original installed starter controls and
  the new extracted-source fixture build/install/reinstall/invalid-selection/
  redaction controls pass outside both checkouts.
- python tools/package_resources.py: changed instruction and update-skill
  resources regenerated; existing drift checks pass.

The developer environment is isolated from real application data. Test fixtures
and credentials are invented; sentinels are generated at runtime rather than
committed whole values. The installed probe uses a clean environment without
PYTHONPATH/PYTHONHOME and the actual pinned interpreter. The local dev fixture
has no extra lock, environment or competing tool configuration.

Python 3.14 review: current annotations and the pinned Ruff target preserve the
selected family's idioms, including parenthesis-free multi-exception syntax
where selected by Ruff. No new need justifies template strings, interpreter
pools, Zstandard or replacing existing exclusive-write/recovery primitives.
The independently verified Python 3.12 host-reference baseline is unchanged.

Internal-use boundary: preserve run-opencode's existing interactive-host contract,
including its operator-supplied environment and interactive lifetime, as now
documented in the foundation inventory. This is not a sensitive-variable-isolation
claim. Removing unknown native provider/plugin inputs without compatibility
evidence would change the existing host product contract; operators remain
responsible for supplying only required sensitive values to that native host.

## Independent review and corrections

A fresh independent reviewer examined all uncommitted implementation and
maintenance changes against the approved design and plan. No Critical or Minor
findings were returned. Four Important findings were reproduced and addressed
in one correction pass:

1. Invalid --repeat values leaked through argparse conversion. The new CLI
   regression failed with the sentinel in stderr; conversion now occurs inside
   the controlled error boundary, and the regression passes.
2. Empty --config-root was normalized to the working directory. The new guarded
   CLI test failed by opening working-directory settings; the raw empty input is
   now rejected before Path construction, and the test passes.
3. The installed probe inherited fixture overrides and could replace an external
   output. A task-owned poisoned-parent reproduction failed with changed prior
   bytes. The verifier now removes the entire EXAMPLE_FOUNDATIONS_ prefix before
   injecting task-owned inputs. Its permanent poisoned-config/message/output
   controls and an external poisoned-parent invocation both pass, preserving
   the protected file.
4. Required guard/boundary controls were incomplete. Tests now cover Path.open
   and builtins.open, lexical/resolved aliases, CLI dispatch, no writer/process
   calls, deliberate-read positive controls, size/type boundaries, output equal
   to settings, spaced output aliases and unchanged prior bytes.

The final full four-hook gate passes. The root unittest suite is **95 passed**;
the source-independent build and complete installed-artifact checker pass again
after corrections. The corrected CLI, environment-contamination reproduction
and preservation controls are observed evidence, not inferred from configuration.
Per the execution workflow, fixes were verified by owning tests/full gate rather
than a second independent review.

The reviewer explicitly set aside native/platform qualification, real-adopter
migration, repeated live freshness, deeper release acceptance and publication.
Disposition: retain each as a separately scoped limit or release prerequisite;
none is silently treated as satisfied. No additional design change follows.

Native Windows/Linux execution, real multi-account permissions, embedded hosts
and full TUI/web/desktop delivery remain unverified. Cohesion and other deeper
release checks retain their existing requirements. Cognitive qualification is
DEFERRED / measurement UNKNOWN (ceiling 15); this is no strict conformance or
release-acceptance claim.

## Final candidate identities

- pyproject.toml: SHA-256 4a332ebe53154bd0ae982fdb7dd93a333dff0928487c780d27e54b34f6f7eeea
- uv.lock: SHA-256 ec0f59ef6688adf82b27d5154d0dc51885b4830500cdd5fd88bca45d773e27ab
- baselines/xplane/pyproject.toml: SHA-256 892ee9c871e3328913e1fc225571d8e3145da91e9355212553e30e167a1a64ba
- baselines/xplane/uv.lock: SHA-256 819614ff64eec66101b0ec2b0a0957dc3f4bcbd603d1bfc5e3179a084e678dd7
- bundle.json: SHA-256 5283fb42e4405ef811d8295fae88e3142759ff96699fba9ade1791a425de63fc
- templates/AGENTS.skills-first.md: SHA-256 3c0b6c14f620ff8fbedeeaa798c441390b56da926b3648a56078fbab393584b3
- templates/skills/update-gz-template/SKILL.md: SHA-256 08c3f7a9a6e793055dd12b43cd80970babf638f91cbbf7b3860ce52d04b39997
