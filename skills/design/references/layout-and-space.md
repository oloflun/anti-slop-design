# Layout and space

> **Diverges from upstream Hallmark: T6 port (2026-09-09).** This file has been
> extended with material ported from the upstream packages named in the design
> chain's v4 plan, sections 2.1 to 2.5. Every addition is traceable to a source
> file; where a port collided with a rule already in this file, the conflict is
> resolved in the text and the winner is named. Upstream is no longer the bar
> here, and `verify-design-system.py` records the divergence rather than
> treating it as drift.

Layout is where "AI-generated" gets caught. Equal columns, everything centred, every card identical — these are the tells.

## Principles

- A layout has a **primary axis**. Left-biased, right-biased, top-heavy, or bottom-weighted. Centre-biased is a default, not a choice.
- **Asymmetry reads as intentional.** Symmetry reads as generated. When in doubt, shift.
- **Spacing is a scale, not a value.** Pick one scale. Use it everywhere. Don't type raw px.
- **Varied spacing.** If every gap is 24px, the page is a template. Mix small, medium, and large gaps within the same layout.
- **Break the grid on purpose.** A page with one element crossing the grid is stronger than a page that never does.

## The spacing scale

4pt base. Nine steps. Named by role, not size.

```css
:root {
  --space-3xs: 0.125rem;  /*  2px */
  --space-2xs: 0.25rem;   /*  4px */
  --space-xs:  0.5rem;    /*  8px */
  --space-sm:  0.75rem;   /* 12px */
  --space-md:  1rem;      /* 16px */
  --space-lg:  1.5rem;    /* 24px */
  --space-xl:  2.5rem;    /* 40px */
  --space-2xl: 4rem;      /* 64px */
  --space-3xl: 6rem;      /* 96px */
  --space-4xl: 9rem;      /* 144px */
}
```

- Use `gap` for sibling spacing. It's cleaner than stacked margins, it participates in flex/grid, and it collapses predictably.
- Use `margin` only for optical adjustments or breaking out of the flow. Never `margin` for a list of siblings.

**Why 4pt and not 8pt.** An 8pt system is too coarse — you keep needing the 12px that sits between 8 and 16 (impeccable `spatial-design.md`: *"Use 4pt for granularity: 4, 8, 12, 16, 24, 32, 48, 64, 96px"*). **Conflict, resolved:** where impeccable's ladder and the scale above differ (it has 32 and 48 where this file has 40 and 144), **the scale printed above wins** — it is what the worked examples use and what `measure.py` reads. What ports is the rule underneath it: every step is a multiple of 4, and nothing off the scale is ever typed.

**Name by relationship, not by value.** `--space-lg`, never `--spacing-24`. A token named for its size cannot be retuned; a token named for its role can.

**Tie the scale to the type.** The body's line box is the vertical unit. At 16px / 1.5 that is 24px, so 12 · 24 · 48 · 72 are the steps that land on the text's own rhythm (Refero `typography.md` § 7 derives its whole spacing set as `0.5 ×` / `1 ×` / `2 ×` / `3 ×` line-height). Refero's summary of why: *"Spacing matters more than font size."* Two pages with the same faces and different spacing read as different products — fix spacing before touching a font.

**Active air before passive air.** Space *inside* a component — line-height, padding — is passive. Space *separating* sections is active. When a section feels cramped, increase the active air first; never crowd line-height or padding to buy room (power-design `design-principles.md` § 6).

## Grouping — the gaps carry the meaning

Three tools make a group, in order of preference: **negative space** (the default), **a background shape** (only where a group must read as one unit — a selectable row, a draggable card), **a separator line** (last resort, dense data only). A layout that reaches for lines first has not tried spacing.

- **The 2× rule.** The gap *between* groups is at least twice the gap *within* one. 8px inside → 16px+ between. Stated from the other side: **related spacing is at most half of unrelated spacing.** Below 2× the eye cannot find the edge, and no border repairs it — uniform spacing plus lines to compensate is the failure shape (`better-layout/grouping-and-alignment.md`).
- That makes it a measurable check, not a feeling: take any two adjacent gaps, one within a group and one between groups. If the between-gap is less than double the within-gap, the grouping is decorative.
- **Borderless controls need 2× the clearance of bordered ones** — 12px between adjacent bordered buttons or inputs, 24px around text and icon buttons, 24px+ between unrelated control groups. Nothing marks where a borderless target ends; the space *is* the boundary.
- **A label sits within 32px of the thing it labels.** Mayer's spatial contiguity, codified (power-design). A caption that drifts further reads as a new block, not as a caption.
- **Closure over enclosure.** The eye completes an implied shape, so not every line needs drawing: a single rule above a section, corner accents, a background that fades at its edge, consistent alignment instead of a drawn grid line. Remove borders iteratively and check whether the boundary is still perceived — if it is, the border was noise. Use a full border only when the boundary *is* the primary grouping signal, when it defines a hit area, or when the layout renders somewhere spacing collapses (`designer-skills/law-of-closure`).
- **Closure needs quiet around it.** The mind cannot close a shape it cannot isolate. Reduce the competing partial shapes before relying on an implied boundary.
- **Figure and ground get decided whether or not you decide them.** Figure: bounded, higher contrast, richer detail, smaller area, in front. Ground: unbounded, flatter, larger, behind. Ambiguous figure-ground is a technique in art and a failure in UI — a card whose luminance sits between the page and the overlay, nested elevation with no contrast step between levels, text laid straight onto photography with no separation layer. Test it by removing colour: if foreground and background are still separable by shape and contrast alone, it holds (`designer-skills/law-of-figure-ground`).

## The squint test

Blur your eyes, or screenshot the page and blur it. Can you still name the most important element? The second? The groupings? **If everything reads at the same weight blurred, the hierarchy is decoration, not structure.**

Hierarchy runs on **2–3 dimensions at once**, never on size alone:

| Tool | Strong hierarchy | Weak hierarchy |
| --- | --- | --- |
| Size | ≥ 3:1 ratio | < 2:1 ratio |
| Weight | Bold vs regular | Medium vs regular |
| Colour | High contrast | Similar tones |
| Position | Top / leading | Bottom / trailing |
| Space | Surrounded by air | Crowded |

A heading that is larger *and* heavier *and* carries more air above it is a heading. A heading that is only 1.4× the body is a paragraph in a bigger font.

## Grids

- **Prefer CSS Grid** for page layout, **Flexbox** for component internals.
- `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` for fluid responsive grids without media queries.
- **Don't default to 3 columns of equal cards with icon-above-heading-above-copy.** This is *the* AI feature-grid. Break it: vary column widths with `grid-template-columns: 1.2fr 1fr 0.8fr`, or use a 12-column underlying grid and give each item a different span, or use 4-up with a 2-span hero, etc.
- Use **named grid areas** for complex layouts and rename them at breakpoints.
- **Grid over flex-math.** Never build columns out of flexbox percentage arithmetic — `width: calc(33% - 1rem)` and its family. Use Grid and let `gap` do the subtraction: `grid-template-columns: repeat(3, 1fr); gap: var(--space-lg)` (taste-skill § 3.E, *"NEVER use complex flexbox percentage math… ALWAYS use CSS Grid"*). Flex-math columns break the moment the gap or the item count changes. Flexbox stays right for component internals, where there is no column count to get wrong.
- **Container queries are for components; viewport queries are for pages.** A card in a narrow sidebar and the same card in the main column should each decide their own layout from the space they are actually in.

  ```css
  .card-list { container-type: inline-size; }

  @container (min-width: 400px) {
    .card { grid-template-columns: 120px 1fr; }
  }
  ```

  A component that reads `@media` where it should read `@container` is correct in exactly one column width — the one it was written in.
- **Hold the structure until it breaks.** Collapse late. Break where the layout actually stops fitting — the sidebar squeezes the measure below its floor, the card grid drops under a usable column width — not at 768px because a preset says so. Premature collapsing throws away space the user paid for. Test the smallest and the largest supported size first; those break first.
- **`gap: 1px` on a grid whose parent carries the rule colour** draws mathematically exact hairlines between cells with no border declarations and no doubled seams at the joins. The cheapest way to put a ledger or a spec table on true 1px lines. (From `industrial-brutalist-ui` § Grid Determinism — the *technique* ports; the CRT / ASCII / `#E61919` direction it belongs to does not, gate 60.)

## Asymmetry techniques

- **Wide left margin.** Treat the left as a permanent negative space — narrow column of labels, wide column of content. **Labels must NOT be section eyebrows / numbers paired with the heading** — that's gate-54-banned. Reserve this technique for body-level micro-labels (caption, footnote, date) alongside body copy.
- **Hanging headers.** ⚠️ **Opt-in only.** Section labels sit in the left margin; content flows to the right. Permitted only when the user explicitly asks for an editorial / hanging-header layout AND no eyebrow / number / chapter tag sits in the left margin. The eyebrow-left / heading-right pattern is banned by slop-test gate 54 — it's the most reliable templated-editorial AI tell. Default to a stacked single-column section head.
- **Offset grids.** Odd columns wider than even. Or the other way.
- **Grid-breaks.** One element that deliberately extends past a column boundary: a pull-quote, a photograph, a rule, a number.
- **Generous top, tight bottom** (or vice-versa). Sections don't need to be evenly padded.
- **Symmetric, or ≥ 15 % asymmetric — never near-symmetric.** The danger zone is the accidental middle: a 10px offset reads as a mistake, not a decision. Codified: if the distance from each side differs by ≤ 5 % of the width, snap it to true centre; otherwise push it to ≥ 15 % so the offset is legibly intentional (power-design `design-principles.md` § Symmetry, Tschichold's asymmetric counter-tradition against the Gestalt default). This is the threshold under house-physics' *"paired columns never top-align"* — the stagger has to be big enough to read as a stagger.
- **Alignment coherence.** A section head's horizontal alignment should be a deliberate choice that *coheres* with the body it introduces — match it (left head over left-flush body; centred head over symmetric / centred body) or break from it on purpose (a head that escapes an asymmetric grid). What reads as an AI mistake is the *accidental* mismatch: a narrow head block auto-centred (`margin-inline: auto` plus a `max-width` / `ch` cap) left floating over full-width, left-flush content beneath it. Centred, hanging, bottom-aligned, and asymmetric heads all stay on the table — the guard is intentionality, not uniformity.

## Depth

- Depth is **weight and scale**, not shadow. A heavier weight, a larger size, a warmer hue — these create hierarchy better than drop shadows.
- If you use shadow, use one:
  - **Whisper** — `0 1px 2px oklch(20% 0.01 <hue> / 0.05)` for hovering cards.
  - **Hairline** — `0 0 0 1px oklch(30% 0.01 <hue> / 0.06)` as an alternative to a 1px border.
- Never stack multiple shadows. Never use a coloured glow on a light background.
- Z-index has **six levels, named.** Don't freestyle numbers.

```css
:root {
  --z-base:     1;
  --z-raised:   10;
  --z-dropdown: 100;
  --z-sticky:   200;
  --z-modal:    400;
  --z-toast:    500;
  --z-tooltip:  600;
}
```

Add `--z-backdrop: 300` when a scrim is in play — impeccable's semantic ladder is dropdown → sticky → modal-backdrop → modal → toast → tooltip, and the scale above is the same ladder with `base` and `raised` beneath it. The point of a named scale is that the names, not the numbers, are what you reason about; `z-index: 9999` means somebody lost track of the ladder.

**Depth in a stack is distance, and distance is three channels at once: smaller, softer, lower-contrast.** The slideshow depth ladder is the worked version — centre `scale 1 / opacity 1 / blur 0`, ±1 `0.75 / 0.7 / 2px`, ±2 `0.6 / 0.4 / 4px`, out `0.5 / 0 / 6px`. **A parallax or an offset without the size, blur and contrast steps reads as sliding, not as depth** — that is the most common reason a layered scene looks cheap rather than deep. Note what the source does *not* use: no `rotateY`, no `perspective`, no 3D transforms at all. Scale, blur and opacity carry the whole effect (`slideshow` § card positioning math).

**A photograph on a light ground gets a 1px inner outline.**

```css
img { outline: 1px solid oklch(0 0 0 / 0.1); outline-offset: -1px; }
/* dark ground: oklch(1 0 0 / 0.1) — pure white at the same alpha */
```

Pure black or pure white only. Never a tinted near-black from the palette (`slate-900`, `#0a0a0a`, `#111827`) — a tinted outline picks up the surrounding surface colour and reads as dirt on the image edge — and never the accent or ink colour; the outline is a neutral separator, not a themed element. `outline` rather than `border` because it takes no layout space at any offset, and `outline-offset: -1px` draws the ring just inside the edge so it hugs the corner radius (`better-ui/surfaces.md`).

## Optical adjustments

Geometry and perception disagree, and perception is the one that ships.

- **Text at `margin-inline-start: 0` looks indented** — the letterform carries its own whitespace. Pull it back optically with roughly `-0.05em` where a display line has to align with a rule, an image edge, or the column above it.
- **Concentric radii: `outerRadius = innerRadius + padding`.** A 12px inner element inside 8px of padding needs a 20px outer radius. The same radius on both is the single most common thing that makes a nested surface feel off. Past 24px of padding the layers read as separate surfaces — pick each radius independently rather than forcing the math (`better-ui/surfaces.md`). Cross-check the result against the page's one radius scale (Shape Consistency Lock, gate 92): concentric math produces a *derived* value, not a new step on the scale.
- **Icon-side padding is the text side minus ~2px.** A button with a trailing icon and symmetric padding looks like the icon has been shoved out.
- **Play triangles shift right; arrows shift toward their direction.** Fix it in the SVG's `viewBox` or path where you can, so the component needs no compensating margin.
- Hit-target expansion via `::before { inset: … }` is the same family of trick, but [`interaction-and-states.md`](interaction-and-states.md) § Hit targets owns the number.

## Bans

- **Centre-aligned everything.** Headings + body + CTA all centred is the landing-page template every LLM emits.
- **`min-height: 100vh` hero with one centred sentence.** Stop.
- **Card-in-card.** A bordered container inside a bordered container. Pick one.
- **Identical feature grid.** Three columns, three icons, three two-line headings, three three-line bodies. Change *something*.
- **Equal padding on everything.** If the card padding equals the section padding equals the page padding, the rhythm is flat.
- **`z-index: 9999`** and other ad-hoc z values. Use the scale.
- **Shadow-on-dark accidental glow.** A drop shadow on a dark card creates a glow; that's wrong.

## Page-edge clipping

The clipped-edge enrichment archetype (E1) — and any other deliberately overflowing element (full-bleed marquee, oversized headline that exceeds the viewport on small screens, a tilted figure that pushes past a column) — needs a parent that *visually* shows the overflow without letting the document scroll horizontally.

The default is unsafe: a `width: calc(100% + 12vw)` figure inside a section with `overflow: visible` makes the document scroll horizontally on every viewport. The page feels broken on touch devices. Slop-test gate 34 fails on this.

**Always pair clipped-edge with a global clip.** At the top of the stylesheet:

```css
html { overflow-x: clip; }
body { overflow-x: clip; }   /* fallback for older Safari */
```

Use `overflow-x: clip` rather than `overflow-x: hidden`:

- `clip` preserves `position: sticky` and `position: fixed` on descendants.
- `hidden` creates a new scroll container, which breaks sticky and can trap focus on overflowing inputs.

The clipped-edge mockup keeps its visual extension; the page no longer scrolls horizontally. Same pattern works for full-bleed marquees, oversized headlines, and any deliberately-decorative overflow.

The hero or section that *contains* the overflowing element keeps `overflow: visible` (so the figure renders past the parent edge); the global clip on `html` and `body` is the only safety net needed.

## When in doubt

If the layout looks fine but flat, do one of these before shipping:

1. Add one break-out element.
2. Unbalance a column width.
3. Move the primary CTA out of the centre.
4. Remove a card and replace it with negative space.
5. Change one section's padding so the rhythm is uneven.
