# Design Language: Areto - Webflow HTML website template

> Extracted from `https://areto.webflow.io/home-two` on September 4, 2026
> 1187 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f8fa8d` | rgb(248, 250, 141) | hsl(61, 92%, 77%) | 38 |
| Secondary | `#36503f` | rgb(54, 80, 63) | hsl(141, 19%, 26%) | 31 |
| Accent | `#120a0e` | rgb(18, 10, 14) | hsl(330, 29%, 5%) | 28 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1375 |
| `#4d4d4d` | hsl(0, 0%, 30%) | 611 |
| `#ece7e4` | hsl(22, 17%, 91%) | 167 |
| `#ffffff` | hsl(0, 0%, 100%) | 160 |
| `#cccccc` | hsl(0, 0%, 80%) | 18 |
| `#333333` | hsl(0, 0%, 20%) | 8 |
| `#f5f5f5` | hsl(0, 0%, 96%) | 2 |
| `#26382c` | hsl(140, 19%, 18%) | 1 |
| `#dddddd` | hsl(0, 0%, 87%) | 1 |

### Background Colors

Used on large-area elements: `#f5f5f5`, `#f8fa8d`, `#000000`, `#ffffff`, `#36503f`, `#26382c`, `#090507`, `#120a0e`, `#0d070a`, `#e0d8cb`

### Text Colors

Text color palette: `#000000`, `#4d4d4d`, `#333333`, `#ffffff`, `#cccccc`, `#f8fa8d`, `#36503f`, `#ece7e4`, `#120a0e`, `#e0d8cb`

### Gradients

```css
background-image: linear-gradient(rgb(0, 0, 0), rgba(0, 0, 0, 0) 22%), linear-gradient(0deg, rgb(0, 0, 0), rgba(0, 0, 0, 0) 50%), linear-gradient(90deg, rgba(0, 0, 0, 0.88), rgba(0, 0, 0, 0.63) 29%, rgba(0, 0, 0, 0) 63%), linear-gradient(270deg, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.84) 26%, rgba(0, 0, 0, 0) 49%);
```

```css
background-image: url("https://cdn.prod.website-files.com/6667e1295d7fb05ba4fa34fe/68b9711ca7ed74416c2d3b8c_Home%20service%20v1%20background%20noise.svg"), radial-gradient(circle at 50% 45%, rgb(248, 250, 141), rgba(248, 250, 141, 0) 35%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 1375 |
| `#4d4d4d` | text, border | 611 |
| `#ece7e4` | text, border | 167 |
| `#ffffff` | text, border, background | 160 |
| `#f8fa8d` | background, text, border | 38 |
| `#36503f` | background, text, border | 31 |
| `#120a0e` | background, text, border | 28 |
| `#e0d8cb` | border, background, text | 20 |
| `#cccccc` | text, border | 18 |
| `#333333` | text, border | 8 |
| `#7ec9a2` | background, text, border | 4 |
| `#f5f5f5` | background | 2 |
| `#26382c` | background | 1 |
| `#dddddd` | background | 1 |
| `#ffdede` | background | 1 |

## Typography

### Font Families

- **Inter Tight** — used for all (1156 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 192px | 12rem | 500 | 153.6px | -1.8px | div |
| 128px | 8rem | 500 | 128px | -1.8px | div |
| 102.4px | 6.4rem | 500 | 92.16px | normal | div |
| 60px | 3.75rem | 500 | 60px | -1.8px | h1, span, a, img |
| 40px | 2.5rem | 500 | 40px | -1.8px | a, img, div, h2 |
| 31px | 1.9375rem | 400 | 31px | normal | span |
| 30px | 1.875rem | 500 | 34.8px | -0.9008px | div |
| 29px | 1.8125rem | 300 | 30.16px | -0.435px | h3, br |
| 24px | 1.5rem | 400 | 25.92px | normal | div |
| 20px | 1.25rem | 500 | 25px | -0.60016px | div |
| 18px | 1.125rem | 500 | 22.86px | -0.54px | div |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14px | 0.875rem | 600 | 25.92px | normal | a, div |
| 13.5px | 0.8438rem | 400 | 17.55px | normal | button, span, b, br |
| 13px | 0.8125rem | 400 | 25.92px | normal | div, s, b, a |

### Heading Scale

```css
h1 { font-size: 60px; font-weight: 500; line-height: 60px; }
h2 { font-size: 40px; font-weight: 500; line-height: 40px; }
h3 { font-size: 29px; font-weight: 300; line-height: 30.16px; }
```

### Body Text

```css
body { font-size: 40px; font-weight: 500; line-height: 40px; }
```

### Font Weights in Use

`500` (543x), `400` (499x), `600` (136x), `700` (5x), `300` (2x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-24 | 24px | 1.5rem |
| spacing-30 | 30px | 1.875rem |
| spacing-35 | 35px | 2.1875rem |
| spacing-38 | 38px | 2.375rem |
| spacing-44 | 44px | 2.75rem |
| spacing-48 | 48px | 3rem |
| spacing-55 | 55px | 3.4375rem |
| spacing-60 | 60px | 3.75rem |
| spacing-64 | 64px | 4rem |
| spacing-67 | 67px | 4.1875rem |
| spacing-70 | 70px | 4.375rem |
| spacing-80 | 80px | 5rem |
| spacing-90 | 90px | 5.625rem |
| spacing-100 | 100px | 6.25rem |
| spacing-108 | 108px | 6.75rem |
| spacing-125 | 125px | 7.8125rem |
| spacing-130 | 130px | 8.125rem |
| spacing-150 | 150px | 9.375rem |
| spacing-190 | 190px | 11.875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 8px | 5 |
| lg | 11px | 8 |
| xl | 18px | 1 |
| full | 40px | 4 |
| full | 50px | 10 |
| full | 100px | 20 |
| full | 999px | 13 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0.449482px;
```

**lg** — blur: 14px
```css
box-shadow: rgba(0, 0, 0, 0.35) 0px 4px 14px 0px;
```

**xl** — blur: 26px
```css
box-shadow: rgba(0, 0, 0, 0.55) 0px 12px 26px -18px;
```

**xl** — blur: 40px
```css
box-shadow: rgba(0, 0, 0, 0.65) 0px 18px 40px -18px;
```

## CSS Custom Properties

### Colors

```css
--_colors---whitesmoke: whitesmoke;
--_colors---dark-gray: #4d4d4d;
--_colors---black: #000;
--_colors---jungle-green: #36503f;
--_colors---lime-yellow: #f8fa8d;
--_colors---white: white;
--_colors---border: #0003;
--_animation-units---home-one--counter-card-1: 3.125rem;
--_animation-units---home-one--counter-card-2: 7.5rem;
--_animation-units---home-one--counter-card-3: 19.375rem;
--_animation-units---home-one--counter-card-4: 13.125rem;
--_animation-units---home-one--service-card-shape-one: 50%;
--_animation-units---home-one--service-card-shape-two: 50%;
--_animation-units---home-one--service-card-shape-three: 50%;
--_animation-units---home-two--video-border-one: 10vw;
--_animation-units---home-two--video-border-two: 8vw;
--_animation-units---home-two--video-border-three: 50vw;
```

### Spacing

```css
--_font-details---font-size--body-size: 1rem;
--_font-details---font-size--h1-size: 3.75rem;
--_font-details---letter-spacing--h1-spacing: -.1125rem;
--_font-details---font-size--h2-size: 2.5rem;
--_font-details---letter-spacing--h2-spacing: -.075rem;
--_font-details---font-size--h3-size: 1.875rem;
--_font-details---letter-spacing--h3-spacing: -.0563rem;
--_font-details---font-size--h4-size: 1.5rem;
--_font-details---letter-spacing--h4-spacing: -.045rem;
--_font-details---font-size--h5-size: 1.25rem;
--_font-details---letter-spacing--h5-spacing: -.03751rem;
--_font-details---font-size--h6-size: 1.125rem;
--_font-details---letter-spacing--h6-spacing: -.03375rem;
--element-gaps--tiny: .9375rem;
--element-gaps--large: 2.1875rem;
--_font-details---font-size--tag-size: .875rem;
--_font-details---letter-spacing--tag-spacing: .08751rem;
--section-gaps--gutter: .9375rem;
--section-gaps--section-gap-large: 8.125rem;
--section-gaps--section-gap-medium: 7.8125rem;
--element-gaps--extra-small: 1.4375rem;
--element-gaps--extra-large: 3.125rem;
--element-gaps--small: 1.75rem;
--section-gaps--section-gap-tiny: 4.375rem;
--element-gaps--xxl: 3.25rem;
--element-gaps--medium: 2rem;
--section-gaps--section-gap-small: 5rem;
--_animation-units---home-two--hero-text-size-one: 3.75rem;
--_animation-units---home-two--hero-text-size-two: 2.5rem;
--_animation-units---home-two--hero-text-size-three: 3.75rem;
--_animation-units---home-two--hero-text-size-four: 3.75rem;
```

### Typography

```css
--_font-family---site-font: "Inter Tight", sans-serif;
--_font-details---line-heights--body-heights: 162.5%;
--_font-details---weights--body: 400;
--_font-family---heading-font: var(--_font-family---site-font);
--_font-details---line-heights--h1-heights: 100%;
--_font-details---weights--heading: 500;
--_font-details---line-heights--h2-heights: 112.5%;
--_font-details---line-heights--h3-heights: 116.67%;
--_font-details---line-heights--h4-heights: 120.83%;
--_font-details---line-heights--h5-heights: 125%;
--_font-details---line-heights--h6-heights: 127.78%;
--_font-details---weights--button: 600;
--_font-details---line-heights--tag-heights: 171.43%;
```

### Other

```css
--containers--container-large: 101.875rem;
--containers--container: 82.5rem;
--containers--container-small: 78.75rem;
--_animation-units---home-two--hero-v2-option-one: white;
--_animation-units---home-two--hero-v2-option-two: #fff0;
--_animation-units---home-two--hero-v2-option-three: white;
--_animation-units---home-two--hero-v2-option-four: white;
```

### Dependencies

```css
--_font-family---heading-font: --_font-family---site-font;
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
| sm | 480px | min-width |
| 560px | 560px | max-width |
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 991px | max-width |
| lg | 992px | min-width |
| xl | 1280px | min-width |
| 1440px | 1440px | min-width |
| 1920px | 1920px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.35s`, `0.4s`, `0.5s`

### Common Transitions

```css
transition: all;
transition: transform 0.3s, color 0.3s;
transition: background-color 0.35s;
transition: color 0.35s;
transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.4s;
transition: opacity 0.4s, visibility 0.4s;
transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
transition: background 0.3s, transform 0.35s;
transition: transform 0.3s;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**rtvpulse**
```css
@keyframes rtvpulse {
  0% { box-shadow: rgba(126, 201, 162, 0.5) 0px 0px 0px 0px; }
  70% { box-shadow: rgba(126, 201, 162, 0) 0px 0px 0px 9px; }
  100% { box-shadow: rgba(126, 201, 162, 0) 0px 0px 0px 0px; }
}
```

**rtvL**
```css
@keyframes rtvL {
  0% { transform: translateX(0px); }
  100% { transform: translateX(-50%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (22 instances)

```css
.button {
  background-color: rgb(248, 250, 141);
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 600;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (75 instances)

```css
.card {
  background-color: rgb(13, 7, 10);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.55) 0px 12px 26px -18px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (3 instances)

```css
.input {
  color: rgb(51, 51, 51);
  border-color: rgb(0, 0, 0) rgb(0, 0, 0) rgba(0, 0, 0, 0.2);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (65 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 600;
}
```

### Navigation (16 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(77, 77, 77);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (36 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(77, 77, 77);
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
  padding-top: 0px;
  padding-right: 0px;
  max-width: 760px;
}
```

### Dropdowns (46 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Badges (9 instances)

```css
.badge {
  background-color: rgb(54, 80, 63);
  color: rgb(54, 80, 63);
  font-size: 14px;
  font-weight: 600;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Tabs (4 instances)

```css
.tab {
  color: rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(77, 77, 77);
  border-radius: 0px;
}
```

### ProgressBars (6 instances)

```css
.progressBar {
  background-color: rgba(54, 80, 63, 0.1);
  color: rgb(77, 77, 77);
  border-radius: 50px;
  font-size: 16px;
}
```

### Switches (5 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(255, 255, 255);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 13 instances, 4 variants

**Variant 1** (3 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 13px 26px 13px 26px;
  border-radius: 8px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 600;
```

**Variant 2** (2 instances)

```css
  background: rgb(54, 80, 63);
  color: rgb(248, 250, 141);
  padding: 13px 26px 13px 26px;
  border-radius: 8px;
  border: 0px none rgb(248, 250, 141);
  font-size: 16px;
  font-weight: 600;
```

**Variant 3** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 600;
```

**Variant 4** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 600;
```

### Button — 13 instances, 2 variants

**Variant 1** (10 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 600;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(248, 250, 141);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(248, 250, 141);
  font-size: 16px;
  font-weight: 600;
```

### Button — 13 instances, 2 variants

**Variant 1** (10 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 600;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(248, 250, 141);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(248, 250, 141);
  font-size: 16px;
  font-weight: 600;
```

### Button — 5 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgb(248, 250, 141);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 600;
```

**Variant 2** (2 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(248, 250, 141);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(248, 250, 141);
  font-size: 16px;
  font-weight: 600;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(77, 77, 77);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

### Card — 32 instances, 4 variants

**Variant 1** (4 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(77, 77, 77);
  padding: 40px 0px 40px 0px;
  border-radius: 20px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (16 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(77, 77, 77);
  padding: 0px 24px 0px 24px;
  border-radius: 0px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

**Variant 3** (4 instances)

```css
  background: rgb(54, 80, 63);
  color: rgb(0, 0, 0);
  padding: 25px 25px 25px 35px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

**Variant 4** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(236, 231, 228);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(236, 231, 228);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(77, 77, 77);
  padding: 0px 24px 0px 24px;
  border-radius: 0px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(77, 77, 77);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(77, 77, 77);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

### Card — 6 instances, 2 variants

**Variant 1** (5 instances)

```css
  background: rgba(54, 80, 63, 0.1);
  color: rgb(77, 77, 77);
  padding: 0px 0px 0px 0px;
  border-radius: 50px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(77, 77, 77);
  padding: 60px 32px 60px 32px;
  border-radius: 20px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(77, 77, 77);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(77, 77, 77);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(77, 77, 77);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(77, 77, 77);
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

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0.2);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 100%;
  border: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 16px;
  font-weight: 400;
```

### Input — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(51, 51, 51);
  padding: 0px 0px 25px 0px;
  border-radius: 0px;
  border: 0px 0px 1px none none solid rgb(0, 0, 0) rgb(0, 0, 0) rgba(0, 0, 0, 0.2);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(54, 80, 63);
  color: rgb(77, 77, 77);
  padding: 0px 0px 0px 0px;
  border-radius: 100%;
  border: 1px solid rgb(54, 80, 63);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 9px 15px 9px 15px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(18, 10, 14);
  color: rgb(236, 231, 228);
  padding: 11px 17px 11px 13px;
  border-radius: 999px;
  border: 1px solid rgba(224, 216, 203, 0.3);
  font-size: 13.5px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(18, 10, 14);
  color: rgb(236, 231, 228);
  padding: 1px 6px 1px 6px;
  border-radius: 50%;
  border: 1px solid rgba(224, 216, 203, 0.4);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**5 grid containers** and **212 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1630px | 15px |
| 567px | 0px |
| 1320px | 15px |
| 1223px | 0px |
| 703px | 0px |
| 1250px | 0px |
| 472px | 0px |
| 740px | 0px |
| 383px | 0px |
| 1220px | 0px |
| 782px | 0px |
| 850px | 0px |
| 330px | 0px |
| 100% | 0px |
| 1519px | 0px |
| 630px | 0px |
| 760px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 3x |
| 3-column | 1x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 722.031px 497.969px;
gap: 30px;
grid-template-columns: 355px 355px;
gap: 68.8px 30px;
grid-template-columns: 212.5px 212.5px 212.5px 212.5px;
grid-template-columns: 192px 866px 192px;
grid-template-columns: 610px 610px;
gap: 30px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 102x |
| column/nowrap | 109x |
| row/wrap | 1x |

**Gap values:** `108px`, `10px`, `11px`, `12px`, `13px`, `14px`, `15px`, `20.8px`, `20px`, `24px`, `25px`, `30px`, `32px`, `35px`, `40px`, `45px`, `50px`, `55px`, `60px`, `64px`, `68.8px 30px`, `7px`, `8px`, `90px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 3 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#120a0e` | `#e0d8cb` | 13.81:1 | AAA |

## Design System Score

**Overall: 87/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 82/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 41 !important rules — prefer specificity over overrides
- 86% of CSS is unused — consider purging
- 5707 duplicate CSS declarations

## Gradients

**5 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | 0deg | 2 | brand |
| linear | 90deg | 3 | bold |
| linear | 270deg | 3 | bold |
| radial | circle at 50% 45% | 2 | brand |

```css
background: linear-gradient(rgb(0, 0, 0), rgba(0, 0, 0, 0) 22%);
background: linear-gradient(0deg, rgb(0, 0, 0), rgba(0, 0, 0, 0) 50%);
background: linear-gradient(90deg, rgba(0, 0, 0, 0.88), rgba(0, 0, 0, 0.63) 29%, rgba(0, 0, 0, 0) 63%);
background: linear-gradient(270deg, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.84) 26%, rgba(0, 0, 0, 0) 49%);
background: radial-gradient(circle at 50% 45%, rgb(248, 250, 141), rgba(248, 250, 141, 0) 35%);
```

## Z-Index Map

**11 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,99999 | div.r.t.-.n.a.v.b.a.r. .w.-.n.a.v, button.r.t.-.v.l.t.-.t.r.i.g.g.e.r, div.r.t.-.v.l.t.-.o.v.e.r.l.a.y |
| dropdown | 900,900 | div.r.t.-.n.a.v.-.d.r.o.p.d.o.w.n. .w.-.d.r.o.p.d.o.w.n, div.r.t.-.n.a.v.-.d.r.o.p.d.o.w.n. .w.-.d.r.o.p.d.o.w.n, div.r.t.-.n.a.v.-.d.r.o.p.d.o.w.n. .w.-.d.r.o.p.d.o.w.n |
| sticky | 10,10 | div.r.t.-.h.e.r.o.-.v.2.-.t.e.x.t.-.b.o.x, div.r.t.-.c.u.r.v.e.d.-.g.a.p, div.r.t.-.c.u.r.v.e.d.-.g.a.p. .r.t.-.c.u.r.v.e.-.c.o.l.o.r.-.g.r.e.e.n |
| base | -100,9 | video, div.w.-.l.a.y.o.u.t.-.h.f.l.e.x. .r.t.-.b.u.t.t.o.n.-.i.n.n.e.r.-.c.o.n.t.e.n.t, div.w.-.l.a.y.o.u.t.-.h.f.l.e.x. .r.t.-.b.u.t.t.o.n.-.i.n.n.e.r.-.c.o.n.t.e.n.t |

**Issues:**
- [object Object]

## SVG Icons

**3 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 3 |

**Icon colors:** `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | normal | normal |
| Inter Tight | google-fonts | 400, 500, 600 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 45 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (16x), 4:3 (14x), 16:9 (13x), 3:4 (4x), 3.03:1 (1x), 3:2 (1x), 4.94:1 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **ease-out** (2 uses) — `cubic-bezier(0.22, 1, 0.36, 1)`, `cubic-bezier(0.16, 1, 0.3, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `rtvpulse` | custom | box-shadow | 1 |
| `rtvL` | slide-x | transform | 1 |

## Component Anatomy

### card — 56 instances

**Slots:** media
**Sizes:** xl

### button — 50 instances

**Slots:** label, icon

### input — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (verbose)

### Top CTA Verbs

- **view** (8)
- **discover** (8)
- **get** (4)
- **start** (4)
- **read** (2)
- **style** (1)
- **open** (1)

### Button Copy Patterns

- "discover more" (8×)
- "view more" (6×)
- "get a quote" (4×)
- "start consulting now" (4×)
- "read more" (2×)
- "view more members" (2×)
- "<style>
  [data-wf-bgvideo-fallback-img] {
    display: none;
  }
  @media (prefers-reduced-motion: reduce) {
    [data-wf-bgvideo-fallback-img] {
      positio" (1×)
- "190
open the vault
190 templates · 3 new this week" (1×)

### Sample Headings

> Accelerating growth
with proven strategies
> Empowering businesses with tailored strategies, innovative insights, and expert guidance to achieve sustainable growth, efficiency, and profitability worldwide
> Innovative solutions that transform
businesses for tomorrow
> Transforming complex challenges into
measurable business success
> Unlock growth opportunities, streamline operations, and achieve measurable results with tailored business consulting solutions designed to transform challenges
> Trusted by 15,000+
business owners
> Elevate the world with our
consultant’s expertise

## Page Intent

**Type:** `blog-post` (confidence 0.23)
**Description:** Discover Areto, your trusted business consulting partner. We provide strategic insights, expert guidance, and solutions to drive lasting success.

Alternates: landing (0.3)

## Section Roles

Reading order (top→bottom): nav → nav → nav → nav → nav → nav → nav → hero → hero → hero → testimonials → content → content → hero → hero → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | nav | — | 0.9 |
| 5 | nav | — | 0.9 |
| 6 | nav | — | 0.9 |
| 7 | hero | Accelerating growth
with proven strategies | 0.85 |
| 8 | hero | Empowering businesses with tailored strategies, innovative insights, and expert  | 0.4 |
| 9 | hero | Innovative solutions that transform
businesses for tomorrow | 0.4 |
| 10 | testimonials | Transforming complex challenges into
measurable business success | 0.4 |
| 11 | content | Unlock growth opportunities, streamline operations, and achieve measurable resul | 0.3 |
| 12 | content | — | 0.3 |
| 13 | hero | Trusted by 15,000+
business owners | 0.4 |
| 14 | hero | Elevate the world with our
consultant’s expertise | 0.4 |
| 15 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.144 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 999px |
| backdrop-filter in use | no |
| Gradients | 5 |

## Imagery Style

**Label:** `photography` (confidence 0.13)
**Counts:** total 50, svg 37, icon 28, screenshot-like 0, photo-like 13
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter Tight` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
