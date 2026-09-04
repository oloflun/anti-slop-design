# Design Language: Veloura - Webflow HTML website template

> Extracted from `https://veloura-hotel-template.webflow.io` on September 4, 2026
> 733 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#9e4632` | rgb(158, 70, 50) | hsl(11, 52%, 41%) | 14 |
| Secondary | `#471b10` | rgb(71, 27, 16) | hsl(12, 63%, 17%) | 4 |
| Accent | `#ba5d48` | rgb(186, 93, 72) | hsl(11, 45%, 51%) | 6 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#f3eeed` | hsl(10, 20%, 94%) | 133 |
| `#000000` | hsl(0, 0%, 0%) | 59 |
| `#ffffff` | hsl(0, 0%, 100%) | 4 |

### Background Colors

Used on large-area elements: `#2a0800`, `#703324`, `#000000`, `#eee3e0`, `#e9dad6`

### Text Colors

Text color palette: `#000000`, `#2a0800`, `#eee3e0`, `#f3eeed`, `#f5ccc2`, `#e9dad6`, `#ba6957`, `#e2c6bf`, `#e8bbb0`, `#ffffff`

### Gradients

```css
background-image: linear-gradient(rgba(48, 20, 13, 0), rgb(42, 8, 0) 20%);
```

```css
background-image: linear-gradient(0deg, rgb(238, 227, 224), rgb(245, 204, 194));
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0), rgb(42, 8, 0) 90%);
```

```css
background-image: radial-gradient(circle farthest-side, rgb(238, 227, 224) 50%, rgba(255, 255, 255, 0)), linear-gradient(rgba(243, 239, 237, 0) 15%, rgb(238, 227, 224) 28%);
```

```css
background-image: radial-gradient(circle farthest-side at 50% 100%, rgb(233, 218, 214), rgba(255, 255, 255, 0)), linear-gradient(rgba(243, 239, 237, 0) 62%, rgb(233, 218, 214));
```

```css
background-image: linear-gradient(rgb(42, 8, 0), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0), rgb(42, 8, 0) 80%);
```

```css
background-image: linear-gradient(rgb(226, 198, 191), rgb(238, 227, 224));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#2a0800` | text, background, border | 630 |
| `#ba6957` | background, text, border | 319 |
| `#eee3e0` | text, border, background | 209 |
| `#f3eeed` | text, border, background | 133 |
| `#f5ccc2` | text, border | 108 |
| `#e8bbb0` | text, border | 84 |
| `#000000` | text, border, background | 59 |
| `#9e4632` | background | 14 |
| `#e2c6bf` | text, border, background | 13 |
| `#703324` | background, text, border | 9 |
| `#ba5d48` | background | 6 |
| `#471b10` | background | 4 |
| `#ffffff` | text, background | 4 |

## Typography

### Font Families

- **Funnel Sans** — used for body (598 elements)
- **Ltremark** — used for all (54 elements)
- **Funnel Display** — used for all (52 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 217.6px | 13.6rem | 700 | 261.12px | -6.4px | div |
| 128px | 8rem | 400 | 128px | normal | div |
| 115.2px | 7.2rem | 500 | 115.2px | normal | h3, div |
| 96px | 6rem | 300 | 96px | normal | h3, div |
| 76.8px | 4.8rem | 500 | 84.48px | normal | h2, div |
| 64px | 4rem | 500 | 76.8px | normal | h2, div |
| 56px | 3.5rem | 500 | 67.2px | normal | h2 |
| 54.4px | 3.4rem | 500 | 65.28px | normal | h3 |
| 51.2px | 3.2rem | 500 | 56.32px | normal | h1 |
| 48px | 3rem | 500 | 57.6px | normal | h2 |
| 36.8px | 2.3rem | 500 | 44.16px | normal | h2, h3 |
| 30.4px | 1.9rem | 300 | 28.8px | normal | div |
| 22.4px | 1.4rem | 600 | 33.6px | normal | p |
| 20.8px | 1.3rem | 400 | 24.96px | normal | div |
| 19.2px | 1.2rem | 400 | 28.8px | normal | a, img, div, p |

### Heading Scale

```css
h3 { font-size: 115.2px; font-weight: 500; line-height: 115.2px; }
h3 { font-size: 96px; font-weight: 300; line-height: 96px; }
h2 { font-size: 76.8px; font-weight: 500; line-height: 84.48px; }
h2 { font-size: 64px; font-weight: 500; line-height: 76.8px; }
h2 { font-size: 56px; font-weight: 500; line-height: 67.2px; }
h3 { font-size: 54.4px; font-weight: 500; line-height: 65.28px; }
h1 { font-size: 51.2px; font-weight: 500; line-height: 56.32px; }
h2 { font-size: 48px; font-weight: 500; line-height: 57.6px; }
h2 { font-size: 36.8px; font-weight: 500; line-height: 44.16px; }
```

### Body Text

```css
body { font-size: 14.4px; font-weight: 400; line-height: 18.72px; }
```

### Font Weights in Use

`400` (544x), `300` (73x), `600` (61x), `500` (50x), `700` (5x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-32 | 32px | 2rem |
| spacing-38 | 38px | 2.375rem |
| spacing-48 | 48px | 3rem |
| spacing-77 | 77px | 4.8125rem |
| spacing-90 | 90px | 5.625rem |
| spacing-102 | 102px | 6.375rem |
| spacing-112 | 112px | 7rem |
| spacing-128 | 128px | 8rem |
| spacing-136 | 136px | 8.5rem |
| spacing-160 | 160px | 10rem |
| spacing-240 | 240px | 15rem |
| spacing-320 | 320px | 20rem |
| spacing-448 | 448px | 28rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 10px | 2 |
| lg | 14px | 12 |
| xl | 20px | 18 |
| full | 50px | 75 |
| full | 99px | 3 |
| full | 800px | 9 |
| full | 999px | 1 |

## CSS Custom Properties

### Colors

```css
--body-bg-dark: var(--_colors---brand-dark-6);
--_colors---brand-main-color: #ba6957;
--_colors---brand-dark-2: #9e4632;
--body-bg: var(--_colors---brand-light-2);
--_colors---brand-light-3: #e9dad6;
--_colors---brand-dark-3: #703324;
--_colors---brand-dark-4: #5a2619;
--_colors---brand-light-5: #f5ccc2;
--_colors---brand-dark-5: #471b10;
--_colors---brand-light-1: #f3eeed;
--_colors---brand-color-light-20: #f3efed33;
--_colors---brand-light-4: #e2c6bf;
--_colors---brand-light-6: #e4b3a7;
--_colors---brand-color-10: #ba69571a;
--_colors---brand-color-20: #ba695733;
--_colors---brand-dark-1: #ba5d48;
--_colors---brand-dark-6: #2a0800;
--_colors---brand-light-2: #eee3e0;
--_colors---dark-brown<deleted|variable-52d39058-521c-1b10-4036-27e59bfa685f>: #30140d;
--_colors---white: #fff;
--_colors---brand-color-40: #ba695766;
--_colors---border-color: #2a08001a;
--_colors---brand-color-light-70: #f3efedb3;
--_colors---transparent: #fff0;
--_colors---brand-color-80: #2a0800cc;
--_colors---brand-color-light-40: #f3efed66;
--_colors---brand-dark-7: #180500;
--_colors---brand-color-light-10: #f3efed1a;
```

### Spacing

```css
--body-size: 1rem;
--_base-text-style---h1--margins: 2rem;
--_base-text-style---h1--font-size: 4.5rem;
--_base-text-style---h1--letter-spacing: 0rem;
--_base-text-style---h2--margins: 2rem;
--_base-text-style---h2--font-size: 3rem;
--_base-text-style---h2--letter-spacing: 0rem;
--_base-text-style---h3--margins: 2rem;
--_base-text-style---h3--font-size: 2.5rem;
--_base-text-style---h3--letter-spacing: 0rem;
--_base-text-style---h4--margins: 2rem;
--_base-text-style---h4--font-size: 2rem;
--_base-text-style---h4--letter-spacing: 0rem;
--_base-text-style---h5--margins: 2rem;
--_base-text-style---h5--font-size: 1.8rem;
--_base-text-style---h5--letter-spacing: 0rem;
--_base-text-style---h6--margins: 2rem;
--_base-text-style---h6--font-size: 1.5rem;
--_base-text-style---paragraph--letter-spacing: 0rem;
--_base-text-style---paragraph--margins: 1.25rem;
--_base-text-style---paragraph--font-size: 1.2rem;
--_base-text-style---uppercase-text--font-size: .9rem;
--icon-size--regular: 3rem;
--_spacing---container-width: 94%;
--_spacing---container-narrow-max-width: 80rem;
--_spacing---container-max-width: 120rem;
--_spacing---padding-small: 5rem;
--_base-text-style---paragraph--font-size-medium: 1.4rem;
--_base-text-style---paragraph--font-size-large: 1.6rem;
--_base-text-style---paragraph--font-size-small: 1rem;
--_spacing---padding: 8rem;
--_spacing---max-widths--medium: 65rem;
--_spacing---max-widths--small: 55rem;
--_spacing---max-widths--large: 72rem;
--_base-text-style---paragraph--font-size-xlarge: 1.8rem;
--_spacing---padding-large: 12rem;
--_spacing---fluid-gap: 8vw;
--_spacing---fluid-gap-small: 5vw;
--icon-size--small: 2rem;
--icon-size--large: 6.5rem;
--_base-text-style---h6--letter-spacing: 0rem;
```

### Typography

```css
--_typography---sans-font: "Funnel Sans",sans-serif;
--body-font: var(--_colors---brand-dark-6);
--_base-text-style---h1--font-family: var(--_typography---sans-font);
--_base-text-style---h1--line-height: 95%;
--_base-text-style---h1--font-weight: var(--font-weight--medium);
--_base-text-style---h2--font-family: var(--_typography---sans-font);
--_base-text-style---h2--line-height: 95%;
--_base-text-style---h2--font-weight: var(--font-weight--medium);
--_base-text-style---h3--font-family: var(--_typography---sans-font);
--_base-text-style---h3--line-height: 100%;
--_base-text-style---h3--font-weight: var(--font-weight--medium);
--_base-text-style---h4--font-family: var(--_typography---sans-font);
--_base-text-style---h4--line-height: 100%;
--_base-text-style---h4--font-weight: var(--font-weight--medium);
--_base-text-style---h5--font-family: var(--_typography---sans-font);
--_base-text-style---h5--line-height: 100%;
--_base-text-style---h5--font-weight: var(--font-weight--medium);
--_base-text-style---h6--font-family: var(--_typography---sans-font);
--_base-text-style---h6--line-height: 100%;
--_base-text-style---h6--font-weight: var(--font-weight--medium);
--_base-text-style---paragraph--font-family: var(--_typography---sans-font);
--_base-text-style---paragraph--line-height: 150%;
--_base-text-style---paragraph--font-weight: var(--font-weight--normal);
--body-font-light: var(--_colors---brand-light-2);
--_typography---display-font: "Funnel Display",sans-serif;
--font-weight--medium: 500;
--_typography---brand-font: Ltremark,"Times New Roman",sans-serif;
--font-weight--semi-bold: 600;
--font-weight--light: 300;
--font-weight--normal: 400;
--_base-text-style---uppercase-text--font-weight: var(--font-weight--light);
--font-weight--bold: 700;
--font-weight--thin: 100;
--font-weight--extra-light: 200;
--font-weight--extra-bold: 800;
--font-weight--black: 900;
--_base-text-style---uppercase-text--font-family: var(--_typography---sans-font);
```

### Radii

```css
--radius--radius-normal: 20px;
--radius--radius-small: 10px;
```

### Dependencies

```css
--body-bg-dark: --_colors---brand-dark-6;
--body-font: --_colors---brand-dark-6;
--_base-text-style---h1--font-family: --_typography---sans-font;
--_base-text-style---h1--font-weight: --font-weight--medium;
--_base-text-style---h2--font-family: --_typography---sans-font;
--_base-text-style---h2--font-weight: --font-weight--medium;
--_base-text-style---h3--font-family: --_typography---sans-font;
--_base-text-style---h3--font-weight: --font-weight--medium;
--_base-text-style---h4--font-family: --_typography---sans-font;
--_base-text-style---h4--font-weight: --font-weight--medium;
--_base-text-style---h5--font-family: --_typography---sans-font;
--_base-text-style---h5--font-weight: --font-weight--medium;
--_base-text-style---h6--font-family: --_typography---sans-font;
--_base-text-style---h6--font-weight: --font-weight--medium;
--_base-text-style---paragraph--font-family: --_typography---sans-font;
--_base-text-style---paragraph--font-weight: --font-weight--normal;
--body-font-light: --_colors---brand-light-2;
--body-bg: --_colors---brand-light-2;
--_base-text-style---uppercase-text--font-weight: --font-weight--light;
--_base-text-style---uppercase-text--font-family: --_typography---sans-font;
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
| lg | 991px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.001s`, `0.2s`, `1s`, `1.2s`, `0.1s`, `0.6s`

### Common Transitions

```css
transition: overflow 0.001s allow-discrete;
transition: all;
transition: color 0.2s, border-color 1s, opacity 0.2s;
transition: transform 1.2s cubic-bezier(0.075, 0.82, 0.165, 1), background-color 0.2s;
transition: color 0.2s, background-color 0.2s;
transition: background-color 0.2s;
transition: background-position 0.2s, background-color 0.2s;
transition: background-color 0.1s, color 0.1s;
transition: opacity 0.2s;
transition: padding 0.6s cubic-bezier(0.075, 0.82, 0.165, 1), opacity 0.2s;
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
  background-color: rgb(158, 70, 50);
  color: rgb(243, 238, 237);
  font-size: 19.2px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 50%;
}
```

### Cards (64 instances)

```css
.card {
  background-color: rgb(186, 93, 72);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (61 instances)

```css
.link {
  color: rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
}
```

### Navigation (11 instances)

```css
.navigatio {
  background-color: rgba(0, 0, 0, 0.1);
  color: rgb(42, 8, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (61 instances)

```css
.foote {
  background-color: rgb(42, 8, 0);
  color: rgb(42, 8, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (6 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (49 instances)

```css
.dropdown {
  background-color: rgb(186, 105, 87);
  border-radius: 0px;
  border-color: rgb(42, 8, 0);
  padding-top: 0px;
}
```

### Badges (4 instances)

```css
.badge {
  background-color: rgb(226, 198, 191);
  color: rgb(42, 8, 0);
  font-size: 19.2px;
  font-weight: 400;
  padding-top: 3.2px;
  padding-right: 9.6px;
  border-radius: 10px;
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

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(158, 70, 50);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

### Button — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

### Button — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgb(158, 70, 50);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(158, 70, 50);
  color: rgb(243, 238, 237);
  padding: 0px 59.2px 0px 16px;
  border-radius: 800px;
  border: 1px solid rgba(243, 239, 237, 0.2);
  font-size: 19.2px;
  font-weight: 400;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(243, 238, 237);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(243, 238, 237);
  font-size: 19.2px;
  font-weight: 500;
```

### Card — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(42, 8, 0);
  padding: 16px 12.8px 32px 12.8px;
  border-radius: 0px;
  border: 0px none rgb(42, 8, 0);
  font-size: 16px;
  font-weight: 400;
```

### Link — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(226, 198, 191);
  color: rgb(42, 8, 0);
  padding: 3.2px 9.6px 3.2px 9.6px;
  border-radius: 10px;
  border: 1px solid rgb(228, 179, 167);
  font-size: 19.2px;
  font-weight: 400;
```

### Card — 8 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(42, 8, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(42, 8, 0);
  font-size: 12.8px;
  font-weight: 500;
```

**Variant 2** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

### Card — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 14.4px;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

### Card — 18 instances, 1 variant

**Variant 1** (18 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

### Card — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(238, 227, 224);
  padding: 80px 16px 0px 16px;
  border-radius: 14.4px;
  border: 0px none rgb(238, 227, 224);
  font-size: 19.2px;
  font-weight: 400;
```

### Card — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(238, 227, 224);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(238, 227, 224);
  font-size: 19.2px;
  font-weight: 400;
```

### Button — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgb(186, 93, 72);
  color: rgb(238, 227, 224);
  padding: 0px 0px 0px 0px;
  border-radius: 50%;
  border: 0px none rgb(238, 227, 224);
  font-size: 19.2px;
  font-weight: 400;
```

### Link — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(186, 105, 87);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(186, 105, 87);
  font-size: 19.2px;
  font-weight: 400;
```

## Layout System

**2 grid containers** and **189 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1280px | 0px |
| 960px | 0px |
| 2000px | 0px |
| 448px | 12.8px |
| 100% | 0px |
| 1920px | 0px |
| 384px | 0px |
| 512px | 0px |
| 640px | 0px |
| 768px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 1x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 377.594px 377.594px 377.609px;
gap: 16px;
grid-template-columns: 616px 616px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 132x |
| column/nowrap | 56x |
| row-reverse/nowrap | 1x |

**Gap values:** `1.6px`, `102.4px`, `11.2px`, `160px`, `16px`, `19.2px`, `240px`, `3.2px`, `32px`, `3px`, `48px`, `4px`, `51.2px`, `6.4px`, `64px`, `76.8px`, `89.6px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#2a0800` | `#e2c6bf` | 11.53:1 | AAA |

## Design System Score

**Overall: 88/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 41 !important rules — prefer specificity over overrides
- 79% of CSS is unused — consider purging
- 5614 duplicate CSS declarations

## Gradients

**10 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | 0deg | 2 | brand |
| linear | — | 2 | brand |
| radial | circle farthest-side | 2 | brand |
| linear | — | 2 | brand |
| radial | circle farthest-side at 50% 100% | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |

```css
background: linear-gradient(rgba(48, 20, 13, 0), rgb(42, 8, 0) 20%);
background: linear-gradient(0deg, rgb(238, 227, 224), rgb(245, 204, 194));
background: linear-gradient(rgba(255, 255, 255, 0), rgb(42, 8, 0) 90%);
background: radial-gradient(circle farthest-side, rgb(238, 227, 224) 50%, rgba(255, 255, 255, 0));
background: linear-gradient(rgba(243, 239, 237, 0) 15%, rgb(238, 227, 224) 28%);
```

## Z-Index Map

**22 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,999 | div.m.e.n.u.-.c.l.o.s.e, header.n.a.v.-.h.e.a.d.e.r. .w.-.v.a.r.i.a.n.t.-.a.8.3.e.2.3.6.b.-.7.b.f.7.-.f.8.9.d.-.4.a.b.9.-.e.3.8.d.1.c.7.f.f.c.1.4, div.m.e.n.u.-.b.u.r.g.e.r |
| sticky | 10,99 | div.p.r.e.l.o.a.d.e.r.-.t.e.x.t, div.p.r.e.l.o.a.d.e.r.-.i.m.a.g.e.-.c.o.l.o.r, a.n.a.v.-.l.i.n.k |
| base | -1,9 | img.r.o.o.m.-.b.l.u.r.r.y.-.b.g, img.r.o.o.m.-.b.l.u.r.r.y.-.b.g, img.r.o.o.m.-.b.l.u.r.r.y.-.b.g |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| Ltremark | self-hosted | 400 | normal |
| Funnel Display | google-fonts | 300, 400, 500, 600, 700 | normal |
| Funnel Sans | cdn | 300, 400, 500, 600, 700 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 34 | objectFit: contain, borderRadius: 0px, shape: square |
| general | 29 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 9 | objectFit: contain, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (46x), 3:4 (14x), 4:3 (5x), 9:16 (3x), 3:2 (2x), 2:3 (1x), 2.57:1 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `lg` | `600ms` | 600 |
| `xl` | `1s` | 1000 |

### Easing Families

- **ease-out** (8 uses) — `cubic-bezier(0.075, 0.82, 0.165, 1)`

## Component Anatomy

### card — 52 instances

**Slots:** media

### button — 33 instances

**Slots:** label, icon

### link — 6 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **booking** (2)
- **featured** (2)
- **location** (2)
- **reservations** (2)
- **deeper** (1)
- **refresh** (1)
- **smooth** (1)
- **unwind** (1)

### Button Copy Patterns

- "booking" (2×)
- "location" (2×)
- "reservations" (2×)
- "featured
calm your senses

aromatherapy massage

warm essential oils ease tension and bring deep relaxation." (1×)
- "featured
detox and renew

herbal steam ritual

herbal steam cleanses the skin and clears the mind." (1×)
- "deeper calm

hot stone therapy

heated stones melt stress and restore harmony." (1×)
- "refresh and glow

rejuvenating facial

gentle care that restores brightness and hydration." (1×)
- "smooth, soft, renewed

body renewal scrub

sea salt and oils refresh and soften the skin." (1×)
- "unwind completely

deep relax massage

slow, flowing movements calm body and mind." (1×)

### Sample Headings

> A BOUTIQUE ESCAPE IN TIMELESS STREETS
> Cozy interiors, warm tones, and thoughtful details that make every stay feel personal.
> Corner Suite
> Velvet Room
> Amber Suite
> A BOUTIQUE ESCAPE IN TIMELESS STREETS
> Cozy interiors, warm tones, and thoughtful details that make every stay feel personal.
> Corner Suite
> Velvet Room
> Amber Suite

## Page Intent

**Type:** `pricing` (confidence 0.42)
**Description:** Veloura is a fictional boutique hotel created for a modern Webflow template, showcasing elegant design, warm atmosphere, and cozy guest experiences.

Alternates: landing (0.45), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → pricing-table → content → pricing-table → feature-grid → content → content → hero

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | pricing-table | A BOUTIQUE ESCAPE IN TIMELESS STREETS | 0.9 |
| 3 | content | A BOUTIQUE ESCAPE IN TIMELESS STREETS | 0.3 |
| 4 | pricing-table | Cozy interiors, warm tones, and thoughtful details that make every stay feel per | 0.9 |
| 5 | feature-grid | Relax that comes with | 0.8 |
| 6 | content | Tucked away in the quiet streets of the old town - historic charm with comfort a | 0.3 |
| 7 | content | Treatments | 0.3 |
| 8 | hero | BOOK NOW | 0.4 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.382 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 999px |
| backdrop-filter in use | no |
| Gradients | 10 |

## Imagery Style

**Label:** `gradient-mesh` (confidence 0.208)
**Counts:** total 72, svg 43, icon 52, screenshot-like 0, photo-like 23
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Funnel Sans` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
