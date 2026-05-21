# Design Skill-Stack Performance Audit

> Reviewed against the failure mode visible in `generic design reference/`: AI-generic SaaS cards, Inter-ish sans, hero-metric template, flat egg-shell palette, generic icon grids. Target quality bar: Impeccable.style/neo-mirai (speculative-futurist editorial, illustrated, dark navy + amber) and Floria-landing-page (editorial luxury minimalism, cream + charcoal, botanical photography, image-layered hero).

## Rubric

Each skill scored on five dimensions, 0–5 each, total /25:

- **Anti-slop teeth** — does it actively *block* AI defaults (Inter, centered hero, identical card grids, hero-metric template, beige restraint)?
- **Aesthetic ceiling** — what's the *best* output it can drive? Template-clean (3), agency-tier (4), Awwwards-tier (5)?
- **Execution fidelity** — does it produce working code with real spacing/motion specs, or just vibes-as-text?
- **Routing clarity** — does its `description` field reliably fire on the right tasks (no ambiguity, good triggers)?
- **Maintenance cost** — does it overlap with stronger skills, gate-block on welcome rituals, or require external services?

## The Verdict — Ranked

| Rank | Skill | Score | Verdict |
|---|---|---:|---|
| 1 | **impeccable** | 24/25 | KEEPER — primary engine |
| 2 | **design-taste-frontend** | 23/25 | KEEPER — anti-bias enforcer |
| 3 | **high-end-visual-design** | 22/25 | KEEPER — variance + double-bezel detail |
| 4 | **gpt-taste** | 21/25 | KEEPER — AIDA/GSAP scrolltelling |
| 5 | **extract-design** | 19/25 | KEEPER — unique capability (URL → tokens) |
| 6 | **minimalist-ui** | 17/25 | Conditional — when "editorial / Notion-adjacent" is the brief |
| 7 | **industrial-brutalist-ui** | 17/25 | Conditional — when "Swiss / terminal / tactical" is the brief |
| 8 | **polish** | 17/25 | Phase-specific — fires at the end of every build |
| 9 | **redesign-existing-projects** | 16/25 | Phase-specific — fires when user says "redesign / upgrade existing" |
| 10 | **brandkit** | 16/25 | Image-only — fires when generating brand boards / logo sheets |
| 11 | **imagegen-frontend-web** | 16/25 | Image-only — fires when generating per-section reference images |
| 12 | **image-to-code** | 16/25 | Image-led build — fires when "make it look like X but I have no mock" |
| 13 | **designpowers/design-taste** | 15/25 | Pair w/ Impeccable — strong taste-calibration *process* |
| 14 | **designpowers/motion-choreography** | 14/25 | Pair — solid motion discipline, complementary to gpt-taste |
| 15 | **designpowers/inspiration-scouting** | 14/25 | Pair — cross-domain reference curation |
| 16 | **animated-navigation** | 13/25 | Component-specific — fires for nav builds (haajp-next style) |
| 17 | **slideshow** | 13/25 | Component-specific — fires for 3D carousel builds |
| 18 | **vercel-react-view-transitions** | 13/25 | Component-specific — fires for cross-route motion |
| 19 | **shadcn-ui** | 12/25 | Component lib — only when user explicitly wants shadcn |
| 20 | **web-design-guidelines** | 12/25 | Audit-only — fetches Vercel guidelines for review pass |
| 21 | **vercel-composition-patterns** | 11/25 | React refactor — non-aesthetic |
| 22 | **vercel-react-best-practices** | 11/25 | React perf — non-aesthetic |
| 23 | **ui-ux-pro-max** | 11/25 | Checklist DB — caps at template-clean, RN-biased |
| 24 | **designpowers/ui-composition** | 10/25 | Process-y, accessibility-led, low aesthetic teeth |
| 25 | **designpowers/designpowers-critique** | 10/25 | Process; useful but no aesthetic teeth |
| 26 | **designpowers/using-designpowers** | 6/25 | Welcome gate — gets in the way for fast lanes |
| 27 | **react-components** | 6/25 | Stitch→Vite converter, niche |
| 28 | **stitch-design** / **stitch-design-taste** / **stitch-loop** | 6/25 | Requires Google Stitch MCP; skip unless Stitch is the chosen tool |
| 29 | **design-md** | 5/25 | Stitch-specific DESIGN.md generator, niche |
| 30 | **imagegen-frontend-mobile** | — | Mobile image gen; not relevant for web work |
| 31 | **ad-creative / ads / popups / image** | — | Marketing/copy skills, not visual design execution |
| 32 | **webpage-builder** | — | Hard-coded for haajp-next; project-specific |

## Why the previous Snipra attempts failed

Looking at `First attempt/` and `Second attempt/` screenshots against the skill set:

1. **No skill was actually loaded.** The output is what a base Claude/Codex produces with no design skill active: Inter, 4-column metric grid, chart card on the right, three-column icon row, standard table. Every single one of those patterns is on Impeccable's *absolute ban* list (the "hero-metric template", "identical card grids") and design-taste-frontend's "anti-slop" list ("3-column card layouts banned", "Inter banned").
2. **The Swedish prompt named skills as nouns ("designpowers", "frontend design", "impeccable")** but didn't invoke them — Codex doesn't run skills by mention, it needs them in scope. The skill descriptions don't fire on Swedish triggers reliably, and my "Använd designlang" instruction never reached `extract-design`'s actual bash command.
3. **Snipra's Apollo/Vercel/Notion references collapsed to the dead center of all three** — "Stripe-minimal beige restraint", aka the Editorial-typographic / Tech-minimal aesthetic lane that Impeccable's brand register specifically flags as currently saturated. The second-order slop test would have caught it.

## Top picks confirmed

**Impeccable is the spine.** It owns context (PRODUCT.md + DESIGN.md + register detection), has 22 sub-commands covering the full design lifecycle, ships the strongest anti-slop bans I've ever seen in a skill (Brand register lists *specific banned font names and aesthetic lanes*, second-order slop test, category-reflex check), and produces real working code with image-verification discipline.

**design-taste-frontend is the co-pilot.** Where Impeccable's brand register tells you *what's banned*, design-taste-frontend tells you *what to write instead*: specific Tailwind classes, OKLCH color tokens, Framer Motion spring physics, Bento 2.0 architecture, 5-card archetypes with named animations.

**high-end-visual-design and gpt-taste are specialty tools, not replacements.** high-end-visual-design owns the Apple/Linear "Double-Bezel + button-in-button" detail vocabulary; gpt-taste owns the Awwwards/GSAP scrolltelling lane with pinned sections, scrubbing reveals, gapless bento, and the 2-line H1 iron rule. Both are stronger than my previous workflow assumed.

**extract-design is the one indispensable utility.** It's the only skill that turns a URL into real tokens. The other top picks operate on briefs; this one operates on existing sites.

## What to retire or demote

- **using-designpowers' welcome ritual** (the bird ASCII art, guided walkthrough, mandatory tip cadence) is overhead for a senior user with a clear brief. Bypass it.
- **ui-ux-pro-max** is comprehensive but checklist-coded — it pulls the design *toward* compliance, not toward distinctiveness. Keep it for accessibility/responsive audits, not for setting visual direction.
- **stitch-*** and **design-md** require the Google Stitch MCP server. Skip unless I explicitly choose Stitch.
- **react-components**, **webpage-builder** are project-specific (Stitch-output, haajp-next). Don't fire them on greenfield briefs.

---

See `~/.agents/skills/design/SKILL.md` for the router that auto-selects from this stack.
