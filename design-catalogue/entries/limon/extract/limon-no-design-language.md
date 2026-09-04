# Design Language: Limón | Healthy Fast Food | Poke Bowls, Ceviche and Fruity Smoothies

> Extracted from `https://www.limon.no/` on September 4, 2026
> 300 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f7ea48` | rgb(247, 234, 72) | hsl(56, 92%, 63%) | 16 |
| Secondary | `#103b15` | rgb(16, 59, 21) | hsl(127, 57%, 15%) | 88 |
| Accent | `#1d0b0d` | rgb(29, 11, 13) | hsl(353, 45%, 8%) | 152 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 59 |
| `#fcf9f0` | hsl(45, 67%, 96%) | 8 |
| `#dbe2dc` | hsl(129, 11%, 87%) | 6 |
| `#ffffff` | hsl(0, 0%, 100%) | 1 |

### Background Colors

Used on large-area elements: `#1d0b0d`, `#fcf9f0`, `#dbe2dc`, `#103b15`

### Text Colors

Text color palette: `#000000`, `#1d0b0d`, `#103b15`, `#f7ea48`, `#ffffff`, `#dbe2dc`, `#fcf9f0`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#1d0b0d` | text, background | 152 |
| `#103b15` | text, border, background | 88 |
| `#000000` | text | 59 |
| `#f7ea48` | background, text, border | 16 |
| `#fcf9f0` | background, text | 8 |
| `#dbe2dc` | text, background, border | 6 |
| `#ffffff` | text | 1 |

## Typography

### Font Families

- **VenusCom** — used for all (222 elements)
- **Times New Roman** — used for body (65 elements)
- **FreeSans** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 75px | 4.6875rem | 400 | 93.75px | normal | p |
| 68px | 4.25rem | 400 | 81.6px | 2.04px | h2 |
| 54px | 3.375rem | 400 | 54px | normal | h1, br, h2, h3 |
| 46px | 2.875rem | 300 | 52.9px | normal | p |
| 36px | 2.25rem | 700 | 43.2px | normal | h2, h3, span, a |
| 30px | 1.875rem | 400 | 40.5px | normal | p, br, a, span |
| 26px | 1.625rem | 300 | 33.8px | normal | p |
| 20px | 1.25rem | 300 | 29px | normal | p, span |
| 19px | 1.1875rem | 700 | 19.2px | 0.38px | a, p, span, ul |
| 16px | 1rem | 400 | normal | normal | html, head, meta, script |
| 14px | 0.875rem | 600 | 19.2px | 0.56px | a, span, i, p |

### Heading Scale

```css
h2 { font-size: 68px; font-weight: 400; line-height: 81.6px; }
h1 { font-size: 54px; font-weight: 400; line-height: 54px; }
h2 { font-size: 36px; font-weight: 700; line-height: 43.2px; }
```

### Body Text

```css
body { font-size: 20px; font-weight: 300; line-height: 29px; }
```

### Font Weights in Use

`400` (227x), `700` (37x), `300` (16x), `600` (14x), `900` (4x), `500` (2x)

## Spacing

**Base unit:** 5px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-0 | 0px | 0rem |
| spacing-25 | 25px | 1.5625rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-45 | 45px | 2.8125rem |
| spacing-50 | 50px | 3.125rem |
| spacing-60 | 60px | 3.75rem |
| spacing-75 | 75px | 4.6875rem |
| spacing-80 | 80px | 5rem |
| spacing-120 | 120px | 7.5rem |
| spacing-144 | 144px | 9rem |
| spacing-165 | 165px | 10.3125rem |
| spacing-320 | 320px | 20rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 1px | 2 |
| full | 100px | 1 |

## CSS Custom Properties

### Typography

```css
--fa-font-solid: normal 900 1em/1 "Font Awesome 6 Free";
--fa-font-regular: normal 400 1em/1 "Font Awesome 6 Free";
--fa-font-brands: normal 400 1em/1 "Font Awesome 6 Brands";
```

### Other

```css
--fa-style-family-brands: "Font Awesome 6 Brands";
--fa-style-family-classic: "Font Awesome 6 Free";
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
| 0px | 0px | min-width |
| xs | 375px | max-width |
| xs | 376px | min-width |
| sm | 426px | max-width |
| sm | 427px | min-width |
| md | 767px | max-width |
| md | 768px | max-width |
| md | 769px | max-width |
| lg | 992px | max-width |
| lg | 1024px | max-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | min-width |
| 2xl | 1600px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.25s`, `1s`, `0.8s`

### Common Transitions

```css
transition: all;
transition: 0.25s ease-in;
transition: visibility 1s ease-in-out;
```

### Keyframe Animations

**infinite-spin**
```css
@keyframes infinite-spin {
  0% { transform: translate(-50%, -50%) rotate(0deg); }
  100% { transform: translate(-50%, -50%) rotate(359deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (5 instances)

```css
.button {
  background-color: rgb(247, 234, 72);
  color: rgb(29, 11, 13);
  font-size: 16px;
  font-weight: 400;
  padding-top: 12px;
  padding-right: 34px;
  border-radius: 0px;
}
```

### Links (27 instances)

```css
.link {
  color: rgb(16, 59, 21);
  font-size: 19px;
  font-weight: 700;
}
```

### Navigation (2 instances)

```css
.navigatio {
  color: rgb(29, 11, 13);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (5 instances)

```css
.foote {
  color: rgb(16, 59, 21);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 30px;
}
```

### Badges (12 instances)

```css
.badge {
  color: rgb(16, 59, 21);
  font-size: 20px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(247, 234, 72);
  color: rgb(16, 59, 21);
  padding: 12px 34px 10px 34px;
  border-radius: 1px;
  border: 2px solid rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 600;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(16, 59, 21);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 600;
```

### Button — 4 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(247, 234, 72);
  color: rgb(16, 59, 21);
  padding: 12px 34px 10px 34px;
  border-radius: 1px;
  border: 2px solid rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 600;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(29, 11, 13);
  padding: 12px 34px 12px 34px;
  border-radius: 0px;
  border: 0px solid rgba(159, 150, 150, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 4 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(16, 59, 21);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 900;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(219, 226, 220);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgba(0, 0, 0, 0);
  font-size: 16px;
  font-weight: 900;
```

## Layout System

**0 grid containers** and **40 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1170px | 0px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/wrap | 10x |
| column/nowrap | 12x |
| row/nowrap | 18x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#1d0b0d` | `#f7ea48` | 15.21:1 | AAA |

## Design System Score

**Overall: 87/100 (Grade: B)**

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
- 142 !important rules — prefer specificity over overrides
- 97% of CSS is unused — consider purging
- 6625 duplicate CSS declarations

## Z-Index Map

**2 unique z-index values** across 1 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| base | 2,5 | div.c.o.n.t.a.i.n.e.r. .c.o.n.t.a.i.n.e.r.-.f.i.x.e.d. .c.o.l.s.S.t.a.c.k, header, a.s.c.r.o.l.l.I.c.o.n. .h.i.d.d.e.n. .b.o.t.t.o.m._.r.i.g.h.t |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| FontAwesome | self-hosted | normal | normal |
| Fontello | self-hosted | normal | normal |
| Nationale | self-hosted | 300, bold, normal | normal |
| VenusCom | self-hosted | normal | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 3 | objectFit: fill, borderRadius: 0px, shape: square |
| thumbnail | 2 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 4:3 (3x), 3.01:1 (2x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `250ms` | 250 |
| `xl` | `1s` | 1000 |

### Easing Families

- **ease-in-out** (7 uses) — `ease`

## Component Anatomy

### button — 14 instances

**Slots:** label

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** unknown (tight)

### Top CTA Verbs

- **order** (10)

### Button Copy Patterns

- "order now" (6×)
- "order" (2×)
- "order here" (2×)

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Get healthy and delicious food on the go. Enjoy one of our colourful poke bowls, our heavenly ceviche or our fruity smoothie bowls.

## Section Roles

Reading order (top→bottom): nav → nav → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.305 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.5)
**Counts:** total 5, svg 2, icon 0, screenshot-like 0, photo-like 3
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `bootstrap` (confidence 0.6)

Evidence:
- bootstrap utility hits: 3

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `VenusCom` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
