# Design Language: Contra Labs - Powered by Contra

> Extracted from `https://contralabs.com` on September 4, 2026
> 990 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fbfaf6` | rgb(251, 250, 246) | hsl(48, 38%, 97%) | 100 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 254 |
| Accent | `#f50c0c` | rgb(245, 12, 12) | hsl(0, 92%, 50%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1469 |
| `#2b2b29` | hsl(60, 2%, 16%) | 203 |
| `#a5beba` | hsl(170, 16%, 70%) | 15 |
| `#494444` | hsl(0, 4%, 28%) | 7 |
| `#918f66` | hsl(57, 17%, 48%) | 2 |
| `#918989` | hsl(0, 4%, 55%) | 1 |
| `#c8bcae` | hsl(32, 19%, 73%) | 1 |
| `#e4e2d9` | hsl(49, 17%, 87%) | 1 |
| `#83a5a0` | hsl(171, 16%, 58%) | 1 |

### Background Colors

Used on large-area elements: `#fbfaf6`, `#c8e1dd`, `#a5beba`, `#387478`, `#2b2b29`, `#918989`, `#c8bcae`, `#918f66`, `#296a6c`, `#eeede7`, `#e4e2d9`, `#f50c0c`, `#0cf523`, `#000000`, `#e7f2f0`, `#c8e0dc`, `#ffffff`, `#faf9f5`, `#fcfbf7`

### Text Colors

Text color palette: `#000000`, `#2b2b29`, `#0000ee`, `#fbfaf6`

### Gradients

```css
background-image: linear-gradient(rgb(251, 250, 246) 0%, rgb(254, 252, 248) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 1469 |
| `#0000ee` | text, border | 254 |
| `#2b2b29` | text, border, background | 203 |
| `#fbfaf6` | background, text, border | 100 |
| `#c8e1dd` | background | 17 |
| `#a5beba` | background | 15 |
| `#494444` | background | 7 |
| `#387478` | background | 4 |
| `#e7f2f0` | background | 3 |
| `#918f66` | background | 2 |
| `#918989` | background | 1 |
| `#c8bcae` | background | 1 |
| `#296a6c` | background | 1 |
| `#e4e2d9` | background | 1 |
| `#f50c0c` | background | 1 |
| `#0cf523` | background | 1 |
| `#83a5a0` | background | 1 |

## Typography

### Font Families

- **GT Standard L Regular** — used for body (69 elements)
- **Source Serif 4 Variable** — used for all (41 elements)
- **Times New Roman** — used for body (32 elements)
- **GT Standard 6 L Medium** — used for body (8 elements)
- **CUSTOMV2;GT Standard 6 L Regular** — used for body (7 elements)
- **GT Standard L Medium** — used for body (4 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 597.662px | 37.3539rem | 400 | 597.662px | -23.9065px | p |
| 354.9px | 22.1812rem | 400 | 319.41px | -17.745px | p |
| 328.936px | 20.5585rem | 400 | 328.936px | -13.1574px | p |
| 316.339px | 19.7712rem | 400 | 316.339px | -12.6535px | p |
| 311.21px | 19.4506rem | 400 | 311.21px | -12.4484px | p |
| 268px | 16.75rem | 400 | 241.2px | -13.4px | p |
| 228.851px | 14.3032rem | 400 | 205.966px | -11.4426px | p |
| 135.252px | 8.4533rem | 400 | 121.726px | -6.76258px | p |
| 64px | 4rem | 400 | 64px | -2.56px | h1 |
| 62px | 3.875rem | 400 | 62px | -2.48px | h5 |
| 56px | 3.5rem | 400 | 56px | -2.24px | h2, br |
| 44px | 2.75rem | 400 | 44px | -1.76px | h2 |
| 42.6667px | 2.6667rem | 400 | 42.6667px | normal | h2 |
| 32px | 2rem | 400 | 32px | -1.6px | h3, span, br |
| 29.3333px | 1.8333rem | 400 | 29.3333px | normal | p |

### Heading Scale

```css
h1 { font-size: 64px; font-weight: 400; line-height: 64px; }
h5 { font-size: 62px; font-weight: 400; line-height: 62px; }
h2 { font-size: 56px; font-weight: 400; line-height: 56px; }
h2 { font-size: 44px; font-weight: 400; line-height: 44px; }
h2 { font-size: 42.6667px; font-weight: 400; line-height: 42.6667px; }
h3 { font-size: 32px; font-weight: 400; line-height: 32px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (978x), `500` (12x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-60 | 60px | 3.75rem |
| spacing-74 | 74px | 4.625rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-120 | 120px | 7.5rem |
| spacing-160 | 160px | 10rem |
| spacing-184 | 184px | 11.5rem |
| spacing-200 | 200px | 12.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 8px | 36 |
| xl | 24px | 19 |
| full | 99px | 6 |
| full | 10000px | 16 |

## CSS Custom Properties

### Other

```css
--one-if-corner-shape-supported: 1;
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
| md | 809px | max-width |
| md | 810px | min-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | min-width |
| 1439px | 1439px | max-width |
| 2xl | 1599px | max-width |
| 2xl | 1600px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.001s`, `0.32s`, `0.35s`

### Common Transitions

```css
transition: overflow 0.001s allow-discrete;
transition: all;
transition: width 0.32s cubic-bezier(0.22, 1, 0.36, 1), transform 0.32s cubic-bezier(0.22, 1, 0.36, 1);
transition: opacity 0.35s;
transition: transform 0.32s cubic-bezier(0.22, 1, 0.36, 1);
```

### Keyframe Animations

**__framer-loading-spin**
```css
@keyframes __framer-loading-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Links (39 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 12px;
  font-weight: 400;
}
```

### Switches (1 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
}
```

## Layout System

**5 grid containers** and **334 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 600px | 0px |
| 560px | 0px |
| 1600px | 100px |
| 100% | 0px |
| 900px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 8-column | 4x |
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 497.5px 497.5px;
gap: 5px;
grid-template-columns: 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px;
gap: 0px 5px;
grid-template-columns: 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px;
gap: 0px 5px;
grid-template-columns: 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px;
gap: 0px 5px;
grid-template-columns: 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px 150.625px;
gap: 0px 5px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 246x |
| row/nowrap | 87x |
| row/wrap | 1x |

**Gap values:** `0px 5px`, `10px`, `12px`, `16px`, `18px`, `20px`, `24px`, `2px`, `30px`, `32px`, `40px`, `4px`, `5px`, `60px`, `6px`, `7.74px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 81/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 40/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 6 font families — consider limiting to 2 (heading + body)
- 24 distinct font sizes — consider a tighter type scale
- 18 !important rules — prefer specificity over overrides
- 4815 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |

```css
background: linear-gradient(rgb(251, 250, 246) 0%, rgb(254, 252, 248) 100%);
```

## Z-Index Map

**11 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.1.t.g.5.9.e.h.-.c.o.n.t.a.i.n.e.r |
| base | 0,9 | div, div.f.r.a.m.e.r.-.1.v.c.e.e.4.o, div.f.r.a.m.e.r.-.b.p.q.c.6.v |

**Issues:**
- [object Object]

## SVG Icons

**6 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 2 |
| md | 3 |
| xl | 1 |

**Icon colors:** `rgb(0, 0, 0)`, `var(--token-41862f85-d984-4269-90b9-0c207a5502ff, rgb(43, 43, 41))`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Source Serif 4 | cdn | 400, 700 | italic, normal |
| Source Serif 4 Variable | cdn | 400 | normal |
| GT Standard L Regular | self-hosted | 400 | normal |
| GT Standard L Bold | self-hosted | 700 | normal |
| GT Standard L Medium | self-hosted | 500 | normal |
| GT Standard 6 L Medium | self-hosted | 500 | normal |
| GT Standard 6 L Semibold | self-hosted | 600 | normal |
| GT Standard L Semibold | self-hosted | 600 | normal |
| GT Standard L Light | self-hosted | 300 | normal |
| Inter | self-hosted | 400, 500, 700, 900 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 17 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 16 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 6 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (17x), 3:4 (16x), 4:3 (5x), 3:2 (2x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |
| `md` | `320ms` | 320 |

### Easing Families

- **ease-out** (6 uses) — `cubic-bezier(0.22, 1, 0.36, 1)`

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** The frontier human data and evaluation lab for creative AI. 1.5M+ verified creative experts setting the benchmark for style, tone, and taste with next-gen creative tools.

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.307 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 10000px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 40, svg 0, icon 6, screenshot-like 0, photo-like 0
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `vuetify` (confidence 0.56)

Evidence:
- 13 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `GT Standard L Regular` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
