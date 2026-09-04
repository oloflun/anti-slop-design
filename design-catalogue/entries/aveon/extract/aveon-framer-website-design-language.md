# Design Language: Avéon — Interior Design Studio | Residential & Commercial Interiors

> Extracted from `https://aveon.framer.website/` on September 4, 2026
> 4092 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 974 |
| Secondary | `#b8845c` | rgb(184, 132, 92) | hsl(26, 39%, 54%) | 124 |
| Accent | `#2c2218` | rgb(44, 34, 24) | hsl(30, 29%, 13%) | 331 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 5692 |
| `#1a1a1a` | hsl(0, 0%, 10%) | 914 |
| `#e5ddd4` | hsl(32, 25%, 86%) | 105 |
| `#ffffff` | hsl(0, 0%, 100%) | 52 |
| `#767676` | hsl(0, 0%, 46%) | 22 |
| `#3e3228` | hsl(27, 22%, 20%) | 5 |

### Background Colors

Used on large-area elements: `#e8e0d6`, `#1a1512`, `#000000`, `#1a1a1a`, `#b8845c`, `#f5f0eb`

### Text Colors

Text color palette: `#000000`, `#f2ede7`, `#2c2218`, `#0000ee`, `#b8845c`, `#e5ddd4`, `#3e3228`, `#241d17`, `#ffffff`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 5692 |
| `#f2ede7` | background, text, border | 980 |
| `#0000ee` | text, border | 974 |
| `#1a1a1a` | background | 914 |
| `#2c2218` | text, border, background | 331 |
| `#b8845c` | background, text, border | 124 |
| `#e5ddd4` | background, text, border | 105 |
| `#ffffff` | background, text, border | 52 |
| `#767676` | border | 22 |
| `#3e3228` | text, border, background | 5 |

## Typography

### Font Families

- **Geist** — used for all (417 elements)
- **Inter Display** — used for body (191 elements)
- **Times New Roman** — used for body (30 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 144px | 9rem | 500 | 129.6px | -10.08px | h1 |
| 80px | 5rem | 600 | 80px | -4.8px | h1, span |
| 60px | 3.75rem | 500 | 60px | -1.8px | span |
| 44px | 2.75rem | 600 | 44px | -2.64px | h2 |
| 36px | 2.25rem | 600 | 36px | -1.8px | h3 |
| 22px | 1.375rem | 600 | 24.2px | -1.32px | h4 |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 14px | 0.875rem | 600 | 16.8px | -0.28px | p, input |
| 13px | 0.8125rem | 600 | 15.6px | -0.26px | p |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |
| 11px | 0.6875rem | 600 | 16.5px | normal | p |

### Heading Scale

```css
h1 { font-size: 144px; font-weight: 500; line-height: 129.6px; }
h1 { font-size: 80px; font-weight: 600; line-height: 80px; }
h2 { font-size: 44px; font-weight: 600; line-height: 44px; }
h3 { font-size: 36px; font-weight: 600; line-height: 36px; }
h4 { font-size: 22px; font-weight: 600; line-height: 24.2px; }
h5 { font-size: 12px; font-weight: 400; line-height: normal; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (3507x), `500` (371x), `600` (211x), `700` (3x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-40 | 40px | 2.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-66 | 66px | 4.125rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-120 | 120px | 7.5rem |
| spacing-240 | 240px | 15rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 5px | 1 |
| md | 10px | 1 |
| lg | 16px | 2 |
| xl | 20px | 3 |
| full | 999px | 1 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgb(242, 237, 231) 0px 0px 0px 2px;
```

**sm** — blur: 0px
```css
box-shadow: rgb(184, 132, 92) 0px 0px 0px 2px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(184, 132, 92, 0.8) 0px 0px 0px 3px;
```

**sm** — blur: 0px
```css
box-shadow: rgb(255, 255, 255) 0px 0px 0px 2px;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(0, 0, 0) 0px 0px 0px 1px inset;
```

**xs** — blur: 0.711334px
```css
box-shadow: rgba(0, 0, 0, 0.14) 0px 0.711334px 0.711334px -0.55px, rgba(0, 0, 0, 0.14) 0px 1.93715px 1.93715px -1.1px, rgba(0, 0, 0, 0.13) 0px 4.25328px 4.25328px -1.65px, rgba(0, 0, 0, 0.13) 0px 9.44132px 9.44132px -2.2px, rgba(0, 0, 0, 0.11) 0px 24px 24px -2.75px;
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
| md | 767px | max-width |
| md | 768px | min-width |
| 1349px | 1349px | max-width |
| 1350px | 1350px | max-width |

## Transitions & Animations

**Durations:** `0.25s`

### Common Transitions

```css
transition: all;
transition: opacity 0.25s;
transition: background, box-shadow;
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
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 16px;
  padding-right: 16px;
  border-radius: 0px;
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

### Inputs (24 instances)

```css
.input {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  border-color: rgb(118, 118, 118);
  border-radius: 0px;
  font-size: 12px;
  padding-top: 1px;
  padding-right: 2px;
}
```

### Links (51 instances)

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
  background-color: rgb(232, 224, 214);
  color: rgb(0, 0, 0);
  padding-top: 16px;
  padding-bottom: 16px;
  padding-left: 16px;
  padding-right: 16px;
  position: relative;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Input — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(242, 237, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(242, 237, 231);
  font-size: 14px;
  font-weight: 500;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 16px 16px 16px 16px;
  border-radius: 0px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**29 grid containers** and **696 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1520px | 0px |
| 1000px | 0px |
| 100% | 0px |
| 880px | 0px |
| 49% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 4-column | 15x |
| 1-column | 10x |
| 2-column | 3x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 614px 614px;
gap: 20px;
grid-template-columns: 312px 312px 312px 312px;
grid-template-columns: 1248px;
gap: 40px 0px;
grid-template-columns: 416px 416px 416px;
gap: 60px 0px;
grid-template-columns: 1248px;
gap: 24px 0px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 425x |
| row/nowrap | 267x |
| row/wrap | 4x |

**Gap values:** `100px`, `10px`, `12px`, `16px`, `20px`, `20px 0px`, `20px 28px`, `24px`, `24px 0px`, `24px 20px`, `28px`, `32px`, `40px`, `40px 0px`, `4px`, `4px 20px`, `5px`, `60px`, `60px 0px`, `66px`, `80px`, `80px 0px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 90/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 17 !important rules — prefer specificity over overrides
- 60% of CSS is unused — consider purging
- 6614 duplicate CSS declarations

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,2147483647 | div, div, div |
| sticky | 10,10 | div.f.r.a.m.e.r.-.1.p.0.4.h.5.a, div.f.r.a.m.e.r.-.1.7.7.n.q.a.f.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.1.6.c.m.5.v.u.-.c.o.n.t.a.i.n.e.r |
| base | 0,8 | div.f.r.a.m.e.r.-.1.f.k.i.t.v.q, div.f.r.a.m.e.r.-.a.3.t.e.p.1, div.f.r.a.m.e.r.-.1.i.h.u.4.a.n |

**Issues:**
- [object Object]

## SVG Icons

**12 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 2 |
| md | 5 |
| lg | 3 |
| xl | 2 |

**Icon colors:** `rgb(242, 237, 231)`, `rgb(0, 0, 0)`, `rgb(44, 34, 24)`, `rgb(255, 255, 255)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Geist | cdn | 400, 500, 600, 700, 900 | normal |
| Inter | self-hosted | 400, 700, 900 | normal, italic |
| Inter Display | self-hosted | 500, 600, 700 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 905 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 29 | objectFit: cover, borderRadius: 6px, shape: rounded |
| hero | 16 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 4:3 (536x), 1:1 (277x), 3:4 (125x), 4.03:1 (5x), 21:9 (3x), 3.47:1 (2x), 16:9 (2x), 3.35:1 (2x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `250ms` | 250 |

## Component Anatomy

### input — 2 instances


### button — 2 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **subscribe** (2)

### Button Copy Patterns

- "subscribe now

subscribe now" (2×)

### Sample Headings

> SPACES THAT TELL A STORY
> Full-Spectrum Interior Design Excellence
> Residential Interiors
> Commercial Spaces
> Furniture Curation
> Spatial Planning
> Where Every Details Matters & Every Space Has A Soul!
> "Our mission is to craft 
> interiors that  don't just look beautiful, but feel like home, where design elevates like a pro vanture."
> Our Story

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** Award-winning interior design studio specializing in residential, commercial, and hospitality spaces. Warm minimalism, honest materials, and design that starts with how you live.

Alternates: blog-post (0.35), docs (0.3)

## Section Roles

Reading order (top→bottom): nav → content → testimonial → content → testimonial → testimonial → content → testimonial → testimonial → faq → testimonial → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | content | SPACES THAT TELL A STORY | 0.3 |
| 1 | testimonial | Full-Spectrum Interior Design Excellence | 0.8 |
| 2 | content | Where Every Details Matters & Every Space Has A Soul! | 0.3 |
| 3 | testimonial | "Our mission is to craft  | 0.8 |
| 4 | testimonial | Projects That Speak for Themselves | 0.8 |
| 5 | content | Five years of transforming spaces into stories worth living in. | 0.3 |
| 6 | testimonial | Spaces That Inspire Lasting Loyalty | 0.8 |
| 7 | testimonial | A Clear Path From Vision to Reality | 0.8 |
| 8 | faq | Everything You Need to Know Before We Start | 0.85 |
| 9 | testimonial | Design Inspiration & Expert Insights | 0.8 |
| 10 | footer | Avéon Studio | 0.95 |
| 11 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.243 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.481)
**Counts:** total 952, svg 0, icon 13, screenshot-like 0, photo-like 913
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `vuetify` (confidence 0.56)

Evidence:
- 13 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Geist` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
