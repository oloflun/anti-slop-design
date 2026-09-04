# Design Language: Bumble | Date, Chat & Meet New People

> Extracted from `https://bumble.com` on September 4, 2026
> 1604 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ffdb5b` | rgb(255, 219, 91) | hsl(47, 100%, 68%) | 8 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 2 |
| Accent | `#fff386` | rgb(255, 243, 134) | hsl(54, 100%, 76%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#202020` | hsl(0, 0%, 13%) | 2489 |
| `#575656` | hsl(0, 1%, 34%) | 350 |
| `#343333` | hsl(0, 1%, 20%) | 276 |
| `#ffffff` | hsl(0, 0%, 100%) | 83 |
| `#f3f3f3` | hsl(0, 0%, 95%) | 1 |

### Background Colors

Used on large-area elements: `#ffdb5b`, `#ffffff`, `#f3f3f3`, `#fcfcfc`, `#fff386`

### Text Colors

Text color palette: `#343333`, `#202020`, `#ffffff`, `#0000ee`, `#3b3b3b`, `#575656`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#202020` | text, border, background | 2489 |
| `#575656` | text, border | 350 |
| `#343333` | text, border | 276 |
| `#ffffff` | text, border, background | 83 |
| `#ffdb5b` | background | 8 |
| `#0000ee` | text, border | 2 |
| `#f3f3f3` | background | 1 |
| `#fff386` | background | 1 |

## Typography

### Font Families

- **BumbleSans** — used for all (1604 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 68px | 4.25rem | 600 | 70px | 0.46px | h2 |
| 49px | 3.0625rem | 600 | 55px | 0.42px | div, blockquote, br |
| 40px | 2.5rem | 400 | 40px | normal | div |
| 34px | 2.125rem | 600 | 34px | 0.4px | h3, div |
| 32px | 2rem | 700 | 48px | normal | h1, div, span, svg |
| 24px | 1.5rem | 400 | 24px | normal | div, h2 |
| 20px | 1.25rem | 400 | 25px | 0.32px | p, br, span, div |
| 18px | 1.125rem | 500 | 21.6px | normal | span |
| 17px | 1.0625rem | 500 | 20px | 0.3px | button, a, span |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, link |
| 15px | 0.9375rem | 400 | 20px | 0.3px | p, span |

### Heading Scale

```css
h2 { font-size: 68px; font-weight: 600; line-height: 70px; }
h3 { font-size: 34px; font-weight: 600; line-height: 34px; }
h1 { font-size: 32px; font-weight: 700; line-height: 48px; }
h2 { font-size: 24px; font-weight: 400; line-height: 24px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: 24px; }
```

### Font Weights in Use

`400` (1442x), `500` (139x), `700` (14x), `600` (9x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-6 | 6px | 0.375rem |
| spacing-20 | 20px | 1.25rem |
| spacing-32 | 32px | 2rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-60 | 60px | 3.75rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 9px | 3 |
| lg | 16px | 19 |
| xl | 24px | 6 |
| full | 1000px | 3 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0) 0px 0px 0px 0px;
```

**md** — blur: 8px
```css
box-shadow: rgba(32, 32, 32, 0.12) 0px 1px 8px 0px;
```

## CSS Custom Properties

### Colors

```css
--token-a11y-focus-ring-inner-color: #ffc629;
--token-a11y-focus-ring-inner-offset: -3px;
--token-a11y-focus-ring-inner-width: 2px;
--token-a11y-focus-ring-outer-color: #ffc629;
--token-a11y-focus-ring-outer-offset: 2px;
--token-a11y-focus-ring-outer-width: 1px;
--token-action-cell-border-radius: 16px;
--token-action-cell-border-width: 1px;
--token-action-cell-extra-color-fill: #6b6b6b;
--token-action-cell-primary-color-background: #f6f6f6;
--token-action-cell-primary-color-background-selected: #fff7de;
--token-action-cell-primary-hint-color: #6b6b6b;
--token-action-cell-primary-title-color: #141414;
--token-action-cell-secondary-color-background: #fff;
--token-action-cell-secondary-color-background-selected: #fff7de;
--token-action-cell-secondary-color-border: #dcdcdc;
--token-action-cell-secondary-color-border-selected: #fff;
--token-action-cell-secondary-hint-color: #6b6b6b;
--token-action-cell-secondary-title-color: #141414;
--token-actionsheet-header-background-primary: #ffc629;
--token-actionsheet-item-border-color: #dcdcdc;
--token-actionsheet-item-border-width: 1px;
--token-actionsheet-item-color-destructive: #cd2e0f;
--token-actionsheet-item-color-generic: #141414;
--token-brick-border-radius-circle: 50%;
--token-brick-border-radius-squared: 16%;
--token-button-color-semi-transparent-white-opacity: .3;
--token-button-medium-border-radius: 24px;
--token-button-primary-background-color-on-brand: #fff;
--token-button-primary-background-color-on-light: #ffc629;
--token-button-primary-text-color-on-brand: #141414;
--token-button-primary-text-color-on-light: #141414;
--token-button-secondary-background-color-on-brand: #ffd95c;
--token-button-secondary-background-color-on-light: #f6f6f6;
--token-button-secondary-text-color-on-brand: #141414;
--token-button-secondary-text-color-on-light: #141414;
--token-button-small-border-radius: 20px;
--token-button-status-pressed-overlay-dark-background-color: #000;
--token-button-tertiary-background-color-on-brand: #00000000;
--token-button-tertiary-background-color-on-light: #00000000;
--token-button-tertiary-text-color-on-brand: #141414;
--token-button-tertiary-text-color-on-light: #141414;
--token-chat-bubble-base-background-color: #fff;
--token-chat-bubble-border-color: #dcdcdc;
--token-chat-bubble-in-background-color: #f6f6f6;
--token-chat-bubble-in-text-color: #141414;
--token-chat-bubble-out-background-color: #ffc629;
--token-chat-bubble-out-text-color: #141414;
--token-chat-composer-action-active-color: #ffc629;
--token-chat-composer-action-base-color: #6b6b6b;
--token-chat-composer-action-disabled-color: #dcdcdc;
--token-chat-composer-mini-base-border-color: #dcdcdc;
--token-chat-composer-mini-base-border-width: 1px;
--token-chat-composer-mini-focused-border-color: #141414;
--token-chat-composer-mini-focused-border-width: 1px;
--token-chat-date-pill-elevated-background-color: #fff;
--token-chat-date-pill-elevated-outer-border-color: #dcdcdc;
--token-chat-date-pill-elevated-outer-border-opacity: .04;
--token-chat-date-pill-elevated-outer-border-size: 1px;
--token-chat-date-pill-elevated-shadow-color: #000;
--token-chat-date-pill-text-color: #6b6b6b;
--token-chat-input-message-background-color: #fff;
--token-chat-input-message-border-color: #dcdcdc;
--token-chat-input-message-content-color: #141414;
--token-chat-input-message-focused-border-color: #141414;
--token-chat-input-message-placeholder-color: #6b6b6b;
--token-chat-input-search-background-color: #f6f6f6;
--token-chat-input-search-border-color: #f6f6f6;
--token-chat-input-search-content-color: #141414;
--token-chat-input-search-icon-color: #6b6b6b;
--token-chat-input-search-placeholder-color: #6b6b6b;
--token-chat-item-group-avatar-border-radius: 16px;
--token-chat-item-status-color-base: #6b6b6b;
--token-chat-item-status-color-error: #cd2e0f;
--token-chat-item-status-color-info: #6b6b6b;
--token-chat-message-reaction-question-preview-background-color: #ffedb3;
--token-chat-panel-pills-item-background-color: #fff;
--token-chat-panel-pills-item-background-color-active: #f6f6f6;
--token-chat-panel-pills-item-border-radius: 8px;
--token-chat-panel-pills-item-content-color: #6b6b6b;
--token-chat-panel-pills-item-content-color-active: #141414;
--token-chat-preview-message-media-shape-circle-border-radius: 50%;
--token-chat-preview-message-media-shape-squared-border-radius: 4px;
--token-chat-preview-message-quote-decoration-in-background-color: #ffc629;
--token-chat-preview-message-quote-decoration-out-background-color: #141414;
--token-chat-scroll-to-bottom-icon-color: #6b6b6b;
--token-chat-scroll-to-bottom-outer-border-opacity: .04;
--token-chat-scroll-to-bottom-outer-border-size: 1px;
--token-chat-scroll-to-bottom-shadow-color: #000;
--token-choice-base-checked-background-color-on-brand: #141414;
--token-choice-base-checked-background-color-on-light: #141414;
--token-choice-base-checked-foreground-color-on-brand: #fff;
--token-choice-base-checked-foreground-color-on-light: #ffc629;
--token-choice-base-unchecked-background-color-on-brand: #ffffff00;
--token-choice-base-unchecked-background-color-on-light: #ffffff00;
--token-choice-base-unchecked-foreground-color-on-brand: #fff;
--token-choice-base-unchecked-foreground-color-on-light: #949494;
--token-choice-border-radius-checkbox: 6px;
--token-choice-border-radius-radio: 12px;
--token-choice-error-checked-background-color: #fff;
--token-choice-error-checked-foreground-color: #cd2e0f;
--token-choice-error-unchecked-background-color: #fff;
--token-choice-error-unchecked-foreground-color: #cd2e0f;
--token-color-black: #141414;
--token-color-feature-bantr-ted-lasso-blue: #0b6cf9;
--token-color-feature-bantr-ted-lasso-blue-dark: #0052ca;
--token-color-feature-bff: #009abf;
--token-color-feature-bizz: #ff6c37;
--token-color-feature-boost: #35e2bd;
--token-color-feature-boost-gradient-start: #35e2bd;
--token-color-feature-boost-gradient-stop: #3fa7cd;
--token-color-feature-boost-light: #ebfcf8;
--token-color-feature-gold-gradient-start: #a4eeff;
--token-color-feature-gold-gradient-stop: #eba5ff;
--token-color-feature-icebreaker: #ffc629;
--token-color-feature-icebreaker-alt: #141414;
--token-color-feature-netflix: #1d252c;
--token-color-feature-nightin-gradient-start: #f0b000;
--token-color-feature-nightin-gradient-stop: #ff94a9;
--token-color-feature-payment-promo: #1f98f9;
--token-color-feature-premium-alt: #141414;
--token-color-feature-premium-alt-gradient-start: #494949;
--token-color-feature-premium-alt-gradient-stop: #0d0d0d;
--token-color-feature-premium-gradient-start: #ffda60;
--token-color-feature-premium-gradient-stop: #ffc60a;
--token-color-feature-safety: #1f98f9;
--token-color-feature-safety-dark: #197ac7;
--token-color-feature-safety-light: #e9f5ff;
--token-color-feature-spotlight: #b377c7;
--token-color-feature-spotlight-gradient-start: #e87b80;
--token-color-feature-spotlight-gradient-stop: #a175de;
--token-color-feature-spotlight-light: #fcebee;
--token-color-feature-sunshine-horizontal-gradient-mid: #ffe605;
--token-color-feature-sunshine-horizontal-gradient-start: #fff091;
--token-color-feature-sunshine-horizontal-gradient-stop: #ffc629;
--token-color-feature-sunshine-main-gradient-start: #ffe600;
--token-color-feature-sunshine-main-gradient-stop: #fff2b3;
--token-color-feature-superswipe: #f5ba4a;
--token-color-feature-superswipe-gradient-start: #ffda60;
--token-color-feature-superswipe-gradient-stop: #ffc60a;
--token-color-feature-superswipe-light: #fdf0e0;
--token-color-generic-blue: #1f98f9;
--token-color-generic-blue-light: #e9f5ff;
--token-color-generic-green: #1a964a;
--token-color-generic-red: #cd2e0f;
--token-color-gray-10: #f6f6f6;
--token-color-gray-30: #ededed;
--token-color-gray-50: #dcdcdc;
--token-color-gray-70: #949494;
--token-color-gray-90: #6b6b6b;
--token-color-primary: #ffc629;
--token-color-primary-dark: #de9e24;
--token-color-primary-gradient-start: #ffd95c;
--token-color-primary-gradient-stop: #ffc629;
--token-color-primary-light: #ffedb3;
--token-color-primary-lighter: #fff7de;
--token-color-provider-apple: #000;
--token-color-provider-facebook: #1778f2;
--token-color-provider-google: #dc4a3d;
--token-color-provider-instagram: #d93175;
--token-color-provider-linkedin: #0076b7;
--token-color-provider-odnoklassniki: #ff8201;
--token-color-provider-spotify: #1db954;
--token-color-provider-twitter: #1ab0ff;
--token-color-provider-vkontakte: #507299;
--token-color-status-error: #cd2e0f;
--token-color-status-notification: #cd2e0f;
--token-color-status-positive: #1a964a;
--token-color-white: #fff;
--token-cosmos-actionbadge-border-radius: 12px;
--token-cosmos-actionbadge-border-width-default: 1px;
--token-cosmos-actionbadge-border-width-selected: 1px;
--token-cosmos-actionbadge-color-background-default: #fff;
--token-cosmos-actionbadge-color-background-overlay-hover: #2020200d;
--token-cosmos-actionbadge-color-background-overlay-pressed: #2020201a;
--token-cosmos-actionbadge-color-background-selected: #ffdb5b;
--token-cosmos-actionbadge-color-border-default: #2020201f;
--token-cosmos-actionbadge-color-border-selected: #2020201f;
--token-cosmos-actionbadge-color-content-default: #202020;
--token-cosmos-actionbadge-color-content-selected: #202020;
--token-cosmos-actionbadge-color-icon-default: #202020;
--token-cosmos-actionbadge-color-icon-selected: #202020;
--token-cosmos-actioncard-border-radius: 16px;
--token-cosmos-actioncard-border-width-accent: .5px;
--token-cosmos-actioncard-border-width-primary: .5px;
--token-cosmos-actioncard-border-width-secondary: .5px;
--token-cosmos-actioncard-border-width-tertiary: 1px;
--token-cosmos-actioncard-color-background-accent: #ffdb5b;
--token-cosmos-actioncard-color-background-overlay-hover: #2020200d;
--token-cosmos-actioncard-color-background-overlay-pressed: #2020201a;
--token-cosmos-actioncard-color-background-primary: #fff;
--token-cosmos-actioncard-color-background-secondary: #f3f3f3;
--token-cosmos-actioncard-color-background-tertiary: #fff;
--token-cosmos-actioncard-color-border-accent: #20202014;
--token-cosmos-actioncard-color-border-primary: #20202014;
--token-cosmos-actioncard-color-border-secondary: #20202014;
--token-cosmos-actioncard-color-border-tertiary: #2020201f;
--token-cosmos-actioncard-color-description-accent: #575656;
--token-cosmos-actioncard-color-description-primary: #575656;
--token-cosmos-actioncard-color-description-secondary: #575656;
--token-cosmos-actioncard-color-description-tertiary: #575656;
--token-cosmos-actioncard-color-icon-accent: #202020;
--token-cosmos-actioncard-color-icon-navigation: #777676;
--token-cosmos-actioncard-color-icon-primary: #202020;
--token-cosmos-actioncard-color-icon-secondary: #202020;
--token-cosmos-actioncard-color-icon-tertiary: #202020;
--token-cosmos-actioncard-color-title-accent: #202020;
--token-cosmos-actioncard-color-title-primary: #202020;
--token-cosmos-actioncard-color-title-secondary: #202020;
--token-cosmos-actioncard-color-title-tertiary: #202020;
--token-cosmos-actioncard-shadow-high-blur: 24px;
--token-cosmos-actioncard-shadow-high-color: #20202033;
--token-cosmos-actioncard-shadow-high-spread: 0px;
--token-cosmos-actioncard-shadow-high-x: 0px;
--token-cosmos-actioncard-shadow-high-y: 1px;
--token-cosmos-actioncard-shadow-low-blur: 8px;
--token-cosmos-actioncard-shadow-low-color: #2020201f;
--token-cosmos-actioncard-shadow-low-spread: 0px;
--token-cosmos-actioncard-shadow-low-x: 0px;
--token-cosmos-actioncard-shadow-low-y: 1px;
--token-cosmos-actioncard-shadow-medium-blur: 12px;
--token-cosmos-actioncard-shadow-medium-color: #20202033;
--token-cosmos-actioncard-shadow-medium-spread: 0px;
--token-cosmos-actioncard-shadow-medium-x: 0px;
--token-cosmos-actioncard-shadow-medium-y: 1px;
--token-cosmos-actioncard-sizing-icon-end: 16px;
--token-cosmos-actioncard-sizing-icon-start-medium: 40px;
--token-cosmos-actioncard-sizing-icon-start-small: 24px;
--token-cosmos-actioncard-spacing-gap-horizontal: 12px;
--token-cosmos-actioncard-spacing-gap-vertical: 2px;
--token-cosmos-actioncard-spacing-horizontal: 16px;
--token-cosmos-actioncard-spacing-vertical: 16px;
--token-cosmos-actioncard-typography-description: p3;
--token-cosmos-actioncard-typography-title: title;
--token-cosmos-actioncell-border-radius: 16px;
--token-cosmos-actioncell-border-width-default: .5px;
--token-cosmos-actioncell-border-width-error: .5px;
--token-cosmos-actioncell-border-width-selected: .5px;
--token-cosmos-actioncell-color-background-default: #f3f3f3;
--token-cosmos-actioncell-color-background-error: #f3f3f3;
--token-cosmos-actioncell-color-background-overlay-hover: #2020200d;
--token-cosmos-actioncell-color-background-overlay-pressed: #2020201a;
--token-cosmos-actioncell-color-background-selected: #ffdb5b;
--token-cosmos-actioncell-color-border-default: #20202014;
--token-cosmos-actioncell-color-border-error: #20202014;
--token-cosmos-actioncell-color-border-selected: #20202014;
--token-cosmos-actioncell-color-content-default: #202020;
--token-cosmos-actioncell-color-content-error: #202020;
--token-cosmos-actioncell-color-content-selected: #202020;
--token-cosmos-actioncell-color-icon: #202020;
--token-cosmos-actionrow-color-background-default: #ffffff00;
--token-cosmos-actionrow-color-background-overlay-hover: #2020200d;
--token-cosmos-actionrow-color-background-overlay-pressed: #2020201a;
--token-cosmos-actionrow-color-chevron: #777676;
--token-cosmos-actionrow-color-description: #575656;
--token-cosmos-actionrow-color-icon-end: #202020;
--token-cosmos-actionrow-color-icon-start: #202020;
--token-cosmos-actionrow-color-label: #202020;
--token-cosmos-actionrow-color-title: #202020;
--token-cosmos-actionsheet-border-radius-rounded: 36px;
--token-cosmos-actionsheet-border-radius-squared: 0px;
--token-cosmos-actionsheet-color-background-backdrop: #20202099;
--token-cosmos-actionsheet-color-background-container: #fff;
--token-cosmos-actionsheet-color-background-media: #fff;
--token-cosmos-actionsheet-shadow-container-color: #20202033;
--token-cosmos-avatar-color-background: #f3f3f3;
--token-cosmos-avatar-color-icon: #dcdcdc;
--token-cosmos-badge-border-radius: 1000px;
--token-cosmos-badge-border-width-alt: .5px;
--token-cosmos-badge-color-background-solid-alt: #fff;
--token-cosmos-badge-color-background-solid-brand: #ffdb5b;
--token-cosmos-badge-color-background-solid-default: #f3f3f3;
--token-cosmos-badge-color-background-solid-highlight: #ffdb5b;
--token-cosmos-badge-color-background-solid-inverse: #202020;
--token-cosmos-badge-color-background-transparent-alt: #ffffffcc;
--token-cosmos-badge-color-background-transparent-brand: #ffdb5b80;
--token-cosmos-badge-color-background-transparent-default: #f3f3f3e6;
--token-cosmos-badge-color-background-transparent-highlight: #ffdb5b80;
--token-cosmos-badge-color-background-transparent-inverse: #202020b3;
--token-cosmos-badge-color-border-alt: #20202014;
--token-cosmos-badge-color-content-solid-alt: #202020;
--token-cosmos-badge-color-content-solid-brand: #202020;
--token-cosmos-badge-color-content-solid-default: #202020;
--token-cosmos-badge-color-content-solid-highlight: #202020;
--token-cosmos-badge-color-content-solid-inverse: #fff;
--token-cosmos-badge-color-content-transparent-alt: #202020;
--token-cosmos-badge-color-content-transparent-brand: #202020;
--token-cosmos-badge-color-content-transparent-default: #202020;
--token-cosmos-badge-color-content-transparent-highlight: #202020;
--token-cosmos-badge-color-content-transparent-inverse: #fff;
--token-cosmos-badge-color-icon-solid-alt: #202020;
--token-cosmos-badge-color-icon-solid-brand: #202020;
--token-cosmos-badge-color-icon-solid-default: #202020;
--token-cosmos-badge-color-icon-solid-highlight: #202020;
--token-cosmos-badge-color-icon-solid-inverse: #fff;
--token-cosmos-badge-color-icon-transparent-alt: #202020;
--token-cosmos-badge-color-icon-transparent-brand: #202020;
--token-cosmos-badge-color-icon-transparent-default: #202020;
--token-cosmos-badge-color-icon-transparent-highlight: #202020;
--token-cosmos-badge-color-icon-transparent-inverse: #fff;
--token-cosmos-brick-border-radius-large: 12px;
--token-cosmos-brick-border-radius-medium: 10px;
--token-cosmos-brick-border-radius-rounded: 1000px;
--token-cosmos-brick-border-radius-small: 8px;
--token-cosmos-brick-border-radius-xlarge: 16px;
--token-cosmos-brick-border-radius-xsmall: 8px;
--token-cosmos-brick-color-icon: #fff;
--token-cosmos-brick-color-overlay: #20202080;
--token-cosmos-button-border-radius-medium: 16px;
--token-cosmos-button-border-radius-micro: 8px;
--token-cosmos-button-border-radius-mini: 10px;
--token-cosmos-button-border-radius-small: 12px;
--token-cosmos-button-border-width-primary-default: 0px;
--token-cosmos-button-border-width-primary-destructive: 0px;
--token-cosmos-button-border-width-primary-inverse: 0px;
--token-cosmos-button-border-width-secondary-default: 1px;
--token-cosmos-button-border-width-secondary-destructive: 1px;
--token-cosmos-button-border-width-secondary-inverse: 1px;
--token-cosmos-button-border-width-tertiary-default: 0px;
--token-cosmos-button-border-width-tertiary-destructive: 0px;
--token-cosmos-button-border-width-tertiary-inverse: 0px;
--token-cosmos-button-color-background-overlay-base-hover: #2020200d;
--token-cosmos-button-color-background-overlay-base-pressed: #2020201a;
--token-cosmos-button-color-background-overlay-inverse-hover: #ffffff0d;
--token-cosmos-button-color-background-overlay-inverse-pressed: #ffffff1a;
--token-cosmos-button-color-background-primary-default: #202020;
--token-cosmos-button-color-background-primary-destructive: #cd2e0f;
--token-cosmos-button-color-background-primary-inverse: #fff;
--token-cosmos-button-color-background-secondary-default: #ffffff00;
--token-cosmos-button-color-background-secondary-destructive: #ffffff00;
--token-cosmos-button-color-background-secondary-inverse: #ffffff00;
--token-cosmos-button-color-background-tertiary-default: #ffffff00;
--token-cosmos-button-color-background-tertiary-destructive: #ffffff00;
--token-cosmos-button-color-background-tertiary-inverse: #ffffff00;
--token-cosmos-button-color-border-primary-default: #2020201f;
--token-cosmos-button-color-border-primary-destructive: #cd2e0f;
--token-cosmos-button-color-border-primary-inverse: #2020201f;
--token-cosmos-button-color-border-secondary-default: #202020;
--token-cosmos-button-color-border-secondary-destructive: #cd2e0f;
--token-cosmos-button-color-border-secondary-inverse: #fff;
--token-cosmos-button-color-border-tertiary-default: #2020201f;
--token-cosmos-button-color-border-tertiary-destructive: #cd2e0f;
--token-cosmos-button-color-border-tertiary-inverse: #2020201f;
--token-cosmos-button-color-content-primary-default: #fff;
--token-cosmos-button-color-content-primary-destructive: #fff;
--token-cosmos-button-color-content-primary-inverse: #202020;
--token-cosmos-button-color-content-secondary-default: #202020;
--token-cosmos-button-color-content-secondary-destructive: #cd2e0f;
--token-cosmos-button-color-content-secondary-inverse: #fff;
--token-cosmos-button-color-content-tertiary-default: #202020;
--token-cosmos-button-color-content-tertiary-destructive: #cd2e0f;
--token-cosmos-button-color-content-tertiary-inverse: #fff;
--token-cosmos-button-color-icon-primary-default: #fff;
--token-cosmos-button-color-icon-primary-destructive: #fff;
--token-cosmos-button-color-icon-primary-inverse: #202020;
--token-cosmos-button-color-icon-secondary-default: #202020;
--token-cosmos-button-color-icon-secondary-destructive: #cd2e0f;
--token-cosmos-button-color-icon-secondary-inverse: #fff;
--token-cosmos-button-color-icon-tertiary-default: #202020;
--token-cosmos-button-color-icon-tertiary-destructive: #cd2e0f;
--token-cosmos-button-color-icon-tertiary-inverse: #fff;
--token-cosmos-card-border-radius: 16px;
--token-cosmos-card-border-width-accent: 1px;
--token-cosmos-card-border-width-primary: .5px;
--token-cosmos-card-border-width-secondary: .5px;
--token-cosmos-card-border-width-tertiary: 1px;
--token-cosmos-card-color-background-accent-default: #ffdb5b;
--token-cosmos-card-color-background-accent-transparent: #ffdb5b80;
--token-cosmos-card-color-background-primary-default: #fff;
--token-cosmos-card-color-background-primary-transparent: #202020b3;
--token-cosmos-card-color-background-secondary-default: #f3f3f3;
--token-cosmos-card-color-background-secondary-transparent: #f3f3f3e6;
--token-cosmos-card-color-background-tertiary-default: #fff;
--token-cosmos-card-color-background-tertiary-transparent: #ffffffcc;
--token-cosmos-card-color-border-accent: #2020201f;
--token-cosmos-card-color-border-primary: #20202014;
--token-cosmos-card-color-border-secondary: #20202014;
--token-cosmos-card-color-border-tertiary: #2020201f;
--token-cosmos-card-shadow-primary-blur: 8px;
--token-cosmos-card-shadow-primary-color: #2020201f;
--token-cosmos-card-shadow-primary-spread: 0px;
--token-cosmos-card-shadow-primary-x: 0px;
--token-cosmos-card-shadow-primary-y: 1px;
--token-cosmos-card-sizing-background-blur-accent: 20px;
--token-cosmos-card-sizing-background-blur-primary: 20px;
--token-cosmos-card-sizing-background-blur-secondary: 20px;
--token-cosmos-card-sizing-background-blur-tertiary: 40px;
--token-cosmos-card-spacing-horizontal-medium: 16px;
--token-cosmos-card-spacing-horizontal-small: 12px;
--token-cosmos-card-spacing-vertical-medium: 16px;
--token-cosmos-card-spacing-vertical-small: 12px;
--token-cosmos-carousel-color-background: #fff;
--token-cosmos-carousel-color-icon-foreground: #202020;
--token-cosmos-checkbox-border-radius: 8px;
--token-cosmos-checkbox-border-width-default-error: 2px;
--token-cosmos-checkbox-border-width-default-selected: 0px;
--token-cosmos-checkbox-border-width-default-unselected: 2px;
--token-cosmos-checkbox-border-width-inverse-error: 2px;
--token-cosmos-checkbox-border-width-inverse-selected: 0px;
--token-cosmos-checkbox-border-width-inverse-unselected: 2px;
--token-cosmos-checkbox-color-background-default-error: #fff;
--token-cosmos-checkbox-color-background-default-selected: #202020;
--token-cosmos-checkbox-color-background-default-unselected: #fff;
--token-cosmos-checkbox-color-background-inverse-error: #202020;
--token-cosmos-checkbox-color-background-inverse-selected: #fff;
--token-cosmos-checkbox-color-background-inverse-unselected: #202020;
--token-cosmos-checkbox-color-border-default-error: #cd2e0f;
--token-cosmos-checkbox-color-border-default-selected: #202020;
--token-cosmos-checkbox-color-border-default-unselected: #202020;
--token-cosmos-checkbox-color-border-inverse-error: #cd2e0f;
--token-cosmos-checkbox-color-border-inverse-selected: #fff;
--token-cosmos-checkbox-color-border-inverse-unselected: #fff;
--token-cosmos-checkbox-color-icon-default-error: #fff;
--token-cosmos-checkbox-color-icon-default-selected: #fff;
--token-cosmos-checkbox-color-icon-default-unselected: #fff;
--token-cosmos-checkbox-color-icon-inverse-error: #202020;
--token-cosmos-checkbox-color-icon-inverse-selected: #202020;
--token-cosmos-checkbox-color-icon-inverse-unselected: #202020;
--token-cosmos-ctabox-color-content-description: #575656;
--token-cosmos-ctabox-color-content-hint: #575656;
--token-cosmos-ctabox-color-content-title: #202020;
--token-cosmos-divider-border-width-interactive: 1px;
--token-cosmos-divider-border-width-supportive: .5px;
--token-cosmos-divider-color-border-interactive: #2020201f;
--token-cosmos-divider-color-border-supportive: #20202014;
--token-cosmos-dotcounternotification-border-radius: 1000px;
--token-cosmos-dotcounternotification-border-width-default: 2px;
--token-cosmos-dotcounternotification-border-width-none: 0px;
--token-cosmos-dotcounternotification-color-background: #cd2e0f;
--token-cosmos-dotcounternotification-color-border-default: #fff;
--token-cosmos-dotcounternotification-color-border-none: #fff;
--token-cosmos-dotcounternotification-color-content: #fff;
--token-cosmos-emptystate-color-description: #575656;
--token-cosmos-emptystate-color-title: #202020;
--token-cosmos-filters-border-radius: 10px;
--token-cosmos-filters-border-width-default: 1px;
--token-cosmos-filters-border-width-selected: 1px;
--token-cosmos-filters-color-background-default: #fff;
--token-cosmos-filters-color-background-overlay-hover: #2020200d;
--token-cosmos-filters-color-background-overlay-pressed: #2020201a;
--token-cosmos-filters-color-background-selected: #ffdb5b;
--token-cosmos-filters-color-border-default: #2020201f;
--token-cosmos-filters-color-border-selected: #2020201f;
--token-cosmos-filters-color-content-default: #202020;
--token-cosmos-filters-color-content-selected: #202020;
--token-cosmos-filters-color-icon-default: #202020;
--token-cosmos-filters-color-icon-selected: #202020;
--token-cosmos-forms-border-radius-rounded: 16px;
--token-cosmos-forms-border-radius-squared: 0px;
--token-cosmos-forms-border-width-error: 1px;
--token-cosmos-forms-border-width-focus: 2px;
--token-cosmos-forms-border-width-resting: 1px;
--token-cosmos-forms-border-width-success: 1px;
--token-cosmos-forms-color-background-default: #fff;
--token-cosmos-forms-color-background-focus: #fff;
--token-cosmos-forms-color-bar: #777676;
--token-cosmos-forms-color-border-error: #cd2e0f;
--token-cosmos-forms-color-border-focus: #202020;
--token-cosmos-forms-color-border-resting: #20202080;
--token-cosmos-forms-color-border-success: #0a6947;
--token-cosmos-forms-color-content-action: #202020;
--token-cosmos-forms-color-content-counter-default: #202020;
--token-cosmos-forms-color-content-counter-error: #cd2e0f;
--token-cosmos-forms-color-content-counter-success: #0a6947;
--token-cosmos-forms-color-content-label: #202020;
--token-cosmos-forms-color-content-optional: #575656;
--token-cosmos-forms-color-content-placeholder: #202020;
--token-cosmos-forms-color-content-prefix: #202020;
--token-cosmos-forms-color-content-sufix: #202020;
--token-cosmos-forms-color-icon-default: #202020;
--token-cosmos-forms-color-item-background-default: #ffffff00;
--token-cosmos-forms-color-item-background-selected: #f3f3f3;
--token-cosmos-forms-color-item-content: #202020;
--token-cosmos-forms-color-item-icon: #202020;
--token-cosmos-helpertext-color-content-default: #575656;
--token-cosmos-helpertext-color-content-error: #cd2e0f;
--token-cosmos-helpertext-color-content-success: #0a6947;
--token-cosmos-helpertext-color-icon-default: #777676;
--token-cosmos-helpertext-color-icon-error: #cd2e0f;
--token-cosmos-helpertext-color-icon-success: #0a6947;
--token-cosmos-iconbutton-border-radius-large: 12px;
--token-cosmos-iconbutton-border-radius-medium: 12px;
--token-cosmos-iconbutton-border-radius-small: 10px;
--token-cosmos-iconbutton-border-radius-xlarge: 16px;
--token-cosmos-iconbutton-border-width-accent: 1px;
--token-cosmos-iconbutton-border-width-outline: 1px;
--token-cosmos-iconbutton-color-background-default-accent: #ffdb5b;
--token-cosmos-iconbutton-color-background-default-inverse: #ffffff00;
--token-cosmos-iconbutton-color-background-default-layered: #202020b3;
--token-cosmos-iconbutton-color-background-default-outline: #fff;
--token-cosmos-iconbutton-color-background-default-solid: #fff;
--token-cosmos-iconbutton-color-background-default-transparent: #ffffff00;
--token-cosmos-iconbutton-color-background-disabled-accent: #dcdcdc;
--token-cosmos-iconbutton-color-background-disabled-inverse: #ffffff00;
--token-cosmos-iconbutton-color-background-disabled-layered: #dcdcdc;
--token-cosmos-iconbutton-color-background-disabled-outline: #fff;
--token-cosmos-iconbutton-color-background-disabled-solid: #fff;
--token-cosmos-iconbutton-color-background-disabled-transparent: #ffffff00;
--token-cosmos-iconbutton-color-border-accent: #2020201f;
--token-cosmos-iconbutton-color-border-outline: #2020201f;
--token-cosmos-iconbutton-color-icon-default-accent: #202020;
--token-cosmos-iconbutton-color-icon-default-inverse: #fff;
--token-cosmos-iconbutton-color-icon-default-layered: #fff;
--token-cosmos-iconbutton-color-icon-default-outline: #202020;
--token-cosmos-iconbutton-color-icon-default-solid: #202020;
--token-cosmos-iconbutton-color-icon-default-transparent: #202020;
--token-cosmos-iconbutton-color-icon-disabled-accent: #fff;
--token-cosmos-iconbutton-color-icon-disabled-inverse: #dcdcdc;
--token-cosmos-iconbutton-color-icon-disabled-layered: #fff;
--token-cosmos-iconbutton-color-icon-disabled-outline: #dcdcdc;
--token-cosmos-iconbutton-color-icon-disabled-solid: #dcdcdc;
--token-cosmos-iconbutton-color-icon-disabled-transparent: #dcdcdc;
--token-cosmos-iconbutton-color-reactive-default-hover: #2020200d;
--token-cosmos-iconbutton-color-reactive-default-pressed: #2020201a;
--token-cosmos-iconbutton-color-reactive-inverse-hover: #ffffff0d;
--token-cosmos-iconbutton-color-reactive-inverse-pressed: #ffffff1a;
--token-cosmos-inappnotification-border-radius: 24px;
--token-cosmos-inappnotification-border-width: .5px;
--token-cosmos-inappnotification-color-background: #fff;
--token-cosmos-inappnotification-color-border: #20202014;
--token-cosmos-inappnotification-color-icon-default: #fff;
--token-cosmos-inappnotification-color-icon-negative-background: #cd2e0f;
--token-cosmos-inappnotification-color-icon-negative-foreground: #fff;
--token-cosmos-inappnotification-color-icon-positive-background: #0a6947;
--token-cosmos-inappnotification-color-icon-positive-foreground: #fff;
--token-cosmos-inappnotification-color-text: #202020;
--token-cosmos-inappnotification-color-title: #202020;
--token-cosmos-inappnotification-color-underlay-end: #ffffff00;
--token-cosmos-inappnotification-color-underlay-start: #20202099;
--token-cosmos-inappnotification-shadow-color: #20202033;
--token-cosmos-mark-border-radius: 1000px;
--token-cosmos-mark-border-width-default: 0px;
--token-cosmos-mark-border-width-inverse: 1px;
--token-cosmos-mark-box-shadow-default-color: #ffffff00;
--token-cosmos-mark-box-shadow-floating-color: #2020201f;
--token-cosmos-mark-color-background-default: #cd2e0f;
--token-cosmos-mark-color-background-inverse: #fff;
--token-cosmos-mark-color-border-default: #2020201f;
--token-cosmos-mark-color-border-inverse: #2020201f;
--token-cosmos-mark-color-icon-default: #fff;
--token-cosmos-mark-color-icon-inverse: #202020;
--token-cosmos-mark-color-text-default: #fff;
--token-cosmos-mark-color-text-inverse: #202020;
--token-cosmos-menu-color-background-default: #ffffff00;
--token-cosmos-menu-color-background-overlay-hover: #2020200d;
--token-cosmos-menu-color-background-overlay-pressed: #2020201a;
--token-cosmos-menu-color-content: #202020;
--token-cosmos-menu-color-icon: #202020;
--token-cosmos-menu-shadow-color: #20202033;
--token-cosmos-modal-border-radius: 24px;
--token-cosmos-modal-color-background-backdrop: #20202099;
--token-cosmos-modal-color-background-container: #fff;
--token-cosmos-navigationbar-color-action-default: #202020;
--token-cosmos-navigationbar-color-action-disabled: #dcdcdc;
--token-cosmos-navigationbar-color-background-default: #fff;
--token-cosmos-navigationbar-color-background-transparent: #ffffff00;
--token-cosmos-navigationbar-color-description-default: #575656;
--token-cosmos-navigationbar-color-icon-default-background: #fff;
--token-cosmos-navigationbar-color-icon-default-foreground: #202020;
--token-cosmos-navigationbar-color-logo: #202020;
--token-cosmos-navigationbar-color-title-default: #202020;
--token-cosmos-nudge-border-radius: 24px;
--token-cosmos-nudge-color-background-default: #f3f3f3;
--token-cosmos-nudge-color-description-default: #575656;
--token-cosmos-nudge-color-hint: #575656;
--token-cosmos-nudge-color-title: #202020;
--token-cosmos-paginationdots-border-radius-default: 1000px;
--token-cosmos-paginationdots-color-background-default-selected: #202020;
--token-cosmos-paginationdots-color-background-default-unselected: #202020;
--token-cosmos-paginationdots-color-background-inverse-selected: #fff;
--token-cosmos-paginationdots-color-background-inverse-unselected: #fff;
--token-cosmos-profilecard-border-radius: 16px;
--token-cosmos-profilecard-border-width-default: .5px;
--token-cosmos-profilecard-color-background-default: #fff;
--token-cosmos-profilecard-color-badge: #202020;
--token-cosmos-profilecard-color-border-default: #20202014;
--token-cosmos-profilecard-color-gradient-end: #1e1e1e80;
--token-cosmos-profilecard-color-gradient-start: #ffffff00;
--token-cosmos-profilecard-color-icon-default: #202020;
--token-cosmos-profilecard-color-icon-inverse: #fff;
--token-cosmos-profilecard-color-title: #202020;
--token-cosmos-profilecard-shadow-blur: 8px;
--token-cosmos-profilecard-shadow-color: #2020201f;
--token-cosmos-profilecard-shadow-spread: 0px;
--token-cosmos-profilecard-shadow-x: 0px;
--token-cosmos-profilecard-shadow-y: 1px;
--token-cosmos-profilecard-sizing-badge: 16px;
--token-cosmos-profilecard-spacing-gap-horizontal-medium: 8px;
--token-cosmos-profilecard-spacing-gap-horizontal-small: 0px;
--token-cosmos-profilecard-spacing-gap-vertical-medium: 8px;
--token-cosmos-profilecard-spacing-gap-vertical-small: 0px;
--token-cosmos-profilecard-spacing-horizontal-left: 16px;
--token-cosmos-profilecard-spacing-horizontal-right-medium: 16px;
--token-cosmos-profilecard-spacing-horizontal-right-small: 4px;
--token-cosmos-profilecard-spacing-vertical-bottom: 4px;
--token-cosmos-profilecard-spacing-vertical-top: 16px;
--token-cosmos-profilecard-typography-title: title;
--token-cosmos-progressbar-border-radius: 1000px;
--token-cosmos-progressbar-color-background-default: #202020;
--token-cosmos-progressbar-color-background-inverse: #fff;
--token-cosmos-progressbar-color-indicator-default: #202020;
--token-cosmos-progressbar-color-indicator-inverse: #fff;
--token-cosmos-progresscircle-border-radius: 1000px;
--token-cosmos-progresscircle-color-background-default: #202020;
--token-cosmos-progresscircle-color-background-inverse: #fff;
--token-cosmos-progresscircle-color-indicator-default: #202020;
--token-cosmos-progresscircle-color-indicator-inverse: #fff;
--token-cosmos-radiobutton-border-radius: 1000px;
--token-cosmos-radiobutton-border-width-default-error: 2px;
--token-cosmos-radiobutton-border-width-default-selected: 0px;
--token-cosmos-radiobutton-border-width-default-unselected: 2px;
--token-cosmos-radiobutton-border-width-inverse-error: 2px;
--token-cosmos-radiobutton-border-width-inverse-selected: 0px;
--token-cosmos-radiobutton-border-width-inverse-unselected: 2px;
--token-cosmos-radiobutton-color-background-default-error: #fff;
--token-cosmos-radiobutton-color-background-default-selected: #202020;
--token-cosmos-radiobutton-color-background-default-unselected: #fff;
--token-cosmos-radiobutton-color-background-inverse-error: #202020;
--token-cosmos-radiobutton-color-background-inverse-selected: #fff;
--token-cosmos-radiobutton-color-background-inverse-unselected: #202020;
--token-cosmos-radiobutton-color-border-default-error: #cd2e0f;
--token-cosmos-radiobutton-color-border-default-selected: #202020;
--token-cosmos-radiobutton-color-border-default-unselected: #202020;
--token-cosmos-radiobutton-color-border-inverse-error: #cd2e0f;
--token-cosmos-radiobutton-color-border-inverse-selected: #fff;
--token-cosmos-radiobutton-color-border-inverse-unselected: #fff;
--token-cosmos-radiobutton-color-icon-default-error: #fff;
--token-cosmos-radiobutton-color-icon-default-selected: #fff;
--token-cosmos-radiobutton-color-icon-default-unselected: #fff;
--token-cosmos-radiobutton-color-icon-inverse-error: #202020;
--token-cosmos-radiobutton-color-icon-inverse-selected: #202020;
--token-cosmos-radiobutton-color-icon-inverse-unselected: #202020;
--token-cosmos-search-border-radius: 16px;
--token-cosmos-search-border-width-default: .5px;
--token-cosmos-search-border-width-filled: .5px;
--token-cosmos-search-color-background-default: #f3f3f3;
--token-cosmos-search-color-border-default: #20202014;
--token-cosmos-search-color-border-filled: #20202014;
--token-cosmos-search-color-content-default: #575656;
--token-cosmos-search-color-content-filled: #202020;
--token-cosmos-search-color-icon-left: #202020;
--token-cosmos-search-color-icon-right: #202020;
--token-cosmos-semantic-border-radius-0: 0px;
--token-cosmos-semantic-border-radius-10: 10px;
--token-cosmos-semantic-border-radius-12: 12px;
--token-cosmos-semantic-border-radius-16: 16px;
--token-cosmos-semantic-border-radius-19: 19px;
--token-cosmos-semantic-border-radius-24: 24px;
--token-cosmos-semantic-border-radius-32: 32px;
--token-cosmos-semantic-border-radius-4: 4px;
--token-cosmos-semantic-border-radius-8: 8px;
--token-cosmos-semantic-border-radius-full: 1000px;
--token-cosmos-semantic-border-radius-level-0: 24px;
--token-cosmos-semantic-border-radius-level-1: 16px;
--token-cosmos-semantic-border-radius-level-1-large: 20px;
--token-cosmos-semantic-border-radius-level-1-small: 12px;
--token-cosmos-semantic-border-radius-level-2: 10px;
--token-cosmos-semantic-border-radius-level-3: 8px;
--token-cosmos-semantic-border-radius-none: 0px;
--token-cosmos-semantic-border-width-focus: 2px;
--token-cosmos-semantic-border-width-interactive: 1px;
--token-cosmos-semantic-border-width-none: 0px;
--token-cosmos-semantic-border-width-resting: 1px;
--token-cosmos-semantic-border-width-supportive: .5px;
--token-cosmos-semantic-border-width-thick: 2px;
--token-cosmos-semantic-border-width-thin: 1px;
--token-cosmos-semantic-color-border-default: #2020201f;
--token-cosmos-semantic-color-border-focus: #202020;
--token-cosmos-semantic-color-border-interactive: #2020201f;
--token-cosmos-semantic-color-border-inverse: #fff;
--token-cosmos-semantic-color-border-resting: #20202080;
--token-cosmos-semantic-color-border-selected: #202020;
--token-cosmos-semantic-color-border-strong: #202020;
--token-cosmos-semantic-color-border-subtle: #20202014;
--token-cosmos-semantic-color-border-supportive: #20202014;
--token-cosmos-semantic-color-container-backgrounds-accent-default: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-accent-transparent: #ffdb5b80;
--token-cosmos-semantic-color-container-backgrounds-brand: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-brand-2: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-brand-3: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-brand-4: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-brand-5: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-brand-primary: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-brand-secondary: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-default: #fff;
--token-cosmos-semantic-color-container-backgrounds-disabled: #dcdcdc;
--token-cosmos-semantic-color-container-backgrounds-inverse: #202020;
--token-cosmos-semantic-color-container-backgrounds-layered-transparent: #20202080;
--token-cosmos-semantic-color-container-backgrounds-overlay-bottom-gradient-end: #20202080;
--token-cosmos-semantic-color-container-backgrounds-overlay-bottom-gradient-start: #ffffff00;
--token-cosmos-semantic-color-container-backgrounds-primary-default: #fff;
--token-cosmos-semantic-color-container-backgrounds-primary-transparent: #202020b3;
--token-cosmos-semantic-color-container-backgrounds-secondary-default: #f3f3f3;
--token-cosmos-semantic-color-container-backgrounds-secondary-transparent: #f3f3f3e6;
--token-cosmos-semantic-color-container-backgrounds-selected: #ffdb5b;
--token-cosmos-semantic-color-container-backgrounds-subtle: #f3f3f3;
--token-cosmos-semantic-color-container-backgrounds-subtle-2: #f3f3f3;
--token-cosmos-semantic-color-container-backgrounds-subtle-3: #f3f3f3;
--token-cosmos-semantic-color-container-backgrounds-tertiary-default: #fff;
--token-cosmos-semantic-color-container-backgrounds-tertiary-transparent: #ffffffcc;
--token-cosmos-semantic-color-container-backgrounds-transparent: #ffffff00;
--token-cosmos-semantic-color-features-bff: #ffde3b;
--token-cosmos-semantic-color-features-bizz: #fe6c37;
--token-cosmos-semantic-color-features-boost: #fffa7f;
--token-cosmos-semantic-color-features-bumble: #ffdb5b;
--token-cosmos-semantic-color-features-compliment: #ffd232;
--token-cosmos-semantic-color-features-premium: #ffeb01;
--token-cosmos-semantic-color-features-premium-plus: #fbca00;
--token-cosmos-semantic-color-features-safety: #202020;
--token-cosmos-semantic-color-features-safety-subtle: #fff;
--token-cosmos-semantic-color-features-spotlight: #ffd232;
--token-cosmos-semantic-color-features-superswipe: #ffd232;
--token-cosmos-semantic-color-features-travel: #202020;
--token-cosmos-semantic-color-features-travel-subtle: #fff;
--token-cosmos-semantic-color-generic-red: #cd2e0f;
--token-cosmos-semantic-color-icon-brand: #ffdb5b;
--token-cosmos-semantic-color-icon-default: #202020;
--token-cosmos-semantic-color-icon-disabled: #dcdcdc;
--token-cosmos-semantic-color-icon-inverse: #fff;
--token-cosmos-semantic-color-icon-selected: #202020;
--token-cosmos-semantic-color-icon-subtle: #777676;
--token-cosmos-semantic-color-page-backgrounds-brand: #ffdb5b;
--token-cosmos-semantic-color-page-backgrounds-brand-2: #ffdb5b;
--token-cosmos-semantic-color-page-backgrounds-brand-3: #ffdb5b;
--token-cosmos-semantic-color-page-backgrounds-brand-4: #ffdb5b;
--token-cosmos-semantic-color-page-backgrounds-brand-5: #ffdb5b;
--token-cosmos-semantic-color-page-backgrounds-default: #fff;
--token-cosmos-semantic-color-page-backgrounds-overlay: #20202099;
--token-cosmos-semantic-color-page-backgrounds-overlay-gradient-end: #ffffff00;
--token-cosmos-semantic-color-page-backgrounds-overlay-gradient-start: #20202080;
--token-cosmos-semantic-color-page-backgrounds-strong: #202020;
--token-cosmos-semantic-color-page-backgrounds-subtle: #f7f7f7;
--token-cosmos-semantic-color-reactive-default-hover: #2020200d;
--token-cosmos-semantic-color-reactive-default-pressed: #2020201a;
--token-cosmos-semantic-color-reactive-inverse-hover: #ffffff0d;
--token-cosmos-semantic-color-reactive-inverse-pressed: #ffffff1a;
--token-cosmos-semantic-color-socials-apple: #000;
--token-cosmos-semantic-color-socials-facebook: #1672e9;
--token-cosmos-semantic-color-socials-google: #fff;
--token-cosmos-semantic-color-socials-instagram: #e4405f;
--token-cosmos-semantic-color-socials-linkedin: #0076b7;
--token-cosmos-semantic-color-socials-netflix: #1d252c;
--token-cosmos-semantic-color-socials-odnoklassniki: #ff8201;
--token-cosmos-semantic-color-socials-spotify: #1db954;
--token-cosmos-semantic-color-socials-twitter: #1ab0ff;
--token-cosmos-semantic-color-socials-vkontakte: #507299;
--token-cosmos-semantic-color-supportive-feedback-alert: #ffc629;
--token-cosmos-semantic-color-supportive-feedback-error: #cd2e0f;
--token-cosmos-semantic-color-supportive-feedback-notification: #cd2e0f;
--token-cosmos-semantic-color-supportive-feedback-success: #0a6947;
--token-cosmos-semantic-color-text-brand: #202020;
--token-cosmos-semantic-color-text-default: #202020;
--token-cosmos-semantic-color-text-disabled: #dcdcdc;
--token-cosmos-semantic-color-text-error: #cd2e0f;
--token-cosmos-semantic-color-text-inverse: #fff;
--token-cosmos-semantic-color-text-links: #202020;
--token-cosmos-semantic-color-text-positive: #0a6947;
--token-cosmos-semantic-color-text-subdued: #575656;
--token-cosmos-semantic-shadows-floating-color: #20202033;
--token-cosmos-semantic-shadows-floating-elevation-1-color: #20202033;
--token-cosmos-semantic-shadows-floating-elevation-2-color: #20202033;
--token-cosmos-semantic-shadows-in-line-color: #2020201f;
--token-cosmos-semantic-shadows-none-color: #ffffff00;
--token-cosmos-semantic-shadows-overlay-color: #20202033;
--token-cosmos-semantic-shadows-static-elevation-1-color: #2020201f;
--token-cosmos-semantic-shadows-static-elevation-2-color: #2020201f;
--token-cosmos-semantic-sizing-blur-accent: 20px;
--token-cosmos-semantic-sizing-blur-primary: 20px;
--token-cosmos-semantic-sizing-blur-secondary: 20px;
--token-cosmos-snackpill-border-radius: 8px;
--token-cosmos-snackpill-box-shadow-color: #20202033;
--token-cosmos-snackpill-color-background-default: #202020;
--token-cosmos-snackpill-color-background-inverse: #fff;
--token-cosmos-snackpill-color-icon-default: #fff;
--token-cosmos-snackpill-color-icon-inverse: #202020;
--token-cosmos-snackpill-color-text-default: #fff;
--token-cosmos-snackpill-color-text-inverse: #202020;
--token-cosmos-socialmediabutton-border-width-google: 1px;
--token-cosmos-socialmediabutton-color-background-apple: #000;
--token-cosmos-socialmediabutton-color-background-facebook: #1672e9;
--token-cosmos-socialmediabutton-color-background-google: #fff;
--token-cosmos-socialmediabutton-color-background-instagram: #e4405f;
--token-cosmos-socialmediabutton-color-border-google: #dadce0;
--token-cosmos-socialmediabutton-color-content-default: #fff;
--token-cosmos-socialmediabutton-color-content-inverse: #202020;
--token-cosmos-socialmediabutton-color-icon-default: #fff;
--token-cosmos-socialmediabutton-color-icon-inverse: #202020;
--token-cosmos-socialmediabutton-color-overlay-hover-apple: #1c1c1e;
--token-cosmos-socialmediabutton-color-overlay-hover-facebook: #166fe5;
--token-cosmos-socialmediabutton-color-overlay-hover-google: #f8f9fa;
--token-cosmos-socialmediabutton-color-overlay-hover-instagram: #e22b4a;
--token-cosmos-socialmediabutton-color-overlay-pressed-apple: #333;
--token-cosmos-socialmediabutton-color-overlay-pressed-facebook: #1546a6;
--token-cosmos-socialmediabutton-color-overlay-pressed-google: #f1f3f4;
--token-cosmos-socialmediabutton-color-overlay-pressed-instagram: #e11b3c;
--token-cosmos-tabbar-color-background: #fff;
--token-cosmos-tabbar-color-icon-default: #777676;
--token-cosmos-tabbar-color-icon-selected: #202020;
--token-cosmos-tabbar-color-text-default: #575656;
--token-cosmos-tabbar-color-text-selected: #202020;
--token-cosmos-tabs-border-width-default-selected: 2px;
--token-cosmos-tabs-border-width-default-unselected: 1px;
--token-cosmos-tabs-border-width-inverse-selected: 2px;
--token-cosmos-tabs-border-width-inverse-unselected: 1px;
--token-cosmos-tabs-color-background-default: #ffffff00;
--token-cosmos-tabs-color-background-inverse: #ffffff00;
--token-cosmos-tabs-color-border-default-selected: #202020;
--token-cosmos-tabs-color-border-default-unselected: #20202014;
--token-cosmos-tabs-color-border-inverse-selected: #fff;
--token-cosmos-tabs-color-border-inverse-unselected: #fff;
--token-cosmos-tabs-color-icon-default-default: #777676;
--token-cosmos-tabs-color-icon-default-selected: #202020;
--token-cosmos-tabs-color-icon-inverse-default: #fff;
--token-cosmos-tabs-color-icon-inverse-selected: #fff;
--token-cosmos-tabs-color-text-default-selected: #202020;
--token-cosmos-tabs-color-text-default-unselected: #575656;
--token-cosmos-tabs-color-text-inverse-selected: #fff;
--token-cosmos-tabs-color-text-inverse-unselected: #fff;
--token-cosmos-textbutton-color-content-default: #202020;
--token-cosmos-textbutton-color-content-inverse: #fff;
--token-cosmos-textbutton-color-icon-default: #777676;
--token-cosmos-textbutton-color-icon-inverse: #fff;
--token-cosmos-tip-border-radius-medium: 16px;
--token-cosmos-tip-border-radius-small: 0px;
--token-cosmos-tip-border-width-primary-floating: .5px;
--token-cosmos-tip-border-width-primary-inline: .5px;
--token-cosmos-tip-border-width-secondary-floating: .5px;
--token-cosmos-tip-border-width-secondary-inline: .5px;
--token-cosmos-tip-color-background-primary-floating: #202020b3;
--token-cosmos-tip-color-background-primary-inline: #fff;
--token-cosmos-tip-color-background-primary-sticky: #202020b3;
--token-cosmos-tip-color-background-secondary-floating: #f3f3f3e6;
--token-cosmos-tip-color-background-secondary-inline: #f3f3f3;
--token-cosmos-tip-color-background-secondary-sticky: #f3f3f3e6;
--token-cosmos-tip-color-border-primary-floating: #20202014;
--token-cosmos-tip-color-border-primary-inline: #20202014;
--token-cosmos-tip-color-border-secondary-floating: #20202014;
--token-cosmos-tip-color-border-secondary-inline: #20202014;
--token-cosmos-tip-color-description-primary-floating: #fff;
--token-cosmos-tip-color-description-primary-inline: #575656;
--token-cosmos-tip-color-description-primary-sticky: #fff;
--token-cosmos-tip-color-description-secondary-floating: #575656;
--token-cosmos-tip-color-description-secondary-inline: #575656;
--token-cosmos-tip-color-description-secondary-sticky: #575656;
--token-cosmos-tip-color-icon-primary-floating: #fff;
--token-cosmos-tip-color-icon-primary-inline: #202020;
--token-cosmos-tip-color-icon-primary-sticky: #fff;
--token-cosmos-tip-color-icon-secondary-floating: #202020;
--token-cosmos-tip-color-icon-secondary-inline: #202020;
--token-cosmos-tip-color-icon-secondary-sticky: #202020;
--token-cosmos-tip-color-reactive-default-hover: #2020200d;
--token-cosmos-tip-color-reactive-default-pressed: #2020201a;
--token-cosmos-tip-color-reactive-inverse-hover: #ffffff0d;
--token-cosmos-tip-color-reactive-inverse-pressed: #ffffff1a;
--token-cosmos-tip-color-title-primary-floating: #fff;
--token-cosmos-tip-color-title-primary-inline: #202020;
--token-cosmos-tip-color-title-primary-sticky: #fff;
--token-cosmos-tip-color-title-secondary-floating: #202020;
--token-cosmos-tip-color-title-secondary-inline: #202020;
--token-cosmos-tip-color-title-secondary-sticky: #202020;
--token-cosmos-tip-shadow-floating-color: #20202033;
--token-cosmos-tip-shadow-inline-color: #2020201f;
--token-cosmos-tip-shadow-none-color: #ffffff00;
--token-cosmos-tip-sizing-background-blur-primary-floating: 20px;
--token-cosmos-tip-sizing-background-blur-primary-sticky: 20px;
--token-cosmos-tip-sizing-background-blur-secondary-floating: 20px;
--token-cosmos-tip-sizing-background-blur-secondary-sticky: 20px;
--token-cosmos-toggle-border-radius: 1000px;
--token-cosmos-toggle-border-width-default-selected: 2px;
--token-cosmos-toggle-border-width-default-unselected: 2px;
--token-cosmos-toggle-border-width-inverse-selected: 2px;
--token-cosmos-toggle-border-width-inverse-unselected: 2px;
--token-cosmos-toggle-color-background-default-selected: #202020;
--token-cosmos-toggle-color-background-default-unselected: #fff;
--token-cosmos-toggle-color-background-inverse-selected: #fff;
--token-cosmos-toggle-color-background-inverse-unselected: #202020;
--token-cosmos-toggle-color-border-default-selected: #202020;
--token-cosmos-toggle-color-border-default-unselected: #202020;
--token-cosmos-toggle-color-border-inverse-selected: #fff;
--token-cosmos-toggle-color-border-inverse-unselected: #fff;
--token-cosmos-toggle-color-handle-default-selected: #fff;
--token-cosmos-toggle-color-handle-default-unselected: #202020;
--token-cosmos-toggle-color-handle-inverse-selected: #202020;
--token-cosmos-toggle-color-handle-inverse-unselected: #fff;
--token-cosmos-tooltip-border-radius: 12px;
--token-cosmos-tooltip-color-background: #202020;
--token-cosmos-tooltip-color-content: #fff;
--token-dotcounternotification-counter-outer-border-width: 2px;
--token-dotcounternotification-dot-outer-border-width: 2px;
--token-form-label-color: #6b6b6b;
--token-form-note-color-error: #cd2e0f;
--token-form-note-color-hint: #6b6b6b;
--token-form-note-color-success: #1a964a;
--token-generic-accent-color-on-brand: #fff;
--token-generic-accent-color-on-light: #ffc629;
--token-generic-accent-front-color-on-brand: #141414;
--token-generic-accent-front-color-on-light: #141414;
--token-generic-default-color-on-brand: #141414;
--token-generic-default-color-on-light: #141414;
--token-generic-inactive-color-on-brand: #0000004c;
--token-generic-inactive-color-on-light: #dcdcdc;
--token-icon-accent-background-color-on-brand: #fff;
--token-icon-accent-background-color-on-light: #ffc629;
--token-icon-accent-color-on-brand: #fff;
--token-icon-accent-color-on-light: #ffc629;
--token-icon-accent-foreground-color-on-brand: #141414;
--token-icon-accent-foreground-color-on-light: #141414;
--token-icon-default-background-color-on-brand: #141414;
--token-icon-default-background-color-on-light: #141414;
--token-icon-default-color-on-brand: #141414;
--token-icon-default-color-on-light: #141414;
--token-icon-default-foreground-color-on-brand: #fff;
--token-icon-default-foreground-color-on-light: #fff;
--token-inappnotification-background-color: #fff;
--token-inappnotification-badge-border-color: #fff;
--token-inappnotification-badge-border-width: 2px;
--token-inappnotification-border-color: #000;
--token-inappnotification-border-opacity: .03;
--token-inappnotification-border-radius: 16px;
--token-inappnotification-border-width: 1px;
--token-inappnotification-content-icon-color: #6b6b6b;
--token-inappnotification-content-text-color: #141414;
--token-inappnotification-shadow-color: #000;
--token-input-choice-color-base-selected: #ffc629;
--token-input-choice-color-base-unselected: #dcdcdc;
--token-input-toggle-color-base-selected: #ffc629;
--token-input-toggle-color-base-unselected: #dcdcdc;
--token-interest-medium-border-radius: 18px;
--token-interest-medium-border-width: 1px;
--token-interest-small-border-radius: 15px;
--token-interest-small-border-width: 1px;
--token-interest-text-color-base: #141414;
--token-lifestylebadge-background-color: #ffedb3;
--token-lifestylebadge-base-color-background: #ffedb3;
--token-lifestylebadge-base-color-border: #00000000;
--token-lifestylebadge-base-color-text: #141414;
--token-lifestylebadge-border-radius: 15px;
--token-lifestylebadge-border-width: 1px;
--token-lifestylebadge-mode-bff-background-color: #bce5ea;
--token-lifestylebadge-mode-bff-text-color: #141414;
--token-lifestylebadge-mode-bizz-background-color: #f9c8b8;
--token-lifestylebadge-mode-bizz-text-color: #141414;
--token-lifestylebadge-mode-dating-background-color: #ffedb4;
--token-lifestylebadge-mode-dating-text-color: #141414;
--token-lifestylebadge-selected-color-background: #ffc629;
--token-lifestylebadge-selected-color-border: #141414;
--token-lifestylebadge-selected-color-text: #141414;
--token-lifestylebadge-text-color: #141414;
--token-mark-border-radius: 11px;
--token-mark-shadow-color: #000;
--token-match-photos-border-color: #fff;
--token-match-photos-border-radius: 20%;
--token-match-photos-lg-border-width: 4px;
--token-match-photos-md-border-width: 4px;
--token-match-photos-xlg-border-width: 6px;
--token-media-overlay-background-color: #141414;
--token-mockcard-border-color: #141414;
--token-mockcard-border-radius-rounded: 16px;
--token-mockcard-border-radius-squared: 4px;
--token-mockcard-border-width: 2px;
--token-mockcard-close-icon-margin-right: 12px;
--token-mockcard-close-icon-margin-top: 12px;
--token-mockcard-close-icon-size: 16px;
--token-mockcard-corner-icon-color: #6b6b6b;
--token-mockcard-corner-icon-size: 24px;
--token-mockcard-min-height: 150px;
--token-mockcard-padding-horizontal: 16px;
--token-mockcard-padding-vertical: 16px;
--token-mockcard-spacing-action-margin-top: 16px;
--token-mockcard-spacing-media-content: 16px;
--token-mockcard-spacing-title-text: 6px;
--token-mockcard-text-max-lines: 2;
--token-mockcard-title-max-lines: 1;
--token-modal-border-radius: 20px;
--token-navigation-bar-background-color: #fff;
--token-navigation-bar-button-color: #ffc629;
--token-navigation-bar-color-base: #6b6b6b;
--token-navigation-bar-profile-additional-color: #6b6b6b;
--token-navigation-bar-profile-heading-color: #141414;
--token-navigation-bar-title-color: #141414;
--token-nudge-border-radius: 12px;
--token-nudge-icon-color: #6b6b6b;
--token-online-status-color-idle: #ffc629;
--token-online-status-color-online: #1a964a;
--token-placard-border-radius: 16px;
--token-placard-extra-color-default: #6b6b6b;
--token-placard-extra-color-inverted: #fff;
--token-placard-extra-size-medium: 22px;
--token-placard-media-size-medium: 22px;
--token-placard-padding-horizontal: 16px;
--token-placard-padding-vertical: 16px;
--token-placard-spacing-content-extra: 12px;
--token-placard-spacing-content-extra-compact: 8px;
--token-placard-spacing-content-extra-loose: 12px;
--token-placard-spacing-media-content: 16px;
--token-placard-spacing-media-content-compact: 12px;
--token-placard-spacing-media-content-loose: 16px;
--token-progress-bar-primary-background-color-on-brand: #00000033;
--token-progress-bar-primary-background-color-on-light: #f6f6f6;
--token-progress-bar-primary-indicator-color-on-brand: #141414;
--token-progress-bar-primary-indicator-color-on-light: #ffc629;
--token-search-border-radius-rounded: 18px;
--token-search-clear-color: #6b6b6b;
--token-search-icon-color: #141414;
--token-search-input-placeholder-color: #6b6b6b;
--token-search-input-text-color: #141414;
--token-select-base-background-color: #fff;
--token-select-base-border-color: #dcdcdc;
--token-select-base-border-width: 1px;
--token-select-base-text-color: #141414;
--token-select-border-radius: 16px;
--token-select-filled-border-color: #6b6b6b;
--token-select-focused-border-color: #141414;
--token-select-focused-border-width: 2px;
--token-select-icon-color: #141414;
--token-select-status-error-border-color: #cd2e0f;
--token-select-status-error-border-width: 2px;
--token-select-status-success-border-color: #1a964a;
--token-select-status-success-border-width: 2px;
--token-settings-item-border-color: #e7e7e7;
--token-settings-item-border-width: 1px;
--token-snackpill-border-radius: 8px;
--token-snackpill-shadow-color: #000;
--token-tabbar-label-color-active: #141414;
--token-tabbar-label-color-base: #6b6b6b;
--token-tabbar-media-color-active: #141414;
--token-tabbar-media-color-base: #949494;
--token-tabs-border-color-on-brand: #dcdcdc;
--token-tabs-border-color-on-light: #dcdcdc;
--token-tabs-border-width: 1px;
--token-tabs-item-border-width: 3px;
--token-tabs-item-color-active-on-brand: #141414;
--token-tabs-item-color-active-on-light: #141414;
--token-tabs-item-color-base-on-brand: #949494;
--token-tabs-item-color-base-on-light: #949494;
--token-text-area-base-background-color: #fff;
--token-text-area-base-border-color: #dcdcdc;
--token-text-area-base-border-width: 1px;
--token-text-area-base-text-color: #141414;
--token-text-area-border-radius: 16px;
--token-text-area-filled-border-color: #6b6b6b;
--token-text-area-focused-border-color: #141414;
--token-text-area-focused-border-width: 2px;
--token-text-area-status-error-border-color: #cd2e0f;
--token-text-area-status-error-border-width: 2px;
--token-text-area-status-success-border-color: #1a964a;
--token-text-area-status-success-border-width: 2px;
--token-text-field-base-background-color: #fff;
--token-text-field-base-border-color: #dcdcdc;
--token-text-field-base-border-width: 1px;
--token-text-field-base-text-color: #141414;
--token-text-field-border-radius: 16px;
--token-text-field-filled-border-color: #6b6b6b;
--token-text-field-focused-border-color: #141414;
--token-text-field-focused-border-width: 2px;
--token-text-field-icon-color: #6b6b6b;
--token-text-field-status-error-border-color: #cd2e0f;
--token-text-field-status-error-border-width: 2px;
--token-text-field-status-success-border-color: #1a964a;
--token-text-field-status-success-border-width: 2px;
--token-toggle-checked-background-color-on-brand: #141414;
--token-toggle-checked-background-color-on-light: #141414;
--token-toggle-checked-thumb-color-on-brand: #fff;
--token-toggle-checked-thumb-color-on-light: #fff;
--token-toggle-unchecked-background-color-on-brand: #6b6b6b;
--token-toggle-unchecked-background-color-on-light: #949494;
--token-toggle-unchecked-thumb-color-on-brand: #fff;
--token-toggle-unchecked-thumb-color-on-light: #fff;
--token-tooltip-border-color: #dcdcdc;
--token-tooltip-border-radius: 18px;
--token-tooltip-shadow-color: #000;
--token-usercard-actions-height: 44px;
--token-usercard-background-color: #f6f6f6;
--token-usercard-border-radius: 12px;
--token-usercard-content-inset: 7.199999999999999%;
--token-usercard-halo-opacity: .8;
--token-usercard-halo-width: 2px;
--token-usercard-media-gradient-bottom-height: 50%;
--token-usercard-media-gradient-bottom-opacity: .4;
--token-usercard-media-gradient-top-height: 25%;
--token-usercard-media-gradient-top-opacity: .4;
--token-usercard-portrait-ratio: 144.144%;
--token-usercard-thin-border-opacity: .05;
--token-usercard-thin-border-width: 1px;
--token-view-profile-block-background-color-default: #fff7de;
--token-cosmos-button-border-width-primary-yellow: 0px;
--token-cosmos-button-border-width-secondary-yellow: 1px;
--token-cosmos-button-border-width-tertiary-yellow: 0px;
--token-cosmos-button-color-background-overlay-primary-default-hover: var( --token-cosmos-button-color-background-overlay-inverse-hover );
--token-cosmos-button-color-background-overlay-secondary-default-hover: var( --token-cosmos-button-color-background-overlay-base-hover );
--token-cosmos-button-color-background-overlay-tertiary-default-hover: var( --token-cosmos-button-color-background-overlay-base-hover );
--token-cosmos-button-color-background-overlay-primary-default-pressed: var( --token-cosmos-button-color-background-overlay-inverse-pressed );
--token-cosmos-button-color-background-overlay-secondary-default-pressed: var( --token-cosmos-button-color-background-overlay-base-pressed );
--token-cosmos-button-color-background-overlay-tertiary-default-pressed: var( --token-cosmos-button-color-background-overlay-base-pressed );
--token-cosmos-button-color-background-overlay-primary-inverse-hover: #1414140d;
--token-cosmos-button-color-background-overlay-secondary-inverse-hover: #ffffff0d;
--token-cosmos-button-color-background-overlay-tertiary-inverse-hover: #ffffff0d;
--token-cosmos-button-color-background-overlay-primary-inverse-pressed: #1414141a;
--token-cosmos-button-color-background-overlay-secondary-inverse-pressed: #ffffff1a;
--token-cosmos-button-color-background-overlay-tertiary-inverse-pressed: #ffffff1a;
--token-cosmos-button-color-background-overlay-primary-yellow-hover: #ffffff1d;
--token-cosmos-button-color-background-overlay-secondary-yellow-hover: #ffdb5b1d;
--token-cosmos-button-color-background-overlay-tertiary-yellow-hover: #ffdb5b1d;
--token-cosmos-button-color-background-overlay-primary-yellow-pressed: #ffffff3d;
--token-cosmos-button-color-background-overlay-secondary-yellow-pressed: #ffdb5b2d;
--token-cosmos-button-color-background-overlay-tertiary-yellow-pressed: #ffdb5b2d;
--token-cosmos-button-color-background-primary-yellow: #ffdb5b;
--token-cosmos-button-color-background-secondary-yellow: #ffffff00;
--token-cosmos-button-color-background-tertiary-yellow: #ffffff00;
--token-cosmos-button-color-border-primary-yellow: #ffdb5b;
--token-cosmos-button-color-border-secondary-yellow: #ffdb5b;
--token-cosmos-button-color-border-tertiary-yellow: #ffdb5b;
--token-cosmos-button-color-content-primary-yellow: #343333;
--token-cosmos-button-color-content-secondary-yellow: #ffdb5b;
--token-cosmos-button-color-content-tertiary-yellow: #ffdb5b;
--color-ui-kit-text-default: var(--token-cosmos-semantic-color-text-default);
--color-ui-kit-text-subdued: var(--token-cosmos-semantic-color-text-subdued);
--color-ui-kit-text-error: var(--token-cosmos-semantic-color-text-error);
--color-ui-kit-text-inverse: var(--token-cosmos-semantic-color-text-inverse);
--color-ui-kit-text-yellow: var(--token-cosmos-button-color-background-primary-yellow);
--color-ui-kit-link-default: var(--token-cosmos-semantic-color-text-links);
--color-ui-kit-link-hover: var(--token-cosmos-semantic-color-text-links);
--color-ui-kit-white: #fff;
--styleguide-color-text-secondary: #717171;
--styleguide-cell-color-background-light: #f4f4f4;
--styleguide-cell-color-background-dark: #999;
--styleguide-cell-color-background-brand: var(--token-cosmos-button-color-background-primary-yellow);
--color-text-default: #343333;
--color-text-subdued: #575656;
--color-text-error: #b24414;
--color-text-inverse: #fff;
--color-text-brand: #fff500;
--color-link-default: #343333;
--color-link-hover: #343333;
--color-icon-default: #343333;
--color-border-default: #dcdcdc;
--color-border-selected: #343333;
--forms-border-width-resting: 1px;
--forms-border-width-focused: 2px;
--forms-border-color-resting: #8d8d8d;
--forms-border-color-focused: #343333;
--forms-border-color-error: #b24414;
--focus-ring-outer-width: 2px;
--focus-ring-outer-color: #000;
--focus-ring-outer-offset: -3px;
--focus-ring-inner-width: 1px;
--focus-ring-inner-color: #000;
--focus-ring-inner-offset: 2px;
--logo-color: #343333;
--card-border-radius: 16px;
--card-content-gap: 12px;
--card-content-padding: clamp(24px,18.614379085px + 1.3071895425vw,32px);
```

### Spacing

```css
--header-padding-horizontal: 20px;
--header-actions-gap-horizontal: 12px;
--header-padding-top: 26px;
--token-a11y-min-target-size: 44px;
--token-action-cell-extra-size-height: 24px;
--token-action-cell-hint-space-margin-top: 2px;
--token-action-cell-large-media-size: 72px;
--token-action-cell-large-space-gap: 12px;
--token-action-cell-large-space-padding-horizontal: 16px;
--token-action-cell-large-space-padding-vertical: 12px;
--token-action-cell-medium-media-size: 24px;
--token-action-cell-medium-space-gap: 12px;
--token-action-cell-medium-space-padding-horizontal: 16px;
--token-action-cell-medium-space-padding-vertical: 12px;
--token-actionsheet-header-padding-horizontal: 16px;
--token-actionsheet-header-padding-vertical: 24px;
--token-actionsheet-item-padding-horizontal: 16px;
--token-actionsheet-item-padding-vertical: 8px;
--token-brick-size-lg: 120px;
--token-brick-size-md: 100px;
--token-brick-size-sm: 70px;
--token-brick-size-xlg: 150px;
--token-brick-size-xxlg: 174px;
--token-brick-size-xxsm: 36px;
--token-button-medium-icon-size: 24px;
--token-button-medium-loader-size: 36px;
--token-button-medium-padding-horizontal: 24px;
--token-button-medium-padding-vertical: 12px;
--token-button-medium-spacing-icon-text: 8px;
--token-button-small-icon-size: 20px;
--token-button-small-loader-size: 24px;
--token-button-small-padding-horizontal: 20px;
--token-button-small-padding-vertical: 8px;
--token-button-small-spacing-icon-text: 8px;
--token-chat-composer-frame-item-gap: 8px;
--token-chat-composer-frame-item-size: 36px;
--token-chat-composer-mini-action-icon-size: 32px;
--token-chat-date-margin-vertical: 6px;
--token-chat-date-pill-padding-horizontal: 12px;
--token-chat-input-field-font-size: 18px;
--token-chat-input-field-icon-size: 24px;
--token-chat-input-search-icon-margin-left: 12px;
--token-chat-input-search-icon-margin-right: 6px;
--token-chat-input-search-icon-size: 16px;
--token-chat-item-group-avatar-margin-bottom: 2px;
--token-chat-item-group-avatar-overall-space: 40px;
--token-chat-item-group-avatar-size: 32px;
--token-chat-item-group-title-margin-bottom: 6px;
--token-chat-item-margin-top: 8px;
--token-chat-item-margin-top-continuation: 4px;
--token-chat-item-select-overall-space: 36px;
--token-chat-item-status-margin-top: 6px;
--token-chat-message-audio-bar-gap: 1px;
--token-chat-message-audio-icon-bar-spacing-size: 4px;
--token-chat-message-audio-icon-size: 20px;
--token-chat-message-emoji-font-size: 48px;
--token-chat-message-reaction-emoji-size: 40px;
--token-chat-message-video-telescope-size: 160px;
--token-chat-panel-pills-item-media-size: 22px;
--token-chat-panel-pills-item-padding-horizontal: 10px;
--token-chat-panel-pills-item-spacing-horizontal: 4px;
--token-chat-preview-message-media-size: 32px;
--token-chat-scroll-to-bottom-icon-size: 24px;
--token-chat-scroll-to-bottom-notification-size: 12px;
--token-chat-scroll-to-bottom-size: 40px;
--token-choice-size: 24px;
--token-cosmos-actionbadge-spacing-gap-medium: 10px;
--token-cosmos-actionbadge-spacing-gap-small: 6px;
--token-cosmos-actionbadge-spacing-horizontal: 20px;
--token-cosmos-actionbadge-spacing-vertical: 12px;
--token-cosmos-actioncell-spacing-gap: 8px;
--token-cosmos-actioncell-spacing-horizontal: 16px;
--token-cosmos-actioncell-spacing-vertical: 16px;
--token-cosmos-actionrow-spacing-gap-horizontal-medium: 12px;
--token-cosmos-actionrow-spacing-gap-horizontal-small: 8px;
--token-cosmos-actionrow-spacing-gap-horizontal-xsmall: 4px;
--token-cosmos-actionrow-spacing-gap-vertical: 2px;
--token-cosmos-actionrow-spacing-horizontal-compact: 0px;
--token-cosmos-actionrow-spacing-horizontal-default: 16px;
--token-cosmos-actionrow-spacing-vertical-compact-medium: 16px;
--token-cosmos-actionrow-spacing-vertical-compact-small: 4px;
--token-cosmos-actionrow-spacing-vertical-default: 16px;
--token-cosmos-actionsheet-spacing-gap-medium: 12px;
--token-cosmos-actionsheet-spacing-gap-small: 0px;
--token-cosmos-actionsheet-spacing-horizontal-medium: 20px;
--token-cosmos-actionsheet-spacing-horizontal-small: 8px;
--token-cosmos-actionsheet-spacing-vertical-bottom: 20px;
--token-cosmos-actionsheet-spacing-vertical-top-medium: 20px;
--token-cosmos-actionsheet-spacing-vertical-top-small: 8px;
--token-cosmos-actionsheet-spacing-vertical-top-xsmall: 0px;
--token-cosmos-badge-spacing-gap-micro: 4px;
--token-cosmos-badge-spacing-gap-mini: 4px;
--token-cosmos-badge-spacing-gap-small: 4px;
--token-cosmos-badge-spacing-horizontal-micro-end-default: 8px;
--token-cosmos-badge-spacing-horizontal-micro-end-media: 8px;
--token-cosmos-badge-spacing-horizontal-micro-start-default: 8px;
--token-cosmos-badge-spacing-horizontal-micro-start-media: 1px;
--token-cosmos-badge-spacing-horizontal-mini-end-default: 8px;
--token-cosmos-badge-spacing-horizontal-mini-end-media: 8px;
--token-cosmos-badge-spacing-horizontal-mini-start-default: 8px;
--token-cosmos-badge-spacing-horizontal-mini-start-media: 1px;
--token-cosmos-badge-spacing-horizontal-small-end-default: 12px;
--token-cosmos-badge-spacing-horizontal-small-end-media: 12px;
--token-cosmos-badge-spacing-horizontal-small-start-default: 12px;
--token-cosmos-badge-spacing-horizontal-small-start-media: 1px;
--token-cosmos-badge-spacing-vertical-media: 1px;
--token-cosmos-badge-spacing-vertical-micro: 2px;
--token-cosmos-badge-spacing-vertical-mini: 4px;
--token-cosmos-badge-spacing-vertical-small: 8px;
--token-cosmos-brick-spacing-offset-circle-horizontal-large: -5px;
--token-cosmos-brick-spacing-offset-circle-horizontal-medium: -2px;
--token-cosmos-brick-spacing-offset-circle-horizontal-small: 0px;
--token-cosmos-brick-spacing-offset-circle-horizontal-xlarge: -10px;
--token-cosmos-brick-spacing-offset-circle-horizontal-xsmall: 0px;
--token-cosmos-brick-spacing-offset-circle-vertical-large: 5px;
--token-cosmos-brick-spacing-offset-circle-vertical-medium: 2px;
--token-cosmos-brick-spacing-offset-circle-vertical-small: 0px;
--token-cosmos-brick-spacing-offset-circle-vertical-xlarge: 10px;
--token-cosmos-brick-spacing-offset-circle-vertical-xsmall: 0px;
--token-cosmos-button-spacing-gap-medium: 8px;
--token-cosmos-button-spacing-gap-micro: 4px;
--token-cosmos-button-spacing-gap-mini: 6px;
--token-cosmos-button-spacing-gap-small: 6px;
--token-cosmos-button-spacing-horizontal-medium: 24px;
--token-cosmos-button-spacing-horizontal-micro: 10px;
--token-cosmos-button-spacing-horizontal-mini: 16px;
--token-cosmos-button-spacing-horizontal-small: 20px;
--token-cosmos-button-spacing-vertical-medium: 14px;
--token-cosmos-button-spacing-vertical-micro: 6px;
--token-cosmos-button-spacing-vertical-mini: 10px;
--token-cosmos-button-spacing-vertical-small: 12px;
--token-cosmos-carousel-spacing-gap: 8px;
--token-cosmos-carousel-spacing-horizontal-left: 20px;
--token-cosmos-carousel-spacing-horizontal-right: 0px;
--token-cosmos-carousel-spacing-vertical: 4px;
--token-cosmos-ctabox-spacing-gap-large: 16px;
--token-cosmos-ctabox-spacing-gap-medium: 8px;
--token-cosmos-ctabox-spacing-gap-small: 8px;
--token-cosmos-ctabox-spacing-gap-xsmall: 0px;
--token-cosmos-dotcounternotification-spacing-horizontal: 4px;
--token-cosmos-dotcounternotification-spacing-vertical: 0px;
--token-cosmos-emptystate-spacing-vertical-large: 16px;
--token-cosmos-emptystate-spacing-vertical-medium: 12px;
--token-cosmos-emptystate-spacing-vertical-small: 8px;
--token-cosmos-filters-spacing-gap-medium: 10px;
--token-cosmos-filters-spacing-gap-small: 6px;
--token-cosmos-filters-spacing-horizontal: 16px;
--token-cosmos-filters-spacing-vertical: 10px;
--token-cosmos-forms-spacing-gap-horizontal-medium: 12px;
--token-cosmos-forms-spacing-gap-horizontal-small: 8px;
--token-cosmos-forms-spacing-gap-horizontal-xsmall: 4px;
--token-cosmos-forms-spacing-gap-horizontal-xxsmall: 0px;
--token-cosmos-forms-spacing-gap-vertical-medium: 4px;
--token-cosmos-forms-spacing-gap-vertical-small: 0px;
--token-cosmos-forms-spacing-horizontal-medium: 16px;
--token-cosmos-forms-spacing-horizontal-small: 0px;
--token-cosmos-forms-spacing-item-gap: 12px;
--token-cosmos-forms-spacing-item-horizontal: 16px;
--token-cosmos-forms-spacing-item-vertical: 8px;
--token-cosmos-forms-spacing-vertical-medium: 16px;
--token-cosmos-forms-spacing-vertical-small: 2px;
--token-cosmos-forms-spacing-vertical-xsmall: 0px;
--token-cosmos-helpertext-spacing-gap: 8px;
--token-cosmos-helpertext-spacing-vertical: 1px;
--token-cosmos-inappnotification-spacing-horizontal: 12px;
--token-cosmos-inappnotification-spacing-item-gap-horizontal-medium: 12px;
--token-cosmos-inappnotification-spacing-item-gap-horizontal-small: 0px;
--token-cosmos-inappnotification-spacing-item-gap-vertical-medium: 12px;
--token-cosmos-inappnotification-spacing-item-gap-vertical-small: 2px;
--token-cosmos-inappnotification-spacing-item-horizontal: 12px;
--token-cosmos-inappnotification-spacing-item-vertical: 12px;
--token-cosmos-inappnotification-spacing-vertical-bottom: 8px;
--token-cosmos-inappnotification-spacing-vertical-top: 8px;
--token-cosmos-mark-spacing-gap: 4px;
--token-cosmos-mark-spacing-horizontal: 8px;
--token-cosmos-mark-spacing-vertical: 2px;
--token-cosmos-menu-spacing-gap-medium: 8px;
--token-cosmos-menu-spacing-gap-small: 0px;
--token-cosmos-menu-spacing-horizontal: 16px;
--token-cosmos-menu-spacing-vertical: 16px;
--token-cosmos-modal-spacing-horizontal: 20px;
--token-cosmos-modal-spacing-outset: 20px;
--token-cosmos-modal-spacing-vertical: 20px;
--token-cosmos-navigationbar-spacing-gap-horizontal-large: 12px;
--token-cosmos-navigationbar-spacing-gap-horizontal-medium: 8px;
--token-cosmos-navigationbar-spacing-gap-horizontal-small: 0px;
--token-cosmos-navigationbar-spacing-gap-horizontal-xlarge: 16px;
--token-cosmos-navigationbar-spacing-gap-vertical: 0px;
--token-cosmos-navigationbar-spacing-horizontal-medium: 20px;
--token-cosmos-navigationbar-spacing-horizontal-small: 12px;
--token-cosmos-navigationbar-spacing-vertical-medium: 8px;
--token-cosmos-navigationbar-spacing-vertical-small: 4px;
--token-cosmos-nudge-spacing-gap-horizontal-medium: 12px;
--token-cosmos-nudge-spacing-gap-vertical-medium: 20px;
--token-cosmos-nudge-spacing-gap-vertical-small: 8px;
--token-cosmos-nudge-spacing-horizontal: 24px;
--token-cosmos-nudge-spacing-vertical: 24px;
--token-cosmos-paginationdots-spacing-gap: 8px;
--token-cosmos-search-spacing-gap: 8px;
--token-cosmos-search-spacing-horizontal-left: 16px;
--token-cosmos-search-spacing-horizontal-right: 2px;
--token-cosmos-search-spacing-vertical: 8px;
--token-cosmos-semantic-motion-easing-emphasized: cubic-bezier(.2,0,0,1);
--token-cosmos-semantic-motion-easing-emphasized-accelerate: cubic-bezier(.3,0,.8,.15);
--token-cosmos-semantic-motion-easing-emphasized-decelerate: cubic-bezier(.05,.7,.1,1);
--token-cosmos-semantic-spacing-0: 0px;
--token-cosmos-semantic-spacing-1: 1px;
--token-cosmos-semantic-spacing-12: 12px;
--token-cosmos-semantic-spacing-16: 16px;
--token-cosmos-semantic-spacing-2: 2px;
--token-cosmos-semantic-spacing-20: 20px;
--token-cosmos-semantic-spacing-24: 24px;
--token-cosmos-semantic-spacing-3: 3px;
--token-cosmos-semantic-spacing-32: 32px;
--token-cosmos-semantic-spacing-4: 4px;
--token-cosmos-semantic-spacing-40: 40px;
--token-cosmos-semantic-spacing-48: 48px;
--token-cosmos-semantic-spacing-56: 56px;
--token-cosmos-semantic-spacing-8: 8px;
--token-cosmos-semantic-spacing-gap-large: 12px;
--token-cosmos-semantic-spacing-gap-medium: 8px;
--token-cosmos-semantic-spacing-gap-small: 4px;
--token-cosmos-semantic-spacing-gap-xlarge: 16px;
--token-cosmos-semantic-spacing-gap-xsmall: 0px;
--token-cosmos-semantic-spacing-gap-xxlarge: 24px;
--token-cosmos-semantic-spacing-margins-horizontal: 20px;
--token-cosmos-semantic-spacing-margins-vertical: 20px;
--token-cosmos-semantic-typography-action-font-size: 17px;
--token-cosmos-semantic-typography-action-letter-spacing: .28px;
--token-cosmos-semantic-typography-action-mini-font-size: 13px;
--token-cosmos-semantic-typography-action-mini-letter-spacing: .32px;
--token-cosmos-semantic-typography-action-mini-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-action-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-action-small-font-size: 15px;
--token-cosmos-semantic-typography-action-small-letter-spacing: .3px;
--token-cosmos-semantic-typography-action-small-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-caption-font-size: 11px;
--token-cosmos-semantic-typography-caption-letter-spacing: .32px;
--token-cosmos-semantic-typography-caption-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-d1-font-size: 70px;
--token-cosmos-semantic-typography-d1-letter-spacing: .46px;
--token-cosmos-semantic-typography-d1-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-d2-font-size: 49px;
--token-cosmos-semantic-typography-d2-letter-spacing: .42px;
--token-cosmos-semantic-typography-d2-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-d3-font-size: 34px;
--token-cosmos-semantic-typography-d3-letter-spacing: .4px;
--token-cosmos-semantic-typography-d3-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-h1-font-size: 28px;
--token-cosmos-semantic-typography-h1-letter-spacing: .36px;
--token-cosmos-semantic-typography-h1-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-h2-font-size: 22px;
--token-cosmos-semantic-typography-h2-letter-spacing: .34px;
--token-cosmos-semantic-typography-h2-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-h3-font-size: 20px;
--token-cosmos-semantic-typography-h3-letter-spacing: .32px;
--token-cosmos-semantic-typography-h3-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-h4-font-size: 17px;
--token-cosmos-semantic-typography-h4-letter-spacing: .28px;
--token-cosmos-semantic-typography-h4-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-link-1-font-size: 17px;
--token-cosmos-semantic-typography-link-1-letter-spacing: .28px;
--token-cosmos-semantic-typography-link-1-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-link-2-font-size: 15px;
--token-cosmos-semantic-typography-link-2-letter-spacing: .3px;
--token-cosmos-semantic-typography-link-2-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-link-3-font-size: 13px;
--token-cosmos-semantic-typography-link-3-letter-spacing: .32px;
--token-cosmos-semantic-typography-link-3-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-p1-bolder-font-size: 17px;
--token-cosmos-semantic-typography-p1-bolder-letter-spacing: .28px;
--token-cosmos-semantic-typography-p1-bolder-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-p1-font-size: 17px;
--token-cosmos-semantic-typography-p1-letter-spacing: .28px;
--token-cosmos-semantic-typography-p1-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-p2-bolder-font-size: 15px;
--token-cosmos-semantic-typography-p2-bolder-letter-spacing: .3px;
--token-cosmos-semantic-typography-p2-bolder-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-p2-font-size: 15px;
--token-cosmos-semantic-typography-p2-letter-spacing: .3px;
--token-cosmos-semantic-typography-p2-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-p3-bolder-font-size: 13px;
--token-cosmos-semantic-typography-p3-bolder-letter-spacing: .32px;
--token-cosmos-semantic-typography-p3-bolder-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-p3-font-size: 13px;
--token-cosmos-semantic-typography-p3-letter-spacing: .32px;
--token-cosmos-semantic-typography-p3-paragraph-spacing: 0px;
--token-cosmos-semantic-typography-title-font-size: 17px;
--token-cosmos-semantic-typography-title-letter-spacing: .28px;
--token-cosmos-semantic-typography-title-paragraph-spacing: 0px;
--token-cosmos-snackpill-spacing-gap: 8px;
--token-cosmos-snackpill-spacing-horizontal: 12px;
--token-cosmos-snackpill-spacing-vertical: 8px;
--token-cosmos-stack-spacing-gap-compact: 8px;
--token-cosmos-stack-spacing-gap-loose: 12px;
--token-cosmos-stack-spacing-gap-tight: 0px;
--token-cosmos-tabbar-spacing-gap: 4px;
--token-cosmos-tabbar-spacing-horizontal: 8px;
--token-cosmos-tabbar-spacing-offset-dotcounternotification-hidden-horizontal: 2px;
--token-cosmos-tabbar-spacing-offset-dotcounternotification-hidden-vertical: -2px;
--token-cosmos-tabbar-spacing-offset-dotcounternotification-visible-horizontal: 6px;
--token-cosmos-tabbar-spacing-offset-dotcounternotification-visible-vertical: -6px;
--token-cosmos-tabbar-spacing-vertical-bottom: 8px;
--token-cosmos-tabbar-spacing-vertical-top: 8px;
--token-cosmos-tabs-spacing-gap: 8px;
--token-cosmos-tabs-spacing-horizontal: 16px;
--token-cosmos-tabs-spacing-item-gap: 8px;
--token-cosmos-tabs-spacing-item-horizontal: 16px;
--token-cosmos-tabs-spacing-item-vertical: 12px;
--token-cosmos-textbutton-spacing-gap-large: 4px;
--token-cosmos-textbutton-spacing-gap-medium: 4px;
--token-cosmos-textbutton-spacing-gap-mini: 4px;
--token-cosmos-textbutton-spacing-gap-small: 4px;
--token-cosmos-tip-spacing-gap-horizontal-large: 12px;
--token-cosmos-tip-spacing-gap-horizontal-medium: 8px;
--token-cosmos-tip-spacing-gap-horizontal-small: 0px;
--token-cosmos-tip-spacing-gap-vertical-medium: 8px;
--token-cosmos-tip-spacing-gap-vertical-small: 2px;
--token-cosmos-tip-spacing-horizontal-end-large: 20px;
--token-cosmos-tip-spacing-horizontal-end-medium: 16px;
--token-cosmos-tip-spacing-horizontal-end-small: 0px;
--token-cosmos-tip-spacing-horizontal-start-large: 20px;
--token-cosmos-tip-spacing-horizontal-start-medium: 16px;
--token-cosmos-tip-spacing-vertical: 12px;
--token-cosmos-toggle-spacing-horizontal-end-selected: 4px;
--token-cosmos-toggle-spacing-horizontal-end-unselected: 20px;
--token-cosmos-toggle-spacing-horizontal-start-selected: 20px;
--token-cosmos-toggle-spacing-horizontal-start-unselected: 4px;
--token-cosmos-toggle-spacing-vertical: 4px;
--token-cosmos-tooltip-spacing-gap-end: 16px;
--token-cosmos-tooltip-spacing-gap-start: 16px;
--token-cosmos-tooltip-spacing-horizontal: 16px;
--token-cosmos-tooltip-spacing-vertical: 12px;
--token-date-field-item-horizontal-gap: 8px;
--token-dotcounternotification-counter-font-size: 11px;
--token-dotcounternotification-counter-min-size: 18px;
--token-dotcounternotification-dot-size: 5px;
--token-floating-action-button-medium-icon-size: 24px;
--token-floating-action-button-medium-loader-size: 24px;
--token-floating-action-button-medium-size: 64px;
--token-font-size-action: 18px;
--token-font-size-action-small: 14px;
--token-font-size-caption: 12px;
--token-font-size-header-0: 40px;
--token-font-size-header-1: 32px;
--token-font-size-header-2: 28px;
--token-font-size-header-3: 24px;
--token-font-size-header-4: 20px;
--token-font-size-link-1: 18px;
--token-font-size-link-2: 16px;
--token-font-size-link-3: 14px;
--token-font-size-paragraph-1: 18px;
--token-font-size-paragraph-1-bolder: 18px;
--token-font-size-paragraph-2: 16px;
--token-font-size-paragraph-2-bolder: 16px;
--token-font-size-paragraph-3: 14px;
--token-font-size-paragraph-3-bolder: 14px;
--token-form-control-gap-vertical: 24px;
--token-form-label-extra-margin-left: 8px;
--token-form-label-margin-bottom: 8px;
--token-form-note-icon-margin-right: 8px;
--token-form-note-icon-margin-top: 2px;
--token-form-note-icon-size: 16px;
--token-form-note-margin-top: 8px;
--token-form-note-padding-left: 8px;
--token-grid-list-spacing-lg: 8px;
--token-grid-list-spacing-md: 4px;
--token-grid-list-spacing-sm: 1px;
--token-grid-list-spacing-xlg: 12px;
--token-inappnotification-media-size: 70px;
--token-input-choice-size: 24px;
--token-input-toggle-thumb-size: 20px;
--token-interest-emoji-margin-right: 4px;
--token-interest-emoji-size: 18px;
--token-interest-medium-padding-horizontal: 12px;
--token-interest-small-padding-horizontal: 12px;
--token-letter-spacing-header-0: 0%;
--token-lifestylebadge-icon-size: 20px;
--token-lifestylebadge-padding-end: 10px;
--token-lifestylebadge-padding-start: 5px;
--token-lifestylebadge-spacing-icon-text: 5px;
--token-mark-icon-size: 12px;
--token-mark-padding-horizontal: 6px;
--token-mark-size: 22px;
--token-mark-spacing-icon-text: 4px;
--token-match-photos-icon-to-image-size-ratio: 40%;
--token-match-photos-lg-image-size: 120px;
--token-match-photos-md-image-size: 100px;
--token-match-photos-xlg-image-size: 150px;
--token-modal-bottom-outset-space: 16px;
--token-modal-popup-outset-space: 16px;
--token-navigation-bar-gap-compact: 6px;
--token-navigation-bar-gap-loose: 10px;
--token-navigation-bar-icon-media-size: 24px;
--token-navigation-bar-profile-avatar-margin-right: 12px;
--token-navigation-bar-profile-avatar-size: 36px;
--token-nudge-icon-size: 24px;
--token-nudge-padding-horizontal: 32px;
--token-nudge-padding-vertical: 16px;
--token-nudge-spacing-action-margin-top: 8px;
--token-nudge-spacing-media-margin-bottom: 8px;
--token-nudge-spacing-title-text: 4px;
--token-online-status-size: 8px;
--token-pagination-dots-dot-gap: 4px;
--token-pagination-dots-dot-size: 6px;
--token-scroll-list-spacing-lg: 8px;
--token-scroll-list-spacing-md: 4px;
--token-scroll-list-spacing-sm: 1px;
--token-scroll-list-spacing-xlg: 16px;
--token-scroll-list-spacing-xxlg: 24px;
--token-search-clear-margin-right: 8px;
--token-search-clear-size: 20px;
--token-search-icon-margin-left: 12px;
--token-search-icon-margin-right: 8px;
--token-search-icon-size: 18px;
--token-search-input-margin-right: 12px;
--token-select-font-size: 18px;
--token-select-icon-margin-left: 4px;
--token-select-icon-size: 16px;
--token-select-padding-horizontal: 16px;
--token-snackpill-icon-size: 16px;
--token-snackpill-padding-horizontal: 15px;
--token-snackpill-padding-vertical: 7px;
--token-snackpill-spacing-icon-text: 5px;
--token-spacing-gap: 16px;
--token-spacing-lg: 16px;
--token-spacing-md: 12px;
--token-spacing-sm: 8px;
--token-spacing-xlg: 24px;
--token-spacing-xsm: 4px;
--token-spacing-xxlg: 32px;
--token-stack-spacing-compact: 8px;
--token-stack-spacing-loose: 12px;
--token-tabbar-item-padding-horizontal: 8px;
--token-tabbar-item-padding-top: 6px;
--token-tabbar-label-font-size: 10px;
--token-tabbar-media-margin-bottom: 4px;
--token-tabbar-media-size: 24px;
--token-tabs-item-gap: 8px;
--token-tabs-item-icon-margin-bottom: 8px;
--token-tabs-item-icon-size: 24px;
--token-tabs-item-notification-margin-left: 8px;
--token-tabs-item-padding-horizontal: 18px;
--token-tabs-item-padding-vertical: 12px;
--token-tabs-padding-horizontal: 16px;
--token-text-area-font-size: 18px;
--token-text-area-padding-horizontal: 16px;
--token-text-area-padding-vertical: 16px;
--token-text-field-font-size: 18px;
--token-text-field-icon-size: 24px;
--token-text-field-padding-horizontal: 16px;
--token-text-field-spacing-icon-action: 8px;
--token-toggle-thumb-size: 20px;
--token-tooltip-arrow-size: 14px;
--token-tooltip-padding-horizontal: 16px;
--token-tooltip-padding-vertical: 8px;
--token-view-profile-block-footer-icon-size: 40px;
--token-view-profile-block-footer-margin-top: 8px;
--token-view-profile-block-header-icon-margin-right: 8px;
--token-view-profile-block-header-icon-size: 16px;
--token-view-profile-block-header-margin-bottom: 8px;
--control-padding-horizontal-medium: 24px;
--font-size-base: 16px;
--content-section-padding-horizontal: clamp(16px,-45.9346405229px + 15.0326797386vw,108px);
--content-section-padding-vertical: clamp(64px,42.4575163399px + 5.2287581699vw,96px);
--content-section-gap-horizontal: clamp(16px,10.614379085px + 1.3071895425vw,24px);
--content-section-gap-vertical: clamp(24px,18.614379085px + 1.3071895425vw,32px);
--header-actions-gap-horizotal: 24px;
```

### Typography

```css
--token-chat-input-field-line-height: 24px;
--token-chat-message-forward-header-text-opacity: 1;
--token-chat-message-text-with-link-preview-image-ratio: 175%;
--token-cosmos-helpertext-sizing-icon: 16px;
--token-cosmos-helpertext-typography-content: p3;
--token-cosmos-inappnotification-typography-text: p2;
--token-cosmos-mark-typography-text: p3;
--token-cosmos-semantic-typography-action-font-family: Bumble Sans;
--token-cosmos-semantic-typography-action-font-weight: medium;
--token-cosmos-semantic-typography-action-line-height: 22px;
--token-cosmos-semantic-typography-action-mini-font-family: Bumble Sans;
--token-cosmos-semantic-typography-action-mini-font-weight: medium;
--token-cosmos-semantic-typography-action-mini-line-height: 18px;
--token-cosmos-semantic-typography-action-mini-text-case: none;
--token-cosmos-semantic-typography-action-mini-text-decoration: none;
--token-cosmos-semantic-typography-action-small-font-family: Bumble Sans;
--token-cosmos-semantic-typography-action-small-font-weight: medium;
--token-cosmos-semantic-typography-action-small-line-height: 20px;
--token-cosmos-semantic-typography-action-small-text-case: none;
--token-cosmos-semantic-typography-action-small-text-decoration: none;
--token-cosmos-semantic-typography-action-text-case: none;
--token-cosmos-semantic-typography-action-text-decoration: none;
--token-cosmos-semantic-typography-caption-font-family: Bumble Sans;
--token-cosmos-semantic-typography-caption-font-weight: medium;
--token-cosmos-semantic-typography-caption-line-height: 13px;
--token-cosmos-semantic-typography-caption-text-case: none;
--token-cosmos-semantic-typography-caption-text-decoration: none;
--token-cosmos-semantic-typography-d1-font-family: Bumble Sans;
--token-cosmos-semantic-typography-d1-font-weight: bold;
--token-cosmos-semantic-typography-d1-line-height: 70px;
--token-cosmos-semantic-typography-d1-text-case: none;
--token-cosmos-semantic-typography-d1-text-decoration: none;
--token-cosmos-semantic-typography-d2-font-family: Bumble Sans;
--token-cosmos-semantic-typography-d2-font-weight: bold;
--token-cosmos-semantic-typography-d2-line-height: 49px;
--token-cosmos-semantic-typography-d2-text-case: none;
--token-cosmos-semantic-typography-d2-text-decoration: none;
--token-cosmos-semantic-typography-d3-font-family: Bumble Sans;
--token-cosmos-semantic-typography-d3-font-weight: bold;
--token-cosmos-semantic-typography-d3-line-height: 34px;
--token-cosmos-semantic-typography-d3-text-case: uppercase;
--token-cosmos-semantic-typography-d3-text-decoration: none;
--token-cosmos-semantic-typography-h1-font-family: Bumble Sans;
--token-cosmos-semantic-typography-h1-font-weight: semibold;
--token-cosmos-semantic-typography-h1-line-height: 34px;
--token-cosmos-semantic-typography-h1-text-case: none;
--token-cosmos-semantic-typography-h1-text-decoration: none;
--token-cosmos-semantic-typography-h2-font-family: Bumble Sans;
--token-cosmos-semantic-typography-h2-font-weight: semibold;
--token-cosmos-semantic-typography-h2-line-height: 28px;
--token-cosmos-semantic-typography-h2-text-case: none;
--token-cosmos-semantic-typography-h2-text-decoration: none;
--token-cosmos-semantic-typography-h3-font-family: Bumble Sans;
--token-cosmos-semantic-typography-h3-font-weight: semibold;
--token-cosmos-semantic-typography-h3-line-height: 25px;
--token-cosmos-semantic-typography-h3-text-case: none;
--token-cosmos-semantic-typography-h3-text-decoration: none;
--token-cosmos-semantic-typography-h4-font-family: Bumble Sans;
--token-cosmos-semantic-typography-h4-font-weight: semibold;
--token-cosmos-semantic-typography-h4-line-height: 22px;
--token-cosmos-semantic-typography-h4-text-case: none;
--token-cosmos-semantic-typography-h4-text-decoration: none;
--token-cosmos-semantic-typography-link-1-font-family: Bumble Sans;
--token-cosmos-semantic-typography-link-1-font-weight: regular;
--token-cosmos-semantic-typography-link-1-line-height: 22px;
--token-cosmos-semantic-typography-link-1-text-case: none;
--token-cosmos-semantic-typography-link-1-text-decoration: underline;
--token-cosmos-semantic-typography-link-2-font-family: Bumble Sans;
--token-cosmos-semantic-typography-link-2-font-weight: regular;
--token-cosmos-semantic-typography-link-2-line-height: 20px;
--token-cosmos-semantic-typography-link-2-text-case: none;
--token-cosmos-semantic-typography-link-2-text-decoration: underline;
--token-cosmos-semantic-typography-link-3-font-family: Bumble Sans;
--token-cosmos-semantic-typography-link-3-font-weight: regular;
--token-cosmos-semantic-typography-link-3-line-height: 18px;
--token-cosmos-semantic-typography-link-3-text-case: none;
--token-cosmos-semantic-typography-link-3-text-decoration: underline;
--token-cosmos-semantic-typography-p1-bolder-font-family: Bumble Sans;
--token-cosmos-semantic-typography-p1-bolder-font-weight: semibold;
--token-cosmos-semantic-typography-p1-bolder-line-height: 22px;
--token-cosmos-semantic-typography-p1-bolder-text-case: none;
--token-cosmos-semantic-typography-p1-bolder-text-decoration: none;
--token-cosmos-semantic-typography-p1-font-family: Bumble Sans;
--token-cosmos-semantic-typography-p1-font-weight: regular;
--token-cosmos-semantic-typography-p1-line-height: 22px;
--token-cosmos-semantic-typography-p1-text-case: none;
--token-cosmos-semantic-typography-p1-text-decoration: none;
--token-cosmos-semantic-typography-p2-bolder-font-family: Bumble Sans;
--token-cosmos-semantic-typography-p2-bolder-font-weight: semibold;
--token-cosmos-semantic-typography-p2-bolder-line-height: 20px;
--token-cosmos-semantic-typography-p2-bolder-text-case: none;
--token-cosmos-semantic-typography-p2-bolder-text-decoration: none;
--token-cosmos-semantic-typography-p2-font-family: Bumble Sans;
--token-cosmos-semantic-typography-p2-font-weight: regular;
--token-cosmos-semantic-typography-p2-line-height: 20px;
--token-cosmos-semantic-typography-p2-text-case: none;
--token-cosmos-semantic-typography-p2-text-decoration: none;
--token-cosmos-semantic-typography-p3-bolder-font-family: Bumble Sans;
--token-cosmos-semantic-typography-p3-bolder-font-weight: semibold;
--token-cosmos-semantic-typography-p3-bolder-line-height: 18px;
--token-cosmos-semantic-typography-p3-bolder-text-case: none;
--token-cosmos-semantic-typography-p3-bolder-text-decoration: none;
--token-cosmos-semantic-typography-p3-font-family: Bumble Sans;
--token-cosmos-semantic-typography-p3-font-weight: regular;
--token-cosmos-semantic-typography-p3-line-height: 18px;
--token-cosmos-semantic-typography-p3-text-case: none;
--token-cosmos-semantic-typography-p3-text-decoration: none;
--token-cosmos-semantic-typography-title-font-family: Bumble Sans;
--token-cosmos-semantic-typography-title-font-weight: medium;
--token-cosmos-semantic-typography-title-line-height: 22px;
--token-cosmos-semantic-typography-title-text-case: none;
--token-cosmos-semantic-typography-title-text-decoration: none;
--token-cosmos-tabbar-typography-text: caption;
--token-cosmos-tabs-typography-text: action-small;
--token-cosmos-textbutton-sizing-icon-large: 12px;
--token-cosmos-textbutton-sizing-icon-medium: 12px;
--token-cosmos-textbutton-sizing-icon-mini: 12px;
--token-cosmos-textbutton-sizing-icon-small: 12px;
--token-cosmos-textbutton-typography-content-large: h3;
--token-cosmos-textbutton-typography-content-medium: p1-bolder;
--token-cosmos-textbutton-typography-content-mini: p3-bolder;
--token-cosmos-textbutton-typography-content-small: p2-bolder;
--token-font-family-action: Circular20;
--token-font-family-action-small: Circular20;
--token-font-family-caption: Circular20;
--token-font-family-custom: Circular20;
--token-font-family-header-0: Circular20;
--token-font-family-header-1: Circular20;
--token-font-family-header-2: Circular20;
--token-font-family-header-3: Circular20;
--token-font-family-header-4: Circular20;
--token-font-family-isometric-text: Circular20;
--token-font-family-link-1: Circular20;
--token-font-family-link-2: Circular20;
--token-font-family-link-3: Circular20;
--token-font-family-paragraph-1: Circular20;
--token-font-family-paragraph-1-bolder: Circular20;
--token-font-family-paragraph-2: Circular20;
--token-font-family-paragraph-2-bolder: Circular20;
--token-font-family-paragraph-3: Circular20;
--token-font-family-paragraph-3-bolder: Circular20;
--token-font-weight-action: medium;
--token-font-weight-action-small: medium;
--token-font-weight-caption: medium;
--token-font-weight-header-0: #000;
--token-font-weight-header-1: bold;
--token-font-weight-header-2: bold;
--token-font-weight-header-3: bold;
--token-font-weight-header-4: medium;
--token-font-weight-isometric-text: #000;
--token-font-weight-link-1: medium;
--token-font-weight-link-2: medium;
--token-font-weight-link-3: medium;
--token-font-weight-paragraph-1: book;
--token-font-weight-paragraph-1-bolder: medium;
--token-font-weight-paragraph-2: book;
--token-font-weight-paragraph-2-bolder: medium;
--token-font-weight-paragraph-3: book;
--token-font-weight-paragraph-3-bolder: medium;
--token-line-height-action: 24px;
--token-line-height-action-small: 20px;
--token-line-height-caption: 18px;
--token-line-height-header-0: 46px;
--token-line-height-header-1: 38px;
--token-line-height-header-2: 34px;
--token-line-height-header-3: 28px;
--token-line-height-header-4: 24px;
--token-line-height-link-1: 24px;
--token-line-height-link-2: 22px;
--token-line-height-link-3: 20px;
--token-line-height-paragraph-1: 24px;
--token-line-height-paragraph-1-bolder: 24px;
--token-line-height-paragraph-2: 22px;
--token-line-height-paragraph-2-bolder: 22px;
--token-line-height-paragraph-3: 20px;
--token-line-height-paragraph-3-bolder: 20px;
--token-select-font-family: Circular20;
--token-select-font-weight: book;
--token-select-line-height: 24px;
--token-tabbar-label-font-family: Circular20;
--token-tabbar-label-font-weight: book;
--token-tabbar-label-line-height: 12px;
--token-text-area-font-family: Circular20;
--token-text-area-font-weight: book;
--token-text-area-line-height: 24px;
--token-text-area-min-height: 124px;
--token-text-field-font-family: Circular20;
--token-text-field-font-weight: book;
--token-text-field-height: 56px;
--token-text-field-line-height: 24px;
--token-text-underline-link-1: true;
--token-text-underline-link-2: true;
--token-text-underline-link-3: true;
--font-family-custom-default: "BumbleSans","BumbleSansFallback",-apple-system,"San Francisco","Helvetica Neue",Roboto,"Segoe WP","Segoe UI",sans-serif;
--font-family-custom-heading: "BumbleSansCondensed","BumbleSansCondensedFallback",-apple-system,"San Francisco","Helvetica Neue",Roboto,"Segoe WP","Segoe UI",sans-serif;
--font-weight-regular: normal;
--font-weight-book: 400;
--font-weight-medium: 500;
--font-weight-bold: 600;
--line-height-base: 1.5;
```

### Shadows

```css
--token-chat-date-pill-elevated-shadow-blur-radius: 8px;
--token-chat-date-pill-elevated-shadow-opacity: .08;
--token-chat-date-pill-elevated-shadow-vertical-offset: 4px;
--token-chat-scroll-to-bottom-shadow-blur-radius: 8px;
--token-chat-scroll-to-bottom-shadow-opacity: .08;
--token-chat-scroll-to-bottom-shadow-vertical-offset: 4px;
--token-cosmos-actionsheet-shadow-container-blur: 12px;
--token-cosmos-actionsheet-shadow-container-spread: 0px;
--token-cosmos-actionsheet-shadow-container-x: 0px;
--token-cosmos-actionsheet-shadow-container-y: 1px;
--token-cosmos-inappnotification-shadow-blur: 12px;
--token-cosmos-inappnotification-shadow-spread: 0px;
--token-cosmos-inappnotification-shadow-x: 0px;
--token-cosmos-inappnotification-shadow-y: 1px;
--token-cosmos-mark-box-shadow-default-blur: 0px;
--token-cosmos-mark-box-shadow-default-spread: 0px;
--token-cosmos-mark-box-shadow-default-x: 0px;
--token-cosmos-mark-box-shadow-default-y: 0px;
--token-cosmos-mark-box-shadow-floating-blur: 8px;
--token-cosmos-mark-box-shadow-floating-spread: 0px;
--token-cosmos-mark-box-shadow-floating-x: 0px;
--token-cosmos-mark-box-shadow-floating-y: 1px;
--token-cosmos-menu-shadow-blur: 12px;
--token-cosmos-menu-shadow-spread: 0px;
--token-cosmos-menu-shadow-x: 0px;
--token-cosmos-menu-shadow-y: 1px;
--token-cosmos-semantic-shadows-floating-blur: 12px;
--token-cosmos-semantic-shadows-floating-elevation-1-blur: 12px;
--token-cosmos-semantic-shadows-floating-elevation-1-spread: 0px;
--token-cosmos-semantic-shadows-floating-elevation-1-x: 0px;
--token-cosmos-semantic-shadows-floating-elevation-1-y: 1px;
--token-cosmos-semantic-shadows-floating-elevation-2-blur: 12px;
--token-cosmos-semantic-shadows-floating-elevation-2-spread: 0px;
--token-cosmos-semantic-shadows-floating-elevation-2-x: 0px;
--token-cosmos-semantic-shadows-floating-elevation-2-y: 1px;
--token-cosmos-semantic-shadows-floating-spread: 0px;
--token-cosmos-semantic-shadows-floating-x: 0px;
--token-cosmos-semantic-shadows-floating-y: 1px;
--token-cosmos-semantic-shadows-in-line-blur: 8px;
--token-cosmos-semantic-shadows-in-line-spread: 0px;
--token-cosmos-semantic-shadows-in-line-x: 0px;
--token-cosmos-semantic-shadows-in-line-y: 1px;
--token-cosmos-semantic-shadows-none-blur: 0px;
--token-cosmos-semantic-shadows-none-spread: 0px;
--token-cosmos-semantic-shadows-none-x: 0px;
--token-cosmos-semantic-shadows-none-y: 0px;
--token-cosmos-semantic-shadows-overlay-blur: 24px;
--token-cosmos-semantic-shadows-overlay-spread: 0px;
--token-cosmos-semantic-shadows-overlay-x: 0px;
--token-cosmos-semantic-shadows-overlay-y: 1px;
--token-cosmos-semantic-shadows-static-elevation-1-blur: 8px;
--token-cosmos-semantic-shadows-static-elevation-1-spread: 0px;
--token-cosmos-semantic-shadows-static-elevation-1-x: 0px;
--token-cosmos-semantic-shadows-static-elevation-1-y: 1px;
--token-cosmos-semantic-shadows-static-elevation-2-blur: 8px;
--token-cosmos-semantic-shadows-static-elevation-2-spread: 0px;
--token-cosmos-semantic-shadows-static-elevation-2-x: 0px;
--token-cosmos-semantic-shadows-static-elevation-2-y: 1px;
--token-cosmos-snackpill-box-shadow-blur: 12px;
--token-cosmos-snackpill-box-shadow-spread: 0px;
--token-cosmos-snackpill-box-shadow-x: 0px;
--token-cosmos-snackpill-box-shadow-y: 1px;
--token-cosmos-tip-shadow-floating-blur: 12px;
--token-cosmos-tip-shadow-floating-spread: 0px;
--token-cosmos-tip-shadow-floating-x: 0px;
--token-cosmos-tip-shadow-floating-y: 1px;
--token-cosmos-tip-shadow-inline-blur: 8px;
--token-cosmos-tip-shadow-inline-spread: 0px;
--token-cosmos-tip-shadow-inline-x: 0px;
--token-cosmos-tip-shadow-inline-y: 1px;
--token-cosmos-tip-shadow-none-blur: 0px;
--token-cosmos-tip-shadow-none-spread: 0px;
--token-cosmos-tip-shadow-none-x: 0px;
--token-cosmos-tip-shadow-none-y: 0px;
--token-inappnotification-shadow-blur-radius: 16px;
--token-inappnotification-shadow-opacity: .05;
--token-inappnotification-shadow-vertical-offset: 8px;
--token-mark-shadow-blur-radius: 4px;
--token-mark-shadow-opacity: .1;
--token-mark-shadow-vertical-offset: 2px;
--token-modal-shadow-opacity: .6;
--token-snackpill-shadow-blur-radius: 10px;
--token-snackpill-shadow-opacity: .2;
--token-snackpill-shadow-vertical-offset: 5px;
--token-tooltip-shadow-blur-radius: 10px;
--token-tooltip-shadow-opacity: .08;
--token-tooltip-shadow-vertical-offset: 4px;
```

### Radii

```css
--token-chat-bubble-radius: 16px;
--token-chat-bubble-radius-small: 4px;
--token-chat-date-pill-elevated-radius: 14px;
--token-chat-message-audio-bar-radius: 1.5px;
--token-chat-preview-message-quote-decoration-radius: 1px;
```

### Other

```css
--logo-width: 125px;
--token-action-cell-hint-typography: paragraph-3;
--token-action-cell-max-width: 480px;
--token-action-cell-title-typography: paragraph-1-bolder;
--token-actionsheet-gravity: center;
--token-actionsheet-header-background-base: #fff;
--token-actionsheet-item-height: 48px;
--token-audiobars-bar-fill-active-on-brand: #141414;
--token-audiobars-bar-fill-active-on-light: #141414;
--token-audiobars-bar-fill-inactive-on-brand: #0000003d;
--token-audiobars-bar-fill-inactive-on-light: #949494;
--token-button-max-width: 480px;
--token-button-medium-height: 48px;
--token-button-small-height: 40px;
--token-button-status-pressed-animation-duration-in: .1s;
--token-button-status-pressed-animation-duration-out: .1s;
--token-button-status-pressed-animation-timing-function-in: ease-in;
--token-button-status-pressed-animation-timing-function-out: cubic-bezier(.7,-.4,.4,1.4);
--token-button-status-pressed-overlay-dark-opacity: .15;
--token-button-status-pressed-overlay-tone-opacity: .08;
--token-button-status-pressed-scale: .95;
--token-chat-bubble-fix-width: 250px;
--token-chat-bubble-inset-horizontal: 12px;
--token-chat-bubble-inset-vertical: 8px;
--token-chat-bubble-rel-width: 80%;
--token-chat-composer-frame-height: 48px;
--token-chat-composer-mini-input-field-height: 36px;
--token-chat-date-pill-height: 28px;
--token-chat-input-field-height: 36px;
--token-chat-input-field-inset-horizontal: 12px;
--token-chat-item-content-width-fixed: 250px;
--token-chat-item-content-width-relative: 80%;
--token-chat-item-group-support: true;
--token-chat-list-inset-horizontal: 10px;
--token-chat-message-audio-bar-max-height: 20px;
--token-chat-message-audio-bar-opacity: .24;
--token-chat-message-audio-bar-width: 3px;
--token-chat-message-inset-horizontal: 12px;
--token-chat-message-inset-vertical: 8px;
--token-chat-message-reaction-emoji-safe-area: 8px;
--token-chat-message-reaction-media-max-height: 200px;
--token-chat-message-reaction-media-width: 250px;
--token-chat-message-reaction-notification-inset-horizontal: 12px;
--token-chat-message-reaction-notification-inset-vertical: 8px;
--token-chat-message-reaction-notification-width: 250px;
--token-chat-message-reaction-question-preview-inset-horizontal: 16px;
--token-chat-message-reaction-question-preview-inset-vertical: 16px;
--token-chat-message-reaction-question-preview-width: 250px;
--token-chat-panel-pills-item-height: 36px;
--token-chat-preview-message-quote-decoration-width: 2px;
--token-choice-status-disabled-opacity: .5;
--token-cosmos-actionbadge-sizing-asset: 18px;
--token-cosmos-actionbadge-sizing-emoji: 18px;
--token-cosmos-actionbadge-sizing-icon: 18px;
--token-cosmos-actionbadge-sizing-min-height: 44px;
--token-cosmos-actionbadge-sizing-navigation: 12px;
--token-cosmos-actionbadge-typography-content: action-small;
--token-cosmos-actioncell-sizing-emoji: 24px;
--token-cosmos-actioncell-sizing-icon: 24px;
--token-cosmos-actioncell-typography-content: action-small;
--token-cosmos-actionrow-sizing-chevron: 16px;
--token-cosmos-actionrow-sizing-icon-end: 16px;
--token-cosmos-actionrow-sizing-icon-start-medium: 40px;
--token-cosmos-actionrow-sizing-icon-start-small: 24px;
--token-cosmos-actionrow-sizing-min-height-small: 23px;
--token-cosmos-actionrow-typography-description: p2;
--token-cosmos-actionrow-typography-label: p3;
--token-cosmos-actionrow-typography-title-small: title;
--token-cosmos-badge-sizing-background-blur-alt: 40px;
--token-cosmos-badge-sizing-background-blur-brand: 20px;
--token-cosmos-badge-sizing-background-blur-default: 20px;
--token-cosmos-badge-sizing-background-blur-highlight: 20px;
--token-cosmos-badge-sizing-background-blur-inverse: 20px;
--token-cosmos-badge-sizing-emoji-micro: 12px;
--token-cosmos-badge-sizing-emoji-mini: 12px;
--token-cosmos-badge-sizing-emoji-small: 16px;
--token-cosmos-badge-sizing-icon-micro: 12px;
--token-cosmos-badge-sizing-icon-mini: 12px;
--token-cosmos-badge-sizing-icon-small: 16px;
--token-cosmos-badge-sizing-media-micro: 21px;
--token-cosmos-badge-sizing-media-mini: 25px;
--token-cosmos-badge-sizing-media-small: 37px;
--token-cosmos-badge-sizing-min-height-micro: 23px;
--token-cosmos-badge-sizing-min-height-mini: 27px;
--token-cosmos-badge-sizing-min-height-small: 39px;
--token-cosmos-badge-typography-micro: caption;
--token-cosmos-badge-typography-mini: action-mini;
--token-cosmos-badge-typography-small: action-small;
--token-cosmos-brick-sizing-background-blur-overlay: 20px;
--token-cosmos-brick-sizing-container-height-large: 64px;
--token-cosmos-brick-sizing-container-height-medium: 40px;
--token-cosmos-brick-sizing-container-height-small: 32px;
--token-cosmos-brick-sizing-container-height-xlarge: 96px;
--token-cosmos-brick-sizing-container-height-xsmall: 24px;
--token-cosmos-brick-sizing-container-width-compact-large: 48px;
--token-cosmos-brick-sizing-container-width-compact-medium: 32px;
--token-cosmos-brick-sizing-container-width-compact-small: 24px;
--token-cosmos-brick-sizing-container-width-compact-xlarge: 72px;
--token-cosmos-brick-sizing-container-width-compact-xsmall: 20px;
--token-cosmos-brick-sizing-container-width-default-large: 64px;
--token-cosmos-brick-sizing-container-width-default-medium: 40px;
--token-cosmos-brick-sizing-container-width-default-small: 32px;
--token-cosmos-brick-sizing-container-width-default-xlarge: 96px;
--token-cosmos-brick-sizing-container-width-default-xsmall: 24px;
--token-cosmos-brick-sizing-halo-large: 68px;
--token-cosmos-brick-sizing-halo-medium: 44px;
--token-cosmos-brick-sizing-halo-small: 34px;
--token-cosmos-brick-sizing-halo-xlarge: 104px;
--token-cosmos-brick-sizing-halo-xsmall: 26px;
--token-cosmos-brick-sizing-icon-default-large: 24px;
--token-cosmos-brick-sizing-icon-default-medium: 16px;
--token-cosmos-brick-sizing-icon-default-xlarge: 40px;
--token-cosmos-brick-sizing-icon-overlay-large: 24px;
--token-cosmos-brick-sizing-icon-overlay-medium: 16px;
--token-cosmos-brick-sizing-icon-overlay-small: 12px;
--token-cosmos-brick-sizing-icon-overlay-xlarge: 40px;
--token-cosmos-brick-sizing-icon-overlay-xsmall: 12px;
--token-cosmos-button-sizing-icon-medium: 20px;
--token-cosmos-button-sizing-icon-micro: 14px;
--token-cosmos-button-sizing-icon-mini: 16px;
--token-cosmos-button-sizing-icon-small: 18px;
--token-cosmos-button-sizing-max-width: 480px;
--token-cosmos-button-sizing-min-height-medium: 50px;
--token-cosmos-button-sizing-min-height-micro: 30px;
--token-cosmos-button-sizing-min-height-mini: 38px;
--token-cosmos-button-sizing-min-height-small: 44px;
--token-cosmos-button-typography-medium: action;
--token-cosmos-button-typography-micro: action-mini;
--token-cosmos-button-typography-mini: action-mini;
--token-cosmos-button-typography-small: action-small;
--token-cosmos-checkbox-sizing-container: 24px;
--token-cosmos-checkbox-sizing-icon: 16px;
--token-cosmos-ctabox-sizing-badge: 48px;
--token-cosmos-ctabox-typography-description: p1;
--token-cosmos-ctabox-typography-hint: p3;
--token-cosmos-ctabox-typography-title: h1;
--token-cosmos-dotcounternotification-sizing-circle: 8px;
--token-cosmos-dotcounternotification-sizing-min-width: 16px;
--token-cosmos-dotcounternotification-typography-content: caption;
--token-cosmos-emptystate-typography-description: p3;
--token-cosmos-emptystate-typography-title: h4;
--token-cosmos-filters-sizing-asset: 16px;
--token-cosmos-filters-sizing-emoji: 16px;
--token-cosmos-filters-sizing-icon: 16px;
--token-cosmos-filters-sizing-min-height: 38px;
--token-cosmos-filters-sizing-navigation: 16px;
--token-cosmos-filters-typography-content: action-mini;
--token-cosmos-forms-sizing-icon-medium: 24px;
--token-cosmos-forms-sizing-icon-small: 16px;
--token-cosmos-forms-typography-action: action;
--token-cosmos-forms-typography-counter: p3;
--token-cosmos-forms-typography-item: p2;
--token-cosmos-forms-typography-label: p3;
--token-cosmos-forms-typography-optional: p3;
--token-cosmos-forms-typography-placeholder: p1;
--token-cosmos-forms-typography-prefix: p1;
--token-cosmos-forms-typography-sufix: p1;
--token-cosmos-iconbutton-sizing-large-container: 48px;
--token-cosmos-iconbutton-sizing-large-icon: 24px;
--token-cosmos-iconbutton-sizing-large-wrapper: 40px;
--token-cosmos-iconbutton-sizing-medium-container: 48px;
--token-cosmos-iconbutton-sizing-medium-icon: 20px;
--token-cosmos-iconbutton-sizing-medium-wrapper: 36px;
--token-cosmos-iconbutton-sizing-small-container: 48px;
--token-cosmos-iconbutton-sizing-small-icon: 16px;
--token-cosmos-iconbutton-sizing-small-wrapper: 32px;
--token-cosmos-iconbutton-sizing-xlarge-container: 56px;
--token-cosmos-iconbutton-sizing-xlarge-icon: 24px;
--token-cosmos-iconbutton-sizing-xlarge-wrapper: 56px;
--token-cosmos-inappnotification-sizing-action: 48px;
--token-cosmos-inappnotification-sizing-background-blur: 20px;
--token-cosmos-inappnotification-sizing-icon: 16px;
--token-cosmos-inappnotification-typography-title: title;
--token-cosmos-mark-sizing-icon: 12px;
--token-cosmos-mark-sizing-min-width: 24px;
--token-cosmos-menu-sizing-icon: 20px;
--token-cosmos-menu-typography-content: action-small;
--token-cosmos-modal-sizing-background-blur: 20px;
--token-cosmos-modal-sizing-max-height: 90%;
--token-cosmos-modal-sizing-max-width: 528px;
--token-cosmos-navigationbar-sizing-background-blur: 4px;
--token-cosmos-navigationbar-sizing-height: 56px;
--token-cosmos-navigationbar-typography-action: action;
--token-cosmos-navigationbar-typography-description: p3;
--token-cosmos-navigationbar-typography-info: p1-bolder;
--token-cosmos-navigationbar-typography-title-medium: h1;
--token-cosmos-navigationbar-typography-title-small: h4;
--token-cosmos-nudge-sizing-icon: 40px;
--token-cosmos-nudge-typography-description: p2;
--token-cosmos-nudge-typography-hint: p3;
--token-cosmos-nudge-typography-title: h3;
--token-cosmos-paginationdots-opacity-default-unselected: 20%;
--token-cosmos-paginationdots-opacity-inverse-unselected: 50%;
--token-cosmos-paginationdots-sizing-circle-large: 8px;
--token-cosmos-paginationdots-sizing-circle-medium: 4px;
--token-cosmos-paginationdots-sizing-circle-small: 2px;
--token-cosmos-paginationdots-sizing-circle-xlarge: 24px;
--token-cosmos-progressbar-opacity-background-default: 20%;
--token-cosmos-progressbar-opacity-background-inverse: 50%;
--token-cosmos-progressbar-sizing-height: 4px;
--token-cosmos-progresscircle-opacity-background-default: 20%;
--token-cosmos-progresscircle-opacity-background-inverse: 50%;
--token-cosmos-progresscircle-sizing-width: 4%;
--token-cosmos-radiobutton-sizing-medium: 24px;
--token-cosmos-radiobutton-sizing-small: 12px;
--token-cosmos-search-sizing-height: 48px;
--token-cosmos-search-sizing-icon-left: 20px;
--token-cosmos-search-typography-action: action;
--token-cosmos-search-typography-content: p1;
--token-cosmos-semantic-aspect-ratio-1-1-height: 100%;
--token-cosmos-semantic-aspect-ratio-1-1-width: 100%;
--token-cosmos-semantic-aspect-ratio-16-9-height: 56.25%;
--token-cosmos-semantic-aspect-ratio-16-9-width: 100%;
--token-cosmos-semantic-aspect-ratio-3-2-height: 66.6%;
--token-cosmos-semantic-aspect-ratio-3-2-width: 100%;
--token-cosmos-semantic-aspect-ratio-3-4-height: 100%;
--token-cosmos-semantic-aspect-ratio-3-4-width: 75%;
--token-cosmos-semantic-aspect-ratio-4-3-height: 75%;
--token-cosmos-semantic-aspect-ratio-4-3-width: 100%;
--token-cosmos-semantic-aspect-ratio-4-5-height: 80%;
--token-cosmos-semantic-aspect-ratio-4-5-width: 100%;
--token-cosmos-semantic-aspect-ratio-9-16-height: 100%;
--token-cosmos-semantic-aspect-ratio-9-16-width: 56.25%;
--token-cosmos-semantic-motion-duration-extralong-1: .7s;
--token-cosmos-semantic-motion-duration-extralong-2: .8s;
--token-cosmos-semantic-motion-duration-extralong-3: .9s;
--token-cosmos-semantic-motion-duration-extralong-4: 1s;
--token-cosmos-semantic-motion-duration-long-1: .45s;
--token-cosmos-semantic-motion-duration-long-2: .5s;
--token-cosmos-semantic-motion-duration-long-3: .55s;
--token-cosmos-semantic-motion-duration-long-4: .6s;
--token-cosmos-semantic-motion-duration-medium-1: .25s;
--token-cosmos-semantic-motion-duration-medium-2: .3s;
--token-cosmos-semantic-motion-duration-medium-3: .35s;
--token-cosmos-semantic-motion-duration-medium-4: .4s;
--token-cosmos-semantic-motion-duration-short-1: 50ms;
--token-cosmos-semantic-motion-duration-short-2: .1s;
--token-cosmos-semantic-motion-duration-short-3: .15s;
--token-cosmos-semantic-motion-duration-short-4: .2s;
--token-cosmos-semantic-motion-easing-standard: cubic-bezier(.2,0,0,1);
--token-cosmos-semantic-motion-easing-standard-accelerate: cubic-bezier(.3,0,1,1);
--token-cosmos-semantic-motion-easing-standard-decelerate: cubic-bezier(0,0,0,1);
--token-cosmos-semantic-opacity-0: 0%;
--token-cosmos-semantic-opacity-10: 10%;
--token-cosmos-semantic-opacity-100: 100%;
--token-cosmos-semantic-opacity-20: 20%;
--token-cosmos-semantic-opacity-30: 30%;
--token-cosmos-semantic-opacity-40: 40%;
--token-cosmos-semantic-opacity-5: 5%;
--token-cosmos-semantic-opacity-50: 50%;
--token-cosmos-semantic-opacity-60: 60%;
--token-cosmos-semantic-opacity-70: 70%;
--token-cosmos-semantic-opacity-80: 80%;
--token-cosmos-semantic-opacity-90: 90%;
--token-cosmos-semantic-sizing-0: 0px;
--token-cosmos-semantic-sizing-12: 12px;
--token-cosmos-semantic-sizing-16: 16px;
--token-cosmos-semantic-sizing-2: 2px;
--token-cosmos-semantic-sizing-20: 20px;
--token-cosmos-semantic-sizing-24: 24px;
--token-cosmos-semantic-sizing-32: 32px;
--token-cosmos-semantic-sizing-36: 36px;
--token-cosmos-semantic-sizing-4: 4px;
--token-cosmos-semantic-sizing-40: 40px;
--token-cosmos-semantic-sizing-48: 48px;
--token-cosmos-semantic-sizing-56: 56px;
--token-cosmos-semantic-sizing-6: 6px;
--token-cosmos-semantic-sizing-64: 64px;
--token-cosmos-semantic-sizing-72: 72px;
--token-cosmos-semantic-sizing-8: 8px;
--token-cosmos-semantic-sizing-80: 80px;
--token-cosmos-semantic-sizing-blur-layered: 20px;
--token-cosmos-semantic-sizing-blur-tertiary: 40px;
--token-cosmos-semantic-sizing-icon-large: 40px;
--token-cosmos-semantic-sizing-icon-medium: 24px;
--token-cosmos-semantic-sizing-icon-small: 20px;
--token-cosmos-semantic-sizing-icon-xsmall: 16px;
--token-cosmos-semantic-sizing-icon-xxsmall: 12px;
--token-cosmos-snackpill-sizing-icon: 16px;
--token-cosmos-snackpill-typography-content: p2;
--token-cosmos-tabbar-sizing-icon: 24px;
--token-cosmos-tabs-sizing-icon: 24px;
--token-cosmos-tip-sizing-icon-start-medium: 40px;
--token-cosmos-tip-sizing-icon-start-small: 24px;
--token-cosmos-tip-sizing-min-height-container: 48px;
--token-cosmos-tip-typography-description: p2;
--token-cosmos-tip-typography-title: title;
--token-cosmos-toggle-sizing-handle: 16px;
--token-cosmos-tooltip-sizing-beak-height: 8px;
--token-cosmos-tooltip-sizing-beak-width: 12px;
--token-cosmos-tooltip-typography-content: p2-bolder;
--token-date-field-item-min-width-2: 56px;
--token-date-field-item-min-width-4: 78px;
--token-dotcounternotification-animation-timing-bounce: .9s;
--token-dotcounternotification-animation-timing-popout: 5s;
--token-dotcounternotification-counter-placement-bottom-shift-top: -5px;
--token-dotcounternotification-counter-placement-center-shift-top: -50%;
--token-floating-action-button-status-pressed-animation-duration-in: .1s;
--token-floating-action-button-status-pressed-animation-duration-out: .1s;
--token-floating-action-button-status-pressed-animation-timing-function-in: ease-in;
--token-floating-action-button-status-pressed-animation-timing-function-out: cubic-bezier(.7,-.4,.4,1.4);
--token-floating-action-button-status-pressed-scale: .95;
--token-form-max-width: 480px;
--token-inappnotification-content-inset-horizontal: 16px;
--token-inappnotification-content-inset-vertical: 16px;
--token-input-toggle-height: 24px;
--token-input-toggle-width: 40px;
--token-interest-medium-height: 36px;
--token-interest-small-height: 30px;
--token-interest-status-disabled-opacity: .4;
--token-lifestylebadge-height: 30px;
--token-match-photos-image-left-rotate: -12;
--token-match-photos-image-left-stack-index: 1;
--token-match-photos-image-left-translate-x: 3.3000000000000003%;
--token-match-photos-image-left-translate-y: 7.7%;
--token-match-photos-image-right-rotate: 12;
--token-match-photos-image-right-stack-index: 2;
--token-match-photos-image-right-translate-x: -3.3000000000000003%;
--token-match-photos-image-right-translate-y: 7.7%;
--token-media-overlay-background-opacity: .4;
--token-modal-max-height: 90%;
--token-modal-max-width: 528px;
--token-navigation-bar-height: 50px;
--token-navigation-bar-logo-height: 36px;
--token-navigation-bar-profile-additional-heading-overlap: 4px;
--token-navigation-bar-slot-min-width: 44px;
--token-pagination-dots-animation-timing-transition: .3s;
--token-pagination-dots-dot-exploration-scaling-factor-p1: 1;
--token-pagination-dots-dot-exploration-scaling-factor-p2: .666;
--token-pagination-dots-dot-exploration-scaling-factor-p3: .333;
--token-pagination-dots-dot-exploration-scaling-factor-p4: 0;
--token-pagination-dots-dot-opacity-active: 1;
--token-pagination-dots-dot-opacity-base: .4;
--token-phone-field-country-code-width: 110px;
--token-phone-field-number-overlap: 2px;
--token-progress-bar-heigh: 4px;
--token-progress-bar-height: 4px;
--token-search-height: 36px;
--token-select-height: 56px;
--token-tabbar-height: 52px;
--token-tabbar-notification-center-position-left: 21.5px;
--token-tabbar-notification-center-position-top: 2.5px;
--token-tabs-item-min-width: 44px;
--token-toggle-height: 24px;
--token-toggle-width: 40px;
--token-tooltip-arrow-offset: 18px;
--token-tooltip-offset: 16px;
--token-view-profile-block-block-inset: 24px;
--control-height-medium: 48px;
--ui-kit-content-max-inner-width: 1360px;
--ui-kit-content-max-width: 1440px;
--header-z-index: 100;
--over-content-z-index: 10;
--content-max-inner-width: 1218px;
--content-max-width: calc(var(--content-max-inner-width) + 2 * var(--content-section-padding-horizontal));
--header-min-height: 64px;
--screen-height: 100dvh;
```

### Dependencies

```css
--color-ui-kit-text-default: --token-cosmos-semantic-color-text-default;
--color-ui-kit-text-subdued: --token-cosmos-semantic-color-text-subdued;
--color-ui-kit-text-error: --token-cosmos-semantic-color-text-error;
--color-ui-kit-text-inverse: --token-cosmos-semantic-color-text-inverse;
--color-ui-kit-text-yellow: --token-cosmos-button-color-background-primary-yellow;
--color-ui-kit-link-default: --token-cosmos-semantic-color-text-links;
--color-ui-kit-link-hover: --token-cosmos-semantic-color-text-links;
--styleguide-cell-color-background-brand: --token-cosmos-button-color-background-primary-yellow;
--content-max-width: --content-max-inner-width,--content-section-padding-horizontal;
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
| xs | 349px | max-width |
| 412px | 412px | min-width |
| sm | 600px | min-width |
| sm | 640px | min-width |
| sm | 641px | min-width |
| sm | 660px | min-width |
| sm | 680px | min-width |
| md | 767px | max-width |
| md | 768px | max-width |
| md | 780px | min-width |
| 900px | 900px | min-width |
| lg | 960px | min-width |
| lg | 1024px | min-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | min-width |
| xl | 1260px | min-width |
| xl | 1320px | min-width |
| 1360px | 1360px | min-width |
| 1420px | 1420px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.2s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: position 0.2s;
transition: opacity 0.2s;
transition: top 0.3s;
transition: transform 0.2s ease-in-out, -webkit-transform 0.2s ease-in-out;
transition: color 0.2s;
```

### Keyframe Animations

**slide-in__RfrZB**
```css
@keyframes slide-in__RfrZB {
  0% { opacity: 0; translate: 0px -40px; }
  100% { opacity: 1; translate: 0px; }
}
```

**slide-in__RfrZB**
```css
@keyframes slide-in__RfrZB {
  0% { opacity: 0; translate: 0px -40px; }
  100% { opacity: 1; translate: 0px; }
}
```

**slide-out__Wb3Nw**
```css
@keyframes slide-out__Wb3Nw {
  0% { opacity: 1; translate: 0px; }
  100% { opacity: 0; translate: 0px 40px; }
}
```

**slide-out__Wb3Nw**
```css
@keyframes slide-out__Wb3Nw {
  0% { opacity: 1; translate: 0px; }
  100% { opacity: 0; translate: 0px 40px; }
}
```

**swap-card-1__xJrIz**
```css
@keyframes swap-card-1__xJrIz {
  0% { opacity: 1; transform: scale(1) translate(0px); }
  100% { opacity: 0; transform: scale(1.1) translate(-100px); }
}
```

**swap-card-1__xJrIz**
```css
@keyframes swap-card-1__xJrIz {
  0% { opacity: 1; transform: scale(1) translate(0px); }
  100% { opacity: 0; transform: scale(1.1) translate(-100px); }
}
```

**swap-card-2__dhyx2**
```css
@keyframes swap-card-2__dhyx2 {
  0% { transform: scale(0.75) translate(250px); }
  100% { transform: scale(1) translate(0px); }
}
```

**swap-card-2__dhyx2**
```css
@keyframes swap-card-2__dhyx2 {
  0% { transform: scale(0.75) translate(250px); }
  100% { transform: scale(1) translate(0px); }
}
```

**swap-card-3__qx2GS**
```css
@keyframes swap-card-3__qx2GS {
  0% { transform: scale(0.5) translate(680px); }
  100% { transform: scale(0.75) translate(250px); }
}
```

**swap-card-3__qx2GS**
```css
@keyframes swap-card-3__qx2GS {
  0% { transform: scale(0.5) translate(680px); }
  100% { transform: scale(0.75) translate(250px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (14 instances)

```css
.button {
  background-color: rgb(32, 32, 32);
  color: rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
  padding-top: 14px;
  padding-right: 24px;
  border-radius: 16px;
}
```

### Cards (46 instances)

```css
.card {
  background-color: rgb(255, 219, 91);
  border-radius: 0px;
  box-shadow: rgba(32, 32, 32, 0.12) 0px 1px 8px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (94 instances)

```css
.link {
  color: rgb(87, 86, 86);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (31 instances)

```css
.navigatio {
  background-color: rgba(255, 255, 255, 0.8);
  color: rgb(32, 32, 32);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (10 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(32, 32, 32);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (3 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 1440px;
}
```

### Dropdowns (136 instances)

```css
.dropdown {
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 0px;
  border-color: rgb(87, 86, 86);
  padding-top: 0px;
}
```

### Badges (5 instances)

```css
.badge {
  background-color: rgb(255, 219, 91);
  color: rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(32, 32, 32);
  color: rgb(255, 255, 255);
  padding: 14px 24px 14px 24px;
  border-radius: 25px;
  border: 0px solid rgba(32, 32, 32, 0.12);
  font-size: 16px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 18px;
  font-weight: 500;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 14px 22px 14px 22px;
  border-radius: 0px;
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 17px;
  font-weight: 500;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(255, 255, 255, 0.8);
  color: rgb(87, 86, 86);
  padding: 12px 24px 12px 24px;
  border-radius: 16px;
  border: 1px solid rgba(32, 32, 32, 0.08);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Card — 9 instances, 1 variant

**Variant 1** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Card — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgba(0, 0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgba(0, 0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 40px 0px 40px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgb(255, 219, 91);
  color: rgb(32, 32, 32);
  padding: 20px 20px 20px 20px;
  border-radius: 24px;
  border: 1px solid rgba(32, 32, 32, 0.08);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 60px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(255, 219, 91);
  color: rgb(52, 51, 51);
  padding: 20px 10px 20px 10px;
  border-radius: 1000px;
  border: 0px none rgb(52, 51, 51);
  font-size: 40px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 24px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

### Link — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 17px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(32, 32, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 32, 32);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**2 grid containers** and **91 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1360px | 0px |
| 1440px | 40px |
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 2x |

### Grid Templates

```css
grid-template-columns: 560px 620px;
gap: 20px;
grid-template-columns: 580px 580px;
gap: 40px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 51x |
| column/nowrap | 40x |

**Gap values:** `0px 8px`, `10px`, `12px`, `15px`, `16px`, `20px`, `24px`, `26px`, `32px`, `34px`, `40px`, `48px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 93/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 90/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 114 !important rules — prefer specificity over overrides
- 79% of CSS is unused — consider purging
- 16724 duplicate CSS declarations

## Z-Index Map

**10 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div |
| dropdown | 101,101 | div.s.k.i.p.-.l.i.n.k |
| sticky | 10,10 | div.d.r.o.p.d.o.w.n.-.d.r.o.p.d.o.w.n._._.Z.s.-.k.r. .d.r.o.p.d.o.w.n.-.d.r.o.p.d.o.w.n.-.-.h.a.s.-.m.a.x.-.h.e.i.g.h.t._._.e.f.8.O.e, div.d.r.o.p.d.o.w.n.-.d.r.o.p.d.o.w.n._._.Z.s.-.k.r. .d.r.o.p.d.o.w.n.-.d.r.o.p.d.o.w.n.-.-.h.a.s.-.m.a.x.-.h.e.i.g.h.t._._.e.f.8.O.e |
| base | 0,6 | div.c.a.r.o.u.s.e.l.-.s.t.a.c.k.e.d.-.c.a.r.d.s._._.c.a.r.d.s.-.i.n.n.e.r._._.u.L.Z.j.I, div.h.e.a.d.e.r.-.c.o.n.t.a.i.n.e.r._._.n.a.v._._.G.S.y.P.J, div.h.e.a.d.e.r.-.c.o.n.t.a.i.n.e.r._._.m.o.d.a.l._._.U.R.f.0.k |

**Issues:**
- [object Object]

## SVG Icons

**12 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| md | 10 |
| xl | 2 |

**Icon colors:** `currentColor`, `#202020`, `white`, `#25F4EE`, `#FE2C55`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| BumbleSans | self-hosted | 400, 500, 600, 700 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 12 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 4 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 3 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (6x), 9:16 (6x), 3:4 (4x), 16:9 (2x), 4:3 (1x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

### Easing Families

- **ease-in-out** (1 uses) — `ease`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `swap-card-1__xJrIz` | slide | opacity, transform | 3 |
| `swap-card-1__xJrIz` | slide | opacity, transform | 3 |
| `swap-card-2__dhyx2` | slide | transform | 1 |
| `swap-card-2__dhyx2` | slide | transform | 1 |
| `swap-card-3__qx2GS` | slide | transform | 1 |
| `swap-card-3__qx2GS` | slide | transform | 1 |
| `swap-card-4__-SUId` | slide | opacity, transform | 1 |
| `swap-card-4__-SUId` | slide | opacity, transform | 1 |

## Component Anatomy

### card — 41 instances

**Slots:** media, footer

### button — 18 instances

**Slots:** label
**Variants:** primary
**Sizes:** medium

| variant | count | sample label |
|---|---|---|
| default | 17 | Skip to main content |
| primary | 1 | Skip to main content |

### link — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **download** (4)
- **skip** (3)
- **sign** (3)
- **read** (3)
- **find** (2)
- **date** (1)
- **bff** (1)
- **stories** (1)

### Button Copy Patterns

- "skip to main content" (3×)
- "download bumble" (3×)
- "sign up" (3×)
- "read more stories" (3×)
- "date" (1×)
- "bff" (1×)
- "stories" (1×)
- "find your person" (1×)
- "find your people" (1×)
- "download the appenglish (united states)english (united kingdom)english (canada)english (australia)english (india)deutschfrançaisfrançais (canada)español (españa" (1×)

### Sample Headings

> We exist to bring people closer to love.
> Share your ideas
> Bumble Date
> BFF
> We exist to bring people closer to love.
> Share your ideas
> Get the app
> Our apps
> Company
> Legal

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Bumble is a social network that allows you to feel empowered while making connections, whether you're dating or looking for friends.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → feature-grid → nav → gallery → cta → gallery → cta → footer → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | feature-grid | — | 0.8 |
| 3 | gallery | We exist to bring people closer to love. | 0.7 |
| 4 | cta | Share your ideas | 0.75 |
| 5 | gallery | — | 0.7 |
| 6 | cta | Get the app | 0.75 |
| 7 | footer | Our apps | 0.95 |
| 8 | nav | Our apps | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.269 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 1000px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0.026)
**Counts:** total 19, svg 1, icon 4, screenshot-like 0, photo-like 0
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `BumbleSans` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
