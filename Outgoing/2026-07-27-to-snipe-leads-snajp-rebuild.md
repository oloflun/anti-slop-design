# Cross-Project Handoff — Snajp Rebuild

**From:** anti-slop-design session 2026-07-27
**To:** snipe-leads
**Source session log:** `anti-slop-design/session-logs/2026-07-27-session-log.md`
**Source plan:** `anti-slop-design/plans/2026-07-27-snajp-rebuild.md`

## What Changed

The `design` skill was rebuilt end to end this session — a brand-derivation gate (Tier 0 locked / 1 derive from evidence / 2 study a reference / 3 invent) backed by a 6-hook chain that moves enforcement from once-per-prompt to once-per-file-write. Full detail in the source session log and plan above; the short version:

- **The rule:** brand derives direction, skills supply craft, themed skills are the last resort. Three installed specialists (`minimalist-ui`, `industrial-brutalist-ui`, `high-end-visual-design`) each hardcode a complete palette — the gate exists specifically so they can't set direction on a project that has its own identity.
- **Hooks are live**, wired into `~/.claude/settings.json`, but **registrations load once at session start** — they were added mid-session, so this is not the session that proves them. The Snajp build is.
- **Every session produces `.impeccable/design-session.jsonl` and a `design-report-<date>.md`** — the router names a skill (`design-route.py`, PostToolUse) and the report measures whether it actually got invoked. That gap has to be zero.
- **impeccable is now v4.0.2.** Its 68-rule detector, four of which (`design-system-color/font/font-size/radius`) check a build's `DESIGN.md` frontmatter directly, is what `design-gate.py` denies writes against.

## What It Means For This Project

This is the **first real build** under the new system, not a synthetic test. Everything below is the actual brief, carried forward verbatim so nothing gets re-litigated or re-derived from a different mood next session.

### The brief

- **Rename** Snipe / Snipra → **Snajp**. More Swedish, more recognizable.
- **Product pivot**: no longer only a leads agent — now also a dedicated **support agent**. Read the scope of this pivot from the repo's own docs (`EMAIL_STUDIO.md` and whatever else exists) **at build time, not before** — see "What NOT to do first" below.
- **What's wrong now**: a very long demo site for the leads agent alone. Too much going on, too much detail. Clarify and simplify the message; make the pages feel like one product, not stitched demos.
- **Hero requirement**: a big **Snajp** wordmark with **Leads / Support** beside it, both clickable, swapping the rest of the page to focus on that offer. This is the page's signature interaction, not decoration.
- **`/snajp-support` is currently orphaned** — unreachable from the landing page. It has an interactive demo analogous to the leads **email studio**. Surface it through the Support half of the hero toggle. **Present both demos uniformly** — shared frame, controls, motion, label voice. **Improve both**, not just the new one — the email studio isn't exempt for already existing.
- **Direction**: modern without losing the soul. **Keep the large fonts.** **Drop the small, thin, corner editorial text.** Register: **Nordic SaaS**.

### What NOT to do first

**Do not read this project's own documentation before the build session actually starts.** That instruction came from the user directly, twice, and it matters mechanically: the gate is supposed to derive direction from the repo's real evidence *at build time*. Pre-reading and summarizing the docs into a plan ahead of time is exactly the kind of pre-derivation that would bias the router toward one interpretation before the gate ever runs.

### The two named traps

Both demoted specialist skills look superficially right for this brief and must not fire:

- **Nordic SaaS is not `minimalist-ui`'s Notion palette** (`#F7F6F3`, `#EAEAEA`, `#787774`, mandated `border: 1px solid #EAEAEA`).
- **"Large fonts, drop the fine print" is not `industrial-brutalist-ui`'s hazard-red Swiss grid** (`#E61919` declared "the ONLY accent color").

Every hex from either skill appearing in the output is gate 60 — a contract violation once `DESIGN.md` is locked, and every firing gets logged as a `trap` event whether the gate catches it or not.

## Actionable Items

1. **Start fresh.** Confirm the hooks are actually active before anything else — make one trivial UI-file edit, verify `design-route.py`'s output appears in context.
2. **`$impeccable init`** to establish `PRODUCT.md`, then read the project's own docs for the leads+support pivot scope.
3. **Run the Tier 1 gate** against the project's real evidence (existing logo, tokens, deployed site) → `DESIGN.md` + `.impeccable/design.json` sidecar + emit a `snajp-design` skill so the derived identity is reusable.
4. **Build**, then run `Skill(design-verify)` — four breakpoints, console and network clean before judging the render.
5. **Read `.impeccable/design-report-<date>.md` before calling this done.** The build passing visually and the telemetry passing are two separate, equally binding checks — full pass criteria in `plans/2026-07-27-snajp-rebuild.md`.
6. There's also an unresolved housekeeping item from this session (22 OneDrive-restored v3 `impeccable` files awaiting a deletion decision — exact-path manifest in the session log) that has no functional impact on this build but should get resolved at some point.
