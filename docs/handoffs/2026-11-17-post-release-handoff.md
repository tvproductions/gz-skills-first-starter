# Fresh handoff after 0.11.1 publication — November 17, 2026

## Resume point

**The requested 0.11.1 release and roadmap reconciliation are complete.** The
maintainer then requested “create handoff and git sync”. This handoff records
that completed work and updates continuation pointers; it selects no new feature,
architectural decision, dependency migration or release target. Resume with the
next explicitly selected work after rechecking live repository state.

Do not reopen the completed canonical rename, mandatory ADR-practice delivery,
application-foundations implementation, design edition 3 or ADR-0002 edition 2
approvals. The [reconciled roadmap](../../ROADMAP.md) distinguishes delivered
work from the remaining backlog. The
[previous foundations handoff](2026-11-16-application-foundations-design-handoff.md)
preserves the design/approval/execution history, including its older superseded
checkpoints; it is no longer the active resume point.
The earlier [ADR-practice save point](2026-11-08-adr-practice-save-point.md)
remains implementation history.

## Verified release and source state

- [GZ Starter 0.11.1](https://github.com/tvproductions/gz-starter/releases/tag/v0.11.1)
  published at **2026-11-17 09:21:50 UTC**, nondraft and nonprerelease.
- Release source: **`041c1989406c1b9c4978042661c2dd38ff1db160`**.
  Annotated tag object: `1aa29e6fe24214a7ce85073fc599da84169cea82`.
  The remote tag peels to that release source; never move it.
- [Exact release-source CI](https://github.com/tvproductions/gz-starter/actions/runs/44054657062)
  passed both `checks` and `xplane-baseline` before tagging.
- Downloaded tagged source matches `git archive` for **216 entries**, including
  both symbolic links. ZIP SHA256:
  `2e8ba788febb9032c8bff5c399eca30fe15a5fee0d19a3582125e352ae90439c`.
- The single publication-result follow-up is main
  **`e645fb356e789000cccc3918b8e5bcc74e6adb1c`**. Its
  [exact-commit CI](https://github.com/tvproductions/gz-starter/actions/runs/44055392126)
  passed both jobs. This handoff starts from that clean main, equal to freshly
  fetched origin (**0 ahead / 0 behind**).

The [release receipt](../evidence/2026-11-17-0.11.1-release.md) records verified
publication, conditional acceptance and the distinction between release source
and its documentation descendants. Preserve earlier immutable releases too.
This handoff's own commit/push and exact CI are reported with the sync result;
do not create a CI-receipt-only follow-up chain.

## Completed work and version decision

Release **0.11.0 -> 0.11.1 / patch** corrected obsolete backlog entries and active
release/continuation pointers. The canonical repository/folder/distribution/CLI
rename and mandatory ADR practice shipped in 0.10.0; the 15 naming/layout topics,
application foundations, path-space rejection and reference fixture shipped in
0.11.0. Broader enforcement and real-adopter migration remain separate work.
The patch adds no runtime behavior or adoption requirement.

Version decision for this request: retain published **0.11.1** and its verified
mirrors. A fresh handoff of the completed release and ordinary Git sync introduce
no new product/release scope; no subsequent version is selected. Bundle,
pyproject, local lock entry, runtime output and packaged bundle agree on 0.11.1.
The changelog already records the governing patch; preserve its released entry.

## Environment, freshness and verification

Actual tools for the completed release: **uv 0.13.8**, managed **CPython 3.14.10**
on macOS ARM64; the independent host-reference family remains **3.12.16**.
Keep minimum-only uv **>=0.13.5**, exact Python pins and locked package selections.

The [same-day candidate-specific freshness receipt](../evidence/2026-11-17-0.11.1-dependencies.json)
covers **77 registry projects**, both Python baselines, components, CI Actions,
catalogs and native bindings. All selected packages match latest non-yanked
stable releases; current approved-family patches are 3.14.10/3.12.16. Python
3.15.2 is outside the approved N-1/embedded-host families. Both exact-lock security
audits cover **75 registry packages**, with zero known vulnerabilities and zero
skipped packages. No dependency/tool selection changed in 0.11.1.

SP **7.0.2**, gz-skills **0.13.0**, and disabled Backplane **0.3.0** retain their
verified exact sources. Both catalogs and Codex/Claude/OpenCode project source,
activation and inherited-duplicate overrides remain unchanged. Configuration
does not prove fresh-session discovery.

All four routine hooks, 95 unittest methods, catalog/resource/lock checks,
source-independent build and isolated installed behavior passed for the release;
its CI and the publication follow-up's CI passed on their exact SHAs. Same-day
source-identical deeper analyses retain their bounded evidence under the
[verification policy](../engineering/verification-policy.md).

This handoff/pointer edit is documentation-only: review its diff and local
references, preserve normal hooks and reuse those unchanged-input passes. Do not
invent behavioral tests, repeat analyzer/platform qualification or migrate tools
for this save point. Observe this handoff commit's own CI after the ordinary push.

Observed handoff checks: **108** local references across the five changed files
resolve; all **14** recorded freshness-input hashes are unchanged. Four static
version mirrors and the actual CLI report **0.11.1**; actual tools remain uv
0.13.8 / managed CPython 3.14.10. The reviewed diff has no whitespace errors.
Final exact-commit CI and branch/worktree alignment follow in the sync response.

## Remaining work and limits

Keep these unselected items in the existing roadmap authority:

- Broader Ruff/ty enforcement, majority-rule quota and 14-finding remediation;
  delivered guidance/path rejection does not implement that deferred patch.
- Authorized real-adopter pilot, with FDAU the proposed candidate: adoption,
  subsequent template upgrade, preservation, rollback and actual discovery.
- Deterministic three-way template upgrade/conflict handling and rollback tooling.
- Remaining desktop/Windows/other-host/model proof and actual embedded XPPython3
  operation; standalone Python 3.12 tooling is not simulator/plugin proof.
- Independently inspectable adoption acceptance, the final planned feature before
  a separately scoped 1.0.0 with a newly written PRD.
- Management sidecars/commit metadata: existing design, schema, Backplane mapping,
  recovery and applicable ADR work remain unresolved.

Cognitive-engine [issue #1](https://github.com/tvproductions/gz-starter/issues/1)
remains open and unscheduled. Record **DEFERRED / measurement UNKNOWN**, ceiling
15, until delivery and independent qualification. Backplane remains disabled
pending readiness, combined-stack evidence and explicit adoption. Cohesion is
adopter-owned; retain all native/embedded and wider interface limits. Acceptance
is conditional, never full strict conformance. Python remains the only supported
language baseline. Select future work and its bounded release scope before
implementation; preserve separate approval of actual new/replacement ADR editions.

## Git and authorization

Work directly on main, preserve unrelated changes and normal hooks, push
ordinarily, verify remote SHA equality and observe both jobs for the final SHA.
The earlier email-privacy push rejection was repaired by changing only an
unpublished commit's identity. Use the established public identity for this
authorized sync without changing global/account settings:

```bash
git -c user.name=Jeffry -c user.email=2949663+ahuimanu@users.noreply.github.com commit -m "Save post-0.11.1 handoff"
```

This request authorizes the handoff and ordinary sync. The prior publication
request is fulfilled; no additional tag/release, native plugin installation,
Backplane activation, companion mutation or real-adopter migration is selected.
