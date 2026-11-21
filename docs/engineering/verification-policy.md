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

Follow SP's applicable development workflow and its verification-before-completion
discipline. This policy supplies the project-specific check scope: execute each
selected command completely, with fresh output and its real exit status, before
claiming the result. The full selected command need not be every repository check.
Small reversible work can update an applicable existing plan briefly. Select
independent review, negative controls and build/installed proof for the changed
boundary and its consequences; retain stronger evidence where the owning workflow
requires it. Preserve separate approval for actual new architectural choices;
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
hand. Earlier results may support unchanged areas when their inputs and scope
remain applicable; cite their date and exact inputs as historical evidence.
They do not establish a fresh execution or a current completion claim. Run the
selected checks freshly for the current change and claim; repeat other checks
when their relevant inputs or risk change. Documentation-only closeout uses
fresh diff/reference checks and may cite earlier code-test evidence by date.
Record scope, rationale, commands, results and important limits concisely in
existing records. Never describe a focused pass as a complete workspace pass.

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

## Starter checkout gates

For a full starter integration or release checkpoint, sync all groups when the
environment state requires it, then run the four-hook, catalog and
installed-artifact gates from the repository root:

```bash
uv sync --locked --all-groups
uv run --locked pre-commit run --all-files
uv run --locked gz-starter validate
uv build --no-sources
uv run --locked python tools/verify_distribution.py
```

Keep the approved routine hooks limited to Ruff check, Ruff format, ty and
unittest. For an analyzer change, explicitly run the checker CLI tests covering
counting, portability, cognitive qualification and consumer gates:

```bash
uv run --locked --group hygiene python -m unittest discover -s tools/engineering -p "test_*.py" -v
```

For bundle changes, verify component pins and both marketplace catalogs. After
changes to any wheel-resource source (the bundle, either catalog, the adopter
fragment, the update skill or the architectural-decision policy), run
`uv run --locked python tools/package_resources.py`. Check parity with
`uv run --locked python tools/package_resources.py --check`. The unittest suite
also detects resource drift. Verify configuration, installed revisions, actual
native discovery and Backplane readiness separately.

## Starter Git synchronization

Work and commit directly on `main`. Do not create feature branches unless the
maintainer explicitly requests one. Preserve unrelated work and normal hooks.

When the user requests Git sync, follow this repository-owned procedure whether
or not gz-skills is installed or discoverable. An available upstream workflow
may assist; its absence does not excuse skipping these steps. Follow the user's
requested branch/PR scope. A local commit alone is not a completed sync.

1. Read project instructions and the current handoff. Inspect branch, worktree,
   staged/unstaged changes and upstream. Fetch the intended remote and inspect
   divergence before integrating changes. Preserve unrelated work; resolve
   relevant conflicts without destructive resets or force pushes.
2. Review the complete intended diff, including new files. Reconcile metadata,
   locks, catalogs and packaged copies when affected. Update changelog/handoff
   for meaningful behavior, policy, verification results and unfinished work.
   Stage only the reviewed scope; do not sweep unrelated files into the commit.
3. Use uv satisfying the checkout's minimum and the managed pinned Python.
   Do not replace a supported uv merely because it differs from CI's tested
   selection. If machine uv is below the floor, use a supported version through
   `uv tool run --from uv==<supported-version> uv ...`; record the actual version
   and ensure nested hooks resolve that selection. Run the repository gate and
   applicable changed-tool/analyzer checks. Keep the four routine hooks intact;
   do not bypass failing checks. For documentation-only edits, run fresh diff/
   reference checks and cite unchanged owning results by date and inputs as
   historical evidence; add no ceremonial tests. Keep the required integration gate.
4. Commit the reviewed changes with the normal hooks enabled. Push the intended
   branch using an ordinary push. If the remote advanced, fetch, reconcile and
   rerun affected checks before retrying; never overwrite remote work.
5. Verify remote branch SHA equals the intended local commit and observe CI for
   that exact SHA through completion. A prior commit's green run is insufficient.
   Fix failures within scope and repeat affected verification. If observation is
   unavailable, report CI as unverified rather than calling the sync fully
   verified. Recheck the final SHA after any evidence follow-up commit.
6. Confirm local/remote alignment and inspect the remaining worktree. Report
   branch/commit, push status, exact-commit CI link/result and any remaining
   changes or blockers. Preserve material results in the existing handoff or
   evidence record; do not create an endless chain of CI-receipt-only commits.

Report Git synchronization, release acceptance and publication separately.
Sync neither runs every deeper release analysis nor waives missing required
evidence. Known deferred work stays explicit. Do not tag, publish, install
plugins, or modify dependent repositories as an incidental sync action.
