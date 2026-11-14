# Risk-based verification

Maintainer direction, November 14, 2026. Applies to the starter and Python adopters
in both lanes. Keep strong engineering evidence while limiting work to changed
behavior and its plausible consumers. Verification effort must not grow with
unrelated repository history.

## Select scope, not ceremony

| Change | Required local evidence |
| --- | --- |
| Human documentation or comments only | Review the diff and references; no new behavioral tests |
| Bounded CSS, markup, labels or layout | Changed-file checks where applicable, relevant existing tests and invented rendered review at affected widths/formats |
| Owning behavior | Owning seam tests; affected caller/compatibility checks when contracts change |
| Shared interface or rule | Affected owners/consumers; full gate when impact is broad or uncertain |
| Persistence, recovery, security or consequential decisions | A reached-fault regression and evidence for affected effects/consumers; full gate when shared state or uncertain impact warrants it |
| Verification machinery, workspace/tool configuration, interpreter or dependency selection | Full applicable gate once for the coherent candidate |
| PR/main integration and release/migration acceptance | Full applicable gate and evidence for the actual deliverable |

The diff's semantics decide scope. A mixed module named `reporting.py` may also
contain rules or persistence; the filename alone cannot justify a narrow run.
Project-owned hooks must distinguish documentation, affected owners, explicit
focused selections and broad-risk changes. Unknown ownership broadens checks;
invalid selections, empty discovery and failures must not become green results.
Use existing scope options and native changed-file support. Do not build a new
framework or permanent evidence registry just to select a few tests.

Keep Ruff check, Ruff format, ty and unittest as routine check categories. Local
hooks may check changed files and focused modules; CI runs the full gate at
deliberate integration checkpoints, not necessarily every feature-branch push.
Keep tools, configuration, assertions and exit-status rules consistent between
scopes. Full checks remain directly runnable. Dependencies, imports, resources,
packaging and entry-point changes require corresponding build/installed proof;
ordinary presentation edits do not require rebuilding an unchanged workspace.

This policy overrides generic imported workflow defaults demanding a full suite,
fresh design/plan, independent review, negative control or build/install replay
for every edit. Small reversible work can update an existing plan briefly. Use
stronger evidence and independent review when the changed boundary/consequence
warrants them. Preserve separate approval for actual new architectural choices;
routine details within approved decisions do not need another ADR.

## Control test cost and repetition

Before adding a test, name the plausible defect and observable consequence it
catches. Reuse or strengthen an existing owning oracle before adding another
workflow fixture. Do not freeze incidental wording/private structure, mirror an
implementation helper, or duplicate canonical behavior through every wrapper.
Consequential behavior corrections need failure at a stable seam; reversible
wording/style edits can use focused checks and invented visual review.

Reserve complete workflow/render/backup tests for claims needing those effects.
Ordinary policy cases should not regenerate every format or repeat persistence
and recovery. Justify expensive tests by the risk cheaper evidence misses.
Consolidate/remove tests only with evidence that their useful oracle survives;
a broad test-quality audit is separate work, not a prelude to every edit.

Run the full gate once for a coherent integration candidate. When commit hooks
provide that gate, use them as the final run rather than first repeating it by
hand. Reuse passes while relevant inputs remain unchanged; later changes
invalidate only evidence they affect. Record scope, rationale, commands, results
and important limits concisely in existing records. Never describe a focused
pass as a complete workspace pass.

## Session-start freshness is a check

At work-session start, check project dependency/tool/starter/component freshness
against official sources, reusing recent dated evidence where still applicable.
Make one bounded check and flag stale/unavailable results; do not repeatedly
query during the same work. Do not rewrite pins, locks, environments or native
plugin state as a startup side effect, or block unrelated safe work solely
because a freshness source is unavailable.

Migrate in a separately authorized maintenance pass. Explicit maintenance/update
requests still follow the completed-migration binding; startup is an explicit
freshness-only context, not a maintenance request. Use gz-skills for the portable
procedure; add no starter-owned updater, schedule or dependency lifecycle.
