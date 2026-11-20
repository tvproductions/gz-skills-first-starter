# Discipline corrections — November 19, 2026

The maintainer's request to address the identified implementation corrections
continues the work after the [completed evaluation](2026-11-19-discipline-evaluation-results.md).
**The sampled adopter binding and declared-verification gaps are now corrected.**
The maintainer subsequently accepted withdrawal of ADR-0004's proposed
enforcement subsystem as exceeding the starter's lightweight scope. The Python
requirement and observed violations remain. No original failure is rewritten
as a pass.

## Disposition

| Correction | Current result | Evidence / remaining gate |
| --- | --- | --- |
| Duplicate selected/inherited SP discovery | Already repaired in producer project configuration | Original fresh root/src/outside controls and full applicable gate remain valid. Pending 0.11.4; no new installation. |
| Fixture trust, resume scope and offline prerequisites | Already corrected in evaluation | Preserve original negatives and corrected actor catalogs. These are runner fixes, not shipped host-product fixes. |
| Evaluator acceptance | Corrected in evidence | Preserve mandatory failures and UNKNOWNs separately from task output. Overall discipline acceptance remains unearned. |
| Codex adopter instruction pointer | **Corrected and retrieved in a fresh session** | Only target/AGENTS.md changes; original authority bytes survive intact. A new target session reads the fragment and reports the required Python invocation and workflow routing. |
| Claude declared verification paths | **Executed successfully in a fresh, explicitly configured session** | All five exact locked commands return successful native results, including all four pre-commit hooks. No candidate files change. |
| Required Python invocation | **Observed violations remain; automatic enforcement not selected** | [ADR-0004 edition 1](../superpowers/specs/ADR-0004-001-python-command-control.md) is withdrawn. Address findings through existing bindings/workflows and evaluate behavior; no new enforcement subsystem is selected. |

## Completed corrective follow-ups

November 20 release-review correction: the Ruff fixture's source was frozen at
November 19 12:12 UTC. Ruff 0.17.6 was published at 15:57 UTC, before the later
verification session. Passing declared commands on fixture-selected 0.17.5 proves
their execution, not live release freshness or completed current-stable maintenance.
Original commands, outputs and hashes remain unchanged.

Three fresh CLI sessions / three turns are recorded in the
[curated observations](2026-11-19-discipline-corrections.json). They are corrective
tests prompted with the known omission, not independent evidence of unprompted
reliability. The original campaign remains 22 sessions / 33 turns; these add
three of each. No failed observation is deleted or repeatedly retried.

The first Codex session uses the existing configured invented adopter. It reads
the owning adoption workflow and appends the fragment link to target/AGENTS.md.
Independent byte comparison confirms that the original file is an exact prefix;
the sole addition is a blank line and the required reference. Every other
candidate file hash is unchanged. Link resolution and the actor's diff check pass.
The helper itself required no change: its contract deliberately preserves existing
AGENTS.md and assigns the additive link to the agent-guided workflow.

The second Codex session starts inside target/ with canonical-path inline trust
and a read-only sandbox. Its native catalog advertises the exact selected SP
7.0.2 and GZ 0.13.0 roots. Command observations show retrieval of AGENTS.md,
AGENTS.skills-first.md and the relevant workflow references. The answer identifies
the lite profile, project-owned operations, SP feature workflow, GZ routing and
`uv run --locked python`. No files change. This proves sampled target instruction
delivery; it does not establish native installation or full adopter acceptance.

The fresh Claude session keeps the earlier migrated Ruff candidate unchanged.
Session-only settings explicitly allow these exact commands, each submitted as a
separate tool call without shell variables, loops, pipes or compound operations:

```bash
uv run --locked ruff check
uv run --locked ruff format --check
uv run --locked ty check
uv run --locked python -m unittest discover -s tests -v
uv run --locked pre-commit run --all-files
```

Native results report passing lint/format/type checks, two passing original
unittests and all four hooks passing. Every permission decision is accepted from
configuration; no command is denied or replaced by a direct binary. The outer
CLI exits zero. Individual numeric exit codes are not emitted in the native tool
records; successful tool results and the actor's reported zeros are retained
without inventing a separate status field. Before/after candidate hashes match.

This repairs the observed verification obstruction under the explicit configuration
and simpler calls together. It does not isolate which change was sufficient or
prove every compound form works. Original denials involved compound/variable
forms; calling them evidence that Ruff itself was forbidden was too broad.
The new session does not retry a denied command in the old session or bypass
sandboxing. No persistent host/user settings are changed.

## Python finding and withdrawn remedy

The rule was already available; another reminder supplies no enforcement proof.
The [Anthropic permission documentation](https://code.claude.com/docs/en/permissions#what-a-bash-rule-doesnt-match)
explains that command patterns have gaps for path and shell-wrapped forms.
The [Codex rules guide](https://learn.chatgpt.com/docs/agent-configuration/rules)
distinguishes prefix matching and host shell handling. Six non-executing native
Codex rule-checker probes confirm only their raw argument matches: the canonical
prefix matches allow, bare Python matches forbidden, and path/shell-token inputs
have no match. They do not execute Python or establish host runtime denials;
the checker invocation does not test the host's shell decomposition or optional
host executable resolution.

The agent proposed a starter-owned classifier and native pre-tool adapters.
During review, the maintainer stated that deterministic hooks and guards
everywhere would defeat the starter's lightweight role, then accepted the
recommendation to withdraw ADR-0004 with “proceed as recommended.” The proposal
turned an observed instruction violation into a new tooling subsystem without
adequate justification. Its ownership, dependency and host-integration choices
are not selected. The original proposal is preserved as withdrawn history.

Return to the evaluation's original scope: clear mandatory policy, upstream
workflow composition, existing native capabilities and truthful verification.
Instruction/workflow changes require affected behavioral evidence before a
correction can be claimed. The available rule and hook observations do not
establish enforcement, and no new experiment or general guard implementation is
selected by this withdrawal.

## Scope, provenance and verification

Inputs remain published starter 0.11.3 at
`309c1a204174d802c69fc7e3c4d65ec236abe121`, SP 7.0.2, GZ 0.13.0 and the
3.14.10 fixture pin. Actual controller uv is 0.13.9; Codex CLI is 0.170.0 and
Claude Code is 2.1.328. Requested models/effort remain gpt-6.2-astra and
claude-opus-5-5, medium; underlying serving snapshots are UNKNOWN. Claude's
selected plugins are supplied through session-only exact-source directories.
Same-day [freshness evidence](2026-11-19-dependency-maintenance.md) is reused;
no dependency update is part of this correction follow-up.

No producer implementation, packaged resource, pin, user configuration, actual
adopter repository, upstream plugin or published artifact changes. The native
actors operate only on invented fixtures. Original source/user-configuration
guard hashes still match; five producer prose files differ from that older guard
through the already recorded evaluator closeout. No new source/user-setting
guard mismatch is observed. Private transcripts are retained by hash; public
records redact local identity/paths and omit upstream skill/policy bodies.

Producer verification is scoped to evidence/design prose: diff/reference review,
JSON parsing/redaction and the independent fixture assertions above.
Closeout checks pass for 123 local links/anchors, JSON structure and privacy,
all three corrective session records, independent assertions and whitespace.
Existing implementation gate evidence is reused for unchanged inputs. Published 0.11.3
-> pending 0.11.4 / patch remains the duplicate-source correction; all development
mirrors stay 0.11.4. ADR-0004 is withdrawn and adds no release scope. No Git sync
or publication is authorized. The Python violations remain unresolved evidence;
overall discipline acceptance remains unearned.
