# Design Language: Website Builder – Easily Create Your Own Website — Squarespace

> Extracted from `https://www.squarespace.com` on September 4, 2026
> 3409 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#200603` | rgb(32, 6, 3) | hsl(6, 83%, 7%) | 1 |
| Secondary | `#1e4c41` | rgb(30, 76, 65) | hsl(166, 43%, 21%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 3585 |
| `#ffffff` | hsl(0, 0%, 100%) | 2722 |
| `#898989` | hsl(0, 0%, 54%) | 624 |
| `#222222` | hsl(0, 0%, 13%) | 31 |
| `#2f2f2f` | hsl(0, 0%, 18%) | 19 |
| `#0e0e0e` | hsl(0, 0%, 5%) | 12 |
| `#e7e7e7` | hsl(0, 0%, 91%) | 10 |
| `#dddddd` | hsl(0, 0%, 87%) | 9 |
| `#5a5a5a` | hsl(0, 0%, 35%) | 6 |
| `#f5f5f4` | hsl(60, 5%, 96%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#000000`, `#2f2f2f`, `#222222`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#1a1a1a`, `#898989`, `#dddddd`, `#222222`, `#101010`, `#0e0e0e`, `#313131`

### Gradients

```css
background-image: linear-gradient(-45deg, rgb(0, 0, 0) 100%, rgba(255, 255, 255, 0) 100%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 70%, rgb(0, 0, 0) 100%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0.4) 0%, rgba(0, 0, 0, 0.4) 100%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 85%, rgb(0, 0, 0) 100%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 50%, rgb(0, 0, 0) 100%);
```

```css
background-image: linear-gradient(90deg, rgb(255, 255, 255) 29.44%, rgb(136, 188, 216) 39.97%, rgb(243, 255, 193) 61.04%, rgb(255, 255, 255) 71.57%), none;
```

```css
background-image: linear-gradient(rgb(255, 255, 255), rgb(255, 255, 255)), linear-gradient(rgb(255, 255, 255), rgb(255, 255, 255));
```

```css
background-image: linear-gradient(0deg, rgba(0, 0, 0, 0) 0%, rgb(0, 0, 0) 100%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 0%, rgb(0, 0, 0) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 3585 |
| `#ffffff` | background, text, border | 2722 |
| `#898989` | text, border | 624 |
| `#222222` | background, text, border | 31 |
| `#2f2f2f` | background, text, border | 19 |
| `#0e0e0e` | text, border | 12 |
| `#e7e7e7` | border | 10 |
| `#dddddd` | text, border, background | 9 |
| `#5a5a5a` | border, background | 6 |
| `#1e4c41` | background | 1 |
| `#200603` | background | 1 |
| `#f5f5f4` | background | 1 |

## Typography

### Font Families

- **Clarkson** — used for all (1088 elements)
- **Clarkson Serif** — used for all (19 elements)
- **ClarksonLight** — used for body (7 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 70px | 4.375rem | 300 | 72.8px | -3.5px | h2 |
| 60px | 3.75rem | 300 | 62.4px | -3.6px | h1, span, p |
| 50px | 3.125rem | 300 | 54px | -2px | h2 |
| 36px | 2.25rem | 400 | 38.88px | -1.44px | p, h2, span |
| 26px | 1.625rem | 400 | 28.08px | -0.52px | h3, p |
| 20px | 1.25rem | 500 | 24px | -0.2px | p, h3 |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 15px | 0.9375rem | 500 | 21px | -0.015px | span, p, a |
| 14px | 0.875rem | 500 | 14px | normal | a, span, div |
| 13px | 0.8125rem | 400 | 18.2px | normal | span, p, div, script |
| 12px | 0.75rem | 400 | 16.8px | normal | span, p, h3, a |

### Heading Scale

```css
h2 { font-size: 70px; font-weight: 300; line-height: 72.8px; }
h1 { font-size: 60px; font-weight: 300; line-height: 62.4px; }
h2 { font-size: 50px; font-weight: 300; line-height: 54px; }
h2 { font-size: 36px; font-weight: 400; line-height: 38.88px; }
h3 { font-size: 26px; font-weight: 400; line-height: 28.08px; }
h3 { font-size: 20px; font-weight: 500; line-height: 24px; }
h3 { font-size: 12px; font-weight: 400; line-height: 16.8px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (3096x), `500` (199x), `300` (87x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-8 | 8px | 0.5rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-52 | 52px | 3.25rem |
| spacing-56 | 56px | 3.5rem |
| spacing-63 | 63px | 3.9375rem |
| spacing-80 | 80px | 5rem |
| spacing-120 | 120px | 7.5rem |
| spacing-160 | 160px | 10rem |
| spacing-240 | 240px | 15rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 40 |
| md | 6px | 6 |
| lg | 16px | 3 |
| full | 30px | 133 |
| full | 50px | 7 |
| full | 100px | 14 |

## Box Shadows

**sm (inset)** — blur: 0px
```css
box-shadow: color(srgb 1 1 1 / 0.2) 0px 0px 0px 2px inset;
```

**sm (inset)** — blur: 0px
```css
box-shadow: color(srgb 0 0 0 / 0.2) 0px 0px 0px 2px inset;
```

**lg** — blur: 16px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 8px 16px 0px;
```

**xl** — blur: 14px
```css
box-shadow: rgba(0, 0, 0, 0.05) 0px 23px 14px 0px, rgba(0, 0, 0, 0.09) 0px 10px 10px 0px, rgba(0, 0, 0, 0.1) 0px 3px 6px 0px;
```

**xl** — blur: 80px
```css
box-shadow: rgba(0, 0, 0, 0.05) 0px 134px 80px 0px, rgba(0, 0, 0, 0.09) 0px 60px 60px 0px, rgba(0, 0, 0, 0.1) 0px 15px 33px 0px;
```

## CSS Custom Properties

### Colors

```css
--color-blue: #0072f0;
--color-focus: #087bb5;
--color-gray-800: #5a5a5a;
--color-shade-t-black-100: #0000000d;
--color-shade-t-white-50: #ffffff14;
--color-gray-500: #898989;
--color-shade-t-white-100: #ffffff1f;
--color-gray-200: #ddd;
--color-pink: #ff9898;
--color-red: #db3642;
--color-gray-900: #1a1a1a;
--color-shade-t-black-50: #00000008;
--color-red-vibrant: red;
```

### Other

```css
--global-nav-height: 80px;
--gradient: 100%;
--grid-gutter-width: 40px;
--promo-banner-height: 48px;
--primitive-white: #fff;
--grid-column-width: calc((100vw - 520px)/12);
--primitive-black: #000;
--gradient-two: 100%;
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
| sm | 420px | max-width |
| sm | 421px | min-width |
| md | 768px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.2s`, `0.35s`, `0.25s`, `0.5s`, `0.6s`, `0.7s`, `0.1s`, `0.75s`, `1s`, `0.45s`, `0.8s`, `0.15s`

### Common Transitions

```css
transition: all;
transition: top 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955);
transition: color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1), background-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
transition: transform 0.35s cubic-bezier(0.645, 0.045, 0.355, 1);
transition: transform 0.25s cubic-bezier(0.645, 0.045, 0.355, 1);
transition: background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), top 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955);
transition: transform 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
transition: opacity 0.3s cubic-bezier(0.895, 0.03, 0.685, 0.22), visibility 0.3s steps(1, start);
transition: opacity 0.3s, visibility 0.3s steps(1);
transition: background-color 0.3s;
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (117 instances)

```css
.button {
  background-color: rgba(255, 255, 255, 0.3);
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (230 instances)

```css
.card {
  background-color: rgb(47, 47, 47);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 23px 14px 0px, rgba(0, 0, 0, 0.09) 0px 10px 10px 0px, rgba(0, 0, 0, 0.1) 0px 3px 6px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (1 instances)

```css
.input {
  background-color: rgba(255, 255, 255, 0.2);
  color: rgb(255, 255, 255);
  border-radius: 8px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (457 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (1034 instances)

```css
.navigatio {
  background-color: rgba(255, 255, 255, 0.1);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
  box-shadow: color(srgb 1 1 1 / 0.2) 0px 0px 0px 2px inset;
}
```

### Footer (491 instances)

```css
.foote {
  background-color: rgb(34, 34, 34);
  color: rgb(255, 255, 255);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (9 instances)

```css
.modal {
  background-color: rgba(0, 0, 0, 0.45);
  border-radius: 8px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (878 instances)

```css
.dropdown {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 0px;
  box-shadow: color(srgb 1 1 1 / 0.2) 0px 0px 0px 2px inset;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Badges (74 instances)

```css
.badge {
  background-color: rgba(255, 255, 255, 0.1);
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
  padding-top: 4px;
  padding-right: 12px;
  border-radius: 30px;
}
```

### Avatars (1 instances)

```css
.avatar {
  border-radius: 100%;
  background-color: rgb(30, 76, 65);
}
```

### Accordions (101 instances)

```css
.accordion {
  color: rgb(0, 0, 0);
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(0, 0, 0);
}
```

### ProgressBars (20 instances)

```css
.progressBar {
  background-color: rgb(0, 0, 0);
  color: rgb(0, 0, 0);
  border-radius: 3px;
  font-size: 16px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 32 instances, 2 variants

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (27 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 12px 16px 12px 16px;
  border-radius: 100px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 27 instances, 1 variant

**Variant 1** (27 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Link — 18 instances, 1 variant

**Variant 1** (18 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 32px 32px 32px 32px;
  border-radius: 8px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 20 instances, 2 variants

**Variant 1** (18 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 26px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgb(217, 217, 217);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 12px;
  font-weight: 400;
```

### Card — 65 instances, 1 variant

**Variant 1** (65 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 15px;
  font-weight: 400;
```

### Button — 4 instances, 3 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 1px solid rgb(221, 221, 221);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgba(255, 255, 255, 0.3);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 30px;
  border: 1px solid rgb(221, 221, 221);
  font-size: 16px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 24px 20px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Other — 12 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 120px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Link — 9 instances, 1 variant

**Variant 1** (9 instances)

```css
  background: rgb(47, 47, 47);
  color: rgb(255, 255, 255);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 9 instances, 1 variant

**Variant 1** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Link — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 16px 48px 40px 48px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Link — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0.2);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 20px 56px 20px 64px solid rgba(0, 0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 32px 40px 32px 40px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 11 instances, 1 variant

**Variant 1** (11 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 32px 0px 32px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 8px 0px 8px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 13px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 8px 0px 8px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 7 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(90, 90, 90);
  color: rgba(16, 16, 16, 0.3);
  padding: 8px 16px 8px 16px;
  border-radius: 4px;
  border: 0px none rgba(16, 16, 16, 0.3);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 8px 16px 8px 16px;
  border-radius: 4px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Button — 3 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgb(49, 49, 49);
  color: rgb(255, 255, 255);
  padding: 17px 22px 17px 22px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 12px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(49, 49, 49);
  padding: 15px 2px 15px 2px;
  border-radius: 0px;
  border: 0px none rgb(49, 49, 49);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**33 grid containers** and **736 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 2400px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 27x |
| 3-column | 2x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 580px 580px;
gap: 40px;
grid-template-columns: 163.328px 163.328px 163.328px 163.344px;
gap: normal 40px;
grid-template-columns: 191.109px 191.109px 191.109px;
gap: 32px;
grid-template-columns: 580px 580px;
gap: 0px 40px;
grid-template-columns: 270px 270px;
gap: 40px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 490x |
| column/nowrap | 245x |
| row/wrap | 1x |

**Gap values:** `0px 40px`, `120px`, `12px`, `16px`, `24px`, `32px`, `40px`, `4px`, `52px`, `8px`, `8px 16px`, `normal 40px`

## Accessibility (WCAG 2.1)

**Overall Score: 50%** — 2 passing, 2 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#ffffff` | `#d9d9d9` | 1.41:1 | FAIL | h3 (2x) |

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#313131` | 13.01:1 | AAA |

## Design System Score

**Overall: 84/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 50/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Good CSS variable tokenization

**Issues:**
- 2 WCAG contrast failures
- 21 !important rules — prefer specificity over overrides
- 53% of CSS is unused — consider purging
- 3388 duplicate CSS declarations

## Gradients

**9 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 3 | bold |
| linear | — | 3 | bold |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 3 | bold |
| linear | 90deg | 4 | bold |
| linear | — | 2 | brand |
| linear | 0deg | 2 | brand |
| linear | — | 2 | brand |

```css
background: linear-gradient(-45deg, rgb(0, 0, 0) 100%, rgba(255, 255, 255, 0) 100%);
background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 70%, rgb(0, 0, 0) 100%);
background: linear-gradient(rgba(0, 0, 0, 0.4) 0%, rgba(0, 0, 0, 0.4) 100%);
background: linear-gradient(rgba(0, 0, 0, 0) 85%, rgb(0, 0, 0) 100%);
background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 50%, rgb(0, 0, 0) 100%);
```

## Z-Index Map

**13 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,20000 | div.g.l.o.b.a.l.-.n.a.v.i.g.a.t.i.o.n._._.a.c.c.o.u.n.t.-.d.r.o.p.d.o.w.n, aside.o.f.f.e.r.s.-.m.o.d.a.l, div.f.o.o.t.e.r._._.l.o.c.a.l.e.-.s.e.t.t.i.n.g.-.m.e.n.u |
| dropdown | 100,900 | div.m.a.d.e.-.w.i.t.h.-.s.q.s.p._._.t.i.t.l.e.-.c.o.n.t.a.i.n.e.r, div.m.o.b.i.l.e.-.c.t.a. .m.o.b.i.l.e.-.c.t.a.-.-.i.s.-.s.t.i.c.k.y, section.c.o.n.v.e.r.s.i.o.n. .c.o.n.v.e.r.s.i.o.n.-.-.c.e.n.t.e.r.e.d |
| sticky | 10,30 | button.c.t.a. .c.t.a.-.-.i.n.l.i.n.e. .c.t.a.-.-.l.i.g.h.t. .g.l.o.b.a.l.-.n.a.v.i.g.a.t.i.o.n._._.a.c.c.o.u.n.t.-.a.v.a.t.a.r, footer.f.o.o.t.e.r, button.c.t.a. .c.t.a.-.-.i.n.l.i.n.e. .c.u.r.s.o.r.-.f.o.l.l.o.w._._.a.r.e.a |
| base | -1,3 | div.g.l.o.b.a.l.-.n.a.v.i.g.a.t.i.o.n._._.d.e.s.k.t.o.p.-.m.e.n.u.-.h.o.v.e.r.-.c.o.n.t.a.i.n.e.r, div.m.a.d.e.-.w.i.t.h.-.s.q.s.p._._.a.c.c.e.s.s.i.b.l.e.-.l.i.s.t, div.v.i.d.e.o.-.b.a.s.e. .c.o.n.v.e.r.s.i.o.n._._.c.e.n.t.e.r.e.d.-.v.i.d.e.o. .c.o.n.v.e.r.s.i.o.n._._.c.e.n.t.e.r.e.d.-.v.i.d.e.o.-.d.e.s.k.t.o.p |

**Issues:**
- [object Object]

## SVG Icons

**12 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 3 |
| sm | 3 |
| md | 4 |
| lg | 1 |
| xl | 1 |

**Icon colors:** `white`, `currentColor`, `black`, `#999999`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| ClarksonLight | self-hosted | 400, normal | normal |
| ClarksonMedium | self-hosted | 400, normal | normal |
| Clarkson | self-hosted | 300, 400, 500 | normal |
| Clarkson Serif | self-hosted | 300, 400, 500 | normal, italic |
| Canela | self-hosted | 400 | normal, italic |
| Noto Sans JP | self-hosted | 300, 400, 500 | normal |
| Noto Sans KR | self-hosted | 300, 400, 500 | normal |
| Noto Serif JP | self-hosted | 300, 400, 500 | normal |
| Noto Serif KR | self-hosted | 300, 400, 500 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 24 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 20 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 5 | objectFit: fill, borderRadius: 0px, shape: square |
| avatar | 5 | objectFit: cover, borderRadius: 50%, shape: circular |
| gallery | 1 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:2 (29x), 3:4 (20x), 1:1 (5x), 4:3 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `450ms` | 450 |
| `xl` | `750ms` | 750 |

### Easing Families

- **custom** (216 uses) — `cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `cubic-bezier(0.645, 0.045, 0.355, 1)`
- **ease-out** (67 uses) — `cubic-bezier(0.165, 0.84, 0.44, 1)`, `cubic-bezier(0.23, 1, 0.32, 1)`, `cubic-bezier(0.25, 0.46, 0.45, 0.94)`
- **ease-in** (1 uses) — `cubic-bezier(0.895, 0.03, 0.685, 0.22)`
- **steps** (49 uses) — `steps(1, start)`, `steps(1)`
- **linear** (13 uses) — `linear`

## Component Anatomy

### card — 184 instances

**Slots:** media

### button — 50 instances

**Slots:** label, icon
**Variants:** link

| variant | count | sample label |
|---|---|---|
| default | 47 | Previous |
| link | 3 | PRODUCTS |

### link — 29 instances


### other — 12 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **get** (8)
- **build** (5)
- **kr** (5)
- **create** (4)
- **sell** (3)
- **previous** (2)
- **next** (2)
- **monetize** (2)

### Button Copy Patterns

- "offer services

promote your experiences and offerings, collect attendee information, and get paid for your work.

great for: camps · consultants · event organi" (3×)
- "sell products

merchandise your products, accept payments, manage orders and shipping, and more.

great for: artisans · retailers · limited releases

→" (3×)
- "kr sek" (3×)
- "previous" (2×)
- "next" (2×)
- "invoice clients

legitimize your business and get paid with professional proposals, contracts, and invoices.

great for: contractors · freelancers · event plann" (2×)
- "get booked

seamless appointment booking, automated calendar management, and integrated payments.

great for: beauty professionals · wellness providers · photog" (2×)
- "collect donations

create fundraising campaigns, accept donations on your website, and send donors targeted emails.

great for: advocacy groups · non-profits ·" (2×)
- "monetize your content

offer exclusive access to your work, earn recurring revenue, and engage with your community.

great for: instructors · content creators ·" (2×)
- "post your ideas

launch a blog, grow your readership, and add paywalls to monetize access.

great for: food writers · wellness coaches · travel influencers

→" (2×)

### Sample Headings

> A website
makes it real
> Grow your business
> Offer services
> Sell products
> Invoice clients
> A website
makes it real
> Grow your business
> Offer services
> Sell products
> Invoice clients

## Page Intent

**Type:** `landing` (confidence 0.47)
**Description:** Create a website and grow your business with a free Squarespace trial. Start with customizable website templates, AI website builder tools, or a domain name.

Alternates: docs (0.7), blog-post (0.35)

## Section Roles

Reading order (top→bottom): cta → nav → pricing-table → pricing-table → sidebar → pricing → pricing → testimonial → hero → content → content → content → faq → content → content → content → pricing → content → content → content → content → content → content → content → content → content → content → content → footer → content → content → sidebar

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | cta | — | 0.75 |
| 1 | nav | — | 0.9 |
| 2 | pricing-table | A website
makes it real | 0.9 |
| 3 | pricing-table | A website
makes it real | 0.9 |
| 4 | sidebar | — | 0.4 |
| 5 | pricing | Grow your business | 0.4 |
| 6 | pricing | Everything you need on one platform | 0.4 |
| 7 | testimonial | Getting started has never been easier with AI | 0.8 |
| 8 | hero | Find the perfect domain for your website | 0.4 |
| 9 | content | Trusted by 14 million entrepreneurs worldwide | 0.3 |
| 10 | content | Websites made with Squarespace | 0.3 |
| 11 | content | How to build a website | 0.3 |
| 12 | content | — | 0.3 |
| 13 | faq | Frequently asked questions | 0.85 |
| 14 | content | — | 0.3 |
| 15 | content | — | 0.3 |
| 16 | content | — | 0.3 |
| 17 | content | — | 0.3 |
| 18 | content | — | 0.3 |
| 19 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.126 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 9 |

## Imagery Style

**Label:** `photography` (confidence 0.603)
**Counts:** total 55, svg 0, icon 1, screenshot-like 0, photo-like 52
**Dominant aspect:** landscape
**Radius profile on images:** soft

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Clarkson` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
