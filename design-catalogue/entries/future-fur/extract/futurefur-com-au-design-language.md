# Design Language: Future Fur | Ultra-Soft Blankets & Throws - 100% Recycled Plastic

> Extracted from `https://futurefur.com.au/` on September 4, 2026
> 1649 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#00a000` | rgb(0, 160, 0) | hsl(120, 100%, 31%) | 2372 |
| Secondary | `#d32c00` | rgb(211, 44, 0) | hsl(13, 100%, 41%) | 430 |
| Accent | `#ebd2c2` | rgb(235, 210, 194) | hsl(23, 51%, 84%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 486 |
| `#ffffff` | hsl(0, 0%, 100%) | 126 |
| `#f6f6f6` | hsl(0, 0%, 96%) | 1 |
| `#242323` | hsl(0, 1%, 14%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#d32c00`

### Text Colors

Text color palette: `#000000`, `#d32c00`, `#ffffff`, `#00a000`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#00a000` | text, border, background | 2372 |
| `#000000` | text, border | 486 |
| `#d32c00` | text, border, background | 430 |
| `#ffffff` | background, text, border | 126 |
| `#503222` | background | 1 |
| `#f6f6f6` | background | 1 |
| `#ebd2c2` | background | 1 |
| `#242323` | background | 1 |

## Typography

### Font Families

- **Inter** — used for all (1339 elements)
- **Times New Roman** — used for body (202 elements)
- **Arial** — used for body (106 elements)
- **GTStandard-M** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 55px | 3.4375rem | 700 | 57px | -2.5px | div, p, br |
| 44px | 2.75rem | 700 | 46px | -2px | h2 |
| 40px | 2.5rem | 700 | 0px | -0.8px | h1, a, div, img |
| 32px | 2rem | 700 | 36px | -1.413px | a |
| 20px | 1.25rem | 700 | 24px | -0.8px | body, link, script, style |
| 16px | 1rem | 700 | 20px | -0.6px | div, span, s |
| 15px | 0.9375rem | 700 | 18px | -0.8px | a |
| 14px | 0.875rem | 700 | 14px | 1px | label, span |
| 13.3333px | 0.8333rem | 400 | normal | normal | input, button, span, svg |
| 13px | 0.8125rem | 700 | 19.5px | -0.8px | legend, span |
| 12px | 0.75rem | 700 | 20.4px | -0.8px | div, span, a |
| 11px | 0.6875rem | 700 | 13.2px | 0.4px | small, span, a, div |
| 10px | 0.625rem | 400 | normal | normal | html, head, meta, link |

### Heading Scale

```css
h2 { font-size: 44px; font-weight: 700; line-height: 46px; }
h1 { font-size: 40px; font-weight: 700; line-height: 0px; }
h2 { font-size: 20px; font-weight: 700; line-height: 24px; }
```

### Body Text

```css
body { font-size: 20px; font-weight: 700; line-height: 24px; }
```

### Font Weights in Use

`700` (1341x), `400` (308x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-24 | 24px | 1.5rem |
| spacing-30 | 30px | 1.875rem |
| spacing-35 | 35px | 2.1875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-44 | 44px | 2.75rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-70 | 70px | 4.375rem |
| spacing-80 | 80px | 5rem |
| spacing-110 | 110px | 6.875rem |
| spacing-128 | 128px | 8rem |
| spacing-256 | 256px | 16rem |
| spacing-385 | 385px | 24.0625rem |
| spacing-425 | 425px | 26.5625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| full | 40px | 2 |
| full | 50px | 36 |

## CSS Custom Properties

### Colors

```css
--media-border-opacity: 0.05;
--media-border-width: 0px;
--product-card-image-padding: 0.0rem;
--product-card-corner-radius: 0.0rem;
--product-card-text-alignment: left;
--product-card-border-width: 0.0rem;
--product-card-border-opacity: 0.1;
--product-card-shadow-opacity: 0.0;
--product-card-shadow-visible: 0;
--product-card-shadow-horizontal-offset: 0.0rem;
--product-card-shadow-vertical-offset: 0.4rem;
--product-card-shadow-blur-radius: 0.5rem;
--collection-card-image-padding: 0.0rem;
--collection-card-corner-radius: 0.0rem;
--collection-card-text-alignment: left;
--collection-card-border-width: 0.0rem;
--collection-card-border-opacity: 0.1;
--collection-card-shadow-opacity: 0.0;
--collection-card-shadow-visible: 0;
--collection-card-shadow-horizontal-offset: 0.0rem;
--collection-card-shadow-vertical-offset: 0.4rem;
--collection-card-shadow-blur-radius: 0.5rem;
--blog-card-image-padding: 0.0rem;
--blog-card-corner-radius: 0.0rem;
--blog-card-text-alignment: left;
--blog-card-border-width: 0.0rem;
--blog-card-border-opacity: 0.1;
--blog-card-shadow-opacity: 0.0;
--blog-card-shadow-visible: 0;
--blog-card-shadow-horizontal-offset: 0.0rem;
--blog-card-shadow-vertical-offset: 0.4rem;
--blog-card-shadow-blur-radius: 0.5rem;
--popup-border-width: 1px;
--popup-border-opacity: 0.1;
--drawer-border-width: 1px;
--drawer-border-opacity: 0.1;
--text-boxes-border-opacity: 0.1;
--text-boxes-border-width: 0px;
--buttons-border-width: 1px;
--buttons-border-opacity: 1.0;
--buttons-border-offset: 0px;
--inputs-border-width: 1px;
--inputs-border-opacity: 0.55;
--variant-pills-border-width: 0px;
--variant-pills-border-opacity: 0.55;
--alpha-button-border: 1;
--alpha-badge-border: 0.1;
--color-badge-foreground: 211,44,0;
--color-background: 255,255,255;
--color-badge-background: 255,255,255;
--color-button-text: 255,255,255;
--color-button: 211,44,0;
--color-secondary-button: 255,255,255;
--color-shadow: 211,44,0;
--color-background-contrast: 191,191,191;
--color-secondary-button-text: 211,44,0;
--color-foreground: 211,44,0;
--payment-terms-background-color: rgb(255 255 255);
--color-link: 211,44,0;
--color-badge-border: 211,44,0;
```

### Spacing

```css
--media-padding: px;
--page-width-margin: 0rem;
--spacing-sections-desktop: 0px;
--spacing-sections-mobile: 0px;
--grid-desktop-vertical-spacing: 16px;
--grid-desktop-horizontal-spacing: 8px;
--grid-mobile-vertical-spacing: 8px;
--grid-mobile-horizontal-spacing: 4px;
--inputs-margin-offset: 0px;
```

### Typography

```css
--font-body-family: Inter, sans-serif;
--font-body-style: normal;
--font-body-weight: 700;
--font-body-weight-bold: 1000;
--font-heading-family: Inter, sans-serif;
--font-heading-style: normal;
--font-heading-weight: 700;
--font-body-scale: 1.0;
--font-heading-scale: 1.0;
--text-boxes-radius: 0px;
--text-boxes-shadow-opacity: 0.0;
--text-boxes-shadow-visible: 0;
--text-boxes-shadow-horizontal-offset: 0px;
--text-boxes-shadow-vertical-offset: 4px;
--text-boxes-shadow-blur-radius: 5px;
```

### Shadows

```css
--media-shadow-opacity: 0.0;
--media-shadow-horizontal-offset: 0px;
--media-shadow-vertical-offset: 4px;
--media-shadow-blur-radius: 5px;
--media-shadow-visible: 0;
--popup-shadow-opacity: 0.05;
--popup-shadow-horizontal-offset: 0px;
--popup-shadow-vertical-offset: 4px;
--popup-shadow-blur-radius: 5px;
--drawer-shadow-opacity: 0.0;
--drawer-shadow-horizontal-offset: 0px;
--drawer-shadow-vertical-offset: 4px;
--drawer-shadow-blur-radius: 5px;
--buttons-shadow-opacity: 0.0;
--buttons-shadow-visible: 0;
--buttons-shadow-horizontal-offset: 0px;
--buttons-shadow-vertical-offset: 4px;
--buttons-shadow-blur-radius: 5px;
--inputs-shadow-opacity: 0.0;
--inputs-shadow-horizontal-offset: 0px;
--inputs-shadow-vertical-offset: 4px;
--inputs-shadow-blur-radius: 5px;
--variant-pills-shadow-opacity: 0.0;
--variant-pills-shadow-horizontal-offset: 0px;
--variant-pills-shadow-vertical-offset: 4px;
--variant-pills-shadow-blur-radius: 5px;
--focused-base-box-shadow: 0 0 0 0.3rem rgb(var(--color-background)), 0 0 0.5rem 0.4rem rgba(var(--color-foreground), 0.3);
```

### Radii

```css
--media-radius: 0px;
--badge-corner-radius: 4.0rem;
--popup-corner-radius: 0px;
--buttons-radius: 0px;
--buttons-radius-outset: 0px;
--inputs-radius: 0px;
--inputs-radius-outset: 0px;
--variant-pills-radius: 0px;
```

### Other

```css
--page-width: 500rem;
--alpha-button-background: 1;
--alpha-link: 0.85;
--focused-base-outline: 0.2rem solid rgba(var(--color-foreground), 0.5);
--focused-base-outline-offset: 0.3rem;
--duration-short: 100ms;
--duration-default: 200ms;
--duration-announcement-bar: 250ms;
--duration-medium: 300ms;
--duration-long: 500ms;
--duration-extra-long: 600ms;
--duration-extra-longer: 750ms;
--duration-extended: 3s;
--ease-out-slow: cubic-bezier(0, 0, 0.3, 1);
--animation-slide-in: slideIn var(--duration-extra-long) var(--ease-out-slow) forwards;
--animation-fade-in: fadeIn var(--duration-extra-long) var(--ease-out-slow);
--header-height: 196px;
--gradient-background: #ffffff;
```

### Dependencies

```css
--focused-base-outline: --color-foreground;
--focused-base-box-shadow: --color-background,--color-foreground;
--animation-slide-in: --duration-extra-long,--ease-out-slow;
--animation-fade-in: --duration-extra-long,--ease-out-slow;
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
| md | 749px | max-width |
| md | 750px | min-width |
| 900px | 900px | min-width |
| lg | 989px | max-width |
| lg | 990px | min-width |
| 1200px | 1200px | max-width |
| 1400px | 1400px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.1s`, `0.2s`, `0.4s`, `0.5s`, `0.15s`, `0.6s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: box-shadow 0.1s;
transition: visibility 0.2s;
transition: transform 0.2s;
transition: transform 0.4s, opacity 0.4s;
transition: background 0.5s cubic-bezier(0.39, 0.58, 0.57, 1), border-color 0.5s cubic-bezier(0.39, 0.58, 0.57, 1);
transition: transform 0.15s, opacity 0.15s;
transition: max-width 0.6s cubic-bezier(0.52, 0, 0.61, 0.99);
transition: width 0.3s cubic-bezier(0.52, 0, 0.61, 0.99);
transition: text-decoration 0.1s;
```

### Keyframe Animations

**shopify-rotator**
```css
@keyframes shopify-rotator {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(270deg); }
}
```

**shopify-dash**
```css
@keyframes shopify-dash {
  0% { stroke-dashoffset: 280px; }
  50% { stroke-dashoffset: 75px; transform: rotate(135deg); }
  100% { stroke-dashoffset: 280px; transform: rotate(450deg); }
}
```

**acceleratedCheckoutLoadingSkeleton**
```css
@keyframes acceleratedCheckoutLoadingSkeleton {
  50% { opacity: var(--shopify-accelerated-checkout-skeleton-animation-opacity-start,1); }
  75% { opacity: var(--shopify-accelerated-checkout-skeleton-animation-opacity-end,.5); }
  100% { opacity: var(--shopify-accelerated-checkout-skeleton-animation-opacity-start,1); }
}
```

**translateAnnouncementSlideIn**
```css
@keyframes translateAnnouncementSlideIn {
  0% { opacity: 0; transform: translateX(var(--announcement-translate-from)); }
  100% { opacity: 1; transform: translateX(0px); }
}
```

**translateAnnouncementSlideOut**
```css
@keyframes translateAnnouncementSlideOut {
  0% { opacity: 1; transform: translateX(0px); }
  100% { opacity: 0; transform: translateX(var(--announcement-translate-to)); }
}
```

**animateMenuOpen**
```css
@keyframes animateMenuOpen {
  0% { opacity: 0; transform: translateY(-1.5rem); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**appear-down**
```css
@keyframes appear-down {
  0% { opacity: 0; margin-top: -1rem; }
  100% { opacity: 1; margin-top: 0px; }
}
```

**animateLocalization**
```css
@keyframes animateLocalization {
  0% { opacity: 0; transform: translateY(0px); }
  100% { opacity: 1; transform: translateY(-1rem); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (54 instances)

```css
.button {
  background-color: rgb(0, 160, 0);
  color: rgb(0, 160, 0);
  font-size: 13.3333px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (53 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (19 instances)

```css
.input {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  border-color: rgb(0, 0, 0);
  border-radius: 0px;
  font-size: 13.3333px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (156 instances)

```css
.link {
  color: rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
}
```

### Navigation (25 instances)

```css
.navigatio {
  color: rgb(0, 160, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (24 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 160, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 20px;
}
```

### Modals (33 instances)

```css
.modal {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 1250px;
}
```

### Dropdowns (28 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(0, 160, 0);
  padding-top: 0px;
}
```

### Badges (4 instances)

```css
.badge {
  color: rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
  padding-top: 5.5px;
  padding-right: 5.5px;
  border-radius: 50%;
}
```

### Accordions (2 instances)

```css
.accordion {
  color: rgb(0, 160, 0);
  font-size: 20px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(0, 160, 0);
}
```

### Switches (28 instances)

```css
.switche {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(0, 160, 0);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(211, 44, 0);
  color: rgb(255, 255, 255);
  padding: 0px 30px 0px 30px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 15px;
  font-weight: 700;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 8px 8px 8px 8px;
  border-radius: 0px;
  border: 4px 0px 0px solid none none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

### Card — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

### Card — 16 instances, 2 variants

**Variant 1** (12 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

**Variant 2** (4 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgba(0, 160, 0, 0.1);
  font-size: 20px;
  font-weight: 700;
```

### Button — 10 instances, 2 variants

**Variant 1** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 1px 6px 1px 6px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgba(0, 160, 0, 0.55);
  padding: 12px 12px 12px 12px;
  border-radius: 50%;
  border: 1px solid rgba(0, 160, 0, 0.1);
  font-size: 13.3333px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 4px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 160, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 160, 0);
  font-size: 20px;
  font-weight: 700;
```

## Layout System

**12 grid containers** and **100 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1250px | 0px |
| 5000px | 8px |
| 100% | 0px |
| 417.066px | 8px |
| calc(25% - 6px) | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 10x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 1280px;
grid-template-columns: 358px;
grid-template-columns: 312px 624px 312px;
gap: 15px 8px;
grid-template-columns: 290px;
grid-template-columns: 290px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 83x |
| column/nowrap | 12x |
| row/wrap | 3x |
| column-reverse/nowrap | 2x |

**Gap values:** `10px`, `15px 8px`, `16px 8px`, `35px`, `50px`, `56px`, `60px 8px`, `80px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 12 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#00a000` | 3.48:1 | AA |
| `#00a000` | `#ffffff` | 3.48:1 | AA |
| `#ffffff` | `#d32c00` | 5.08:1 | AA |

## Design System Score

**Overall: 82/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 56 !important rules — prefer specificity over overrides
- 81% of CSS is unused — consider purging
- 2456 duplicate CSS declarations

## Z-Index Map

**10 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,1000 | cart-drawer.d.r.a.w.e.r. .i.s.-.e.m.p.t.y |
| dropdown | 998,999 | div.c.o.l.l.e.c.t.i.o.n.-.m.e.d.i.a.-.i.m.g. .s.l.i.c.k.-.s.l.i.d.e, div.c.o.l.l.e.c.t.i.o.n.-.m.e.d.i.a.-.i.m.g. .s.l.i.c.k.-.s.l.i.d.e, div.c.o.l.l.e.c.t.i.o.n.-.m.e.d.i.a.-.i.m.g. .s.l.i.c.k.-.s.l.i.d.e |
| base | -100,9 | div, product-modal.p.r.o.d.u.c.t.-.m.e.d.i.a.-.m.o.d.a.l. .m.e.d.i.a.-.m.o.d.a.l, div.f.e.a.t.u.r.e.d.-.p.r.o.d.u.c.t. .p.r.o.d.u.c.t. .p.r.o.d.u.c.t.-.-.m.e.d.i.u.m. .g.r.i.d. .g.r.i.d.-.-.1.-.c.o.l. .g.r.a.d.i.e.n.t. .c.o.l.o.r.-.s.c.h.e.m.e.-.1. .p.r.o.d.u.c.t.-.-.l.e.f.t. .i.s.o.l.a.t.e. .g.r.i.d.-.-.2.-.c.o.l.-.t.a.b.l.e.t |

## SVG Icons

**2 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| md | 1 |

**Icon colors:** `#D32C00`, `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Inter | self-hosted | 700 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 142 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 29 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 7 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (172x), 9.62:1 (2x), 16:9 (2x), 9.21:1 (1x), 1:1 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **ease-out** (35 uses) — `cubic-bezier(0.39, 0.58, 0.57, 1)`, `cubic-bezier(0.25, 0.46, 0.45, 0.94)`
- **custom** (12 uses) — `cubic-bezier(0.52, 0, 0.61, 0.99)`, `cubic-bezier(0.86, 0, 0.07, 1)`

## Component Anatomy

### card — 37 instances

**Slots:** media, footer

### button — 17 instances

**Slots:** label
**Variants:** link

| variant | count | sample label |
|---|---|---|
| default | 14 | Close |
| link | 3 | Skip to content |

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **skip** (2)
- **shop** (2)
- **close** (1)
- **keep** (1)
- **cart** (1)
- **subscribe** (1)

### Button Copy Patterns

- "shop now
shop now" (2×)
- "skip to content" (1×)
- "close" (1×)
- "keep shopping
                x" (1×)
- "cart
(0)
cart" (1×)
- "skip to product information" (1×)
- "subscribe" (1×)

### Sample Headings

> Keep in touch. Feel the soft.
> Dark Brown
> 
              
                Dark Brown
              
            
> Dark Brown
> 
              
                Cream
              
            
> Cream
> Dark Brown
> Dark Brown
> Dark Brown
> 
              
                Dark Brown
              
            

## Page Intent

**Type:** `landing` (confidence 0.51)
**Description:** Made from 100% recycled plastic bottles diverted from landfill, our ultra-soft blankets are a resounding “no thank you” to fast fashion and animal cruelty. Designed for a softer future that just makes

Alternates: pricing (0.6)

## Section Roles

Reading order (top→bottom): nav → nav → pricing-table → hero → nav → content → content → pricing-table → pricing-table → pricing-table → content → pricing-table → content → content → content → content → footer → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | Keep in touch. Feel the soft. | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | pricing-table | Dark Brown | 0.9 |
| 4 | hero | — | 0.85 |
| 5 | content | — | 0.3 |
| 6 | content | — | 0.3 |
| 7 | pricing-table | Dark Brown | 0.9 |
| 8 | pricing-table | Dark Brown | 0.9 |
| 9 | pricing-table | Dark Brown | 0.9 |
| 10 | content | — | 0.3 |
| 11 | pricing-table | 
              
                Dark Brown
              
             | 0.9 |
| 12 | content | — | 0.3 |
| 13 | content | — | 0.3 |
| 14 | content | — | 0.3 |
| 15 | content | — | 0.3 |
| 16 | footer | Keep in touch. Feel the soft. | 0.95 |
| 17 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.347 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.497)
**Counts:** total 178, svg 0, icon 0, screenshot-like 0, photo-like 175
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
