# Design Language: What Matters Agency

> Extracted from `https://www.whatmattersagency.com` on September 4, 2026
> 1160 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fef073` | rgb(254, 240, 115) | hsl(54, 99%, 72%) | 7 |
| Secondary | `#ffa23c` | rgb(255, 162, 60) | hsl(31, 100%, 62%) | 1 |
| Accent | `#5a92e7` | rgb(90, 146, 231) | hsl(216, 75%, 63%) | 4 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#050505` | hsl(0, 0%, 2%) | 2095 |
| `#ffffff` | hsl(0, 0%, 100%) | 249 |
| `#6c6b6a` | hsl(30, 1%, 42%) | 18 |
| `#312821` | hsl(26, 20%, 16%) | 2 |
| `#f7f7f1` | hsl(60, 27%, 96%) | 2 |

### Background Colors

Used on large-area elements: `#ffffff`, `#fef073`, `#312821`, `#000000`, `#69b16a`, `#050505`, `#ffa23c`, `#f7f7f1`, `#ecc8eb`, `#5a92e7`, `#302f2c`

### Text Colors

Text color palette: `#000000`, `#050505`, `#ffffff`, `#6c6b6a`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#050505` | text, border, background | 2095 |
| `#ffffff` | background, text, border | 249 |
| `#6c6b6a` | text, border | 18 |
| `#fef073` | background | 7 |
| `#5a92e7` | background | 4 |
| `#69b16a` | background | 3 |
| `#312821` | background | 2 |
| `#f7f7f1` | background | 2 |
| `#ecc8eb` | background | 2 |
| `#ffa23c` | background | 1 |

## Typography

### Font Families

- **Inter** — used for body (477 elements)
- **Neue Haas Display** — used for all (338 elements)
- **Denim Ink** — used for all (317 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 135.434px | 8.4646rem | 500 | 111.056px | -2.70867px | h1, div, br, span |
| 98px | 6.125rem | 500 | 80.36px | -1.96px | h1, div, br |
| 97.7152px | 6.1072rem | 400 | 97.7152px | -0.157152px | div |
| 71.4336px | 4.4646rem | 500 | 58.5756px | -0.714336px | h2, span, h3, div |
| 57.2768px | 3.5798rem | 500 | 57.2768px | -0.572768px | h1, span |
| 40px | 2.5rem | 500 | 42px | -1px | h3, div, span, h2 |
| 30px | 1.875rem | 500 | 30px | -0.3px | h2, div, h4, span |
| 24px | 1.5rem | 400 | 32.4px | -0.157152px | div |
| 23.1488px | 1.4468rem | 500 | 25.4637px | normal | p, h2 |
| 20.5728px | 1.2858rem | 500 | 20.5728px | -0.205728px | span |
| 19.7152px | 1.2322rem | 400 | 26.6155px | -0.157152px | div, svg, path, p |
| 17.7152px | 1.1072rem | 500 | 17.7152px | -0.177152px | h2, p, a, div |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 15.7152px | 0.9822rem | 400 | 21.2155px | -0.157152px | body, div, style, a |
| 15.1424px | 0.9464rem | 400 | 20.4422px | -0.157152px | div, h2, p, br |

### Heading Scale

```css
h1 { font-size: 135.434px; font-weight: 500; line-height: 111.056px; }
h1 { font-size: 98px; font-weight: 500; line-height: 80.36px; }
h2 { font-size: 71.4336px; font-weight: 500; line-height: 58.5756px; }
h1 { font-size: 57.2768px; font-weight: 500; line-height: 57.2768px; }
h3 { font-size: 40px; font-weight: 500; line-height: 42px; }
h2 { font-size: 30px; font-weight: 500; line-height: 30px; }
h2 { font-size: 23.1488px; font-weight: 500; line-height: 25.4637px; }
h6 { font-size: 19.7152px; font-weight: 400; line-height: 26.6155px; }
h2 { font-size: 17.7152px; font-weight: 500; line-height: 17.7152px; }
h2 { font-size: 15.1424px; font-weight: 400; line-height: 20.4422px; }
```

### Body Text

```css
body { font-size: 30px; font-weight: 500; line-height: 30px; }
```

### Font Weights in Use

`500` (655x), `400` (495x), `600` (10x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-12 | 12px | 0.75rem |
| spacing-14 | 14px | 0.875rem |
| spacing-24 | 24px | 1.5rem |
| spacing-27 | 27px | 1.6875rem |
| spacing-31 | 31px | 1.9375rem |
| spacing-35 | 35px | 2.1875rem |
| spacing-39 | 39px | 2.4375rem |
| spacing-63 | 63px | 3.9375rem |
| spacing-67 | 67px | 4.1875rem |
| spacing-70 | 70px | 4.375rem |
| spacing-72 | 72px | 4.5rem |
| spacing-75 | 75px | 4.6875rem |
| spacing-93 | 93px | 5.8125rem |
| spacing-122 | 122px | 7.625rem |
| spacing-180 | 180px | 11.25rem |
| spacing-370 | 370px | 23.125rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 4 |
| full | 800px | 19 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgb(5, 5, 5) 0px 3.6808px 0px 0px;
```

## CSS Custom Properties

### Colors

```css
--_color---nav--color: var(--_color---nav--light);
--colors--text: var(--_color---neutral--black);
--colors--primary-accent: var(--_color---primary--yellow);
--_typography---fonts--primary-font: "Neue Haas Display", Arial, sans-serif;
--colors--background: var(--_color---neutral--white);
--_color---neutral--light-gray: #dfddd6;
--_color---neutral--black: #050505;
--_color---neutral--dark-gray: #302f2c;
--_color---neutral--white: white;
--_color---primary--yellow: #fef073;
--_components---card--padding: clamp(var(--_components---card--padding-min-rem) * 1rem, ((var(--_components---card--padding-min-rem)  - ((var(--_components---card--padding-max-rem)  - var(--_components---card--padding-min-rem)) / (var(--_layout---fluid--max)  - var(--_layout---fluid--min)) * var(--_layout---fluid--min))) * 1rem + ((var(--_components---card--padding-max-rem)  - var(--_components---card--padding-min-rem)) / (var(--_layout---fluid--max)  - var(--_layout---fluid--min))) * 100vw), var(--_components---card--padding-max-rem) * 1rem);
--_color---neutral--mid-gray: #6c6b6a;
--_components---input--border-radius: .5rem;
--colors--border: var(--_color---neutral--black);
--_components---card--border-radius: .5rem;
--_responsive---padding--card<deleted|variable-5fcf010a-6fe9-5ba2-24fb-53a12ac0d5b0>: 1.5rem;
--_components---card--card-body-padding-sm<deleted|variable-886aa6f6-843b-26b9-170b-96cc08ca36e2>: 20px;
--_color---neutral--transparent: #fff0;
--_components---button--border-radius: 50rem;
--_color---secondary--blue: #5a92e7;
--_color---secondary--green: #69b16a;
--_color---secondary--pink: #ecc8eb;
--_color---secondary--orange: #ffa32c;
--_color---secondary--beige: #f7f7f1;
--_color---secondary--brown: #312821;
--_typography---fonts--secondary-font: "Denim Ink", Arial, sans-serif;
--_components---card--padding-min-rem: 1;
--_components---card--padding-max-rem: 1.5;
--_color---nav--light: white;
--_color---nav--dark: #050505;
```

### Spacing

```css
--_typography---paragraph-body--font-size: clamp(.875rem, .839rem + .179vw, 100vw);
--_typography---paragraph-body--letter-spacing: -.01em;
--_typography---h1--bottom-margin: .075em;
--_typography---h1--font-size: clamp(3.75rem, 2.179rem + 7.857vw, 100vw);
--_typography---h1--letter-spacing: -.02em;
--_typography---h2--bottom-margin: .2em;
--_typography---h2--font-size: clamp(2.75rem, 2.179rem + 2.857vw, 100vw);
--_typography---h2--letter-spacing: -.01em;
--_typography---h3--bottom-margin: .3em;
--_typography---h3--font-size: clamp(2.563rem, 2.223rem + 1.696vw, 100vw);
--_typography---h3--letter-spacing: -.01em;
--_typography---h4--bottom-margin: .6em;
--_typography---h4--font-size: clamp(1.75rem, 1.5rem + 1.25vw, 100vw);
--_typography---h4--letter-spacing: -.025em;
--_typography---h5--bottom-margin: .5em;
--_typography---h5--font-size: clamp(1.125rem, .875rem + 1.25vw, 100vw);
--_typography---h5--letter-spacing: -.01em;
--_typography---h6--bottom-margin: .4em;
--_typography---h6--font-size: clamp(1.125rem, 1.018rem + .536vw, 100vw);
--_typography---h6--letter-spacing: 0em;
--_typography---paragraph-body--bottom-margin: 1em;
--_components---section--padding-md: clamp(4.5rem, 4.071rem + 2.143vw, 100vw);
--_components---section--padding-lg: clamp(5.5rem, 4.786rem + 3.571vw, 100vw);
--_components---section--padding-sm: clamp(2.5rem, 1.929rem + 2.857vw, 100vw);
--_layout---grid--gap-main: 48px;
--_size---0rem: 0rem;
--_layout---grid--gap-md: 24px;
--_layout---grid--gap-xs: 8px;
--_layout---grid--gap-button: 16px;
--_layout---grid--gap-xl: 64px;
--_components---input--bottom-margin: 1rem;
--_components---input--font-size: 1rem;
--_components---input--letter-spacing: 0em;
--_components---input-label--font-size: .9rem;
--_components---input-label--letter-spacing: 0em;
--_typography---eyebrow-lg--bottom-margin: 1.4em;
--_typography---eyebrow-lg--font-size: clamp(1rem, .964rem + .179vw, 100vw);
--_typography---eyebrow-sm--letter-spacing: -.01em;
--_typography---paragraph-sm--bottom-margin: 1em;
--_typography---paragraph-sm--font-size: clamp(.781rem, .754rem + .134vw, .875rem);
--_typography---paragraph-sm--letter-spacing: -.015em;
--_typography---paragraph-lg--bottom-margin: 1em;
--_typography---paragraph-lg--font-size: clamp(1rem, .964rem + .179vw, 100vw);
--_typography---paragraph-lg--letter-spacing: -.02em;
--_typography---paragraph-xl--bottom-margin: 1em;
--_typography---paragraph-xl--font-size: clamp(1.125rem, 1.089rem + .179vw, 100vw);
--_typography---paragraph-xl--letter-spacing: -.01em;
--_layout---spacing--margin-md: 2em;
--_layout---spacing--margin-lg: 3em;
--_layout---spacing--margin-sm: 1em;
--_layout---spacing--margin-xs: .5em;
--_size---1-5rem: 1.5rem;
--_size---2rem: 2rem;
--_size---3rem: 3rem;
--_size---0-75rem: .75rem;
--_layout---grid--gap-sm: 16px;
--_typography---eyebrow-sm--font-size: clamp(.813rem, .768rem + .223vw, 100vw);
--_components---button--vertical-padding-s: clamp(.5rem, .464rem + .179vw, 100vw);
--_components---button--horizontal-padding-s: clamp(.875rem, .839rem + .179vw, 100vw);
--_components---button--font-size: clamp(.813rem, .777rem + .179vw, 100vw);
--_components---button--letter-spacing: -.015em;
--_components---button--vertical-padding-l: clamp(.875rem, .839rem + .179vw, 100vw);
--_components---button--horizontal-padding-l: clamp(1.313rem, 1.188rem + .625vw, 100vw);
--_components---section--padding-min-rem: 3;
--_components---section--padding-max-rem: 6;
--_typography---h1--font-size-min-rem: 4;
--_typography---h1--font-size-max-rem: 10.8;
--_typography---h2--font-size-min-rem: 3;
--_typography---h2--font-size-max-rem: 6;
--_typography---h3--font-size-min-rem: 2.5;
--_typography---h3--font-size-max-rem: 4.375;
--_typography---h4--font-size-min-rem: 2;
--_typography---h4--font-size-max-rem: 2.75;
--_typography---h5--font-size-min-rem: 1.25;
--_typography---h5--font-size-max-rem: 2.275;
--_typography---h6--font-size-min-rem: .8;
--_typography---h6--font-size-max-rem: 1.25;
--_typography---paragraph-xl--font-size-min-rem: 1.175;
--_typography---paragraph-xl--font-size-max-rem: 1.4;
--_typography---paragraph-lg--font-size-min-rem: 1.03125;
--_typography---paragraph-lg--font-size-max-rem: 1.1875;
--_typography---paragraph-body--font-size-min-rem: .875;
--_typography---paragraph-body--font-size-max-rem: 1.0625;
--_typography---paragraph-sm--font-size-min-rem: .8;
--_typography---paragraph-sm--font-size-max-rem: .9;
--_size---spacing-utility-em--0-5em: .5em;
--_size---spacing-utility-em--1em: 1em;
--_size---spacing-utility-em--2em: 2em;
--_size---spacing-utility-em--3em: 3em;
--_typography---eyebrow-lg--font-size-min-rem: 1;
--_typography---eyebrow-lg--font-size-max-rem: 1.1875;
--_typography---eyebrow-lg--letter-spacing: .1em;
--_typography---eyebrow-sm--font-size-min-rem: .75;
--_typography---eyebrow-sm--font-size-max-rem: .9375;
--_typography---eyebrow-sm--bottom-margin: 1em;
--_size---0-125rem: .125rem;
--_size---0-25rem: .25rem;
--_size---0-5rem: .5rem;
--_size---1rem: 1rem;
--_size---1-25rem: 1.25rem;
--_size---2-5rem: 2.5rem;
--_size---3-5rem: 3.5rem;
--_size---4rem: 4rem;
--_size---4-5rem: 4.5rem;
--_size---5-5rem: 5.5rem;
--_size---6rem: 6rem;
--_size---6-5rem: 6.5rem;
--_size---7rem: 7rem;
--_size---7-5rem: 7.5rem;
--_size---8rem: 8rem;
--_size---8-5rem: 8.5rem;
--_size---9rem: 9rem;
--_size---9-5rem: 9.5rem;
--_size---10rem: 10rem;
--_size---11rem: 11rem;
--_size---12rem: 12rem;
--_size---sizes--size: 0px;
```

### Typography

```css
--_typography---paragraph-body--font: var(--_typography---fonts--tertiary-font);
--_typography---paragraph-body--line-height: 1.35;
--_typography---paragraph-body--font-weight: 400;
--_typography---h1--font: var(--_typography---fonts--primary-font);
--_typography---h1--line-height: .82;
--_typography---h1--font-weight: 500;
--_typography---h2--font: var(--_typography---fonts--primary-font);
--_typography---h2--line-height: .82;
--_typography---h2--font-weight: 500;
--_typography---h3--font: var(--_typography---fonts--primary-font);
--_typography---h3--line-height: 1;
--_typography---h3--font-weight: 500;
--_typography---h4--font: var(--_typography---fonts--secondary-font);
--_typography---h4--line-height: 1.05;
--_typography---h4--font-weight: 500;
--_typography---h5--font: var(--_typography---fonts--secondary-font);
--_typography---h5--line-height: 1;
--_typography---h5--font-weight: 500;
--_typography---h6--font: var(--_typography---fonts--secondary-font);
--_typography---h6--line-height: 1.1;
--_typography---h6--font-weight: 500;
--_components---input--font: var(--_typography---fonts--primary-font);
--_components---input--line-height: 1.5em;
--_components---input--font-weight: 400;
--_components---input-label--font: var(--_typography---fonts--primary-font);
--_components---input-label--line-height: 1em;
--_components---input-label--font-weight: 500;
--_typography---eyebrow-lg--font: var(--_typography---fonts--primary-font);
--_typography---eyebrow-lg--line-height: 1;
--_typography---eyebrow-lg--font-weight: 500;
--_typography---paragraph-sm--font: var(--_typography---fonts--tertiary-font);
--_typography---paragraph-sm--line-height: 1.3;
--_typography---paragraph-sm--font-weight: 0;
--_typography---paragraph-lg--font: var(--_typography---fonts--tertiary-font);
--_typography---paragraph-lg--line-height: 1.3;
--_typography---paragraph-lg--font-weight: 400;
--_typography---paragraph-xl--font: var(--_typography---fonts--secondary-font);
--_typography---paragraph-xl--line-height: 1.2;
--_typography---paragraph-xl--font-weight: 500;
--_typography---eyebrow-sm--font: var(--_typography---fonts--secondary-font);
--_typography---eyebrow-sm--line-height: 1.2;
--_components---button--font: var(--_typography---fonts--secondary-font);
--_components---button--line-height: 1.3em;
--_components---button--font-weight: 500;
--_typography---button--font<deleted|variable-14482639-7a2f-c2b8-9d91-63e2f5329682>: var(--_typography---fonts--secondary-font);
--_typography---fonts--tertiary-font: Inter, Arial, sans-serif;
--_typography---eyebrow-sm--font-weight: 500;
```

### Other

```css
--_layout---fluid--max: 120;
--_layout---fluid--min: 20;
--_components---container--max-width: calc(var(--_layout---fluid--max) * 1rem);
--basic-ease: cubic-bezier(.625,.5,0,1);
```

### Dependencies

```css
--_color---nav--color: --_color---nav--light;
--_typography---paragraph-body--font: --_typography---fonts--tertiary-font;
--colors--text: --_color---neutral--black;
--_typography---h1--font: --_typography---fonts--primary-font;
--_typography---h2--font: --_typography---fonts--primary-font;
--_typography---h3--font: --_typography---fonts--primary-font;
--_typography---h4--font: --_typography---fonts--secondary-font;
--_typography---h5--font: --_typography---fonts--secondary-font;
--_typography---h6--font: --_typography---fonts--secondary-font;
--colors--primary-accent: --_color---primary--yellow;
--colors--background: --_color---neutral--white;
--_components---card--padding: --_components---card--padding-min-rem,--_components---card--padding-min-rem,--_components---card--padding-max-rem,--_components---card--padding-min-rem,--_layout---fluid--max,--_layout---fluid--min,--_layout---fluid--min,--_components---card--padding-max-rem,--_components---card--padding-min-rem,--_layout---fluid--max,--_layout---fluid--min,--_components---card--padding-max-rem;
--_components---input--font: --_typography---fonts--primary-font;
--_components---input-label--font: --_typography---fonts--primary-font;
--_typography---eyebrow-lg--font: --_typography---fonts--primary-font;
--_typography---paragraph-sm--font: --_typography---fonts--tertiary-font;
--_typography---paragraph-lg--font: --_typography---fonts--tertiary-font;
--_typography---paragraph-xl--font: --_typography---fonts--secondary-font;
--colors--border: --_color---neutral--black;
--_typography---eyebrow-sm--font: --_typography---fonts--secondary-font;
--_components---button--font: --_typography---fonts--secondary-font;
--_typography---button--font<deleted|variable-14482639-7a2f-c2b8-9d91-63e2f5329682>: --_typography---fonts--secondary-font;
--_components---container--max-width: --_layout---fluid--max;
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
| 560px | 560px | max-width |
| sm | 600px | max-width |
| md | 767px | max-width |
| md | 768px | max-width |
| lg | 991px | max-width |
| lg | 992px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.5s`, `0.02s`, `0.04s`, `0.06s`, `0.08s`, `0.1s`, `0.12s`, `0.14s`, `0.4s`, `0.15s`, `0.25s`, `0.16s`, `0.18s`, `0.2s`, `0.22s`, `0.24s`, `0.26s`, `0.6s`, `0.28s`, `0.32s`, `0.34s`, `0.36s`, `0.38s`, `0.42s`, `0.44s`

### Common Transitions

```css
transition: all;
transition: color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
transition: transform 0.5s cubic-bezier(0.625, 0.05, 0, 1);
transition: transform 0.5s cubic-bezier(0.625, 0.05, 0, 1) 0.02s;
transition: transform 0.5s cubic-bezier(0.625, 0.05, 0, 1) 0.04s;
transition: transform 0.5s cubic-bezier(0.625, 0.05, 0, 1) 0.06s;
transition: transform 0.5s cubic-bezier(0.625, 0.05, 0, 1) 0.08s;
transition: transform 0.5s cubic-bezier(0.625, 0.05, 0, 1) 0.1s;
transition: transform 0.5s cubic-bezier(0.625, 0.05, 0, 1) 0.12s;
transition: transform 0.5s cubic-bezier(0.625, 0.05, 0, 1) 0.14s;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**translateXCursor**
```css
@keyframes translateXCursor {
  100% { transform: translateX(-100%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (9 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(5, 5, 5);
  font-size: 14.7232px;
  font-weight: 500;
  padding-top: 15.7152px;
  padding-right: 27.008px;
  border-radius: 800px;
}
```

### Cards (54 instances)

```css
.card {
  background-color: rgb(5, 5, 5);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (37 instances)

```css
.link {
  color: rgb(5, 5, 5);
  font-size: 14.7232px;
  font-weight: 400;
}
```

### Navigation (32 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(5, 5, 5);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
  box-shadow: rgb(5, 5, 5) 0px 3.6808px 0px 0px;
}
```

### Footer (48 instances)

```css
.foote {
  background-color: rgb(254, 240, 115);
  color: rgb(5, 5, 5);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 15.7152px;
}
```

### Modals (2 instances)

```css
.modal {
  background-color: rgb(48, 47, 44);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (34 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(5, 5, 5);
  padding-top: 0px;
}
```

### ProgressBars (1 instances)

```css
.progressBar {
  background-color: rgb(5, 5, 5);
  color: rgb(5, 5, 5);
  border-radius: 0px;
  font-size: 15.7152px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(5, 5, 5);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(5, 5, 5);
  font-size: 13.7152px;
  font-weight: 500;
```

### Link — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(5, 5, 5);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(5, 5, 5);
  font-size: 15.7152px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(105, 177, 106);
  color: rgb(5, 5, 5);
  padding: 0px 0px 0px 0px;
  border-radius: 1.9644px;
  border: 0px none rgb(5, 5, 5);
  font-size: 15.7152px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(5, 5, 5);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(5, 5, 5);
  font-size: 15.7152px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(5, 5, 5);
  color: rgb(5, 5, 5);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(5, 5, 5);
  font-size: 15.7152px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(5, 5, 5);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(5, 5, 5);
  font-size: 15.7152px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(5, 5, 5);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(5, 5, 5);
  font-size: 15.7152px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(5, 5, 5);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(5, 5, 5);
  font-size: 15.7152px;
  font-weight: 400;
```

### Card — 10 instances, 1 variant

**Variant 1** (10 instances)

```css
  background: rgb(105, 177, 106);
  color: rgb(5, 5, 5);
  padding: 31.4304px 23.5728px 31.4304px 23.5728px;
  border-radius: 0px;
  border: 0px none rgb(5, 5, 5);
  font-size: 15.7152px;
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
  font-size: 15.7152px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **155 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 66.6667% | 24px |
| 75% | 24px |
| 58.3333% | 24px |
| 1216px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 6-column | 1x |

### Grid Templates

```css
grid-template-columns: 86.125px 86.1406px 86.125px 86.1406px 86.125px 86.1406px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 58x |
| row/nowrap | 85x |
| row/wrap | 12x |

**Gap values:** `12px`, `15.7152px normal`, `16px`, `19.644px`, `19.7152px 78.8608px`, `2.2144px`, `24px normal`, `32px`, `35.3592px`, `4.71456px`, `48px normal`, `6.28608px`, `8px`, `8px normal`, `9.08544px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 86/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 70/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 62 !important rules — prefer specificity over overrides
- 74% of CSS is unused — consider purging
- 2341 duplicate CSS declarations

## Z-Index Map

**6 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,999 | div.c.u.r.s.o.r.-.m.a.r.q.u.e.e, div.n.a.v. .w.-.n.a.v |
| base | 0,9 | div.l.o.a.d.e.r._.s.c.r.e.e.n, div.h.o.m.e.-.v.e.r.t.i.c.a.l.-.v.i.d.e.o._.w.r.a.p, span.n.a.v.-.l.i.n.k |

## SVG Icons

**8 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| md | 1 |
| xl | 7 |

**Icon colors:** `currentColor`, `fffffff`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | normal | normal |
| Inter | self-hosted | 400, 500, 600 | normal |
| Denim Ink | self-hosted | 500 | normal |
| Neue Haas Display | self-hosted | 500 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 4 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 3 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 16:9 (6x), 3:4 (2x), 3:2 (1x), 21:9 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `20ms` | 20 |
| `xs` | `100ms` | 100 |
| `sm` | `160ms` | 160 |
| `md` | `260ms` | 260 |
| `lg` | `420ms` | 420 |

### Easing Families

- **ease-out** (9 uses) — `cubic-bezier(0.165, 0.84, 0.44, 1)`
- **custom** (275 uses) — `cubic-bezier(0.625, 0.05, 0, 1)`, `cubic-bezier(0.75, 0, 0.25, 1)`, `cubic-bezier(0.625, 0.5, 0, 1)`
- **ease-in-out** (6 uses) — `ease`
- **linear** (14 uses) — `linear`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `translateXCursor` | slide-x | transform | 2 |

## Component Anatomy

### card — 31 instances

**Slots:** description

### link — 4 instances


### button — 2 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **sydney** (2)
- **house** (1)
- **solotel** (1)
- **view** (1)
- **get** (1)

### Button Copy Patterns

- "sydney fish market

lo-fi social shoots, paid media

(01)" (1×)
- "sydney restaurant group

lo-fi social shoots, paid media, social media management

(02)" (1×)
- "house made hospitality

lo-fi social shoots, paid media, social media management

(03)" (1×)
- "solotel

lo-fi social shoots, photography, talent

(04)" (1×)
- "view some work" (1×)
- "get in touch
say hi" (1×)

### Sample Headings

> CONTENT +
SOCIAL MEDIA +
PAID MEDIA
> CONTENT +
SOCIAL MEDIA +
PAID MEDIA
> CONTENT +
SOCIAL MEDIA +
PAID MEDIA
> WHAT
MATTERS

> (AGENCY)
> CONTENT +
SOCIAL MEDIA +
PAID MEDIA
> CONTENT +
SOCIAL MEDIA +
PAID MEDIA
> CONTENT +
SOCIAL MEDIA +
PAID MEDIA
> WHAT
MATTERS

> (AGENCY)

## Page Intent

**Type:** `landing` (confidence 0.59)
**Description:** Australia's leading marketing agency for multi-venue hospitality groups. We focus on mobile-native content, social media distribution and paid media. Our clients include: Sydney Fish Market, Solotel, 

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → feature-grid → hero → nav → content → content → content → content → testimonials → content → testimonial → hero → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | feature-grid | CONTENT +
SOCIAL MEDIA +
PAID MEDIA | 0.8 |
| 3 | hero | CONTENT +
SOCIAL MEDIA +
PAID MEDIA | 0.85 |
| 4 | content | OUR CLIENTS | 0.3 |
| 5 | content | CREATIVE-
CREATIVE-
FIRST.
FIRST.
HOSPITALITY
HOSPITALITY
 FOCUSED.
 FOCUSED.
SY | 0.3 |
| 6 | content | OUR PROUD SELECTION | 0.3 |
| 7 | content | WE DO WHAT (REALLY) MATTERS | 0.3 |
| 8 | testimonials | WHAT WE OFFER | 0.4 |
| 9 | content | WHY PARTNER WITH WHAT MATTERS? | 0.3 |
| 10 | testimonial | Testimonials | 0.8 |
| 11 | hero | READY TO INVEST IN WHAT MATTERS? | 0.4 |
| 12 | footer | WHAT
MATTERS
 | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.285 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 800px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.467)
**Counts:** total 10, svg 0, icon 0, screenshot-like 0, photo-like 7
**Dominant aspect:** landscape
**Radius profile on images:** square

## Component Library

**Detected:** `bootstrap` (confidence 0.6)

Evidence:
- bootstrap utility hits: 3

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
