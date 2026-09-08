# Design Language: Tidvatten, kallbadhus och vedeldad bastuklubb i Malmö

> Extracted from `http://127.0.0.1:3055/sites/tidvatten.html` on September 8, 2026
> 200 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#680c00` | rgb(104, 12, 0) | hsl(7, 100%, 20%) | 6 |
| Secondary | `#af2c0a` | rgb(175, 44, 10) | hsl(12, 89%, 36%) | 3 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 179 |
| `#020304` | hsl(210, 33%, 1%) | 123 |
| `#d6e0e5` | hsl(200, 22%, 87%) | 46 |
| `#12161b` | hsl(213, 20%, 9%) | 31 |
| `#6d7c85` | hsl(203, 10%, 47%) | 19 |
| `#cbd6de` | hsl(205, 22%, 83%) | 5 |
| `#b1c0ca` | hsl(204, 19%, 74%) | 1 |

### Background Colors

Used on large-area elements: `#cbd6de`, `#010204`, `#b1c0ca`

### Text Colors

Text color palette: `#020304`, `#d6e0e5`, `#680c00`, `#12161b`, `#6d7c85`, `#af2c0a`, `#0a1f15`

### Gradients

```css
background-image: linear-gradient(oklch(0.2 0.022 245 / 0.7), oklch(0.2 0.022 245 / 0.15), oklch(0.2 0.022 245 / 0.85));
```

```css
background-image: linear-gradient(oklch(0.2 0.022 245), oklch(0.2 0.022 245 / 0.4), oklch(0.2 0.022 245));
```

```css
background-image: radial-gradient(rgba(0, 0, 0, 0) 0%, oklch(0.1 0.02 250 / 0.5) 62%, oklch(0.1 0.02 250 / 0.85) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 179 |
| `#020304` | text, background, border | 123 |
| `#d6e0e5` | text, border, background | 46 |
| `#12161b` | text | 31 |
| `#6d7c85` | text | 19 |
| `#680c00` | text | 6 |
| `#cbd6de` | background | 5 |
| `#af2c0a` | text | 3 |
| `#b1c0ca` | background | 1 |

## Typography

### Font Families

- **Literata** — used for body (120 elements)
- **Fragment Mono** — used for body (38 elements)
- **Familjen Grotesk** — used for all (27 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 166.4px | 10.4rem | 600 | 166.4px | -3.328px | p |
| 147.2px | 9.2rem | 600 | 132.48px | -2.944px | h1 |
| 76.8px | 4.8rem | 600 | 69.12px | -1.536px | p |
| 64px | 4rem | 600 | 60.8px | -1.28px | h2, br |
| 46.08px | 2.88rem | 600 | 46.08px | -0.9216px | h3 |
| 43.52px | 2.72rem | 600 | 41.344px | -0.8704px | h2, br |
| 35.84px | 2.24rem | 400 | 35.84px | normal | div |
| 34.56px | 2.16rem | 600 | 51.84px | -0.3456px | a |
| 30.72px | 1.92rem | 400 | 30.72px | normal | div |
| 25.6px | 1.6rem | 500 | 35.2px | 0.512px | p, br |
| 23.04px | 1.44rem | 500 | 31.104px | 0.4608px | p, br |
| 22.5px | 1.4063rem | 600 | 31.5px | 3.15px | a |
| 21.6px | 1.35rem | 400 | 33.48px | normal | p |
| 20.7px | 1.2937rem | 400 | 33.12px | normal | p |
| 20.25px | 1.2656rem | 400 | 31.5px | normal | span |

### Heading Scale

```css
h1 { font-size: 147.2px; font-weight: 600; line-height: 132.48px; }
h2 { font-size: 64px; font-weight: 600; line-height: 60.8px; }
h3 { font-size: 46.08px; font-weight: 600; line-height: 46.08px; }
h2 { font-size: 43.52px; font-weight: 600; line-height: 41.344px; }
```

### Body Text

```css
body { font-size: 10.5px; font-weight: 400; line-height: 15.75px; }
```

### Font Weights in Use

`400` (174x), `600` (22x), `500` (4x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-5 | 5px | 0.3125rem |
| spacing-45 | 45px | 2.8125rem |
| spacing-63 | 63px | 3.9375rem |
| spacing-72 | 72px | 4.5rem |
| spacing-90 | 90px | 5.625rem |
| spacing-108 | 108px | 6.75rem |
| spacing-162 | 162px | 10.125rem |
| spacing-180 | 180px | 11.25rem |
| spacing-198 | 198px | 12.375rem |

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-ring-offset-width: 0px;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgb(59 130 246 / 0.5);
--tw-ring-offset-color: #fff;
```

### Spacing

```css
--tw-contain-size: ;
--tw-numeric-spacing: ;
```

### Shadows

```css
--tw-shadow: 0 0 #0000;
--tw-drop-shadow: ;
```

### Other

```css
--is: oklch(0.94 0.008 240);
--hav: oklch(0.20 0.022 245);
--djup: oklch(0.22 0.016 250);
--glod: oklch(0.51 0.155 42);
--skugga: oklch(0.10 0.02 250);
--tw-contrast: ;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-contain-style: ;
--tw-backdrop-blur: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-backdrop-invert: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-brightness: ;
--tw-numeric-fraction: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-skew-y: 0;
--tw-backdrop-brightness: ;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-rotate: 0;
--tw-pinch-zoom: ;
--tw-contain-paint: ;
--tw-contain-layout: ;
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
| md | 768px | min-width |
| lg | 1024px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.5s`, `0.15s`, `1.25s`, `1.4s`

### Common Transitions

```css
transition: all;
transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.5s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), fill 0.5s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.5s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 1.25s cubic-bezier(0.16, 1, 0.3, 1), transform 1.25s cubic-bezier(0.16, 1, 0.3, 1);
transition: transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Links (3 instances)

```css
.link {
  color: oklch(0.955 0.006 230);
  font-size: 22.5px;
  font-weight: 600;
}
```

## Layout System

**13 grid containers** and **12 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1680px | 63px |
| 865.638px | 0px |
| 542.88px | 0px |
| 900px | 0px |
| 100% | 0px |
| 480.24px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 13x |

### Grid Templates

```css
grid-template-columns: 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px;
gap: normal 45px;
grid-template-columns: 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px;
gap: normal 45px;
grid-template-columns: 63.1562px 63.1562px 63.1562px 63.1562px 63.1562px 63.1562px 63.1562px 63.1562px 63.1562px 63.1562px 63.1562px 63.1562px;
gap: normal 36px;
grid-template-columns: 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px;
gap: 72px 45px;
grid-template-columns: 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px 54.9062px;
gap: 27px 45px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 10x |
| column/nowrap | 1x |
| row/wrap | 1x |

**Gap values:** `13.5px 45px`, `27px`, `27px 45px`, `72px`, `72px 45px`, `normal 36px`, `normal 45px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 88/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 91% of CSS is unused — consider purging
- 258 duplicate CSS declarations

## Gradients

**3 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 3 | bold |
| linear | — | 3 | bold |
| radial | — | 3 | bold |

```css
background: linear-gradient(oklch(0.2 0.022 245 / 0.7), oklch(0.2 0.022 245 / 0.15), oklch(0.2 0.022 245 / 0.85));
background: linear-gradient(oklch(0.2 0.022 245), oklch(0.2 0.022 245 / 0.4), oklch(0.2 0.022 245));
background: radial-gradient(rgba(0, 0, 0, 0) 0%, oklch(0.1 0.02 250 / 0.5) 62%, oklch(0.1 0.02 250 / 0.85) 100%);
```

## Z-Index Map

**1 unique z-index values** across 1 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 30,30 | header.f.i.x.e.d. .t.o.p.-.0. .l.e.f.t.-.0. .r.i.g.h.t.-.0. .z.-.3.0 |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Familjen Grotesk | google-fonts | 400, 500, 600, 700 | italic, normal |
| Fragment Mono | google-fonts | 400 | italic, normal |
| Literata | google-fonts | 400, 500 | italic, normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 4:3 (1x), 3:4 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `lg` | `500ms` | 500 |
| `xxl` | `1.25s` | 1250 |

### Easing Families

- **custom** (4 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (14 uses) — `cubic-bezier(0.16, 1, 0.3, 1)`

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Sample Headings

> TIDVATTEN
> Kallt vatten,
varmt trä
> Året
på piren
> Morgonbastu
> Vinterdopp
> Fullmånebad
> Gästeldare
> Liggaren
> Tolvbadet
> Säsong

## Page Intent

**Type:** `unknown` (confidence 0)
**Description:** Tidvatten är ett kallbadhus och en vedeldad bastuklubb längst ut på Pir 4 i Nyhamnen, Malmö. Öppet året runt.

## Section Roles

Reading order (top→bottom): nav → content → content → content → content → content → content → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | content | TIDVATTEN | 0.3 |
| 2 | content | Kallt vatten,
varmt trä | 0.3 |
| 3 | content | — | 0.3 |
| 4 | content | Året
på piren | 0.3 |
| 5 | content | — | 0.3 |
| 6 | content | Liggaren | 0.3 |
| 7 | content | Längst ut,
där kajen tar slut | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.362 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 3 |

## Imagery Style

**Label:** `photography` (confidence 1)
**Counts:** total 2, svg 0, icon 0, screenshot-like 0, photo-like 2
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.697)

Evidence:
- tailwind-like class density 68%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Literata` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
