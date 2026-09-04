# Design Language: Les voiliers de nos rêves • Miti Navi

> Extracted from `https://miti-navi.com/fr` on September 4, 2026
> 351 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#000e13` | rgb(0, 14, 19) | hsl(196, 100%, 4%) | 156 |
| Secondary | `#ffdead` | rgb(255, 222, 173) | hsl(36, 100%, 84%) | 7 |
| Accent | `#e6dece` | rgb(230, 222, 206) | hsl(40, 32%, 85%) | 94 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#232323` | hsl(0, 0%, 14%) | 361 |
| `#999999` | hsl(0, 0%, 60%) | 70 |
| `#000000` | hsl(0, 0%, 0%) | 18 |
| `#808080` | hsl(0, 0%, 50%) | 2 |

### Background Colors

Used on large-area elements: `#e8ded0`, `#e6dece`, `#000e13`

### Text Colors

Text color palette: `#232323`, `#000e13`, `#999999`, `#000000`, `#e8ded0`, `#e6dece`, `#808080`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#232323` | text, border | 361 |
| `#000e13` | text, border, background | 156 |
| `#e6dece` | background, text, border | 94 |
| `#999999` | text, border | 70 |
| `#000000` | text, border, background | 18 |
| `#ffdead` | border | 7 |
| `#808080` | text | 2 |

## Typography

### Font Families

- **GT Pressura Mono** — used for body (265 elements)
- **Times New Roman** — used for all (57 elements)
- **Voyage** — used for all (25 elements)
- **GTSectraDisplay** — used for headings (4 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 180px | 11.25rem | 400 | 170px | normal | div, span |
| 130px | 8.125rem | 400 | 120px | normal | div, span |
| 110px | 6.875rem | 400 | 154px | normal | span |
| 100px | 6.25rem | 400 | 140px | normal | span |
| 90px | 5.625rem | 400 | 126px | normal | span |
| 80px | 5rem | 400 | 112px | normal | span |
| 72px | 4.5rem | 400 | 64.8px | normal | h1, div |
| 46px | 2.875rem | 400 | 41.4px | normal | h2 |
| 26px | 1.625rem | 400 | 31.2px | normal | h3, img |
| 16px | 1rem | 400 | 22.4px | normal | html, head, meta, title |
| 14px | 0.875rem | 400 | 19.6px | normal | a, span, h4, div |
| 12px | 0.75rem | 400 | 16.8px | 1px | a, div, p, svg |
| 10px | 0.625rem | 400 | 14px | 1px | a, span |

### Heading Scale

```css
h1 { font-size: 72px; font-weight: 400; line-height: 64.8px; }
h2 { font-size: 46px; font-weight: 400; line-height: 41.4px; }
h3 { font-size: 26px; font-weight: 400; line-height: 31.2px; }
h4 { font-size: 14px; font-weight: 400; line-height: 19.6px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 400; line-height: 19.6px; }
```

### Font Weights in Use

`400` (351x)

## Spacing

**Base unit:** 5px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-5 | 5px | 0.3125rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-90 | 90px | 5.625rem |
| spacing-140 | 140px | 8.75rem |
| spacing-240 | 240px | 15rem |

## CSS Custom Properties

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
| md | 768px | min-width |
| lg | 992px | min-width |
| 1090px | 1090px | max-width |
| 1200px | 1200px | min-width |
| xl | 1280px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `1s`, `0.6s`, `1.6s`, `1.2s`, `3s`, `4s`, `0.2s`, `2.75s`, `2.25s`, `2s`

### Common Transitions

```css
transition: all;
transition: 1s 1s;
transition: 0.6s cubic-bezier(0.82, 0, 0.36, 1);
transition: top 1.6s cubic-bezier(0.82, 0, 0.36, 1) 1.2s;
transition: top 1s cubic-bezier(0.82, 0, 0.36, 1);
transition: 3s cubic-bezier(0.82, 0, 0.36, 1);
transition: 4s cubic-bezier(0.82, 0, 0.36, 1);
transition: 1s cubic-bezier(0.82, 0, 0.36, 1);
transition: 1.2s cubic-bezier(0.82, 0, 0.36, 1);
transition: 1.2s cubic-bezier(0.82, 0, 0.36, 1) 0.2s;
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (16 instances)

```css
.button {
  background-color: rgb(0, 14, 19);
  color: rgb(230, 222, 206);
  font-size: 14px;
  font-weight: 400;
  padding-top: 15px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (5 instances)

```css
.card {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 24px;
}
```

### Links (42 instances)

```css
.link {
  color: rgb(0, 14, 19);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (15 instances)

```css
.navigatio {
  color: rgb(0, 14, 19);
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (2 instances)

```css
.foote {
  background-color: rgb(0, 14, 19);
  color: rgb(230, 222, 206);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Card — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(35, 35, 35);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(35, 35, 35);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**0 grid containers** and **15 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1320px | 0px |
| 45% | 60px |
| 50% | 16px |
| 33.333% | 16px |
| 25% | 16px |
| 1180px | 0px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 3x |
| column/nowrap | 1x |
| row/wrap | 11x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#e8ded0` | `#000e13` | 14.73:1 | AAA |

## Design System Score

**Overall: 83/100 (Grade: B)**

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
- 26 !important rules — prefer specificity over overrides
- 68% of CSS is unused — consider purging
- 716 duplicate CSS declarations

## Z-Index Map

**6 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 999,999 | div.l.o.g.o.-.l.o.a.d.e.r |
| base | -1,3 | div.s.e.p.-.f.o.o.t, section.h.e.r.o.-.b.a.n.n.e.r. .d.a.r.k. .i.s.-.i.n.v.i.e.w, div.l.o.g.o |

## SVG Icons

**2 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| lg | 1 |
| xl | 1 |

**Icon colors:** `#E8DED0`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Voyage | self-hosted | 400 | normal |
| GT Pressura Mono | self-hosted | 400 | normal |
| GTSectraDisplay | self-hosted | 300 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 2 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 9:16 (3x), 2:3 (2x), 3:2 (1x), 5.52:1 (1x), 3.62:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `lg` | `600ms` | 600 |
| `xl` | `1s` | 1000 |
| `xxl` | `1.6s` | 1600 |

### Easing Families

- **custom** (102 uses) — `cubic-bezier(0.82, 0, 0.36, 1)`

## Component Anatomy

### card — 5 instances

**Slots:** media

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Sample Headings

> Les voiliers de
nos rêves
> Un voilier selon vos envies
> Chantier Naval
> Les voiliers de
nos rêves
> Un voilier selon vos envies
> Chantier Naval
> Les voiliers de
nos rêves
> Un voilier selon vos envies
> Chantier Naval
> Louer votre voilier

## Page Intent

**Type:** `landing` (confidence 0.3)
**Description:** Depuis 40 ans, amoureux de la vie en mer sous toutes ses formes, nous avons fait une synthèse de nos expériences et créé les voiliers de nos rêves.

## Section Roles

Reading order (top→bottom): nav → nav → nav → nav → content → content → hero → content → content → content → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | content | Les voiliers de
nos rêves | 0.3 |
| 5 | content | Les voiliers de
nos rêves | 0.3 |
| 6 | hero | Les voiliers de
nos rêves | 0.85 |
| 7 | content | — | 0.3 |
| 8 | content | Un voilier selon vos envies | 0.3 |
| 9 | content | — | 0.3 |
| 10 | content | — | 0.3 |
| 11 | content | Chantier Naval | 0.3 |
| 12 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.204 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.5)
**Counts:** total 8, svg 2, icon 1, screenshot-like 0, photo-like 6
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `GT Pressura Mono` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
