# Design Language: Calyx — Botanical Architecture, Stockholm

> Extracted from `http://127.0.0.1:3055/sites/calyx.html` on September 8, 2026
> 147 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#400d05` | rgb(64, 13, 5) | hsl(8, 86%, 14%) | 5 |
| Secondary | `#ede5d3` | rgb(237, 229, 211) | hsl(42, 42%, 88%) | 25 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 147 |
| `#020201` | hsl(60, 33%, 1%) | 85 |
| `#191915` | hsl(60, 9%, 9%) | 39 |

### Background Colors

Used on large-area elements: `#ede5d3`, `#020201`

### Text Colors

Text color palette: `#020201`, `#191915`, `#ede5d3`, `#400d05`

### Gradients

```css
background-image: linear-gradient(oklch(0.18 0.014 110 / 0.25), oklch(0.18 0.014 110 / 0.05) 30%, oklch(0.965 0.012 88 / 0.5)), url("https://images.unsplash.com/photo-1487530811176-3780de880c2d?auto=format&fit=crop&w=2400&q=80");
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 147 |
| `#020201` | text, background | 85 |
| `#191915` | text | 39 |
| `#ede5d3` | background, text | 25 |
| `#400d05` | text | 5 |

## Typography

### Font Families

- **Cardo** — used for all (96 elements)
- **PT Mono** — used for body (39 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 115.2px | 7.2rem | 400 | 105.984px | -2.304px | h1, br, span |
| 89.6px | 5.6rem | 400 | 83.328px | normal | h2, br, span |
| 88px | 5.5rem | 400 | 61.6px | normal | div |
| 53.76px | 3.36rem | 400 | 56.9856px | normal | p |
| 51.2px | 3.2rem | 400 | 53.248px | normal | h2 |
| 36px | 2.25rem | 400 | 40px | normal | a |
| 30px | 1.875rem | 400 | 36px | normal | a, h3, div |
| 24px | 1.5rem | 400 | 32px | normal | div |
| 17px | 1.0625rem | 400 | 26.35px | normal | p |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |
| 15px | 0.9375rem | 400 | 20.625px | normal | p |
| 10.5px | 0.6563rem | 400 | 15.75px | 2.31px | div, nav, a, p |

### Heading Scale

```css
h1 { font-size: 115.2px; font-weight: 400; line-height: 105.984px; }
h2 { font-size: 89.6px; font-weight: 400; line-height: 83.328px; }
h2 { font-size: 51.2px; font-weight: 400; line-height: 53.248px; }
h3 { font-size: 30px; font-weight: 400; line-height: 36px; }
```

### Body Text

```css
body { font-size: 10.5px; font-weight: 400; line-height: 15.75px; }
```

### Font Weights in Use

`400` (147x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-96 | 96px | 6rem |
| spacing-112 | 112px | 7rem |

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-offset-width: 0px;
--tw-ring-inset: ;
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
--tw-contrast: ;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-backdrop-blur: ;
--tw-contain-style: ;
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

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `1.2s`, `1.4s`

### Common Transitions

```css
transition: all;
transition: opacity 1.2s cubic-bezier(0.16, 1, 0.3, 1), transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
transition: transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Links (5 instances)

```css
.link {
  color: oklch(0.46 0.012 110);
  font-size: 10.5px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: oklch(0.46 0.012 110);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

## Layout System

**13 grid containers** and **10 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1480px | 32px |
| 715.943px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 12x |
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 48px 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 9x |
| column/nowrap | 1x |

**Gap values:** `12px`, `24px`, `28px`, `40px`, `48px`, `48px 32px`, `normal 24px`, `normal 32px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 94/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 92/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 82% of CSS is unused — consider purging
- 130 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 3 | bold |

```css
background: linear-gradient(oklch(0.18 0.014 110 / 0.25), oklch(0.18 0.014 110 / 0.05) 30%, oklch(0.965 0.012 88 / 0.5));
```

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Cardo | google-fonts | 400, 700 | italic, normal |
| PT Mono | google-fonts | 400 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xl` | `1.2s` | 1200 |
| `xxl` | `1.4s` | 1400 |

### Easing Families

- **ease-out** (26 uses) — `cubic-bezier(0.16, 1, 0.3, 1)`

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Sample Headings

> Botanical
architecture,
from Stockholm.
> Eleven cuttings, this week.
> Midnight Orchid
> Old Lavender, New Pine
> Hyacinth, in Spite of April
> Untitled, for a Restaurant
> Commission
a thing
that lasts a week.

## Page Intent

**Type:** `blog-post` (confidence 0.35)

## Section Roles

Reading order (top→bottom): nav → nav → testimonial → testimonial → testimonial → testimonial → content → testimonial → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | testimonial | Botanical
architecture,
from Stockholm. | 0.8 |
| 3 | testimonial | — | 0.8 |
| 4 | testimonial | — | 0.8 |
| 5 | testimonial | Eleven cuttings, this week. | 0.8 |
| 6 | content | — | 0.3 |
| 7 | testimonial | — | 0.8 |
| 8 | content | Commission
a thing
that lasts a week. | 0.3 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.343 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Component Library

**Detected:** `tailwindcss` (confidence 0.655)

Evidence:
- tailwind-like class density 65%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Cardo` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
