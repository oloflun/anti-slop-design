# CHECKPOINT
agent: claude (Opus 5.5), session b0a224e3
timestamp: 2026-10-03
branch: design-rework-v3
uncommitted files: ~760 (mostly design-catalogue/entries/*)

## Current task
Alunix V3g R9 (`PLAN-ALUNIX-R9.md`, approved 2026-10-03) is built. After that comes the design
audit against the showcase floor and three reviewers (heuristics, critic, a11y).

## Done
- R9 §§ 1–5b in `tests/alunix-r8/runs/V3g/index.html` (backup `index.before-r9.html`).
- Critic fixes:
  - hero NH clip has a single owner
  - pricing lead-cell hierarchy, lede `.5 × headline`
  - tes A optical centre .437, hand-over compressed to .20 of the pin
  - contact gap 32 px, rhythm band before contact removed
  - Calyx step 2 fact error, Calyx nav at < md
- All measured headless at 1440 and 390.
- Name removal from `sites/calyx.html` / `horai.html` (0 hits on `microtext_scan.py --names`).
- showcase-floor § 6 (`scripts/catalogue/showcase_stats.py`); 562 read, 81 skipped, 3 queued.
- GPU/orphan fix in `motion_capture.py`.
- Plugin 1.2.1 built, `sync-from-live --check` in sync, `verify-design-system.py` 206/206 (anti-patterns.md divergence recorded).
- FEEDBACK F-027.

## Status (2026-10-03, end of session)
All of it is done and committed locally as `0199866` (not pushed).

- a11y fixes verified: H1–H3, M1 pris, L1.
- Walks at 1440/768/390 read.
- section_probe: 0 failures.
- browse.html verified.
- Recapture done:
  - collabcapitolium and drinksom read
  - chanel skipped, with the reason logged
- Era 60-frame sheet read.
- Audit: `AUDIT-ALUNIX-R9.md`.

## Waiting for Anton
- The next-round plan (`AUDIT-ALUNIX-R9.md` § 4).
- The git decision on catalogue images.
- Push.
