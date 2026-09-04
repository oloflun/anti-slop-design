# Design Language: Vistal - Webflow HTML website template

> Extracted from `https://vistal.webflow.io` on September 4, 2026
> 665 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ebf213` | rgb(235, 242, 19) | hsl(62, 90%, 51%) | 1 |
| Secondary | `#8f00ff` | rgb(143, 0, 255) | hsl(274, 100%, 50%) | 1 |
| Accent | `#efd556` | rgb(239, 213, 86) | hsl(50, 83%, 64%) | 128 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 793 |
| `#ffffff` | hsl(0, 0%, 100%) | 419 |
| `#656565` | hsl(0, 0%, 40%) | 32 |
| `#131313` | hsl(0, 0%, 7%) | 27 |
| `#333333` | hsl(0, 0%, 20%) | 11 |
| `#f0efed` | hsl(40, 9%, 94%) | 5 |
| `#bababa` | hsl(0, 0%, 73%) | 2 |
| `#c8c8c8` | hsl(0, 0%, 78%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#000000`, `#efd556`, `#c8c8c8`, `#f0efed`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#333333`, `#131313`, `#efd556`, `#656565`, `#3a3a3a`, `#bababa`

### Gradients

```css
background-image: radial-gradient(circle, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.8)), url("https://cdn.prod.website-files.com/68ed0d0a63da252f1cf81e7e/68ed4dca2f918d4d9bec4e05_cca08177ff658763a1e71f0d6107f6cb_Hero.webp");
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0), rgb(0, 0, 0));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 793 |
| `#ffffff` | background, text, border | 419 |
| `#efd556` | text, border, background | 128 |
| `#656565` | text, border | 32 |
| `#131313` | text, border, background | 27 |
| `#333333` | text, border, background | 11 |
| `#f0efed` | background | 5 |
| `#bababa` | text, border | 2 |
| `#8f00ff` | background | 1 |
| `#c8c8c8` | background | 1 |
| `#ebf213` | background | 1 |

## Typography

### Font Families

- **Inter** — used for all (638 elements)
- **webflow-icons** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 80px | 5rem | 400 | 88px | -3.2px | h1 |
| 72px | 4.5rem | 500 | 79.2px | -2.88px | h2 |
| 64px | 4rem | 500 | 70.4px | -2.56px | h2, span |
| 48px | 3rem | 500 | 52.8px | -1.92px | h2, h4 |
| 40px | 2.5rem | 500 | 48px | -1.2px | h6, div, svg, path |
| 24px | 1.5rem | 400 | 36px | 0.32px | div |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14px | 0.875rem | 600 | 20px | 0.28px | div |
| 12px | 0.75rem | 400 | 18px | -0.36px | div, br |

### Heading Scale

```css
h1 { font-size: 80px; font-weight: 400; line-height: 88px; }
h2 { font-size: 72px; font-weight: 500; line-height: 79.2px; }
h2 { font-size: 64px; font-weight: 500; line-height: 70.4px; }
h2 { font-size: 48px; font-weight: 500; line-height: 52.8px; }
h6 { font-size: 40px; font-weight: 500; line-height: 48px; }
```

### Body Text

```css
body { font-size: 64px; font-weight: 500; line-height: 70.4px; }
```

### Font Weights in Use

`400` (605x), `500` (38x), `600` (22x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-32 | 32px | 2rem |
| spacing-40 | 40px | 2.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-72 | 72px | 4.5rem |
| spacing-95 | 95px | 5.9375rem |
| spacing-109 | 109px | 6.8125rem |
| spacing-120 | 120px | 7.5rem |
| spacing-240 | 240px | 15rem |
| spacing-247 | 247px | 15.4375rem |
| spacing-298 | 298px | 18.625rem |
| spacing-332 | 332px | 20.75rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 3 |
| md | 8px | 1 |
| lg | 12px | 10 |
| xl | 24px | 20 |
| full | 40px | 20 |
| full | 80px | 3 |
| full | 100px | 6 |

## Box Shadows

**xl** — blur: 32px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 14px 32px 0px, rgba(0, 0, 0, 0.09) 0px 58px 58px 0px, rgba(0, 0, 0, 0.05) 0px 130px 78px 0px, rgba(0, 0, 0, 0.01) 0px 232px 93px 0px, rgba(0, 0, 0, 0) 0px 362px 101px 0px;
```

## CSS Custom Properties

### Colors

```css
--bg-color--bg-default: var(--base--white);
--text-color--text-primary: var(--base--black);
--bg-color--bg-accent: var(--base--yellow);
--bg-color--bg-secondary: var(--base--black);
--_sizes---border-radius--small: var(--_sizes---fixed--xlarge);
--bg-color--bg-subtle: var(--grey--grey-100);
--bg-color--bg-primary: var(--base--white);
--text-color--text-secondary: var(--grey--grey-400);
--text-color--text-accent: var(--base--yellow);
--border-color--border-primary<deleted|variable-d4c54ba4-ee41-67ce-58a5-5216ca039f83>: #efeff2;
--_sizes---border-radius--medium: var(--_sizes---fixed--xhuge);
--text-color--text-on-primary: var(--base--white);
--border-color--border-alternate<deleted|variable-551aa6d2-4bf8-6036-137a-78e1c71841a4>: var(--base-color-neutral--neutral-darker\<deleted\|variable-dda6ad91-259a-0202-f70f-965feb273058\>);
--bg-color--bg-button: var(--grey--grey-800);
--bg-color--bg-hover<deleted|variable-07249897-f71c-dd53-6216-4b6845d3f64e>: var(--base--grey-light\<deleted\|variable-e77efb59-b29d-151a-6f0f-bfc9f2744592\>);
--text-color--text-tertiary: var(--grey--grey-200);
--_colors-2---bg-color--bg-secondary<deleted|variable-cdd04b90-31c4-c33e-cf74-59e4718ac2ba>: var(--_colors-2---grey--grey-300\<deleted\|variable-abd6a00d-c6ae-1f7a-b1b2-d4caaacd79d4\>);
--text-color--text-grey: var(--grey--grey-500);
--_colors-2---bg-color--bg-default<deleted|variable-dc586243-6b41-7a0c-9587-b6ca4843c937>: var(--_colors-2---base--white\<deleted\|variable-44983526-49be-f53c-19b5-8b8d07e2fc58\>);
--new-base---accent-violet: #7c3aed;
--new-base---bg-primary: #0a0a0f;
--new-base---bg-secondary: #0f0f0f;
--new-base---border-default: #ffffff14;
--new-base---border-subtle: #ffffff1f;
--new-base---text-primary: #fff;
--new-base---text-secondary: #ffffff80;
--new-base---accent-indigo: #4f46e5;
--new-base---accent-sky: #0ea5e9;
--new-base---accent-cyan: #06b6d4;
--base-color-neutral--neutral-darker<deleted|variable-dda6ad91-259a-0202-f70f-965feb273058>: #27272a;
--_colors-2---grey--grey-300<deleted|variable-abd6a00d-c6ae-1f7a-b1b2-d4caaacd79d4>: grey;
--_colors-2---base--white<deleted|variable-44983526-49be-f53c-19b5-8b8d07e2fc58>: #fff;
```

### Spacing

```css
--new-base_typography---xs--font-size<deleted|variable-590942ba-b1e0-292d-9ab7-babc67474ac2>: var(--new-base_sizes---fixed--0-75rem\<deleted\|variable-cdba2c83-583b-e8ad-bf49-6066f8d1a3f8\>);
--_typography---base--font-size: var(--_sizes---fixed--medium);
--_sizes---fixed--none: 0rem;
--_typography---h1--font-size: 5rem;
--_typography---h1--letter-spacing: -.04em;
--_typography---h2--font-size: 4rem;
--_typography---h2--letter-spacing: -.04em;
--_typography---h3--font-size: 3.5rem;
--_typography---h3--letter-spacing: 0em;
--_typography---h4--font-size: 3rem;
--_typography---h4--letter-spacing: -.04em;
--_typography---h5--font-size: 2.75rem;
--_typography---h5--letter-spacing: 0em;
--_typography---h6--font-size: var(--_sizes---fixed--xhuge);
--_typography---h6--letter-spacing: -.03em;
--_sizes---fixed--xlarge: 1.5rem;
--_sizes---fixed--xxsmall: .25rem;
--_sizes---fixed--large: 1.25rem;
--_sizes---fixed--medium: 1rem;
--_sizes---fixed--huge: 2rem;
--_typography---2xl--letter-spacing: -.03em;
--_typography---sm--font-size: var(--_sizes---fixed--regular);
--_typography---sm--letter-spacing: .02em;
--_sizes---fixed--3-75rem<deleted|variable-020ac7fb-3de4-afcc-d44f-d83ce96c0339>: 3.75rem;
--_sizes---padding-section--small: 3.75rem;
--_typography---xl--font-size: var(--_sizes---fixed--large);
--_typography---xl--letter-spacing: -.05em;
--_typography---base--letter-spacing: .02em;
--_sizes---fixed--xsmall: .5rem;
--_typography---lg--font-size: 1.125rem;
--_typography---lg--letter-spacing: -.05em;
--_sizes---fixed--xhuge: 2.5rem;
--_sizes---fixed--small: .75rem;
--_sizes---padding-section--large: 7.5rem;
--_typography---2xs--font-size: var(--_sizes---fixed--small);
--_typography---2xs--letter-spacing: -.03em;
--_typography---button--font-size: var(--_sizes---fixed--medium);
--_typography---button--letter-spacing: -.01em;
--_sizes---padding-section--medium: 6.25rem;
--_sizes---fixed--tiny: .125rem;
--_sizes---fixed--xxlarge: 1.75rem;
--_typography---2xl--font-size: var(--_sizes---fixed--xlarge);
--_typography---3xl--font-size: var(--_sizes---fixed--xxlarge);
--_typography---3xl--letter-spacing: 0em;
--_typography---4xl--font-size: var(--_sizes---fixed--huge);
--_typography---4xl--letter-spacing: 0em;
--_typography---5xl--font-size: 2.25rem;
--_typography---5xl--letter-spacing: -.03em;
--_sizes---fixed--0-625rem<deleted|variable-793f1bc2-1f10-d147-d6a2-c10718aa6f22>: .625rem;
--_sizes-2---fixed--2-5rem<deleted|variable-bc4dd7c2-0799-939d-5a0d-1a80ba4ec0c5>: 2.5rem;
--_sizes-2---fixed--2rem<deleted|variable-214f6513-5eea-edd3-ba41-1058412147c6>: 2rem;
--_sizes-2---fixed--1rem<deleted|variable-1c54121d-d5f4-6054-ed1a-4b44e0075228>: 1rem;
--_sizes-2---padding-section--medium<deleted|variable-c2f7b7f5-550e-e7cc-8fe5-30ed1e40168c>: var(--_sizes-2---fixed--5rem\<deleted\|variable-86ce10dd-0070-554a-954e-1db821670347\>);
--_typography---xs--size: .625rem;
--_typography---xs--letter-spacing: .02em;
--_sizes---fixed--regular: .875rem;
--new-base_sizes---fixed--0-75rem<deleted|variable-cdba2c83-583b-e8ad-bf49-6066f8d1a3f8>: .75rem;
--_sizes-2---fixed--5rem<deleted|variable-86ce10dd-0070-554a-954e-1db821670347>: 5rem;
--_sizes-2---fixed--4rem<deleted|variable-56954ee4-0391-fed1-31ee-90886e479a8d>: 4rem;
--_sizes-2---fixed--3rem<deleted|variable-0a5dfaae-b20c-7843-f42a-b77837ece4e6>: 3rem;
```

### Typography

```css
--new-base_typography---font-weight--semibold<deleted|variable-dda78fa4-804c-91c3-7ee6-2d62dfe4690b>: 600;
--_typography---font-family--body: Inter,sans-serif;
--_typography---base--line-height: 1.5;
--_typography---font-weight--regular: 400;
--_typography---h1--font-family: var(--_typography---font-family--headers);
--_typography---h1--line-height: 1.1;
--_typography---h1--font-weight: var(--_typography---font-weight--regular);
--_typography---h2--font-family: var(--_typography---font-family--headers);
--_typography---h2--line-height: 1.1;
--_typography---h2--font-weight: var(--_typography---font-weight--medium);
--_typography---h3--font-family: var(--_typography---font-family--headers);
--_typography---h3--line-height: 1;
--_typography---h3--font-weight: var(--_typography---font-weight--regular);
--_typography---h4--font-family: var(--_typography---font-family--headers);
--_typography---h4--line-height: 1.1;
--_typography---h4--font-weight: var(--_typography---font-weight--medium);
--_typography---h5--font-family: var(--_typography---font-family--headers);
--_typography---h5--line-height: 1.15;
--_typography---h5--font-weight: var(--_typography---font-weight--regular);
--_typography---h6--font-family: var(--_typography---font-family--headers);
--_typography---h6--line-height: 1.2;
--_typography---h6--font-weight: var(--_typography---font-weight--medium);
--_typography---font-weight--semibold: 600;
--_typography---3xl--line-height: 1.5;
--_typography---sm--line-height: 1.42857;
--_typography---sm--font-weight: var(--_typography---font-weight--semibold);
--_typography---font-weight--medium: 500;
--_typography---xl--line-height: 1.4;
--_typography---xl--font-weight: var(--_typography---font-weight--medium);
--_typography---font-weight--light: 300;
--_typography---lg--line-height: 1.4;
--_typography---2xs--line-height: 1.2;
--_typography---button--font-family: var(--_typography---font-family--body);
--_typography---button--line-height: 1.5;
--_typography---button--font-weight: var(--_typography---font-weight--regular);
--_typography---2xl--line-height: 1.2;
--_typography---2xl--font-weight: var(--_typography---font-weight--medium);
--_typography---4xl--line-height: 1.5;
--_typography---5xl--line-height: 1.222;
--_typography---font-weight--bold: 700;
--new-base---text-tertiary: #ffffff4d;
--_typography---xs--line-height: 2;
--_typography---font-weight--thin: 100;
--_typography---font-weight--extra-light: 200;
--_typography---font-weight--extra-bold: 800;
--_typography---font-weight--black: 900;
--_typography---font-family--headers: Inter,sans-serif;
```

### Other

```css
--new-base---base--black<deleted|variable-5d35bd76-5bb1-d212-3539-17e3067bcbaa>: #1d1d1d;
--base--yellow: #efd556;
--base--white: #fff;
--grey--grey-100: #f0efed;
--new-base---black: #050505;
--new-base---white: #fff;
--base--black: black;
--grey--grey-200: #bababa;
--grey--grey-300: grey;
--grey--grey-400: #656565;
--grey--grey-500: #3a3a3a;
--grey--grey-600: #292929;
--grey--grey-700: #171717;
--grey--grey-800: #131313;
--grey--grey-900: #0a0a0a;
--base--grey-light<deleted|variable-e77efb59-b29d-151a-6f0f-bfc9f2744592>: #eeecea;
```

### Dependencies

```css
--new-base_typography---xs--font-size<deleted|variable-590942ba-b1e0-292d-9ab7-babc67474ac2>: --new-base_sizes---fixed--0-75rem;
--bg-color--bg-default: --base--white;
--text-color--text-primary: --base--black;
--_typography---base--font-size: --_sizes---fixed--medium;
--_typography---h1--font-family: --_typography---font-family--headers;
--_typography---h1--font-weight: --_typography---font-weight--regular;
--_typography---h2--font-family: --_typography---font-family--headers;
--_typography---h2--font-weight: --_typography---font-weight--medium;
--_typography---h3--font-family: --_typography---font-family--headers;
--_typography---h3--font-weight: --_typography---font-weight--regular;
--_typography---h4--font-family: --_typography---font-family--headers;
--_typography---h4--font-weight: --_typography---font-weight--medium;
--_typography---h5--font-family: --_typography---font-family--headers;
--_typography---h5--font-weight: --_typography---font-weight--regular;
--_typography---h6--font-family: --_typography---font-family--headers;
--_typography---h6--font-size: --_sizes---fixed--xhuge;
--_typography---h6--font-weight: --_typography---font-weight--medium;
--bg-color--bg-accent: --base--yellow;
--bg-color--bg-secondary: --base--black;
--_sizes---border-radius--small: --_sizes---fixed--xlarge;
--bg-color--bg-subtle: --grey--grey-100;
--bg-color--bg-primary: --base--white;
--text-color--text-secondary: --grey--grey-400;
--_typography---sm--font-size: --_sizes---fixed--regular;
--_typography---sm--font-weight: --_typography---font-weight--semibold;
--text-color--text-accent: --base--yellow;
--_typography---xl--font-size: --_sizes---fixed--large;
--_typography---xl--font-weight: --_typography---font-weight--medium;
--_typography---2xs--font-size: --_sizes---fixed--small;
--_sizes---border-radius--medium: --_sizes---fixed--xhuge;
--_typography---button--font-family: --_typography---font-family--body;
--_typography---button--font-size: --_sizes---fixed--medium;
--_typography---button--font-weight: --_typography---font-weight--regular;
--text-color--text-on-primary: --base--white;
--border-color--border-alternate<deleted|variable-551aa6d2-4bf8-6036-137a-78e1c71841a4>: --base-color-neutral--neutral-darker;
--_typography---2xl--font-size: --_sizes---fixed--xlarge;
--_typography---2xl--font-weight: --_typography---font-weight--medium;
--_typography---3xl--font-size: --_sizes---fixed--xxlarge;
--_typography---4xl--font-size: --_sizes---fixed--huge;
--bg-color--bg-button: --grey--grey-800;
--bg-color--bg-hover<deleted|variable-07249897-f71c-dd53-6216-4b6845d3f64e>: --base--grey-light;
--text-color--text-tertiary: --grey--grey-200;
--_colors-2---bg-color--bg-secondary<deleted|variable-cdd04b90-31c4-c33e-cf74-59e4718ac2ba>: --_colors-2---grey--grey-300;
--text-color--text-grey: --grey--grey-500;
--_colors-2---bg-color--bg-default<deleted|variable-dc586243-6b41-7a0c-9587-b6ca4843c937>: --_colors-2---base--white;
--_sizes-2---padding-section--medium<deleted|variable-c2f7b7f5-550e-e7cc-8fe5-30ed1e40168c>: --_sizes-2---fixed--5rem;
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

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.2s`, `0.1s`

### Common Transitions

```css
transition: all;
transition: 0.3s ease-in-out;
transition: opacity 0.3s;
transition: transform 0.2s;
transition: transform 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
transition: background-color 0.1s, color 0.1s;
transition: transform 0.2s, background-color 0.2s;
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

### Buttons (21 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
  padding-top: 8px;
  padding-right: 8px;
  border-radius: 40px;
}
```

### Cards (27 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 14px 32px 0px, rgba(0, 0, 0, 0.09) 0px 58px 58px 0px, rgba(0, 0, 0, 0.05) 0px 130px 78px 0px, rgba(0, 0, 0, 0.01) 0px 232px 93px 0px, rgba(0, 0, 0, 0) 0px 362px 101px 0px;
  padding-top: 16px;
  padding-right: 0px;
}
```

### Links (52 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (39 instances)

```css
.navigatio {
  background-color: rgb(41, 45, 50);
  color: rgb(255, 255, 255);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (20 instances)

```css
.foote {
  background-color: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding-top: 12px;
  padding-bottom: 12px;
  font-size: 16px;
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

### Dropdowns (21 instances)

```css
.dropdown {
  background-color: rgb(239, 238, 235);
  border-radius: 0px;
  border-color: rgb(255, 255, 255);
  padding-top: 0px;
}
```

### Badges (7 instances)

```css
.badge {
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Tabs (10 instances)

```css
.tab {
  background-color: rgb(0, 0, 0);
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(0, 0, 0);
  border-radius: 0px;
}
```

### Switches (2 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(255, 255, 255);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 10 instances, 2 variants

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

**Variant 2** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 6 instances, 2 variants

**Variant 1** (4 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 12px 20px 12px 20px;
  border-radius: 40px;
  border: 1px solid rgba(255, 255, 255, 0.16);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 8px 8px 8px 24px;
  border-radius: 40px;
  border: 1px solid rgba(255, 255, 255, 0.16);
  font-size: 16px;
  font-weight: 400;
```

### Button — 5 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgb(19, 19, 19);
  color: rgb(239, 213, 86);
  padding: 0px 0px 0px 0px;
  border-radius: 40px;
  border: 0px none rgb(239, 213, 86);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgb(239, 213, 86);
  color: rgb(239, 213, 86);
  padding: 0px 0px 0px 0px;
  border-radius: 40px;
  border: 0px none rgb(239, 213, 86);
  font-size: 16px;
  font-weight: 400;
```

### Card — 7 instances, 1 variant

**Variant 1** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 60px 0px 240px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (3 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 32px 0px 32px 0px;
  border-radius: 12px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 6 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 16px 16px 16px 16px;
  border-radius: 24px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 8px 8px 8px 8px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 298.109px 0px 0px 0px;
  border-radius: 12px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Link — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 16px 16px 16px 16px;
  border-radius: 24px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 12px 12px 12px 12px;
  border-radius: 12px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 8px 12px 8px 12px;
  border-radius: 4px;
  border: 1px solid rgb(102, 102, 102);
  font-size: 16px;
  font-weight: 600;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(235, 242, 19);
  color: rgb(0, 0, 0);
  padding: 8px 12px 8px 12px;
  border-radius: 4px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 600;
```

## Layout System

**10 grid containers** and **155 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1320px | 0px |
| 100% | 0px |
| 800px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 4x |
| 2-column | 4x |
| 4-column | 1x |
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 381.328px 762.672px;
gap: 16px;
grid-template-columns: 381.328px 762.672px;
gap: 16px;
grid-template-columns: 381.328px 762.672px;
gap: 16px;
grid-template-columns: 580px 580px;
grid-template-columns: 272px 272px 272px 272px;
gap: 24px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 72x |
| column/nowrap | 83x |

**Gap values:** `10px`, `12px`, `16px`, `16px normal`, `17.92px`, `2.4px`, `20px`, `24px`, `32px`, `40px`, `44.8px`, `45.92px`, `4px`, `64px`, `6px`, `72px`, `8px`, `8px normal`, `9.92px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 90/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 92/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 84 !important rules — prefer specificity over overrides
- 80% of CSS is unused — consider purging
- 3690 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| radial | circle | 2 | brand |
| linear | — | 2 | brand |

```css
background: radial-gradient(circle, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.8));
background: linear-gradient(rgba(0, 0, 0, 0), rgb(0, 0, 0));
```

## Z-Index Map

**11 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,1000 | div.n.a.v.b.a.r. .w.-.n.a.v |
| dropdown | 900,999 | div.n.a.v._.d.r.o.p.d.o.w.n. .w.-.d.r.o.p.d.o.w.n, div.n.e.w.-.b.a.s.e.-.-.t.-.t.e.m.l.i.s.-.c.o.m.p.o.n.e.n.t |
| sticky | 10,15 | div.h.e.r.o._.s.t.i.c.k.y, div.h.e.r.o._.i.m.g.-.o.v.e.r.l.a.y |
| base | 0,5 | div.h.e.r.o._.t.i.t.l.e, div.s.e.r.v.i.c.e._.i.m.g.-.w.r.a.p, div.s.e.r.v.i.c.e._.i.m.g.-.w.r.a.p |

## SVG Icons

**4 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 1 |
| md | 3 |

**Icon colors:** `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| Inter | google-fonts | 300, 400, 500, 600, 700 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 12 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 9 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 4 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (11x), 3:2 (6x), 3.5:1 (2x), 3.39:1 (1x), 16:9 (1x), 3:4 (1x), 3.38:1 (1x), 3:1 (1x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

### Easing Families

- **ease-in-out** (5 uses) — `ease`
- **ease-out** (2 uses) — `cubic-bezier(0.25, 0.46, 0.45, 0.94)`

## Component Anatomy

### button — 24 instances

**Slots:** label, icon
**Variants:** secondary

| variant | count | sample label |
|---|---|---|
| default | 23 | Contact us |
| secondary | 1 | Join our AI community |

### card — 21 instances

**Slots:** media

### link — 6 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **learn** (18)
- **contact** (2)
- **get** (2)
- **join** (2)
- **see** (1)

### Button Copy Patterns

- "learn more" (12×)
- "contact us" (2×)
- "get started" (2×)
- "october 4, 2024
the green space revolution: is the 'living building' the future of cities?
learn more" (1×)
- "october 4, 2024
form meets function: why good design starts with purpose
learn more" (1×)
- "october 4, 2024
5 ways functional design can add value to your home
learn more" (1×)
- "october 4, 2024
designing for real life: the rise of practical minimalism
learn more" (1×)
- "october 4, 2024
functional interiors: the secret behind effortless living
learn more" (1×)
- "october 4, 2024
from studio to family home: flexible spaces that grow with you
learn more" (1×)
- "join our ai community
see all templates" (1×)

### Sample Headings

> Your gateway to prestige properties
> Experience innovative architecture that transforms your vision
> We deliver exceptional real estate solutions.
> Seamless property solutions tailored for you.
> With a commitment to excellence and customer satisfaction.
> Your gateway to prestige properties
> Experience innovative architecture that transforms your vision
> We deliver exceptional real estate solutions.
> Seamless property solutions tailored for you.
> With a commitment to excellence and customer satisfaction.

## Page Intent

**Type:** `landing` (confidence 0.75)
**Description:** Vistal is a modern Webflow template. Customize it to match your brand and create a unique, professional experience in minutes.

## Section Roles

Reading order (top→bottom): nav → nav → feature-grid → hero → nav → content → cta → cta → cta → testimonials → feature-grid → faq → cta

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | feature-grid | Your gateway to prestige properties | 0.8 |
| 4 | hero | Your gateway to prestige properties | 0.85 |
| 5 | cta | Experience innovative architecture that transforms your vision | 0.75 |
| 6 | cta | We deliver exceptional real estate solutions. | 0.75 |
| 7 | cta | Seamless property solutions tailored for you. | 0.75 |
| 8 | testimonials | With a commitment to excellence and customer satisfaction. | 0.4 |
| 9 | feature-grid | Our feature blogs | 0.8 |
| 10 | faq | — | 0.85 |
| 11 | cta | Schedule a free consultation | 0.75 |
| 12 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.234 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.207)
**Counts:** total 25, svg 9, icon 9, screenshot-like 0, photo-like 10
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.326)

Evidence:
- tailwind-like class density 37%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
