# Design Language: Bobbin - AI lesson planning for tutors | TutorCruncher

> Extracted from `https://withbobbin.com/` on September 4, 2026
> 1639 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fbf27e` | rgb(251, 242, 126) | hsl(56, 94%, 74%) | 189 |
| Secondary | `#f7f4f0` | rgb(247, 244, 240) | hsl(34, 30%, 95%) | 28 |
| Accent | `#faf39b` | rgb(250, 243, 155) | hsl(56, 90%, 79%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 2179 |
| `#ffffff` | hsl(0, 0%, 100%) | 614 |
| `#70685c` | hsl(36, 10%, 40%) | 154 |
| `#544e45` | hsl(36, 10%, 30%) | 100 |
| `#8c8273` | hsl(36, 10%, 50%) | 66 |
| `#a39b8f` | hsl(36, 10%, 60%) | 42 |
| `#cdc6bc` | hsl(35, 15%, 77%) | 17 |
| `#2a241d` | hsl(32, 18%, 14%) | 7 |
| `#413c33` | hsl(39, 12%, 23%) | 4 |
| `#e8e4de` | hsl(36, 18%, 89%) | 3 |

### Background Colors

Used on large-area elements: `#000000`, `#2a241d`, `#ffffff`, `#f7f4f0`, `#413c33`, `#fbf27e`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#fbf27e`, `#2a241d`, `#70685c`, `#544e45`, `#a39b8f`, `#cdc6bc`, `#8c8273`

### Gradients

```css
background-image: linear-gradient(90deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(oklab(0 0 0 / 0.6) 0px, oklab(0 0 0 / 0.2) 50%, rgba(0, 0, 0, 0) 100%);
```

```css
background-image: radial-gradient(100% 100% at 50% 100%, rgb(251, 242, 126) 0px, rgba(251, 242, 126, 0) 58%);
```

```css
background-image: radial-gradient(100% 100% at 50% 100%, rgb(251, 242, 126) 27%, rgba(251, 242, 126, 0) 100%);
```

```css
background-image: linear-gradient(rgb(0, 0, 0), rgb(0, 0, 0)), none;
```

```css
background-image: linear-gradient(rgb(0, 0, 0), rgb(0, 0, 0)), conic-gradient(rgb(65, 60, 51), rgb(167, 154, 131), rgb(65, 60, 51));
```

```css
background-image: linear-gradient(in oklab, rgba(0, 0, 0, 0) 0px, rgb(255, 247, 192) 50%, rgb(251, 242, 126) 100%);
```

```css
background-image: linear-gradient(to top, oklab(0 0 0 / 0.4) 0px, rgba(0, 0, 0, 0) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, background, border | 2179 |
| `#ffffff` | text, border, background | 614 |
| `#fbf27e` | background, text, border | 189 |
| `#70685c` | text, border, background | 154 |
| `#544e45` | text, border | 100 |
| `#8c8273` | text, border | 66 |
| `#a39b8f` | text, border | 42 |
| `#f7f4f0` | background | 28 |
| `#cdc6bc` | text, border, background | 17 |
| `#2a241d` | background, text, border | 7 |
| `#413c33` | background | 4 |
| `#e8e4de` | border, background | 3 |
| `#f8f3d3` | background | 1 |
| `#faf39b` | background | 1 |

## Typography

### Font Families

- **GT Standard** — used for all (1609 elements)
- **GT Alpina** — used for all (30 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 60px | 3.75rem | 400 | 66px | -1.5px | h1, span, p, h2 |
| 48px | 3rem | 400 | 51.84px | -1.2px | h2, span, br |
| 34px | 2.125rem | 500 | 37.4px | -0.85px | h3 |
| 32px | 2rem | 500 | 35.2px | -0.8px | h3 |
| 24px | 1.5rem | 400 | 36px | normal | p |
| 20px | 1.25rem | 400 | 26px | -0.5px | h2, p, span, h3 |
| 16px | 1rem | 400 | 24px | normal | html, head, link, script |
| 14px | 0.875rem | 500 | 21px | normal | a, button, svg, path |
| 12px | 0.75rem | 400 | 12px | normal | a, div, span, svg |

### Heading Scale

```css
h1 { font-size: 60px; font-weight: 400; line-height: 66px; }
h2 { font-size: 48px; font-weight: 400; line-height: 51.84px; }
h3 { font-size: 34px; font-weight: 500; line-height: 37.4px; }
h3 { font-size: 32px; font-weight: 500; line-height: 35.2px; }
h2 { font-size: 20px; font-weight: 400; line-height: 26px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: 24px; }
```

### Font Weights in Use

`400` (1543x), `500` (91x), `700` (4x), `300` (1x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-51 | 51px | 3.1875rem |
| spacing-56 | 56px | 3.5rem |
| spacing-74 | 74px | 4.625rem |
| spacing-80 | 80px | 5rem |
| spacing-89 | 89px | 5.5625rem |
| spacing-107 | 107px | 6.6875rem |
| spacing-120 | 120px | 7.5rem |
| spacing-137 | 137px | 8.5625rem |
| spacing-150 | 150px | 9.375rem |
| spacing-160 | 160px | 10rem |
| spacing-200 | 200px | 12.5rem |
| spacing-285 | 285px | 17.8125rem |
| spacing-290 | 290px | 18.125rem |
| spacing-330 | 330px | 20.625rem |
| spacing-343 | 343px | 21.4375rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 5px | 3 |
| lg | 11px | 2 |
| lg | 14px | 3 |
| xl | 20px | 34 |
| xl | 24px | 11 |
| full | 36px | 18 |
| full | 48px | 1 |
| full | 9999px | 8 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
```

**lg** — blur: 15px
```css
box-shadow: rgba(250, 177, 47, 0.15) 0px 7px 15px 0px, rgba(250, 177, 47, 0.13) 0px 27px 27px 0px, rgba(250, 177, 47, 0.08) 0px 61px 37px 0px;
```

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--color-spark-cream-dark: #e8e4de;
--color-spark-grey-50: #70685c;
--color-spark-grey-20: #e8e4de;
--color-spark-black: #000;
--tw-inset-ring-shadow: 0 0 #0000;
--color-spark-cream: #f7f4f0;
--color-spark-mute: #a39b8f;
--border-angle: 0deg;
--tw-ring-offset-color: #fff;
--color-spark-charcoal: #2a241d;
--color-white: #fff;
--color-spark-grey-70: #544e45;
--color-spark-line: #cdc6bc;
--tw-border-style: solid;
--color-spark-pale-yellow: #fbf27e;
--color-spark-grey-60: #625b50;
--tw-ring-offset-width: 0px;
--color-spark-yellow: #fbf27e;
--color-spark-grey-30: #cdc6bc;
--color-black: #000;
--color-spark-footer-text: #8c8273;
--color-spark-white: #fff;
--color-spark-grey-40: #a39b8f;
--color-spark-grey-80: #413c33;
--color-spark-yellow-deep: #f0e367;
--color-spark-yellow-soft: #fff7c0;
--color-spark-grey-10: #f7f4f0;
```

### Spacing

```css
--text-h1--letter-spacing: -.02em;
--spacing: .25rem;
--text-h3--letter-spacing: -.01em;
--spacing-m: 40px;
--tw-space-y-reverse: 0;
--text-h2--letter-spacing: -.02em;
```

### Typography

```css
--text-body-sm: 12px;
--text-h2: 60px;
--text-body-md: 14px;
--text-h6: 20px;
--text-base--line-height: calc(1.5 / 1);
--text-h4: 32px;
--text-body-lg: 16px;
--font-mono: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
--text-body-sm--line-height: 1.5;
--tracking-wide: .025em;
--text-h2--line-height: 1.05;
--text-body-xs: 10px;
--leading-tight: 1.25;
--text-h5: 24px;
--font-sans: "GT Standard",system-ui,-apple-system,"Segoe UI",sans-serif;
--text-h5--line-height: 1.2;
--text-h4--line-height: 1.1;
--text-xs: .75rem;
--default-font-family: "GT Standard",system-ui,-apple-system,"Segoe UI",sans-serif;
--text-xs--line-height: calc(1 / .75);
--font-weight-medium: 500;
--font-weight-normal: 400;
--font-weight-light: 300;
--text-h6--line-height: 1.3;
--font-serif: "GT Alpina",Georgia,serif;
--text-h3--line-height: 1.08;
--text-h1: 72px;
--text-h1--line-height: 1.03;
--text-body-md--line-height: 1.5;
--text-h3: 48px;
--text-body-lg--line-height: 1.3;
--text-base: 1rem;
--default-mono-font-family: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
```

### Shadows

```css
--tw-inset-shadow-alpha: 100%;
--tw-drop-shadow-alpha: 100%;
--tw-inset-shadow: 0 0 #0000;
--tw-shadow-alpha: 100%;
--tw-shadow: 0 0 #0000;
```

### Radii

```css
--radius-sm: 12px;
--radius-2xl: 1rem;
--radius-md: 20px;
--radius-lg: 36px;
```

### Other

```css
--default-transition-timing-function: cubic-bezier(.4,0,.2,1);
--tw-translate-z: 0;
--tw-gradient-via: rgba(0, 0, 0, 0);
--tw-scale-y: 1;
--tw-translate-y: 0;
--blur-md: 12px;
--ease-out: cubic-bezier(0,0,.2,1);
--tw-gradient-from: rgba(0, 0, 0, 0);
--tw-gradient-to: rgba(0, 0, 0, 0);
--tw-scale-z: 1;
--tw-translate-x: 0;
--tw-gradient-via-position: 50%;
--tw-scroll-snap-strictness: proximity;
--height-hero: 950px;
--tw-scale-x: 1;
--tw-gradient-to-position: 100%;
--default-transition-duration: .15s;
--animate-pulse: pulse 2s cubic-bezier(.4,0,.6,1) infinite;
--tw-gradient-from-position: 0px;
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
| 560px | 560px | max-width |
| sm | 640px | min-width |
| md | 768px | min-width |
| 860px | 860px | min-width |
| lg | 960px | min-width |
| 1100px | 1100px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.15s`, `0.7s`, `0.2s`, `0.5s`, `0.6s`, `0.4s`, `0.35s`, `0.45s`, `0.25s`, `8s`

### Common Transitions

```css
transition: all;
transition: color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), translate 0.3s cubic-bezier(0.4, 0, 0.2, 1), scale 0.3s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.3s cubic-bezier(0.4, 0, 0.2, 1), filter 0.3s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.3s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.3s cubic-bezier(0.4, 0, 0.2, 1), display 0.3s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.3s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.3s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.3s cubic-bezier(0, 0, 0.2, 1), translate 0.3s cubic-bezier(0, 0, 0.2, 1), scale 0.3s cubic-bezier(0, 0, 0.2, 1), rotate 0.3s cubic-bezier(0, 0, 0.2, 1);
transition: opacity 0.7s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.2s cubic-bezier(0, 0, 0.2, 1), translate 0.2s cubic-bezier(0, 0, 0.2, 1), scale 0.2s cubic-bezier(0, 0, 0.2, 1), rotate 0.2s cubic-bezier(0, 0, 0.2, 1);
transition: opacity 0.7s cubic-bezier(0, 0, 0.2, 1) 0.15s;
transition: color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.7s cubic-bezier(0, 0, 0.2, 1);
```

### Keyframe Animations

**cta-fade-up**
```css
@keyframes cta-fade-up {
  0% { opacity: 0; transform: translateY(10px); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**cta-unlock-in**
```css
@keyframes cta-unlock-in {
  0% { opacity: 0; translate: -50% 24px; }
  100% { opacity: 1; translate: -50%; }
}
```

**cookie-pop**
```css
@keyframes cookie-pop {
  0% { opacity: 0; transform: translateY(8px) scale(0.98); }
  100% { opacity: 1; transform: translateY(0px) scale(1); }
}
```

**border-rotate**
```css
@keyframes border-rotate {
  100% { --border-angle: 360deg; }
}
```

**cursor-blink**
```css
@keyframes cursor-blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}
```

**pulse**
```css
@keyframes pulse {
  50% { opacity: 0.5; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (24 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 28px;
  border-radius: 3.35544e+07px;
}
```

### Cards (83 instances)

```css
.card {
  background-color: rgb(247, 244, 240);
  border-radius: 0px;
  box-shadow: rgba(250, 177, 47, 0.15) 0px 7px 15px 0px, rgba(250, 177, 47, 0.13) 0px 27px 27px 0px, rgba(250, 177, 47, 0.08) 0px 61px 37px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (1 instances)

```css
.input {
  color: rgb(0, 0, 0);
  border-color: rgb(0, 0, 0);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (22 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (7 instances)

```css
.navigatio {
  color: rgb(255, 255, 255);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 16px;
  padding-right: 16px;
  position: static;
}
```

### Footer (4 instances)

```css
.foote {
  background-color: rgb(0, 0, 0);
  color: rgb(140, 130, 115);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
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

### Badges (1 instances)

```css
.badge {
  color: rgb(84, 78, 69);
  font-size: 20px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Accordions (14 instances)

```css
.accordion {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(0, 0, 0);
}
```

### ProgressBars (28 instances)

```css
.progressBar {
  background-color: rgb(247, 244, 240);
  color: rgb(255, 255, 255);
  border-radius: 0px;
  font-size: 16px;
}
```

### Switches (8 instances)

```css
.switche {
  background-color: rgb(247, 244, 240);
  border-radius: 9999px;
  border-color: rgb(0, 0, 0);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(251, 242, 126);
  color: rgb(0, 0, 0);
  padding: 0px 16px 0px 16px;
  border-radius: 3.35544e+07px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 500;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgb(251, 242, 126);
  color: rgb(0, 0, 0);
  padding: 0px 24px 0px 24px;
  border-radius: 3.35544e+07px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 500;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 28px 28px 28px 28px;
  border-radius: 20px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(84, 78, 69);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(84, 78, 69);
  font-size: 20px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 20px;
  font-weight: 500;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(248, 243, 211);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 9999px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 24px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(247, 244, 240);
  color: rgb(163, 155, 143);
  padding: 0px 20px 0px 20px;
  border-radius: 3.35544e+07px;
  border: 0px solid rgb(163, 155, 143);
  font-size: 14px;
  font-weight: 500;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 20px;
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 6 instances, 2 variants

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 8px 12px 8px 12px;
  border-radius: 3.35544e+07px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 500;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(140, 130, 115);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(140, 130, 115);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**25 grid containers** and **336 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1512px | 20px |
| 100% | 0px |
| 681px | 0px |
| 600px | 28px |
| 1000px | 0px |
| 820px | 0px |
| 800px | 0px |
| 900px | 0px |
| 700px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 10x |
| 1-column | 4x |
| 2-column | 3x |
| 4-column | 3x |
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 560px 560px;
grid-template-columns: 500px 250px 250px;
grid-template-columns: 420px 644px;
gap: 56px;
grid-template-columns: 265px 265px 265px 265px;
gap: 20px;
grid-template-columns: 360px 360px 360px;
gap: 20px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 235x |
| column/nowrap | 98x |
| row/wrap | 3x |

**Gap values:** `10px`, `12px`, `16px`, `20px`, `28px`, `32px`, `32px normal`, `40px`, `4px`, `56px`, `6px`, `80px`, `8px`, `8px 20px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 18 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#000000` | `#fbf27e` | 18.1:1 | AAA |
| `#544e45` | `#f7f4f0` | 7.5:1 | AAA |
| `#ffffff` | `#000000` | 21:1 | AAA |

## Design System Score

**Overall: 87/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 90/100 |
| Spacing System | 70/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Clean elevation system, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 15 !important rules — prefer specificity over overrides
- 956 duplicate CSS declarations

## Gradients

**8 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 90deg | 2 | brand |
| linear | — | 3 | bold |
| radial | — | 3 | bold |
| radial | — | 3 | bold |
| linear | — | 2 | brand |
| conic | — | 3 | bold |
| linear | — | 4 | bold |
| linear | to top | 2 | brand |

```css
background: linear-gradient(90deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0));
background: linear-gradient(oklab(0 0 0 / 0.6) 0px, oklab(0 0 0 / 0.2) 50%, rgba(0, 0, 0, 0) 100%);
background: radial-gradient(100% 100% at 50% 100%, rgb(251, 242, 126) 0px, rgba(251, 242, 126, 0) 58%);
background: radial-gradient(100% 100% at 50% 100%, rgb(251, 242, 126) 27%, rgba(251, 242, 126, 0) 100%);
background: linear-gradient(rgb(0, 0, 0), rgb(0, 0, 0));
```

## Z-Index Map

**5 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | div.p.r.o.g.r.e.s.s.i.v.e.-.b.l.u.r. .i.s.-.-.l.i.g.h.t, div.c.o.n.t.a.i.n.e.r.-.w.i.d.e. .r.e.l.a.t.i.v.e. .z.-.1.0. .f.l.e.x. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.b.e.t.w.e.e.n. .p.-.5. .x.l.:.p.y.-.7, div.a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .z.-.1.0. .f.l.e.x. .f.l.e.x.-.c.o.l. .i.t.e.m.s.-.c.e.n.t.e.r |
| base | -10,2 | footer.t.e.x.t.-.s.p.a.r.k.-.f.o.o.t.e.r.-.t.e.x.t. .f.i.x.e.d. .i.n.s.e.t.-.x.-.0. .b.o.t.t.o.m.-.0. .-.z.-.1.0. .b.g.-.b.l.a.c.k, div.r.e.l.a.t.i.v.e. .z.-.2. .m.x.-.a.u.t.o. .m.b.-.1.6. .f.l.e.x. .h.-.f.u.l.l. .m.a.x.-.w.-.[.7.0.0.p.x.]. .f.l.e.x.-.c.o.l. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .g.a.p.-.1.0 |

## SVG Icons

**34 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 8 |
| sm | 1 |
| md | 5 |
| lg | 13 |
| xl | 7 |

**Icon colors:** `rgb(250,241,125)`, `rgb(29,24,19)`, `rgb(0, 0, 0)`, `currentColor`, `#1D1914`, `rgba(255,255,255,0.3)`, `black`, `#FBF27E`, `#1A1A1A`, `#CDC6BC`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| GT Alpina | self-hosted | 400 | normal |
| GT Standard | self-hosted | 300, 400, 500 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| avatar | 8 | objectFit: cover, borderRadius: 3.35544e+07px, shape: circular |
| general | 7 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 5 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (12x), 3:4 (7x), 4:3 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `450ms` | 450 |
| `xxl` | `8s` | 8000 |

### Easing Families

- **custom** (112 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`, `cubic-bezier(0.7, 0, 0.3, 1)`
- **ease-out** (40 uses) — `cubic-bezier(0, 0, 0.2, 1)`, `cubic-bezier(0.22, 1, 0.36, 1)`
- **linear** (4 uses) — `linear`
- **ease-in-out** (2 uses) — `ease`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `cursor-blink` | fade | opacity | 2 |

## Component Anatomy

### card — 32 instances

**Slots:** description, media
**Sizes:** xl

### button — 19 instances

**Slots:** label, icon
**Sizes:** medium · md · sm

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **start** (6)
- **create** (2)
- **capture** (1)
- **teach** (1)
- **generate** (1)
- **plans** (1)
- **calculator** (1)
- **gbp** (1)

### Button Copy Patterns

- "start free trial" (5×)
- "plan without headaches

ai-generated lesson plans

tell bobbin what you're teaching next and it'll create a fully editable, structured lesson plan

curriculum-b" (1×)
- "capture without confusion

integrated lesson transcription

bobbin captures what's covered in lessons through an integrated online whiteboard and app for in-per" (1×)
- "report without procrastination

parent-ready reporting

bobbin uses every session summary to create a parent-ready progress report for you to review, edit and s" (1×)
- "teach without compromise

data-driven improvement

bobbin brings together all the threads of your lessons, tracking analytics and powering the insights you need" (1×)
- "generate" (1×)
- "plans" (1×)
- "calculator" (1×)
- "gbp" (1×)
- "usd" (1×)

### Sample Headings

> Better 
testing
> TutorCruncher and Bobbin are trusted by 1,800+ tutoring companies
> AI tools for online and in-person tutoring
> Turn your lessons into momentum
> Find your flow
> Better 
testing
> TutorCruncher and Bobbin are trusted by 1,800+ tutoring companies
> AI tools for online and in-person tutoring
> Turn your lessons into momentum
> Find your flow

## Page Intent

**Type:** `landing` (confidence 0.59)
**Description:** Bobbin is an AI tutoring platform from TutorCruncher that plans lessons, captures live notes, and writes parent reports — so tutors spend more time teaching.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): steps → pricing → hero → nav → footer → logo-wall → testimonials → content → nav → nav → nav → testimonials → hero → content → testimonial → content → pricing-table → faq → feature-grid → pricing

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | steps | — | 0.75 |
| 1 | nav | — | 0.9 |
| 2 | pricing | Better 
testing | 0.4 |
| 3 | hero | Better 
testing | 0.85 |
| 4 | logo-wall | TutorCruncher and Bobbin are trusted by 1,800+ tutoring companies | 0.85 |
| 5 | testimonials | AI tools for online and in-person tutoring | 0.4 |
| 6 | content | Turn your lessons into momentum | 0.3 |
| 7 | nav | Find your flow | 0.4 |
| 8 | nav | Focus your mind | 0.4 |
| 9 | nav | Feel your value | 0.4 |
| 10 | testimonials | Fits the way you already work | 0.4 |
| 11 | hero | Try Bobbin's lesson planner for yourself... | 0.4 |
| 12 | content | Built for tutor trust | 0.3 |
| 13 | testimonial | Don't just take our word for it | 0.8 |
| 14 | content | Made for tutoring | 0.3 |
| 15 | pricing-table | Explore our pricing | 0.9 |
| 16 | faq | Frequently Asked Questions | 0.85 |
| 17 | feature-grid | Designed for tutors
made by TutorCruncher | 0.8 |
| 18 | pricing | Your lessons, your threads, all in one place | 0.4 |
| 19 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.169 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 8 |

## Imagery Style

**Label:** `photography` (confidence 0.433)
**Counts:** total 20, svg 0, icon 0, screenshot-like 0, photo-like 13
**Dominant aspect:** square-ish
**Radius profile on images:** full

## Component Library

**Detected:** `tailwindcss` (confidence 0.83)

Evidence:
- tailwind-like class density 79%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `GT Standard` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
