# Design Language: ORYZO AI

> Extracted from `https://oryzo.ai` on September 4, 2026
> 3577 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#382416` | rgb(56, 36, 22) | hsl(25, 44%, 15%) | 8 |
| Secondary | `#ffedd7` | rgb(255, 237, 215) | hsl(33, 100%, 92%) | 6070 |
| Accent | `#dc5000` | rgb(220, 80, 0) | hsl(22, 100%, 43%) | 175 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#100904` | hsl(25, 60%, 4%) | 439 |
| `#445231` | hsl(85, 25%, 26%) | 417 |
| `#bbac97` | hsl(35, 21%, 66%) | 46 |
| `#6c5f51` | hsl(31, 14%, 37%) | 10 |
| `#000000` | hsl(0, 0%, 0%) | 10 |
| `#5d6c49` | hsl(86, 19%, 35%) | 2 |
| `#201914` | hsl(25, 23%, 10%) | 1 |

### Background Colors

Used on large-area elements: `#100904`, `#445231`, `#f6e0c6`, `#ffedd6`, `#201914`

### Text Colors

Text color palette: `#ffedd7`, `#dc5000`, `#bbac97`, `#100904`, `#5d6c49`, `#445231`, `#ffedd6`, `#6c5f51`, `#000000`

### Gradients

```css
background-image: repeating-linear-gradient(90deg, rgb(255, 237, 215) 0px, rgb(255, 237, 215) 2px, rgba(255, 237, 215, 0) 0px, rgba(255, 237, 215, 0) 4px);
```

```css
background-image: linear-gradient(rgb(253, 254, 237), rgb(255, 191, 2) 17%, rgb(233, 80, 14) 32%, rgb(205, 25, 125), rgb(140, 1, 156), rgb(37, 1, 135), rgb(3, 3, 16));
```

```css
background-image: repeating-linear-gradient(90deg, rgb(255, 237, 215) 0px, rgb(255, 237, 215) 3px, rgba(255, 237, 215, 0) 0px, rgba(255, 237, 215, 0) 6px);
```

```css
background-image: repeating-linear-gradient(0deg, rgb(255, 237, 215) 0px, rgb(255, 237, 215) 3px, rgba(255, 237, 215, 0) 0px, rgba(255, 237, 215, 0) 6px);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#ffedd7` | text, border, background | 6070 |
| `#100904` | background, text, border | 439 |
| `#445231` | background, text, border | 417 |
| `#dc5000` | text, border, background | 175 |
| `#bbac97` | text, border | 46 |
| `#6c5f51` | background, text, border | 10 |
| `#000000` | background, text, border | 10 |
| `#382416` | background | 8 |
| `#ff0000` | background | 5 |
| `#5d6c49` | text, border | 2 |
| `#f6e0c6` | background | 2 |
| `#201914` | background | 1 |

## Typography

### Font Families

- **halyard-display-variable** — used for all (3347 elements)
- **Arial** — used for body (195 elements)
- **Literata** — used for body (34 elements)
- **DM Mono** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 364px | 22.75rem | 500 | 364px | normal | div |
| 201.481px | 12.5926rem | 600 | 241.778px | normal | h5 |
| 192px | 12rem | 600 | 192px | 3.456px | h2 |
| 130.37px | 8.1481rem | 600 | 156.444px | normal | h5 |
| 109.333px | 6.8333rem | 500 | 98.4px | -1.968px | h1, div |
| 57.1437px | 3.5715rem | 600 | 68.5724px | normal | h5, br |
| 45.3333px | 2.8333rem | 500 | 45.3333px | normal | h2, div, svg, use |
| 43.7333px | 2.7333rem | 500 | 39.36px | -1.968px | sup, div |
| 42.88px | 2.68rem | 400 | 51.456px | normal | div |
| 38.6735px | 2.4171rem | 500 | 46.4081px | normal | div, span |
| 36.2667px | 2.2667rem | 500 | 32.64px | normal | span |
| 32.5178px | 2.0324rem | 200 | 76.8px | normal | div, svg, path, span |
| 32px | 2rem | 500 | 34.88px | normal | span |
| 30px | 1.875rem | 500 | 30px | normal | h3, div |
| 25.3333px | 1.5833rem | 400 | 31.996px | normal | div, span |

### Heading Scale

```css
h5 { font-size: 201.481px; font-weight: 600; line-height: 241.778px; }
h2 { font-size: 192px; font-weight: 600; line-height: 192px; }
h5 { font-size: 130.37px; font-weight: 600; line-height: 156.444px; }
h1 { font-size: 109.333px; font-weight: 500; line-height: 98.4px; }
h5 { font-size: 57.1437px; font-weight: 600; line-height: 68.5724px; }
h2 { font-size: 45.3333px; font-weight: 500; line-height: 45.3333px; }
h3 { font-size: 30px; font-weight: 500; line-height: 30px; }
h4 { font-size: 21.3333px; font-weight: 500; line-height: 23.2533px; }
h5 { font-size: 16.2909px; font-weight: 600; line-height: 19.5491px; }
h5 { font-size: 13.3333px; font-weight: 600; line-height: 16px; }
h5 { font-size: 10.6667px; font-weight: 500; line-height: 11.6267px; }
```

### Body Text

```css
body { font-size: 10.6667px; font-weight: 500; line-height: 11.6267px; }
```

### Font Weights in Use

`500` (2214x), `400` (1322x), `300` (19x), `600` (15x), `200` (4x), `700` (3x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-27 | 27px | 1.6875rem |
| spacing-36 | 36px | 2.25rem |
| spacing-40 | 40px | 2.5rem |
| spacing-43 | 43px | 2.6875rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-64 | 64px | 4rem |
| spacing-69 | 69px | 4.3125rem |
| spacing-76 | 76px | 4.75rem |
| spacing-96 | 96px | 6rem |
| spacing-107 | 107px | 6.6875rem |
| spacing-181 | 181px | 11.3125rem |
| spacing-280 | 280px | 17.5rem |
| spacing-364 | 364px | 22.75rem |
| spacing-400 | 400px | 25rem |
| spacing-404 | 404px | 25.25rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| lg | 12px | 4 |
| xl | 20px | 1 |
| full | 32px | 10 |
| full | 40px | 4 |
| full | 50px | 3 |
| full | 100px | 2 |

## Box Shadows

**xs (inset)** — blur: 3px
```css
box-shadow: rgb(255, 160, 0) 0px 0px 3px 2px inset, rgb(224, 112, 16) 0px 0px 8px 4px inset;
```

**sm (inset)** — blur: 5px
```css
box-shadow: rgba(255, 160, 0, 0.6) 0px 0px 5px 2px inset, rgb(224, 112, 16) 0px 0px 15px 8px inset, rgba(230, 100, 10, 0.45) 0px 0px 35px 15px inset, rgba(230, 80, 10, 0.35) 0px 0px 45px 20px inset;
```

**md** — blur: 10px
```css
box-shadow: rgba(255, 140, 0, 0.6) 0px 0px 10px 3px;
```

**md** — blur: 10px
```css
box-shadow: rgba(255, 140, 0, 0.6) 0px 0px 10px 3px, rgba(230, 80, 10, 0.25) 0px 0px 60px 45px;
```

## CSS Custom Properties

### Colors

```css
--color-white: #ffedd7;
--color-white-transparent: #ffedd700;
--color-black: #100904;
--color-black-transparent: #10090400;
--color-grey-brown: #6c5f51;
--color-green: #445231;
--color-green-light: #5d6c49;
--color-green-lightest: #f6e0c6;
--color-pure-white: #fff;
--color-pure-black: #000;
--color-orange: #dc5000;
--color-brown: #382416;
```

### Spacing

```css
--site-padding-x: 3.125vw;
--site-padding-y: calc(var(--site-row-height) * 4);
--grid-gap-scale: calc(24 / 90);
--grid-gap-width: calc((100vw - var(--site-padding-x) * 2) / ((var(--grid-columns) / var(--grid-gap-scale)) + var(--grid-columns) - 1));
```

### Typography

```css
--display-font: "halyard-display-variable";
--text-font: "halyard-text-variable";
```

### Other

```css
--vh: 1vh;
--site-row-height: calc(var(--site-padding-x) * 8 / 60);
--grid-columns: 16;
--grid-rows: 1;
--grid-column-width: calc(var(--grid-gap-width) / var(--grid-gap-scale));
--grid-span-width: calc(var(--grid-gap-width) + var(--grid-column-width));
--grid-span-1: var(--grid-column-width);
--grid-span-2: calc(var(--grid-span-width) * 1 + var(--grid-column-width));
--grid-span-3: calc(var(--grid-span-width) * 2 + var(--grid-column-width));
--grid-span-4: calc(var(--grid-span-width) * 3 + var(--grid-column-width));
--grid-span-5: calc(var(--grid-span-width) * 4 + var(--grid-column-width));
--grid-span-6: calc(var(--grid-span-width) * 5 + var(--grid-column-width));
--grid-span-7: calc(var(--grid-span-width) * 6 + var(--grid-column-width));
--grid-span-8: calc(var(--grid-span-width) * 7 + var(--grid-column-width));
--grid-span-9: calc(var(--grid-span-width) * 8 + var(--grid-column-width));
--grid-span-10: calc(var(--grid-span-width) * 9 + var(--grid-column-width));
--grid-span-11: calc(var(--grid-span-width) * 10 + var(--grid-column-width));
--grid-span-12: calc(var(--grid-span-width) * 11 + var(--grid-column-width));
--grid-span-13: calc(var(--grid-span-width) * 12 + var(--grid-column-width));
--grid-span-14: calc(var(--grid-span-width) * 13 + var(--grid-column-width));
--grid-span-15: calc(var(--grid-span-width) * 14 + var(--grid-column-width));
--grid-span-16: calc(var(--grid-span-width) * 15 + var(--grid-column-width));
--inner-width: calc(100vw - var(--site-padding-x) * 2);
--screen-unit: min(var(--inner-width) / (1920 - 60 * 2), calc(var(--vh) * 100) / 1024 * 1.25);
--h1: calc(164 * var(--screen-unit));
--h2: calc(68 * var(--screen-unit));
--h3: calc(45 * var(--screen-unit));
--h4: calc(32 * var(--screen-unit));
--h5: calc(20 * var(--screen-unit));
--sub1: calc(24 * var(--screen-unit));
--sub2: calc(16 * var(--screen-unit));
--body1: calc(38 * var(--screen-unit));
--body2: calc(24 * var(--screen-unit));
--body3: calc(18 * var(--screen-unit));
--link-header: calc(16 * var(--screen-unit));
--quote: calc(30 * var(--screen-unit));
--default: calc(18 * var(--screen-unit));
--btn: calc(16 * var(--screen-unit));
--site-header: 21px;
```

### Dependencies

```css
--site-row-height: --site-padding-x;
--site-padding-y: --site-row-height;
--grid-gap-width: --site-padding-x,--grid-columns,--grid-gap-scale,--grid-columns;
--grid-column-width: --grid-gap-width,--grid-gap-scale;
--grid-span-width: --grid-gap-width,--grid-column-width;
--grid-span-1: --grid-column-width;
--grid-span-2: --grid-span-width,--grid-column-width;
--grid-span-3: --grid-span-width,--grid-column-width;
--grid-span-4: --grid-span-width,--grid-column-width;
--grid-span-5: --grid-span-width,--grid-column-width;
--grid-span-6: --grid-span-width,--grid-column-width;
--grid-span-7: --grid-span-width,--grid-column-width;
--grid-span-8: --grid-span-width,--grid-column-width;
--grid-span-9: --grid-span-width,--grid-column-width;
--grid-span-10: --grid-span-width,--grid-column-width;
--grid-span-11: --grid-span-width,--grid-column-width;
--grid-span-12: --grid-span-width,--grid-column-width;
--grid-span-13: --grid-span-width,--grid-column-width;
--grid-span-14: --grid-span-width,--grid-column-width;
--grid-span-15: --grid-span-width,--grid-column-width;
--grid-span-16: --grid-span-width,--grid-column-width;
--inner-width: --site-padding-x;
--screen-unit: --inner-width,--vh;
--h1: --screen-unit;
--h2: --screen-unit;
--h3: --screen-unit;
--h4: --screen-unit;
--h5: --screen-unit;
--sub1: --screen-unit;
--sub2: --screen-unit;
--body1: --screen-unit;
--body2: --screen-unit;
--body3: --screen-unit;
--link-header: --screen-unit;
--quote: --screen-unit;
--default: --screen-unit;
--btn: --screen-unit;
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

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.3s`, `0.5s`, `0.18s`, `0.25s`, `0.2s`, `0.15s`

### Common Transitions

```css
transition: all;
transition: opacity 0.3s, filter 0.3s;
transition: transform 0.3s;
transition: filter 0.5s;
transition: transform 0.5s cubic-bezier(0.3, 0, 0.66, -0.3);
transition: transform 0.18s ease-in-out;
transition: flex-grow 0.3s, background-color 0.3s;
transition: background-color 0.18s ease-in-out, color 0.18s;
transition: border-color 0.25s;
transition: opacity 0.2s, transform 0.2s;
```

### Keyframe Animations

**hero-card-dot-blink**
```css
@keyframes hero-card-dot-blink {
  0% { opacity: 1; }
  50% { opacity: 0.2; }
  100% { opacity: 1; }
}
```

**bikini-btn-pulse-animation**
```css
@keyframes bikini-btn-pulse-animation {
  0% { transform: scale(0.8); }
  50% { transform: scale(1); }
  100% { transform: scale(0.8); }
}
```

**grip-instruction-wheel-dash**
```css
@keyframes grip-instruction-wheel-dash {
  0% { stroke-dashoffset: 2; }
  100% { stroke-dashoffset: 0; }
}
```

**newsletter-btn-loading**
```css
@keyframes newsletter-btn-loading {
  0%, 100% { transform: translate(0px); }
  50% { transform: translate(0.25em); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (13 instances)

```css
.button {
  background-color: rgb(56, 36, 22);
  color: rgb(255, 237, 215);
  font-size: 10.6667px;
  font-weight: 500;
  padding-top: 12.8px;
  padding-right: 21.3333px;
  border-radius: 32px;
}
```

### Inputs (2 instances)

```css
.input {
  color: rgb(255, 237, 215);
  border-color: rgb(255, 237, 215);
  border-radius: 0px;
  font-size: 10.6667px;
  padding-top: 10.6667px;
  padding-right: 16px;
}
```

### Links (22 instances)

```css
.link {
  color: rgb(255, 237, 215);
  font-size: 10.6667px;
  font-weight: 500;
}
```

### Navigation (2 instances)

```css
.navigatio {
  color: rgb(255, 237, 215);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: fixed;
}
```

### Footer (13 instances)

```css
.foote {
  color: rgb(255, 237, 215);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12px;
}
```

### Modals (2 instances)

```css
.modal {
  border-radius: 40px;
  box-shadow: rgba(255, 140, 0, 0.6) 0px 0px 10px 3px, rgba(230, 80, 10, 0.25) 0px 0px 60px 45px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Tables (1 instances)

```css
.table {
  border-color: rgb(255, 237, 215);
  cell-style: [object Object];
}
```

### ProgressBars (9 instances)

```css
.progressBar {
  background-color: rgb(108, 95, 81);
  color: rgb(255, 237, 215);
  border-radius: 0px;
  font-size: 12px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(220, 80, 0);
  color: rgb(16, 9, 4);
  padding: 12.8px 21.3333px 12.8px 21.3333px;
  border-radius: 32px;
  border: 0px none rgb(16, 9, 4);
  font-size: 10.6667px;
  font-weight: 500;
```

### Input — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 237, 215);
  padding: 10.6667px 16px 10.6667px 16px;
  border-radius: 0px;
  border: 0px none rgb(255, 237, 215);
  font-size: 10.6667px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 237, 215);
  color: rgb(16, 9, 4);
  padding: 12.8px 21.3333px 12.8px 21.3333px;
  border-radius: 32px;
  border: 0px none rgb(16, 9, 4);
  font-size: 10.6667px;
  font-weight: 500;
```

### Button — 4 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgb(56, 36, 22);
  color: rgb(255, 237, 215);
  padding: 16px 32px 16px 32px;
  border-radius: 32px;
  border: 2px solid rgb(220, 80, 0);
  font-size: 10.6667px;
  font-weight: 500;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 237, 215);
  padding: 6.66667px 0px 6.66667px 0px;
  border-radius: 20px;
  border: 1px dashed rgb(255, 237, 215);
  font-size: 6.66667px;
  font-weight: 500;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(56, 36, 22);
  color: rgb(255, 237, 215);
  padding: 12.8px 21.3333px 12.8px 21.3333px;
  border-radius: 32px;
  border: 2px solid rgba(220, 80, 0, 0);
  font-size: 10.6667px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(56, 36, 22);
  color: rgb(255, 237, 215);
  padding: 12.8px 21.3333px 12.8px 21.3333px;
  border-radius: 32px;
  border: 2px solid rgba(220, 80, 0, 0);
  font-size: 10.6667px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 237, 215);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 237, 215);
  font-size: 13.3333px;
  font-weight: 400;
```

## Layout System

**2 grid containers** and **58 flex containers** detected.

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 16-column | 2x |

### Grid Templates

```css
grid-template-columns: 65.3281px 65.3281px 65.3281px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px;
gap: 0px 16px;
grid-template-columns: 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px 60px;
gap: 0px 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 20x |
| row/nowrap | 37x |
| row/wrap | 1x |

**Gap values:** `0px 16px`, `12px`, `14.2222px`, `2.51576px`, `2.832px`, `21.3333px`, `36px`, `5.33333px`, `7.46667px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#100904` | `#dc5000` | 4.88:1 | AA |

## Design System Score

**Overall: 83/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 40/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 35 distinct font sizes — consider a tighter type scale
- 1336 duplicate CSS declarations

## Gradients

**4 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| repeating-linear | 90deg | 4 | bold |
| linear | — | 7 | complex |
| repeating-linear | 90deg | 4 | bold |
| repeating-linear | 0deg | 4 | bold |

```css
background: repeating-linear-gradient(90deg, rgb(255, 237, 215) 0px, rgb(255, 237, 215) 2px, rgba(255, 237, 215, 0) 0px, rgba(255, 237, 215, 0) 4px);
background: linear-gradient(rgb(253, 254, 237), rgb(255, 191, 2) 17%, rgb(233, 80, 14) 32%, rgb(205, 25, 125), rgb(140, 1, 156), rgb(37, 1, 135), rgb(3, 3, 16));
background: repeating-linear-gradient(90deg, rgb(255, 237, 215) 0px, rgb(255, 237, 215) 3px, rgba(255, 237, 215, 0) 0px, rgba(255, 237, 215, 0) 6px);
background: repeating-linear-gradient(0deg, rgb(255, 237, 215) 0px, rgb(255, 237, 215) 3px, rgba(255, 237, 215, 0) 0px, rgba(255, 237, 215, 0) 6px);
```

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,100 | div |
| sticky | 10,99 | span.h.e.r.o.-.v.i.d.e.o._._.b.o.r.d.e.r, header.l.i.n.k.-.h.e.a.d.e.r, span.v.i.d.e.o.-.o.v.e.r.l.a.y._._.b.o.r.d.e.r |
| base | -1,9 | div, button.b.t.n. .i.s.-.o.r.a.n.g.e, button.b.t.n. .i.s.-.f.l.i.p.p.e.r |

## SVG Icons

**20 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 4 |
| sm | 3 |
| md | 4 |
| xl | 9 |

**Icon colors:** `rgb(0, 0, 0)`, `#FFEDD6`, `#FDE9CE`, `#ffedd6`, `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Literata | self-hosted | 200 900 | normal |
| DM Mono | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 23 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 14 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (23x), 4:3 (6x), 16:9 (2x), 2.08:1 (2x), 3:2 (1x), 3.82:1 (1x), 1.98:1 (1x), 3:1 (1x)

## Motion Language

**Feel:** springy · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `sm` | `180ms` | 180 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **spring** (1 uses) — `cubic-bezier(0.3, 0, 0.66, -0.3)`
- **ease-in-out** (2 uses) — `ease`

### Spring / Overshoot Easings

- `cubic-bezier(0.3, 0, 0.66, -0.3)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `grip-instruction-wheel-dash` | custom | stroke-dashoffset | 2 |

## Component Anatomy

### button — 11 instances

**Slots:** label
**Sizes:** large

### input — 2 instances


## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** unknown (tight)

### Top CTA Verbs

- **oorryyzzoo** (3)
- **send** (1)
- **eennccooddee** (1)
- **ppaappeerr** (1)
- **mmooddeell** (1)
- **ccooddee** (1)
- **l** (1)
- **c** (1)

### Button Copy Patterns

- "send" (1×)
- "eennccooddee mmeessssaaggeeddeeccooddee mmeessssaaggee" (1×)
- "oorryyzzoo" (1×)
- "oorryyzzoo pprroo" (1×)
- "oorryyzzoo pprroo mmaaxx" (1×)
- "ppaappeerr" (1×)
- "mmooddeell ((..oobbjj))" (1×)
- "ccooddee ccoommiinngg ssoooonn" (1×)
- "l
l
u
u
s
s
i
i
o
o
n
n
.
.
c
c
o
o" (1×)
- "c
c
o
o
p
p
y
y
 u
u
r
r
l
l" (1×)

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** A physical product, reimagined for the AI era, proving even the smallest idea can feel extraordinary.

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
| Avg saturation | 0.438 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 4 |

## Imagery Style

**Label:** `photography` (confidence 0.473)
**Counts:** total 37, svg 0, icon 0, screenshot-like 0, photo-like 33
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `halyard-display-variable` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
