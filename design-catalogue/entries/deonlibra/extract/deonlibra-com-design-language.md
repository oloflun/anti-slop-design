# Design Language: DEON LIBRA

> Extracted from `https://deonlibra.com` on September 4, 2026
> 1508 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#c00121` | rgb(192, 1, 33) | hsl(350, 99%, 38%) | 80 |
| Secondary | `#fff8e7` | rgb(255, 248, 231) | hsl(42, 100%, 95%) | 1480 |
| Accent | `#146ff8` | rgb(20, 111, 248) | hsl(216, 94%, 53%) | 3 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1457 |
| `#ffffff` | hsl(0, 0%, 100%) | 47 |
| `#66635c` | hsl(42, 5%, 38%) | 12 |
| `#808080` | hsl(0, 0%, 50%) | 2 |
| `#f0f0f0` | hsl(0, 0%, 94%) | 1 |
| `#1f2533` | hsl(222, 24%, 16%) | 1 |
| `#949494` | hsl(0, 0%, 58%) | 1 |
| `#c9c9c9` | hsl(0, 0%, 79%) | 1 |
| `#fee9e8` | hsl(3, 92%, 95%) | 1 |

### Background Colors

Used on large-area elements: `#fff8e7`, `#000000`, `#ffffff`, `#c00121`

### Text Colors

Text color palette: `#000000`, `#1f2533`, `#ffffff`, `#0a2540`, `#c00121`, `#28a745`, `#ff0000`, `#808080`, `#fff8e7`, `#66635c`

### Gradients

```css
background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(0, 0, 0));
```

```css
background-image: linear-gradient(to right, rgb(255, 248, 231), rgb(255, 248, 231));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#fff8e7` | background, text, border | 1480 |
| `#000000` | text, border, background | 1457 |
| `#c00121` | background, text, border | 80 |
| `#ffffff` | background, text, border | 47 |
| `#66635c` | text, border | 12 |
| `#0a2540` | text, border | 8 |
| `#146ff8` | border, background | 3 |
| `#28a745` | text, border | 2 |
| `#ff0000` | text, border | 2 |
| `#808080` | text, border | 2 |
| `#8e1f0b` | text, border | 2 |
| `#f0f0f0` | background | 1 |
| `#1f2533` | text | 1 |
| `#949494` | border | 1 |
| `#c9c9c9` | background | 1 |
| `#fee9e8` | background | 1 |

## Typography

### Font Families

- **Inter** — used for body (1200 elements)
- **Times New Roman** — used for body (129 elements)
- **Anton** — used for all (108 elements)
- **Arial** — used for body (68 elements)
- **GTStandard-M** — used for body (2 elements)
- **Roboto** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 60px | 3.75rem | 400 | 72px | -2.4px | h2, motion-element, highlight-text-image |
| 48px | 3rem | 400 | 60px | -1.92px | highlight-text-image, h2, motion-element, strong |
| 40px | 2.5rem | 400 | 48px | -1.6px | h1, h3 |
| 32px | 2rem | 400 | 32px | normal | div, span |
| 28px | 1.75rem | 700 | 38.0016px | -1.12px | h3, a, img, h2 |
| 22px | 1.375rem | 400 | 35.75px | normal | summary, span, svg, path |
| 19.2px | 1.2rem | 400 | 30px | normal | motion-element, p |
| 18px | 1.125rem | 900 | 27px | normal | button, svg, path, h2 |
| 17.92px | 1.12rem | 700 | 27.92px | -0.7168px | h3, a, motion-element |
| 16px | 1rem | 400 | 26px | normal | body, svg, symbol, title |
| 15px | 0.9375rem | 400 | 15px | normal | span |
| 14.4px | 0.9rem | 700 | 18px | normal | span, p, motion-element, div |
| 14px | 0.875rem | 500 | normal | normal | div, span, svg, path |
| 13.6px | 0.85rem | 700 | 16.32px | normal | div, span |
| 13.3333px | 0.8333rem | 400 | normal | normal | button, svg, g, path |

### Heading Scale

```css
h2 { font-size: 60px; font-weight: 400; line-height: 72px; }
h2 { font-size: 48px; font-weight: 400; line-height: 60px; }
h1 { font-size: 40px; font-weight: 400; line-height: 48px; }
h3 { font-size: 28px; font-weight: 700; line-height: 38.0016px; }
h4 { font-size: 22px; font-weight: 400; line-height: 35.75px; }
h2 { font-size: 18px; font-weight: 900; line-height: 27px; }
h3 { font-size: 17.92px; font-weight: 700; line-height: 27.92px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: 26px; }
```

### Font Weights in Use

`400` (1308x), `700` (91x), `800` (91x), `900` (12x), `500` (4x), `600` (2x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-20 | 20px | 1.25rem |
| spacing-24 | 24px | 1.5rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-70 | 70px | 4.375rem |
| spacing-78 | 78px | 4.875rem |
| spacing-84 | 84px | 5.25rem |
| spacing-100 | 100px | 6.25rem |
| spacing-287 | 287px | 17.9375rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 2 |
| md | 8px | 1 |
| xl | 20px | 33 |
| xl | 24px | 21 |
| full | 30px | 1 |
| full | 50px | 63 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(19, 110, 248, 0.3) 0px 0px 0px 5px;
```

**lg** — blur: 13.333px
```css
box-shadow: rgba(8, 19, 79, 0.16) 0px 4px 13.333px 0px;
```

## CSS Custom Properties

### Colors

```css
--buttons-border-width: 1px;
--inputs-border-width: 1px;
--font-pcard-title-family: Anton, sans-serif;
--font-pcard-title-style: normal;
--font-pcard-title-weight: 700;
--font-pcard-title-scale: 1.12;
--font-pcard-title-transform: uppercase;
--font-pcard-title-size: calc(var(--font-pcard-title-scale) * var(--font-body-size));
--color-badge-sale: #c00121;
--color-badge-sale-text: #fff8e7;
--color-badge-soldout: #c00121;
--color-badge-soldout-text: #fff8e7;
--color-badge-hot: #c00121;
--color-badge-hot-text: #fff8e7;
--color-badge-new: #c00121;
--color-badge-new-text: #fff8e7;
--color-cart-bubble: #c00121;
--color-keyboard-focus: 255 248 231;
--pcard-radius: 2.0rem;
--pcard-inner-radius: 1.0rem;
--swiper-theme-color: #007aff;
--color-swiper-controls: var(--color-foreground);
--junipOutlineColor: #637381;
--junipPrimaryColor: #000;
--junipButtonColor: #000;
--junipButtonOutlineColor: undefined80;
--junipStarColor: #c00121;
--junipButtonTextColor: #000;
--junipBorderColor: rgba(0, 0, 0, 0.08);
--junipSurfaceColor: rgba(0, 0, 0, 0.03);
--color-secondary-button: 192,1,33;
--color-secondary-background: 0,0,0;
--color-button-before: #333333;
--color-button-hover-background: 0,0,0;
--color-text-heading: 0,0,0;
--color-secondary-button-text: 255,248,231;
--color-field-text: 0,0,0;
--color-button-hover-text: 255,248,231;
--color-secondary-button-border: 0,0,0;
--color-background: 255,248,231;
--color-border: 0,0,0;
--color-primary: 192,1,33;
--color-foreground-lighten-19: #cfc9bb;
--color-field: 192,1,33;
--color-foreground: 0,0,0;
--color-button-text: 255,255,255;
--color-product-price-sale: 192,1,33;
--color-foreground-lighten-60: #66635c;
--color-button: 0,0,0;
--color-link-hover: 0,0,0;
--color-link: 0,0,0;
```

### Spacing

```css
--font-body-size: 1.6rem;
--font-heading-letter-spacing: -0.04em;
--font-subheading-letter-spacing: 0.0em;
--buttons-letter-spacing: 0.0em;
--font-h1-size: clamp(
      3.2rem,
      calc(1.559454vw + 2.003899rem),
      4.0rem
    );
--font-h2-size: clamp(
      2.56rem,
      calc(1.247563vw + 1.603119rem),
      3.2rem
    );
--font-h3-size: clamp(
      2.24rem,
      calc(1.091618vw + 1.402729rem),
      2.8rem
    );
--font-h4-size: clamp(
      1.76rem,
      calc(0.8577vw + 1.102144rem),
      2.2rem
    );
--font-hd1-size: clamp(
      4.8rem,
      calc(2.339181vw + 3.005848rem),
      6.0rem
    );
--font-hd2-size: clamp(
      3.84rem,
      calc(1.871345vw + 2.404678rem),
      4.8rem
    );
--font-hd3-size: clamp(
      2.88rem,
      calc(1.403509vw + 1.803509rem),
      3.6rem
    );
--font-h5-size: calc(var(--font-heading-scale) * 1.8rem);
--font-h6-size: calc(var(--font-heading-scale) * 1.6rem);
--font-subheading-size: calc(var(--font-subheading-scale) * var(--font-body-size));
--page-width-margin: 0rem;
--header-padding-bottom: 4rem;
--header-padding-bottom-mobile: 3.2rem;
--header-padding-bottom-large: 6rem;
--header-padding-bottom-large-lg: 4rem;
--swiper-navigation-size: 4.8rem;
--page-padding: 1.5rem;
--swiper-navigation-icon-size: 2rem;
--swiper-pagination-bullet-size: 1rem;
--swiper-pagination-bullet-horizontal-gap: .6rem;
--swiper-pagination-bullet-vertical-gap: .6rem;
```

### Typography

```css
--font-body-family: Inter, sans-serif;
--font-body-style: normal;
--font-body-weight: 400;
--font-body-weight-bolder: 800;
--font-body-weight-bold: 700;
--font-body-line-height: 1.625;
--font-heading-family: Anton, sans-serif;
--font-heading-style: normal;
--font-heading-weight: 400;
--font-heading-transform: uppercase;
--font-heading-scale: 1.0;
--font-heading-mobile-scale: 0.8;
--font-hd1-transform: uppercase;
--font-subheading-family: Inter, sans-serif;
--font-subheading-weight: 700;
--font-subheading-scale: 1.12;
--font-subheading-transform: capitalize;
--font-navigation-family: Anton, sans-serif;
--font-navigation-weight: 900;
--font-button-family: Inter, sans-serif;
--font-button-weight: 800;
--textareas-radius: 1.6rem;
```

### Radii

```css
--buttons-radius: 2.4rem;
--inputs-radius: 2.4rem;
--blocks-radius: 2.0rem;
--blocks-radius-mobile: 1.6rem;
--small-blocks-radius: 0.6rem;
--medium-blocks-radius: 1.0rem;
--badges-radius: 0.5rem;
```

### Other

```css
--animation-nav: .5s cubic-bezier(.6, 0, .4, 1);
--animation-default: .5s cubic-bezier(.3, 1, .3, 1);
--animation-fast: .3s cubic-bezier(.7, 0, .3, 1);
--transform-origin-start: left;
--transform-origin-end: right;
--duration-default: 200ms;
--duration-image: 1000ms;
--navigation-transform: uppercase;
--buttons-transform: capitalize;
--buttons-height: 4.8rem;
--page-width: 1410px;
--swiper-navigation-offset-x: 2.4rem;
--header-height: 84px;
--header-offset-top: 56px;
```

### Dependencies

```css
--font-h5-size: --font-heading-scale;
--font-h6-size: --font-heading-scale;
--font-subheading-size: --font-subheading-scale,--font-body-size;
--font-pcard-title-size: --font-pcard-title-scale,--font-body-size;
--color-swiper-controls: --color-foreground;
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
| sm | 512px | max-width |
| sm | 640px | max-width |
| md | 750px | min-width |
| md | 767px | max-width |
| md | 768px | max-width |
| lg | 1024px | min-width |
| 1200px | 1200px | min-width |
| xl | 1280px | min-width |
| 1410px | 1410px | min-width |
| 2xl | 1485px | min-width |
| 2xl | 1536px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.22s`, `0.2s`, `0.15s`, `0.3s`, `0.5s`, `0.1s`, `0.8s`, `0.6s`, `0.54s`, `0.25s`

### Common Transitions

```css
transition: all;
transition: top 0.22s;
transition: opacity 0.2s, transform 0.2s;
transition: 0.15s;
transition: transform 0.3s, opacity 0.3s, visibility 0.3s;
transition: 0.3s;
transition: background-color 0.3s, border-color 0.3s, box-shadow 0.2s;
transition: opacity 0.5s cubic-bezier(0.6, 0, 0.4, 1), transform 0.5s cubic-bezier(0.6, 0, 0.4, 1);
transition: color 0.5s cubic-bezier(0.6, 0, 0.4, 1) 0.1s;
transition: opacity 0.5s cubic-bezier(0.6, 0, 0.4, 1) 0.1s;
```

### Keyframe Animations

**text-underlined**
```css
@keyframes text-underlined {
  0% { transform: scaleX(1); transform-origin: var(--transform-origin-end); }
  50% { transform: scaleX(0); transform-origin: var(--transform-origin-end); }
  51% { transform-origin: var(--transform-origin-start); }
  100% { transform: scaleX(1); }
}
```

**zoom-fade**
```css
@keyframes zoom-fade {
  0% { opacity: 0; transform: scale(1.2); }
  50% { opacity: 1; }
  100% { opacity: 1; transform: scale(1); }
}
```

**zoom-fade-short**
```css
@keyframes zoom-fade-short {
  0% { opacity: 0; transform: scale(1.1); }
  100% { opacity: 1; transform: scale(1); }
}
```

**spin**
```css
@keyframes spin {
  100% { transform: rotate(1turn); }
}
```

**fade-in**
```css
@keyframes fade-in {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**fade-in-up**
```css
@keyframes fade-in-up {
  0% { opacity: 0; transform: translate3d(0px, 30px, 0px); }
  100% { opacity: 1; transform: translateZ(0px); }
}
```

**scrolling-left**
```css
@keyframes scrolling-left {
  0% { transform: translateZ(0px); visibility: visible; }
  100% { transform: translate3d(-100%, 0px, 0px); }
}
```

**scrolling-right**
```css
@keyframes scrolling-right {
  0% { transform: translate3d(-100%, 0px, 0px); visibility: visible; }
  100% { transform: translateZ(0px); }
}
```

**scrolling-left-rtl**
```css
@keyframes scrolling-left-rtl {
  0% { transform: translateZ(0px); visibility: visible; }
  100% { transform: translate3d(100%, 0px, 0px); }
}
```

**scrolling-right-rtl**
```css
@keyframes scrolling-right-rtl {
  0% { transform: translate3d(100%, 0px, 0px); visibility: visible; }
  100% { transform: translateZ(0px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (45 instances)

```css
.button {
  background-color: rgb(192, 1, 33);
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 800;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 24px;
}
```

### Cards (48 instances)

```css
.card {
  background-color: rgb(255, 248, 231);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (23 instances)

```css
.input {
  background-color: rgb(192, 1, 33);
  color: rgb(0, 0, 0);
  border-color: rgb(0, 0, 0);
  border-radius: 0px;
  font-size: 13.3333px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (56 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (34 instances)

```css
.navigatio {
  background-color: rgb(0, 0, 0);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (34 instances)

```css
.foote {
  background-color: rgb(0, 0, 0);
  color: rgb(255, 248, 231);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (39 instances)

```css
.modal {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 0px;
  box-shadow: rgba(8, 19, 79, 0.16) 0px 4px 13.333px 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 420px;
}
```

### Dropdowns (33 instances)

```css
.dropdown {
  background-color: rgb(255, 248, 231);
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Badges (6 instances)

```css
.badge {
  background-color: rgb(192, 1, 33);
  color: rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Tabs (2 instances)

```css
.tab {
  color: rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(255, 248, 231);
  border-radius: 0px;
}
```

### Accordions (27 instances)

```css
.accordion {
  background-color: rgb(255, 248, 231);
  color: rgb(255, 248, 231);
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(255, 248, 231);
}
```

### ProgressBars (1 instances)

```css
.progressBar {
  background-color: rgba(0, 0, 0, 0.1);
  color: rgb(0, 0, 0);
  border-radius: 30px;
  font-size: 16px;
}
```

### Switches (6 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(255, 248, 231);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 4 instances, 3 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 5px 5px 5px 5px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 700;
```

**Variant 2** (1 instance)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 10px 10px 10px 10px;
  border-radius: 10px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 800;
```

**Variant 3** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Input — 3 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 8px 15px 8px 15px;
  border-radius: 10px;
  border: 1px solid rgb(148, 148, 148);
  font-size: 13.3333px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgb(192, 1, 33);
  color: rgb(0, 0, 0);
  padding: 0px 16px 0px 16px;
  border-radius: 24px;
  border: 1px solid rgb(192, 1, 33);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

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

### Button — 1 instance, 1 variant

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

### Button — 1 instance, 1 variant

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

### Button — 1 instance, 1 variant

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

### Button — 5 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgb(192, 1, 33);
  color: rgb(255, 248, 231);
  padding: 0px 40px 0px 40px;
  border-radius: 24px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 800;
```

**Variant 2** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 4px 0px;
  border-radius: 24px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 800;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(255, 248, 231);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 20px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 6 instances, 2 variants

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

**Variant 2** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 20px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Button — 4 instances, 3 variants

**Variant 1** (2 instances)

```css
  background: rgb(192, 1, 33);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 800;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 24px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 800;
```

**Variant 3** (1 instance)

```css
  background: rgb(255, 248, 231);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 1px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 800;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(192, 1, 33);
  color: rgb(255, 248, 231);
  padding: 0px 15px 0px 15px;
  border-radius: 24px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 800;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 800;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 24px 24px 24px 24px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 17.92px;
  font-weight: 700;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 20px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 28px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 248, 231);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 20px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0.03);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(255, 248, 231);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 20px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 248, 231);
  padding: 0px 0px 0px 0px;
  border-radius: 20px;
  border: 0px none rgb(255, 248, 231);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 40px 0px 40px;
  border-radius: 24px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 800;
```

## Layout System

**12 grid containers** and **313 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 460px | 0px |
| 100% | 0px |
| 880px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 3x |
| 3-column | 2x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 585px 585px;
gap: 10px;
grid-template-columns: 590px 590px;
grid-template-columns: 302.844px 757.156px 0px;
gap: normal 60px;
grid-template-columns: 280px 280px 280px 280px;
gap: 20px;
grid-template-columns: 405.328px 309.344px 405.328px;
gap: normal 30px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 278x |
| column/nowrap | 20x |
| row/wrap | 15x |

**Gap values:** `0px 48px`, `0px 6px`, `0px 8px`, `10px`, `12px`, `16px`, `16px 24px`, `20px`, `20px normal`, `24px`, `30px 0px`, `32px`, `40px`, `40px 0px`, `4px`, `5px`, `6px`, `8px`, `8px 16px`, `normal 16px`, `normal 30px`, `normal 4px`, `normal 60px`, `normal 8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 11 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#fff8e7` | `#c00121` | 6.07:1 | AA |
| `#ffffff` | `#000000` | 21:1 | AAA |
| `#000000` | `#f0f0f0` | 18.43:1 | AAA |
| `#1f2533` | `#ffffff` | 15.32:1 | AAA |
| `#fff8e7` | `#000000` | 19.83:1 | AAA |

## Design System Score

**Overall: 83/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 6 font families — consider limiting to 2 (heading + body)
- 125 !important rules — prefer specificity over overrides
- 80% of CSS is unused — consider purging
- 2747 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | to right | 2 | brand |
| linear | to right | 2 | brand |

```css
background: linear-gradient(to right, rgb(0, 0, 0), rgb(0, 0, 0));
background: linear-gradient(to right, rgb(255, 248, 231), rgb(255, 248, 231));
```

## Z-Index Map

**17 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,2147483647 | div.m.d.-.o.v.e.r.l.a.y, div.t.i.m.e.s.a.c.t._.b.i.s._.p.o.p.u.p._.o.v.e.r.l.a.y, div.t.i.m.e.s.a.c.t._.b.i.s._.d.i.a.l.o.g |
| sticky | 10,50 | div.f.i.x.e.d.-.o.v.e.r.l.a.y. .z.-.1.0, div.d.r.a.w.e.r._._.i.n.n.e.r. .f.l.e.x. .f.l.e.x.-.c.o.l. .w.-.f.u.l.l. .h.-.f.u.l.l. .o.v.e.r.f.l.o.w.-.h.i.d.d.e.n, div.d.r.a.w.e.r._._.i.n.n.e.r |
| base | -100,9 | div, button.s.c.r.e.e.n.-.r.e.a.d.e.r.-.b.u.t.t.o.n, a.a.c.s.b.-.s.r.-.o.n.l.y |

**Issues:**
- [object Object]

## SVG Icons

**18 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| md | 13 |
| lg | 4 |

**Icon colors:** `rgb(0, 0, 0)`, `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Inter | self-hosted | 400, 500, 700, 800 | normal, italic |
| Anton | self-hosted | 400 | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 53 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 5 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 16:9 (45x), 1:1 (13x), 3:4 (4x), 1.97:1 (1x), 4.46:1 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `800ms` | 800 |

### Easing Families

- **custom** (30 uses) — `cubic-bezier(0.6, 0, 0.4, 1)`, `cubic-bezier(0.7, 0, 0.2, 1)`, `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (107 uses) — `cubic-bezier(0.3, 1, 0.3, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `scrolling-left` | slide | transform, visibility | 22 |
| `rotator` | rotate | transform | 7 |
| `dash` | rotate | stroke-dashoffset, transform | 7 |
| `junipNodeInserted` | slide | transform | 1 |

## Component Anatomy

### card — 40 instances

**Slots:** media
**Sizes:** medium

### button — 21 instances

**Slots:** label
**Variants:** primary
**Sizes:** lg · md

| variant | count | sample label |
|---|---|---|
| default | 13 | x |
| primary | 8 | SHOP YOUR RITUAL |

### input — 3 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **shop** (4)
- **log** (2)
- **add** (2)
- **x** (1)
- **cart** (1)
- **archive** (1)
- **candles** (1)
- **our** (1)

### Button Copy Patterns

- "add to cart" (2×)
- "shop unbothered elixir" (2×)
- "x" (1×)
- "log in
cart" (1×)
- "log in" (1×)
- "cart" (1×)
- "shop your ritual" (1×)
- "archive" (1×)
- "candles" (1×)
- "shop all" (1×)

### Sample Headings

> SERVING NERVOUS SYSTEM RESETS + SENSORY RITUALS.
> AWARDS
> 4 DIELINE AWARDS
> AWARDS
> 4 DIELINE AWARDS
> ALLURE BEST OF BEAUTY AWARD
> COSMOPOLITAN HOLY GRAIL BEAUTY AWARD
> 2 HYPEBAE BEAUTY AWARDS
> STAY IN THE LOOP:
> ABOUT

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** WELLNESS ROOTED IN RITUAL, ART, & DROP CULTURE. POWERED BY ADAPTOGENS.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → content → feature-grid → nav → features → content → content → content → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | content | — | 0.3 |
| 1 | feature-grid | — | 0.8 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | features | SERVING NERVOUS SYSTEM RESETS + SENSORY RITUALS. | 0.4 |
| 5 | content | — | 0.3 |
| 6 | content | — | 0.3 |
| 7 | content | AWARDS | 0.3 |
| 8 | content | — | 0.3 |
| 9 | content | — | 0.3 |
| 10 | footer | STAY IN THE LOOP: | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.382 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.023)
**Counts:** total 64, svg 0, icon 0, screenshot-like 0, photo-like 3
**Dominant aspect:** landscape
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
