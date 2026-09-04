# Design Language: Home | Studio Agriculture

> Extracted from `https://studioagriculture.co` on September 4, 2026
> 171 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#e7371e` | rgb(231, 55, 30) | hsl(7, 81%, 51%) | 90 |
| Secondary | `#671235` | rgb(103, 18, 53) | hsl(335, 70%, 24%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 225 |
| `#ffffff` | hsl(0, 0%, 100%) | 31 |
| `#eeeeee` | hsl(0, 0%, 93%) | 8 |

### Background Colors

Used on large-area elements: `#ffffff`, `#671235`, `#eeeeee`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#e7371e`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border | 225 |
| `#e7371e` | text, border, background | 90 |
| `#ffffff` | background, text, border | 31 |
| `#eeeeee` | background | 8 |
| `#671235` | background | 1 |

## Typography

### Font Families

- **PP Neue Montreal** — used for body (131 elements)
- **Times New Roman** — used for body (35 elements)
- **PP Neue Montreal Book** — used for body (4 elements)
- **Macan** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 100px | 6.25rem | 400 | 100px | -2px | div |
| 38px | 2.375rem | 400 | 41.8px | normal | div, a, span |
| 18px | 1.125rem | 400 | normal | normal | div, a, p |
| 16px | 1rem | 400 | normal | normal | html, head, meta, style |
| 14px | 0.875rem | 400 | normal | normal | body, div, header, main |

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (171x)

## Spacing

**Base unit:** 5px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-5 | 5px | 0.3125rem |
| spacing-100 | 100px | 6.25rem |
| spacing-165 | 165px | 10.3125rem |
| spacing-300 | 300px | 18.75rem |

## CSS Custom Properties

### Colors

```css
--swiper-theme-color: #007aff;
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
| md | 768px | max-width |
| lg | 968px | max-width |
| lg | 991px | max-width |
| 1200px | 1200px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.5s`, `0.65s`, `0.2s`, `0.4s`, `1.25s`, `1s`, `0.25s`, `0.35s`, `0.75s`, `0.7s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: transform 0.5s;
transition: opacity 0.65s 0.2s;
transition: background 0.4s;
transition: transform 1.25s 1s;
transition: opacity 0.5s linear;
transition: opacity 0.25s linear;
transition: 0.2s;
transition: transform 0.35s;
transition: width 0.75s 0.2s;
```

### Keyframe Animations

**fadeIn**
```css
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**fadeOut**
```css
@keyframes fadeOut {
  0% { opacity: 1; }
  100% { opacity: 0; }
}
```

**scroll-left**
```css
@keyframes scroll-left {
  0% { transform: translateX(0px); }
  100% { transform: translateX(-100%); }
}
```

**swiper-preloader-spin**
```css
@keyframes swiper-preloader-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (1 instances)

```css
.button {
  color: rgb(231, 55, 30);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Inputs (4 instances)

```css
.input {
  color: rgb(231, 55, 30);
  border-color: rgb(231, 55, 30);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (20 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: rgb(255, 255, 255);
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
  padding-right: 20px;
  position: static;
}
```

### Footer (2 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding-top: 20px;
  padding-bottom: 20px;
  font-size: 14px;
}
```

### Switches (1 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(255, 255, 255);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Input — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(231, 55, 30);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px 0px 1px none none solid rgb(231, 55, 30);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(231, 55, 30);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(231, 55, 30);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **16 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1920px | 0px |
| 100% | 0px |
| 950px | 20px |
| 1400px | 0px |
| 1200px | 0px |
| 2880px | 0px |
| 2189px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 506.406px 187.188px 506.406px;
gap: 20px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 11x |
| column/nowrap | 5x |

**Gap values:** `100px`, `10px`, `20px`, `5px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 84/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 60% of CSS is unused — consider purging
- 232 duplicate CSS declarations

## Z-Index Map

**3 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9999,9999 | div.p.a.g.e.-.-.t.r.a.n.s.i.t.i.o.n. .f.a.d.e.-.-.i.n |
| sticky | 12,12 | header.m.a.s.t.h.e.a.d |
| base | 2,2 | div.m.t.a. .w.-.1.0.0. .p.2.0. .p.o.s.-.r.e.l. .z.-.2, div.p.r.o.j.e.c.t.-.-.f.e.e.d. .m.a.x.-.1.2.0.0. .m.a. .p.o.s.-.r.e.l. .z.-.2. .f.l.e.x. .f.l.e.x.-.c.o.l. .g.a.p.-.1.0.0 |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| PP Neue Montreal Book | self-hosted | 400 | normal |
| PP Neue Montreal | self-hosted | 500, 700 | normal |
| Macan | self-hosted | 700 | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 9 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 16:9 (7x), 3:2 (2x)

## Motion Language

**Feel:** mechanical · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `750ms` | 750 |
| `xxl` | `1.25s` | 1250 |

### Easing Families

- **linear** (6 uses) — `linear`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `fadeIn` | fade | opacity | 1 |
| `scroll-left` | slide-x | transform | 1 |

## Component Anatomy

### input — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** unknown (tight)

### Top CTA Verbs

- **submit** (1)

### Button Copy Patterns

- "submit" (1×)

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** We are Studio Agriculture. We work with brands connected to the earth and underpinned by an integrated bigger purpose. 

## Section Roles

Reading order (top→bottom): nav → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | content | — | 0.3 |
| 2 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.339 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0.167)
**Counts:** total 9, svg 3, icon 0, screenshot-like 0, photo-like 2
**Dominant aspect:** landscape
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.312)

Evidence:
- tailwind-like class density 36%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `PP Neue Montreal` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
