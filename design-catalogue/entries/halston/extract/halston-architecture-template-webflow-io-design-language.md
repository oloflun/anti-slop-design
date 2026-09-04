# Design Language: Halston - Webflow HTML website template

> Extracted from `https://halston-architecture-template.webflow.io/` on September 4, 2026
> 1244 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#583939` | hsl(0, 21%, 28%) | 85 |
| `#000000` | hsl(0, 0%, 0%) | 66 |
| `#ffffff` | hsl(0, 0%, 100%) | 18 |
| `#99988f` | hsl(54, 5%, 58%) | 9 |

### Background Colors

Used on large-area elements: `#583939`

### Text Colors

Text color palette: `#000000`, `#583939`, `#ffffff`

### Gradients

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 40%, color(srgb 0.09 0.0894118 0.0841176));
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0), color(srgb 0.09 0.0894118 0.0841176) 70%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0), color(srgb 0.09 0.0894118 0.0841176));
```

```css
background-image: linear-gradient(0deg, color(srgb 0.09 0.0894118 0.0841176), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(135deg, color(srgb 0.09 0.0894118 0.0841176), rgba(0, 0, 0, 0) 65%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#583939` | background, text, border | 85 |
| `#000000` | text, border | 66 |
| `#ffffff` | text, border | 18 |
| `#99988f` | background | 9 |

## Typography

### Font Families

- **General Sans** — used for all (1169 elements)
- **JetBrains Mono** — used for body (40 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 192px | 12rem | 500 | 153.6px | -6.4px | p, span |
| 115.2px | 7.2rem | 600 | 92.16px | normal | div, span |
| 102.4px | 6.4rem | 600 | 102.4px | -6.4px | div, span, img |
| 56px | 3.5rem | 500 | 56px | normal | h2 |
| 51.2px | 3.2rem | 500 | 51.2px | normal | div, span |
| 40.8px | 2.55rem | 500 | 40.8px | normal | h1, span, p |
| 38.4px | 2.4rem | 500 | 38.4px | normal | div, span |
| 30px | 1.875rem | 500 | 30px | normal | div, span, h2 |
| 26.4px | 1.65rem | 500 | 26.4px | normal | a, h2, span, p |
| 25.6px | 1.6rem | 500 | 25.6px | 12.8px | h2, span |
| 20.4px | 1.275rem | 500 | 22.44px | normal | div |
| 19.2px | 1.2rem | 400 | 19.2px | normal | div, p |
| 17.2px | 1.075rem | 500 | 25.8px | normal | h2, span, p |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14.6px | 0.9125rem | 400 | 18.98px | 0.8px | a, div |

### Heading Scale

```css
h2 { font-size: 56px; font-weight: 500; line-height: 56px; }
h1 { font-size: 40.8px; font-weight: 500; line-height: 40.8px; }
h2 { font-size: 30px; font-weight: 500; line-height: 30px; }
h2 { font-size: 26.4px; font-weight: 500; line-height: 26.4px; }
h2 { font-size: 25.6px; font-weight: 500; line-height: 25.6px; }
h2 { font-size: 17.2px; font-weight: 500; line-height: 25.8px; }
```

### Body Text

```css
body { font-size: 13.6px; font-weight: 500; line-height: 13.6px; }
```

### Font Weights in Use

`400` (618x), `500` (461x), `600` (148x), `200` (15x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-3 | 3px | 0.1875rem |
| spacing-42 | 42px | 2.625rem |
| spacing-48 | 48px | 3rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-115 | 115px | 7.1875rem |
| spacing-192 | 192px | 12rem |
| spacing-320 | 320px | 20rem |
| spacing-483 | 483px | 30.1875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 50 |
| full | 50px | 13 |

## CSS Custom Properties

### Colors

```css
--background-colors--body-background: var(--section-colors--light-base);
--_typography---primary-font: "General Sans",Arial,sans-serif;
--text-colors--primary-text: var(--_colors---brand-accent-primary--brand-accent-900);
--brand-accent--secondary-base: var(--_colors---accent-secondary--accent-secondary-500);
--_colors---brand-accent-primary--brand-accent-500: var(--_colors---brand-accent-primary--brand-accent-default);
--section-colors--light-base: var(--_colors---brand-accent-primary--brand-accent-100);
--section-colors--light-strong: var(--_colors---brand-accent-primary--brand-accent-200);
--section-colors--light-subtle: var(--_colors---brand-accent-primary--brand-accent-50);
--section-colors--dark-strong: var(--_colors---brand-accent-primary--brand-accent-900);
--brand-accent--subtle: var(--_colors---brand-accent-primary--brand-accent-50);
--_colors---neutral--transparent: transparent;
--section-colors--dark-base: var(--_colors---brand-accent-primary--brand-accent-800);
--text-colors--inverse-text: var(--_colors---brand-accent-primary--brand-accent-50);
--section-colors--dark-subtle: var(--_colors---brand-accent-primary--brand-accent-700);
--section-colors--secondary-light-subtle: var(--_colors---accent-secondary--accent-secondary-50);
--section-colors--secondary-light-base: var(--_colors---accent-secondary--accent-secondary-100);
--section-colors--secondary-light-strong: var(--_colors---accent-secondary--accent-secondary-200);
--section-colors--secondary-dark-strong: var(--_colors---accent-secondary--accent-secondary-900);
--section-colors--secondary-dark-base: var(--_colors---accent-secondary--accent-secondary-800);
--_colors---accent-secondary--accent-secondary-100: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)30%,white);
--section-colors--secondary-dark-subtle: var(--_colors---accent-secondary--accent-secondary-700);
--brand-accent--secondary-subtle: var(--_colors---accent-secondary--accent-secondary-300);
--brand-accent--strong: var(--_colors---brand-accent-primary--brand-accent-800);
--brand-accent--base: var(--_colors---brand-accent-primary--brand-accent-300);
--_colors---accent-secondary--accent-secondary-50: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)20%,white);
--_colors---accent-secondary--accent-secondary-200: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)50%,white);
--background-colors--body-background-dark: var(--section-colors--dark-base);
--_colors---neutral-colors--neutral-500: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)50%,white);
--_colors---neutral-colors--neutral-0: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)2%,white);
--_colors---neutral-colors--neutral-50: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)5%,white);
--_colors---neutral-colors--neutral-100: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)10%,white);
--_colors---neutral-colors--neutral-200: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)20%,white);
--_colors---neutral-colors--neutral-300: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)30%,white);
--_colors---neutral-colors--neutral-400: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)40%,white);
--_colors---neutral-colors--neutral-600: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)80%,white);
--_colors---neutral-colors--neutral-700: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)90%,black);
--_colors---neutral-colors--neutral-800: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)80%,black);
--_colors---neutral-colors--neutral-900: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)70%,black);
--_colors---neutral-colors--neutral-950: color-mix(in srgb,var(--_colors---neutral-colors--neutral-accent-color)50%,black);
--_colors---brand-accent-primary--brand-accent-300: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)70%,white);
--_colors---brand-accent-primary--brand-accent-10: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)10%,white);
--_colors---brand-accent-primary--brand-accent-50: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)25%,white);
--_colors---brand-accent-primary--brand-accent-100: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)35%,white);
--_colors---brand-accent-primary--brand-accent-200: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)45%,white);
--_colors---brand-accent-primary--brand-accent-400: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)90%,white);
--_colors---brand-accent-primary--brand-accent-600: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)65%,black);
--_colors---brand-accent-primary--brand-accent-700: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)50%,black);
--_colors---brand-accent-primary--brand-accent-800: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)30%,black);
--_colors---brand-accent-primary--brand-accent-900: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)15%,black);
--_colors---brand-accent-primary--brand-accent-950: color-mix(in srgb,var(--_colors---brand-accent-primary--brand-accent-default)10%,black);
--_colors---brand-accent-primary--brand-accent-default: #99988f;
--_colors---brand-accent-primary-opacity--brand-30: color-mix(in srgb,var(--brand-accent--base)30%,transparent);
--_colors---state--success: #24690a;
--_colors---state--error: #eb2c2f;
--text-colors--secondary-text: var(--_colors---brand-accent-primary--brand-accent-800);
--_colors---dark-opacity--dark-20: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)20%,transparent);
--_colors---light-opacity--light-05: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)5%,transparent);
--brand-accent--secondary-strong: var(--_colors---accent-secondary--accent-secondary-700);
--_colors---brand-opacity-light--brand-light-50: color-mix(in srgb,var(--brand-accent--subtle)50%,transparent);
--_colors---brand-opacity-light--brand-light-80: color-mix(in srgb,var(--brand-accent--subtle)80%,transparent);
--_colors---brand-accent-primary-opacity--brand-70: color-mix(in srgb,var(--brand-accent--base)70%,transparent);
--_colors---dark-opacity--dark-30: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)30%,transparent);
--_colors---brand-accent-primary-opacity--brand-60: color-mix(in srgb,var(--brand-accent--base)60%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-20: color-mix(in srgb,var(--brand-accent--secondary-base)20%,transparent);
--_colors---brand-accent-primary-opacity--brand-10: color-mix(in srgb,var(--brand-accent--base)10%,transparent);
--_colors---accent-secondary--accent-secondary-default: #583939;
--_colors---accent-secondary--accent-secondary-300: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)70%,white);
--_colors---accent-secondary--accent-secondary-400: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)90%,white);
--_colors---accent-secondary--accent-secondary-500: var(--_colors---accent-secondary--accent-secondary-default);
--_colors---accent-secondary--accent-secondary-600: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)65%,black);
--_colors---accent-secondary--accent-secondary-700: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)50%,black);
--_colors---accent-secondary--accent-secondary-800: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)30%,black);
--_colors---accent-secondary--accent-secondary-900: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)15%,black);
--_colors---accent-secondary--accent-secondary-950: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)10%,black);
--_colors---accent-secondary--accent-secondary-10: color-mix(in srgb,var(--_colors---accent-secondary--accent-secondary-default)10%,white);
--borders--border-default-color: var(--_colors---brand-accent-primary-opacity--brand-40);
--text-colors--muted-text: var(--_colors---brand-accent-primary--brand-accent-200);
--_colors---brand-accent-secondary-opacity--brand-secondary-60: color-mix(in srgb,var(--brand-accent--secondary-base)60%,transparent);
--_colors---brand-opacity-light--brand-light-70: color-mix(in srgb,var(--brand-accent--subtle)70%,transparent);
--_colors---brand-accent-primary-opacity--brand-50: color-mix(in srgb,var(--brand-accent--base)50%,transparent);
--_colors---dark-opacity--dark-40: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)40%,transparent);
--_colors---brand-accent-primary-opacity--brand-90: color-mix(in srgb,var(--brand-accent--base)90%,transparent);
--_colors---brand-accent-primary-opacity--brand-80: color-mix(in srgb,var(--brand-accent--base)80%,transparent);
--_colors---brand-accent-primary-opacity--brand-40: color-mix(in srgb,var(--brand-accent--base)40%,transparent);
--_colors---brand-accent-primary-opacity--brand-20: color-mix(in srgb,var(--brand-accent--base)20%,transparent);
--_colors---brand-accent-primary-opacity--brand-05: color-mix(in srgb,var(--brand-accent--base)5%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-90: color-mix(in srgb,var(--brand-accent--secondary-base)90%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-80: color-mix(in srgb,var(--brand-accent--secondary-base)80%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-70: color-mix(in srgb,var(--brand-accent--secondary-base)70%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-50: color-mix(in srgb,var(--brand-accent--secondary-base)50%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-40: color-mix(in srgb,var(--brand-accent--secondary-base)40%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-30: color-mix(in srgb,var(--brand-accent--secondary-base)30%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-10: color-mix(in srgb,var(--brand-accent--secondary-base)10%,transparent);
--_colors---brand-accent-secondary-opacity--brand-secondary-05: color-mix(in srgb,var(--brand-accent--secondary-base)5%,transparent);
--_colors---brand-opacity-light--brand-light-90: color-mix(in srgb,var(--brand-accent--subtle)90%,transparent);
--_colors---brand-opacity-light--brand-light-60: color-mix(in srgb,var(--brand-accent--subtle)60%,transparent);
--_colors---brand-opacity-light--brand-light-40: color-mix(in srgb,var(--brand-accent--subtle)40%,transparent);
--_colors---brand-opacity-light--brand-light-30: color-mix(in srgb,var(--brand-accent--subtle)30%,transparent);
--_colors---brand-opacity-light--brand-light-20: color-mix(in srgb,var(--brand-accent--subtle)20%,transparent);
--_colors---brand-opacity-light--brand-light-10: color-mix(in srgb,var(--brand-accent--subtle)10%,transparent);
--_colors---neutral-colors--neutral-accent-color: var(--_colors---brand-accent-primary--brand-accent-800);
--_colors---dark-opacity--primary-neutral-dark: var(--section-colors--dark-base);
--_colors---dark-opacity--dark-90: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)90%,transparent);
--_colors---dark-opacity--dark-80: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)80%,transparent);
--_colors---dark-opacity--dark-70: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)70%,transparent);
--_colors---dark-opacity--dark-60: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)60%,transparent);
--_colors---dark-opacity--dark-50: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)50%,transparent);
--_colors---dark-opacity--dark-10: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)10%,transparent);
--_colors---dark-opacity--dark-05: color-mix(in srgb,var(--_colors---dark-opacity--primary-neutral-dark)5%,transparent);
--_colors---light-opacity--primary-neutral-light: var(--section-colors--light-subtle);
--_colors---light-opacity--light-90: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)90%,transparent);
--_colors---light-opacity--light-80: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)80%,transparent);
--_colors---light-opacity--light-70: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)70%,transparent);
--_colors---light-opacity--light-60: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)60%,transparent);
--_colors---light-opacity--light-50: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)50%,transparent);
--_colors---light-opacity--light-40: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)40%,transparent);
--_colors---light-opacity--light-30: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)30%,transparent);
--_colors---light-opacity--light-20: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)20%,transparent);
--_colors---light-opacity--light-10: color-mix(in srgb,var(--_colors---light-opacity--primary-neutral-light)10%,transparent);
--_colors---state--accepting: #bee6af;
--_colors---state--declined: #faea7f;
```

### Spacing

```css
--layout-core-sizes--body-size: var(--_layout---body-sizes--body-medium);
--_typography---h1--h1-margin-top: var(--_layout---spacing--space-medium);
--_typography---h1--h1-margin-bottom: var(--_layout---spacing--space-xlarge);
--_typography---h1--h1-font-size: var(--_text-styles---heading-size--large);
--_typography---h2--h2-margin-top: var(--_layout---spacing--space-medium);
--_typography---h2--h2-margin-bottom: var(--_layout---spacing--space-medium);
--_typography---h2--h2-font-size: var(--_text-styles---heading-size--medium);
--_typography---h3--h3-margin-top: var(--_layout---spacing--space-medium);
--_typography---h3--h3-margin-bottom: var(--_layout---spacing--space-small);
--_typography---h3--h3-font-size: var(--_text-styles---heading-size--small);
--_typography---h4--h4-margin-top: var(--_layout---spacing--space-medium);
--_typography---h4--h4-margin-bottom: var(--_layout---spacing--space-medium);
--_typography---h4--h4-font-size: var(--_text-styles---heading-size--xsmall);
--_typography---h5--h5-margin-top: var(--_layout---spacing--space-medium);
--_typography---h5--h5-margin-bottom: var(--_layout---spacing--space-medium);
--_typography---h5--h5-font-size: var(--_text-styles---heading-size--xsmall);
--_typography---h6--h6-margin-top: var(--_layout---spacing--space-medium);
--_typography---h6--h6-margin-bottom: var(--_layout---spacing--space-medium);
--_typography---h6--h6-font-size: var(--_text-styles---heading-size--xsmall);
--_typography---paragraph--paragraph-margin-top: var(--_layout---spacing--space-small);
--_typography---paragraph--paragraph-margin-bottom: var(--_layout---spacing--space-medium);
--_typography---paragraph--paragraph-font-size: var(--_text-styles---paragraph-size--medium);
--_layout---spacing--space-large: clamp(1rem,.9rem + .5vw,1.5rem);
--_layout---raw-sizes--size-025: .25rem;
--_layout---spacing--space-xsmall: clamp(.25rem,.2rem + .25vw,.5rem);
--_layout---spacing--space-2xsmall: clamp(.125rem,.1rem + .125vw,.25rem);
--layout-core-sizes--spacing-default: var(--_layout---spacing--space-medium);
--_layout---spacing--space-xlarge: clamp(1.25rem,1.1rem + .75vw,2rem);
--layout-core-sizes--container-max-width: var(--_layout---container--container-default);
--layout-core-sizes--container-padding: var(--layout-core-sizes--gap-default);
--layout-core-sizes--gap-default: var(--_layout---spacing--space-medium);
--layout-core-sizes--padding-default: var(--_layout---padding--padding-medium);
--_layout---spacing--no-space: 0rem;
--_layout---raw-sizes--size-5: 5rem;
--_layout---layout-calculations--nav-size: 3rem;
--_typography---label--label-font-size: var(--_text-styles---paragraph-size--xsmall);
--_layout---raw-sizes--size-075: .75rem;
--_layout---raw-sizes--size-2: 2rem;
--_text-styles---heading-size--medium: clamp(1.5rem,1.45rem + .25vw,1.75rem);
--_text-styles---heading-size--large: clamp(1.5rem,1.375rem + .625vw,2.125rem);
--_text-styles---heading-size--2xlarge: clamp(2.375rem,2rem + 1.875vw,4.25rem);
--_text-styles---heading-size--small: clamp(1.125rem,1.075rem + .25vw,1.375rem);
--_text-styles---heading-size--xsmall: clamp(1rem,.975rem + .125vw,1.125rem);
--_text-styles---heading-size--2xsmall: clamp(.8125rem,.7875rem + .125vw,.9375rem);
--_text-styles---heading-size--xlarge: clamp(1.875rem,1.65rem + 1.125vw,3rem);
--_text-styles---paragraph-size--medium: clamp(1rem,.975rem + .125vw,1.125rem);
--_text-styles---paragraph-size--large: clamp(1.125rem,1.1rem + .125vw,1.25rem);
--_text-styles---paragraph-size--small: clamp(.9375rem,.9125rem + .125vw,1rem);
--_text-styles---paragraph-size--xlarge: clamp(1.2rem,1.12rem + .4vw,1.6rem);
--layout-core-sizes--radius-default: var(--_layout---radius--radius-small);
--_layout---spacing--space-small: clamp(.5rem,.45rem + .25vw,.75rem);
--_layout---spacing--space-medium: clamp(.75rem,.7rem + .25vw,1rem);
--_text-styles---paragraph-size--2xsmall: clamp(.8125rem,.8rem + .0625vw,.875rem);
--_text-styles---paragraph-size--xsmall: clamp(.875rem,.8625rem + .0625vw,.9375rem);
--_layout---raw-sizes--size-8: 8rem;
--_layout---raw-sizes--size-200: 20rem;
--_layout---raw-sizes--size-05: .5rem;
--_layout---layout-calculations--nav-size<deleted|variable-722f8f2d-f280-bb08-c313-519bcc824856>: calc(var(--layout-core-sizes--action-size-default) + 2*var(--layout-core-sizes--nav-gap));
--_layout---raw-sizes--size-3: 3rem;
--_layout---spacing--fluid-spacing-medium: 2.5vw;
--_layout---padding--padding-large: clamp(2rem,1.5rem + 6vw,6rem);
--_layout---padding--padding-xlarge: clamp(3rem,2rem + 6vw,8rem);
--_layout---spacing--space-2xlarge: clamp(2rem,1.8rem + 1vw,3rem);
--_layout---raw-sizes--size-1: 1rem;
--_layout---spacing--fluid-spacing-large: 5vw;
--_layout---spacing--space-3xlarge: clamp(3rem,2.8rem + 1vw,4rem);
--_layout---raw-sizes--size-25: 2.5rem;
--_layout---raw-sizes--size-15: 1.5rem;
--_layout---raw-sizes--size-125: 1.25rem;
--_layout---raw-sizes--size-015: .15rem;
--layout-core-sizes--nav-gap: var(--_layout---spacing--no-space);
--_layout---spacing--fluid-spacing-small: 1.5vw;
--_layout---padding--padding-medium: clamp(2rem,1rem + 4vw,4rem);
--_layout---raw-sizes--size-175: 1.75rem;
--_layout---raw-sizes--size-100: 10rem;
--_layout---raw-sizes--size-4: 4rem;
--_text-styles---paragraph-size--2xlarge: clamp(1.3rem,1.16rem + .7vw,2rem);
--_layout---spacing--fluid-spacing-xlarge: 10vw;
--_layout---padding--padding-small: clamp(1rem,.8rem + 1vw,2rem);
--_layout---body-sizes--body-small: .875rem;
--_layout---body-sizes--body-medium: 1rem;
--_layout---body-sizes--body-large: 1.125rem;
--_layout---body-sizes--body-xlarge: 1.25rem;
--layout-core-sizes--button-radius-default: var(--_layout---radius--radius-max);
--layout-core-sizes--action-size-default: var(--_layout---action-sizes--medium);
--_layout---raw-sizes--size-35: 3.5rem;
--_layout---raw-sizes--size-45: 4.5rem;
--_layout---raw-sizes--size-6: 6rem;
--_layout---raw-sizes--size-7: 7rem;
--_layout---raw-sizes--size-9: 9rem;
--_layout---raw-sizes--size-150: 15rem;
--_layout---raw-sizes--size-300: 30rem;
--_layout---action-sizes--small: clamp(2rem,1.9rem + .5vw,2.5rem);
--_layout---action-sizes--medium: clamp(2.5rem,2.35rem + .75vw,3.25rem);
--_layout---action-sizes--large: clamp(3rem,2.8rem + 1vw,4rem);
--_layout---container-padding--container-padding-small: clamp(1rem,.8rem + 1vw,2rem);
--_layout---container-padding--container-padding-medium: clamp(1.25rem,.95rem + 1.5vw,3rem);
--_layout---container-padding--container-padding-large: clamp(1.5rem,1rem + 2.5vw,4rem);
--_layout---container-padding--container-padding-xlarge: clamp(2rem,1.3rem + 3.5vw,6rem);
```

### Typography

```css
--_text-styles---line-height--130: 130%;
--_text-styles---weight--normal: 400;
--_typography---h1--h1-font-family: var(--typography--heading);
--_typography---h1--h1-line-height: var(--_text-styles---line-height--110);
--_typography---h1--h1-font-weight: var(--_text-styles---weight--medium);
--_typography---h2--h2-font-family: var(--typography--heading);
--_typography---h2--h2-line-height: var(--_text-styles---line-height--110);
--_typography---h2--h2-font-weight: var(--_text-styles---weight--medium);
--_typography---h3--h3-font-family: var(--typography--heading);
--_typography---h3--h3-line-height: var(--_text-styles---line-height--110);
--_typography---h3--h3-font-weight: var(--_text-styles---weight--medium);
--_typography---h4--h4-font-family: var(--typography--heading);
--_typography---h4--h4-line-height: var(--_text-styles---line-height--110);
--_typography---h4--h4-font-weight: var(--_text-styles---weight--medium);
--_typography---h5--h5-font-family: var(--typography--heading);
--_typography---h5--h5-line-height: var(--_text-styles---line-height--110);
--_typography---h5--h5-font-weight: var(--_text-styles---weight--medium);
--_typography---h6--h6-font-family: var(--typography--heading);
--_typography---h6--h6-line-height: var(--_text-styles---line-height--110);
--_typography---h6--h6-font-weight: var(--_text-styles---weight--medium);
--_typography---paragraph--paragraph-font-family: var(--typography--body-font);
--_typography---paragraph--paragraph-line-height: var(--_text-styles---line-height--160);
--_typography---paragraph--paragraph-font-weight: var(--_text-styles---weight--medium);
--_text-styles---line-height--150: 150%;
--_text-styles---weight--semi-bold: 600;
--_typography---label--label-line-height: var(--_text-styles---line-height--120);
--_typography---label--label-font-family: var(--typography--label);
--_typography---label--label-font-weight: var(--_text-styles---weight--normal);
--_text-styles---weight--medium: 500;
--_text-styles---line-height--120: 120%;
--_text-styles---line-height--90: 90%;
--_text-styles---line-height--100: 100%;
--_typography---display-font: "General Sans",Arial,sans-serif;
--_text-styles---line-height--80: 80%;
--_text-styles---line-height--140: 140%;
--_text-styles---line-height--110: 110%;
--typography--body-font: var(--_typography---primary-font);
--_text-styles---weight--extra-light: 200;
--_text-styles---line-height--160: 160%;
--_typography---mono-font: "JetBrains Mono",sans-serif;
--_text-styles---weight--thin: 100;
--_text-styles---weight--light: 300;
--_text-styles---weight--bold: 700;
--_text-styles---weight--extra-bold: 800;
--_text-styles---weight--black: 900;
```

### Radii

```css
--_layout---radius--radius-max: 999rem;
--_layout---radius--radius-small: 3px;
--_layout---radius--radius-medium: 6px;
--_layout---radius--radius-large: 10px;
```

### Other

```css
--_layout---container--container-narrow: 90rem;
--typography--heading: var(--_typography---display-font);
--_layout---max-fluid-width--max-fluid-small: clamp(18rem,15.6rem + 12vw,30rem);
--_layout---column--col-2: calc((100% - var(--layout-core-sizes--spacing-default))/2);
--_layout---column--col-3: calc((100% - (2*var(--layout-core-sizes--spacing-default)))/3);
--_layout---column--col-4: calc((100% - (3*var(--layout-core-sizes--spacing-default)))/4);
--_layout---max-width--max-width-30: 30rem;
--_layout---max-width--max-width-40: 40rem;
--_layout---max-width--max-width-48: 48rem;
--_layout---max-width--max-width-56: 56rem;
--_layout---max-width--max-width-64: 64rem;
--_layout---max-width--max-width-72: 72rem;
--_layout---max-width--max-width-80: 80rem;
--_layout---max-width--max-width-35: 35rem;
--_layout---max-width--max-width-20: 20rem;
--_layout---max-width--max-width-15: 15rem;
--_layout---layout-calculations--full-width-section: calc(100% - 2*var(--layout-core-sizes--container-padding));
--_media---image--medium: clamp(15rem,30vw,30rem);
--_media---image--xlarge: clamp(30rem,60vw,60rem);
--_media---image--large: clamp(20rem,40vw,40rem);
--typography--label: var(--_typography---mono-font);
--_layout---max-fluid-width--max-fluid-large: clamp(26rem,22.4rem + 18vw,44rem);
--_layout---column--col-30: calc((100% - var(--layout-core-sizes--spacing-default))*.3);
--_layout---column--col-40: calc((100% - var(--layout-core-sizes--spacing-default))*.4);
--_layout---column--col-60: calc((100% - var(--layout-core-sizes--spacing-default))*.6);
--_layout---column--col-70: calc((100% - var(--layout-core-sizes--spacing-default))*.7);
--_layout---layout-calculations--full-height-section: calc(100svh - 2*var(--layout-core-sizes--container-padding));
--_layout---max-fluid-width--max-fluid-medium: clamp(22rem,19.2rem + 14vw,36rem);
--_layout---max-fluid-width--max-fluid-xlarge: clamp(34rem,29.2rem + 24vw,58rem);
--_layout---max-fluid-width--max-fluid-2xlarge: clamp(42rem,36rem + 30vw,72rem);
--_layout---max-fluid-width--max-fluid-xsmall: clamp(15rem,13rem + 10vw,25rem);
--_layout---max-fluid-width--max-fluid-2xsmall: clamp(12rem,10.4rem + 8vw,20rem);
--_media---image--2xsmall: clamp(3rem,5vw,5rem);
--_media---image--xsmall: clamp(5rem,10vw,10rem);
--_media---image--small: clamp(10rem,20vw,20rem);
--_layout---max-width--max-width-25: 25rem;
--_layout---max-width--max-width-27: 27rem;
--_media---image--2xlarge: clamp(40rem,80vw,80rem);
--_layout---layout-calculations--full-height-inner-block: calc(100svh - var(--_layout---layout-calculations--nav-size));
--_layout---container--container-article: 60rem;
--_layout---container--container-default: 120rem;
--_layout---container--container-wide: 140rem;
--_layout---container--inner-container: calc(100% - 2*var(--layout-core-sizes--padding-default));
```

### Dependencies

```css
--background-colors--body-background: --section-colors--light-base;
--text-colors--primary-text: --_colors---brand-accent-primary--brand-accent-900;
--layout-core-sizes--body-size: --_layout---body-sizes--body-medium;
--_typography---h1--h1-margin-top: --_layout---spacing--space-medium;
--_typography---h1--h1-margin-bottom: --_layout---spacing--space-xlarge;
--_typography---h1--h1-font-family: --typography--heading;
--_typography---h1--h1-font-size: --_text-styles---heading-size--large;
--_typography---h1--h1-line-height: --_text-styles---line-height--110;
--_typography---h1--h1-font-weight: --_text-styles---weight--medium;
--_typography---h2--h2-margin-top: --_layout---spacing--space-medium;
--_typography---h2--h2-margin-bottom: --_layout---spacing--space-medium;
--_typography---h2--h2-font-family: --typography--heading;
--_typography---h2--h2-font-size: --_text-styles---heading-size--medium;
--_typography---h2--h2-line-height: --_text-styles---line-height--110;
--_typography---h2--h2-font-weight: --_text-styles---weight--medium;
--_typography---h3--h3-margin-top: --_layout---spacing--space-medium;
--_typography---h3--h3-margin-bottom: --_layout---spacing--space-small;
--_typography---h3--h3-font-family: --typography--heading;
--_typography---h3--h3-font-size: --_text-styles---heading-size--small;
--_typography---h3--h3-line-height: --_text-styles---line-height--110;
--_typography---h3--h3-font-weight: --_text-styles---weight--medium;
--_typography---h4--h4-margin-top: --_layout---spacing--space-medium;
--_typography---h4--h4-margin-bottom: --_layout---spacing--space-medium;
--_typography---h4--h4-font-family: --typography--heading;
--_typography---h4--h4-font-size: --_text-styles---heading-size--xsmall;
--_typography---h4--h4-line-height: --_text-styles---line-height--110;
--_typography---h4--h4-font-weight: --_text-styles---weight--medium;
--_typography---h5--h5-margin-top: --_layout---spacing--space-medium;
--_typography---h5--h5-margin-bottom: --_layout---spacing--space-medium;
--_typography---h5--h5-font-family: --typography--heading;
--_typography---h5--h5-font-size: --_text-styles---heading-size--xsmall;
--_typography---h5--h5-line-height: --_text-styles---line-height--110;
--_typography---h5--h5-font-weight: --_text-styles---weight--medium;
--_typography---h6--h6-margin-top: --_layout---spacing--space-medium;
--_typography---h6--h6-margin-bottom: --_layout---spacing--space-medium;
--_typography---h6--h6-font-family: --typography--heading;
--_typography---h6--h6-font-size: --_text-styles---heading-size--xsmall;
--_typography---h6--h6-line-height: --_text-styles---line-height--110;
--_typography---h6--h6-font-weight: --_text-styles---weight--medium;
--_typography---paragraph--paragraph-margin-top: --_layout---spacing--space-small;
--_typography---paragraph--paragraph-margin-bottom: --_layout---spacing--space-medium;
--_typography---paragraph--paragraph-font-family: --typography--body-font;
--_typography---paragraph--paragraph-font-size: --_text-styles---paragraph-size--medium;
--_typography---paragraph--paragraph-line-height: --_text-styles---line-height--160;
--_typography---paragraph--paragraph-font-weight: --_text-styles---weight--medium;
--brand-accent--secondary-base: --_colors---accent-secondary--accent-secondary-500;
--layout-core-sizes--spacing-default: --_layout---spacing--space-medium;
--_colors---brand-accent-primary--brand-accent-500: --_colors---brand-accent-primary--brand-accent-default;
--layout-core-sizes--container-max-width: --_layout---container--container-default;
--layout-core-sizes--container-padding: --layout-core-sizes--gap-default;
--layout-core-sizes--gap-default: --_layout---spacing--space-medium;
--layout-core-sizes--padding-default: --_layout---padding--padding-medium;
--section-colors--light-base: --_colors---brand-accent-primary--brand-accent-100;
--section-colors--light-strong: --_colors---brand-accent-primary--brand-accent-200;
--section-colors--light-subtle: --_colors---brand-accent-primary--brand-accent-50;
--section-colors--dark-strong: --_colors---brand-accent-primary--brand-accent-900;
--brand-accent--subtle: --_colors---brand-accent-primary--brand-accent-50;
--section-colors--dark-base: --_colors---brand-accent-primary--brand-accent-800;
--text-colors--inverse-text: --_colors---brand-accent-primary--brand-accent-50;
--section-colors--dark-subtle: --_colors---brand-accent-primary--brand-accent-700;
--section-colors--secondary-light-subtle: --_colors---accent-secondary--accent-secondary-50;
--section-colors--secondary-light-base: --_colors---accent-secondary--accent-secondary-100;
--section-colors--secondary-light-strong: --_colors---accent-secondary--accent-secondary-200;
--section-colors--secondary-dark-strong: --_colors---accent-secondary--accent-secondary-900;
--section-colors--secondary-dark-base: --_colors---accent-secondary--accent-secondary-800;
--_colors---accent-secondary--accent-secondary-100: --_colors---accent-secondary--accent-secondary-default;
--section-colors--secondary-dark-subtle: --_colors---accent-secondary--accent-secondary-700;
--_typography---label--label-line-height: --_text-styles---line-height--120;
--brand-accent--secondary-subtle: --_colors---accent-secondary--accent-secondary-300;
--brand-accent--strong: --_colors---brand-accent-primary--brand-accent-800;
--_typography---label--label-font-family: --typography--label;
--_typography---label--label-font-size: --_text-styles---paragraph-size--xsmall;
--_typography---label--label-font-weight: --_text-styles---weight--normal;
--typography--heading: --_typography---display-font;
--layout-core-sizes--radius-default: --_layout---radius--radius-small;
--brand-accent--base: --_colors---brand-accent-primary--brand-accent-300;
--_colors---accent-secondary--accent-secondary-50: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-200: --_colors---accent-secondary--accent-secondary-default;
--_layout---layout-calculations--nav-size<deleted|variable-722f8f2d-f280-bb08-c313-519bcc824856>: --layout-core-sizes--action-size-default,--layout-core-sizes--nav-gap;
--background-colors--body-background-dark: --section-colors--dark-base;
--_colors---neutral-colors--neutral-500: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-0: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-50: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-100: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-200: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-300: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-400: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-600: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-700: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-800: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-900: --_colors---neutral-colors--neutral-accent-color;
--_colors---neutral-colors--neutral-950: --_colors---neutral-colors--neutral-accent-color;
--_layout---column--col-2: --layout-core-sizes--spacing-default;
--_layout---column--col-3: --layout-core-sizes--spacing-default;
--_layout---column--col-4: --layout-core-sizes--spacing-default;
--_colors---brand-accent-primary--brand-accent-300: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-10: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-50: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-100: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-200: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-400: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-600: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-700: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-800: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-900: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary--brand-accent-950: --_colors---brand-accent-primary--brand-accent-default;
--_colors---brand-accent-primary-opacity--brand-30: --brand-accent--base;
--text-colors--secondary-text: --_colors---brand-accent-primary--brand-accent-800;
--_colors---dark-opacity--dark-20: --_colors---dark-opacity--primary-neutral-dark;
--_layout---layout-calculations--full-width-section: --layout-core-sizes--container-padding;
--_colors---light-opacity--light-05: --_colors---light-opacity--primary-neutral-light;
--typography--label: --_typography---mono-font;
--brand-accent--secondary-strong: --_colors---accent-secondary--accent-secondary-700;
--_colors---brand-opacity-light--brand-light-50: --brand-accent--subtle;
--_colors---brand-opacity-light--brand-light-80: --brand-accent--subtle;
--typography--body-font: --_typography---primary-font;
--_colors---brand-accent-primary-opacity--brand-70: --brand-accent--base;
--_layout---column--col-30: --layout-core-sizes--spacing-default;
--_layout---column--col-40: --layout-core-sizes--spacing-default;
--_layout---column--col-60: --layout-core-sizes--spacing-default;
--_layout---column--col-70: --layout-core-sizes--spacing-default;
--_layout---layout-calculations--full-height-section: --layout-core-sizes--container-padding;
--_colors---dark-opacity--dark-30: --_colors---dark-opacity--primary-neutral-dark;
--_colors---brand-accent-primary-opacity--brand-60: --brand-accent--base;
--_colors---brand-accent-secondary-opacity--brand-secondary-20: --brand-accent--secondary-base;
--_colors---brand-accent-primary-opacity--brand-10: --brand-accent--base;
--_colors---accent-secondary--accent-secondary-300: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-400: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-500: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-600: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-700: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-800: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-900: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-950: --_colors---accent-secondary--accent-secondary-default;
--_colors---accent-secondary--accent-secondary-10: --_colors---accent-secondary--accent-secondary-default;
--layout-core-sizes--nav-gap: --_layout---spacing--no-space;
--borders--border-default-color: --_colors---brand-accent-primary-opacity--brand-40;
--text-colors--muted-text: --_colors---brand-accent-primary--brand-accent-200;
--_colors---brand-accent-secondary-opacity--brand-secondary-60: --brand-accent--secondary-base;
--_colors---brand-opacity-light--brand-light-70: --brand-accent--subtle;
--_colors---brand-accent-primary-opacity--brand-50: --brand-accent--base;
--_colors---dark-opacity--dark-40: --_colors---dark-opacity--primary-neutral-dark;
--layout-core-sizes--button-radius-default: --_layout---radius--radius-max;
--layout-core-sizes--action-size-default: --_layout---action-sizes--medium;
--_colors---brand-accent-primary-opacity--brand-90: --brand-accent--base;
--_colors---brand-accent-primary-opacity--brand-80: --brand-accent--base;
--_colors---brand-accent-primary-opacity--brand-40: --brand-accent--base;
--_colors---brand-accent-primary-opacity--brand-20: --brand-accent--base;
--_colors---brand-accent-primary-opacity--brand-05: --brand-accent--base;
--_colors---brand-accent-secondary-opacity--brand-secondary-90: --brand-accent--secondary-base;
--_colors---brand-accent-secondary-opacity--brand-secondary-80: --brand-accent--secondary-base;
--_colors---brand-accent-secondary-opacity--brand-secondary-70: --brand-accent--secondary-base;
--_colors---brand-accent-secondary-opacity--brand-secondary-50: --brand-accent--secondary-base;
--_colors---brand-accent-secondary-opacity--brand-secondary-40: --brand-accent--secondary-base;
--_colors---brand-accent-secondary-opacity--brand-secondary-30: --brand-accent--secondary-base;
--_colors---brand-accent-secondary-opacity--brand-secondary-10: --brand-accent--secondary-base;
--_colors---brand-accent-secondary-opacity--brand-secondary-05: --brand-accent--secondary-base;
--_colors---brand-opacity-light--brand-light-90: --brand-accent--subtle;
--_colors---brand-opacity-light--brand-light-60: --brand-accent--subtle;
--_colors---brand-opacity-light--brand-light-40: --brand-accent--subtle;
--_colors---brand-opacity-light--brand-light-30: --brand-accent--subtle;
--_colors---brand-opacity-light--brand-light-20: --brand-accent--subtle;
--_colors---brand-opacity-light--brand-light-10: --brand-accent--subtle;
--_colors---neutral-colors--neutral-accent-color: --_colors---brand-accent-primary--brand-accent-800;
--_colors---dark-opacity--primary-neutral-dark: --section-colors--dark-base;
--_colors---dark-opacity--dark-90: --_colors---dark-opacity--primary-neutral-dark;
--_colors---dark-opacity--dark-80: --_colors---dark-opacity--primary-neutral-dark;
--_colors---dark-opacity--dark-70: --_colors---dark-opacity--primary-neutral-dark;
--_colors---dark-opacity--dark-60: --_colors---dark-opacity--primary-neutral-dark;
--_colors---dark-opacity--dark-50: --_colors---dark-opacity--primary-neutral-dark;
--_colors---dark-opacity--dark-10: --_colors---dark-opacity--primary-neutral-dark;
--_colors---dark-opacity--dark-05: --_colors---dark-opacity--primary-neutral-dark;
--_colors---light-opacity--primary-neutral-light: --section-colors--light-subtle;
--_colors---light-opacity--light-90: --_colors---light-opacity--primary-neutral-light;
--_colors---light-opacity--light-80: --_colors---light-opacity--primary-neutral-light;
--_colors---light-opacity--light-70: --_colors---light-opacity--primary-neutral-light;
--_colors---light-opacity--light-60: --_colors---light-opacity--primary-neutral-light;
--_colors---light-opacity--light-50: --_colors---light-opacity--primary-neutral-light;
--_colors---light-opacity--light-40: --_colors---light-opacity--primary-neutral-light;
--_colors---light-opacity--light-30: --_colors---light-opacity--primary-neutral-light;
--_colors---light-opacity--light-20: --_colors---light-opacity--primary-neutral-light;
--_colors---light-opacity--light-10: --_colors---light-opacity--primary-neutral-light;
--_layout---layout-calculations--full-height-inner-block: --_layout---layout-calculations--nav-size;
--_layout---container--inner-container: --layout-core-sizes--padding-default;
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

**Durations:** `0.001s`, `0.2s`

### Common Transitions

```css
transition: overflow 0.001s allow-discrete;
transition: all;
transition: color 0.2s;
transition: color 0.2s, border-color 0.2s;
transition: background-color 0.2s;
transition: opacity 0.2s;
transition: padding 0.2s, background-color 0.2s, color 0.2s;
transition: border-color 0.2s, opacity 0.2s;
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

### Buttons (7 instances)

```css
.button {
  color: color(srgb 0.172549 0.111765 0.111765);
  font-size: 16px;
  font-weight: 400;
  padding-top: 10.4px;
  padding-right: 14.4px;
  border-radius: 0px;
}
```

### Links (76 instances)

```css
.link {
  color: color(srgb 0.09 0.0894118 0.0841176);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (27 instances)

```css
.navigatio {
  color: color(srgb 0.09 0.0894118 0.0841176);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (44 instances)

```css
.foote {
  background-color: color(srgb 0.172549 0.111765 0.111765);
  color: color(srgb 0.09 0.0894118 0.0841176);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 13.6px;
}
```

### Modals (1 instances)

```css
.modal {
  background-color: color(srgb 0.09 0.0894118 0.0841176);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (85 instances)

```css
.dropdown {
  background-color: color(srgb 0.410588 0.301176 0.301176);
  border-radius: 0px;
  border-color: color(srgb 0.09 0.0894118 0.0841176);
  padding-top: 0px;
}
```

### Badges (44 instances)

```css
.badge {
  color: color(srgb 0.09 0.0894118 0.0841176);
  font-size: 16px;
  font-weight: 400;
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

### Button — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: color(srgb 0.172549 0.111765 0.111765);
  padding: 10.4px 14.4px 10.4px 14.4px;
  border-radius: 0px;
  border: 1px solid color(srgb 0.18 0.178824 0.168235);
  font-size: 16px;
  font-weight: 400;
```

### Button — 24 instances, 1 variant

**Variant 1** (24 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: color(srgb 0.172549 0.111765 0.111765);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none color(srgb 0.172549 0.111765 0.111765);
  font-size: 13.6px;
  font-weight: 500;
```

### Button — 12 instances, 1 variant

**Variant 1** (12 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: color(srgb 0.172549 0.111765 0.111765);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none color(srgb 0.172549 0.111765 0.111765);
  font-size: 16px;
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
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**12 grid containers** and **218 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1280px | 0px |
| 486.4px | 0px |
| 100% | 0px |
| 960px | 0px |
| 588.8px | 0px |
| 480px | 41.6px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 8x |
| 4-column | 4x |

### Grid Templates

```css
grid-template-columns: 302px 302.016px 302.016px 302.016px;
gap: 14.4px;
grid-template-columns: 407.469px 407.484px 407.469px;
gap: 14.4px;
grid-template-columns: 397.875px 397.875px 397.875px;
gap: 14.4px;
grid-template-columns: 203.734px 814.953px 203.734px;
gap: 14.4px;
grid-template-columns: 203.734px 814.953px 203.734px;
gap: 14.4px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 139x |
| column/nowrap | 74x |
| row-reverse/nowrap | 3x |
| row/wrap | 2x |

**Gap values:** `10.4px`, `14.4px`, `14.4px 27.2px`, `19.2px`, `20.8px`, `25.6px`, `27.2px`, `28px`, `3.2px`, `3.2px 19.2px`, `32px`, `6.4px`, `64px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 86/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 85/100 |
| Typography Consistency | 82/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- No clear primary brand color detected
- 41 !important rules — prefer specificity over overrides
- 56% of CSS is unused — consider purging
- 3853 duplicate CSS declarations

## Gradients

**5 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | 0deg | 2 | brand |
| linear | 135deg | 2 | brand |

```css
background: linear-gradient(rgba(0, 0, 0, 0) 40%, color(srgb 0.09 0.0894118 0.0841176));
background: linear-gradient(rgba(0, 0, 0, 0), color(srgb 0.09 0.0894118 0.0841176) 70%);
background: linear-gradient(rgba(0, 0, 0, 0), color(srgb 0.09 0.0894118 0.0841176));
background: linear-gradient(0deg, color(srgb 0.09 0.0894118 0.0841176), rgba(0, 0, 0, 0));
background: linear-gradient(135deg, color(srgb 0.09 0.0894118 0.0841176), rgba(0, 0, 0, 0) 65%);
```

## Z-Index Map

**17 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9999,9999 | div.h.e.r.o.-.d.i.s.p.l.a.y.-.p.r.e.l.o.a.d |
| dropdown | 999,999 | nav.n.a.v |
| sticky | 10,99 | div.s.e.c.t.i.o.n.-.r.e.v.e.a.l.-.2.n.d, div.s.e.c.t.i.o.n.-.p.r.o.j.e.c.t.-.l.i.s.t.i.n.g. .w.-.v.a.r.i.a.n.t.-.b.b.d.d.4.e.6.4.-.6.7.2.e.-.f.7.1.d.-.0.4.b.b.-.2.f.0.0.1.e.6.3.4.4.5.5, div.m.e.n.u.-.l.a.y.o.u.t |
| base | -100,9 | video, div.m.e.n.u.-.b.a.c.k.g.r.o.u.n.d, div.m.e.n.u.-.b.a.c.k.g.r.o.u.n.d |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| General Sans | self-hosted | 200 700 | normal |
| JetBrains Mono | google-fonts | 300, 400, 500, 600, 700 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 41 | objectFit: contain, borderRadius: 0px, shape: square |
| hero | 12 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 8 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (42x), 16:9 (5x), 3:2 (4x), 2.49:1 (3x), 3:4 (3x), 4:3 (2x), 9:16 (2x), 2:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |
| `sm` | `200ms` | 200 |

## Component Anatomy

### button — 43 instances

**Slots:** label, icon
**Sizes:** large

## Brand Voice

**Tone:** friendly · **Pronoun:** we-only · **Headings:** Title Case (verbose)

### Top CTA Verbs

- **consultation** (6)
- **read** (6)
- **about** (3)
- **start** (3)

### Button Copy Patterns

- "consultation" (4×)
- "read" (4×)
- "consultation
consultation" (2×)
- "about us" (2×)
- "start your project" (2×)
- "read
read" (2×)
- "about us
about us" (1×)
- "start your project
start your project" (1×)

### Sample Headings

> Wannsee Residence
> BESPOKE LIVING
DEFINED BY CLARITY
> Founded in 2003, Halston is a
deliberately small practice. The
principal architect leads every project
from brief to handover, so the thinking
that shapes the first sketch carries all
the way through to the last detail on
site.
> Every project begins with reading the
site and the brief honestly, then
deciding what the new work should add,
contrast, or preserve. Nothing is drawn
before the questions have been asked
properly.
> WHAT THE WORK IS BUILT ON. THREE
PRINCIPLES THAT RUN THROUGH EVERY
PROJECT WE TAKE ON.
> ARCHITECTURE

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** Build an interactive Webflow CMS website fast with this component-based, content-rich professional template. Perfect for architecture and interior design.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): testimonial → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | Wannsee Residence | 0.9 |
| 1 | testimonial | BESPOKE LIVING
DEFINED BY CLARITY | 0.8 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.104 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 5 |

## Imagery Style

**Label:** `photography` (confidence 0.169)
**Counts:** total 62, svg 34, icon 45, screenshot-like 0, photo-like 21
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `General Sans` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
