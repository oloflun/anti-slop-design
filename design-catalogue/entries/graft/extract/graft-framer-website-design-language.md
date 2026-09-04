# Design Language: Graft is Furniture & Interior Design Studio Template

> Extracted from `https://graft.framer.website/` on September 4, 2026
> 1468 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#392615` | rgb(57, 38, 21) | hsl(28, 46%, 15%) | 148 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 454 |
| Accent | `#736557` | rgb(115, 101, 87) | hsl(30, 14%, 40%) | 64 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1930 |
| `#ffffff` | hsl(0, 0%, 100%) | 111 |
| `#585048` | hsl(30, 10%, 31%) | 108 |
| `#c2bbb5` | hsl(28, 10%, 74%) | 57 |
| `#767676` | hsl(0, 0%, 46%) | 22 |
| `#f6f6f6` | hsl(0, 0%, 96%) | 17 |
| `#d9d9d9` | hsl(0, 0%, 85%) | 16 |

### Background Colors

Used on large-area elements: `#ffffff`, `#000000`, `#f6f6f6`, `#392615`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#ffffff`, `#392615`, `#dbc0a9`, `#585048`, `#736557`, `#956e4b`, `#d9d9d9`, `#c2bbb5`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 1930 |
| `#0000ee` | text, border | 454 |
| `#392615` | background, text, border | 148 |
| `#ffffff` | background, text, border | 111 |
| `#585048` | text, border | 108 |
| `#956e4b` | text, border | 88 |
| `#736557` | text, border, background | 64 |
| `#c2bbb5` | text, border, background | 57 |
| `#767676` | border | 22 |
| `#f6f6f6` | background, text, border | 17 |
| `#d9d9d9` | text, border | 16 |
| `#fcead9` | text, border | 8 |
| `#dbc0a9` | text, border, background | 3 |

## Typography

### Font Families

- **Inter** — used for all (196 elements)
- **Times New Roman** — used for body (30 elements)
- **Inter Tight** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 585.57px | 36.5981rem | 400 | 468.456px | -29.2785px | p |
| 180px | 11.25rem | 400 | 144px | -12.6px | h1 |
| 100px | 6.25rem | 400 | 100px | -8px | h2 |
| 40px | 2.5rem | 400 | 44px | -2.8px | h3, span |
| 26px | 1.625rem | 400 | 28.6px | -1.82px | h4, a |
| 18px | 1.125rem | 500 | 23.4px | -1.26px | p |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 14px | 0.875rem | 500 | 22.4px | -0.84px | p |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |

### Heading Scale

```css
h1 { font-size: 180px; font-weight: 400; line-height: 144px; }
h2 { font-size: 100px; font-weight: 400; line-height: 100px; }
h3 { font-size: 40px; font-weight: 400; line-height: 44px; }
h4 { font-size: 26px; font-weight: 400; line-height: 28.6px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (1431x), `600` (28x), `500` (9x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-5 | 5px | 0.3125rem |
| spacing-25 | 25px | 1.5625rem |
| spacing-30 | 30px | 1.875rem |
| spacing-35 | 35px | 2.1875rem |
| spacing-50 | 50px | 3.125rem |
| spacing-60 | 60px | 3.75rem |
| spacing-70 | 70px | 4.375rem |
| spacing-100 | 100px | 6.25rem |
| spacing-124 | 124px | 7.75rem |
| spacing-131 | 131px | 8.1875rem |
| spacing-142 | 142px | 8.875rem |
| spacing-200 | 200px | 12.5rem |
| spacing-218 | 218px | 13.625rem |
| spacing-360 | 360px | 22.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 3 |
| md | 7px | 9 |
| md | 10px | 74 |
| lg | 15px | 46 |
| xl | 22px | 1 |
| full | 25px | 15 |
| full | 29px | 4 |
| full | 38px | 3 |
| full | 50px | 1 |
| full | 59px | 3 |
| full | 100px | 13 |
| full | 200px | 3 |

## Box Shadows

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(0, 0, 0) 0px 0px 0px 1px inset;
```

**xs** — blur: 1.56569px
```css
box-shadow: rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px;
```

**lg** — blur: 20px
```css
box-shadow: rgba(0, 0, 0, 0.25) 0px 10px 20px 0px;
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

### Common Transitions

```css
transition: all;
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
  background-color: rgb(115, 101, 87);
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 50px;
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

### Inputs (26 instances)

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

### Links (33 instances)

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
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Input — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(88, 80, 72);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(88, 80, 72);
  font-size: 16px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(88, 80, 72);
  padding: 12px 12px 12px 12px;
  border-radius: 0px;
  border: 0px none rgb(88, 80, 72);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(115, 101, 87);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 50px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 10px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**2 grid containers** and **542 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1620px | 50px |
| 1520px | 0px |
| 50% | 0px |
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 4-column | 2x |

### Grid Templates

```css
grid-template-columns: 276.25px 276.25px 276.25px 276.25px;
gap: 25px;
grid-template-columns: 277.75px 277.75px 277.75px 277.75px;
gap: 25px 23px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 340x |
| row/nowrap | 198x |
| row/wrap | 4x |

**Gap values:** `100px`, `10px`, `11px`, `124px`, `131px`, `13px`, `142px`, `14px`, `15px`, `16px`, `1px`, `20px`, `218px`, `25px`, `25px 23px`, `26px`, `30px`, `35px`, `360px`, `36px`, `50px`, `5px`, `70px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 83/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 80/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 65/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance

**Issues:**
- 18 !important rules — prefer specificity over overrides
- 69% of CSS is unused — consider purging
- 5250 duplicate CSS declarations

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.1.s.t.n.a.g.m, div.f.r.a.m.e.r.-.1.m.3.8.1.i.r.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.1.i.g.q.2.l.v.-.c.o.n.t.a.i.n.e.r |
| base | 0,6 | div.f.r.a.m.e.r.-.1.3.k.7.w.w.8, div.f.r.a.m.e.r.-.1.3.k.7.w.w.8, div.f.r.a.m.e.r.-.1.3.k.7.w.w.8 |

**Issues:**
- [object Object]

## SVG Icons

**18 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 2 |
| sm | 3 |
| md | 1 |
| lg | 6 |
| xl | 6 |

**Icon colors:** `rgb(57, 38, 21)`, `rgb(0, 0, 0)`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Inter Tight | cdn | 400 | normal |
| Inter | self-hosted | 400, 500, 600, 700 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 33 | objectFit: cover, borderRadius: 38px, shape: pill |
| thumbnail | 19 | objectFit: cover, borderRadius: 10px, shape: rounded |
| hero | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| avatar | 4 | objectFit: cover, borderRadius: 59px, shape: circular |

**Aspect ratios:** 1:1 (36x), 3:4 (12x), 9:16 (4x), 4:3 (2x), 1.99:1 (1x), 21:9 (1x), 3.56:1 (1x), 16:9 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

## Component Anatomy

### input — 4 instances


### button — 2 instances

**Slots:** label

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **submit** (1)

### Button Copy Patterns

- "submit" (1×)

### Sample Headings

> Graft 
> Sofas
> Sidetables
> Chairs
> Tables
> Dressing Room
> Not just furniture. It's tactile architecture for your home.
> New item
> Meet Onda chair
> Be inspired

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** Furniture Design Studio Landing page

Alternates: blog-post (0.35), docs (0.3)

## Section Roles

Reading order (top→bottom): nav → hero → content → content → content → content → pricing → content → content → testimonial → testimonial → testimonial → hero → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | hero | Graft  | 0.85 |
| 2 | content | Sofas | 0.3 |
| 3 | content | Not just furniture. It's tactile architecture for your home. | 0.3 |
| 4 | content | New item | 0.3 |
| 5 | content | Be inspired | 0.3 |
| 6 | pricing | Furnishing a 30 sqm loft  | 0.4 |
| 7 | content | Сreating your | 0.3 |
| 8 | content | How we work | 0.3 |
| 9 | testimonial | People say… | 0.8 |
| 10 | testimonial | — | 0.8 |
| 11 | testimonial | Meet our creators | 0.8 |
| 12 | hero | Get in Touch | 0.4 |
| 13 | content | Our social hub | 0.3 |
| 14 | footer | Subscribe to Newsletter | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.23 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 200px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.025)
**Counts:** total 61, svg 0, icon 15, screenshot-like 0, photo-like 3
**Dominant aspect:** square-ish
**Radius profile on images:** soft

## Component Library

**Detected:** `vuetify` (confidence 0.48)

Evidence:
- 9 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
