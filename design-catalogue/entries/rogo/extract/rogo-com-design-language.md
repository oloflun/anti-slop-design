# Design Language: Rogo | AI for the most ambitious firms in finance

> Extracted from `https://rogo.com` on September 4, 2026
> 1109 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 58 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1980 |
| `#ffffff` | hsl(0, 0%, 100%) | 88 |
| `#151515` | hsl(0, 0%, 8%) | 81 |
| `#737373` | hsl(0, 0%, 45%) | 29 |
| `#eeedec` | hsl(30, 6%, 93%) | 5 |
| `#383838` | hsl(0, 0%, 22%) | 3 |
| `#444444` | hsl(0, 0%, 27%) | 2 |

### Background Colors

Used on large-area elements: `#ffffff`, `#737373`, `#f7f7f7`, `#eeedec`, `#151515`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#ffffff`, `#151515`, `#171717`, `#737373`, `#444444`

### Gradients

```css
background-image: linear-gradient(rgba(21, 21, 21, 0) 85%, rgb(21, 21, 21) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 1980 |
| `#ffffff` | background, text, border | 88 |
| `#151515` | text, border, background | 81 |
| `#0000ee` | text, border | 58 |
| `#737373` | background, text, border | 29 |
| `#eeedec` | background | 5 |
| `#383838` | background | 3 |
| `#444444` | text, border | 2 |

## Typography

### Font Families

- **Inter** — used for all (83 elements)
- **Times New Roman** — used for body (43 elements)
- **ABC Arizona Mix Regular** — used for all (14 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 96px | 6rem | 400 | 128px | -3.84px | h4 |
| 64px | 4rem | 400 | 60.8px | -3.2px | h1 |
| 48px | 3rem | 400 | 50.4px | -2.4px | h1, h3, h2, span |
| 44px | 2.75rem | 400 | 46.2px | -2.2px | h3, br |
| 28px | 1.75rem | 400 | 35px | -0.84px | h5, h3 |
| 24px | 1.5rem | 500 | 26.4px | -0.48px | h4 |
| 20px | 1.25rem | 400 | 25px | -0.4px | p, br, span |
| 18px | 1.125rem | 400 | 27px | -0.1px | p |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 14px | 0.875rem | 500 | 21px | -0.14px | p, a, span |
| 12px | 0.75rem | 400 | normal | normal | body, script, img, div |

### Heading Scale

```css
h4 { font-size: 96px; font-weight: 400; line-height: 128px; }
h1 { font-size: 64px; font-weight: 400; line-height: 60.8px; }
h1 { font-size: 48px; font-weight: 400; line-height: 50.4px; }
h3 { font-size: 44px; font-weight: 400; line-height: 46.2px; }
h5 { font-size: 28px; font-weight: 400; line-height: 35px; }
h4 { font-size: 24px; font-weight: 500; line-height: 26.4px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (1076x), `500` (32x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-108 | 108px | 6.75rem |
| spacing-120 | 120px | 7.5rem |
| spacing-164 | 164px | 10.25rem |
| spacing-196 | 196px | 12.25rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 6px | 19 |

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
| 2xl | 1600px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.3s`

### Common Transitions

```css
transition: all;
transition: color 0.3s cubic-bezier(0.44, 0, 0.56, 1);
```

### Keyframe Animations

**react-loading-skeleton**
```css
@keyframes react-loading-skeleton {
  100% { transform: translate(100%); }
}
```

**__framer-loading-spin**
```css
@keyframes __framer-loading-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Cards (1 instances)

```css
.card {
}
```

### Inputs (2 instances)

```css
.input {
  background-color: rgb(238, 238, 238);
  color: rgb(68, 68, 68);
  border-color: rgb(68, 68, 68);
  border-radius: 8px;
  font-size: 16px;
  padding-top: 12px;
  padding-right: 12px;
}
```

### Links (26 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 400;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(21, 21, 21);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(238, 238, 238);
  color: rgb(68, 68, 68);
  padding: 12px 12px 12px 12px;
  border-radius: 8px;
  border: 0px none rgb(68, 68, 68);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 12px 12px 12px 12px;
  border-radius: 8px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **218 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1280px | 0px |
| 840px | 0px |
| 844px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 240px 240px 240px 240px 240px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 138x |
| row/nowrap | 80x |

**Gap values:** `108px`, `10px`, `12px`, `164px`, `16px`, `20px`, `24px`, `28px`, `32px`, `40px`, `48px`, `4px`, `56px`, `64px`, `72px`, `80px`, `88px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 88/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 18 !important rules — prefer specificity over overrides
- 73% of CSS is unused — consider purging
- 2689 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |

```css
background: linear-gradient(rgba(21, 21, 21, 0) 85%, rgb(21, 21, 21) 100%);
```

## Z-Index Map

**13 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| dropdown | 100,100 | div |
| sticky | 10,10 | div |
| base | 0,9 | div.f.r.a.m.e.r.-.z.y.j.r.j.u.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.y.h.q.t.v.r.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.e.3.9.y.g.h |

**Issues:**
- [object Object]

## SVG Icons

**42 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| md | 1 |
| lg | 4 |
| xl | 37 |

**Icon colors:** `rgb(0, 0, 0)`, `rgb(255, 255, 255)`, `white`, `var(--token-0bc1d917-0b22-49ae-8ecb-1066429bce0e, rgb(255, 255, 255))`, `var(--token-0d31da53-baed-4296-8f09-eb72c6059553, rgb(21, 21, 21))`, `#fff`, `#6D6D6D`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Fragment Mono | cdn | 400 | normal |
| ABC Arizona Mix Regular | self-hosted | 400 | normal |
| Inter Regular | self-hosted | 400 | normal |
| BR Sonoma Regular | self-hosted | 400 | normal |
| Rooftop Mono Regular | self-hosted | 400 | normal |
| Rooftop Regular | self-hosted | 400 | normal |
| Test Martina Plantijn Regular | self-hosted | 400 | normal |
| Inter Display Medium | self-hosted | 500 | normal |
| Inter Display Bold | self-hosted | 700 | normal |
| Inter Display Bold Italic | self-hosted | 700 | italic |
| Inter Display Medium Italic | self-hosted | 500 | italic |
| BR Sonoma Medium | self-hosted | 500 | normal |
| Martina Plantijn Light | self-hosted | 300 | normal |
| Inter Display SemiBold | self-hosted | 600 | normal |
| Martina Plantijn Regular | self-hosted | 400 | normal |
| ABC Arizona Flare Regular | self-hosted | 400 | normal |
| ABC Arizona Flare Light | self-hosted | 300 | normal |
| Inter | self-hosted | 400, 500, 600, 700 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 30 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 4.35:1 (3x), 6.09:1 (3x), 4.8:1 (3x), 4.29:1 (3x), 3.64:1 (3x), 4:3 (3x), 3.5:1 (3x), 2:1 (3x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `300ms` | 300 |

### Easing Families

- **custom** (13 uses) — `cubic-bezier(0.44, 0, 0.56, 1)`

## Component Anatomy

### button — 2 instances

**Slots:** label

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (balanced)

### Sample Headings

> Helping finance teams build smarter organizations
> Why financial institutions 
choose Rogo
> By the numbers
> Built for enterprise, secure by design
> Unlock financial AI
for your firm

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Rogo is the trusted AI partner to the world’s leading financial institutions. Rogo helps finance teams make better decisions and build smarter teams.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → content → testimonial → testimonial → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | content | — | 0.3 |
| 2 | testimonial | Helping finance teams build smarter organizations | 0.8 |
| 3 | testimonial | Why financial institutions 
choose Rogo | 0.8 |
| 4 | content | By the numbers | 0.3 |
| 5 | content | Built for enterprise, secure by design | 0.3 |
| 6 | footer | Unlock financial AI
for your firm | 0.95 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.126 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 6px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.411)
**Counts:** total 30, svg 30, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
