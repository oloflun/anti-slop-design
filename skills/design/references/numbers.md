# Numbers — the measurable floor

Ported from `power-design`'s `web-principles.md` Appendix A ("Numbers Cheat Sheet",
~90 values) plus its four codifiable formulas. The whole point of a table like this is
that it turns review into a **check** instead of a judgment: a reviewer who has this
open can say "measure 88ch, floor is 75" instead of "the lines feel long".

`power-design` itself is otherwise held at arm's length — its 93 brand dossiers are a
Tier-3 anti-reference only, because loading a finished palette *is* applying a house
style (gate **60**). The numbers are the part that ports.

**These are floors and defaults, not the design.** Where this table and a chain file
disagree, the chain file wins; every such row is marked **†** and resolved under
[Where the chain's own number wins](#where-the-chains-own-number-wins).

## Appendix A, as ported

| Category | Variable | Value |
|---|---|---|
| Layout | Test widths | 320, 390, 768, 1024, 1440 px |
| Layout | Default breakpoints | 640 / 768 / 1024 / 1280 px |
| Layout | Page shell max-width | 1200–1440 px |
| Layout | Reflow (WCAG 1.4.10) | no 2-axis scroll at 320 px / 400 % zoom |
| Type | Body min | 16 px (inputs 16 px too) |
| Type | Body fluid | `clamp(1rem, 0.92rem + 0.4vw, 1.125rem)` |
| Type | H1 fluid **†** | `clamp(2rem, 1.1rem + 4.5vw, 3.75rem)` |
| Type | Measure | 45–75ch (max-width 65ch) |
| Type | Body line-height | ≥ 1.5 (WCAG 1.4.12) |
| Type | Display line-height | 1.0–1.2 |
| Type | Paragraph spacing | ≥ 0.75em |
| Type | Families **†** | ≤ 2, woff2, `font-display: swap` |
| Type | Default scale ratio **†** | 1.25 (web); 1.333 (marketing) |
| Spacing | 8-pt scale | 4, 8, 12, 16, 24, 32, 48, 64, 96, 128 |
| Spacing | Related / unrelated gap | ≤ 16 px / ≥ 48 px |
| Spacing | Section padding (y) | `clamp(48px, 6vw, 128px)` |
| Grid | Columns / gap | 12 / `clamp(16px, 2vw, 32px)` |
| Color | Split | 60-30-10 |
| Color | Accent coverage | ≤ 10 % |
| Color | Body contrast (AA / AAA) | 4.5:1 / 7:1 |
| Color | Large text (AA / AAA) | 3:1 / 4.5:1 |
| Color | UI / focus / icons (SC 1.4.11) | ≥ 3:1 |
| Color | Ramp space **†** | OKLCH, 12 steps |
| Touch | Target size | ≥ 44×44 px, ≥ 8 px apart |
| States | Per interactive element **†** | default / hover / focus-visible / active / disabled |
| States | Focus ring | ≥ 2 px, ≥ 3:1 contrast |
| Motion | UI transition **†** | 150–300 ms |
| Motion | Section reveal | ≤ 500 ms |
| Motion | Flashes/sec max | < 3 |
| Motion | Animate only **†** | `transform`, `opacity` |
| Perf | LCP / INP / CLS **†** | < 2.5 s / < 200 ms / < 0.1 |
| Perf | Hero image **†** | ≤ 200 KB (AVIF/WebP) |
| Perf | Total JS **†** | ≤ 300 KB gzip |
| Perf | Total transfer (marketing) **†** | ≤ 1–1.5 MB |
| Conversion | Primary CTAs per viewport | ≤ 1 |
| Conversion | Pricing tiers visible **†** | 3 (middle default), ≤ 4 |
| Conversion | "How it works" steps **†** | 3 |
| Forms | Layout | single column |
| Forms | Labels | persistent, visible, associated |
| Forms | Validation | on blur, inline, adjacent, preserves input |
| Forms | Fields | fewest that do the job |
| Nav | Top-level items | ≤ 7 |
| Nav | Depth to any page | ≤ 3 clicks |
| Nav | Sticky header height | ≤ 10–12 % viewport |
| SEO | `<title>` / description | ≤ 60ch / ≤ 155ch |
| SEO | OG image | 1200×630 |
| A11y | `<h1>` per page | exactly 1 |
| A11y | Text zoom | 200 % no loss |
| A11y | Standard | WCAG 2.2 AA (floor) |

## Fluid type and space — the Utopia formula

Interpolate type and spacing between a minimum at ~320 px and a maximum at ~1240 px
viewport, so nothing snaps at a breakpoint. `clamp(MIN, PREFERRED, MAX)` where
`PREFERRED` mixes a **`rem` base and a `vw` term**:

```css
--step-body:   clamp(1rem, 0.92rem + 0.4vw, 1.125rem);  /* 16 → 18 px */
--step-h1:     clamp(2rem, 1.1rem + 4.5vw, 3.75rem);    /* 32 → 60 px — see † */
--space-section: clamp(3rem, 2rem + 6vw, 8rem);
```

**The guard is the whole reason for the formula.** Never put a raw `vw` unit on type
without `clamp()`: it fails WCAG 1.4.4, because text must scale to 200 %. The `rem`
term *inside* the clamp is what preserves user zoom. A `font-size: 4vw` heading is
unzoomable and that is a defect, not a style.

Same primitive for widths: `padding-inline: clamp(1rem, 5vw, 4rem)` on the shell,
`max-width: 68ch` on prose.

## Metric-matched font fallback

`font-display: swap` costs a layout shift unless the fallback has the same metrics as
the real face. Declare a fallback `@font-face` over a local system font with
`size-adjust`, `ascent-override` and `descent-override` (or `font-size-adjust`) so the
swap changes the shapes and nothing else:

```css
@font-face {
  font-family: "Display fallback";
  src: local("Georgia");
  size-adjust: 104%;
  ascent-override: 90%;
  descent-override: 22%;
}
```

The override values are **measured against the real face**, not copied from here — an
unmeasured `size-adjust` is a CLS source pretending to be a fix. This is the row that
makes CLS ≤ 0.05 reachable at all; see [`performance.md`](performance.md) § 2.

## WCAG 1.4.12 — the text-spacing survival test

Users may force `line-height: 1.5`, `paragraph-spacing: 2em`,
`letter-spacing: 0.12em`, `word-spacing: 0.16em`. **No content may be lost or clipped
under all four at once.** In practice this means one rule: never give a text container
a fixed `height`. `min-height` and let it grow.

Run it as an actual override in the browser, not as a thought experiment — the failure
is always a card, a badge or a hero with a hard-coded height, and it never looks broken
until the test runs.

## Intrinsic layout primitives

Prefer primitives that do the math over breakpoint-toggled columns:

```css
/* Cards that reflow with no media query at all. */
grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));

/* Toolbars and chip rows. */
flex-wrap: wrap;  flex: 1 1 <basis>;
```

`min(100%, 18rem)` is what stops the track overflowing below 18rem, which a bare
`minmax(18rem, 1fr)` does. The argument for the whole family, verbatim from the source:
*"a web layout that only works at the widths you happened to test is broken. Intrinsic
layouts survive widths you never tried."*

## Where the chain's own number wins

Every **†** row above, and why:

| Row | What binds instead |
|---|---|
| **Perf: LCP / INP / CLS, hero, JS, transfer** | [`performance.md`](performance.md) § 1 is the budget and gate **93** enforces it — LCP ≤ 1.8 s, CLS ≤ 0.05, hero ≤ 250 kB WebP, ≤ 2.5 MB at 1440, measured locally at 4× CPU. It also carries rows Appendix A has none of: long tasks during scroll, frame time, font count, DOM nodes, resting `will-change`, blurred area, and the scrubbed-clip budget. Read Appendix A's perf rows as the field-condition reference (CWV at the 75th percentile), never as the shipping bar |
| **Type: H1 fluid** | The clamp's *shape* ports; its 60 px ceiling does not. Against an 18 px body that is a 3.3× size contrast, and TASTE.md § 2.4 measured **5–15×** across 89 saved sources — *"En sida med 'h1 48 / h2 32 / p 16' finns inte i materialet."* Keep the formula, raise the max term to what the register earns |
| **Type: default scale ratio** | Same reason. 1.25 / 1.333 produce the missing middle TASTE § 2.4 says does not exist in the material: sub-heads are either small uppercase kickers (11–13 px, tracking 0.1–0.2em) or as large as the display. [`typography.md`](typography.md) carries the register values |
| **Type: families ≤ 2** | The chain runs a **2+1** discipline (display + text + mono) — see `SKILL.md` § Component branch. Two *text* families remains the ceiling |
| **Color: ramp space, 12 steps** | OKLCH ports and is the chain's colour space. The 12-step ramp is a derivation aid, not a token budget: [`house-physics.md`](house-physics.md) ships **8–10 named tokens and exactly one saturated accent**. Deriving twelve and shipping ten is fine; shipping twelve is not |
| **States: five per element** | [`interaction-and-states.md`](interaction-and-states.md) requires **eight** — the five here plus loading, error and success — and a `<Name>.preview.html` rendering all of them |
| **Motion: UI transition, animate only** | [`motion.md`](motion.md) governs: three duration buckets (100–150 / 200–300 / 300–500 ms), exits ~75 % of the enter, three named easing tokens. The 150–300 ms band applies to **state** motion and not to a scroll-driven act, whose duration is the reader's hand. [`performance.md`](performance.md) § 3 adds `filter` to the composited list. `Motion: flashes/sec < 3` is **not** superseded — WCAG 2.3.1 is a safety limit, explicitly preserved by F-011 |
| **Conversion: pricing tiers 3, "how it works" steps 3** | Not binding. These are the canonical landing spine, which is exactly what TASTE.md § 5 rejects as cookie-cutter — three equal feature cards appear four times in 89 saved sources and all four are AI templates. Section count comes from the content, per [`structure.md`](structure.md). *"Primary CTAs per viewport ≤ 1"* does bind, corroborated independently by `cognitive-accessibility`'s "one primary action per screen" |

## The rule that makes the file usable

A number you did not measure on the actual page is not a pass. Quoting a floor from
this table in a review, without the measurement beside it, is the same failure as
inventing a metric in copy — see [`performance.md`](performance.md) § 6 and gate **46**.

## Related

[`typography.md`](typography.md) · [`layout-and-space.md`](layout-and-space.md) ·
[`color.md`](color.md) · [`performance.md`](performance.md) ·
[`responsive.md`](responsive.md) · [`page-mechanics.md`](page-mechanics.md) ·
`~/.agents/skills/power-design/principles/web-principles.md` (Appendix A, §§ 1, 3, 10) ·
`design-catalogue/TASTE.md` §§ 2, 5.
