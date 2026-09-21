# `hallmark redesign`

> **Diverges from upstream Hallmark: T6 port (2026-09-09).** Extended with the
> redesign material named in the design chain's v4 plan, sections 2.2 and 2.5:
> mode detection, the modernisation levers in priority order, the preservation
> rules, and the knob-delta form. Where two upstream fix-priority lists
> collided, the winner is named in the text.

The user wants a different page from the same content. They are not happy with the current visual structure — typically because it reads as templated, generic, or AI-shaped. Your job is to redesign the page's structure, rhythm, and component voice while respecting the existing implementation boundaries unless the user explicitly confirms a full rebuild.

## Non-destructive implementation rule

Hallmark redesigns visual and interaction layers. It does not delete production files by default.

- Never delete existing route files, component directories, page trees, or the old website unless the user explicitly asks for deletion or approves a file-level plan that lists the deletions.
- Default to in-place edits of the named page/component files, or additive new components/tokens wired through the existing route.
- If the redesign would require removing multiple components, replacing a route tree, or collapsing the app into a single new page, stop and ask for confirmation first.
- Treat PDFs, README files, `.md` briefs, docs, transcripts, and pitch decks as source material for understanding the product. They are not page copy by default. Summarize and adapt them unless the user explicitly says to use their wording verbatim.
- Before editing, state the files you expect to modify, create, and delete. Any deletion needs explicit confirmation.

## Step 0 · Detect scope first

Before anything else, decide whether the redesign is **single-page** or **multi-page**. The behaviour diverges hard.

**Multi-page signals (any one fires):**
- The target is a directory (e.g. `./app/`, `./pages/`, `./src/routes/`).
- The target is a glob (`**/*.tsx`, `app/*/page.tsx`).
- The user names more than one file in the brief (`./hero.tsx and ./pricing.tsx`).
- The user says "the whole site", "every page", "the app", "all the pages", "the marketing site".
- The codebase has multiple route files (`app/page.tsx`, `app/about/page.tsx`, `app/pricing/page.tsx`, etc.) and the user pointed at the project root.

If any of those fires → **multi-page redesign**. Go to § Multi-page flow.
If none fires → **single-page redesign**. Go to § Single-page flow.

## Step 0b · Detect the mode

Scope says how many files. Mode says how much of the existing brand survives, and
*"misclassifying the mode is the single biggest source of bad redesign output"*
(`design-taste-frontend` § 11.A). Three modes:

- **Greenfield** — no existing site, or a full overhaul the user approved. Dials from the
  brief, nothing preserved.
- **Redesign · Preserve** — modernise without breaking the brand. Audit first, extract the
  brand tokens, evolve gradually.
- **Redesign · Overhaul** — a new visual language on top of existing content. Treat as
  greenfield for visuals; preserve content and information architecture.

If it is ambiguous, ask **once**: *"Should this redesign preserve the existing brand, or are
we starting visually from scratch?"* One question, then proceed — this is not the
multi-round approval ceremony the front door already replaced.

## Step 0c · Audit before touching

Document the current state before proposing anything. Seven readings, from § 11.B:

- **Brand tokens** — primary and accent colours, type stack, logo treatment, radii.
- **Information architecture** — page tree, primary nav, key conversion paths.
- **Content blocks** — what exists, what is doing work, what is filler.
- **Patterns to preserve** — signature interactions, recognisable hero, copy voice.
- **Patterns to retire** — AI-slop tells, broken layouts, dead links, generic stock imagery,
  performance traps.
- **Dial reading of the existing site** — infer its current variance, motion and density.
  *"That's your starting point, not the baseline."*
- **SEO baseline** — ranking pages, meta titles, structured data, OG cards.
  ***"SEO migration is the #1 redesign risk."***

The audit is also what makes the fingerprint decision honest: you cannot pick *a different*
structural fingerprint from the source until you have written down what the source's was.

## Modernisation levers, in priority order

Apply in this order and **stop when the brief is satisfied** (§ 11.D). The order is
ranked by visual lift per unit of risk, which is why type comes first and block
replacement last:

1. **Typography refresh** — *"biggest visual lift per unit of risk."*
2. **Spacing and rhythm** — section padding, vertical rhythm.
3. **Colour recalibration** — desaturate, unify neutrals, keep the brand accent.
4. **Motion layer** — micro-interactions on the components that already exist.
5. **Hero and key-section recomposition** — restructure top-of-funnel.
6. **Full block replacement** — only when the existing block is unsalvageable.

A second, older list from `redesign-existing-projects` ranks the same work slightly
differently: font swap → colour palette cleanup → hover and active states → layout and
spacing → replace generic components → add loading, empty and error states → polish the
type scale. **Where the two disagree, § 11.D wins** — it is the current upstream, and it
ranks by risk rather than by visible effect. The older list contributes two steps § 11.D
does not name at all, and those are kept: **states** (hover, active, loading, empty, error)
sit between levers 3 and 4, because a redesign that never adds a state ships a page that
looks new and behaves exactly as unfinished as the old one.

**Decision tree** (§ 11.E): information architecture, content and SEO sound →
**targeted evolution**, levers 1–4, *"~70 % of value at ~40 % of risk"*. Visual debt is
structural (broken IA, no design system, broken mobile) → **full redesign** with strict
content preservation. The brand itself is changing → **greenfield**.

## Preservation rules

From § 11.C, and they bind in Preserve *and* Overhaul mode:

- **Do not change the information architecture** unless asked. Page slugs, anchor ids and
  primary nav labels stay stable, for SEO and for muscle memory.
- **Extract the brand colours before applying any palette rule.** A brand that is already
  purple stays purple; the anti-purple default is for invented palettes, not for a brand
  that owns the hue.
- **Preserve copy voice** unless a rewrite was asked for. *"Visual modernisation ≠ content
  rewrite."*
- **Honour existing accessibility wins.** Do not regress focus states, alt text, keyboard
  navigation, or contrast. A redesign that loses a focus ring has made the page worse no
  matter how it looks.
- **Respect existing analytics events.** Do not rename buttons, form fields, or section ids
  that downstream tracking depends on.

## What never changes silently

Never modify these without explicit user approval (§ 11.F). Each one breaks something
outside the page:

- URL structure and route slugs.
- Primary nav labels.
- Form field names or order (breaks analytics and browser autofill).
- Brand logo or wordmark.
- Existing legal, consent, or cookie copy.

"Silently" is the operative word: any of these may change when the user asks for it. What is
banned is changing one as a side effect of a visual decision.

## The random inversion

*"A single dark-background section breaking an otherwise light page looks like a copy-paste
accident."* Either commit to a full dark theme or hold one background tone through the page.
Where a section genuinely needs separation, *"use a slightly darker shade of the same
palette — not a sudden jump to `#111` in the middle of a cream page."*

This is the same rule the page-theme lock states from the other side: **one deliberate tonal
inversion per page is the allowance, and it is a composition decision** (a footer, a single
full-bleed act) with a real transition. Two inversions, or one that arrives without a
reason, is the accident. When a redesign inherits a random inversion from the source, flatten
it rather than reproducing it for parity.

## Same archetype, different fingerprint

When the user overrides the rotation — *"use Bento Grid again, I want the same shape"* — the
diversification rule does not evaporate, it moves down a level. State the delta out loud in
the hallmark form:

> *"Last build was Bento Grid (you requested it). You've asked for it again, so I'll pick
> different knob values. Knob deltas: tiles=8 (was 6), accent=full-bleed (was corner-only),
> spans=irregular (was even). Same archetype, different fingerprint."*

(Upstream's wording, with its one dash re-punctuated: this line is spoken output, and gate 75
applies to anything the chain writes for a human to read.)

The user gets the shape they asked for; the build still differs on the within-archetype
knobs from [`component-cookbook.md`](../component-cookbook.md). Silently repeating the
previous knob values is how two "different" builds turn out to be one build twice.

---

## § Multi-page flow — design.md first, then redesign

A web app needs a *design system*, not seventeen unrelated theme pickings. Hallmark's diversification rule is wrong here: across pages of the same product, **consistency is the goal, not variety**. If you redesign every page with a different macrostructure / theme / accent, you've shipped a slop split-personality app, even if each individual page is fine.

The flow is:

### 1. Read the project, then pause

Before redesigning a single file:

- Walk the target directory. List every page-level file you found, with a one-line description of what it does. (Hero / pricing / docs / dashboard / etc.)
- Note any existing design assets: a `tokens.css`, a tailwind config with brand values, a logo, brand colours mentioned in `README`, a marketing screenshot.
- Check for an existing `.hallmark/log.json` — if it has prior runs, read the most recent stamp; if all those entries are different macrostructures / themes, it confirms the user's complaint.

### 2. Produce `design.md` at the project root

Write a single file at the project root: `design.md` (or `DESIGN.md` — match the project's existing case convention). This file is the **one source of truth** every subsequent page redesign reads. Format:

````markdown
# Design — <Project name>

A locked design system for this app. Every page redesign reads this file before
emitting code. Do not regenerate per page — extend or amend this file when the
system needs to grow.

## Genre
<editorial · modern-minimal · atmospheric · playful>

## Macrostructure family
Pick one base macrostructure for marketing pages, one for app pages, one for
content pages (if applicable). Pages within a family share the family's shape;
they vary only in component archetypes.

- Marketing pages: <macrostructure name + the 1–2 archetypes that vary>
- App pages:       <macrostructure name + variation knobs>
- Content pages:   <macrostructure name + variation knobs>

## Theme
- `--color-paper`   oklch(<L> <C> <H>)
- `--color-paper-2` oklch(<L> <C> <H>)
- `--color-ink`     oklch(<L> <C> <H>)
- `--color-ink-2`   oklch(<L> <C> <H>)
- `--color-rule`    oklch(<L> <C> <H>)
- `--color-accent`  oklch(<L> <C> <H>)
- `--color-focus`   oklch(<L> <C> <H>)

## Typography
- Display: <face>, weight <N>, style <normal/italic>
- Body:    <face>, weight <N>
- Mono:    <face>, weight <N>
- Display tracking: <em>
- Type scale anchor: <text-display> = clamp(...)

## Spacing
4-point named scale. The values are in `tokens.css`. Pages must use named
tokens (`var(--space-md)`), never raw values.

## Motion
- Easings: cubic-bezier(<x>, <y>, <z>, <w>) named `--ease-out`, etc.
- Reveal pattern: <fade only / fade + slide / none>
- Motion plays unconditionally. No preference gate, no static fallback (F-011).
- Every reveal falls back to *visible* without JS.

## Microinteractions stance
- <silent success / celebratory toasts: never>
- <hover delay 800 ms · focus delay 0 ms>
- <other named choices>

## CTA voice
- Primary CTA: <fill style, shape, copy pattern>
- Secondary CTA: <outline style, shape, copy pattern>

## Per-page allowances
- Marketing pages MAY use enrichment (Tier-A CSS art, Tier-B SVG, etc.).
- App pages MUST NOT use enrichment — function carries the page.
- Content pages: typography only.

## What pages MUST share
- The wordmark / logotype.
- The accent colour and its placement (≤ 5 % per viewport).
- The display + body fonts.
- The CTA voice (button shape, border-radius, padding rhythm).
- Section heading rhythm (numeral + label + display heading pattern).

## What pages MAY differ on
- Macrostructure within the page-type family (a marketing page can be Marquee
  Hero on one route and Long Document on another — both still use the system's
  type, colour, and CTA voice).
- Hero archetype (within the family's allowance).
- Enrichment — only on marketing pages, only Tier-A or Tier-B.

## Exports

Drop-in formats for re-using this design system in other projects.
See [`export-formats.md`](../export-formats.md) for the canonical mapping.

### tokens.css
```css
:root {
  --color-paper:      oklch(<L> <C> <H>);
  --color-paper-2:    oklch(<L> <C> <H>);
  --color-ink:        oklch(<L> <C> <H>);
  --color-ink-2:      oklch(<L> <C> <H>);
  --color-rule:       oklch(<L> <C> <H>);
  --color-accent:     oklch(<L> <C> <H>);
  --color-accent-ink: oklch(<L> <C> <H>);
  --color-focus:      oklch(<L> <C> <H>);

  --font-display: "<face>", ...;
  --font-body:    "<face>", ...;
  --font-outlier: "<face>", ...;

  --space-3xs: 0.25rem;  --space-2xs: 0.5rem;  --space-xs: 0.75rem;
  --space-sm:  1rem;     --space-md:  1.5rem;  --space-lg: 2rem;
  --space-xl:  3rem;     --space-2xl: 4.5rem;  --space-3xl: 7rem;

  --text-xs: 0.75rem;  --text-sm: 0.875rem; --text-md: 1.125rem;
  --text-lg: 1.375rem; --text-xl: 1.75rem;  --text-2xl: 2.25rem;

  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --dur-short: 220ms;
  --radius-card: <px>; --radius-pill: <px>; --radius-input: <px>;
}
```

### Tailwind v4 `@theme`
```css
@theme {
  --color-paper:   oklch(<L> <C> <H>);
  --color-ink:     oklch(<L> <C> <H>);
  --color-accent:  oklch(<L> <C> <H>);
  --font-display:  "<face>", sans-serif;
  --font-body:     "<face>", sans-serif;
  --spacing-md:    1.5rem;
  --text-md:       1.125rem;
  --ease-out:      cubic-bezier(0.16, 1, 0.3, 1);
  /* mirror the rest of tokens.css with `--spacing-*` for Tailwind's spacing utilities */
}
```

### DTCG `tokens.json`
```json
{
  "color": {
    "paper":  { "$value": "oklch(<L> <C> <H>)", "$type": "color" },
    "ink":    { "$value": "oklch(<L> <C> <H>)", "$type": "color" },
    "accent": { "$value": "oklch(<L> <C> <H>)", "$type": "color" }
  },
  "font": {
    "display": { "$value": "<face>", "$type": "fontFamily" },
    "body":    { "$value": "<face>", "$type": "fontFamily" }
  },
  "space": {
    "md": { "$value": "1.5rem", "$type": "dimension" }
  }
}
```

### shadcn/ui CSS variables
```css
:root {
  --background:        <L>  <C>  <H>;   /* paper */
  --foreground:        <L>  <C>  <H>;   /* ink */
  --primary:           <L>  <C>  <H>;   /* accent */
  --primary-foreground: <L> <C>  <H>;   /* accent-ink */
  --muted:             <L>  <C>  <H>;   /* rule */
  --muted-foreground:  <L>  <C>  <H>;   /* muted */
  --border:            <L>  <C>  <H>;   /* rule */
  --input:             <L>  <C>  <H>;   /* rule */
  --ring:              <L>  <C>  <H>;   /* focus */
  --radius:            <px>;
}
```
````

State the picks aloud in plain text BEFORE writing the file. *"Genre: modern-minimal. Theme: a custom OKLCH palette anchored on your brand teal. Display: Geist 600. Body: Geist 400. Three macrostructure families: Marquee Hero (marketing), Workbench (app), Long Document (content)."* Then ask: *"Want me to proceed with this system across every page, or amend any of it first?"*

Wait for confirmation. Only after the user confirms (or says "go ahead") do you write `design.md` and start redesigning pages.

### 3. Redesign each page reading from `design.md`

For each target page:

- **Read `design.md` first.** It is now the rule of the project; the per-build references in [`references/`](../) defer to it. Where `design.md` and the references conflict, `design.md` wins.
- Pick the macrostructure from the family declared in `design.md` for this page's type (marketing / app / content). Within the family, you may vary archetypes — but only those `design.md` allows.
- Apply the locked theme. Do **not** swap to a different theme to "add variety". The variety lives in macrostructure / archetype choice, not theme.
- Apply the locked typography, spacing, motion, microinteractions stance.
- Stamp every page's CSS with: `/* Hallmark · genre: <genre> · macrostructure: <name> · design-system: design.md · designed-as-app */`. The `designed-as-app` flag tells future Hallmark runs to read `design.md`, not invent a new system.
- Write a single combined `.hallmark/log.json` entry for the multi-page redesign, with `"scope": "app"` instead of one entry per page.

### 4. Diversification rule — INVERTED for multi-page

Across pages of the same app, the diversification rule is *inverted*: consecutive pages MUST share theme, accent, type pairing. They may differ on macrostructure within the family. The 58 slop-test gates that check "differs from previous Hallmark run" are skipped for `designed-as-app` outputs — the system overrides the catalog rotation here.

Pages that drift from `design.md` are slop. The audit verb flags `design.md` drift as a critical structural finding (`stamp-vs-design.md disagreement`).

### 5. When to amend `design.md` instead of overriding

If a page genuinely needs something `design.md` doesn't allow (e.g. a marketing landing for a new sub-product wants a different theme), the rule is **amend `design.md` first**, not override locally. Add an explicit per-page allowance or a `## Variants` section. The file evolves; per-page overrides do not.

---

## § Single-page flow

(The classic redesign behaviour — unchanged.)

**What to preserve:**
- The copy intent, factual claims, product names, and primary message. Preserve exact wording only when it already lives in the target UI or the user explicitly asks for verbatim copy.
- The information architecture (which sections exist, in roughly what order)
- The brand (colours and fonts they've named, if any)
- The primary action
- The existing route/component ownership boundaries, unless the user has approved a full rebuild

**What to replace:**
- The structural fingerprint — pick a **different** combination from [`structure.md`](../structure.md) than the source had.
- The component voice — different button style, different divider language, different image treatment.
- The reveal pattern — if the original faded everything in on scroll, the new one might have no reveals at all.
- The visual rhythm — different sections having different padding, different alignments, deliberate breaks.

**What not to replace without confirmation:**
- Route trees, production component directories, or the old website's file structure.
- Working app logic, data fetching, auth, forms, analytics, or integration code.
- Existing copy with pasted text from PDFs, docs, or markdown files unless the user requested verbatim copy.

**Optional `--mood <name>` argument:**

If the user specifies a mood (`hallmark redesign ./hero.tsx --mood luxury`), pick a tone aligned to that mood and let it drive the structural fingerprint. Mood names map to tones from [`typography.md`](../typography.md) and [`structure.md`](../structure.md). If no mood is given, ask the user what *feeling* they want — one word — and proceed.

**Genre escape hatch.** If the user explicitly asks for a *kind* of design that the current genre doesn't fit (e.g. "redesign this editorial page as a modern SaaS hero"), switch genre too. Load [`genres/<new-genre>.md`](../genres/) and apply its rule overlay. Stamp the new genre into the output so future runs respect it.

**Project-level check.** Before treating this as a true single-page redesign, look for `design.md` at the project root. If it exists, the project is being designed as an app and **the single-page rules don't apply** — read `design.md` and follow it instead. The diversification rule reverses (consistency wins). If you actually want to break from the locked system, *update `design.md` first*, then redesign.

**Output:**

Return the redesigned code, plus a short note explaining:

- The structural fingerprint you picked, axis by axis.
- Why this combination fits the brief better than the original.
- One thing you removed and why.
- (If genre changed) why the new genre fits the user's stated kind of design.
