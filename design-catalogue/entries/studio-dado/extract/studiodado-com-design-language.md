# Design Language: Home - Studio Dado

> Extracted from `https://www.studiodado.com/` on September 4, 2026
> 502 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 653 |
| `#ffffff` | hsl(0, 0%, 100%) | 358 |
| `#1b1b1c` | hsl(240, 2%, 11%) | 22 |
| `#5d5346` | hsl(34, 14%, 32%) | 5 |

### Background Colors

Used on large-area elements: `#5d5346`, `#ffffff`, `#1b1b1c`, `#000000`

### Text Colors

Text color palette: `#000000`, `#ffffff`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 653 |
| `#ffffff` | background, text, border | 358 |
| `#1b1b1c` | background, border | 22 |
| `#5d5346` | background | 5 |

## Typography

### Font Families

- **sans** — used for all (443 elements)
- **disp** — used for all (59 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 187.733px | 11.7333rem | 400 | 150.187px | -3.75467px | h2, span, div |
| 138.24px | 8.64rem | 400 | 110.592px | -2.7648px | h1, div, span, h2 |
| 59.7333px | 3.7333rem | 400 | 60.928px | -1.19467px | p, div, h2 |
| 34.1333px | 2.1333rem | 400 | 40.96px | -0.341333px | div, nav, ul, li |
| 25.6px | 1.6rem | 400 | 28.16px | -0.341333px | div, span, h3, b |
| 17.0667px | 1.0667rem | 400 | 20.48px | -0.341333px | body, div, svg, path |
| 11.9467px | 0.7467rem | 400 | 14.336px | -0.341333px | p, div, span, a |
| 8.53333px | 0.5333rem | 400 | 10.24px | normal | html, head, meta, link |

### Heading Scale

```css
h2 { font-size: 187.733px; font-weight: 400; line-height: 150.187px; }
h1 { font-size: 138.24px; font-weight: 400; line-height: 110.592px; }
h2 { font-size: 59.7333px; font-weight: 400; line-height: 60.928px; }
h3 { font-size: 25.6px; font-weight: 400; line-height: 28.16px; }
h3 { font-size: 17.0667px; font-weight: 400; line-height: 20.48px; }
```

### Body Text

```css
body { font-size: 17.0667px; font-weight: 400; line-height: 20.48px; }
```

### Font Weights in Use

`400` (497x), `500` (4x), `700` (1x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-9 | 9px | 0.5625rem |
| spacing-85 | 85px | 5.3125rem |
| spacing-120 | 120px | 7.5rem |
| spacing-154 | 154px | 9.625rem |
| spacing-208 | 208px | 13rem |
| spacing-239 | 239px | 14.9375rem |
| spacing-282 | 282px | 17.625rem |
| spacing-316 | 316px | 19.75rem |
| spacing-394 | 394px | 24.625rem |
| spacing-444 | 444px | 27.75rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| full | 9999px | 5 |

## CSS Custom Properties

### Colors

```css
--wp-block-synced-color: #7a00df;
--wp-block-synced-color--rgb: 122,0,223;
--wp-bound-block-color: var(--wp-block-synced-color);
--wp-admin-theme-color: #007cba;
--wp-admin-theme-color--rgb: 0,124,186;
--wp-admin-theme-color-darker-10: #006ba1;
--wp-admin-theme-color-darker-10--rgb: 0,107,160.5;
--wp-admin-theme-color-darker-20: #005a87;
--wp-admin-theme-color-darker-20--rgb: 0,90,135;
--wp-admin-border-width-focus: 2px;
```

### Spacing

```css
--wp--preset--font-size--normal: 16px;
--wp--preset--font-size--huge: 42px;
--size: 402;
```

### Other

```css
--wp-editor-canvas-background: #ddd;
--clamp: 13px;
--admin-bar-height: 32px;
```

### Dependencies

```css
--wp-bound-block-color: --wp-block-synced-color;
```

### Semantic

```css
success: [object Object];
warning: [object Object];
error: [object Object];
info: [object Object];
```

## Breakpoints

| Name | Value | Type |
|------|-------|------|
| sm | 600px | max-width |
| sm | 640px | max-width |
| sm | 650px | min-width |
| md | 768px | min-width |
| lg | 1024px | min-width |
| xl | 1280px | min-width |
| 1440px | 1440px | min-width |
| 1920px | 1920px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.5s`, `1s`

### Common Transitions

```css
transition: all;
transition: transform 0.5s;
transition: color 0.5s cubic-bezier(0.23, 1, 0.32, 1), background-color 0.5s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.5s cubic-bezier(0.23, 1, 0.32, 1), text-decoration-color 0.5s cubic-bezier(0.23, 1, 0.32, 1), fill 0.5s cubic-bezier(0.23, 1, 0.32, 1), stroke 0.5s cubic-bezier(0.23, 1, 0.32, 1);
transition: transform 1s cubic-bezier(0.23, 1, 0.32, 1);
transition: 0.5s cubic-bezier(0.23, 1, 0.32, 1);
transition: 0.5s;
transition: opacity 0.5s ease-in-out;
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (9 instances)

```css
.button {
  color: rgb(255, 255, 255);
  font-size: 17.0667px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (4 instances)

```css
.card {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (1 instances)

```css
.input {
  background-color: rgb(85, 77, 66);
  color: rgb(255, 255, 255);
  border-color: rgb(255, 255, 255);
  border-radius: 0px;
  font-size: 17.0667px;
  padding-top: 17.0667px;
  padding-right: 25.6px;
}
```

### Links (47 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 17.0667px;
  font-weight: 400;
}
```

### Navigation (10 instances)

```css
.navigatio {
  color: rgb(255, 255, 255);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(93, 83, 70);
  color: rgb(255, 255, 255);
  padding-top: 25.6px;
  padding-bottom: 34.1333px;
  font-size: 17.0667px;
}
```

### Modals (1 instances)

```css
.modal {
  background-color: rgba(27, 27, 28, 0.35);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (29 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(255, 255, 255);
  padding-top: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 6 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(255, 255, 255);
  font-size: 17.0667px;
  font-weight: 400;
```

**Variant 2** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 17.0667px;
  font-weight: 400;
```

### Other — 12 instances, 2 variants

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(255, 255, 255);
  font-size: 17.0667px;
  font-weight: 400;
```

**Variant 2** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 17.0667px;
  font-weight: 400;
```

### Link — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 17.0667px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(85, 77, 66);
  color: rgb(255, 255, 255);
  padding: 17.0667px 25.6px 17.0667px 25.6px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 17.0667px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 17.0667px 25.6px 17.0667px 25.6px;
  border-radius: 0px;
  border: 0px solid rgb(255, 255, 255);
  font-size: 17.0667px;
  font-weight: 400;
```

## Layout System

**17 grid containers** and **54 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1066.67px | 0px |
| 1237.33px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 24-column | 16x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 35.5469px 35.5469px 35.5625px 35.5625px 35.5469px 35.5469px 35.5625px 35.5625px 35.5625px 35.5625px 35.5469px 35.5469px 35.5625px 35.5625px 35.5625px 35.5625px 35.5469px 35.5469px 35.5625px 35.5625px 35.5625px 35.5625px 35.5469px 35.5469px;
gap: normal 17.0667px;
grid-template-columns: 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px;
gap: 34.1333px 17.0667px;
grid-template-columns: 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px;
gap: 51.2px 17.0667px;
grid-template-columns: 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px;
gap: 17.0667px;
grid-template-columns: 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px 35.5469px;
gap: 51.2px 17.0667px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 45x |
| column/nowrap | 9x |

**Gap values:** `1.70667px normal`, `17.0667px`, `17.0667px normal`, `34.1333px 17.0667px`, `4.26667px 17.0667px`, `51.2px 17.0667px`, `normal 17.0667px`, `normal 4.26667px`, `normal 8.53333px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 85/100 |
| Typography Consistency | 100/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- No clear primary brand color detected
- 24 !important rules — prefer specificity over overrides
- 67% of CSS is unused — consider purging
- 406 duplicate CSS declarations

## Z-Index Map

**5 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9999,9999 | div.f.i.x.e.d. .i.n.s.e.t.-.0. .b.g.-.b.r.o.w.n. .z.-.[.9.9.9.9.]. .f.l.e.x. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .j.s.-.t.-.p.r.e.l.o.a.d.e.r. .o.r.i.g.i.n.-.c.e.n.t.e.r, div.f.i.x.e.d. .i.n.s.e.t.-.0. .p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .f.l.e.x. .z.-.[.9.9.9.9.]. .o.p.a.c.i.t.y.-.0. .d.a.d.o.-.g.r.i.d |
| dropdown | 999,999 | header.f.i.x.e.d. .t.o.p.-.0. .l.e.f.t.-.0. .r.i.g.h.t.-.0. .z.-.[.9.9.9.] |
| sticky | 50,99 | div.f.i.x.e.d. .i.n.s.e.t.-.0. .b.g.-.b.l.a.c.k./.3.5. .z.-.[.5.0.]. .o.p.a.c.i.t.y.-.0. .p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .j.s.-.t.-.o.v.e.r.l.a.y, div.f.i.x.e.d. .i.n.s.e.t.-.0. .b.g.-.w.h.i.t.e. .z.-.[.9.9.]. .j.s.-.t.-.m.a.s.k, div.j.s.-.m.e.n.u. .m.o.b.i.l.e.-.m.e.n.u. .f.i.x.e.d. .t.o.p.-.0. .l.e.f.t.-.0. .r.i.g.h.t.-.0. .b.o.t.t.o.m.-.0. .b.g.-.[.#.0.0.0.]. .z.-.[.9.9.]. .h.-.f.u.l.l. .t.e.x.t.-.w.h.i.t.e. .p.t.-.1.8.0 |
| base | 1,1 | div.s.e.c.t.i.o.n.s. .r.e.l.a.t.i.v.e. .b.g.-.w.h.i.t.e. .z.-.1, div.j.s.-.p.r.e.l.o.a.d.-.l.i.n.e. .r.e.l.a.t.i.v.e. .h.-.[.1.p.x.]. .b.g.-.w.h.i.t.e./.1.0. .w.-.f.u.l.l. .z.-.1. .o.r.i.g.i.n.-.l.e.f.t, div.r.e.l.a.t.i.v.e. .w.-.f.u.l.l. .h.-.f.u.l.l. .z.-.1 |

## SVG Icons

**2 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| md | 1 |
| lg | 1 |

**Icon colors:** `rgb(255, 255, 255)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| disp | self-hosted | normal | normal |
| sans | self-hosted | normal | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 4 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (3x), 3:4 (3x), 4:3 (1x), 2:3 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **ease-out** (29 uses) — `cubic-bezier(0.23, 1, 0.32, 1)`
- **ease-in-out** (8 uses) — `ease`

## Component Anatomy

### other — 12 instances


### button — 8 instances

**Slots:** label, icon

### link — 4 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **approach** (2)
- **all** (1)
- **ap** (1)
- **allura** (1)
- **serene** (1)
- **grand** (1)
- **see** (1)
- **more** (1)

### Button Copy Patterns

- "approach" (2×)
- "all projects" (1×)
- "ap house miami

featured project" (1×)
- "allura vista suite

guestrooms & suites" (1×)
- "serene spa and wellness

spa & fitness" (1×)
- "grand atrium

public spaces" (1×)
- "see all blog articles" (1×)
- "more about studio dado" (1×)
- "contact" (1×)
- "→" (1×)

### Sample Headings

> FORM
FOLLOWS
FEELING
> FEATURED
PROJECTS
> AP House Miami
> Allura Vista Suite
> Serene Spa and Wellness
> OUR BLOG IS A BRIGHT, EVER-EVOLVING
PLATFORM WHERE OUR IDEAS, OUR
CULTURE AND OUR PERSPECTIVE LIVE AND
BREATHE.
> Slow Travel and the Future of Cruise Design
> The Return of Authenticity
> C+F Cover Story: A Decade of Redefining Cruise Design

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Studio DADO is a boutique interior design firm specializing in hospitality spaces for some of the most well-known brands in the world.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → feature-grid → nav → nav → nav → nav → nav → nav → content → content → footer → nav → nav → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | nav | — | 0.9 |
| 5 | nav | — | 0.9 |
| 6 | nav | — | 0.9 |
| 7 | feature-grid | FORM
FOLLOWS
FEELING | 0.8 |
| 8 | content | — | 0.3 |
| 9 | content | OUR BLOG IS A BRIGHT, EVER-EVOLVING
PLATFORM WHERE OUR IDEAS, OUR
CULTURE AND OU | 0.3 |
| 10 | footer | — | 0.95 |
| 11 | nav | — | 0.9 |
| 12 | nav | — | 0.9 |
| 13 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.071 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.625)
**Counts:** total 8, svg 0, icon 0, screenshot-like 0, photo-like 8
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.424)

Evidence:
- tailwind-like class density 45%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `sans` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
