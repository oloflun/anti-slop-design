# Design Language: Busy Bee Honey | America's Truly Traceable Raw Honey

> Extracted from `https://www.busybeehoney.com/` on September 4, 2026
> 911 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ffca50` | rgb(255, 202, 80) | hsl(42, 100%, 66%) | 40 |
| Secondary | `#3b2722` | rgb(59, 39, 34) | hsl(12, 27%, 18%) | 1346 |
| Accent | `#a0342a` | rgb(160, 52, 42) | hsl(5, 58%, 40%) | 31 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 114 |
| `#6fa162` | hsl(108, 25%, 51%) | 21 |

### Background Colors

Used on large-area elements: `#f2ebd0`, `#ffca50`, `#a0342a`, `#6aacc2`, `#000000`, `#3b2722`

### Text Colors

Text color palette: `#000000`, `#3b2722`, `#f2ebd0`, `#a0342a`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#3b2722` | text, border, background | 1346 |
| `#f2ebd0` | background, text, border | 379 |
| `#000000` | text, border, background | 114 |
| `#ffca50` | background, border | 40 |
| `#6aacc2` | background | 35 |
| `#a0342a` | background, text, border | 31 |
| `#6fa162` | background | 21 |

## Typography

### Font Families

- **Times New Roman** — used for body (361 elements)
- **TayBirdie-Regular** — used for all (310 elements)
- **TayMakawao-Regular** — used for all (161 elements)
- **Arial** — used for body (59 elements)
- **barkmanhoney** — used for body (13 elements)
- **AnonymousPro-Regular** — used for body (7 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 210px | 13.125rem | 400 | 210px | normal | h2, span |
| 185px | 11.5625rem | 400 | 148px | -1.85px | h1, div |
| 112.667px | 7.0417rem | 400 | 92.3867px | normal | h2, div, img |
| 76.6667px | 4.7917rem | 400 | 62.8667px | normal | div, h2, br |
| 65px | 4.0625rem | 400 | 65px | normal | span |
| 25.3333px | 1.5833rem | 400 | 25.3333px | normal | h3 |
| 24px | 1.5rem | 400 | 24px | normal | span |
| 18.6667px | 1.1667rem | 400 | 20.5333px | normal | h3 |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 15.3333px | 0.9583rem | 400 | 24.6867px | 0.5px | dialog, div, span |
| 15px | 0.9375rem | 400 | 15px | normal | p, span |
| 14px | 0.875rem | 400 | 14px | normal | nav, div, ul, li |
| 13.6667px | 0.8542rem | 400 | 20.5px | normal | h3, div |
| 13.3333px | 0.8333rem | 400 | 16px | normal | button, span, div |
| 12.6667px | 0.7917rem | 400 | 12.6667px | normal | footer, div, nav, ul |

### Heading Scale

```css
h2 { font-size: 210px; font-weight: 400; line-height: 210px; }
h1 { font-size: 185px; font-weight: 400; line-height: 148px; }
h2 { font-size: 112.667px; font-weight: 400; line-height: 92.3867px; }
h2 { font-size: 76.6667px; font-weight: 400; line-height: 62.8667px; }
h3 { font-size: 25.3333px; font-weight: 400; line-height: 25.3333px; }
h3 { font-size: 18.6667px; font-weight: 400; line-height: 20.5333px; }
h3 { font-size: 13.6667px; font-weight: 400; line-height: 20.5px; }
h5 { font-size: 12px; font-weight: 400; line-height: 12px; }
```

### Body Text

```css
body { font-size: 13.3333px; font-weight: 400; line-height: 16px; }
```

### Font Weights in Use

`400` (911x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-6 | 6px | 0.375rem |
| spacing-60 | 60px | 3.75rem |
| spacing-80 | 80px | 5rem |
| spacing-218 | 218px | 13.625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| full | 38px | 1 |
| full | 50px | 6 |
| full | 500px | 8 |
| full | 1000px | 7 |

## CSS Custom Properties

### Colors

```css
--foreground: #3B2722;
--buttons-border-radius: 500px;
--box-border-radius: 40px;
--border-radius-desktop-large-radius-vw: 3vw;
--border-radius-tab-large-radius-vw: 10vw;
--border-radius-hero: 0px;
--loader-bar-color: var(--color-pale-cream);
--color-white: #ffffff;
--color-dark: #3b2722;
--color-pale-cream: #f2ebd0;
--color-dusty-cian: #6aacc2;
--color-green: #6fa162;
--color-yellow: #ffca50;
--color-red: #a0342a;
--color-transparent: rgba(255,255,255,0);
--color-black-25: rgba(0,0,0,0.25);
--color-black: #000000;
--color-black-50: rgba(0,0,0,0.5);
--color-black-40: rgba(0,0,0,0.4);
--color-black-30: rgba(0,0,0,0.3);
--color-black-20: rgba(0,0,0,0.2);
--color-black-10: rgba(0,0,0,0.1);
--border-radius-small-radius: 16px;
--border-radius-none: 0px;
--border-radius-medium-radius: 40px;
--border-radius-full-rounded-radius: 1000px;
--buttons-circle-button-bg: rgba(255,255,255,0);
--buttons-tertiary-button-hover-color-text: #3b2722;
--form-field-color-default: #f2ebd0;
--buttons-primary-button-icon: #3b2722;
--buttons-primary-button-hover-stroke: #f2ebd0;
--text-text-color-primary: #f2ebd0;
--buttons-tertiary-button-color-line: #f2ebd0;
--form-field-color-active: #ffca50;
--buttons-circle-button-color-icon: #f2ebd0;
--buttons-secondary-button-bg: rgba(255,255,255,0);
--buttons-tertiary-button-color-text: #f2ebd0;
--buttons-secondary-button-hover-bg: rgba(255,255,255,0);
--buttons-seconary-button-color-icon: #f2ebd0;
--buttons-primary-button-hover-color-text: #f2ebd0;
--buttons-tertiary-button-color-icon: #f2ebd0;
--buttons-tertiary-button-hover-bg: rgba(255,255,255,0);
--buttons-secondary-button-stroke: #f2ebd0;
--form-field-color-hover: #ffffff;
--buttons-secondary-button-color-text: #f2ebd0;
--buttons-primary-button-color-text: #3b2722;
--buttons-secondary-button-hover-color-text: #3b2722;
--buttons-primary-button-bg: #ffca50;
--text-text-highlighted-color: #6aacc2;
--labels-circle-label-bg: #ffca50;
--nav-border-color: rgba(0,0,0,0.2);
--buttons-primary-button-stroke: #ffca50;
--text-text-color-secondary: #f2ebd0;
--buttons-primary-button-hover-bg: #ffca50;
--buttons-secondary-button-hover-stroke: #f2ebd0;
--buttons-primary-button-hover-bg-2: #ffca50;
--page-wrap-bg-container: #3b2722;
```

### Spacing

```css
--site-margin-x: var(--spacing-20);
--site-margin-y: var(--spacing-20);
--space-on-top: 5rem;
--desktop-display-1-font-size: 258px;
--desktop-h1-font-size: 135px;
--desktop-h2-font-size: 90px;
--desktop-h3-font-size: 72px;
--desktop-h4-font-size: 56px;
--desktop-h5-font-size: 48px;
--desktop-h6-font-size: 40px;
--desktop-h7-font-size: 32px;
--desktop-h8-font-size: 28px;
--desktop-cta-medium-font-size: 16px;
--desktop-cta-small-font-size: 14px;
--desktop-detail-nav-font-size: 14px;
--desktop-detail-footer-font-size: 14px;
--desktop-detail-large-font-size: 20px;
--desktop-detail-medium-font-size: 14px;
--desktop-detail-small-font-size: 12px;
--desktop-body-large-font-size: 20px;
--desktop-body-medium-font-size: 16px;
--desktop-body-small-font-size: 12.000000953674316px;
--mobile-display-1-font-size: 100px;
--mobile-h1-font-size: 68px;
--mobile-h2-font-size: 50px;
--mobile-h3-font-size: 48px;
--mobile-h4-font-size: 32px;
--mobile-h5-font-size: 40px;
--mobile-h6-font-size: 32px;
--mobile-h7-font-size: 28px;
--mobile-h8-font-size: 20px;
--mobile-body-large-font-size: 16px;
--mobile-body-medium-font-size: 14px;
--mobile-body-small-font-size: 12px;
--mobile-detail-nav-font-size: 40px;
--mobile-detail-footer-font-size: 10px;
--mobile-detail-large-font-size: 16px;
--mobile-detail-medium-font-size: 13px;
--mobile-detail-small-font-size: 12px;
--mobile-cta-medium-font-size: 13px;
--mobile-cta-small-font-size: 12px;
--spacing-0: 0px;
--spacing-1: 4px;
--spacing-2: 8px;
--spacing-3: 12px;
--spacing-4: 16px;
--spacing-5: 20px;
--spacing-6: 24px;
--spacing-7: 28px;
--spacing-8: 32px;
--spacing-9: 36px;
--spacing-10: 40px;
--spacing-11: 44px;
--spacing-12: 48px;
--spacing-13: 52px;
--spacing-14: 56px;
--spacing-15: 60px;
--spacing-16: 64px;
--spacing-17: 68px;
--spacing-18: 72px;
--spacing-19: 76px;
--spacing-20: 80px;
```

### Typography

```css
--desktop-display-1-font-family: TayMakawao-Regular,sans-serif;
--desktop-display-1-line-height: 80%;
--desktop-display-1-font-weight: 400;
--desktop-display-1-font-style: normal;
--desktop-h1-font-family: TayMakawao-Regular,sans-serif;
--desktop-h1-line-height: 82%;
--desktop-h1-font-weight: 400;
--desktop-h1-font-style: normal;
--desktop-h2-font-family: TayMakawao-Regular,sans-serif;
--desktop-h2-line-height: 82%;
--desktop-h2-font-weight: 400;
--desktop-h2-font-style: normal;
--desktop-h3-font-family: TayMakawao-Regular,sans-serif;
--desktop-h3-line-height: 82%;
--desktop-h3-font-weight: 400;
--desktop-h3-font-style: normal;
--desktop-h4-font-family: TayMakawao-Regular,sans-serif;
--desktop-h4-line-height: 100%;
--desktop-h4-font-weight: 400;
--desktop-h4-font-style: normal;
--desktop-h5-font-family: TayMakawao-Regular,sans-serif;
--desktop-h5-line-height: 100%;
--desktop-h5-font-weight: 400;
--desktop-h5-font-style: normal;
--desktop-h6-font-family: TayMakawao-Regular,sans-serif;
--desktop-h6-line-height: 100%;
--desktop-h6-font-weight: 400;
--desktop-h6-font-style: normal;
--desktop-h7-font-family: TayMakawao-Regular,sans-serif;
--desktop-h7-line-height: 100%;
--desktop-h7-font-weight: 400;
--desktop-h7-font-style: normal;
--desktop-h8-font-family: TayMakawao-Regular,sans-serif;
--desktop-h8-line-height: 100%;
--desktop-h8-font-weight: 400;
--desktop-h8-font-style: normal;
--desktop-cta-medium-font-family: TayBirdie-Regular,sans-serif;
--desktop-cta-medium-line-height: 100%;
--desktop-cta-medium-font-weight: 400;
--desktop-cta-medium-font-style: normal;
--desktop-cta-small-font-family: TayBirdie-Regular,sans-serif;
--desktop-cta-small-line-height: 80%;
--desktop-cta-small-font-weight: 400;
--desktop-cta-small-font-style: normal;
--desktop-detail-nav-font-family: TayBirdie-Regular,sans-serif;
--desktop-detail-nav-line-height: 100%;
--desktop-detail-nav-font-weight: 400;
--desktop-detail-nav-font-style: normal;
--desktop-detail-footer-font-family: TayBirdie-Regular,sans-serif;
--desktop-detail-footer-line-height: 100%;
--desktop-detail-footer-font-weight: 400;
--desktop-detail-footer-font-style: normal;
--desktop-detail-large-font-family: TayBirdie-Regular,sans-serif;
--desktop-detail-large-line-height: 110%;
--desktop-detail-large-font-weight: 400;
--desktop-detail-large-font-style: normal;
--desktop-detail-medium-font-family: TayBirdie-Regular,sans-serif;
--desktop-detail-medium-line-height: 150%;
--desktop-detail-medium-font-weight: 400;
--desktop-detail-medium-font-style: normal;
--desktop-detail-small-font-family: TayBirdie-Regular,sans-serif;
--desktop-detail-small-line-height: 100%;
--desktop-detail-small-font-weight: 400;
--desktop-detail-small-font-style: normal;
--desktop-body-large-font-family: AnonymousPro-Regular,sans-serif;
--desktop-body-large-line-height: 150%;
--desktop-body-large-font-weight: 400;
--desktop-body-large-font-style: normal;
--desktop-body-medium-font-family: AnonymousPro-Regular,sans-serif;
--desktop-body-medium-line-height: 161%;
--desktop-body-medium-font-weight: 400;
--desktop-body-medium-font-style: normal;
--desktop-body-small-font-family: AnonymousPro-Regular,sans-serif;
--desktop-body-small-line-height: 130%;
--desktop-body-small-font-weight: 400;
--desktop-body-small-font-style: normal;
--mobile-display-1-font-family: TayMakawao-Regular,sans-serif;
--mobile-display-1-line-height: 80%;
--mobile-display-1-font-weight: 400;
--mobile-display-1-font-style: normal;
--mobile-h1-font-family: TayMakawao-Regular,sans-serif;
--mobile-h1-line-height: 80%;
--mobile-h1-font-weight: 400;
--mobile-h1-font-style: normal;
--mobile-h2-font-family: TayMakawao-Regular,sans-serif;
--mobile-h2-line-height: 81%;
--mobile-h2-font-weight: 400;
--mobile-h2-font-style: normal;
--mobile-h3-font-family: TayMakawao-Regular,sans-serif;
--mobile-h3-line-height: 90%;
--mobile-h3-font-weight: 400;
--mobile-h3-font-style: normal;
--mobile-h4-font-family: TayMakawao-Regular,sans-serif;
--mobile-h4-line-height: 95%;
--mobile-h4-font-weight: 400;
--mobile-h4-font-style: normal;
--mobile-h5-font-family: TayMakawao-Regular,sans-serif;
--mobile-h5-line-height: 100%;
--mobile-h5-font-weight: 400;
--mobile-h5-font-style: normal;
--mobile-h6-font-family: TayMakawao-Regular,sans-serif;
--mobile-h6-line-height: 100%;
--mobile-h6-font-weight: 400;
--mobile-h6-font-style: normal;
--mobile-h7-font-family: TayMakawao-Regular,sans-serif;
--mobile-h7-line-height: 100%;
--mobile-h7-font-weight: 400;
--mobile-h7-font-style: normal;
--mobile-h8-font-family: TayMakawao-Regular,sans-serif;
--mobile-h8-line-height: 100%;
--mobile-h8-font-weight: 400;
--mobile-h8-font-style: normal;
--mobile-body-large-font-family: AnonymousPro-Regular,sans-serif;
--mobile-body-large-line-height: 150%;
--mobile-body-large-font-weight: 400;
--mobile-body-large-font-style: normal;
--mobile-body-medium-font-family: AnonymousPro-Regular,sans-serif;
--mobile-body-medium-line-height: 160%;
--mobile-body-medium-font-weight: 400;
--mobile-body-medium-font-style: normal;
--mobile-body-small-font-family: AnonymousPro-Regular,sans-serif;
--mobile-body-small-line-height: 130%;
--mobile-body-small-font-weight: 400;
--mobile-body-small-font-style: normal;
--mobile-detail-nav-font-family: TayMakawao-Regular,sans-serif;
--mobile-detail-nav-line-height: 81%;
--mobile-detail-nav-font-weight: 400;
--mobile-detail-nav-font-style: normal;
--mobile-detail-footer-font-family: TayBirdie-Regular,sans-serif;
--mobile-detail-footer-line-height: 100%;
--mobile-detail-footer-font-weight: 400;
--mobile-detail-footer-font-style: normal;
--mobile-detail-large-font-family: TayBirdie-Regular,sans-serif;
--mobile-detail-large-line-height: 100%;
--mobile-detail-large-font-weight: 400;
--mobile-detail-large-font-style: normal;
--mobile-detail-medium-font-family: TayBirdie-Regular,sans-serif;
--mobile-detail-medium-line-height: 100%;
--mobile-detail-medium-font-weight: 400;
--mobile-detail-medium-font-style: normal;
--mobile-detail-small-font-family: TayBirdie-Regular,sans-serif;
--mobile-detail-small-line-height: 100%;
--mobile-detail-small-font-weight: 400;
--mobile-detail-small-font-style: normal;
--mobile-cta-medium-font-family: TayBirdie-Regular,sans-serif;
--mobile-cta-medium-line-height: 80%;
--mobile-cta-medium-font-weight: 400;
--mobile-cta-medium-font-style: normal;
--mobile-cta-small-font-family: TayBirdie-Regular,sans-serif;
--mobile-cta-small-line-height: 80%;
--mobile-cta-small-font-weight: 400;
--mobile-cta-small-font-style: normal;
--labels-circle-label-text: #3b2722;
--product-grid-product-text: #3b2722;
```

### Other

```css
--background: #F2EBD0;
--buttons-stroke-width: 2px;
--mobile-breakpoint: 700;
--medium-breakpoint: 960;
--medium-plus-breakpoint: 1024;
--large-breakpoint: 1280;
--ease-out-quad: cubic-bezier(0.25,0.46,0.45,0.94);
--ease-out-cubic: cubic-bezier(0.215,0.61,0.355,1);
--ease-in-cubic: cubic-bezier(0.55,0.055,0.675,0.19);
--ease-in-out-cubic: cubic-bezier(0.645,0.045,0.355,1);
--ease-in-out-quart: cubic-bezier(0.77,0,0.175,1);
--ease-in-out-quint: cubic-bezier(0.86,0,0.07,1);
--ease-out-expo: cubic-bezier(0.19,1,0.22,1);
--ease-in-expo: cubic-bezier(0.95,0.05,0.795,0.035);
--ease-in-out-expo: cubic-bezier(1,0,0,1);
--buttons-circle-button-stroke: #f2ebd0;
--_number-flow-d-opacity: 0;
--product-grid-product-background: #f2ebd0;
--_number-flow-d: 0;
--page-wrap-body-page: #3b2722;
--_number-flow-dx: 0px;
--_number-flow-d-width: 0;
```

### Dependencies

```css
--site-margin-x: --spacing-20;
--site-margin-y: --spacing-20;
--loader-bar-color: --color-pale-cream;
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
| sm | 699px | max-width |
| sm | 700px | min-width |
| 959px | 959px | max-width |
| lg | 960px | min-width |
| xl | 1279px | max-width |
| xl | 1280px | max-width |
| 1410px | 1410px | min-width |
| 1440px | 1440px | min-width |
| 1920px | 1920px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.2s`, `1s`, `0.7s`, `0.5s`, `0.4s`

### Common Transitions

```css
transition: all;
transition: opacity 0.3s ease-out, display 0.3s ease-out allow-discrete, overlay 0.3s ease-out allow-discrete;
transition: opacity 0.3s ease-out, transform 0.3s ease-out;
transition: transform 0.3s ease-in-out;
transition: transform 0.2s ease-in-out, opacity 0.2s ease-in-out;
transition: background-color 0.3s cubic-bezier(0.215, 0.61, 0.355, 1), color 0.3s cubic-bezier(0.215, 0.61, 0.355, 1), border-bottom 0.3s cubic-bezier(0.215, 0.61, 0.355, 1), transform 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
transition: transform 1s cubic-bezier(0.215, 0.61, 0.355, 1);
transition: transform 0.7s cubic-bezier(0.215, 0.61, 0.355, 1);
transition: transform 0.5s cubic-bezier(0.215, 0.61, 0.355, 1);
transition: transform 0.3s cubic-bezier(0.215, 0.61, 0.355, 1);
```

### Keyframe Animations

**BeeBeesponsible_wingLeftFlap__mbYnK**
```css
@keyframes BeeBeesponsible_wingLeftFlap__mbYnK {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(45deg); }
}
```

**BeeBeesponsible_wingRightFlap__3JULu**
```css
@keyframes BeeBeesponsible_wingRightFlap__3JULu {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(-45deg); }
}
```

**Emblem_rotate__mHRL_**
```css
@keyframes Emblem_rotate__mHRL_ {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

**Bee_leftWingFlap__3xFZj**
```css
@keyframes Bee_leftWingFlap__3xFZj {
  0% { transform: rotate(10deg) skewY(10deg); }
  100% { transform: rotate(-15deg) skewY(-25deg); }
}
```

**Bee_rightWingFlap__lNjlz**
```css
@keyframes Bee_rightWingFlap__lNjlz {
  0% { transform: rotate(10deg) skewY(10deg); }
  100% { transform: rotate(-15deg) skewY(-25deg); }
}
```

**LoaderLogo_rotateBee__ZLDQG**
```css
@keyframes LoaderLogo_rotateBee__ZLDQG {
  0% { transform: scale(0.32) rotate(0deg); }
  50% { transform: scale(0.32) rotate(-1turn); }
  100% { transform: scale(0.32) rotate(0deg); }
}
```

**LoaderLogo_slideGradient__q3gqu**
```css
@keyframes LoaderLogo_slideGradient__q3gqu {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}
```

**Modal_fadeIn__m04fn**
```css
@keyframes Modal_fadeIn__m04fn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**Modal_slideIn__IX9ol**
```css
@keyframes Modal_slideIn__IX9ol {
  0% { opacity: 0; transform: translateX(20px); }
  100% { opacity: 1; transform: translateX(0px); }
}
```

**CookieBanner_slideInUp__Vx76_**
```css
@keyframes CookieBanner_slideInUp__Vx76_ {
  0% { opacity: 0; transform: translateY(40px); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (20 instances)

```css
.button {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
  padding-top: 24px;
  padding-right: 24px;
  border-radius: 500px;
}
```

### Cards (25 instances)

```css
.card {
  background-color: rgba(255, 255, 255, 0);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (32 instances)

```css
.link {
  color: rgb(59, 39, 34);
  font-size: 12.6667px;
  font-weight: 400;
}
```

### Navigation (23 instances)

```css
.navigatio {
  color: rgb(242, 235, 208);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (26 instances)

```css
.foote {
  background-color: rgb(255, 202, 80);
  color: rgb(59, 39, 34);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12.6667px;
}
```

### Modals (7 instances)

```css
.modal {
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (1 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(59, 39, 34);
  padding-top: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 5 instances, 4 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 500px;
  border: 0px none rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(59, 39, 34);
  color: rgb(242, 235, 208);
  padding: 16px 28px 16px 28px;
  border-radius: 500px;
  border: 2px solid rgb(59, 39, 34);
  font-size: 13.3333px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(59, 39, 34);
  padding: 16px 28px 16px 28px;
  border-radius: 500px;
  border: 2px solid rgb(59, 39, 34);
  font-size: 13.3333px;
  font-weight: 400;
```

**Variant 4** (2 instances)

```css
  background: rgb(255, 202, 80);
  color: rgb(59, 39, 34);
  padding: 24px 24px 24px 24px;
  border-radius: 500px;
  border: 2px solid rgb(242, 235, 208);
  font-size: 13.3333px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(59, 39, 34);
  padding: 0px 60px 0px 60px;
  border-radius: 0px;
  border: 0px none rgb(59, 39, 34);
  font-size: 16px;
  font-weight: 400;
```

### Button — 3 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgb(59, 39, 34);
  color: rgb(242, 235, 208);
  padding: 24px 24px 24px 24px;
  border-radius: 500px;
  border: 2px solid rgb(59, 39, 34);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(255, 202, 80);
  color: rgb(160, 52, 42);
  padding: 24px 24px 24px 24px;
  border-radius: 500px;
  border: 2px solid rgb(255, 202, 80);
  font-size: 16px;
  font-weight: 400;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(59, 39, 34);
  padding: 24px 40px 24px 40px;
  border-radius: 1000px;
  border: 2px solid rgb(59, 39, 34);
  font-size: 13.3333px;
  font-weight: 400;
```

### Button — 5 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(59, 39, 34);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 1px solid rgb(59, 39, 34);
  font-size: 13.3333px;
  font-weight: 400;
```

**Variant 2** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 1px solid rgb(59, 39, 34);
  font-size: 13.3333px;
  font-weight: 400;
```

## Layout System

**6 grid containers** and **167 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1000px | 0px |
| 1280px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 3x |
| 1-column | 2x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 1265px;
grid-template-columns: 632.5px 632.5px;
grid-template-columns: 256.25px 256.25px 256.25px 256.25px;
gap: 48px;
grid-template-columns: 592.625px 624.375px;
gap: 12px 0px;
grid-template-columns: 616.5px 616.5px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 29x |
| row/nowrap | 137x |
| row/wrap | 1x |

**Gap values:** `12px`, `12px 0px`, `16px`, `20px`, `28px`, `40px`, `48px`, `52px`, `8px`, `8px 16px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 84/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 6 font families — consider limiting to 2 (heading + body)
- 54 !important rules — prefer specificity over overrides
- 86% of CSS is unused — consider purging
- 5326 duplicate CSS declarations

## Z-Index Map

**16 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,999999 | div.L.o.a.d.e.r._.s.s.r.B.a.c.k.g.r.o.u.n.d._._._.7.l._.a, div.C.i.r.c.l.e.T.r.a.n.s.i.t.i.o.n._.w.r.a.p.p.e.r._._.y.9.o.p.n. .C.i.r.c.l.e.T.r.a.n.s.i.t.i.o.n._.f.u.l.l.V.i.e.w.p.o.r.t._._.T.O._.Q.U. .u.n.d.e.f.i.n.e.d. .C.i.r.c.l.e.T.r.a.n.s.i.t.i.o.n._.f.i.x.e.d._._.x.b.v.D.x, div.C.o.o.k.i.e.B.a.n.n.e.r._.c.o.o.k.i.e.B.a.n.n.e.r._._.f.S.i.G.e. .C.o.o.k.i.e.B.a.n.n.e.r._.v.i.s.i.b.l.e._._.D.J.R.z.A. .C.o.o.k.i.e.B.a.n.n.e.r._.a.n.i.m.a.t.i.n.g._._.a.a.L.c.E. .C.o.o.k.i.e.B.a.n.n.e.r._.y.e.l.l.o.w.T.h.e.m.e._._._.e.j.z.N |
| dropdown | 100,999 | span.B.u.t.t.o.n._.c.o.n.t.e.n.t._._.T.L.r.8.d, span.B.u.t.t.o.n._.c.o.n.t.e.n.t._._.T.L.r.8.d, span.B.u.t.t.o.n._.c.o.n.t.e.n.t._._.T.L.r.8.d |
| sticky | 10,10 | div.M.o.d.a.l._.c.l.o.s.e.B.u.t.t.o.n.C.o.n.t.a.i.n.e.r._._.1.x.D.k.M, div.M.o.u.s.e.T.r.a.i.l._.c.o.n.t.a.i.n.e.r._._._.0.Y.D.B, div.e.m.b.l.e.m. .E.m.b.l.e.m._.c.o.n.t.a.i.n.e.r._._.w.0.C.j.q. .E.m.b.l.e.m._.e.m.b.l.e.m._._.E.S.g.j.l |
| base | -3,9 | div.L.i.n.k.L.i.n.e._.l.i.n.e._._.U.t.G.S.v. .L.i.n.k.L.i.n.e._.l.i.n.e.4._._.1.Y.3.W.E, div.L.i.n.k.L.i.n.e._.l.i.n.e._._.U.t.G.S.v. .L.i.n.k.L.i.n.e._.l.i.n.e.4._._.1.Y.3.W.E, div.L.i.n.k.L.i.n.e._.l.i.n.e._._.U.t.G.S.v. .L.i.n.k.L.i.n.e._.l.i.n.e.4._._.1.Y.3.W.E |

**Issues:**
- [object Object]

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| TayBirdie-Regular | self-hosted | 400 | normal |
| TayMakawao-Regular | self-hosted | 400 | normal |
| AnonymousPro-Bold | self-hosted | 400 | normal |
| AnonymousPro-Regular | self-hosted | 400 | normal |
| barkmanhoney | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 34 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 6 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 4:3 (21x), 1:1 (12x), 3:4 (8x), 3.51:1 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **ease-in-out** (19 uses) — `ease`
- **ease-out** (91 uses) — `cubic-bezier(0.215, 0.61, 0.355, 1)`, `cubic-bezier(0.25, 0.46, 0.45, 0.94)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `Bee_leftWingFlap__3xFZj` | rotate | transform | 11 |
| `Bee_rightWingFlap__lNjlz` | rotate | transform | 11 |
| `CookieBanner_slideInUp__Vx76_` | slide-y | opacity, transform | 1 |

## Component Anatomy

### button — 19 instances

**Slots:** label

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Title Case (tight)

### Top CTA Verbs

- **learn** (6)
- **confirm** (2)
- **opt** (1)
- **get** (1)
- **find** (1)

### Button Copy Patterns

- "learn more" (6×)
- "confirm
opt me out" (1×)
- "confirm" (1×)
- "opt me out" (1×)
- "get started" (1×)
- "find store" (1×)

### Sample Headings

> Busy Bee Honey

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Shop Busy Bee Raw Honey — Pure, raw honey you can fully trace from flower to hive to bottle.

Alternates: legal (0.4)

## Section Roles

Reading order (top→bottom): nav → footer → nav → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | footer | Busy Bee Honey | 0.95 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.405 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 1000px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 42, svg 0, icon 15, screenshot-like 0, photo-like 0
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Times New Roman` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
