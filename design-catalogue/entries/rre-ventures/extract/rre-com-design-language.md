# Design Language: RRE: Early-Stage Venture Capital Partner

> Extracted from `https://rre.com/` on September 4, 2026
> 577 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#3898ec` | rgb(56, 152, 236) | hsl(208, 83%, 57%) | 1 |
| Secondary | `#07020a` | rgb(7, 2, 10) | hsl(278, 67%, 2%) | 322 |
| Accent | `#6ccfff` | rgb(108, 207, 255) | hsl(200, 100%, 71%) | 7 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#ffffff` | hsl(0, 0%, 100%) | 889 |
| `#333333` | hsl(0, 0%, 20%) | 4 |
| `#cccccc` | hsl(0, 0%, 80%) | 2 |

### Background Colors

Used on large-area elements: `#07020a`, `#d3e7f1`, `#ffffff`, `#6ccfff`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#333333`, `#07020a`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#ffffff` | text, border, background | 889 |
| `#07020a` | text, border, background | 322 |
| `#6ccfff` | background | 7 |
| `#333333` | text, border | 4 |
| `#d3e7f1` | background | 2 |
| `#cccccc` | border | 2 |
| `#3898ec` | background | 1 |
| `#ffdede` | background | 1 |

## Typography

### Font Families

- **RRE Monument Grotesk Trial** — used for all (550 elements)
- **webflow-icons** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 80px | 5rem | 400 | 88px | -4px | h1, div |
| 56px | 3.5rem | 400 | 56px | -2px | h2, div, h3, a |
| 32px | 2rem | 400 | 38.4px | normal | h3 |
| 24px | 1.5rem | 400 | 33.6px | normal | div |
| 20px | 1.25rem | 400 | 28px | normal | body, div, style, iframe |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 15px | 0.9375rem | 400 | 21px | normal | a, div, svg, path |
| 12px | 0.75rem | 400 | 16.8px | normal | div |

### Heading Scale

```css
h1 { font-size: 80px; font-weight: 400; line-height: 88px; }
h2 { font-size: 56px; font-weight: 400; line-height: 56px; }
h3 { font-size: 32px; font-weight: 400; line-height: 38.4px; }
h3 { font-size: 20px; font-weight: 400; line-height: 28px; }
```

### Body Text

```css
body { font-size: 15px; font-weight: 400; line-height: 21px; }
```

### Font Weights in Use

`400` (577x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-48 | 48px | 3rem |
| spacing-78 | 78px | 4.875rem |
| spacing-96 | 96px | 6rem |
| spacing-128 | 128px | 8rem |
| spacing-200 | 200px | 12.5rem |

## CSS Custom Properties

### Colors

```css
--_theme---text-color--primary: var(--neutral--white);
--_theme---text-color--alternate: var(--neutral--black);
--_theme---background--primary: var(--neutral--black);
--_theme---text-color--secondary: var(--neutral--light-80);
--_theme---text-color--success: var(--_theme---system--success-text);
--_theme---border-color--primary: var(--neutral--dark-90);
--_theme---background--secondary: var(--brand--light-powder-blue);
--_theme---text-color--tertiary: var(--neutral--light-50);
--_theme---link-color--primary: var(--_theme---text-color--primary);
--_theme---text-color--error: var(--_theme---system--error-text);
--_theme---text-color--warning: var(--_theme---system--warning-text);
--brand--primary: #6ccfff;
--_theme---link-color--secondary: var(--neutral--black);
--_sizes---border-radius--small: .25rem;
--_sizes---border-width--thin: 1px;
--_sizes---border-width--normal: .125rem;
--_sizes---border-width--bold: .25rem;
--_sizes---border-radius--medium: .5rem;
--_sizes---border-radius--large: 1rem;
--_theme---border-color--secondary: var(--brand--blue\<deleted\|variable-de000a4d-0fee-1f9e-af85-624658122d10\>);
--_theme---border-color--alternate: var(--neutral--dark-10);
--_theme---link-color--alternate: var(--neutral--white);
--swiper-theme-color: #007aff;
```

### Spacing

```css
--_typography---body--body-font-size: var(--_typography---font-size--regular);
--_typography---body--body-letter-spacing: var(--_typography---letter-spacing--default);
--_typography---h1--h1-font-size: 5rem;
--_typography---h1--h1-letter-spacing: var(--_typography---letter-spacing--tighter);
--_typography---h2--h2-font-size: 3.5rem;
--_typography---h2--h2-letter-spacing: var(--_typography---letter-spacing--tight);
--_typography---h3--h3-font-size: 2rem;
--_typography---h3--h3-letter-spacing: var(--_typography---letter-spacing--default);
--_typography---h4--h4-font-size: 1.25rem;
--_typography---h4--h4-letter-spacing: var(--_typography---letter-spacing--tighter);
--_typography---h5--h5-font-size: .875rem;
--_typography---h5--h5-letter-spacing: var(--_typography---letter-spacing--tight);
--_typography---h6--h6-font-size: .75rem;
--_typography---h6--h6-letter-spacing: var(--_typography---letter-spacing--tight);
--_layout---spacing--xxsmall: .25rem;
--_layout---spacing--xlarge: 4rem;
--_layout---spacing--xsmall: .5rem;
--_layout---spacing--huge: 6rem;
--_layout---spacing--large: 3rem;
--_layout---spacing--xxlarge: 5rem;
--_layout---spacing--tiny: .125rem;
--_layout---spacing--small: 1rem;
--_layout---spacing--medium: 2rem;
--_sizes---container--small: 48rem;
--_layout---spacing--global-padding: 5rem;
--_layout---section-padding--small: 3rem;
--_sizes---max-width--small: 24rem;
--_typography---font-size--tiny: .8125rem;
--_sizes---max-width--xxlarge: 80rem;
--_sizes---max-width--xsmall: 16rem;
--_typography---font-size--regular: 1.25rem;
--_sizes---max-width--medium: 32rem;
--_sizes---max-width--large: 48rem;
--_typography---font-size--small: .9375rem;
--_sizes---max-width--xlarge: 64rem;
--_layout---section-padding--large: 8rem;
--_typography---font-size--large: 1.5rem;
--_sizes---container--large: 85rem;
--_sizes---max-width--xxsmall: 12rem;
--_typography---font-size--huge: 7.5rem;
--_layout---section-padding--medium: 5rem;
--_sizes---container--medium: 64rem;
--_layout---spacing--none: 0rem;
--_layout---spacing--xhuge: 8rem;
--_layout---spacing--xxhuge: 12rem;
--_layout---spacing--xsmall-plus: .75rem;
--_layout---spacing--small-plus: 1.5rem;
--_layout---gaps--regular: 2rem;
--_typography---font-size--eyebrow: .75rem;
--_layout---gaps--medium: 3rem;
--_typography---letter-spacing--tighter: -.25rem;
--_typography---letter-spacing--tight: -.125rem;
--_typography---letter-spacing--default: 0rem;
--_typography---letter-spacing--wide: .125rem;
--_typography---letter-spacing--wider: .25rem;
--_layout---gaps--small: 1.5rem;
--_layout---gaps--large: 4rem;
--_layout---gaps--zero: 0rem;
--swiper-navigation-size: 44px;
```

### Typography

```css
--font-family--body: "RRE Monument Grotesk Trial",Arial,sans-serif;
--_typography---body--body-line-height: var(--_typography---font-height--large);
--font-weight--normal: 400;
--font-family--heading: "RRE Monument Grotesk Trial",Arial,sans-serif;
--_typography---h1--h1-line-height: var(--_typography---font-height--small);
--_typography---h1--h1-font-weight: var(--font-weight--normal);
--_typography---h2--h2-line-height: var(--_typography---font-height--tiny-plus);
--_typography---h2--h2-font-weight: var(--font-weight--normal);
--_typography---h3--h3-line-height: var(--_typography---font-height--medium);
--_typography---h3--h3-font-weight: var(--font-weight--normal);
--_typography---h4--h4-line-height: var(--_typography---font-height--small);
--_typography---h4--h4-font-weight: var(--font-weight--normal);
--_typography---h5--h5-line-height: var(--_typography---font-height--tiny);
--_typography---h5--h5-font-weight: var(--font-weight--normal);
--_typography---h6--h6-line-height: var(--_typography---font-height--tiny-plus);
--_typography---h6--h6-font-weight: var(--font-weight--normal);
--font-weight--semi-bold: 600;
--font-weight--medium: 500;
--font-weight--light: 300;
--font-weight--xbold: 800;
--font-weight--bold: 700;
--_typography---font-height--tiny: .95;
--_typography---body--body-font-weight: var(--font-weight--normal);
--_typography---font-height--tiny-plus: 1;
--_typography---font-height--small: 1.1;
--_typography---font-height--medium: 1.2;
--_typography---font-height--large: 1.4;
--_typography---font-height--xlarge: 1.5;
--font-weight--thin: 100;
--font-weight--xlight: 200;
--font-weight--black: 900;
--_theme---system--success-text: var(--brand--green-darker\<deleted\|variable-af4a66ed-29aa-6390-d88f-85bf78389f92\>);
--_theme---system--warning-text: var(--brand--yellow-darker\<deleted\|variable-e2069969-82a7-5819-d260-1d46a98a5b09\>);
--_theme---system--error-text: var(--brand--red-darker\<deleted\|variable-0e7bdc29-3f49-d18d-fc12-7f927e485f61\>);
--_theme---system--selection-text: var(--neutral--white);
```

### Other

```css
--neutral--black: var(--brand--black);
--_theme---background--success: var(--_theme---system--success-background);
--_theme---background--alternate: var(--brand--primary);
--_theme---background--tertiary-not-in-use<deleted|variable-6632d948-2d2d-2556-731d-05a71c92f234>: var(--brand--pink\<deleted\|variable-c4661572-8a15-7367-e98c-cc1a0987f6d1\>);
--_theme---background--error: var(--_theme---system--error-background);
--_theme---background--warning: var(--_theme---system--warning-background);
--neutral--white: #fff;
--neutral--dark-90: #07020ae6;
--neutral--transparent: transparent;
--neutral--dark-50: #07020a80;
--brand--light-powder-blue: #d3e7f1;
--brand--black: #07020a;
--neutral--dark-70: #07020ab3;
--neutral--dark-2: #07020a05;
--neutral--dark-30: #07020a4d;
--neutral--dark-15: #07020a26;
--neutral--dark-10: #07020a1a;
--neutral--dark-5: #07020a0d;
--neutral--light-90: #d3e7f1e6;
--neutral--light-80: #d3e7f1cc;
--neutral--light-70: #d3e7f1b3;
--neutral--light-50: #d3e7f180;
--neutral--light-30: #d3e7f14d;
--neutral--light-15: #d3e7f126;
--neutral--light-10: #d3e7f11a;
--neutral--light-5: #d3e7f10d;
--neutral--light-2: #d3e7f105;
--focus--width: .125rem;
--focus--offset: .125rem;
--_layout---grid-columns--default-count: 8;
--_layout---grid-columns--xsmall: 15rem;
--_layout---grid-columns--small: 20rem;
--_layout---grid-columns--medium: 25rem;
--_layout---grid-columns--large: 30rem;
--_layout---grid-columns--xlarge: 35rem;
--_layout---grid-columns--xxlarge: 40rem;
--_theme---system--success-background: var(--brand--green\<deleted\|variable-250c51ef-9593-472e-ebda-2eee102638aa\>);
--_theme---system--warning-background: var(--brand--yellow\<deleted\|variable-32cfb3c9-dd46-3c5b-bfbe-c5b8defe4663\>);
--_theme---system--error-background: var(--brand--red\<deleted\|variable-15c39f21-4118-4533-342f-c29e9852fd79\>);
--_theme---system--focus-state: var(--brand--blue\<deleted\|variable-de000a4d-0fee-1f9e-af85-624658122d10\>);
--_theme---system--selection-background: var(--brand--blue\<deleted\|variable-de000a4d-0fee-1f9e-af85-624658122d10\>);
--brand--pink<deleted|variable-c4661572-8a15-7367-e98c-cc1a0987f6d1>: #dd23bb;
--brand--blue<deleted|variable-de000a4d-0fee-1f9e-af85-624658122d10>: #2d62ff;
--brand--green<deleted|variable-250c51ef-9593-472e-ebda-2eee102638aa>: #cef5ca;
--brand--green-darker<deleted|variable-af4a66ed-29aa-6390-d88f-85bf78389f92>: #114e0b;
--brand--yellow<deleted|variable-32cfb3c9-dd46-3c5b-bfbe-c5b8defe4663>: #fcf8d8;
--brand--yellow-darker<deleted|variable-e2069969-82a7-5819-d260-1d46a98a5b09>: #5e5515;
--brand--red<deleted|variable-15c39f21-4118-4533-342f-c29e9852fd79>: #f8e4e4;
--brand--red-darker<deleted|variable-0e7bdc29-3f49-d18d-fc12-7f927e485f61>: #3b0b0b;
```

### Dependencies

```css
--neutral--black: --brand--black;
--_theme---text-color--primary: --neutral--white;
--_typography---body--body-font-size: --_typography---font-size--regular;
--_typography---body--body-line-height: --_typography---font-height--large;
--_typography---body--body-letter-spacing: --_typography---letter-spacing--default;
--_typography---h1--h1-line-height: --_typography---font-height--small;
--_typography---h1--h1-font-weight: --font-weight--normal;
--_typography---h1--h1-letter-spacing: --_typography---letter-spacing--tighter;
--_typography---h2--h2-line-height: --_typography---font-height--tiny-plus;
--_typography---h2--h2-font-weight: --font-weight--normal;
--_typography---h2--h2-letter-spacing: --_typography---letter-spacing--tight;
--_typography---h3--h3-line-height: --_typography---font-height--medium;
--_typography---h3--h3-font-weight: --font-weight--normal;
--_typography---h3--h3-letter-spacing: --_typography---letter-spacing--default;
--_typography---h4--h4-line-height: --_typography---font-height--small;
--_typography---h4--h4-font-weight: --font-weight--normal;
--_typography---h4--h4-letter-spacing: --_typography---letter-spacing--tighter;
--_typography---h5--h5-line-height: --_typography---font-height--tiny;
--_typography---h5--h5-font-weight: --font-weight--normal;
--_typography---h5--h5-letter-spacing: --_typography---letter-spacing--tight;
--_typography---h6--h6-line-height: --_typography---font-height--tiny-plus;
--_typography---h6--h6-font-weight: --font-weight--normal;
--_typography---h6--h6-letter-spacing: --_typography---letter-spacing--tight;
--_theme---text-color--alternate: --neutral--black;
--_theme---background--primary: --neutral--black;
--_theme---text-color--secondary: --neutral--light-80;
--_theme---background--success: --_theme---system--success-background;
--_theme---text-color--success: --_theme---system--success-text;
--_theme---border-color--primary: --neutral--dark-90;
--_theme---background--alternate: --brand--primary;
--_theme---background--secondary: --brand--light-powder-blue;
--_theme---text-color--tertiary: --neutral--light-50;
--_theme---link-color--primary: --_theme---text-color--primary;
--_theme---background--tertiary-not-in-use<deleted|variable-6632d948-2d2d-2556-731d-05a71c92f234>: --brand--pink;
--_theme---background--error: --_theme---system--error-background;
--_theme---text-color--error: --_theme---system--error-text;
--_theme---background--warning: --_theme---system--warning-background;
--_theme---text-color--warning: --_theme---system--warning-text;
--_theme---link-color--secondary: --neutral--black;
--_typography---body--body-font-weight: --font-weight--normal;
--_theme---border-color--secondary: --brand--blue;
--_theme---border-color--alternate: --neutral--dark-10;
--_theme---link-color--alternate: --neutral--white;
--_theme---system--success-background: --brand--green;
--_theme---system--success-text: --brand--green-darker;
--_theme---system--warning-background: --brand--yellow;
--_theme---system--warning-text: --brand--yellow-darker;
--_theme---system--error-background: --brand--red;
--_theme---system--error-text: --brand--red-darker;
--_theme---system--focus-state: --brand--blue;
--_theme---system--selection-text: --neutral--white;
--_theme---system--selection-background: --brand--blue;
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
| sm | 479px | max-width |
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 991px | min-width |
| 2xl | 1520px | min-width |
| 1920px | 1920px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.2s`, `0.3s`, `0.4s`

### Common Transitions

```css
transition: all;
transition: filter 0.2s, height 0.2s;
transition: 0.3s;
transition: color 0.2s;
transition: background-color 0.3s, color 0.3s;
transition: transform 0.3s;
transition: height 0.2s;
transition: opacity 0.3s;
transition: transform;
transition: opacity;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (10 instances)

```css
.button {
  background-color: rgba(239, 239, 239, 0);
  color: rgb(255, 255, 255);
  font-size: 15px;
  font-weight: 400;
  padding-top: 12px;
  padding-right: 16px;
  border-radius: 0px;
}
```

### Inputs (2 instances)

```css
.input {
  background-color: rgb(56, 152, 236);
  color: rgb(255, 255, 255);
  border-color: rgb(204, 204, 204);
  border-radius: 0px;
  font-size: 20px;
  padding-top: 0px;
  padding-right: 16px;
}
```

### Links (48 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 15px;
  font-weight: 400;
}
```

### Navigation (12 instances)

```css
.navigatio {
  color: rgb(255, 255, 255);
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
  background-color: rgb(7, 2, 10);
  color: rgb(255, 255, 255);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 20px;
}
```

### Modals (1 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (5 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(255, 255, 255);
  padding-top: 0px;
}
```

### ProgressBars (1 instances)

```css
.progressBar {
  color: rgb(255, 255, 255);
  border-radius: 0px;
  font-size: 20px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 5 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(7, 2, 10);
  padding: 12px 16px 12px 16px;
  border-radius: 0px;
  border: 0px none rgb(7, 2, 10);
  font-size: 15px;
  font-weight: 400;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 12px 16px 12px 16px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 15px;
  font-weight: 400;
```

### Button — 5 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(7, 2, 10);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(7, 2, 10);
  font-size: 15px;
  font-weight: 400;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 15px;
  font-weight: 400;
```

### Other — 20 instances, 2 variants

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(7, 2, 10);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(7, 2, 10);
  font-size: 15px;
  font-weight: 400;
```

**Variant 2** (12 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 15px;
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
  font-size: 20px;
  font-weight: 400;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(239, 239, 239, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 20px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 20px;
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
  font-size: 15px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 16px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(204, 204, 204);
  font-size: 20px;
  font-weight: 400;
```

## Layout System

**19 grid containers** and **58 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1360px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 14-column | 16x |
| 1-column | 1x |
| 2-column | 1x |
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 79.9219px 79.9219px 79.9375px 79.9219px 79.9375px 79.9219px 79.9375px 79.9219px 79.9219px 79.9375px 79.9219px 79.9375px 79.9219px 79.9375px;
grid-template-columns: 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px;
grid-template-columns: 1280px;
grid-template-columns: 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px;
grid-template-columns: 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px 80px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 27x |
| column/nowrap | 30x |
| row/wrap | 1x |

**Gap values:** `12px`, `16px`, `32px`, `48px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 93/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 100/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 176 !important rules — prefer specificity over overrides
- 81% of CSS is unused — consider purging
- 2333 duplicate CSS declarations

## Z-Index Map

**5 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,1000 | div.n.a.v._.c.o.m.p.o.n.e.n.t. .w.-.n.a.v |
| base | -1,2 | div.p.a.g.e._.b.g.-.w.r.a.p.p.e.r, div.f.o.o.t.e.r._.r.i.g.h.t.-.b.g, div.f.o.o.t.e.r._.l.e.f.t.-.b.g |

## SVG Icons

**6 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 4 |
| xl | 2 |

**Icon colors:** `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| RRE Monument Grotesk Trial | self-hosted | 400 | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 20 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (7x), 3:4 (6x), 16:9 (3x), 21:9 (1x), 2.01:1 (1x), 4:3 (1x), 3:2 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

### Easing Families

- **ease-out** (12 uses) — `cubic-bezier(0.25, 1, 0.5, 1)`

## Component Anatomy

### other — 20 instances


### button — 15 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (verbose)

### Top CTA Verbs

- **our** (2)
- **subscribe** (1)
- **limited** (1)
- **general** (1)

### Button Copy Patterns

- "our portfolio" (2×)
- "subscribe" (1×)
- "limited partner login" (1×)
- "general partner login" (1×)

### Sample Headings

> Backing the
best for the
distance
> The confidence
to commit early
> $2.5B+
> 125+
> 400+
> Backing the
best for the
distance
> The confidence
to commit early
> $2.5B+
> 125+
> 400+

## Page Intent

**Type:** `landing` (confidence 0.51)
**Description:** RRE is a boutique venture capital firm with 30 years of experience, backing bold early-stage founders across diverse sectors. We provide deep expertise, AI-driven insights, and committed partnerships 

Alternates: pricing (0.6), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → pricing-table → testimonial → pricing-table → testimonial → testimonial → testimonial → pricing-table → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | pricing-table | Backing the
best for the
distance | 0.9 |
| 2 | testimonial | Backing the
best for the
distance | 0.8 |
| 3 | pricing-table | The confidence
to commit early | 0.9 |
| 4 | testimonial | Investment areas | 0.8 |
| 5 | testimonial | Our difference?
Depth. | 0.8 |
| 6 | testimonial | "RRE was always going to be a core part of our round in the Seed and Series A as | 0.8 |
| 7 | pricing-table | Latest from RRE | 0.9 |
| 8 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.299 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.042)
**Counts:** total 20, svg 7, icon 6, screenshot-like 0, photo-like 0
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.35)

Evidence:
- tailwind-like class density 39%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `RRE Monument Grotesk Trial` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
