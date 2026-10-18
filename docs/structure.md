# A template with zero authored skills

This starter authors and distributes **zero agent skills**. It selects and binds
the SP + SP-BP + gz-skills stack through versioned configuration, project
instructions and documentation. SP-BP remains expected, deferred and disabled
until readiness and explicit adoption. Project operational skills remain
project-owned.

The starter reinforces and highlights upstream behaviors so adopters understand
which practices matter here. gz-skills supplies the reusable skills; this template
makes freshness, version-appropriate Python code, portability and project-policy
precedence visible in its instructions and guidance. It adds no parallel workflow.

Zero skills describes ownership, not a neutral or unconfigured template. The
starter deliberately selects uv-managed Python 3.14 (3.12 for XPPython3-bound
code), Astral's Ruff and ty,
unittest and the approved pre-commit checks. Exact verified pins, selected
release families, lockfiles and aligned local/CI targets make dependency choices
reproducible. See [Python policy](engineering/python.md) and the
[configuration contract](project-configuration.md). The required
[Astral contract](engineering/astral-alignment.md) adds `src/` packaging,
centralized Python configuration and necessary adopter refactoring. Pinned ty,
pre-commit and stricter reviewed Ruff rules are configured in this starter;
each adopter must establish its own enforcement and artifact verification.

| Location | Responsibility |
| --- | --- |
| `bundle.json` and native marketplace catalogs | Independent upstream identities, immutable component pins and default activation |
| `src/skills_first_starter/` | Installed helper package, CLI and generated wheel resources |
| `starter.py` | Compatibility launcher for the installed helper |
| `templates/AGENTS.skills-first.md` | Adopter instructions: workflow routing, baseline policy and maintenance obligations |
| `docs/adoption-workflow.md` and `docs/adoption.md` | Adoption procedure and host verification |
| `docs/baseline-policy.md` | Adopter allowed ranges, selection rules and documented constraint reasons |
| `docs/gz-skills-python.md` | Verified upstream Python workflow coverage and project-policy precedence |
| `docs/engineering/` | Python requirements, version-aware design and analyzer contracts |
| `tools/engineering/` | Explicit on-demand analysis utilities and their CLI tests |
| `docs/versioning.md` and `CHANGELOG.md` | Template compatibility, release identity and adopter impact |

There is no starter `skills/` tree or `SKILL.md` package. Configure writes host
configuration, a provenance lock and instructions; it creates no skill discovery
tree. Native managers install upstream skills separately. Existing app skills
and instructions are preserved, and no lite/heavy profile is inferred.

Project instructions route feature work to SP and engineering selection to
gz-skills. Generic maintenance stays in gz-skills `gzs-update-dependencies`;
dependency-risk review stays in `gzs-dependency-risk-audit`. This repository owns
the policy binding and adoption helper, not another skill catalog or generic
dependency updater. Supporting utilities remain ordinary tooling, not skills.

The [baseline policy](baseline-policy.md#code-must-follow-its-python-version)
also requires code to observe relevant idioms and advances of its Python family.
gz-skills owns reusable engineering workflows; the starter sets the runtime and
assessment requirement. That dependency is explicit and versioned. The pinned
Pythonic-pattern skills provide partial coverage, not a complete version audit;
missing capability stays visible rather than becoming another starter skill.

## Maintenance ownership

The starter maintainer publishes reviewed baseline changes and describes their
adopter impact. Each adopter must check template releases, upstream components,
runtime/tool versions and baseline-policy changes at adoption, scoped upgrades
and quarterly on-demand maintenance. Record evidence, adopt/defer decisions,
exceptions and revisit conditions in the project's existing authority.

Checking is distinct from updating. Preserve exact pins after verification;
Python stays current within the approved 3.14.x or host-bound 3.12.x family;
family changes require separate review. An exact patch records a verified run,
not a permanent adopter baseline. Adopters
reconcile template changes against their own app dependencies, overrides,
instructions and native manager state. New template guidance neither silently
waives existing requirements nor automatically migrates a project. Follow
[stack maintenance](adoption.md#maintaining-the-adopted-stack).

## Design precedents

These precedents support the separation of policy, template provenance and
consumer-managed updates; they do not explicitly prescribe zero agent skills.

- [AGENTS.md](https://agents.md/) puts project conventions, build steps and test
  instructions in ordinary agent-facing Markdown.
- [Cruft](https://cruft.github.io/cruft/) records the template commit in a project
  and uses a separate tool for checking and reviewing updates.
- [Copier](https://copier.readthedocs.io/en/stable/updating/) separates template
  evolution from consumer changes and requires reconciliation of conflicts.
- [NIST's Python template](https://pages.nist.gov/cookiecutter-nist-python/)
  selects an opinionated tooling baseline and delegates template updates to
  Copier or Cruft. Its [update guidance](https://pages.nist.gov/cookiecutter-nist-python/ci.html)
  describes update PRs in the consuming repository.

Our application of those precedents is zero starter-authored skills with explicit
policy and adopter-owned review. Their tool choices and scheduling mechanisms
are not adopted here. Existing adopters use the [0.3 migration guide](migration-0.3.md).
