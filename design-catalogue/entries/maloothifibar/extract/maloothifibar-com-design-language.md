# Design Language: MALOOT | HiFi Bar & Cocktails in Vieux-Lille

> Extracted from `https://www.maloothifibar.com` on September 4, 2026
> 1669 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#191313` | rgb(25, 19, 19) | hsl(0, 14%, 9%) | 1252 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#efeeec` | hsl(40, 9%, 93%) | 1412 |
| `#a8a99e` | hsl(65, 6%, 64%) | 745 |
| `#000000` | hsl(0, 0%, 0%) | 55 |

### Background Colors

Used on large-area elements: `#a8a99e`, `#191313`, `#131313`

### Text Colors

Text color palette: `#000000`, `#191313`, `#f1f1f1`, `#a8a99e`, `#efeeec`

### Gradients

```css
background-image: linear-gradient(90deg, rgb(25, 19, 19), rgba(25, 19, 19, 0));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#efeeec` | text, border, background | 1412 |
| `#191313` | text, border, background | 1252 |
| `#a8a99e` | background, text, border | 745 |
| `#000000` | text, border, background | 55 |

## Typography

### Font Families

- **Times Now** — used for all (1513 elements)
- **Inter Tight** — used for all (127 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 49px | 3.0625rem | 300 | 49px | -2.45px | h1, br, h2, div |
| 22.75px | 1.4219rem | 700 | 22.75px | -0.2275px | h2 |
| 17.5px | 1.0938rem | 700 | 17.5px | -0.175px | h3, h4, p, div |
| 15.75px | 0.9844rem | 400 | 18.9px | -0.4725px | a |
| 14px | 0.875rem | 400 | normal | normal | html, head, style, meta |
| 12.25px | 0.7656rem | 300 | 14.7px | -0.42px | div, p |
| 10.5px | 0.6563rem | 300 | 13.125px | 0.21px | div |

### Heading Scale

```css
h1 { font-size: 49px; font-weight: 300; line-height: 49px; }
h2 { font-size: 22.75px; font-weight: 700; line-height: 22.75px; }
h3 { font-size: 17.5px; font-weight: 700; line-height: 17.5px; }
h3 { font-size: 14px; font-weight: 400; line-height: normal; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`300` (1602x), `400` (41x), `700` (24x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-28 | 28px | 1.75rem |
| spacing-35 | 35px | 2.1875rem |
| spacing-70 | 70px | 4.375rem |
| spacing-88 | 88px | 5.5rem |
| spacing-105 | 105px | 6.5625rem |
| spacing-112 | 112px | 7rem |
| spacing-119 | 119px | 7.4375rem |
| spacing-140 | 140px | 8.75rem |
| spacing-154 | 154px | 9.625rem |
| spacing-168 | 168px | 10.5rem |
| spacing-175 | 175px | 10.9375rem |
| spacing-191 | 191px | 11.9375rem |
| spacing-201 | 201px | 12.5625rem |
| spacing-236 | 236px | 14.75rem |
| spacing-252 | 252px | 15.75rem |
| spacing-296 | 296px | 18.5rem |
| spacing-335 | 335px | 20.9375rem |
| spacing-343 | 343px | 21.4375rem |
| spacing-387 | 387px | 24.1875rem |

## CSS Custom Properties

### Colors

```css
--light-theme--set-tile-color: #191313;
```

### Typography

```css
--light-theme--text: #191313;
--font--sans-serif: "Inter Tight",Arial,sans-serif;
--light-theme--revert-text: #a8a99e;
--font--serif: "Times Now","Times New Roman",sans-serif;
--light-theme--button-text: #f1f1f1;
```

### Other

```css
--overlay-20: #0003;
--transparent: #fff0;
--grey: #a8a99e;
--light-theme--background: #a8a99e;
--light-theme--button-background: #191313;
--overlay-60: #0009;
--light-theme--revert-background: #191313;
--white: #f1f1f1;
--overlay-40: #0006;
--overlay-08: #00000014;
--dark: #191313;
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
| sm | 479px | max-width |
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 991px | max-width |
| lg | 992px | min-width |
| 2xl | 1600px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.45s`, `0.25s`, `0.2s`, `0.3s`, `0.8s`, `1s`, `0.04s`, `0.08s`, `0.12s`, `0.16s`, `0.24s`, `0.28s`, `0.32s`, `0.55s`, `0.15s`, `0.35s`

### Common Transitions

```css
transition: all;
transition: color 0.45s cubic-bezier(0.23, 1, 0.32, 1), padding 0.45s cubic-bezier(0.23, 1, 0.32, 1), background-color 0.45s cubic-bezier(0.23, 1, 0.32, 1);
transition: opacity 0.25s;
transition: opacity 0.2s;
transition: color 0.2s, background-color 0.2s;
transition: transform 0.45s cubic-bezier(0.23, 1, 0.32, 1);
transition: opacity 0.3s;
transition: opacity 0.3s, transform 0.8s cubic-bezier(0.19, 1, 0.22, 1);
transition: opacity 0.3s, filter 0.3s, transform 1s cubic-bezier(0.19, 1, 0.22, 1);
transition: opacity 0.3s 0.04s, filter 0.3s 0.04s, transform 1s cubic-bezier(0.19, 1, 0.22, 1) 0.04s;
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (15 instances)

```css
.button {
  color: rgb(25, 19, 19);
  font-size: 14px;
  font-weight: 300;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Links (37 instances)

```css
.link {
  color: rgb(25, 19, 19);
  font-size: 14px;
  font-weight: 300;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: rgb(241, 241, 241);
  padding-top: 17.5px;
  padding-bottom: 17.5px;
  padding-left: 0px;
  padding-right: 0px;
  position: fixed;
}
```

### Footer (13 instances)

```css
.foote {
  background-color: rgb(25, 19, 19);
  color: rgb(25, 19, 19);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 14px;
}
```

### Modals (5 instances)

```css
.modal {
  background-color: rgb(25, 19, 19);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (23 instances)

```css
.dropdown {
  background-color: rgb(25, 19, 19);
  border-radius: 0px;
  border-color: rgb(241, 241, 241);
  padding-top: 0px;
}
```

### Badges (40 instances)

```css
.badge {
  color: rgb(241, 241, 241);
  font-size: 10.5px;
  font-weight: 300;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Switches (11 instances)

```css
.switche {
  background-color: rgb(241, 241, 241);
  border-radius: 0px;
  border-color: rgb(241, 241, 241);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 14 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(241, 241, 241);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(241, 241, 241);
  font-size: 14px;
  font-weight: 300;
```

**Variant 2** (12 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(25, 19, 19);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(25, 19, 19);
  font-size: 14px;
  font-weight: 300;
```

### Button — 10 instances, 2 variants

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(241, 241, 241);
  padding: 8.75px 14px 8.75px 14px;
  border-radius: 0px;
  border: 0px none rgb(241, 241, 241);
  font-size: 14px;
  font-weight: 300;
```

**Variant 2** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(25, 19, 19);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(25, 19, 19);
  font-size: 10.5px;
  font-weight: 300;
```

### Button — 14 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgb(241, 241, 241);
  color: rgb(241, 241, 241);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(241, 241, 241);
  font-size: 14px;
  font-weight: 300;
```

**Variant 2** (12 instances)

```css
  background: rgb(25, 19, 19);
  color: rgb(25, 19, 19);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(25, 19, 19);
  font-size: 14px;
  font-weight: 300;
```

### Button — 34 instances, 2 variants

**Variant 1** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(241, 241, 241);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(241, 241, 241);
  font-size: 14px;
  font-weight: 300;
```

**Variant 2** (14 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(25, 19, 19);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(25, 19, 19);
  font-size: 14px;
  font-weight: 300;
```

### Button — 12 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(241, 241, 241);
  padding: 3.5px 3.5px 3.5px 7px;
  border-radius: 0px;
  border: 0px none rgb(241, 241, 241);
  font-size: 14px;
  font-weight: 300;
```

**Variant 2** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(25, 19, 19);
  padding: 3.5px 3.5px 3.5px 7px;
  border-radius: 0px;
  border: 0px none rgb(25, 19, 19);
  font-size: 14px;
  font-weight: 300;
```

## Layout System

**20 grid containers** and **296 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1680px | 42px |
| 2000px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 12x |
| 12-column | 7x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px;
gap: 14px;
grid-template-columns: 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px;
gap: 14px;
grid-template-columns: 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px;
gap: 14px;
grid-template-columns: 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px;
gap: 14px;
grid-template-columns: 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px 88px;
gap: 14px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 265x |
| column/nowrap | 31x |

**Gap values:** `10.5px`, `14px`, `154px`, `168px`, `2.8px`, `21px`, `28px`, `3.5px 21px`, `42px`, `7px`, `80.5px`, `normal 14px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 100/100 |
| Spacing System | 70/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 47 !important rules — prefer specificity over overrides
- 66% of CSS is unused — consider purging
- 1576 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 90deg | 2 | brand |

```css
background: linear-gradient(90deg, rgb(25, 19, 19), rgba(25, 19, 19, 0));
```

## Z-Index Map

**6 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,100 | nav.m.e.n.u |
| sticky | 50,50 | div.t.h.e.m.e._.s.w.i.t.c.h.-.c.o.m.p.o.n.e.n.t. .h.i.d.e.-.m.o.b.i.l.e.-.l |
| base | 0,3 | div.h.e.r.o._.b.g, div.d.r.i.n.k.s._.g.a.l.l.e.r.y.-.c.m.s. .d.i.v.-.h.i.d.e. .w.-.d.y.n.-.l.i.s.t, div.d.r.i.n.k._.g.a.l.l.e.r.y.-.i.t.e.m. .w.-.d.y.n.-.i.t.e.m |

## SVG Icons

**9 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 5 |
| md | 2 |
| xl | 2 |

**Icon colors:** `currentcolor`, `#F1F1F1`, `white`, `#191313`, `currentColor`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| Inter Tight | self-hosted | 300, 700 | normal |
| Times Now | self-hosted | 300, 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 31 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 16 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 11 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (30x), 3:2 (6x), 6.25:1 (6x), 2:3 (6x), 14.3:1 (3x), 1:1 (2x), 16:9 (1x), 7.12:1 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `40ms` | 40 |
| `xs` | `120ms` | 120 |
| `sm` | `160ms` | 160 |
| `md` | `280ms` | 280 |
| `lg` | `450ms` | 450 |
| `xl` | `800ms` | 800 |

### Easing Families

- **ease-out** (191 uses) — `cubic-bezier(0.23, 1, 0.32, 1)`, `cubic-bezier(0.19, 1, 0.22, 1)`, `cubic-bezier(0.075, 0.82, 0.165, 1)`
- **linear** (120 uses) — `linear`

## Component Anatomy

### button — 84 instances

**Slots:** label
**Sizes:** small · large

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **listen** (50)
- **book** (15)
- **visit** (5)

### Button Copy Patterns

- "listen" (30×)
- "listen
listen" (20×)
- "book a table" (9×)
- "book a table
book a table" (6×)
- "visit our youtube channel" (3×)
- "visit our youtube channel
visit our youtube channel" (2×)

### Sample Headings

> Hifi Bar

> Cocktails
> Vinyls
> Located in the heart of
Vieux-Lille, Maloot officially
opened its doors in early February
2024 and has been buzzing ever
since.
> Discover unique signature
cocktails, our selection of
champagnes, and premium spirits.
> Chicago
> Maïlen
> Voyagerz
> Espresso Love
> A place where every detail is designed to
feel warm and intimate, yet infused with
a festive energy that builds as the night
unfolds.

## Page Intent

**Type:** `landing` (confidence 0.59)
**Description:** Experience bold craft cocktails and vinyl DJ sets at Maloot, Lille's premier audiophile bar. Located in Vieux-Lille. Book your table today.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → hero → hero → content → gallery → content → testimonial → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | hero | Hifi Bar
 | 0.85 |
| 2 | hero | Located in the heart of
Vieux-Lille, Maloot officially
opened its doors in early | 0.4 |
| 3 | content | Discover unique signature
cocktails, our selection of
champagnes, and premium sp | 0.3 |
| 4 | gallery | A place where every detail is designed to
feel warm and intimate, yet infused wi | 0.7 |
| 5 | content | PREVIOUS SETS | 0.3 |
| 6 | testimonial | — | 0.8 |
| 7 | content | — | 0.3 |
| 8 | footer | Come join us —
and experience what Maloot is all about. | 0.95 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.079 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `photography` (confidence 0.39)
**Counts:** total 59, svg 7, icon 0, screenshot-like 0, photo-like 44
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Times Now` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
