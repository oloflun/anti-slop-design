# Design Language: OLIPOP | Healthy Prebiotic Soda

> Extracted from `https://drinkolipop.com` on September 8, 2026
> 4293 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#034638` | rgb(3, 70, 56) | hsl(167, 92%, 14%) | 1189 |
| Secondary | `#ffff7d` | rgb(255, 255, 125) | hsl(60, 100%, 75%) | 2 |
| Accent | `#98e1c3` | rgb(152, 225, 195) | hsl(155, 55%, 74%) | 2 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#3a3a3a` | hsl(0, 0%, 23%) | 1339 |
| `#000000` | hsl(0, 0%, 0%) | 1083 |
| `#ffffff` | hsl(0, 0%, 100%) | 450 |
| `#fff6ea` | hsl(34, 100%, 96%) | 116 |
| `#9a9a9a` | hsl(0, 0%, 60%) | 38 |
| `#737373` | hsl(0, 0%, 45%) | 24 |
| `#4f7456` | hsl(131, 19%, 38%) | 20 |
| `#cccccc` | hsl(0, 0%, 80%) | 8 |
| `#e3e3e3` | hsl(0, 0%, 89%) | 8 |
| `#f0f0f0` | hsl(0, 0%, 94%) | 5 |

### Background Colors

Used on large-area elements: `#ffffff`, `#000000`, `#034638`, `#fff6ea`, `#008168`, `#ffb8b3`, `#fffbf5`

### Text Colors

Text color palette: `#000000`, `#14433d`, `#3a3a3a`, `#ffffff`, `#034638`, `#008168`, `#fff6ea`, `#0a3128`, `#fff7e5`, `#16433d`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#14433d` | text, border, background | 4241 |
| `#3a3a3a` | text, border | 1339 |
| `#034638` | background, text, border | 1189 |
| `#000000` | text, border, background | 1083 |
| `#ffffff` | background, text, border | 450 |
| `#fff6ea` | background, text, border | 116 |
| `#0a3128` | text, border | 78 |
| `#008168` | background, text, border | 61 |
| `#9a9a9a` | text, border | 38 |
| `#44be70` | text, border | 36 |
| `#737373` | text, border | 24 |
| `#4f7456` | text, border | 20 |
| `#f3e4cd` | border, background | 14 |
| `#cccccc` | border | 8 |
| `#e3e3e3` | border | 8 |
| `#f0f0f0` | border, background | 5 |
| `#98e1c3` | background | 2 |
| `#ffff7d` | background | 2 |
| `#ffb8b3` | background | 1 |

## Typography

### Font Families

- **Ano** — used for all (3640 elements)
- **Times New Roman** — used for body (370 elements)
- **Helvetica** — used for body (120 elements)
- **Ano Bold** — used for body (86 elements)
- **WindsorEF** — used for all (61 elements)
- **Windsor Bold** — used for body (8 elements)
- **Arial** — used for body (2 elements)
- **GTStandard-M** — used for body (2 elements)
- **SF-Secondary-Font** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 80px | 5rem | 800 | 80px | normal | h2, br |
| 54px | 3.375rem | 800 | 54px | normal | h4 |
| 52px | 3.25rem | 800 | 52px | normal | h2 |
| 50px | 3.125rem | 700 | 62px | normal | h2 |
| 48px | 3rem | 800 | 62px | normal | h2, h3 |
| 40px | 2.5rem | 900 | 44px | normal | h2, h4 |
| 32px | 2rem | 900 | 35.2px | normal | h4, h2 |
| 24px | 1.5rem | 800 | 26.4px | normal | h3, h4 |
| 22px | 1.375rem | 400 | 36px | normal | p |
| 20px | 1.25rem | 700 | 20px | normal | h1, a, img, span |
| 18px | 1.125rem | 700 | 30px | normal | a, button, span, svg |
| 16px | 1rem | 400 | normal | normal | html, head, div, style |
| 14px | 0.875rem | 400 | 25.2px | normal | div, span, a, svg |
| 12px | 0.75rem | 700 | 14.4px | normal | span, div, button |
| 10px | 0.625rem | 700 | 10px | normal | span, div |

### Heading Scale

```css
h2 { font-size: 80px; font-weight: 800; line-height: 80px; }
h4 { font-size: 54px; font-weight: 800; line-height: 54px; }
h2 { font-size: 52px; font-weight: 800; line-height: 52px; }
h2 { font-size: 50px; font-weight: 700; line-height: 62px; }
h2 { font-size: 48px; font-weight: 800; line-height: 62px; }
h2 { font-size: 40px; font-weight: 900; line-height: 44px; }
h4 { font-size: 32px; font-weight: 900; line-height: 35.2px; }
h3 { font-size: 24px; font-weight: 800; line-height: 26.4px; }
h1 { font-size: 20px; font-weight: 700; line-height: 20px; }
h4 { font-size: 14px; font-weight: 400; line-height: 25.2px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (3955x), `700` (229x), `900` (46x), `600` (39x), `800` (15x), `500` (6x), `300` (1x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-0 | 0px | 0rem |
| spacing-30 | 30px | 1.875rem |
| spacing-36 | 36px | 2.25rem |
| spacing-40 | 40px | 2.5rem |
| spacing-45 | 45px | 2.8125rem |
| spacing-48 | 48px | 3rem |
| spacing-53 | 53px | 3.3125rem |
| spacing-60 | 60px | 3.75rem |
| spacing-63 | 63px | 3.9375rem |
| spacing-72 | 72px | 4.5rem |
| spacing-80 | 80px | 5rem |
| spacing-86 | 86px | 5.375rem |
| spacing-92 | 92px | 5.75rem |
| spacing-106 | 106px | 6.625rem |
| spacing-120 | 120px | 7.5rem |
| spacing-160 | 160px | 10rem |
| spacing-168 | 168px | 10.5rem |
| spacing-172 | 172px | 10.75rem |
| spacing-224 | 224px | 14rem |
| spacing-248 | 248px | 15.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 118 |
| sm | 5px | 6 |
| md | 8px | 2 |
| lg | 12px | 45 |
| lg | 16px | 47 |
| xl | 24px | 2 |
| full | 48px | 2 |
| full | 100px | 27 |
| full | 9999px | 11 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgb(3, 70, 56) 0px 0px 0px 1.5px;
```

**sm** — blur: 0px
```css
box-shadow: rgb(20, 67, 61) 0px 0px 0px 1.5px;
```

**md** — blur: 8px
```css
box-shadow: rgba(0, 0, 0, 0.25) 0px 4px 8px 0px;
```

**xl** — blur: 32px
```css
box-shadow: rgba(0, 0, 0, 0.07) 8px 0px 32px 0px;
```

**xl** — blur: 80px
```css
box-shadow: rgba(0, 0, 0, 0.12) 0px 0px 80px 0px;
```

## CSS Custom Properties

### Colors

```css
--color-text: #3a3a3a;
--color-text-shadow: rgba(0,0,0,0.4);
--color-body-text: #333232;
--color-sale-text: #fa4545;
--color-small-button-text-border: #3a3a3a;
--color-text-field: rgba(0,0,0,0);
--color-text-field-text: #000000;
--color-navigation-text: #3a3a3a;
--color-btn-primary: #3a3a3a;
--color-btn-primary-darken: #212121;
--color-btn-primary-transparent: rgba(58, 58, 58, 0.8);
--color-btn-primary-text: #ffffff;
--color-body: #ffffff;
--color-bg: #ffffff;
--color-drawer-background: rgba(0, 0, 0, 0.6);
--color-bg-alt: rgba(51, 50, 50, 0.05);
--color-link: var(--color-body-text);
--color-overlay-title-text: #ffffff;
--color-image-overlay: #685858;
--color-text-focus: #606060;
--color-overlay-text-focus: #e6e6e6;
--color-btn-primary-focus: #606060;
--color-btn-social-focus: #d2d2d2;
--color-small-button-text-border-focus: #606060;
--color-disabled: #f4f4f4;
--color-disabled-border: #f4f4f4;
--color-error: #d20000;
--color-error-message-list: #651818;
--color-error-bg: #fff8f8;
--color-success: #1F873D;
--color-success-bg: #f8fff9;
--color-grey: #B5C1BF;
--color-dark-green: #14433D;
--color-border: #ebebeb;
--color-border-form: #cccccc;
--color-border-form-darken: #b3b3b3;
--color-form-text: #333;
--color-error-input-text: var(--color-error);
--input-border-width: 1px;
--color-facebook: #3b5998;
--color-twitter: #00aced;
--color-pinterest: #cb2027;
--color-slideshow-arrows: #000;
--color-slideshow-dots: #fff;
--border-radius: 2px;
--color-giftcard-tooltip-fallback: #333;
--color-giftcard-light: #fff;
--color-giftcard-tooltip: rgba(0, 0, 0, 0.9);
--color-giftcard-disabled: #999;
--color-giftcard-small-text: #b3b3b3;
--color-giftcard-shadow: rgba(0, 0, 0, 0.1);
--color-giftcard-print-bg: #fff;
--color-giftcard-print: #000;
--color-giftcard-bg: #e95e61;
--z-index-giftcard-image: 2;
--z-index-giftcard-corners: 3;
--z-index-giftcard-tooltip: 4;
--z-index-giftcard-code: 5;
--color-video-bg: #f2f2f2;
--color-video-controls: #fff;
--color-video-controls-background: #000;
--preview-card-url: url(//drinkolipop.com/cdn/shop/products/1DigitalGiftCard-WEB-080422-AM_200x.png?v=1767277571);
--flavor-color-overlay: ;
--flavor-color-100: ;
--flavor-color-200: ;
--flavor-color-300: ;
--flavor-color-selector: ;
--sl-color-gray-200: hsl(240 5.9% 90%);
--sl-color-teal-950: hsl(176.5 58.6% 11.4%);
--sl-panel-border-width: 1px;
--sl-color-amber-700: hsl(26 90.5% 37.1%);
--sl-color-fuchsia-800: hsl(295.4 70.2% 32.9%);
--rb-smart-collections-button-background-color: #16433d;
--sl-color-pink-950: hsl(336.2 65.4% 15.9%);
--sl-color-green-50: hsl(138.5 76.5% 96.7%);
--sl-color-amber-100: hsl(48 96.5% 88.8%);
--sl-color-blue-500: hsl(217.2 91.2% 59.8%);
--rb-smart-search-results-product-price-compare-at-color: #9a9a9a;
--sl-input-filled-background-color-hover: hsl(240 4.8% 95.9%);
--rb-smart-search-quick-view-button-text-color: #ffffff;
--sl-color-rose-300: hsl(352.6 95.7% 81.8%);
--tw-ring-color: rgb(59 130 246 / 0.5);
--sl-color-lime-50: hsl(78.3 92% 95.1%);
--sl-overlay-background-color: hsl(240 3.8% 46.1% / 33%);
--sl-input-required-content-color: ;
--sl-color-primary-600: hsl(200.4 98% 39.4%);
--sl-color-red-400: hsl(0 90.6% 70.8%);
--sl-color-emerald-50: hsl(151.8 81% 95.9%);
--sl-color-fuchsia-950: hsl(297.1 56.8% 14.5%);
--sl-input-background-color: hsl(0, 0%, 100%);
--sl-color-sky-700: hsl(201.3 96.3% 32.2%);
--sl-input-filled-background-color-focus: hsl(240 4.8% 95.9%);
--rb-smart-search-quick-view-button-border-width: 2px;
--sl-color-pink-50: hsl(327.3 73.3% 97.1%);
--sl-color-cyan-900: hsl(196.4 63.6% 23.7%);
--sl-color-lime-100: hsl(79.6 89.1% 89.2%);
--sl-color-warning-200: hsl(48 96.6% 76.7%);
--sl-color-neutral-200: hsl(240 5.9% 90%);
--sl-color-warning-700: hsl(26 90.5% 37.1%);
--sl-color-green-400: hsl(141.9 69.2% 58%);
--sl-color-gray-50: hsl(0 0% 97.5%);
--rb-smart-search-results-button-text-color: #ffffff;
--sl-color-blue-700: hsl(224.3 76.3% 48%);
--sl-color-orange-100: hsl(34.3 100% 91.8%);
--sl-input-filled-color-focus: hsl(240 5.3% 26.1%);
--sl-color-warning-300: hsl(45.9 96.7% 64.5%);
--sl-color-sky-200: hsl(200.6 94.4% 86.1%);
--sl-color-red-100: hsl(0 93.3% 94.1%);
--sl-color-rose-950: hsl(341.3 70.1% 17.1%);
--sl-color-success-600: hsl(142.1 76.2% 36.3%);
--sl-color-yellow-50: hsl(54.5 91.7% 95.3%);
--sl-color-warning-950: hsl(22.9 74.1% 16.7%);
--sl-border-radius-large: 0.5rem;
--rb-widget-input-border-color: #cccccc;
--sl-color-pink-700: hsl(335.1 77.6% 42%);
--sl-color-teal-600: hsl(174.7 83.9% 31.6%);
--sl-color-danger-50: hsl(0 85.7% 97.3%);
--sl-color-indigo-500: hsl(238.7 83.5% 66.7%);
--rb-smart-search-results-reviews-background-color: #E5E5E5;
--sl-color-orange-200: hsl(32.1 97.7% 83.1%);
--sl-color-amber-900: hsl(21.7 77.8% 26.5%);
--sl-color-pink-600: hsl(333.3 71.4% 50.6%);
--sl-color-teal-500: hsl(173.4 80.4% 40%);
--sl-color-violet-500: hsl(258.3 89.5% 66.3%);
--sl-input-border-color: hsl(240 4.9% 83.9%);
--sl-color-fuchsia-900: hsl(296.7 63.6% 28%);
--sl-color-neutral-600: hsl(240 5.2% 33.9%);
--rb-smart-collections-pagination-button-text-color: #ffffff;
--sl-color-indigo-100: hsl(226.5 100% 93.9%);
--rb-smart-search-results-product-price-sale-color: #44BE70;
--sl-color-amber-500: hsl(37.7 92.1% 50.2%);
--sl-input-color: hsl(240 5.3% 26.1%);
--sl-color-lime-950: hsl(86.5 60.6% 13.9%);
--sl-border-radius-small: 0.1875rem;
--rb-smart-search-quick-view-reviews-foreground-color: #FBCA10;
--sl-color-warning-900: hsl(21.7 77.8% 26.5%);
--sl-color-orange-300: hsl(30.7 97.2% 72.4%);
--sl-color-teal-50: hsl(166.2 76.5% 96.7%);
--sl-color-primary-400: hsl(198.4 93.2% 59.6%);
--sl-color-indigo-700: hsl(244.5 57.9% 50.6%);
--sl-color-danger-950: hsl(0 60% 19.6%);
--rb-smart-collections-button-border-color: #16433d;
--sl-input-background-color-focus: hsl(0, 0%, 100%);
--sl-input-filled-color: hsl(240 3.7% 15.9%);
--sl-color-violet-700: hsl(263.4 70% 50.4%);
--sl-color-violet-100: hsl(251.4 91.3% 95.5%);
--rb-smart-collections-button-text-color: #ffffff;
--sl-color-amber-400: hsl(43.3 96.4% 56.3%);
--sl-color-rose-100: hsl(355.6 100% 94.7%);
--sl-input-filled-color-hover: hsl(240 3.7% 15.9%);
--sl-color-emerald-400: hsl(158.1 64.4% 51.6%);
--sl-color-fuchsia-500: hsl(292.2 84.1% 60.6%);
--sl-color-success-900: hsl(143.8 61.2% 20.2%);
--sl-color-blue-950: hsl(226.2 55.3% 18.4%);
--tw-ring-shadow: 0 0 #0000;
--sl-color-cyan-50: hsl(183.2 100% 96.3%);
--rb-smart-search-quick-view-product-title-color: #16433d;
--sl-color-rose-50: hsl(355.7 100% 97.3%);
--sl-color-primary-100: hsl(204 93.8% 93.7%);
--sl-color-yellow-900: hsl(28.4 72.5% 25.7%);
--sl-color-danger-100: hsl(0 93.3% 94.1%);
--sl-color-teal-700: hsl(175.3 77.4% 26.1%);
--sl-color-amber-300: hsl(45.9 96.7% 64.5%);
--sl-color-yellow-500: hsl(45.4 93.4% 47.5%);
--sl-color-success-200: hsl(141 78.9% 85.1%);
--sl-color-rose-700: hsl(345.3 82.7% 40.8%);
--tw-border-spacing-x: 0;
--sl-color-blue-200: hsl(213.3 96.9% 87.3%);
--sl-color-primary-950: hsl(202.3 73.8% 16.5%);
--rb-smart-search-quick-view-button-background-color: #16433d;
--sl-input-background-color-hover: hsl(0, 0%, 100%);
--sl-color-blue-600: hsl(221.2 83.2% 53.3%);
--sl-color-violet-950: hsl(265.1 61.5% 21.4%);
--sl-color-green-700: hsl(142.4 71.8% 29.2%);
--sl-color-primary-50: hsl(204 100% 97.1%);
--sl-color-rose-800: hsl(343.4 79.7% 34.7%);
--sl-color-lime-900: hsl(87.6 61.2% 20.2%);
--sl-color-danger-600: hsl(0 72.2% 50.6%);
--sl-border-radius-pill: 9999px;
--sl-color-red-600: hsl(0 72.2% 50.6%);
--rb-smart-collections-product-title-color: #16433d;
--rb-smart-collections-product-price-color: #16433d;
--sl-tooltip-background-color: hsl(240 3.7% 15.9%);
--rb-smart-search-results-content-description-color: #405768;
--rb-smart-search-quick-view-reviews-text-color: #535353;
--sl-color-lime-200: hsl(80.9 88.5% 79.6%);
--vw-focus-outline-color: #0018ff;
--rb-smart-search-results-button-border-width: 2px;
--rb-smart-search-quick-view-product-price-color: #16433d;
--sl-color-green-200: hsl(141 78.9% 85.1%);
--tw-ring-offset-width: 0px;
--sl-focus-ring-color: hsl(200.4 98% 39.4%);
--sl-color-warning-500: hsl(37.7 92.1% 50.2%);
--sl-color-sky-900: hsl(202 80.3% 23.9%);
--tw-shadow-colored: 0 0 #0000;
--sl-color-pink-400: hsl(328.6 85.5% 70.2%);
--sl-color-sky-300: hsl(199.4 95.5% 73.9%);
--rb-smart-search-results-reviews-foreground-color: #FBCA10;
--sl-color-yellow-800: hsl(31.8 81% 28.8%);
--sl-color-violet-400: hsl(255.1 91.7% 76.3%);
--sl-color-sky-400: hsl(198.4 93.2% 59.6%);
--sl-input-label-color: ;
--sl-color-orange-50: hsl(33.3 100% 96.5%);
--sl-color-red-800: hsl(0 70% 35.3%);
--sl-color-success-500: hsl(142.1 70.6% 45.3%);
--sl-color-sky-950: hsl(202.3 73.8% 16.5%);
--tw-ring-offset-shadow: 0 0 #0000;
--sl-color-red-500: hsl(0 84.2% 60.2%);
--sl-color-pink-300: hsl(327.4 87.1% 81.8%);
--sl-color-green-100: hsl(140.6 84.2% 92.5%);
--sl-color-primary-200: hsl(200.6 94.4% 86.1%);
--sl-color-neutral-300: hsl(240 4.9% 83.9%);
--rb-widget-input-border-focus-color: #16433d;
--sl-border-radius-circle: 50%;
--tw-ring-inset: ;
--sl-input-border-color-focus: hsl(198.6 88.7% 48.4%);
--sl-color-purple-300: hsl(269.2 97.4% 85.1%);
--sl-color-teal-100: hsl(167.2 85.5% 89.2%);
--sl-input-border-color-disabled: hsl(240 4.9% 83.9%);
--sl-input-filled-color-disabled: hsl(240 3.7% 15.9%);
--sl-color-danger-300: hsl(0 93.5% 81.8%);
--sl-color-cyan-400: hsl(187.9 85.7% 53.3%);
--sl-color-green-600: hsl(142.1 76.2% 36.3%);
--sl-color-rose-500: hsl(349.7 89.2% 60.2%);
--sl-focus-ring: solid 3px
    hsl(200.4 98% 39.4%);
--sl-color-success-100: hsl(140.6 84.2% 92.5%);
--sl-input-border-radius-medium: 0.25rem;
--sl-focus-ring-offset: 1px;
--sl-input-border-radius-large: 0.25rem;
--sl-input-icon-color-hover: hsl(240 5.2% 33.9%);
--sl-color-gray-100: hsl(240 4.8% 95.9%);
--sl-color-purple-700: hsl(272.1 71.7% 47.1%);
--sl-color-purple-400: hsl(270 95.2% 75.3%);
--sl-color-violet-900: hsl(263.5 67.4% 34.9%);
--sl-color-green-950: hsl(144.3 60.7% 12%);
--rb-smart-search-quick-view-button-border-color: #16433d;
--rb-smart-search-results-pagination-button-background-color: #16433d;
--rb-smart-search-results-content-active-tab-color: #335eea;
--sl-color-blue-400: hsl(213.1 93.9% 67.8%);
--sl-color-sky-600: hsl(200.4 98% 39.4%);
--sl-color-teal-900: hsl(175.9 60.8% 19%);
--sl-color-indigo-900: hsl(242.2 47.4% 34.3%);
--sl-color-neutral-1000: hsl(0, 0%, 0%);
--sl-color-cyan-700: hsl(192.9 82.3% 31%);
--sl-color-orange-900: hsl(15.3 74.6% 27.8%);
--sl-color-neutral-50: hsl(0 0% 97.5%);
--videowise-story-border: linear-gradient(to top right,#4efac0,#ff5742);
--sl-color-green-300: hsl(141.7 76.6% 73.1%);
--sl-color-sky-50: hsl(204 100% 97.1%);
--sl-color-warning-600: hsl(32.1 94.6% 43.7%);
--sl-color-amber-950: hsl(22.9 74.1% 16.7%);
--sl-color-warning-400: hsl(43.3 96.4% 56.3%);
--sl-color-yellow-200: hsl(52.8 98.3% 76.9%);
--sl-color-emerald-900: hsl(164.2 85.7% 16.5%);
--sl-color-emerald-800: hsl(163.1 88.1% 19.8%);
--sl-color-yellow-400: hsl(47.9 95.8% 53.1%);
--sl-color-yellow-700: hsl(35.5 91.7% 32.9%);
--sl-color-neutral-500: hsl(240 3.8% 46.1%);
--sl-color-amber-600: hsl(32.1 94.6% 43.7%);
--sl-input-placeholder-color: hsl(240 3.8% 46.1%);
--sl-color-danger-200: hsl(0 96.3% 89.4%);
--sl-color-orange-500: hsl(24.6 95% 53.1%);
--sl-input-focus-ring-offset: 0;
--rb-smart-search-results-pagination-button-text-color: #ffffff;
--sl-color-sky-800: hsl(201 90% 27.5%);
--sl-color-emerald-100: hsl(149.3 80.4% 90%);
--rb-smart-search-results-button-border-color: #16433d;
--rb-smart-collections-reviews-foreground-color: #FBCA10;
--sl-input-border-width: 1px;
--sl-color-success-800: hsl(142.8 64.2% 24.1%);
--rb-smart-search-quick-view-product-price-compare-at-color: #9a9a9a;
--sl-color-amber-200: hsl(48 96.6% 76.7%);
--sl-input-color-hover: hsl(240 5.3% 26.1%);
--sl-color-teal-400: hsl(172.5 66% 50.4%);
--sl-color-primary-800: hsl(201 90% 27.5%);
--rb-smart-collections-product-price-compare-at-color: #9a9a9a;
--sl-color-neutral-0: hsl(0, 0%, 100%);
--sl-color-gray-400: hsl(240 5% 64.9%);
--sl-color-red-700: hsl(0 73.7% 41.8%);
--sl-panel-background-color: hsl(0, 0%, 100%);
--sl-color-gray-700: hsl(240 5.3% 26.1%);
--rb-smart-collections-button-border-width: 2px;
--sl-color-emerald-600: hsl(161.4 93.5% 30.4%);
--sl-input-background-color-disabled: hsl(240 4.8% 95.9%);
--sl-color-blue-800: hsl(225.9 70.7% 40.2%);
--sl-color-danger-400: hsl(0 90.6% 70.8%);
--sl-color-gray-950: hsl(240 7.3% 8%);
--rb-smart-collections-product-price-sale-color: #44BE70;
--rb-smart-collections-reviews-text-color: #535353;
--sl-color-sky-500: hsl(198.6 88.7% 48.4%);
--sl-color-purple-500: hsl(270.7 91% 65.1%);
--sl-color-teal-200: hsl(168.4 83.8% 78.2%);
--sl-input-icon-color-focus: hsl(240 5.2% 33.9%);
--sl-input-icon-color: hsl(240 3.8% 46.1%);
--sl-color-rose-900: hsl(341.5 75.5% 30.4%);
--rb-smart-search-results-pagination-button-border-color: #16433d;
--sl-color-indigo-200: hsl(228 96.5% 88.8%);
--rb-smart-search-results-button-background-color: #16433d;
--sl-color-danger-500: hsl(0 84.2% 60.2%);
--sl-color-violet-600: hsl(262.1 83.3% 57.8%);
--sl-color-fuchsia-50: hsl(289.1 100% 97.8%);
--sl-color-indigo-600: hsl(243.4 75.4% 58.6%);
--sl-input-border-color-hover: hsl(240 5% 64.9%);
--sl-color-danger-700: hsl(0 73.7% 41.8%);
--sl-color-purple-800: hsl(272.9 67.2% 39.4%);
--sl-color-blue-900: hsl(224.4 64.3% 32.9%);
--sl-color-teal-800: hsl(176.1 69.4% 21.8%);
--sl-color-gray-900: hsl(240 5.9% 10%);
--sl-input-filled-background-color: hsl(240 4.8% 95.9%);
--sl-color-pink-800: hsl(335.8 74.4% 35.3%);
--sl-color-orange-950: hsl(15.2 69.1% 19%);
--sl-color-fuchsia-400: hsl(292 91.4% 72.5%);
--sl-color-rose-600: hsl(346.8 77.2% 49.8%);
--rb-widget-option-selected-color: #16433d;
--sl-color-violet-300: hsl(252.5 94.7% 85.1%);
--sl-input-border-radius-small: 0.25rem;
--sl-color-success-50: hsl(138.5 76.5% 96.7%);
--sl-color-gray-500: hsl(240 3.8% 46.1%);
--rb-smart-search-results-product-price-color: #16433d;
--sl-color-emerald-300: hsl(156.2 71.6% 66.9%);
--sl-color-orange-800: hsl(15 79.1% 33.7%);
--sl-color-cyan-100: hsl(185.1 95.9% 90.4%);
--sl-color-indigo-800: hsl(243.7 54.5% 41.4%);
--sl-border-radius-x-large: 1rem;
--sl-color-cyan-500: hsl(188.7 94.5% 42.7%);
--sl-color-yellow-300: hsl(50.4 97.8% 63.5%);
--sl-color-gray-300: hsl(240 4.9% 83.9%);
--sl-tooltip-color: hsl(0, 0%, 100%);
--sl-color-red-950: hsl(0 60% 19.6%);
--sl-color-purple-200: hsl(268.6 100% 91.8%);
--sl-color-purple-600: hsl(271.5 81.3% 55.9%);
--sl-focus-ring-style: solid;
--rb-smart-search-results-content-heading-color: #000;
--sl-color-yellow-600: hsl(40.6 96.1% 40.4%);
--rb-smart-search-results-pagination-button-border-width: 2px;
--sl-color-success-300: hsl(141.7 76.6% 73.1%);
--sl-border-radius-medium: 0.25rem;
--sl-input-color-focus: hsl(240 5.3% 26.1%);
--sl-color-emerald-700: hsl(162.9 93.5% 24.3%);
--sl-color-fuchsia-200: hsl(288.3 95.8% 90.6%);
--rb-smart-collections-pagination-button-border-color: #16433d;
--sl-color-fuchsia-700: hsl(294.7 72.4% 39.8%);
--tw-border-spacing-y: 0;
--sl-color-emerald-950: hsl(164.3 87.5% 9.4%);
--sl-color-gray-800: hsl(240 3.7% 15.9%);
--sl-color-emerald-200: hsl(152.4 76% 80.4%);
--sl-color-sky-100: hsl(204 93.8% 93.7%);
--sl-color-blue-50: hsl(213.8 100% 96.9%);
--sl-color-violet-800: hsl(263.4 69.3% 42.2%);
--sl-color-pink-200: hsl(325.9 84.6% 89.8%);
--sl-color-green-900: hsl(143.8 61.2% 20.2%);
--sl-color-amber-50: hsl(48 100% 96.1%);
--rb-smart-search-results-product-title-color: #16433d;
--sl-color-neutral-900: hsl(240 5.9% 10%);
--sl-color-indigo-50: hsl(225.9 100% 96.7%);
--sl-color-primary-500: hsl(198.6 88.7% 48.4%);
--sl-color-pink-900: hsl(335.9 69% 30.4%);
--sl-color-emerald-500: hsl(160.1 84.1% 39.4%);
--sl-color-blue-100: hsl(214.3 94.6% 92.7%);
--sl-color-neutral-800: hsl(240 3.7% 15.9%);
--sl-color-pink-100: hsl(325.7 77.8% 94.7%);
--rb-smart-collections-reviews-background-color: #E5E5E5;
--sl-color-purple-900: hsl(273.6 65.6% 32%);
--rb-smart-search-results-content-inactive-tab-color: #546b7d;
--sl-color-lime-400: hsl(82.7 78% 55.5%);
--sl-color-fuchsia-100: hsl(287 100% 95.5%);
--rb-smart-search-quick-view-product-price-sale-color: #44BE70;
--sl-color-lime-800: hsl(86.3 69% 22.7%);
--sl-color-orange-400: hsl(27 96% 61%);
--tw-ring-offset-color: #fff;
--sl-color-indigo-400: hsl(234.5 89.5% 73.9%);
--rb-smart-search-quick-view-reviews-background-color: #E5E5E5;
--sl-panel-border-color: hsl(240 5.9% 90%);
--sl-color-purple-100: hsl(268.7 100% 95.5%);
--sl-focus-ring-width: 3px;
--rb-smart-search-results-reviews-text-color: #535353;
--rb-widget-option-border-color: #cccccc;
--sl-color-green-800: hsl(142.8 64.2% 24.1%);
--sl-color-cyan-200: hsl(186.2 93.5% 81.8%);
--sl-color-neutral-400: hsl(240 5% 64.9%);
--sl-color-gray-600: hsl(240 5.2% 33.9%);
--sl-color-lime-700: hsl(85.9 78.4% 27.3%);
--videowise-button-border-radius: 8px;
--sl-color-lime-600: hsl(84.8 85.2% 34.5%);
--sl-color-red-50: hsl(0 85.7% 97.3%);
--sl-color-indigo-300: hsl(229.7 93.5% 81.8%);
--sl-color-warning-100: hsl(48 96.5% 88.8%);
--sl-color-cyan-300: hsl(187 92.4% 69%);
--sl-color-primary-700: hsl(201.3 96.3% 32.2%);
--sl-color-lime-500: hsl(83.7 80.5% 44.3%);
--sl-color-warning-50: hsl(48 100% 96.1%);
--sl-color-warning-800: hsl(22.7 82.5% 31.4%);
--sl-color-indigo-950: hsl(243.5 43.6% 22.9%);
--sl-color-primary-300: hsl(199.4 95.5% 73.9%);
--sl-color-danger-900: hsl(0 62.8% 30.6%);
--sl-color-primary-900: hsl(202 80.3% 23.9%);
--sl-input-help-text-color: hsl(240 3.8% 46.1%);
--sl-color-success-950: hsl(144.3 60.7% 12%);
--sl-color-cyan-950: hsl(196.8 61% 16.1%);
--sl-color-cyan-800: hsl(194.4 69.6% 27.1%);
--sl-input-color-disabled: hsl(240 5.9% 10%);
--sl-color-fuchsia-600: hsl(293.4 69.5% 48.8%);
--sl-input-filled-background-color-disabled: hsl(240 4.8% 95.9%);
--sl-color-pink-500: hsl(330.4 81.2% 60.4%);
--sl-color-blue-300: hsl(211.7 96.4% 78.4%);
--sl-color-green-500: hsl(142.1 70.6% 45.3%);
--sl-color-orange-700: hsl(17.5 88.3% 40.4%);
--sl-tooltip-border-radius: 0.25rem;
--sl-color-purple-950: hsl(276 59.5% 16.5%);
--sl-color-amber-800: hsl(22.7 82.5% 31.4%);
--sl-color-red-300: hsl(0 93.5% 81.8%);
--sl-color-fuchsia-300: hsl(291.1 93.1% 82.9%);
--sl-color-neutral-950: hsl(240 7.3% 8%);
--sl-color-neutral-700: hsl(240 5.3% 26.1%);
--sl-color-rose-200: hsl(352.7 96.1% 90%);
--sl-color-violet-50: hsl(250 100% 97.6%);
--sl-color-orange-600: hsl(20.5 90.2% 48.2%);
--sl-color-red-900: hsl(0 62.8% 30.6%);
--sl-color-danger-800: hsl(0 70% 35.3%);
--sl-color-teal-300: hsl(170.6 76.9% 64.3%);
--sl-color-rose-400: hsl(351.3 94.5% 71.4%);
--sl-color-success-400: hsl(141.9 69.2% 58%);
--sl-color-lime-300: hsl(82 84.5% 67.1%);
--sl-color-violet-200: hsl(250.5 95.2% 91.8%);
--sl-color-cyan-600: hsl(191.6 91.4% 36.5%);
--sl-color-yellow-100: hsl(54.9 96.7% 88%);
--sl-color-purple-50: hsl(270 100% 98%);
--sl-color-red-200: hsl(0 96.3% 89.4%);
--videowise-sale-color: #3cfecf;
--sl-input-focus-ring-color: hsl(198.6 88.7% 48.4% / 40%);
--sl-color-yellow-950: hsl(33.1 69% 13.9%);
--sl-color-neutral-100: hsl(240 4.8% 95.9%);
--sl-color-success-700: hsl(142.4 71.8% 29.2%);
--sl-input-placeholder-color-disabled: hsl(240 5.2% 33.9%);
```

### Spacing

```css
--font-size-mobile-input: 16px;
--font-size-base: 15;
--font-size-header: 26;
--input-padding-top-bottom: 10px;
--input-padding-left-right: 18px;
--input-padding-top-bottom-small: 8px;
--input-padding-left-right-small: 15px;
--section-spacing: 55px;
--section-spacing-small: 35px;
--icon-size: 20px;
--connected-submit-size: calc(var(--icon-size) * 2.5);
--footer-spacing-extra-small: 5px;
--footer-spacing-small: 15px;
--footer-wrapper-spacing: 18px;
--footer-hr-bottom-spacing: 20px;
--footer-spacing-medium: 25px;
--footer-spacing-large: 45px;
--video-button-wrapper-size: 50px;
--video-pause-button-size: 34px;
--video-close-button-size: 30px;
--video-loader-size: 2.875rem;
--sl-letter-spacing-looser: 0.15em;
--sl-spacing-3x-large: 3rem;
--sl-button-font-size-large: 1rem;
--sl-font-size-3x-large: 3rem;
--sl-input-spacing-small: 0.75rem;
--sl-spacing-small: 0.75rem;
--sl-spacing-2x-large: 2.25rem;
--sl-spacing-4x-large: 4.5rem;
--sl-input-help-text-font-size-small: 0.75rem;
--sl-input-label-font-size-small: 0.875rem;
--sl-font-size-4x-large: 4.5rem;
--sl-spacing-medium: 1rem;
--sl-toggle-size-small: 0.875rem;
--sl-spacing-x-large: 1.75rem;
--sl-letter-spacing-dense: -0.015em;
--sl-font-size-x-small: 0.75rem;
--sl-tooltip-font-size: 0.875rem;
--sl-tooltip-padding: 0.25rem 0.5rem;
--sl-letter-spacing-loose: 0.075em;
--sl-input-spacing-large: 1.25rem;
--sl-input-font-size-large: 1.25rem;
--sl-spacing-3x-small: 0.125rem;
--sl-tooltip-arrow-size: 6px;
--sl-input-spacing-medium: 1rem;
--sl-input-help-text-font-size-large: 1rem;
--sl-spacing-x-small: 0.5rem;
--sl-spacing-2x-small: 0.25rem;
--sl-input-help-text-font-size-medium: 0.875rem;
--sl-toggle-size-large: 1.375rem;
--sl-font-size-large: 1.25rem;
--sl-spacing-large: 1.25rem;
--tw-numeric-spacing: ;
--sl-button-font-size-medium: 0.875rem;
--sl-font-size-2x-large: 2.25rem;
--sl-font-size-medium: 1rem;
--sl-input-label-font-size-medium: 1rem;
--sl-button-font-size-small: 0.75rem;
--sl-input-font-size-small: 0.875rem;
--sl-input-label-font-size-large: 1.25rem;
--sl-letter-spacing-normal: normal;
--sl-letter-spacing-denser: -0.03em;
--sl-input-letter-spacing: normal;
--sl-font-size-x-large: 1.5rem;
--sl-font-size-2x-small: 0.625rem;
--sl-toggle-size-medium: 1.125rem;
--sl-font-size-small: 0.875rem;
--sl-input-font-size-medium: 1rem;
```

### Typography

```css
--font-weight-body--bold: 700;
--font-weight-body--bolder: 700;
--font-stack-header: Helvetica, Arial, sans-serif;
--font-style-header: normal;
--font-weight-header: 700;
--font-stack-body: Helvetica, Arial, sans-serif;
--font-style-body: normal;
--font-weight-body: 400;
--font-stack-cart-notification: "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;
--font-h1-desktop: 35;
--font-h1-mobile: 32;
--font-h2-desktop: 20;
--font-h2-mobile: 18;
--font-h3-mobile: 20;
--font-h4-desktop: 17;
--font-h4-mobile: 15;
--font-h4-min-height-mobile: 11;
--font-h5-desktop: 15;
--font-h5-mobile: 13;
--font-h6-desktop: 14;
--font-h6-mobile: 12;
--font-mega-title-large-desktop: 65;
--font-rich-text-large: 17;
--font-rich-text-small: 13;
--z-index-video-text: 3;
--sl-tooltip-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol";
--sl-line-height-normal: 1.8;
--sl-line-height-looser: 2.6;
--sl-tooltip-font-weight: 400;
--sl-input-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol";
--sl-font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol";
--sl-font-weight-bold: 700;
--sl-input-font-weight: 400;
--sl-font-weight-semibold: 500;
--sl-line-height-dense: 1.4;
--sl-tooltip-line-height: 1.4;
--sl-line-height-loose: 2.2;
--sl-font-serif: Georgia, "Times New Roman", serif;
--sl-font-weight-light: 300;
--sl-font-weight-normal: 400;
--sl-line-height-denser: 1;
--sl-font-mono: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
```

### Shadows

```css
--sl-shadow-x-small: 0 1px 2px hsl(240 3.8% 46.1% / 6%);
--sl-shadow-large: 0 2px 8px hsl(240 3.8% 46.1% / 12%);
--tw-drop-shadow: ;
--sl-shadow-medium: 0 2px 4px hsl(240 3.8% 46.1% / 12%);
--sl-shadow-small: 0 1px 2px hsl(240 3.8% 46.1% / 12%);
--sl-shadow-x-large: 0 4px 16px hsl(240 3.8% 46.1% / 12%);
--tw-shadow: 0 0 #0000;
```

### Radii

```css
--rb-smart-collections-button-radius: 25px;
--rb-smart-search-results-button-radius: 25px;
--rb-smart-search-quick-view-button-radius: 25px;
--rb-smart-search-results-pagination-button-radius: 25px;
```

### Other

```css
--opacity-link-hover: 0.6;
--opacity-image-overlay: 0.4;
--hover-overlay-opacity: 0.8;
--predictive-search-focus: #e6e6e6;
--transition-duration-fast: 100ms;
--transition-duration: 250ms;
--transition-duration-slow: 400ms;
--transition-link-hover: var(--transition-duration-fast) cubic-bezier(0.44, 0.13, 0.48, 0.87);
--transition-drawer: all var(--transition-duration-slow) cubic-bezier(0.29, 0.63, 0.44, 1);
--input-group-height: 46px;
--input-group-height-small: 42px;
--width-site: 1200px;
--gutter-site: 55px;
--gutter-site-mobile: 22px;
--z-index-base: 1;
--z-index-dropdown: 7;
--z-index-sub-nav: 8;
--z-index-drawer: 9;
--z-index-mobile-nav: 11;
--z-index-search-bar: 999;
--z-index-predictive-search-wrapper: 1000;
--z-index-skip-to-content: 10000;
--video-height-small: 475px;
--video-height-medium: 650px;
--video-height-large: 775px;
--z-index-video-image: 1;
--z-index-video: 2;
--z-index-video-controls: 4;
--z-index-video-loader: 5;
--ease-transition: cubic-bezier(0.44, 0.13, 0.48, 0.87);
--transition-controls-video: color 0.2s var(--ease-transition), background-color 0.2s var(--ease-transition);
--svg-select-icon: url(//drinkolipop.com/cdn/shop/t/1366/assets/ico-select.svg?v=29003672709104678581773709785);
--slick-img-url: url(//drinkolipop.com/cdn/shop/t/1366/assets/ajax-loader.gif?v=41356863302472015721773709641);
--home-banner-new-wave-url: url("https://cdn.shopify.com/s/files/1/0034/6610/0806/files/home-banner-new-wave.png?v=1623156746");
--home-blue-wave-url: url("https://cdn.shopify.com/s/files/1/0034/6610/0806/files/home-blue-wave.png?v=1773705965");
--story-hero-wave-url: url("https://cdn.shopify.com/s/files/1/0034/6610/0806/files/story-hero-wave.png?v=1773706032");
--story-mission-wave-url: url("https://cdn.shopify.com/s/files/1/0034/6610/0806/files/story-mission-wave.png?v=1773706074");
--home-bluedark-wave-url: url("https://cdn.shopify.com/s/files/1/0034/6610/0806/files/home-bluedark-wave.png?v=1773706124");
--home-yellowdark-wave-url: url("https://cdn.shopify.com/s/files/1/0034/6610/0806/files/home-yellowdark-wave.png?v=1773706165");
--check-symbol-url: url(//drinkolipop.com/cdn/shop/t/1366/assets/check-symbol.svg?v=64434976676356328551773709640);
--arrow-down-green-url: url(//drinkolipop.com/cdn/shop/t/1366/assets/arrow-down-green.svg?v=150330452122212680781773709642);
--arrow-up-white-url: url(//drinkolipop.com/cdn/shop/t/1366/assets/arrow-up-white.svg?v=167673162154222429001773709643);
--arrow-down-white-url: url(//drinkolipop.com/cdn/shop/t/1366/assets/arrow-down-white.svg?v=68322919614181549641773709643);
--wave-image-curve-up-left: url(//drinkolipop.com/cdn/shop/t/1366/assets/wave-image-curve-up-left.svg?v=142377189923728873181773709642);
--wave-image-curve-up-right: url(//drinkolipop.com/cdn/shop/t/1366/assets/wave-image-curve-up-right.svg?v=115639462512050186531773709642);
--sf-z-index-program-widget-modal: 2147483000;
--sl-input-height-small: 1.875rem;
--tw-saturate: ;
--rb-widget-option-selected-background: transparent;
--tw-gradient-to-position: ;
--sl-input-height-medium: 2.5rem;
--sl-input-required-content-offset: -2px;
--sl-input-required-content: "*";
--tw-scale-y: 1;
--tw-pan-x: ;
--sl-z-index-tooltip: 1000;
--sl-transition-x-slow: 1000ms;
--tw-sepia: ;
--tw-hue-rotate: ;
--tw-backdrop-grayscale: ;
--tw-pan-y: ;
--tw-rotate: 0;
--tw-backdrop-hue-rotate: ;
--tw-skew-y: 0;
--tw-slashed-zero: ;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--sl-transition-x-fast: 50ms;
--tw-brightness: ;
--tw-backdrop-brightness: ;
--tw-skew-x: 0;
--videowise-viewport-height: 100%;
--sl-transition-fast: 150ms;
--sl-z-index-toast: 950;
--sl-transition-slow: 500ms;
--tw-gradient-via-position: ;
--tw-grayscale: ;
--tw-pinch-zoom: ;
--sl-input-height-large: 3.125rem;
--tw-backdrop-contrast: ;
--tw-translate-y: 0;
--tw-translate-x: 0;
--header-group-bottom-position: 110px;
--tw-blur: ;
--tw-invert: ;
--tw-backdrop-sepia: ;
--tw-ordinal: ;
--tw-backdrop-invert: ;
--sl-z-index-drawer: 700;
--rb-widget-progress-bar-track: #ececec;
--tw-scroll-snap-strictness: proximity;
--tw-numeric-fraction: ;
--sl-transition-medium: 250ms;
--tw-backdrop-saturate: ;
--rb-widget-option-background: transparent;
--rb-widget-progress-bar-fill: #16433d;
--tw-contrast: ;
--sl-z-index-dropdown: 900;
--tw-backdrop-blur: ;
--videowise-story-title: #000;
--tw-scale-x: 1;
--sl-z-index-dialog: 800;
--rb-smart-collections-pagination-button-background: #16433d;
--tw-numeric-figure: ;
```

### Dependencies

```css
--color-link: --color-body-text;
--transition-link-hover: --transition-duration-fast;
--transition-drawer: --transition-duration-slow;
--color-error-input-text: --color-error;
--connected-submit-size: --icon-size;
--transition-controls-video: --ease-transition,--ease-transition;
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
| xs | 344px | max-width |
| xs | 360px | max-width |
| sm | 440px | min-width |
| sm | 479px | max-width |
| sm | 480px | max-width |
| sm | 481px | min-width |
| sm | 540px | max-width |
| 560px | 560px | max-width |
| 567px | 567px | max-width |
| 569px | 569px | max-width |
| 574px | 574px | max-width |
| 575px | 575px | max-width |
| sm | 576px | max-width |
| sm | 600px | max-width |
| sm | 640px | min-width |
| sm | 650px | min-width |
| md | 709px | max-width |
| md | 710px | min-width |
| md | 749px | max-width |
| md | 750px | min-width |
| md | 760px | max-width |
| md | 761px | min-width |
| md | 767px | max-width |
| md | 768px | max-width |
| md | 811px | min-width |
| 860px | 860px | max-width |
| lg | 960px | min-width |
| lg | 989px | max-width |
| lg | 990px | min-width |
| lg | 991px | max-width |
| lg | 992px | min-width |
| lg | 999px | max-width |
| lg | 1000px | min-width |
| lg | 1023px | min-width |
| lg | 1024px | min-width |
| lg | 1025px | max-width |
| 1152px | 1152px | min-width |
| 1180px | 1180px | min-width |
| 1182px | 1182px | max-width |
| 1183px | 1183px | min-width |
| 1198px | 1198px | min-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | max-width |
| xl | 1225px | max-width |
| xl | 1260px | min-width |
| xl | 1279px | max-width |
| xl | 1280px | min-width |
| xl | 1300px | min-width |
| 1365px | 1365px | max-width |
| 1389px | 1389px | max-width |
| 1400px | 1400px | max-width |
| 1439px | 1439px | max-width |
| 1440px | 1440px | min-width |
| 2xl | 1500px | min-width |
| 2xl | 1536px | min-width |
| 1650px | 1650px | max-width |
| 1920px | 1920px | min-width |
| 1980px | 1980px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.25s`, `0.15s`, `0.3s`, `0.5s`, `0.1s`, `0.2s`, `0.4s`, `0.23s`

### Common Transitions

```css
transition: all;
transition: 0.25s ease-in-out;
transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: margin 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.15s linear;
transition: 0.5s ease-in-out;
transition: opacity 0.1s ease-in-out, visibility 0.1s ease-in-out;
transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: colors 0.2s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

### Keyframe Animations

**fade-in**
```css
@keyframes fade-in {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**slide-rtl**
```css
@keyframes slide-rtl {
  0% { transform: translateX(100%); }
  100% { transform: translateX(0%); }
}
```

**blink**
```css
@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}
```

**shine**
```css
@keyframes shine {
  0% { filter: brightness(1); }
  50% { filter: brightness(1.5); }
  100% { filter: brightness(1); }
}
```

**fly**
```css
@keyframes fly {
  0% { transform: translateY(0px); }
  25% { transform: translateY(-10px); }
  50% { transform: translateY(-20px); }
  75% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}
```

**zoom-in-out**
```css
@keyframes zoom-in-out {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.3); }
}
```

**zoom-out-in**
```css
@keyframes zoom-out-in {
  0%, 100% { transform: scale(1.3); }
  50% { transform: scale(1); }
}
```

**tw-bubble-splode**
```css
@keyframes tw-bubble-splode {
  0% { transform: scale(0.001); opacity: 0; }
  80% { transform: scale(0.9); opacity: 1; }
  100% { transform: scale(0); }
}
```

**tw-bubble-splode**
```css
@keyframes tw-bubble-splode {
  0% { transform: scale(0.001); opacity: 0; }
  80% { transform: scale(0.9); opacity: 1; }
  100% { transform: scale(0); }
}
```

**tw-bubble-circle-scale**
```css
@keyframes tw-bubble-circle-scale {
  0% { transform: scale(0.001); opacity: 1; }
  100% { transform: scale(1.1); opacity: 1; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (131 instances)

```css
.button {
  background-color: rgb(3, 70, 56);
  color: rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 700;
  padding-top: 3px;
  padding-right: 20px;
  border-radius: 50px;
}
```

### Cards (385 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (126 instances)

```css
.input {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  border-color: rgb(0, 0, 0);
  border-radius: 2px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (282 instances)

```css
.link {
  color: rgb(3, 70, 56);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (376 instances)

```css
.navigatio {
  background-color: rgb(255, 251, 245);
  color: rgb(20, 67, 61);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
  box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px;
}
```

### Footer (8 instances)

```css
.foote {
  background-color: rgb(3, 70, 56);
  color: rgb(255, 255, 255);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (13 instances)

```css
.modal {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.07) 8px 0px 32px 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 1280px;
}
```

### Dropdowns (724 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px;
  border-color: rgb(3, 70, 56);
  padding-top: 0px;
}
```

### Badges (5 instances)

```css
.badge {
  color: rgb(3, 70, 56);
  font-size: 16px;
  font-weight: 700;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Tabs (2 instances)

```css
.tab {
  background-color: rgb(152, 225, 195);
  color: rgb(3, 70, 56);
  font-size: 18px;
  font-weight: 400;
  padding-top: 8px;
  padding-right: 16px;
  border-color: rgb(0, 0, 0);
  border-radius: 50px;
}
```

### Accordions (40 instances)

```css
.accordion {
  color: rgb(3, 70, 56);
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(3, 70, 56);
}
```

### ProgressBars (1 instances)

```css
.progressBar {
  background-color: rgb(243, 228, 205);
  color: rgb(20, 67, 61);
  border-radius: 10px;
  font-size: 16px;
}
```

### Switches (23 instances)

```css
.switche {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(20, 67, 61);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(20, 67, 61);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(20, 67, 61);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(20, 67, 61);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px 0px 2px solid rgb(0, 0, 0) rgb(0, 0, 0) rgba(0, 0, 0, 0);
  font-size: 18px;
  font-weight: 700;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(58, 58, 58);
  padding: 10px 11px 10px 11px;
  border-radius: 0px;
  border: 0px none rgb(58, 58, 58);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(58, 58, 58);
  padding: 0px 0px 0px 0px;
  border-radius: 100%;
  border: 0px none rgb(58, 58, 58);
  font-size: 16px;
  font-weight: 400;
```

### Button — 4 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 125);
  color: rgb(3, 70, 56);
  padding: 10px 32px 10px 32px;
  border-radius: 50px;
  border: 0px none rgb(3, 70, 56);
  font-size: 18px;
  font-weight: 700;
```

**Variant 2** (3 instances)

```css
  background: rgb(20, 67, 61);
  color: rgb(255, 247, 229);
  padding: 10px 32px 10px 32px;
  border-radius: 50px;
  border: 0px none rgb(255, 247, 229);
  font-size: 18px;
  font-weight: 700;
```

### Card — 20 instances, 1 variant

**Variant 1** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(20, 67, 61);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(20, 67, 61);
  font-size: 16px;
  font-weight: 400;
```

### Button — 25 instances, 3 variants

**Variant 1** (20 instances)

```css
  background: rgb(3, 70, 56);
  color: rgb(255, 255, 255);
  padding: 3px 20px 1px 20px;
  border-radius: 50px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 700;
```

**Variant 2** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(58, 58, 58);
  padding: 5px 5px 5px 5px;
  border-radius: 0px;
  border: 0px none rgb(20, 67, 61);
  font-size: 16px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgb(255, 255, 125);
  color: rgb(3, 70, 56);
  padding: 10px 32px 10px 32px;
  border-radius: 50px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 18px;
  font-weight: 700;
```

### Card — 20 instances, 1 variant

**Variant 1** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(20, 67, 61);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(20, 67, 61);
  font-size: 16px;
  font-weight: 400;
```

### Button — 20 instances, 1 variant

**Variant 1** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(20, 67, 61);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(20, 67, 61);
  font-size: 16px;
  font-weight: 400;
```

### Button — 11 instances, 2 variants

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(58, 58, 58);
  padding: 0px 0px 0px 0px;
  border-radius: 100%;
  border: 0px none rgb(58, 58, 58);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 1px solid rgb(3, 70, 56);
  font-size: 0px;
  font-weight: 600;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(20, 67, 61);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(20, 67, 61);
  font-size: 16px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 246, 234);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 246, 234);
  font-size: 16px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(3, 70, 56);
  padding: 14px 20px 14px 20px;
  border-radius: 48px;
  border: 0px none rgb(3, 70, 56);
  font-size: 16px;
  font-weight: 700;
```

## Layout System

**45 grid containers** and **820 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 312px | 2px |
| 740px | 0px |
| 1024px | 0px |
| 1440px | 20px |
| 100% | 0px |
| 1280px | 0px |
| 560px | 0px |
| 506px | 0px |
| 540px | 0px |
| 480px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 24x |
| 5-column | 1x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 308px;
grid-template-columns: 308px;
grid-template-columns: 308px;
grid-template-columns: 308px;
grid-template-columns: 308px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 628x |
| column/nowrap | 181x |
| row/wrap | 10x |
| row-reverse/nowrap | 1x |

**Gap values:** `12px`, `16px`, `24px`, `24px 78px`, `27px`, `2px`, `30px`, `4px`, `6px`, `8px`, `normal 6px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 94 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#034638` | 10.84:1 | AAA |
| `#3a3a3a` | `#f0f0f0` | 9.98:1 | AAA |
| `#ffffff` | `#14433d` | 11.05:1 | AAA |
| `#fff7e5` | `#14433d` | 10.36:1 | AAA |
| `#034638` | `#ffff7d` | 10.25:1 | AAA |
| `#034638` | `#98e1c3` | 7.17:1 | AAA |
| `#034638` | `#ffffff` | 10.84:1 | AAA |

## Design System Score

**Overall: 79/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 90/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 9 font families — consider limiting to 2 (heading + body)
- 3060 !important rules — prefer specificity over overrides
- 97% of CSS is unused — consider purging
- 45060 duplicate CSS declarations

## Z-Index Map

**18 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,2147483647 | div.p.r.e.d.i.c.t.i.v.e.-.s.e.a.r.c.h.-.w.r.a.p.p.e.r. .p.r.e.d.i.c.t.i.v.e.-.s.e.a.r.c.h.-.w.r.a.p.p.e.r.-.-.d.r.a.w.e.r, div.d.i.a.l.o.g.-.o.v.e.r.l.a.y, div.d.i.a.l.o.g.-.c.o.n.t.e.n.t. .t.w.-.b.g.-.c.r.e.m.e |
| dropdown | 999,999 | div.s.e.a.r.c.h.-.b.a.r. .d.r.a.w.e.r. .d.r.a.w.e.r.-.-.t.o.p |
| sticky | 10,50 | div.k.e.e.n.-.s.l.i.d.e.r._._.s.l.i.d.e. .t.w.-.r.e.l.a.t.i.v.e. .t.w.-.z.-.1.0. .t.w.-.f.l.e.x. .!.t.w.-.w.-.a.u.t.o. .t.w.-.i.t.e.m.s.-.c.e.n.t.e.r. .t.w.-.j.u.s.t.i.f.y.-.c.e.n.t.e.r. .t.w.-.p.y.-.[.4.p.x.]. .t.w.-.t.e.x.t.-.c.e.n.t.e.r. .t.w.-.t.r.a.n.s.i.t.i.o.n.-.o.p.a.c.i.t.y. .t.w.-.d.u.r.a.t.i.o.n.-.1.5.0. .t.w.-.e.a.s.e.-.l.i.n.e.a.r. .s.m.:.t.w.-.f.l.e.x.-.r.o.w, button.s.i.t.e.-.n.a.v.-.d.r.o.p.d.o.w.n._._.c.a.r.o.u.s.e.l.-.b.t.n. .s.i.t.e.-.n.a.v.-.d.r.o.p.d.o.w.n._._.c.a.r.o.u.s.e.l.-.b.t.n.-.-.p.r.e.v. .s.i.t.e.-.n.a.v.-.d.r.o.p.d.o.w.n._._.c.a.r.o.u.s.e.l.-.b.t.n.-.-.t.o.o.l.b.a.r, button.s.i.t.e.-.n.a.v.-.d.r.o.p.d.o.w.n._._.c.a.r.o.u.s.e.l.-.b.t.n. .s.i.t.e.-.n.a.v.-.d.r.o.p.d.o.w.n._._.c.a.r.o.u.s.e.l.-.b.t.n.-.-.n.e.x.t. .s.i.t.e.-.n.a.v.-.d.r.o.p.d.o.w.n._._.c.a.r.o.u.s.e.l.-.b.t.n.-.-.t.o.o.l.b.a.r |
| base | -100,6 | div, div.l.a.u.n.c.h.U.I.B.u.t.t.o.n. .t.o.p._.l.e.f.t, div.m.o.b.i.l.e.-.m.e.n.u._._.b.a.c.k.d.r.o.p. .t.w.-.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .t.w.-.a.b.s.o.l.u.t.e. .t.w.-.i.n.s.e.t.-.0. .t.w.-.z.-.0. .t.w.-.t.r.a.n.s.i.t.i.o.n.-.o.p.a.c.i.t.y. .t.w.-.d.u.r.a.t.i.o.n.-.3.0.0. .t.w.-.e.a.s.e.-.o.u.t |

**Issues:**
- [object Object]

## SVG Icons

**117 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 101 |
| md | 11 |
| lg | 2 |
| xl | 3 |

**Icon colors:** `#034638`, `white`, `rgb(0, 0, 0)`, `#FFF6EA`, `rgb(255, 255, 255)`, `currentColor`, `#14433D`, `#444`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Ano | self-hosted | 900, bold, normal | normal |
| WindsorEF | self-hosted | 900, bold | normal |
| SF-Primary-Font | self-hosted | 100 300, 400 500, 600 900 | normal |
| SF-Secondary-Font | self-hosted | 100 300, 400 500, 600 900 | normal |
| Font Awesome 5 Pro | self-hosted | 300, 400, 900 | normal |
| Open Sans | google-fonts | 400, 500, 600, 700 | normal |
| Poppins | google-fonts | 400, 500, 600, 700 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Open+Sans:wght@400;500;600;700&display=swap`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 23 | objectFit: contain, borderRadius: 0px, shape: square |
| thumbnail | 12 | objectFit: contain, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (25x), 3:4 (6x), 2.91:1 (1x), 5.5:1 (1x), 6.38:1 (1x), 2:3 (1x)

## Motion Language

**Feel:** springy · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **ease-in-out** (438 uses) — `ease`
- **custom** (171 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`, `cubic-bezier(0.65, 0.05, 0.36, 1)`
- **linear** (1 uses) — `linear`
- **ease-out** (2 uses) — `cubic-bezier(0, 0, 0.2, 1)`, `cubic-bezier(0.29, 0.63, 0.44, 1)`
- **spring** (1 uses) — `cubic-bezier(0.18, 0.89, 0.32, 1.28)`

### Spring / Overshoot Easings

- `cubic-bezier(0.18, 0.89, 0.32, 1.28)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `fade-in` | fade | opacity | 1 |

## Component Anatomy

### button — 70 instances

**Slots:** label, icon
**Variants:** outline
**Sizes:** md · lg · sm

| variant | count | sample label |
|---|---|---|
| default | 50 | Skip to content
Accessibility Statement
 |
| outline | 20 | Add 12 Pack |

### card — 40 instances

**Slots:** media

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **add** (20)
- **shop** (3)
- **find** (2)
- **ship** (1)
- **learn** (1)
- **what's** (1)
- **subscribe** (1)

### Button Copy Patterns

- "add 12 pack" (20×)
- "find your flavor" (2×)
- "skip to content
accessibility statement

$3.99 flat rate shipping • orders $50+ ship free

shop
 
learn
 
subscribe
find a store
log in
the feel
good soda

real" (1×)
- "learn" (1×)
- "shop now" (1×)
- "shop 9g fiber" (1×)
- "shop 6g fiber" (1×)
- "what's in olipop?" (1×)
- "subscribe" (1×)

### Sample Headings

> 
                      
                        Shop 9g fiber
                      
                    
> 
                      
                        Shop 6g fiber
                      
                    
> 
                      
                        Shop MINIs
                      
                    
> 
                      
                        Shop limited edition flavors
                      
                    
> 
                      
                        Shop 9g fiber
                      
                    
> 
                      
                        Shop 6g fiber
                      
                    
> 
                      
                        Shop MINIs
                      
                    
> 
                      
                        Shop limited edition flavors
                      
                    
> 
                      
                        Shop 9g fiber
                      
                    
> 
                      
                        Shop 6g fiber
                      
                    

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Discover a new kind of soda made with plant fiber and prebiotics. Non-GMO, gluten-free, paleo, and vegan, with high fiber and 2-5g of sugar. Enjoy a variety of delicious, refreshing and classic flavor

Alternates: legal (0.4)

## Section Roles

Reading order (top→bottom): nav → pricing-table → sidebar → nav → nav → nav → nav → nav → nav → nav → nav → nav → nav → nav → footer → content → nav → nav → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | pricing-table | — | 0.9 |
| 2 | nav | — | 0.4 |
| 3 | nav | — | 0.9 |
| 4 | nav | — | 0.9 |
| 5 | sidebar | — | 0.4 |
| 6 | nav | — | 0.9 |
| 7 | nav | 
                      
                        Shop 9g fiber
                   | 0.4 |
| 8 | nav | 
                      
                        Shop 6g fiber
                   | 0.4 |
| 9 | nav | 
                      
                        Shop MINIs
                      | 0.4 |
| 10 | nav | 
                      
                        Shop limited edition flavors
    | 0.4 |
| 11 | nav | 
                      
                        Shop variety packs
              | 0.4 |
| 12 | nav | — | 0.4 |
| 13 | nav | — | 0.4 |
| 14 | footer | Sign up to get 15% off your first order | 0.95 |
| 15 | content | — | 0.3 |
| 16 | nav | — | 0.9 |
| 17 | nav | — | 0.9 |
| 18 | nav | — | 0.9 |

## Material Language

**Label:** `material-you` (confidence 0.45)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.305 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.343)
**Counts:** total 35, svg 0, icon 1, screenshot-like 0, photo-like 22
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Ano` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
