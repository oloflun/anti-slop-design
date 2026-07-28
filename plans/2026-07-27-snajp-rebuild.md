# Plan — Snajp rebuild (snipe-leads) · first end-to-end test of Design System v2

## Scope

Rebuild the `snipe-leads` site under the new design system. This is simultaneously a real deliverable and **the first genuine end-to-end test** of the brand-derivation gate, the 6-hook enforcement chain, and the telemetry report. Both goals matter; if the site ships well but the telemetry is empty, the test failed.

**First action of the build session: read `snipe-leads`' project documentation.** Understand the product properly — the existing leads agent *and* the newer dedicated support agent — before touching the site.

*(Revised 2026-07-28. The original instruction here was to defer reading the docs, so that summarizing them would not water down the design-system plan's context while that system was being designed. The design system is now built and committed, so that reason no longer applies. The gate still derives visual direction from the repo's real evidence at build time; reading the product docs informs **what the site has to say**, which is a different question and one the build genuinely needs answered up front.)*

## The brief (from the user, verbatim intent)

- **Rename** Snipe / Snipra → **Snajp**. More Swedish, more recognizable.
- **Product pivot**: no longer only a leads agent — it now also provides a dedicated **support agent**. Scope of the pivot is in the repo's docs, to be read at build time.
- **What's wrong now**: a very long demo site for the leads agent alone. Too much going on, too much detail. The message needs clarifying and simplifying; the pages need to feel seamless rather than like separate demos.
- **Hero requirement**: a big **Snajp** wordmark with **Leads / Support** beside it. Both clickable, swapping the rest of the page to focus on that offer. This is a real interaction spec and the page's signature moment.
- **The support offer is orphaned**: it lives at `/snajp-support`, unreachable from the landing page. It contains an interactive demo analogous to the leads **email studio** (`email-studio/`, `EMAIL_STUDIO.md`). Surface it through the Support half of the toggle; present **both demos uniformly** (shared frame, controls, motion, label voice); **improve both** — neither is exempt for already existing.
- **Direction**: more modern without losing its soul. **Keep the large fonts** (the confirmed trait to preserve). **Drop the small, thin, descriptive editorial text scattered in the corners.** Target register: **Nordic SaaS**.

## Why this is the right test

Exercises every mechanism at once: Tier 1 derivation against *partial* brand evidence (keep large type, drop corner editorial, rename), the targeted-vs-broad scope rule, the inheritance rule across a multi-page site, component routing on a real interactive control, the copy gate on Swedish and English strings, and the four-breakpoint verification sweep.

**Named traps for this build** — both demoted lanes look superficially right here and must not fire:
- Nordic SaaS is **not** `minimalist-ui`'s Notion palette
- "large fonts, drop the fine print" is **not** `industrial-brutalist-ui`'s hazard-red Swiss grid

Both must lose to tokens derived from Snajp's own evidence. `gates.md` gate 60 treats either skill's hardcoded hex in the output as a contract violation, and every firing is logged as a `trap` event.

## Completed

- [x] Design System v2 built, verified (60/60), committed (`anti-slop-design@1b0c136`)
- [x] Propagated to installer v0.4.0 (`super-intelligence@a6fc48b`)
- [x] Live install upgraded: impeccable v4.0.2, 7 hooks in `~/.claude/hooks/`, 6 registrations in `~/.claude/settings.json`, `~/.carl/carl.json` DESIGN domain synced
- [x] Brief captured (this file)

## In Progress

- [ ] Nothing — clean break before the build

## Remaining

- [ ] **Start a fresh session** (hook registrations load at session start; they were added mid-session and are not active in the session that wrote this)
- [ ] **Read `snipe-leads`' project documentation first** — the leads agent, the new support agent, and how the two relate as one offering
- [ ] Confirm hooks are live: make one trivial UI-file edit, verify `design-route.py` output appears
- [ ] `$impeccable init` in `snipe-leads` → `PRODUCT.md`
- [ ] Run the Tier 1 gate against real brand evidence → `DESIGN.md` + `.impeccable/design.json` sidecar + emit `snajp-design` skill
- [ ] Rebuild: hero wordmark + Leads/Support toggle, surface `/snajp-support`, unify both demos, simplify throughout
- [ ] Copy gate over all user-facing strings, both languages
- [ ] `Skill(design-verify)` — four breakpoints, console + network clean
- [ ] Review `.impeccable/design-report-<date>.md`

## Deferred

- Promoting `design-gate.py` from advisory to blocking (`DESIGN_GATE_BLOCKING=1`) — do this only after one clean Snajp run is on record
- Resolving the dual-hook-system question (impeccable v4's own project-level PostToolUse manifest vs. our global one) — only matters if `npx impeccable install` is run inside a project

## Blockers

- **Decision needed**: the 22 OneDrive-restored v3 impeccable files (exact-path manifest in `session-logs/2026-07-27-session-log.md`). Cosmetic, not functional — `verify-design-system.py` passes 60/60 with them present — but should be resolved before or during the next session. Nothing deleted without explicit approval.

## Next Steps

1. Fresh session, confirm hooks fire.
2. Approve (or decline) the v3-leftover deletion manifest.
3. Run the Snajp build.
4. **Judge the result on two axes, not one**: the site itself, *and* the telemetry report.

## Pass criteria

**The build:**
- Leads/Support hero control works and swaps page content
- `/snajp-support` surfaced through it rather than orphaned
- Email studio and support demo read as one product's two capabilities — shared frame, controls, motion, label voice
- Site reads as one product, not stitched demos
- Large type preserved; corner editorial text gone
- Full `gates.md` sweep clean; `npx impeccable detect` clean
- Four breakpoints verified (320/375/414/768); copy gate clean in both languages

**The system (equally binding):**
- Every UI component touched has at least one attributed skill call
- **Route-vs-invocation gap = 0** — no route named a skill that never loaded. This is the direct measurement of the failure the whole rebuild exists to fix
- Every trap firing recorded with pre- or post-write catch
- Timeline unbroken from first edit to last
- Every derived token traces to real brand evidence with the source cited
- No hex from `minimalist-ui` / `industrial-brutalist-ui` / `high-end-visual-design` anywhere in the output
