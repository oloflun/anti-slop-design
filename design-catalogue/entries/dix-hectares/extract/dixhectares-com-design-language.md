# Design Language: Dix Hectares

> Extracted from `https://dixhectares.com/en` on September 4, 2026
> 1375 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#a85435` | rgb(168, 84, 53) | hsl(16, 52%, 43%) | 1109 |
| Secondary | `#555114` | rgb(85, 81, 20) | hsl(56, 62%, 21%) | 3 |
| Accent | `#efe5d7` | rgb(239, 229, 215) | hsl(35, 43%, 89%) | 50 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 1272 |
| `#000000` | hsl(0, 0%, 0%) | 203 |
| `#ffffff` | hsl(0, 0%, 100%) | 174 |
| `#6b7280` | hsl(220, 9%, 46%) | 3 |

### Background Colors

Used on large-area elements: `#efe5d7`, `#000000`, `#ffffff`, `#b8705e`, `#555114`

### Text Colors

Text color palette: `#000000`, `#a85435`, `#a75335`, `#efe5d7`, `#ffffff`, `#9c4c2e`

### Gradients

```css
background-image: linear-gradient(rgb(168, 84, 53), rgb(168, 84, 53));
```

```css
background-image: linear-gradient(0deg, rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 1272 |
| `#a85435` | text, border, background | 1109 |
| `#000000` | text, background | 203 |
| `#ffffff` | text, background | 174 |
| `#efe5d7` | background, text, border | 50 |
| `#9c4c2e` | text | 4 |
| `#6b7280` | border, background | 3 |
| `#b8705e` | background | 3 |
| `#555114` | background | 3 |

## Typography

### Font Families

- **Sackers Gothic Std Heavy** — used for all (136 elements)
- **EngraversMTPro** — used for all (79 elements)
- **Francesco-Regular** — used for all (77 elements)
- **Ceraph-Italic** — used for all (52 elements)
- **GTStandard-M** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 46px | 2.875rem | 400 | 54px | normal | h2, br |
| 40px | 2.5rem | 400 | 18px | -3.6px | div |
| 28px | 1.75rem | 400 | 32px | normal | c-text, div |
| 22px | 1.375rem | 400 | 24px | normal | a, span |
| 20px | 1.25rem | 400 | 23px | normal | p, h3, div, bodytext-animate |
| 16px | 1rem | 400 | 18.4px | normal | html, head, style, meta |
| 14px | 0.875rem | 400 | 20px | normal | div, p, a, button |
| 12px | 0.75rem | 400 | 16px | 2.64px | button, span, p, label |
| 11px | 0.6875rem | 400 | 16px | normal | button, p, span, a |
| 10px | 0.625rem | 700 | 16px | 1.2px | h2, button, h4, div |

### Heading Scale

```css
h2 { font-size: 46px; font-weight: 400; line-height: 54px; }
h3 { font-size: 20px; font-weight: 400; line-height: 23px; }
h3 { font-size: 16px; font-weight: 400; line-height: 18.4px; }
h1 { font-size: 14px; font-weight: 400; line-height: 20px; }
h4 { font-size: 11px; font-weight: 400; line-height: 16px; }
h2 { font-size: 10px; font-weight: 700; line-height: 16px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: 18.4px; }
```

### Font Weights in Use

`400` (1368x), `700` (1x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-56 | 56px | 3.5rem |
| spacing-72 | 72px | 4.5rem |
| spacing-80 | 80px | 5rem |
| spacing-105 | 105px | 6.5625rem |
| spacing-111 | 111px | 6.9375rem |
| spacing-120 | 120px | 7.5rem |
| spacing-144 | 144px | 9rem |
| spacing-152 | 152px | 9.5rem |
| spacing-177 | 177px | 11.0625rem |
| spacing-324 | 324px | 20.25rem |
| spacing-360 | 360px | 22.5rem |
| spacing-399 | 399px | 24.9375rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 1 |
| full | 50px | 19 |
| full | 9999px | 2 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px;
```

**md** — blur: 10px
```css
box-shadow: rgba(63, 63, 68, 0.4) 0px 4px 10px 0px;
```

## CSS Custom Properties

### Colors

```css
--oke-reviewsTab-backgroundColor: #676986;
--oke-reviewsTab-textColor: #FFFFFF;
--font-color: var(--black);
--oke-button-backgroundColor: #A85435;
--oke-button-backgroundColorHover: #944a2f;
--oke-button-backgroundColorActive: #A85435;
--oke-button-textColor: #FFFFFF;
--oke-button-textColorHover: #454545;
--oke-button-textColorActive: #FFFFFF;
--oke-button-borderColor: #DBDDE4;
--oke-button-borderColorHover: #DBDDE4;
--oke-button-borderColorActive: #A85435;
--oke-button-borderRadius: 4px;
--oke-button-borderWidth: 1px;
--oke-border-color: #A85435;
--oke-border-width: 1px;
--oke-text-primaryColor: #A85435;
--oke-text-secondaryColor: #9C4C2E;
--oke-avatar-backgroundColor: #E5E5EB;
--oke-avatar-placeholderTextColor: #A85435;
--oke-highlightColor: #A85435;
--oke-shadingColor: #F7F7F8;
--oke-attributeBar-shadingColor: #A85435;
--oke-attributeBar-borderColor: #A85435;
--oke-attributeBar-backgroundColor: #D6B3A4;
--oke-attributeBar-markerColor: #00CAAA;
--oke-filter-backgroundColor: #FFFFFF;
--oke-filter-backgroundColorActive: #878787;
--oke-filter-borderColor: #DBDDE4;
--oke-filter-borderColorActive: #878787;
--oke-filter-textColor: #A85435;
--oke-filter-textColorActive: #FFFFFF;
--oke-filter-borderRadius: 100px;
--oke-filter-searchHighlightColor: #dcbbae;
--oke-mediaGrid-chevronColor: #676986;
--oke-stars-foregroundColor: #A85435;
--oke-stars-backgroundColor: #C48E76;
--oke-stars-borderWidth: 0;
--swiper-theme-color: #007aff;
--tw-ring-shadow: 0 0 #0000;
--tw-border-spacing-x: 0;
--tw-ring-color: rgba(59,130,246,.5);
--tw-ring-offset-color: #fff;
--tw-ring-offset-width: 0px;
--tw-shadow-colored: 0 0 #0000;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-border-spacing-y: 0;
```

### Spacing

```css
--font-size: 16px;
--font-size-h0: 24vw;
--font-size-h1: 8vw;
--font-size-h2: 4vw;
--font-size-h3: 20px;
--font-size-h4: 18px;
--font-size-h5: 16px;
--padding: var(--unit);
--base-column-gap: var(--unit-small);
--oke-widget-spaceAbove: 18px;
--oke-widget-spaceBelow: 18px;
--oke-starRating-spaceAbove: 0px;
--oke-starRating-spaceBelow: 0px;
--oke-button-fontSize: var(--oke-text-regular, 14px);
--oke-avatar-size: 48px;
--oke-productImageSize: 48px;
--swiper-navigation-size: 44px;
--tw-numeric-spacing: ;
--tw-contain-size: ;
```

### Typography

```css
--line-height: 1;
--font-ceraph: "Ceraph-Italic";
--line-height-h: var(--line-height);
--oke-button-fontWeight: 700;
--oke-button-fontFamily: inherit;
--oke-text-small: 12px;
--oke-text-regular: 14px;
--oke-text-large: 20px;
--oke-text-fontFamily: inherit;
```

### Shadows

```css
--tw-drop-shadow: ;
--tw-shadow: 0 0 #0000;
```

### Other

```css
--black: #222;
--light: 300;
--normal: 400;
--medium: 500;
--bold: 700;
--speed: .3s;
--speed-slow: .6s;
--easing: var(--power2-out);
--unit: 60px;
--unit-small: 30px;
--base-column-nb: 12;
--power1-in: cubic-bezier(.55,.085,.68,.53);
--power1-out: cubic-bezier(.25,.46,.45,.94);
--power1-in-out: cubic-bezier(.455,.03,.515,.955);
--power2-in: cubic-bezier(.55,.055,.675,.19);
--power2-out: cubic-bezier(.215,.61,.355,1);
--power2-in-out: cubic-bezier(.645,.045,.355,1);
--power3-in: cubic-bezier(.895,.03,.685,.22);
--power3-out: cubic-bezier(.165,.84,.44,1);
--power3-in-out: cubic-bezier(.77,0,.175,1);
--power4-in: cubic-bezier(.755,.05,.855,.06);
--power4-out: cubic-bezier(.23,1,.32,1);
--power4-in-out: cubic-bezier(.86,0,.07,1);
--expo-in: cubic-bezier(.95,.05,.795,.035);
--expo-out: cubic-bezier(.19,1,.22,1);
--expo-in-out: cubic-bezier(1,0,0,1);
--back-in: cubic-bezier(.6,-.28,.735,.045);
--back-out: cubic-bezier(.175,00.885,.32,1.275);
--back-in-out: cubic-bezier(.68,-.55,.265,1.55);
--sine-in: cubic-bezier(.47,0,.745,.715);
--sine-out: cubic-bezier(.39,.575,.565,1);
--sine-in-out: cubic-bezier(.445,.05,.55,.95);
--circ-in: cubic-bezier(.6,.04,.98,.335);
--circ-out: cubic-bezier(.075,.82,.165,1);
--circ-in-out: cubic-bezier(.785,.135,.15,.86);
--bounce: cubic-bezier(.17,.67,.3,1.33);
--slow-out: cubic-bezier(.04,1.15,.4,.99);
--smooth: cubic-bezier(.38,.005,.215,1);
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-ordinal: ;
--tw-contain-style: ;
--tw-backdrop-invert: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--scrollValue: 0px;
--tw-pan-y: ;
--tw-rotate: 0;
--top-header-height: 28px;
--tw-gradient-via-position: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-numeric-fraction: ;
--tw-skew-y: 0;
--tw-slashed-zero: ;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-pinch-zoom: ;
--tw-contain-paint: ;
--tw-backdrop-saturate: ;
--cart-footer-height: 204px;
--tw-brightness: ;
--app-height-negative: -800px;
--tw-scale-y: 1;
--tw-backdrop-contrast: ;
--tw-backdrop-brightness: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-contrast: ;
--tw-skew-x: 0;
--tw-backdrop-blur: ;
--tw-translate-x: 0;
--app-availheight: 800px;
--tw-scale-x: 1;
--scrollbar: 0px;
--tw-blur: ;
--absRatio: 1.6;
--app-height: 800px;
--tw-invert: ;
--tw-numeric-figure: ;
--tw-contain-layout: ;
```

### Dependencies

```css
--font-color: --black;
--line-height-h: --line-height;
--easing: --power2-out;
--padding: --unit;
--base-column-gap: --unit-small;
--oke-button-fontSize: --oke-text-regular;
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
| sm | 480px | max-width |
| sm | 600px | max-width |
| sm | 640px | min-width |
| md | 749px | max-width |
| md | 750px | min-width |
| md | 768px | min-width |
| lg | 1023px | max-width |
| lg | 1024px | min-width |
| 1400px | 1400px | min-width |
| 1680px | 1680px | min-width |
| 1900px | 1900px | min-width |
| 2600px | 2600px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.7s`, `0.15s`, `0.8s`, `0.5s`, `1s`, `0.875s`, `0.4s`, `0.95s`, `1.025s`, `0.9s`, `1.05s`, `0.1s`

### Common Transitions

```css
transition: all;
transition: color 0.3s cubic-bezier(0.33, 1, 0.68, 1), background-color 0.3s cubic-bezier(0.33, 1, 0.68, 1), border-color 0.3s cubic-bezier(0.33, 1, 0.68, 1), text-decoration-color 0.3s cubic-bezier(0.33, 1, 0.68, 1), fill 0.3s cubic-bezier(0.33, 1, 0.68, 1), stroke 0.3s cubic-bezier(0.33, 1, 0.68, 1);
transition: 0.7s cubic-bezier(0.65, 0, 0.35, 1);
transition: color 0.3s cubic-bezier(0.25, 1, 0.5, 1), background-color 0.3s cubic-bezier(0.25, 1, 0.5, 1), border-color 0.3s cubic-bezier(0.25, 1, 0.5, 1), text-decoration-color 0.3s cubic-bezier(0.25, 1, 0.5, 1), fill 0.3s cubic-bezier(0.25, 1, 0.5, 1), stroke 0.3s cubic-bezier(0.25, 1, 0.5, 1);
transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.3s cubic-bezier(0.215, 0.61, 0.355, 1);
transition: transform 0.8s, -webkit-transform 0.8s;
transition: opacity 0.8s;
transition: opacity 0.3s;
transition: transform 0.5s cubic-bezier(0.645, 0.045, 0.355, 1), -webkit-transform 0.5s cubic-bezier(0.645, 0.045, 0.355, 1);
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

**oke-spin**
```css
@keyframes oke-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

**oke-fade-in**
```css
@keyframes oke-fade-in {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**swiper-preloader-spin**
```css
@keyframes swiper-preloader-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

**swiper-preloader-spin**
```css
@keyframes swiper-preloader-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (33 instances)

```css
.button {
  background-color: rgb(168, 84, 53);
  color: rgb(168, 84, 53);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Inputs (16 instances)

```css
.input {
  background-color: rgb(239, 229, 215);
  color: rgb(168, 84, 53);
  border-color: rgb(229, 231, 235);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (57 instances)

```css
.link {
  color: rgb(168, 84, 53);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (22 instances)

```css
.navigatio {
  color: rgb(168, 84, 53);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (4 instances)

```css
.foote {
  background-color: rgb(239, 229, 215);
  color: rgb(168, 84, 53);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (4 instances)

```css
.modal {
  background-color: rgb(239, 229, 215);
  border-radius: 0px;
  box-shadow: rgba(63, 63, 68, 0.4) 0px 4px 10px 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 650px;
}
```

### ProgressBars (1 instances)

```css
.progressBar {
  color: rgb(255, 255, 255);
  border-radius: 0px;
  font-size: 16px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(167, 83, 53);
  padding: 8px 25px 8px 25px;
  border-radius: 2px;
  border: 0px none rgb(167, 83, 53);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(168, 84, 53);
  color: rgb(255, 255, 255);
  padding: 13px 56px 10px 56px;
  border-radius: 0px;
  border: 1px solid rgb(168, 84, 53);
  font-size: 12px;
  font-weight: 400;
```

### Button — 9 instances, 3 variants

**Variant 1** (4 instances)

```css
  background: rgb(167, 83, 53);
  color: rgb(239, 229, 215);
  padding: 12px 25px 10px 25px;
  border-radius: 0px;
  border: 0px solid rgb(239, 229, 215);
  font-size: 10px;
  font-weight: 400;
```

**Variant 2** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(168, 84, 53);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 10px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(168, 84, 53);
  padding: 12px 0px 10px 0px;
  border-radius: 0px;
  border: 1px solid rgb(168, 84, 53);
  font-size: 11px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(168, 84, 53);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

### Input — 4 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(168, 84, 53);
  padding: 8px 12px 8px 0px;
  border-radius: 0px;
  border: 0px none rgb(107, 114, 128);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(239, 229, 215);
  color: rgb(0, 0, 0);
  padding: 16px 16px 16px 16px;
  border-radius: 0px;
  border: 1px solid rgb(168, 84, 53);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(168, 84, 53);
  color: rgb(255, 255, 255);
  padding: 13px 0px 10px 0px;
  border-radius: 0px;
  border: 1px solid rgb(168, 84, 53);
  font-size: 11px;
  font-weight: 400;
```

### Button — 3 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(168, 84, 53);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **76 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 650px | 24px |
| 600px | 0px |
| 100% | 0px |
| 500px | 0px |
| 448px | 48px |
| 384px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 1x |

### Grid Templates

```css
grid-template-columns: 78.6562px 78.6562px 78.6562px 78.6562px 78.6562px 78.6562px 78.6562px 78.6562px 78.6562px 78.6562px 78.6562px 78.6562px;
gap: 24px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 31x |
| row/nowrap | 45x |

**Gap values:** `14px`, `20px`, `24px`, `72px`, `8px`, `normal 10px`, `normal 13px`, `normal 8px`

## Accessibility (WCAG 2.1)

**Overall Score: 60%** — 3 passing, 2 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#efe5d7` | `#a75335` | 4.29:1 | FAIL | button (2x) |

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#a85435` | 5.27:1 | AA |
| `#a85435` | `#ffffff` | 5.27:1 | AA |

## Design System Score

**Overall: 77/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 60/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Good CSS variable tokenization

**Issues:**
- 5 font families — consider limiting to 2 (heading + body)
- 2 WCAG contrast failures
- 551 !important rules — prefer specificity over overrides
- 80% of CSS is unused — consider purging
- 5800 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | 0deg | 2 | brand |

```css
background: linear-gradient(rgb(168, 84, 53), rgb(168, 84, 53));
background: linear-gradient(0deg, rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3));
```

## Z-Index Map

**18 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9998,9999999 | overlay-panel, panel-engraving.p.a.n.e.l.-.e.n.g.r.a.v.i.n.g.-.a.c.t.i.v.e.:.t.w.-.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.a.u.t.o. .p.a.n.e.l.-.e.n.g.r.a.v.i.n.g.-.a.c.t.i.v.e.:.t.w.-.t.r.a.n.s.l.a.t.e.-.y.-.0. .p.a.n.e.l.-.e.n.g.r.a.v.i.n.g.-.a.c.t.i.v.e.:.l.g.:.t.w.-.t.r.a.n.s.l.a.t.e.-.x.-.0, section.s.h.o.p.i.f.y.-.p.c._._.b.a.n.n.e.r._._.d.i.a.l.o.g |
| dropdown | 999,999 | reveal-fade-out.t.w.-.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .t.w.-.f.i.x.e.d. .t.w.-.i.n.s.e.t.-.0. .t.w.-.z.-.[.9.9.9.]. .t.w.-.b.g.-.b.e.i.g.e._.1.0.0. .i.s.-.a.n.i.m.a.t.e.d |
| sticky | 10,90 | div.t.w.-.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .t.w.-.a.b.s.o.l.u.t.e. .t.w.-.i.n.s.e.t.-.x.-.1. .t.w.-.b.o.t.t.o.m.-.1. .t.w.-.t.o.p.-.4. .t.w.-.z.-.1.0. .t.w.-.b.o.r.d.e.r. .t.w.-.b.o.r.d.e.r.-.b.r.o.w.n._.1.0.0, p, div.s.w.i.p.e.r.-.p.a.g.i.n.a.t.i.o.n |
| base | 0,5 | c-background.u.-.d.e.s.k.t.o.p. .t.w.-.a.b.s.o.l.u.t.e. .t.w.-.i.n.s.e.t.-.y.-.0. .t.w.-.r.i.g.h.t.-.0. .t.w.-.h.-.f.u.l.l. .t.w.-.w.-.[.4.0.%.]. .t.w.-.b.g.-.b.e.i.g.e._.1.0.0, slideshow-fills.u.-.d.e.s.k.t.o.p. .t.w.-.a.b.s.o.l.u.t.e. .t.w.-.i.n.s.e.t.-.0. .t.w.-.z.-.0. .t.w.-.h.-.h.v.i.e.w. .t.w.-.w.-.f.u.l.l, slideshow-visual.t.w.-.a.b.s.o.l.u.t.e. .t.w.-.i.n.s.e.t.-.0. .t.w.-.b.l.o.c.k. .t.w.-.h.-.f.u.l.l. .t.w.-.w.-.f.u.l.l. .t.w.-.o.v.e.r.f.l.o.w.-.h.i.d.d.e.n |

**Issues:**
- [object Object]

## SVG Icons

**6 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 2 |
| md | 1 |
| lg | 3 |

**Icon colors:** `white`, `#A85435`, `#9C5431`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Carta Nueva Small | self-hosted | 400 | normal |
| Francesco-Regular | self-hosted | 400 | normal |
| Francesco-Italic | self-hosted | 400 | normal |
| Sackers Gothic Std Light | self-hosted | 400 | normal |
| Sackers Gothic Std Heavy | self-hosted | 400 | normal |
| EngraversMTPro | self-hosted | 400 | normal |
| LTC Caslon Pro Regular | self-hosted | 400 | normal |
| Ceraph-Italic | self-hosted | 400 | normal |
| oke-widget-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 26 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 21 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 6 | objectFit: cover, borderRadius: 0px, shape: square |
| avatar | 2 | objectFit: cover, borderRadius: 9999px, shape: circular |

**Aspect ratios:** 1:1 (23x), 3:4 (16x), 21:9 (10x), 2:3 (3x), 3:2 (2x), 16:9 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `800ms` | 800 |

### Easing Families

- **ease-out** (81 uses) — `cubic-bezier(0.33, 1, 0.68, 1)`, `cubic-bezier(0.25, 1, 0.5, 1)`, `cubic-bezier(0.215, 0.61, 0.355, 1)`
- **custom** (43 uses) — `cubic-bezier(0.65, 0, 0.35, 1)`, `cubic-bezier(0.4, 0, 0.2, 1)`, `cubic-bezier(0.645, 0.045, 0.355, 1)`
- **ease-in-out** (2 uses) — `ease`

## Component Anatomy

### button — 19 instances

**Slots:** label
**Variants:** outline
**Sizes:** lg

| variant | count | sample label |
|---|---|---|
| default | 18 | Manage preferences |
| outline | 1 | SUBSCRIBE |

### input — 4 instances

**Variants:** outline
**Sizes:** lg

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (verbose)

### Top CTA Verbs

- **subscribe** (2)
- **manage** (1)
- **accept** (1)
- **decline** (1)
- **continue** (1)
- **appliquer** (1)
- **check** (1)
- **fr** (1)

### Button Copy Patterns

- "subscribe" (2×)
- "manage preferences" (1×)
- "accept" (1×)
- "decline" (1×)
- "continue shopping" (1×)
- "appliquer" (1×)
- "check out — 0 €" (1×)
- "fr" (1×)
- "en" (1×)
- "remove" (1×)

### Sample Headings

> COOKIE CONSENT
> JOIN THE NEWSLETTER
> FRENCH SKINCARE, CULTIVATED ON A GRAND CRU TERROIR

DEVELOPED IN HARMONY WITH THE SEASONS

DESIGNED FOR YOUR SKIN LONGEVITY
> LES SOINS
> As the skin evolves with the seasons, so does our skincare.

Our formulas are designed to support the skin's evolving needs, through the seasons and throughout life.

Discover the skincare best suited to your skin today.
> PREPARE YOUR SKIN, ALL YEAR LONG
> THE FERTILE BALM

> PREPARE YOUR SKIN, ALL YEAR LONG
> TARGETED SPRING - SUMMER SKINCARE
> TARGETED AUTUMN - WINTER SKINCARE

## Page Intent

**Type:** `legal` (confidence 0.26)
**Description:** Dix Hectares offers exceptional skincare products that are 100% natural, grown on the bicentennial Grand Cru terroir of Château Montrose, and formulated in harmony with the seasons for radiant skin th

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): testimonials → nav → nav → nav → cta → nav → nav → nav → nav → nav → nav → footer → nav → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | cta | COOKIE CONSENT | 0.75 |
| 1 | nav | — | 0.4 |
| 2 | nav | JOIN THE NEWSLETTER | 0.4 |
| 3 | nav | — | 0.4 |
| 4 | testimonials | FRENCH SKINCARE, CULTIVATED ON A GRAND CRU TERROIR

DEVELOPED IN HARMONY WITH TH | 0.4 |
| 5 | nav | PREPARE YOUR SKIN, ALL YEAR LONG | 0.4 |
| 6 | nav | TARGETED SPRING - SUMMER SKINCARE | 0.4 |
| 7 | nav | TARGETED AUTUMN - WINTER SKINCARE | 0.4 |
| 8 | nav | — | 0.4 |
| 9 | nav | — | 0.4 |
| 10 | nav | PRESS

H
I
G
H
L
I
G
H
T
S


 | 0.4 |
| 11 | footer | — | 0.95 |
| 12 | nav | — | 0.9 |
| 13 | nav | — | 0.9 |

## Material Language

**Label:** `material-you` (confidence 0.45)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.326 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.218)
**Counts:** total 55, svg 0, icon 13, screenshot-like 0, photo-like 24
**Dominant aspect:** square-ish
**Radius profile on images:** rounded

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Sackers Gothic Std Heavy` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
