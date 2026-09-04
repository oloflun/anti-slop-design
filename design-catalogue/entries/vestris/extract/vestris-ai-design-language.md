# Design Language: Vestris — Agents that automate real estate pre-closing

> Extracted from `https://vestris.ai/` on September 4, 2026
> 713 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#62644e` | rgb(98, 100, 78) | hsl(65, 12%, 35%) | 16 |
| Secondary | `#f2efe5` | rgb(242, 239, 229) | hsl(46, 33%, 92%) | 38 |
| Accent | `#e6e0ce` | rgb(230, 224, 206) | hsl(45, 32%, 85%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1010 |
| `#2b2927` | hsl(30, 5%, 16%) | 298 |
| `#736e6a` | hsl(27, 4%, 43%) | 30 |
| `#ffffff` | hsl(0, 0%, 100%) | 26 |
| `#5c7c68` | hsl(143, 15%, 42%) | 8 |
| `#a89e95` | hsl(28, 10%, 62%) | 4 |

### Background Colors

Used on large-area elements: `#f2efe5`, `#ffffff`, `#fdfbf5`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#2b2927`, `#62644e`, `#ffffff`, `#111b27`, `#736e6a`, `#5c7c68`, `#f2efe5`

### Gradients

```css
background-image: linear-gradient(rgb(92, 124, 104) 0%, rgb(92, 124, 104) 100%, rgba(92, 124, 104, 0) 100%);
```

```css
background-image: linear-gradient(rgba(34, 51, 37, 0) 0%, rgb(35, 52, 38) 77.9566%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border | 1010 |
| `#2b2927` | text, border | 298 |
| `#f2efe5` | background, text, border | 38 |
| `#736e6a` | text, border | 30 |
| `#ffffff` | text, border, background | 26 |
| `#0000ee` | text, border | 18 |
| `#62644e` | text, border, background | 16 |
| `#5c7c68` | text, border | 8 |
| `#a89e95` | background | 4 |
| `#111b27` | text, border | 2 |
| `#e6e0ce` | background | 1 |

## Typography

### Font Families

- **Instrument Serif** — used for body (125 elements)
- **Geist** — used for body (71 elements)
- **Inter** — used for body (40 elements)
- **Times New Roman** — used for body (29 elements)
- **Manrope** — used for body (3 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 96px | 6rem | 400 | 105.6px | normal | p, span |
| 75px | 4.6875rem | 400 | 75px | -2.25px | p, span |
| 73px | 4.5625rem | 400 | 73px | -2.19px | p, span, br |
| 69px | 4.3125rem | 400 | 69px | -2.07px | p, span |
| 64px | 4rem | 400 | 64px | normal | p, span, br |
| 36px | 2.25rem | 400 | 39.6px | normal | p, span |
| 20px | 1.25rem | 400 | 24px | normal | p, span |
| 18px | 1.125rem | 400 | 23.4px | -0.18px | p, span, br |
| 17px | 1.0625rem | 500 | 20.4px | normal | p |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 15px | 0.9375rem | 400 | 18px | normal | p, a, span |
| 14px | 0.875rem | 400 | 18.2px | normal | p, span, a |
| 13px | 0.8125rem | 400 | 15.6px | normal | p, span |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |
| 10px | 0.625rem | 400 | 11px | normal | p, span |

### Body Text

```css
body { font-size: 75px; font-weight: 400; line-height: 75px; }
```

### Font Weights in Use

`400` (683x), `500` (17x), `600` (13x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-19 | 19px | 1.1875rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-50 | 50px | 3.125rem |
| spacing-56 | 56px | 3.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-72 | 72px | 4.5rem |
| spacing-80 | 80px | 5rem |
| spacing-90 | 90px | 5.625rem |
| spacing-103 | 103px | 6.4375rem |
| spacing-120 | 120px | 7.5rem |
| spacing-160 | 160px | 10rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 2 |
| md | 8px | 10 |
| lg | 16px | 3 |
| xl | 20px | 14 |
| full | 64px | 1 |
| full | 100px | 3 |

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
| md | 810px | max-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | max-width |

## Transitions & Animations

**Durations:** `0.001s`

### Common Transitions

```css
transition: overflow 0.001s allow-discrete;
transition: all;
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

### Links (13 instances)

```css
.link {
  color: rgb(0, 0, 0);
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

### Switches (1 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
}
```

## Layout System

**0 grid containers** and **203 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1600px | 20px |
| 1400px | 0px |
| 1200px | 40px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 148x |
| row/nowrap | 55x |

**Gap values:** `103px`, `10px`, `11px`, `12px`, `16px`, `19px`, `20px`, `21px`, `22px`, `23px`, `24px`, `30px`, `32px`, `4px`, `50px`, `56px`, `5px`, `60px`, `6px`, `72px`, `7px`, `8px`, `90px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 82/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 5 font families — consider limiting to 2 (heading + body)
- 16 !important rules — prefer specificity over overrides
- 70% of CSS is unused — consider purging
- 2008 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 3 | bold |
| linear | — | 2 | brand |

```css
background: linear-gradient(rgb(92, 124, 104) 0%, rgb(92, 124, 104) 100%, rgba(92, 124, 104, 0) 100%);
background: linear-gradient(rgba(34, 51, 37, 0) 0%, rgb(35, 52, 38) 77.9566%);
```

## Z-Index Map

**6 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.o.z.8.y.b.u.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.t.c.1.1.c.n.-.c.o.n.t.a.i.n.e.r |
| base | 0,7 | div, div.f.r.a.m.e.r.-.1.0.k.e.j.3.4. .h.i.d.d.e.n.-.a.b.7.9.j.6, div.f.r.a.m.e.r.-.o.x.7.w.w.c. .h.i.d.d.e.n.-.a.b.7.9.j.6 |

**Issues:**
- [object Object]

## SVG Icons

**13 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 2 |
| md | 2 |
| lg | 2 |
| xl | 7 |

**Icon colors:** `rgb(0, 0, 0)`, `#1A1A1A`, `#111B27`, `#FC6723`, `white`, `#5C7C68`, `#F2EFE5`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Geist | cdn | 400, 500, 600, 700 | italic, normal |
| Instrument Serif | cdn | 400 | italic, normal |
| Manrope | cdn | 400 | normal |
| Inter | self-hosted | 400, 500, 600 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 6 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 3 | objectFit: cover, borderRadius: 20px, shape: pill |
| thumbnail | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:2 (3x), 9:16 (2x), 4:3 (2x), 1:1 (2x), 0.28:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** AI-powered real estate settlement software that automates document processing, title workflows, communication, and closing coordination—helping title teams handle more files with less manual work.

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.226 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 10, svg 0, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** landscape
**Radius profile on images:** soft

## Component Library

**Detected:** `vuetify` (confidence 0.48)

Evidence:
- 9 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Instrument Serif` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
