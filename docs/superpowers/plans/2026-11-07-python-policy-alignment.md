# Python policy alignment correction

Approved scope: the maintainer directed fixing/alignment across the starter,
gz-skills and SP-BP and reaffirmed the current policy: Python 3.14 unless
X-Plane/XPPython3-bound, then 3.12. This is correction of existing authority,
not a new lifecycle or blanket policy for unrelated portable-skill consumers.

- [x] Preserve existing SP-BP changes; use only standalone canonical source
  checkouts. Leave installed caches and consumer copies untouched.
- [x] Preserve the starter's 3.14/3.12 adopter policy. Update its gz-skills mapping
  to distinguish the selected published release from the corrected candidate.
- [x] Remove gz-skills' competing runtime/tool/package baseline in setup/update
  skills and active guides; resolve project/adopted authority, preserve explicit
  unrelated-consumer policy and report missing/unavailable authority. Keep
  historical receipts and profile schema intact. Exercise baseline/green cases.
- [x] Bind gz-skills' own ordinary Python project to 3.14 and managed exact
  3.14.10; reconcile its declared support range and package metadata through uv.
  Classify the changed pre-1.0 contracts with pending skill/bundle versions.
- [x] Reaffirm SP-BP's independent 3.14 tooling decision and existing 3.14.10
  environment, current source binding and consumer language neutrality. Add
  scoped evidence without absorbing its unrelated release-doctrine work.
- [x] Run each repository's applicable checks, actual managed runtime probes,
  skill structural/behavior checks and installed Python artifact verification.
  Preserve explicit broader acceptance gaps. Review all intended diffs.

No unrelated dependency freshness upgrade, template self-adoption, global
installation, consumer/plugin propagation, tag, release, commit or push is
implied. The unchanged installed release will remain distinguishable from this
unpublished candidate; do not rewrite immutable published sources to hide that.
The backend/resource contract and other engineering migrations are outside this
Python policy correction; do not claim full Astral or native-host acceptance.
