# Design Language: Aarke Official Website | Aarke

> Extracted from `https://aarke.com` on September 4, 2026
> 4069 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 7025 |
| `#ffffff` | hsl(0, 0%, 100%) | 1249 |
| `#3c3c3c` | hsl(0, 0%, 24%) | 61 |
| `#efefef` | hsl(0, 0%, 94%) | 16 |
| `#101010` | hsl(0, 0%, 6%) | 12 |
| `#adadad` | hsl(0, 0%, 68%) | 7 |

### Background Colors

Used on large-area elements: `#ffffff`, `#000000`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#adadad`, `#3c3c3c`, `#101010`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 7025 |
| `#ffffff` | background, text, border | 1249 |
| `#3c3c3c` | text, border, background | 61 |
| `#efefef` | background, border | 16 |
| `#101010` | text, border | 12 |
| `#adadad` | border, text | 7 |

## Typography

### Font Families

- **Body Font** — used for all (3967 elements)
- **Button Font** — used for body (96 elements)
- **Heading Font** — used for headings (6 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 22px | 1.375rem | 500 | 27px | -1px | h1, h3 |
| 20px | 1.25rem | 400 | 35px | normal | span |
| 16px | 1rem | 300 | 20.8px | normal | html, body, input, li |
| 14px | 0.875rem | 300 | 18.2px | normal | head, link, script, meta |
| 12px | 0.75rem | 300 | 15px | normal | div, li, a, span |
| 10.0002px | 0.625rem | 300 | 18.2px | normal | span |
| 10px | 0.625rem | 300 | 14px | normal | a, span, p, div |
| 9px | 0.5625rem | 300 | 11.52px | normal | span |

### Heading Scale

```css
h1 { font-size: 22px; font-weight: 500; line-height: 27px; }
h4 { font-size: 16px; font-weight: 300; line-height: 20.8px; }
h5 { font-size: 12px; font-weight: 300; line-height: 15px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 300; line-height: 18.2px; }
```

### Font Weights in Use

`300` (3962x), `500` (102x), `400` (3x), `600` (2x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-14 | 14px | 0.875rem |
| spacing-16 | 16px | 1rem |
| spacing-20 | 20px | 1.25rem |
| spacing-24 | 24px | 1.5rem |
| spacing-28 | 28px | 1.75rem |
| spacing-32 | 32px | 2rem |
| spacing-36 | 36px | 2.25rem |
| spacing-40 | 40px | 2.5rem |
| spacing-57 | 57px | 3.5625rem |
| spacing-64 | 64px | 4rem |
| spacing-128 | 128px | 8rem |
| spacing-290 | 290px | 18.125rem |
| spacing-330 | 330px | 20.625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| lg | 12px | 3 |
| full | 40px | 2 |
| full | 50px | 55 |

## Box Shadows

**md** — blur: 10px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 10px 0px;
```

**xl** — blur: 80px
```css
box-shadow: rgba(0, 0, 0, 0.2) 0px 26px 80px 0px;
```

## CSS Custom Properties

### Colors

```css
--body_color: #FFFFFF;
--primary_grey: #ADADAD;
--secondary_grey: #3C3C3C;
--loader_color: #000000;
--btn_primary_on_light_bg: rgb(0, 0, 0);
--btn_primary_on_light_txt: rgb(255, 255, 255);
--btn_primary_on_light_border: rgb(0, 0, 0);
--btn_primary_on_light_hoveredBg: rgb(60, 60, 60);
--btn_primary_on_light_hoveredTxt: rgb(255, 255, 255);
--btn_primary_on_light_hoveredBorder: rgb(60, 60, 60);
--btn_primary_on_light_pressedBg: rgb(60, 60, 60);
--btn_primary_on_light_pressedTxt: rgb(255, 255, 255);
--btn_primary_on_light_pressedBorder: rgb(60, 60, 60);
--btn_primary_on_dark_bg: rgb(255, 255, 255);
--btn_primary_on_dark_txt: rgb(0, 0, 0);
--btn_primary_on_dark_border: rgb(255, 255, 255);
--btn_primary_on_dark_hoveredBg: rgb(239, 239, 239);
--btn_primary_on_dark_hoveredTxt: rgb(0, 0, 0);
--btn_primary_on_dark_hoveredBorder: rgb(239, 239, 239);
--btn_primary_on_dark_pressedBg: rgb(239, 239, 239);
--btn_primary_on_dark_pressedTxt: rgb(0, 0, 0);
--btn_primary_on_dark_pressedBorder: rgb(239, 239, 239);
--btn_primary_misc_bg: rgb(255, 100, 0);
--btn_primary_misc_txt: rgb(255, 255, 255);
--btn_primary_misc_border: rgb(255, 100, 0);
--btn_primary_misc_hoveredBg: rgb(255, 100, 0);
--btn_primary_misc_hoveredTxt: rgb(255, 255, 255);
--btn_primary_misc_hoveredBorder: rgb(255, 100, 0);
--btn_primary_misc_pressedBg: rgb(239, 239, 239);
--btn_primary_misc_pressedTxt: rgb(255, 255, 255);
--btn_primary_misc_pressedBorder: rgb(60, 60, 60);
--btn_secondary_bg: rgba(0, 0, 0, 0.0);
--btn_secondary_txt: ;
--btn_secondary_border: rgb(0, 0, 0);
--btn_secondary_hoveredBg: rgba(0, 0, 0, 0.0);
--btn_secondary_hoveredTxt: rgb(0, 0, 0);
--btn_secondary_hoveredBorder: rgb(60, 60, 60);
--btn_secondary_pressedBg: rgba(0, 0, 0, 0.0);
--btn_secondary_pressedTxt: rgb(0, 0, 0);
--btn_secondary_pressedBorder: rgb(0, 0, 0);
--label_onSale_Bg: #000000;
--label_custom_Bg: #ebebeb;
--label_soldOut_Bg: #000000;
--secondary_font: "Secondary Heading Font";
--primary_font: "Body Font";
--pageTransitionColor: #FFFFFF;
--product-card-color-dropdown-index: 20;
--recharge-color-brand-120: var(--btn_primary_on_light_bg);
--recharge-button-secondary: var(--p_text_1);
--recharge-color-brand: var(--p_text_1);
--jdgm-primary-color: #000;
--jdgm-secondary-color: rgba(0,0,0,0.1);
--jdgm-star-color: #000;
--jdgm-write-review-text-color: white;
--jdgm-write-review-bg-color: #000000;
--jdgm-paginate-color: #000;
--jdgm-border-radius: 0;
--jdgm-reviewer-name-color: #000000;
--ann-transparentTextColor: #000000;
--header-tx-color: transparent;
--header-bg-color: #ffffff;
--header-text-color: #000000;
--header-trtxt-color: #ffffff;
--swiper-theme-color: #007aff;
--secondary_accent: #e8e8e8;
--background_color: #ffffff;
--primary_accent: #efefef;
--button-bg: #efefef;
--primary_text: #000000;
--secondary_text: #f8f8f8;
--button-border: #efefef;
```

### Spacing

```css
--swiper-navigation-size: 44px;
```

### Typography

```css
--p_text_1: #000000;
--p_text_2: #3C3C3C;
--p_text_3: ;
--s_text_1: #000000;
--s_text_2: #3C3C3C;
--s_text_3: ;
--t_text_1: #FFFFFF;
--t_text_2: #EFEFEF;
--t_text_3: ;
--label_onSale_text: #ffffff;
--label_custom_text: #3C3C3C;
--label_soldOut_text: #ffffff;
--header_font: "Heading Font";
--rich_text_font: "Rich Text Font";
--button_font: "Button Font";
--button-text-index: 10;
--text_1: #000000;
--text_2: #3C3C3C;
--text_3: ;
```

### Other

```css
--p_background_1: #FFFFFF;
--p_details_1: #EFEFEF;
--p_details_2: #E8E8E8;
--s_background_1: #EFEFEF;
--s_details_1: #FFFFFF;
--s_details_2: #E8E8E8;
--t_background_1: #000000;
--t_details_1: #FFFFFF;
--t_details_2: #EFEFEF;
--product_price_when_compare: #000000;
--submenu-position: 54px;
--header-height: 54px;
--btn_tertiary: rgb(0, 0, 0);
--alert_success: #000000;
--alert_error: #000000;
--background_mob_image: ;
--background_desk_image: ;
--ann-is-transparent: 0;
--section_max_width: 1440px;
--swiper-notification-index: 999;
--page-transition-index: 999;
--product-zoom-index: 100;
--skip-to-content-index: 99;
--popup-index: 99;
--selectbox-index: 23;
--drawer-index: 22;
--search-wrapper-index: 22;
--overlay-index: 21;
--header-index: 20;
--page-loader-index: 10;
--header-sticky-index: 20;
--swiper-component-index: 10;
--announcement-bar-index: 8;
--ann-is-transparent-control: 1;
--ann-transparent: #ebebeb;
--header-sticky: 1;
--header-is-transparent: 1;
--header-is-transparent-control: 0;
--logo-invert: invert(1);
--details_2: #E8E8E8;
--announcement-height: 30px;
--button-content: #ffffff;
--window-height: 800px;
--background_1: #FFFFFF;
--details_1: #EFEFEF;
--footer-height: 1085px;
--announcement-dynamic-height: 30px;
--search-header-height: 65px;
```

### Dependencies

```css
--recharge-color-brand-120: --btn_primary_on_light_bg;
--recharge-button-secondary: --p_text_1;
--recharge-color-brand: --p_text_1;
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
| xs | 375px | max-width |
| 560px | 560px | max-width |
| sm | 600px | min-width |
| sm | 650px | max-width |
| md | 750px | max-width |
| md | 767px | max-width |
| md | 768px | max-width |
| md | 769px | max-width |
| 899px | 899px | max-width |
| 905px | 905px | min-width |
| lg | 1024px | max-width |
| lg | 1025px | min-width |
| lg | 1044px | min-width |
| lg | 1051px | max-width |
| lg | 1080px | max-width |
| xl | 1225px | min-width |
| xl | 1280px | max-width |
| xl | 1281px | min-width |
| 1439px | 1439px | max-width |
| 1440px | 1440px | min-width |
| 1920px | 1920px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.5s`, `0.1s`, `0.2s`, `0.15s`, `0.35s`, `0.6s`, `1s`, `0.8s`, `0.4s`

### Common Transitions

```css
transition: all;
transition: transform 0.3s;
transition: 0.3s ease-in-out;
transition: width 0.5s ease-in-out;
transition: 0.1s ease-in-out;
transition: 0.5s;
transition: opacity 0.3s, transform 0.5s, background-color 0.3s, visibility 0.3s;
transition: opacity 0.3s ease-in-out;
transition: opacity 0.2s;
transition: 0.3s ease-in, opacity 0.2s ease-in;
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

**opacityIn**
```css
@keyframes opacityIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**fromTopAndOpacityIn**
```css
@keyframes fromTopAndOpacityIn {
  0% { opacity: 0; transform: translateY(-100%); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**opacityOut**
```css
@keyframes opacityOut {
  0% { opacity: 1; }
  100% { opacity: 0; }
}
```

**ScaleIn**
```css
@keyframes ScaleIn {
  0% { transform: scale(0.96); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}
```

**ScaleOut**
```css
@keyframes ScaleOut {
  0% { transform: scale(1.04); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}
```

**hide-scroll**
```css
@keyframes hide-scroll {
  0%, 100% { overflow: hidden; }
}
```

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (117 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (793 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (595 instances)

```css
.input {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  border-color: rgb(0, 0, 0);
  border-radius: 0px;
  font-size: 14px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (107 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 300;
}
```

### Navigation (57 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (84 instances)

```css
.foote {
  background-color: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 14px;
}
```

### Modals (43 instances)

```css
.modal {
  background-color: rgb(0, 0, 0);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.2) 0px 26px 80px 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 100%;
}
```

### Dropdowns (141 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Badges (29 instances)

```css
.badge {
  background-color: rgb(235, 235, 235);
  color: rgb(255, 255, 255);
  font-size: 12px;
  font-weight: 500;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Switches (1 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 300;
```

### Button — 45 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 16px 16px 16px 16px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

**Variant 2** (42 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 13.5px 32px 13.5px 32px;
  border-radius: 0px;
  border: 1px solid rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Button — 22 instances, 1 variant

**Variant 1** (22 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 300;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 10px 12px 10px 16px;
  border-radius: 0px;
  border: 1px solid rgb(173, 173, 173);
  font-size: 14px;
  font-weight: 300;
```

### Button — 21 instances, 1 variant

**Variant 1** (21 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 12px 32px 12px 32px;
  border-radius: 0px;
  border: 1px solid rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Button — 21 instances, 1 variant

**Variant 1** (21 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 300;
```

### Card — 21 instances, 1 variant

**Variant 1** (21 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Card — 21 instances, 1 variant

**Variant 1** (21 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Card — 61 instances, 1 variant

**Variant 1** (61 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Button — 21 instances, 1 variant

**Variant 1** (21 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 300;
```

### Card — 20 instances, 1 variant

**Variant 1** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Card — 20 instances, 1 variant

**Variant 1** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 300;
```

### Card — 23 instances, 2 variants

**Variant 1** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(60, 60, 60);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(60, 60, 60);
  font-size: 12px;
  font-weight: 300;
```

**Variant 2** (3 instances)

```css
  background: rgb(235, 235, 235);
  color: rgb(60, 60, 60);
  padding: 4px 12px 4px 12px;
  border-radius: 12px;
  border: 0px none rgb(60, 60, 60);
  font-size: 10px;
  font-weight: 300;
```

## Layout System

**9 grid containers** and **815 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 700px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 7x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 1280px;
grid-template-columns: 264px 264px 264px 264px;
gap: 64px 32px;
grid-template-columns: 540px;
grid-template-columns: 384px;
gap: 32px;
grid-template-columns: 102px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 95x |
| row/nowrap | 695x |
| row/wrap | 25x |

**Gap values:** `128px`, `12px`, `16px`, `24px`, `32px`, `4px`, `64px`, `64px 32px`, `8px`, `normal 5.25px`

## Responsive Design

### Viewport Snapshots

| Viewport | Body Font | Nav Visible | Max Columns | Hamburger | Page Height |
|----------|-----------|-------------|-------------|-----------|-------------|
| mobile (375px) | 14px | No | 1 | Yes | 5688px |
| tablet (768px) | 14px | No | 1 | Yes | 9220px |
| desktop (1280px) | 16px | No | 1 | Yes | 4729px |
| wide (1920px) | 16px | No | 1 | Yes | 6427px |

### Breakpoint Changes

**375px → 768px** (mobile → tablet):
- Page height: `5688px` → `9220px`

**768px → 1280px** (tablet → desktop):
- Body font size: `14px` → `16px`
- Page height: `9220px` → `4729px`

**1280px → 1920px** (desktop → wide):
- Page height: `4729px` → `6427px`

## Interaction States

### Button States

**"IT / EUR"**
```css
/* Hover */
color: rgb(255, 255, 255) → rgb(160, 160, 160);
border-color: rgb(255, 255, 255) → rgb(160, 160, 160);
outline: rgb(255, 255, 255) none 3px → rgb(160, 160, 160) none 3px;
```
```css
/* Focus */
color: rgb(255, 255, 255) → rgb(59, 59, 59);
border-color: rgb(255, 255, 255) → rgb(59, 59, 59);
outline: rgb(255, 255, 255) none 3px → rgb(59, 59, 59) none 3px;
```

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 27 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#000000` | `#ffffff` | 21:1 | AAA |
| `#ffffff` | `#000000` | 21:1 | AAA |

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 85/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- No clear primary brand color detected
- 386 !important rules — prefer specificity over overrides
- 86% of CSS is unused — consider purging
- 3738 duplicate CSS declarations

## Z-Index Map

**24 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9998,2147483636 | div.m.d.-.m.o.d.a.l._._.b.a.c.k.d.r.o.p, div.m.d.-.a.p.p.-.e.m.b.e.d. .o.r.b.e.-.-.h.i.d.d.e.n, div.m.d.-.m.o.d.a.l._._.c.o.n.t.a.i.n.e.r |
| dropdown | 100,999 | localization-selectors.l.o.c.a.l.i.z.a.t.i.o.n.S.e.l.e.c.t.o.r.s.A.n.d.L.o.g.i.n. .s.i.d.e.b.a.r.-.m.e.n.u._._.l.o.c.a.l.i.z.a.t.i.o.n.-.s.e.l.e.c.t.o.r.s, div.p.a.g.e.T.r.a.n.s.i.t.i.o.n. .l.o.a.d._.f.i.n.i.s.h.e.d, span.s.w.i.p.e.r.-.n.o.t.i.f.i.c.a.t.i.o.n |
| sticky | 10,99 | div.p.a.g.e.L.o.a.d.e.r, span.b.u.t.t.o.n.-.-.t.e.x.t. .u.-.p.2, span.b.u.t.t.o.n.-.-.t.e.x.t. .u.-.p.2 |
| base | -100,8 | div, div.c.o.l.o.r.G.r.o.u.p.-.-.h.e.a.d.e.r. .d.e.s.k.t.o.p.M.e.n.u.-.-.D.r.o.p.d.o.w.n. .m.a.i.n.M.e.n.u.-.-.L.i.n.k.s._.s.h.o.p, div.d.e.s.k.t.o.p.M.e.n.u.-.-.L.i.n.k.H.o.l.d.e.r. .m.a.i.n.M.e.n.u.-.-.L.i.n.k.H.o.l.d.e.r._.s.h.o.p. .s.h.o.p |

**Issues:**
- [object Object]

## SVG Icons

**23 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 4 |
| md | 6 |
| xl | 12 |

**Icon colors:** `black`, `#000`, `#0071CE`, `white`, `#FFF`, `rgb(0, 0, 0)`, `#fff`, `#1E3764`, `url(#pi-bancontact-a)`, `url(#pi-bancontact-b)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Heading Font | self-hosted | 400 | normal |
| Secondary Heading Font | self-hosted | 500 | normal |
| Rich Text Font | self-hosted | 400 | normal |
| Body Font | self-hosted | 400 | normal |
| Button Font | self-hosted | 500 | normal |
| JudgemeStar | self-hosted | normal | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 167 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 14 | objectFit: contain, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (167x), 3:2 (12x), 2.7:1 (2x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `800ms` | 800 |

### Easing Families

- **ease-in-out** (91 uses) — `ease`
- **ease-out** (51 uses) — `cubic-bezier(0.215, 0.61, 0.355, 1)`
- **custom** (52 uses) — `cubic-bezier(0.86, 0, 0.07, 1)`, `cubic-bezier(0.37, 0, 0, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `slideOut` | slide-y | transform, opacity | 1 |
| `movingText` | slide-x | transform | 2 |
| `msSelectboxSlideOut` | slide-y | transform, opacity | 2 |

## Component Anatomy

### card — 166 instances

**Slots:** media
**Variants:** link

| variant | count | sample label |
|---|---|---|
| default | 145 | Add to cart
Carbonator 3 Steel Starter k |
| link | 21 | Add to cart
Carbonator 3 Steel Starter k |

### button — 133 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **add** (81)
- **confirm** (3)
- **shop** (2)
- **it** (1)
- **english** (1)

### Button Copy Patterns

- "add to cart" (81×)
- "confirm and close" (3×)
- "shop now" (2×)
- "it / eur" (1×)
- "english" (1×)

### Sample Headings

> Don’t forget to add
> All products
> Don’t forget to add
> All products
> Thank you!

## Page Intent

**Type:** `landing` (confidence 0.29)

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): content → content → content → pricing → testimonials → content → pricing-table → content → content → pricing-table → nav → feature-grid → footer → content → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | content | — | 0.3 |
| 1 | content | — | 0.3 |
| 2 | content | — | 0.3 |
| 3 | pricing | — | 0.4 |
| 4 | content | — | 0.3 |
| 5 | pricing-table | Don’t forget to add | 0.9 |
| 6 | content | Don’t forget to add | 0.3 |
| 7 | testimonials | — | 0.4 |
| 8 | content | All products | 0.3 |
| 9 | pricing-table | — | 0.9 |
| 10 | nav | — | 0.9 |
| 11 | feature-grid | — | 0.8 |
| 12 | footer | — | 0.95 |
| 13 | content | — | 0.3 |
| 14 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 181, svg 12, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Body Font` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
