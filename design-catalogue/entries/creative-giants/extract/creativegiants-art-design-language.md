# Design Language: Creative Giants | Immersive Activations & Public Art Interventions UK

> Extracted from `https://creativegiants.art` on September 4, 2026
> 885 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fffef7` | rgb(255, 254, 247) | hsl(53, 100%, 98%) | 672 |
| Secondary | `#009fff` | rgb(0, 159, 255) | hsl(203, 100%, 50%) | 9 |
| Accent | `#ffd001` | rgb(255, 208, 1) | hsl(49, 100%, 50%) | 3 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 880 |
| `#efeeec` | hsl(40, 9%, 93%) | 100 |
| `#666666` | hsl(0, 0%, 40%) | 62 |
| `#aaaaaa` | hsl(0, 0%, 67%) | 12 |
| `#1f1f1f` | hsl(0, 0%, 12%) | 6 |
| `#131313` | hsl(0, 0%, 7%) | 2 |
| `#444444` | hsl(0, 0%, 27%) | 1 |
| `#cccccc` | hsl(0, 0%, 80%) | 1 |
| `#dddddd` | hsl(0, 0%, 87%) | 1 |
| `#ecfdf3` | hsl(145, 81%, 96%) | 1 |

### Background Colors

Used on large-area elements: `#fffef7`, `#ffffff`, `#000000`, `#ffacea`, `#a5ebd6`, `#101731`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#fffef7`, `#efeeec`, `#009fff`, `#666666`, `#8a0467`, `#03624c`, `#a5c8eb`, `#027a48`

### Gradients

```css
background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.2) 20%, rgba(255, 255, 255, 0.2) 80%, rgba(255, 255, 255, 0));
```

```css
background-image: linear-gradient(rgb(77, 76, 74), rgb(0, 0, 0));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 880 |
| `#fffef7` | background, text, border | 672 |
| `#efeeec` | text, border | 100 |
| `#666666` | background, text, border | 62 |
| `#8a0467` | text, border | 22 |
| `#03624c` | text, border | 22 |
| `#a5c8eb` | text, border | 22 |
| `#aaaaaa` | text, border | 12 |
| `#009fff` | text, border, background | 9 |
| `#1f1f1f` | background | 6 |
| `#027a48` | text, border | 4 |
| `#b42318` | text, border | 4 |
| `#ffd001` | background | 3 |
| `#131313` | background | 2 |
| `#444444` | background | 1 |
| `#cccccc` | background | 1 |
| `#ffacea` | background | 1 |
| `#a5ebd6` | background | 1 |
| `#101731` | background | 1 |
| `#dddddd` | background | 1 |
| `#ecfdf3` | background | 1 |
| `#ffdede` | background | 1 |
| `#48d1d6` | background | 1 |
| `#fc4c00` | background | 1 |
| `#ee77cf` | background | 1 |

## Typography

### Font Families

- **Switzer** — used for all (840 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 80.2584px | 5.0161rem | 300 | 60.1938px | -3.21033px | p, h2, span |
| 61.1492px | 3.8218rem | 300 | 61.1492px | -2.44597px | h2, span |
| 51.5947px | 3.2247rem | 300 | 51.5947px | -2.06379px | h1, div |
| 32.4855px | 2.0303rem | 300 | 32.4855px | -1.29942px | h2 |
| 19.1091px | 1.1943rem | 300 | 26.7528px | -0.764365px | h3 |
| 17.1982px | 1.0749rem | 300 | 17.1982px | normal | p, span, div, a |
| 15.2873px | 0.9555rem | 400 | normal | normal | html, head, style, meta |
| 13.3764px | 0.836rem | 300 | 18.7269px | -0.305746px | div, label, a |
| 11.4655px | 0.7166rem | 300 | 16.0517px | -0.305746px | div, p |

### Heading Scale

```css
h2 { font-size: 80.2584px; font-weight: 300; line-height: 60.1938px; }
h2 { font-size: 61.1492px; font-weight: 300; line-height: 61.1492px; }
h1 { font-size: 51.5947px; font-weight: 300; line-height: 51.5947px; }
h2 { font-size: 32.4855px; font-weight: 300; line-height: 32.4855px; }
h3 { font-size: 19.1091px; font-weight: 300; line-height: 26.7528px; }
```

### Body Text

```css
body { font-size: 15.2873px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`300` (638x), `400` (237x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-31 | 31px | 1.9375rem |
| spacing-38 | 38px | 2.375rem |
| spacing-46 | 46px | 2.875rem |
| spacing-61 | 61px | 3.8125rem |
| spacing-76 | 76px | 4.75rem |
| spacing-107 | 107px | 6.6875rem |
| spacing-117 | 117px | 7.3125rem |
| spacing-153 | 153px | 9.5625rem |
| spacing-173 | 173px | 10.8125rem |
| spacing-190 | 190px | 11.875rem |
| spacing-232 | 232px | 14.5rem |
| spacing-255 | 255px | 15.9375rem |
| spacing-313 | 313px | 19.5625rem |
| spacing-387 | 387px | 24.1875rem |
| spacing-400 | 400px | 25rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xl | 23px | 1 |
| full | 50px | 2 |
| full | 1280px | 21 |
| full | 1529px | 1 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.2) 0px 0px 0px 1px;
```

## CSS Custom Properties

### Colors

```css
--_theme---background-color--background-primary: var(--neutral--white);
--_typography---font--primary-font: Switzer, Arial, sans-serif;
--_theme---text-color--text-primary: var(--neutral--black);
--_theme---link-color--link-primary: var(--neutral--black);
--_theme---text-color--text-secondary: var(--neutral--neutral);
--_theme---text-color--text-alternate<deleted|relume-variable-text-color-3>: var(--neutral--white);
--_theme---border-color--border-primary: var(--neutral--black);
--_theme---button-primary--button-border: var(--neutral--black);
--_theme---button-primary--button-bg: var(--neutral--black);
--_theme---button-primary--button-text: var(--neutral--white);
--_theme---button-tertiary--button-border: var(--neutral--neutral-lightest);
--_theme---button-tertiary--button-bg: var(--neutral--neutral-lightest);
--_theme---border-color--border-tertiary: var(--neutral--neutral-light);
--_theme---background-color--background-secondary<deleted|relume-variable-background-color-2>: var(--neutral--neutral-lightest);
--_theme---background-color--background-alternate<deleted|relume-variable-background-color-4>: var(--neutral--black);
--_theme---link-color--link-alternate<deleted|relume-variable-link-color-3>: var(--neutral--white);
--_theme---background-color--background-tertiary<deleted|relume-variable-background-color-3>: var(--neutral--neutral-light);
--_theme---text-color--text-secondary<deleted|relume-variable-text-color-2>: var(--neutral--black);
--_theme---background-color--background-success: var(--system--success-green-light);
--_theme---text-color--text-success: var(--system--success-green);
--_theme---background-color--background-error: var(--system--error-red-light);
--_theme---text-color--text-error: var(--system--error-red);
--_projects---secondary: var(--brand--white);
--_theme---border-color--border-divider: var(--neutral--neutral-lighter);
--_brand---color: var(--brand--yellow);
--_theme---button-primary--button-icon-bg: var(--neutral--white);
--_theme---button-primary--button-icon: var(--neutral--black);
--_projects---primary: var(--brand--black);
--_theme---button-secondary--button-border: var(--neutral--black);
--_theme---button-secondary--button-text: var(--brand--black);
--_theme---button-secondary--button-bg: var(--neutral--transparent);
--_theme---button-secondary--button-icon: var(--brand--white);
--_theme---button-secondary--button-icon-bg: var(--neutral--black);
--_theme---border-color--border-secondary: var(--neutral--neutral-darker);
--_theme---button-tertiary--button-icon-bg: var(--neutral--transparent);
--_theme---button-link--button-bg: var(--neutral--transparent);
--_theme---button-link--button-border: var(--neutral--transparent);
--_theme---button-link--button-icon-bg: var(--neutral--transparent);
--swiper-theme-color: #007aff;
```

### Spacing

```css
--_typography---font-size--main: 1rem;
--_typography---letter-spacing--0-02em: -.02em;
--_typography---font-size--h1: 5.25rem;
--_typography---letter-spacing--0-04em: -.04em;
--_typography---font-size--h2: 4.625rem;
--_typography---font-size--h3: 4rem;
--_typography---font-size--h4: 3.375rem;
--_typography---font-size--h5: 2.75rem;
--_typography---font-size--h6: 2.125rem;
--_typography---font-size--small: .875rem;
--_typography---font-size--large: 1.125rem;
--swiper-navigation-size: 44px;
```

### Typography

```css
--_typography---line-height--body: 1.4;
--_typography---line-height--heading: 1;
--_typography---font-weight--light: 300;
--_theme---button-link--button-text: var(--neutral--black);
--_theme---button-tertiary--button-text: var(--neutral--black);
--_typography---font-weight--regular: 400;
--_typography---font-weight--medium: 500;
```

### Other

```css
--neutral--white: var(--brand--white);
--neutral--black: var(--brand--black);
--brand--white: #fffef7;
--brand--yellow: #ffd001;
--brand--black: black;
--black-archive<deleted|variable-dccb7db6>: black;
--neutral--transparent: #fff0;
--brand--pink: #ee77cf;
--neutral--neutral-dark: #444;
--neutral--neutral-lighter: #ccc;
--brand--blue: #009fff;
--neutral--neutral-lightest: #eee;
--brand--yellow-light: #fffa86;
--brand--yellow-dark: #d19800;
--brand--teal-light: #b0f0f1;
--brand--teal: #48d1d6;
--brand--teal-dark: #1e8f9c;
--brand--blue-light: #b6e2ff;
--brand--blue-dark: #007ad4;
--brand--pink-light: #f9d1f1;
--brand--pink-dark: #d32f9b;
--brand--orange-light: #ffd3a5;
--brand--orange: #fc4c00;
--brand--orange-dark: #cc3502;
--neutral--neutral-light: #aaa;
--neutral--neutral: #666;
--neutral--neutral-darker: #222;
--neutral--neutral-darkest: #111;
--system--success-green: #027a48;
--system--success-green-light: #ecfdf3;
--system--error-red: #b42318;
--system--error-red-light: #fef3f2;
--_theme---button-tertiary--button-icon: var(--neutral--black);
--_theme---button-link--button-icon: var(--brand--black);
```

### Dependencies

```css
--_theme---background-color--background-primary: --neutral--white;
--_theme---text-color--text-primary: --neutral--black;
--_theme---link-color--link-primary: --neutral--black;
--_theme---text-color--text-secondary: --neutral--neutral;
--_theme---text-color--text-alternate<deleted|relume-variable-text-color-3>: --neutral--white;
--_theme---border-color--border-primary: --neutral--black;
--neutral--white: --brand--white;
--_theme---button-primary--button-border: --neutral--black;
--_theme---button-primary--button-bg: --neutral--black;
--_theme---button-primary--button-text: --neutral--white;
--neutral--black: --brand--black;
--_theme---button-link--button-text: --neutral--black;
--_theme---button-tertiary--button-border: --neutral--neutral-lightest;
--_theme---button-tertiary--button-bg: --neutral--neutral-lightest;
--_theme---button-tertiary--button-text: --neutral--black;
--_theme---border-color--border-tertiary: --neutral--neutral-light;
--_theme---background-color--background-secondary<deleted|relume-variable-background-color-2>: --neutral--neutral-lightest;
--_theme---background-color--background-alternate<deleted|relume-variable-background-color-4>: --neutral--black;
--_theme---link-color--link-alternate<deleted|relume-variable-link-color-3>: --neutral--white;
--_theme---background-color--background-tertiary<deleted|relume-variable-background-color-3>: --neutral--neutral-light;
--_theme---text-color--text-secondary<deleted|relume-variable-text-color-2>: --neutral--black;
--_theme---background-color--background-success: --system--success-green-light;
--_theme---text-color--text-success: --system--success-green;
--_theme---background-color--background-error: --system--error-red-light;
--_theme---text-color--text-error: --system--error-red;
--_projects---secondary: --brand--white;
--_theme---border-color--border-divider: --neutral--neutral-lighter;
--_brand---color: --brand--yellow;
--_theme---button-primary--button-icon-bg: --neutral--white;
--_theme---button-primary--button-icon: --neutral--black;
--_projects---primary: --brand--black;
--_theme---button-secondary--button-border: --neutral--black;
--_theme---button-secondary--button-text: --brand--black;
--_theme---button-secondary--button-bg: --neutral--transparent;
--_theme---button-secondary--button-icon: --brand--white;
--_theme---button-secondary--button-icon-bg: --neutral--black;
--_theme---border-color--border-secondary: --neutral--neutral-darker;
--_theme---button-tertiary--button-icon-bg: --neutral--transparent;
--_theme---button-tertiary--button-icon: --neutral--black;
--_theme---button-link--button-bg: --neutral--transparent;
--_theme---button-link--button-border: --neutral--transparent;
--_theme---button-link--button-icon-bg: --neutral--transparent;
--_theme---button-link--button-icon: --brand--black;
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
| 1440px | 1440px | max-width |
| 1920px | 1920px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.55s`, `0.375s`, `0.2s`, `0.7s`, `0.6s`

### Common Transitions

```css
transition: all;
transition: opacity 0.3s ease-in-out;
transition: transform 0.55s cubic-bezier(0.65, 0.05, 0, 1);
transition: opacity 0.3s linear;
transition: background-color 0.375s cubic-bezier(0.625, 0.05, 0, 1), height 0.375s cubic-bezier(0.625, 0.05, 0, 1), width 0.375s cubic-bezier(0.625, 0.05, 0, 1);
transition: opacity 0.2s;
transition: opacity 0.3s;
transition: transform;
transition: color 0.3s;
transition: height 0.7s cubic-bezier(0.625, 0.05, 0, 1);
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**marquee_timeline**
```css
@keyframes marquee_timeline {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (16 instances)

```css
.button {
  background-color: rgb(0, 0, 0);
  color: rgb(255, 254, 247);
  font-size: 15.2873px;
  font-weight: 300;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (4 instances)

```css
.card {
  background-color: rgb(0, 0, 0);
  border-radius: 0px;
  box-shadow: rgba(255, 255, 255, 0.2) 0px 0px 0px 1px;
  padding-top: 45.8619px;
  padding-right: 45.8619px;
}
```

### Inputs (6 instances)

```css
.input {
  background-color: rgb(255, 254, 247);
  color: rgb(0, 0, 0);
  border-color: rgb(0, 0, 0) rgb(0, 0, 0) rgb(170, 170, 170);
  border-radius: 0px;
  font-size: 15.2873px;
  padding-top: 7.64365px;
  padding-right: 11.4655px;
}
```

### Links (34 instances)

```css
.link {
  color: rgb(255, 254, 247);
  font-size: 15.2873px;
  font-weight: 300;
}
```

### Navigation (19 instances)

```css
.navigatio {
  background-color: rgb(0, 0, 0);
  color: rgb(255, 254, 247);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
  box-shadow: rgba(255, 255, 255, 0.2) 0px 0px 0px 1px;
}
```

### Footer (48 instances)

```css
.foote {
  background-color: rgb(0, 0, 0);
  color: rgb(255, 254, 247);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 15.2873px;
}
```

### Modals (2 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (29 instances)

```css
.dropdown {
  background-color: rgb(0, 0, 0);
  border-radius: 0px;
  box-shadow: rgba(255, 255, 255, 0.2) 0px 0px 0px 1px;
  border-color: rgb(255, 254, 247);
  padding-top: 0px;
}
```

### Badges (12 instances)

```css
.badge {
  color: rgb(255, 254, 247);
  font-size: 15.2873px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### ProgressBars (7 instances)

```css
.progressBar {
  background-color: rgb(68, 68, 68);
  color: rgb(255, 254, 247);
  border-radius: 0px;
  font-size: 15.2873px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 6 instances, 2 variants

**Variant 1** (5 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 254, 247);
  padding: 13.4528px 19.1091px 13.4528px 19.1091px;
  border-radius: 1280px;
  border: 0px none rgb(255, 254, 247);
  font-size: 15.2873px;
  font-weight: 300;
```

**Variant 2** (1 instance)

```css
  background: rgba(239, 239, 239, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 15.2873px;
  font-weight: 300;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 254, 247);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 254, 247);
  font-size: 15.2873px;
  font-weight: 300;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 254, 247);
  padding: 5.80918px 5.80918px 5.80918px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 254, 247);
  font-size: 15.2873px;
  font-weight: 300;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 15.2873px;
  font-weight: 300;
```

### Card — 3 instances, 3 variants

**Variant 1** (1 instance)

```css
  background: rgb(255, 172, 234);
  color: rgb(138, 4, 103);
  padding: 45.8619px 45.8619px 45.8619px 45.8619px;
  border-radius: 0px;
  border: 0px none rgb(138, 4, 103);
  font-size: 15.2873px;
  font-weight: 300;
```

**Variant 2** (1 instance)

```css
  background: rgb(165, 235, 214);
  color: rgb(3, 98, 76);
  padding: 45.8619px 45.8619px 45.8619px 45.8619px;
  border-radius: 0px;
  border: 0px none rgb(3, 98, 76);
  font-size: 15.2873px;
  font-weight: 300;
```

**Variant 3** (1 instance)

```css
  background: rgb(16, 23, 49);
  color: rgb(165, 200, 235);
  padding: 45.8619px 45.8619px 45.8619px 45.8619px;
  border-radius: 0px;
  border: 0px none rgb(165, 200, 235);
  font-size: 15.2873px;
  font-weight: 300;
```

### Input — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(255, 254, 247);
  color: rgb(0, 0, 0);
  padding: 7.64365px 11.4655px 0px 0px;
  border-radius: 0px;
  border: 0px 0px 1px none none solid rgb(0, 0, 0) rgb(0, 0, 0) rgb(170, 170, 170);
  font-size: 15.2873px;
  font-weight: 300;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 254, 247);
  color: rgb(0, 0, 0);
  padding: 0px 11.4655px 7.64365px 0px;
  border-radius: 0px;
  border: 0px 0px 1px none none solid rgb(0, 0, 0) rgb(0, 0, 0) rgb(170, 170, 170);
  font-size: 15.2873px;
  font-weight: 300;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 254, 247);
  padding: 5.80918px 5.80918px 5.80918px 19.1091px;
  border-radius: 1280px;
  border: 1px solid rgb(0, 0, 0);
  font-size: 15.2873px;
  font-weight: 300;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 254, 247);
  padding: 30.5746px 30.5746px 30.5746px 30.5746px;
  border-radius: 0px;
  border: 0px none rgb(255, 254, 247);
  font-size: 15.2873px;
  font-weight: 400;
```

## Layout System

**11 grid containers** and **187 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1834.48px | 0px |
| 1280px | 0px |
| 396.058px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 4x |
| 2-column | 2x |
| 5-column | 2x |
| 3-column | 1x |
| 6-column | 1x |
| 11-column | 1x |

### Grid Templates

```css
grid-template-columns: 189.578px 1px 189.578px 1px 189.578px 1px 189.578px 1px 189.578px 1px 189.578px;
gap: 7.64365px;
grid-template-columns: 152.188px 152.203px 152.188px 152.203px 152.188px 152.203px;
gap: 61.1492px;
grid-template-columns: 426px 1px 426px 1px 426px;
grid-template-columns: 91.0625px 91.0781px 91.0781px 91.0781px 91.0625px 91.0781px 91.0781px 91.0781px 91.0625px 91.0781px 91.0781px 91.0781px;
gap: 11.4655px;
grid-template-columns: 91.0625px 91.0781px 91.0781px 91.0781px 91.0625px 91.0781px 91.0781px 91.0781px 91.0625px 91.0781px 91.0781px 91.0781px;
gap: 11.4655px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 83x |
| row/nowrap | 99x |
| row/wrap | 5x |

**Gap values:** `11.4655px`, `15.2873px`, `19.1091px`, `22.931px`, `3.82183px`, `30.5746px`, `45.8619px`, `45.8619px 11.4655px`, `5.80918px`, `61.1492px`, `7.64365px`, `76.4365px`, `9.55457px`, `9.631px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 87/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 92/100 |
| Spacing System | 70/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 108 !important rules — prefer specificity over overrides
- 82% of CSS is unused — consider purging
- 4978 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 4 | bold |
| linear | — | 2 | brand |

```css
background: linear-gradient(rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.2) 20%, rgba(255, 255, 255, 0.2) 80%, rgba(255, 255, 255, 0));
background: linear-gradient(rgb(77, 76, 74), rgb(0, 0, 0));
```

## Z-Index Map

**16 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,2147483647 | div.c.u.r.s.o.r.-.d.o.t, div.c.u.r.s.o.r, a.l.o.g.o.-.l.i.n.k. .w.-.n.a.v.-.b.r.a.n.d. .w.-.-.c.u.r.r.e.n.t |
| dropdown | 999,999 | section.s.e.c.t.i.o.n._.n.a.v |
| sticky | 10,40 | button.m.e.n.u.-.b.u.t.t.o.n, div.g.r.a.d.i.e.n.t.-.l.i.n.e.-.d.i.v.i.d.e, div.g.r.a.d.i.e.n.t.-.l.i.n.e.-.d.i.v.i.d.e |
| base | -1000,9 | span.s.w.i.p.e.r.-.n.o.t.i.f.i.c.a.t.i.o.n, span.s.w.i.p.e.r.-.n.o.t.i.f.i.c.a.t.i.o.n, video |

**Issues:**
- [object Object]

## SVG Icons

**11 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 4 |
| md | 3 |
| xl | 4 |

**Icon colors:** `currentColor`, `inherit`, `currentcolor`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | normal | normal |
| Switzer | self-hosted | 300, 400 | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 11 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:2 (8x), 3:4 (4x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `550ms` | 550 |

### Easing Families

- **ease-in-out** (6 uses) — `ease`
- **custom** (14 uses) — `cubic-bezier(0.65, 0.05, 0, 1)`, `cubic-bezier(0.625, 0.05, 0, 1)`, `cubic-bezier(0.25, 0.1, 0.25, 1)`
- **linear** (6 uses) — `linear`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `marquee_timeline` | slide-x | transform | 1 |

## Component Anatomy

### button — 17 instances

**Slots:** label
**Variants:** link

| variant | count | sample label |
|---|---|---|
| default | 16 | Menu

Close |
| link | 1 | VIEW ALL PROJECTS |

### input — 4 instances


### card — 3 instances

**Slots:** media

## Brand Voice

**Tone:** neutral · **Pronoun:** we→you · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **send** (3)
- **menu** (2)
- **view** (1)
- **home** (1)
- **projects** (1)
- **what** (1)
- **latest** (1)
- **get** (1)

### Button Copy Patterns

- "send enquiry" (3×)
- "menu

close" (2×)
- "view all projects" (1×)
- "home" (1×)
- "projects" (1×)
- "what we do" (1×)
- "latest news" (1×)
- "get in touch" (1×)

### Sample Headings

> Production, design, and the art of the possible.
> We are artists, designers,
producers, creatives, clients
and technicians. We work
together to create immersive
experiences and bring ideas to
life in real-world spaces.
> Halo Masterpiece
> Impossible to ignore
> Silent Fall
> Production, design, and the art of the possible.
> We are artists, designers,
producers, creatives, clients
and technicians. We work
together to create immersive
experiences and bring ideas to
life in real-world spaces.
> Halo Masterpiece
> Impossible to ignore
> Silent Fall

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** Creative Giants design and produce immersive activations and unique public art experiences across the UK. From bold brand events to world-class exhibitions, we make ambitious ideas real.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): testimonials → nav → content → hero → content → content → cta → testimonial → content → hero → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | testimonials | Production, design, and the art of the possible. | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | content | — | 0.3 |
| 3 | hero | Production, design, and the art of the possible. | 0.85 |
| 4 | content | We are artists, designers,
producers, creatives, clients
and technicians. We wor | 0.3 |
| 5 | content | Halo Masterpiece | 0.3 |
| 6 | cta | Let’s make
things happen. | 0.4 |
| 7 | testimonial | — | 0.8 |
| 8 | content | Stay up to date | 0.3 |
| 9 | hero | Speak to us. | 0.4 |
| 10 | footer | Ready to kick start a discovery session? | 0.95 |

## Material Language

**Label:** `material-you` (confidence 0.45)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.391 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 1529px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.542)
**Counts:** total 12, svg 0, icon 0, screenshot-like 0, photo-like 11
**Dominant aspect:** landscape
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Switzer` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
