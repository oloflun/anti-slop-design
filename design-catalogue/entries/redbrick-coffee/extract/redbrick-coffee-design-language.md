# Design Language: Redbrick Coffee

> Extracted from `https://redbrick.coffee/` on September 4, 2026
> 779 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#e82c2a` | rgb(232, 44, 42) | hsl(1, 81%, 54%) | 975 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 513 |
| `#212529` | hsl(210, 11%, 15%) | 56 |
| `#f2f2f2` | hsl(0, 0%, 95%) | 32 |
| `#ffffff` | hsl(0, 0%, 100%) | 17 |
| `#121212` | hsl(0, 0%, 7%) | 2 |

### Background Colors

Used on large-area elements: `#ffffff`, `#f2f2f2`, `#e82c2a`

### Text Colors

Text color palette: `#000000`, `#212529`, `#e82c2a`, `#ffffff`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e82c2a` | text, border, background | 975 |
| `#000000` | text, border, background | 513 |
| `#212529` | text, border | 56 |
| `#f2f2f2` | background | 32 |
| `#ffffff` | background, text, border | 17 |
| `#121212` | background, border | 2 |

## Typography

### Font Families

- **Surt** — used for all (492 elements)
- **Times New Roman** — used for body (253 elements)
- **Editorial Old** — used for headings (6 elements)
- **GTStandard-M** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 150px | 9.375rem | 300 | 165px | 0.6px | h1 |
| 105px | 6.5625rem | 300 | 103.95px | -0.5px | h2 |
| 100px | 6.25rem | 300 | 120px | 0.6px | h1 |
| 60px | 3.75rem | 400 | 108px | 0.6px | a |
| 35px | 2.1875rem | 400 | 52.5px | 0.6px | span |
| 30px | 1.875rem | 400 | 45px | 0.4px | input, button |
| 20px | 1.25rem | 400 | 24px | 1px | a, div, link, noscript |
| 15px | 0.9375rem | 400 | 22.5px | 0.6px | span, a, p |
| 10px | 0.625rem | 400 | normal | normal | html, head, meta, link |
| 0px | 0rem | 400 | 0px | normal | button |

### Heading Scale

```css
h1 { font-size: 150px; font-weight: 300; line-height: 165px; }
h2 { font-size: 105px; font-weight: 300; line-height: 103.95px; }
h1 { font-size: 100px; font-weight: 300; line-height: 120px; }
h3 { font-size: 20px; font-weight: 400; line-height: 24px; }
```

### Body Text

```css
body { font-size: 20px; font-weight: 400; line-height: 24px; }
```

### Font Weights in Use

`400` (773x), `300` (6x)

## Spacing

**Base unit:** 5px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-45 | 45px | 2.8125rem |
| spacing-64 | 64px | 4rem |
| spacing-105 | 105px | 6.5625rem |
| spacing-210 | 210px | 13.125rem |
| spacing-420 | 420px | 26.25rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 7 |
| full | 25px | 35 |
| full | 50px | 4 |

## CSS Custom Properties

### Colors

```css
--media-border-opacity: 0.05;
--media-border-width: 1px;
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
--variant-pills-border-width: 1px;
--variant-pills-border-opacity: 0.55;
--alpha-button-border: 1;
--alpha-badge-border: .1;
--bs-border-style: solid;
--bs-border-radius-2xl: 2rem;
--bs-primary-border-subtle: #9ec5fe;
--PhoneInputCountrySelectArrow-color--focus: #03b2cb;
--bs-border-radius-sm: 0.25rem;
--color-badge-foreground: 18,18,18;
--bs-border-radius: 0.375rem;
--bs-highlight-color: #212529;
--bs-border-radius-xxl: 2rem;
--bs-success-bg-subtle: #d1e7dd;
--bs-secondary-bg-subtle: #e2e3e5;
--bs-info-border-subtle: #9eeaf9;
--bs-primary-rgb: 13,110,253;
--bs-secondary-text-emphasis: #2b2f32;
--color-button: 18,18,18;
--PhoneInputCountryFlag-borderColor--focus: #03b2cb;
--bs-info-bg-subtle: #cff4fc;
--bs-light-border-subtle: #e9ecef;
--bs-border-radius-xl: 1rem;
--color-background-contrast: 191,191,191;
--bs-tertiary-color: rgba(33, 37, 41, 0.5);
--bs-dark-bg-subtle: #ced4da;
--bs-border-width: 1px;
--bs-secondary: #6c757d;
--bs-danger-border-subtle: #f1aeb5;
--color-secondary-button-text: 18,18,18;
--bs-form-valid-color: #198754;
--PhoneInputCountryFlag-borderColor: rgba(0, 0, 0, .5);
--PhoneInputCountryFlag-backgroundColor--loading: rgba(0, 0, 0, .1);
--bs-tertiary-color-rgb: 33,37,41;
--bs-highlight-bg: #fff3cd;
--bs-focus-ring-opacity: 0.25;
--PhoneInputCountryFlag-borderWidth: 1px;
--bs-secondary-border-subtle: #c4c8cb;
--bs-tertiary-bg: #f8f9fa;
--bs-form-invalid-border-color: #dc3545;
--color-foreground: 18,18,18;
--bs-secondary-bg-rgb: 233,236,239;
--bs-body-bg: #fff;
--bs-focus-ring-width: 0.25rem;
--bs-link-color: #0d6efd;
--color-link: 18,18,18;
--bs-form-valid-border-color: #198754;
--bs-body-color: #212529;
--color-badge-border: 18,18,18;
--bs-link-hover-color-rgb: 10,88,202;
--bs-warning-bg-subtle: #fff3cd;
--bs-code-color: #d63384;
--bs-primary: #0d6efd;
--bs-light-bg-subtle: #fcfcfd;
--bs-link-hover-color: #0a58ca;
--bs-primary-text-emphasis: #052c65;
--bs-primary-bg-subtle: #cfe2ff;
--bs-body-bg-rgb: 255,255,255;
--color-background: 255,255,255;
--color-badge-background: 255,255,255;
--bs-link-color-rgb: 13,110,253;
--color-button-text: 255,255,255;
--bs-border-radius-lg: 0.5rem;
--bs-success-border-subtle: #a3cfbb;
--bs-focus-ring-color: rgba(13, 110, 253, 0.25);
--bs-border-color: #dee2e6;
--bs-warning-border-subtle: #ffe69c;
--bs-secondary-color-rgb: 33,37,41;
--color-secondary-button: 255,255,255;
--PhoneInput-color--focus: #03b2cb;
--bs-emphasis-color: #000;
--bs-form-invalid-color: #dc3545;
--bs-secondary-color: rgba(33, 37, 41, 0.75);
--bs-body-color-rgb: 33,37,41;
--PhoneInputCountrySelectArrow-color: currentColor;
--color-shadow: 18,18,18;
--bs-danger-bg-subtle: #f8d7da;
--bs-secondary-bg: #e9ecef;
--bs-secondary-rgb: 108,117,125;
--bs-heading-color: ;
--PhoneInputCountrySelectArrow-borderWidth: 1px;
--bs-emphasis-color-rgb: 0,0,0;
--bs-tertiary-bg-rgb: 248,249,250;
--payment-terms-background-color: rgb(255 255 255);
--bs-border-radius-pill: 50rem;
--bs-dark-border-subtle: #adb5bd;
--bs-border-color-translucent: rgba(0, 0, 0, 0.175);
```

### Spacing

```css
--media-padding: px;
--page-width-margin: 0rem;
--spacing-sections-desktop: 0px;
--spacing-sections-mobile: 0px;
--grid-desktop-vertical-spacing: 8px;
--grid-desktop-horizontal-spacing: 8px;
--grid-mobile-vertical-spacing: 4px;
--grid-mobile-horizontal-spacing: 4px;
--inputs-margin-offset: 0px;
--bs-font-monospace: SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
--PhoneInputCountrySelect-marginRight: .35em;
--bs-body-font-size: 1rem;
--PhoneInputCountrySelectArrow-marginLeft: .35em;
```

### Typography

```css
--font-body-family: Assistant, sans-serif;
--font-body-style: normal;
--font-body-weight: 400;
--font-body-weight-bold: 700;
--font-heading-family: Assistant, sans-serif;
--font-heading-style: normal;
--font-heading-weight: 400;
--font-body-scale: 1.0;
--font-heading-scale: 1.0;
--text-boxes-radius: 0px;
--text-boxes-shadow-opacity: 0.0;
--text-boxes-shadow-visible: 0;
--text-boxes-shadow-horizontal-offset: 0px;
--text-boxes-shadow-vertical-offset: 4px;
--text-boxes-shadow-blur-radius: 5px;
--bs-info-text-emphasis: #055160;
--bs-body-line-height: 1.5;
--bs-dark-text-emphasis: #495057;
--bs-light-text-emphasis: #495057;
--bs-font-sans-serif: system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans","Liberation Sans",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
--bs-danger-text-emphasis: #58151c;
--bs-body-font-weight: 400;
--bs-success-text-emphasis: #0a3622;
--bs-warning-text-emphasis: #664d03;
--bs-body-font-family: system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans","Liberation Sans",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
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
--bs-box-shadow-inset: inset 0 1px 2px rgba(0, 0, 0, 0.075);
--bs-box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
--bs-box-shadow-sm: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
--bs-box-shadow-lg: 0 1rem 3rem rgba(0, 0, 0, 0.175);
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
--variant-pills-radius: 40px;
```

### Other

```css
--page-width: 120rem;
--alpha-button-background: 1;
--alpha-link: .85;
--duration-short: .1s;
--duration-default: .2s;
--duration-announcement-bar: .25s;
--duration-medium: .3s;
--duration-long: .5s;
--duration-extra-long: .6s;
--duration-extended: 3s;
--ease-out-slow: cubic-bezier(0, 0, .3, 1);
--animation-slide-in: slideIn var(--duration-extra-long) var(--ease-out-slow) forwards;
--animation-fade-in: fadeIn var(--duration-extra-long) var(--ease-out-slow);
--bs-breakpoint-xs: 0;
--bs-breakpoint-sm: 576px;
--bs-breakpoint-md: 768px;
--bs-breakpoint-lg: 992px;
--bs-breakpoint-xl: 1200px;
--bs-breakpoint-xxl: 1400px;
--bs-orange: #fd7e14;
--bs-cyan: #0dcaf0;
--bs-purple: #6f42c1;
--bs-info-rgb: 13,202,240;
--bs-pink: #d63384;
--bs-gray-100: #f8f9fa;
--bs-white: #fff;
--bs-danger: #dc3545;
--bs-gray-500: #adb5bd;
--bs-teal: #20c997;
--bs-dark: #212529;
--bs-gray-800: #343a40;
--PhoneInputInternationalIconPhone-opacity: .8;
--PhoneInputCountrySelectArrow-transform: rotate(45deg);
--bs-success-rgb: 25,135,84;
--bs-yellow: #ffc107;
--bs-info: #0dcaf0;
--PhoneInputCountryFlag-aspectRatio: 1.5;
--bs-danger-rgb: 220,53,69;
--bs-gray-200: #e9ecef;
--bs-gray-dark: #343a40;
--PhoneInputCountryFlag-height: 1em;
--bs-white-rgb: 255,255,255;
--easter-egg: none;
--bs-light-rgb: 248,249,250;
--PhoneInputCountrySelectArrow-opacity: .45;
--bs-success: #198754;
--PhoneInputCountrySelectArrow-width: .3em;
--bs-warning-rgb: 255,193,7;
--sparkle: url(./sparkle.gif);
--bs-green: #198754;
--bs-gray-400: #ced4da;
--bs-link-decoration: underline;
--bs-gray-600: #6c757d;
--bs-dark-rgb: 33,37,41;
--bs-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));
--bs-indigo: #6610f2;
--PhoneInputInternationalIconGlobe-opacity: .65;
--bs-black-rgb: 0,0,0;
--bs-warning: #ffc107;
--bs-blue: #0d6efd;
--bs-gray: #6c757d;
--bs-red: #dc3545;
--bs-gray-700: #495057;
--bs-black: #000;
--bs-gray-300: #dee2e6;
--bs-gray-900: #212529;
--bs-light: #f8f9fa;
--gradient-background: #ffffff;
```

### Dependencies

```css
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
| 400px | 400px | max-width |
| sm | 500px | min-width |
| sm | 576px | min-width |
| sm | 600px | min-width |
| md | 749px | max-width |
| md | 750px | min-width |
| md | 767px | min-width |
| md | 768px | min-width |
| 880px | 880px | max-width |
| lg | 989px | max-width |
| lg | 990px | min-width |
| lg | 992px | min-width |
| lg | 1023px | max-width |
| lg | 1024px | min-width |
| 1200px | 1200px | min-width |
| 1400px | 1400px | min-width |
| 1440px | 1440px | min-width |
| 1460px | 1460px | min-width |
| 2xl | 1600px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.1s`, `0.15s`, `0.5s`

### Common Transitions

```css
transition: all;
transition: box-shadow 0.1s;
transition: text-decoration 0.1s;
transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
transition: 0.5s ease-out;
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
  0% { opacity: 0; transform: translate(var(--announcement-translate-from)); }
  100% { opacity: 1; transform: translate(0px); }
}
```

**translateAnnouncementSlideOut**
```css
@keyframes translateAnnouncementSlideOut {
  0% { opacity: 1; transform: translate(0px); }
  100% { opacity: 0; transform: translate(var(--announcement-translate-to)); }
}
```

**animateMenuOpen**
```css
@keyframes animateMenuOpen {
  0% { opacity: 0; transform: translateY(-1.5rem); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**upDownMoreEnergy**
```css
@keyframes upDownMoreEnergy {
  0% { transform: translate(0px); }
  25% { transform: translateY(10px); }
  50% { transform: translate(0px); }
  75% { transform: translateY(-10px); }
  100% { transform: translateY(-1px); }
}
```

**progress-bar-stripes**
```css
@keyframes progress-bar-stripes {
  0% { background-position-x: 1rem; }
}
```

**spinner-border**
```css
@keyframes spinner-border {
  100% { transform: rotate(360deg); }
}
```

**spinner-grow**
```css
@keyframes spinner-grow {
  0% { transform: scale(0); }
  50% { opacity: 1; transform: none; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (11 instances)

```css
.button {
  background-color: rgb(18, 18, 18);
  color: rgb(232, 44, 42);
  font-size: 20px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 50px;
  border-radius: 3.75px;
}
```

### Inputs (4 instances)

```css
.input {
  color: rgb(0, 0, 0);
  border-color: rgb(0, 0, 0);
  border-radius: 0px;
  font-size: 20px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (78 instances)

```css
.link {
  color: rgb(232, 44, 42);
  font-size: 20px;
  font-weight: 400;
}
```

### Navigation (11 instances)

```css
.navigatio {
  color: rgb(232, 44, 42);
  padding-top: 12px;
  padding-bottom: 12px;
  padding-left: 12px;
  padding-right: 0px;
  position: static;
}
```

### Footer (5 instances)

```css
.foote {
  color: rgb(232, 44, 42);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 20px;
}
```

### Modals (7 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (42 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(232, 44, 42);
  padding-top: 0px;
}
```

### Switches (1 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(232, 44, 42);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 8 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(18, 18, 18);
  color: rgb(232, 44, 42);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(232, 44, 42);
  font-size: 20px;
  font-weight: 400;
```

**Variant 2** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(232, 44, 42);
  padding: 0px 50px 0px 0px;
  border-radius: 3.75px;
  border: 0px none rgb(232, 44, 42);
  font-size: 20px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(232, 44, 42);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(232, 44, 42);
  font-size: 0px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(232, 44, 42);
  padding: 5px 30px 5px 30px;
  border-radius: 50px;
  border: 1px solid rgb(232, 44, 42);
  font-size: 30px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **69 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 10px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 1x |

### Grid Templates

```css
grid-template-columns: 1280px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 46x |
| row/wrap | 22x |
| column/nowrap | 1x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#e82c2a` | `#121212` | 4.3:1 | AA |

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
- 2006 !important rules — prefer specificity over overrides
- 91% of CSS is unused — consider purging
- 6620 duplicate CSS declarations

## Z-Index Map

**7 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1001,2147483646 | div.w.r.a.p.p.e.r.-.h.e.a.d.e.r, section.s.h.o.p.i.f.y.-.s.e.c.t.i.o.n. .s.h.o.p.i.f.y.-.s.e.c.t.i.o.n.-.g.r.o.u.p.-.h.e.a.d.e.r.-.g.r.o.u.p. .w.r.a.p.p.e.r.-.o.v.e.r.l.a.y.-.m.e.n.u. .p.r.o.m.o.-.v.i.s.i.b.l.e, div.c.o.w.l.e.n.d.a.r.-.b.g. .c.o.w.l.e.n.d.a.r.-.r.o.o.t |
| sticky | 99,99 | div.s.h.o.p.i.f.y.-.s.e.c.t.i.o.n. .w.r.a.p.p.e.r.-.p.r.o.m.o.-.b.a.r |
| base | -100,3 | div, div.s.u.b.s.c.r.i.b.e._._.w.r.a.p.p.e.r. .c.o.l.o.r.-.b.a.c.k.g.r.o.u.n.d.-.1. .g.r.a.d.i.e.n.t. .c.o.n.t.e.n.t.-.c.o.n.t.a.i.n.e.r. .i.s.o.l.a.t.e. .c.o.n.t.e.n.t.-.c.o.n.t.a.i.n.e.r.-.-.f.u.l.l.-.w.i.d.t.h. .s.e.c.t.i.o.n.-.t.e.m.p.l.a.t.e.-.-.1.6.9.6.0.2.7.5.9.3.9.5.8.0._._.3.0.2.0.6.e.c.b.-.2.6.a.b.-.4.5.1.9.-.a.1.6.8.-.4.c.4.6.4.f.4.f.c.a.f.7.-.p.a.d.d.i.n.g, div.f.i.e.l.d |

**Issues:**
- [object Object]

## SVG Icons

**11 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| lg | 10 |
| xl | 1 |

**Icon colors:** `#e82c2a`, `rgb(0, 0, 0)`, `#000`, `#0071CE`, `black`, `white`, `#FFF`, `#fff`, `#1E3764`, `url(#pi-bancontact-a)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Assistant | self-hosted | 400, 700 | normal |
| Surt | self-hosted | 400 | normal |
| Choy | self-hosted | 400 | normal |
| Editorial Old | self-hosted | 300 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 10 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 2 | objectFit: fill, borderRadius: 25px, shape: pill |

**Aspect ratios:** 3:2 (12x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `lg` | `500ms` | 500 |

### Easing Families

- **ease-in-out** (8 uses) — `ease`

## Component Anatomy

### button — 11 instances

**Slots:** label
**Variants:** link · primary

| variant | count | sample label |
|---|---|---|
| primary | 7 | Shop blends |
| default | 3 | Previous |
| link | 1 | Skip to content |

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **shop** (4)
- **skip** (1)
- **stock** (1)
- **previous** (1)
- **next** (1)
- **learn** (1)
- **enquire** (1)
- **reveal** (1)

### Button Copy Patterns

- "skip to content" (1×)
- "shop blends" (1×)
- "stock up" (1×)
- "shop singles" (1×)
- "shop all" (1×)
- "shop merch" (1×)
- "previous" (1×)
- "next" (1×)
- "learn more" (1×)
- "enquire" (1×)

### Sample Headings

> For Coffee Drinkers
> Blends
> Coffee Coffee
> Pods for all drinkers
> Singles
> For Coffee Drinkers
> Blends
> Coffee Coffee
> Pods for all drinkers
> Singles

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** For Coffee Drinkers. Specialty coffee proudly roasted in Canberra.

Alternates: legal (0.4)

## Section Roles

Reading order (top→bottom): content → pricing-table → nav → content → gallery → content → gallery → content → gallery → cta → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | content | — | 0.3 |
| 2 | pricing-table | For Coffee Drinkers | 0.9 |
| 3 | content | For Coffee Drinkers | 0.3 |
| 4 | gallery | Blends | 0.7 |
| 5 | content | Coffee Coffee | 0.3 |
| 6 | gallery | Singles | 0.7 |
| 7 | content | Subscriptions | 0.3 |
| 8 | gallery | Winter Drop | 0.7 |
| 9 | cta | Home Espresso | 0.75 |
| 10 | content | Wholesale | 0.3 |
| 11 | content | Subscribe to get 10% off. | 0.3 |
| 12 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.169 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0.167)
**Counts:** total 12, svg 10, icon 10, screenshot-like 0, photo-like 2
**Dominant aspect:** landscape
**Radius profile on images:** soft

## Component Library

**Detected:** `bootstrap` (confidence 0.7)

Evidence:
- bootstrap utility hits: 4

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Surt` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
