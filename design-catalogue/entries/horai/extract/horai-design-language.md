# Design Language: Hōrai — A Three-Sister Restaurant, Stockholm

> Extracted from `http://127.0.0.1:3055/sites/horai.html` on September 8, 2026
> 210 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#650001` | rgb(101, 0, 1) | hsl(359, 100%, 20%) | 12 |
| Secondary | `#06190f` | rgb(6, 25, 15) | hsl(148, 61%, 6%) | 3 |
| Accent | `#e0cbab` | rgb(224, 203, 171) | hsl(36, 46%, 77%) | 3 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 210 |
| `#040202` | hsl(0, 33%, 1%) | 145 |
| `#1e1513` | hsl(11, 22%, 10%) | 10 |

### Background Colors

Used on large-area elements: `#e0cbab`, `#040202`

### Text Colors

Text color palette: `#040202`, `#efdfcc`, `#650001`, `#1e1513`, `#06190f`

### Gradients

```css
background-image: linear-gradient(oklch(0.22 0.022 38), oklch(0.22 0.022 38));
```

```css
background-image: radial-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.45) 60%, rgba(0, 0, 0, 0.85) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 210 |
| `#040202` | text, background | 145 |
| `#efdfcc` | text, background | 47 |
| `#650001` | text | 12 |
| `#1e1513` | text | 10 |
| `#e0cbab` | background | 3 |
| `#06190f` | text | 3 |

## Typography

### Font Families

- **Vollkorn** — used for body (141 elements)
- **Cinzel** — used for all (51 elements)
- **Noto Serif JP** — used for body (6 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 192px | 12rem | 400 | 172.8px | 11.52px | h1 |
| 114px | 7.125rem | 400 | 114px | 4.56px | div |
| 89.6px | 5.6rem | 400 | 80.64px | 3.584px | p |
| 81.92px | 5.12rem | 400 | 77.824px | 4.9152px | h2, br, span |
| 71.68px | 4.48rem | 400 | 71.68px | 4.3008px | h2 |
| 58.88px | 3.68rem | 400 | 58.88px | 1.7664px | h3 |
| 51.2px | 3.2rem | 400 | 51.2px | normal | p |
| 46.08px | 2.88rem | 400 | 46.08px | 2.7648px | h2, br, a |
| 35.84px | 2.24rem | 500 | 45.8752px | 12.9024px | blockquote, br |
| 34.2px | 2.1375rem | 400 | 34.2px | normal | p |
| 28.5px | 1.7813rem | 400 | 38px | 5.13px | a, p, span |
| 28.16px | 1.76rem | 400 | 38.72px | 3.9424px | p, br |
| 26.6px | 1.6625rem | 400 | 41.23px | normal | p, br |
| 25.6px | 1.6rem | 500 | 25.6px | 6.656px | p |
| 24.7px | 1.5437rem | 400 | 39.52px | normal | p |

### Heading Scale

```css
h1 { font-size: 192px; font-weight: 400; line-height: 172.8px; }
h2 { font-size: 81.92px; font-weight: 400; line-height: 77.824px; }
h2 { font-size: 71.68px; font-weight: 400; line-height: 71.68px; }
h3 { font-size: 58.88px; font-weight: 400; line-height: 58.88px; }
h2 { font-size: 46.08px; font-weight: 400; line-height: 46.08px; }
```

### Body Text

```css
body { font-size: 28.5px; font-weight: 400; line-height: 38px; }
```

### Font Weights in Use

`400` (206x), `500` (4x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-10 | 10px | 0.625rem |
| spacing-57 | 57px | 3.5625rem |
| spacing-67 | 67px | 4.1875rem |
| spacing-114 | 114px | 7.125rem |
| spacing-152 | 152px | 9.5rem |
| spacing-190 | 190px | 11.875rem |
| spacing-209 | 209px | 13.0625rem |
| spacing-410 | 410px | 25.625rem |

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
| 900px | 900px | max-width |
| lg | 1024px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.5s`, `0.3s`, `0.12s`, `1.3s`, `0.9s`, `1.4s`, `0.15s`

### Common Transitions

```css
transition: all;
transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.3s, visibility 0.3s;
transition: color 0.5s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), fill 0.5s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.5s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.12s ease-out;
transition: opacity 1.3s cubic-bezier(0.16, 1, 0.3, 1), transform 1.3s cubic-bezier(0.16, 1, 0.3, 1);
transition: opacity 0.9s cubic-bezier(0.16, 1, 0.3, 1);
transition: transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Links (3 instances)

```css
.link {
  color: oklch(0.96 0.015 75);
  font-size: 28.5px;
  font-weight: 400;
}
```

## Layout System

**9 grid containers** and **4 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1880px | 66.5px |
| 1061.97px | 0px |
| 820px | 0px |
| 927.223px | 0px |
| 860.993px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 9x |

### Grid Templates

```css
grid-template-columns: 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px;
gap: normal 57px;
grid-template-columns: 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px;
gap: normal 47.5px;
grid-template-columns: 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px;
gap: normal 57px;
grid-template-columns: 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px 52.0312px;
gap: 95px 47.5px;
grid-template-columns: 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px 43.3281px;
gap: normal 57px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 2x |
| column/nowrap | 1x |
| row/wrap | 1x |

**Gap values:** `14.25px normal`, `47.5px 57px`, `57px`, `95px 47.5px`, `normal 47.5px`, `normal 57px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 87/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 70/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 26 distinct font sizes — consider a tighter type scale
- 99% of CSS is unused — consider purging
- 2218 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| radial | — | 3 | bold |

```css
background: linear-gradient(oklch(0.22 0.022 38), oklch(0.22 0.022 38));
background: radial-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.45) 60%, rgba(0, 0, 0, 0.85) 100%);
```

## Z-Index Map

**1 unique z-index values** across 1 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 30,30 | header.f.i.x.e.d. .t.o.p.-.0. .l.e.f.t.-.0. .r.i.g.h.t.-.0. .z.-.3.0 |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Cinzel | google-fonts | 400, 500, 600, 700, 800 | normal |
| Noto Serif JP | google-fonts | 400, 500, 700 | normal |
| Vollkorn | google-fonts | 400, 500, 600 | italic, normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `120ms` | 120 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `900ms` | 900 |
| `xxl` | `1.3s` | 1300 |

### Easing Families

- **custom** (3 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-in-out** (1 uses) — `ease`
- **ease-out** (80 uses) — `cubic-bezier(0.16, 1, 0.3, 1)`

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Sample Headings

> HŌRAI
> THE
HOUSE
> THE
MENUS
> SANSAI
> SEKAI
> UMI
> THE ROOM
> RESERVATIONS
OPEN MONDAYS

## Page Intent

**Type:** `blog-post` (confidence 0.23)

Alternates: landing (0.3)

## Section Roles

Reading order (top→bottom): nav → hero → testimonial → testimonial → testimonial → content → content → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | hero | HŌRAI | 0.85 |
| 2 | testimonial | THE
HOUSE | 0.8 |
| 3 | testimonial | — | 0.8 |
| 4 | testimonial | THE
MENUS | 0.8 |
| 5 | content | — | 0.3 |
| 6 | content | THE ROOM | 0.3 |
| 7 | content | RESERVATIONS
OPEN MONDAYS | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.434 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Component Library

**Detected:** `tailwindcss` (confidence 0.598)

Evidence:
- tailwind-like class density 60%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Vollkorn` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
