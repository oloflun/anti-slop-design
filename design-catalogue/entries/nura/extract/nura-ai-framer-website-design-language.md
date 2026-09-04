# Design Language: Nura — Adaptive Daily Planning

> Extracted from `https://nura-ai.framer.website/` on September 4, 2026
> 2436 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 282 |
| Secondary | `#ff5f54` | rgb(255, 95, 84) | hsl(4, 100%, 66%) | 1 |
| Accent | `#ffbe32` | rgb(255, 190, 50) | hsl(41, 100%, 60%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 3647 |
| `#ffffff` | hsl(0, 0%, 100%) | 407 |
| `#1a1a1a` | hsl(0, 0%, 10%) | 229 |
| `#5d5d5d` | hsl(0, 0%, 36%) | 203 |
| `#464646` | hsl(0, 0%, 27%) | 120 |
| `#737373` | hsl(0, 0%, 45%) | 78 |
| `#242424` | hsl(0, 0%, 14%) | 44 |
| `#2e2e2e` | hsl(0, 0%, 18%) | 12 |
| `#ededed` | hsl(0, 0%, 93%) | 6 |
| `#8c8c8c` | hsl(0, 0%, 55%) | 6 |
| `#dae2d3` | hsl(92, 21%, 86%) | 1 |
| `#0e0b0f` | hsl(285, 15%, 5%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#f8f8f8`, `#1a1a1a`, `#fcfcfc`, `#1c1c1c`, `#000000`, `#000100`, `#dae2d3`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#ffffff`, `#464646`, `#1a1a1a`, `#737373`, `#8c8c8c`, `#5d5d5d`, `#e7543c`, `#2e2e2e`

### Gradients

```css
background-image: linear-gradient(rgba(26, 26, 26, 0) 0%, rgb(26, 26, 26) 100%);
```

```css
background-image: linear-gradient(rgb(0, 0, 0) 0%, rgba(0, 0, 0, 0) 100%);
```

```css
background-image: linear-gradient(-90deg, rgb(0, 0, 0) 0%, rgba(174, 174, 174, 0) 100%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 0%, rgb(0, 0, 0) 100%);
```

```css
background-image: linear-gradient(rgb(81, 81, 81) 0%, rgb(102, 102, 102) 100%);
```

```css
background-image: linear-gradient(90deg, rgb(81, 81, 81) 0%, rgb(102, 102, 102) 100%);
```

```css
background-image: linear-gradient(0deg, rgb(81, 81, 81) 0%, rgb(102, 102, 102) 100%);
```

```css
background-image: linear-gradient(270deg, rgb(81, 81, 81) 0%, rgb(102, 102, 102) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 3647 |
| `#ffffff` | background, text, border | 407 |
| `#0000ee` | text, border | 282 |
| `#1a1a1a` | background, text, border | 229 |
| `#5d5d5d` | text, border, background | 203 |
| `#464646` | text, border | 120 |
| `#737373` | text, border | 78 |
| `#e7543c` | background, text, border | 59 |
| `#242424` | background | 44 |
| `#2e2e2e` | text, border | 12 |
| `#ededed` | background | 6 |
| `#8c8c8c` | text, border | 6 |
| `#ff5f54` | background | 1 |
| `#ffbe32` | background | 1 |
| `#2fc941` | background | 1 |
| `#dae2d3` | background | 1 |
| `#0e0b0f` | background | 1 |
| `#0f0f2a` | background | 1 |
| `#393752` | background | 1 |

## Typography

### Font Families

- **Inter Display** — used for all (466 elements)
- **Times New Roman** — used for body (29 elements)
- **Inter** — used for all (20 elements)
- **Hooskai Chamfered Square** — used for body (7 elements)
- **Instrument Serif** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 120px | 7.5rem | 400 | 120px | -8.4px | p |
| 100px | 6.25rem | 400 | 100px | -7px | p |
| 90px | 5.625rem | 400 | 90px | -4.5px | h1, span |
| 48px | 3rem | 500 | 48px | -1.44px | span |
| 36px | 2.25rem | 500 | 39.6px | -0.72px | h2 |
| 28px | 1.75rem | 500 | 33.6px | -0.56px | p, h4 |
| 26px | 1.625rem | 500 | 31.2px | -0.52px | p, h5 |
| 22px | 1.375rem | 400 | 26.4px | -0.8px | p, h6 |
| 20px | 1.25rem | 400 | normal | normal | p, span |
| 18px | 1.125rem | 500 | 23.4px | -0.36px | p, span |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 14px | 0.875rem | 500 | 18.2px | -0.56px | p, span |
| 13px | 0.8125rem | 600 | 16.2918px | -0.59px | p |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |
| 10px | 0.625rem | 400 | 14px | -0.2px | p, span |

### Heading Scale

```css
h1 { font-size: 90px; font-weight: 400; line-height: 90px; }
h2 { font-size: 36px; font-weight: 500; line-height: 39.6px; }
h4 { font-size: 28px; font-weight: 500; line-height: 33.6px; }
h5 { font-size: 26px; font-weight: 500; line-height: 31.2px; }
h6 { font-size: 22px; font-weight: 400; line-height: 26.4px; }
```

### Body Text

```css
body { font-size: 18px; font-weight: 500; line-height: 23.4px; }
```

### Font Weights in Use

`400` (2080x), `500` (336x), `600` (20x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-24 | 24px | 1.5rem |
| spacing-28 | 28px | 1.75rem |
| spacing-32 | 32px | 2rem |
| spacing-40 | 40px | 2.5rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-120 | 120px | 7.5rem |
| spacing-300 | 300px | 18.75rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 1px | 30 |
| sm | 4px | 78 |
| md | 8px | 5 |
| lg | 11px | 2 |
| lg | 15px | 1 |
| xl | 20px | 9 |
| xl | 24px | 29 |
| full | 37px | 1 |
| full | 40px | 9 |
| full | 43px | 3 |
| full | 46px | 6 |
| full | 50px | 12 |
| full | 74px | 4 |
| full | 100px | 48 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgb(255, 255, 255) 0px 0px 0px 2px;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(0, 0, 0) 0px 0px 0px 1px inset;
```

**xs** — blur: 1.56569px
```css
box-shadow: rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px;
```

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
| 1200px | 1200px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.4s`

### Common Transitions

```css
transition: all;
transition: color 0.4s cubic-bezier(0.44, 0, 0.56, 1), text-decoration-color 0.4s cubic-bezier(0.44, 0, 0.56, 1), text-decoration-thickness 0.4s cubic-bezier(0.44, 0, 0.56, 1), text-underline-offset 0.4s cubic-bezier(0.44, 0, 0.56, 1);
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

### Buttons (2 instances)

```css
.button {
  background-color: rgba(0, 0, 0, 0.2);
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 40px;
}
```

### Cards (1 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (34 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 12px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(0, 0, 0);
  padding-top: 40px;
  padding-bottom: 20px;
  padding-left: 40px;
  padding-right: 40px;
  position: relative;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(248, 248, 248);
  color: rgb(0, 0, 0);
  padding-top: 120px;
  padding-bottom: 40px;
  font-size: 12px;
}
```

## Layout System

**2 grid containers** and **859 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 700px | 0px |
| 1520px | 0px |
| 100% | 0px |
| 520px | 12px |
| 310px | 24px |
| 1080px | 16px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 4-column | 1x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 288px 288px 288px 288px;
gap: 8px;
grid-template-columns: 174.656px 174.672px 174.672px;
gap: 24px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 557x |
| row/nowrap | 299x |
| row/wrap | 3x |

**Gap values:** `100px`, `10px`, `11px`, `12px`, `16px`, `18px`, `1px`, `20px`, `24px`, `28px`, `2px`, `300px`, `32px`, `3px`, `42px`, `4px`, `64px`, `6px`, `80px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 80/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 65/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance

**Issues:**
- 5 font families — consider limiting to 2 (heading + body)
- 17 !important rules — prefer specificity over overrides
- 56% of CSS is unused — consider purging
- 5178 duplicate CSS declarations

## Gradients

**8 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 3 | bold |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | 90deg | 2 | brand |
| linear | 0deg | 2 | brand |
| linear | 270deg | 2 | brand |

```css
background: linear-gradient(rgba(26, 26, 26, 0) 0%, rgb(26, 26, 26) 100%);
background: linear-gradient(rgb(0, 0, 0) 0%, rgba(0, 0, 0, 0) 100%);
background: linear-gradient(-90deg, rgb(0, 0, 0) 0%, rgba(174, 174, 174, 0) 100%);
background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgb(0, 0, 0) 100%);
background: linear-gradient(rgb(81, 81, 81) 0%, rgb(102, 102, 102) 100%);
```

## Z-Index Map

**5 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.c.9.l.n.p.z.-.c.o.n.t.a.i.n.e.r |
| base | 0,2 | div, div.f.r.a.m.e.r.-.1.n.9.9.0.k.l, div.f.r.a.m.e.r.-.w.f.8.z.7 |

**Issues:**
- [object Object]

## SVG Icons

**34 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 18 |
| sm | 9 |
| md | 5 |
| xl | 2 |

**Icon colors:** `rgb(0, 0, 0)`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Instrument Serif | cdn | 400 | italic |
| Fragment Mono | cdn | 400 | normal |
| Inter Display | self-hosted | 400, 500, 600, 700 | normal, italic |
| Inter | self-hosted | 400, 500, 700 | normal, italic |
| Hooskai Chamfered Square | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 26 | objectFit: contain, borderRadius: 0px, shape: square |
| avatar | 12 | objectFit: cover, borderRadius: 100%, shape: circular |
| hero | 7 | objectFit: cover, borderRadius: 20px, shape: pill |
| general | 3 | objectFit: cover, borderRadius: 24px, shape: pill |

**Aspect ratios:** 1:1 (32x), 21:9 (6x), 3:2 (5x), 4:3 (2x), 2.17:1 (1x), 5:1 (1x), 16:9 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `400ms` | 400 |

### Easing Families

- **custom** (2 uses) — `cubic-bezier(0.44, 0, 0.56, 1)`

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (balanced)

### Sample Headings

> Start your day with a better plan
> Built to organize tasks, priorities, and daily decisions
> Plan and communicate without language barriers
> Flexible plans for focused work
> Your days finally start working for you
> Start your day with a better plan
> Built to organize tasks, priorities, and daily decisions
> Plan and communicate without language barriers
> Flexible plans for focused work
> Your days finally start working for you

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Nura is a daily planning system that adapts to your real schedule. Capture tasks, set priorities, and stay focused as your day changes.

## Section Roles

Reading order (top→bottom): nav → testimonial → content → nav → testimonial → content → testimonials → content → testimonials → content → content → pricing → testimonials → content → content → faq → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.4 |
| 2 | testimonial | Start your day with a better plan | 0.8 |
| 3 | content | Start your day with a better plan | 0.3 |
| 4 | testimonial | — | 0.8 |
| 5 | content | — | 0.3 |
| 6 | testimonials | Built to organize tasks, priorities, and daily decisions | 0.4 |
| 7 | content | — | 0.3 |
| 8 | testimonials | — | 0.4 |
| 9 | content | Plan and communicate without language barriers | 0.3 |
| 10 | content | — | 0.3 |
| 11 | pricing | Flexible plans for focused work | 0.4 |
| 12 | testimonials | Your days finally start working for you | 0.4 |
| 13 | content | — | 0.3 |
| 14 | content | — | 0.3 |
| 15 | faq | Everything you might be wondering about | 0.85 |
| 16 | content | When everything feels unclear, make your day simple again | 0.3 |
| 17 | footer | ✦ | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.278 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 8 |

## Imagery Style

**Label:** `photography` (confidence 0.052)
**Counts:** total 48, svg 0, icon 16, screenshot-like 0, photo-like 5
**Dominant aspect:** square-ish
**Radius profile on images:** rounded

## Component Library

**Detected:** `vuetify` (confidence 0.5)

Evidence:
- 10 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter Display` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
