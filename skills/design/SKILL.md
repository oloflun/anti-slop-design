---
name: design
description: "Master router that fires on ANY design work — websites, landing pages, ads, dashboards, app UI, components, redesigns, polishes, animations, color, typography, layout, motion. Use whenever the user says 'design', 'redesign', 'build a page', 'build a site', 'build a landing page', 'make it premium', 'make it look better', 'polish this', 'add animation', 'extract the design from', 'visual direction', 'mockup', 'hero', 'CTA', 'bento', 'pricing page', or any synonym for visual design execution. Auto-selects from the full design skill stack (impeccable + design-taste-frontend + high-end-visual-design + gpt-taste + extract-design + specialty skills) instead of letting the model fall back to AI-generic SaaS defaults (Inter, 3-column card grids, hero-metric template, beige restraint). Triggers in any language including Swedish ('design', 'designa', 'bygg en sida', 'gör om', 'polera', 'premiumkänsla')."
user-invocable: true
---

# Design Router — The Anti-Slop Spine

You are about to do design work. Before writing a single line of UI code or making a single visual decision, run this router.

The user's previous attempts in this codebase failed because the model fell back to base AI taste: Inter, centered hero stacks with chart-card-on-the-right, 4-column metric grids with tiny captions, generic icon-title-text card rows. Every one of those patterns is on the absolute-ban list of the skills that should have fired but didn't. **This router exists so that never happens again.**

## Iron Rules — Apply Before Every Decision

These compound across every sub-skill. Even if no other skill loads, these alone block the dominant failure mode:

### The five bans
1. **No Inter, no DM Sans, no Plus Jakarta, no Outfit, no Space Grotesk.** Reach further. The brand register's reflex-reject list is binding for greenfield work.
2. **No centered hero stack with subhead-buttons-screenshot.** That's the template silhouette. Use asymmetric, editorial split, drenched-color, image-led, or rigorously-gridded — but not the AI default.
3. **No 3-column card grid with icon + title + body.** Use Bento 2.0 (asymmetric tile sizes with grid-flow-dense), 2-column zig-zag, horizontal scroll, masonry, or a single feature spread.
4. **No hero-metric template** (big number + small label + supporting stats + gradient accent). Banned by both Impeccable and design-taste-frontend.
5. **No `#fff` / `#000` / pure beige restraint as the default.** OKLCH with the neutral tinted toward the brand hue. Pick a color *strategy* (Restrained / Committed / Full palette / Drenched) before picking colors.

### The two slop tests
- **First-order:** could someone guess the theme + palette from the category alone? (observability → dark blue, healthcare → white + teal, fintech → navy + gold, AI-SDR → egg-shell + navy). If yes, rework.
- **Second-order:** could they guess the aesthetic family from category + anti-references? ("Notion-adjacent SaaS that's not Stripe-minimal → Editorial-typographic"). If yes, rework. The second reflex is the trap one tier deeper.

## Step 1 — Detect the task type

Read the user's request. Classify it into one of these lanes, then route. If multiple lanes apply, run them in the order listed.

| Lane | Cues | Route to |
|---|---|---|
| **Ground-up build** | "build a [site/landing/page]", "make me a", "create a", "design a [X] for [Y]" | Lane A |
| **Redesign existing** | "redesign", "make this look premium", "gör om", "fix this AI-looking page", "upgrade", "the page looks generic" | Lane B |
| **Polish / finishing** | "polish", "tighten up", "ship-ready", "final pass", "pre-launch", "something's off" | Lane C |
| **Reference-driven** | URL or screenshot provided as inspiration, "make it look like X", "match the style of" | Lane D |
| **Component / motif** | "add a [nav/hero/pricing/bento/animation]", isolated piece | Lane E |
| **Visual direction only** | "what should this look like", "mood / direction", brief without code | Lane F |
| **Audit / critique** | "review my UI", "what's wrong with", "is this accessible" | Lane G |

Default if uncertain: **Lane A** (treat as ground-up).

## Step 2 — Run the lane

### Lane A — Ground-up build

Sequence is strict. Do not collapse gates.

1. **Detect the register.** Brand (landing, marketing, portfolio, campaign — design IS the product) vs Product (app, dashboard, admin — design SERVES the product). Cue in the brief wins; falling back to the surface in focus.
2. **Invoke `impeccable craft [feature]`** — this is the spine. It loads PRODUCT.md if present, runs the register reference (brand.md or product.md), and runs the shape → mocks → build → iterate → present flow with proper gates.
3. **Layer the aesthetic specialist** based on the named or implied aesthetic lane:
   - "Awwwards-tier / cinematic / scrolltelling" → also invoke **gpt-taste** for AIDA structure + GSAP scroll choreography (pinned sections, scrubbing reveals, gapless bento).
   - "Apple-/Linear-tier / haptic / glass / dock-magnification" → also invoke **high-end-visual-design** for Double-Bezel + button-in-button + Variance Engine (Ethereal Glass / Editorial Luxury / Soft Structuralism).
   - "Premium SaaS / Bento 2.0 / Vercel-core meets Dribbble" → also invoke **design-taste-frontend** for the Bento 2.0 spec + 5-card archetypes with named perpetual micro-animations.
   - "Editorial / document-style / muted pastels" → **minimalist-ui**.
   - "Brutalist / Swiss / tactical / terminal" → **industrial-brutalist-ui**.
   - **Default if no lane stated:** layer design-taste-frontend (it's the strongest anti-bias enforcer and works under any aesthetic).
4. **If imagery is required** (restaurants, hotels, magazines, photography, fashion, food, travel, product, portfolios): you must ship imagery, not CSS scenery. Use `imagegen-frontend-web` to generate one image per section, or sourced photography per Impeccable's brand register (verify URLs before referencing).
5. **Pre-flight check** (every build, no exceptions):
   - [ ] Font is NOT in the reflex-reject list. Read `~/.agents/skills/impeccable/reference/brand.md` if unsure.
   - [ ] Color strategy named explicitly (Restrained / Committed / Full palette / Drenched) before tokens chosen.
   - [ ] Aesthetic lane named explicitly (e.g. "Liquid Death acid-green drench", "Klim-style typographic specimen") — unnamed ambition becomes beige.
   - [ ] Both slop tests pass.
   - [ ] No banned pattern from "The five bans" appears in the design plan.
6. **Build the code** following the chosen specialist's specs. The specialist's pre-flight checklist is binding.
7. **Iterate visually** per `impeccable craft` Step 5 — read screenshots back into the conversation. A screenshot you didn't read doesn't count.
8. **Always end with `impeccable polish`** — final pass against the design system, drift named and resolved by root cause.

### Lane B — Redesign existing

1. **Invoke `redesign-existing-projects`** — it audits the current design and identifies generic AI patterns.
2. **If the user named a reference site:** invoke `extract-design <url>` to pull real tokens (colors, type, spacing, components) from it. This is the only skill that operates on existing sites instead of briefs — use it.
3. **Run `impeccable critique`** on the current state for structured findings.
4. **Then run Lane A from step 3 onward** with the audit findings as the design brief.

### Lane C — Polish

1. **Invoke `impeccable polish`** (or the standalone `polish` skill — they're aliases). Mandatory design-system discovery first; aligning to the system is not optional.
2. **If animation/interaction polish is in scope:** layer `emil-design-eng` — it outputs a Before/After/Why review table covering easing misuse, `scale(0)` entries, missing `:active` states, wrong `transform-origin` on popovers, keyframes where transitions belong, and durations > 300ms.
3. **If accessibility is in scope:** layer `ui-ux-pro-max` for the 99-rule checklist pass (it's strong here; just don't let it set visual direction).
4. **If review against external guidelines is asked:** `web-design-guidelines` fetches Vercel's interface guidelines for a structured review.

### Lane D — Reference-driven

1. **Invoke `extract-design <url>`** first — produces tokens, type scale, palette, shadcn theme, all 8 output files. This is non-negotiable when a URL is the brief; it stops the model from guessing tokens.
2. **Read the extracted markdown** for the design language understanding.
3. **If the reference is one of the named aesthetic lanes from Lane A step 3,** layer the matching specialist.
4. **Build via `impeccable craft`** with the extracted tokens loaded into DESIGN.md.
5. **Critical:** *borrow principle, not pixel.* The user's brief said this explicitly in Swedish: "Var noga med att inte kopiera hela designer eller enskilda varumärkeselement från andra bolag rakt av, utan skapa en egen premiumidentitet genom att blanda de olika element du hämtat från inspirationskällorna." Mix elements; never clone.

### Lane E — Component / motif

1. **Identify the motif.** Animated nav → `animated-navigation`. 3D carousel → `slideshow`. Page transition → `vercel-react-view-transitions`. shadcn component → `shadcn-ui`. **Animation/interaction on any component** (button press feel, drawer, popover, tooltip, toast, drag gesture, easing choice, micro-interaction review) → `emil-design-eng`. Otherwise → `impeccable <verb>` (animate, colorize, typeset, layout, delight, distill, overdrive, etc.).
2. **Apply the relevant Iron Rules.** A component that contains a banned pattern is still wrong, even if it's "just a piece."
3. **Always end with `impeccable polish`** for the component.

### Lane F — Visual direction only

1. **Invoke `designpowers/design-taste`** (or `impeccable shape`) to calibrate references + emotional target + craft standards + quality bar.
2. **Layer `designpowers/inspiration-scouting`** for cross-domain references.
3. **If image mocks are wanted:** `imagegen-frontend-web` to produce per-section reference images. One image per section, never compressed.
4. **Do not write code** until the user confirms direction.

### Lane G — Audit / critique

1. **`impeccable critique`** for design intent + heuristic scoring.
2. **`impeccable audit`** for technical quality (a11y, perf, responsive).
3. **`web-design-guidelines`** for the Vercel interface guidelines pass.
4. **`ui-ux-pro-max`** for the 99-rule checklist if comprehensive coverage is wanted.

## Step 3 — Production discipline

Across every lane:

- **Real content, not lorem.** No placeholder copy at presentation time. The Snipra examples shipped "Nord Byggpartner / Fjord Fastigheter / Lyft Gymkedja" placeholder names — those are exactly the "Acme / Nexus / SmartFlow" startup-slop names design-taste-frontend bans. Use realistic Swedish company names with messy organic data: `47.2%` not `50.0%`, `+46 70 847 1928` not `+1 555 1234`.
- **No emojis as icons.** Phosphor or Radix only; consistent stroke width (1.5 or 2.0).
- **Real imagery on image-led briefs.** Unsplash URL format `https://images.unsplash.com/photo-{id}?auto=format&fit=crop&w=1600&q=80` — verify resolves before referencing. Without verification, fewer photos you're confident exist beats more guessed IDs.
- **OKLCH for all color tokens.** Never `#fff` / `#000`. Tint the neutral toward the brand hue (chroma 0.005–0.01).
- **Modular scale with `clamp()` for fluid type.** ≥1.25 ratio between steps. Flat scales read as uncommitted.
- **GPU-only animation.** Animate `transform` and `opacity` only. Layout-triggering animation is banned; grain/noise only on fixed `pointer-events-none` overlays. For easing curves, timing tables, spring config, and the full interaction review checklist → `emil-design-eng`.
- **Mobile collapse for any asymmetric layout above `md:`.** Asymmetry on desktop, single-column on mobile, always.

## Step 4 — The exit bar

The work is done when ALL of these are true:

- A high-end studio reviewer would defend it.
- The category-reflex test passes (you couldn't guess theme from category).
- The aesthetic-lane test passes (named reference, not "modern + minimal").
- Production build is clean (no console errors, no broken assets, no CLS).
- Every state covered: default, hover, focus-visible, active, disabled, loading, error, success, empty.
- Reduced-motion alternative exists for every animation.
- The user has been shown screenshots of mobile + desktop and confirmed.

## Skill paths

For Claude Code's Skill loader, all of these are accessible:

```
~/.agents/skills/impeccable/                                                  # primary
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/design-taste-frontend/    # anti-bias
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/high-end-visual-design/   # detail vocabulary
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/gpt-taste/                # GSAP scrolltelling
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/extract-design/           # URL → tokens
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/minimalist-ui/            # editorial lane
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/industrial-brutalist-ui/  # brutalist lane
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/redesign-existing-projects/
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/polish/
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/imagegen-frontend-web/
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/brandkit/
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/web-design-guidelines/
~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills/ui-ux-pro-max/
~/designpowers/skills/design-taste/                                                  # taste calibration process
~/designpowers/skills/inspiration-scouting/
~/designpowers/skills/motion-choreography/
```

## What this skill is NOT

This is a router, not a builder. It does not replace any sub-skill. Its job is to *select and sequence* sub-skills so the model never falls back to base AI taste again. If you find yourself implementing UI inside this skill's scope, you've gone wrong — route to Impeccable's `craft` and let the proper chain run.
