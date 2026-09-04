# Design Language: Paper – design, share, ship

> Extracted from `https://paper.design/` on September 4, 2026
> 4925 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#3d7cff` | rgb(61, 124, 255) | hsl(221, 100%, 62%) | 8 |
| Secondary | `#0fa821` | rgb(15, 168, 33) | hsl(127, 84%, 36%) | 2 |
| Accent | `#4d94fb` | rgb(77, 148, 251) | hsl(216, 96%, 64%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 4358 |
| `#1e2126` | hsl(218, 12%, 13%) | 778 |
| `#373a40` | hsl(220, 8%, 23%) | 544 |
| `#b7babf` | hsl(218, 6%, 73%) | 192 |
| `#585c62` | hsl(216, 5%, 36%) | 141 |
| `#82858b` | hsl(220, 4%, 53%) | 127 |
| `#797979` | hsl(0, 0%, 47%) | 120 |
| `#ebedef` | hsl(210, 11%, 93%) | 109 |
| `#959595` | hsl(0, 0%, 58%) | 72 |
| `#ffffff` | hsl(0, 0%, 100%) | 31 |

### Background Colors

Used on large-area elements: `#f2f2f2`, `#b7babf`, `#ebedef`, `#ffffff`, `#82858b`, `#000102`

### Text Colors

Text color palette: `#222222`, `#000000`, `#959595`, `#797979`, `#010203`, `#1e2126`, `#373a40`, `#000102`, `#ffffff`, `#0fa821`

### Gradients

```css
background-image: linear-gradient(90deg, lab(96.172 0 0) 33%, lab(88.168 0 0) 33%, lab(88.168 0 0) 67%, lab(99.304 -0.0000298023 0) 67%);
```

```css
background-image: linear-gradient(oklch(0.776395 0.0894303 257.993), oklch(0.703994 0.126381 257.994));
```

```css
background-image: linear-gradient(to right, lab(0 0 0) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(lab(0 0 0) 1px, rgba(0, 0, 0, 0) 1px);
```

```css
background-image: linear-gradient(to right, lab(94.2188 -1.42306 5.34524) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(lab(94.2188 -1.42306 5.34524) 1px, rgba(0, 0, 0, 0) 1px);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 4358 |
| `#1e2126` | text, border, background | 778 |
| `#373a40` | text, border | 544 |
| `#b7babf` | background, border, text | 192 |
| `#585c62` | text, border, background | 141 |
| `#82858b` | border, background | 127 |
| `#797979` | text, border | 120 |
| `#ebedef` | background, border, text | 109 |
| `#959595` | text, border | 72 |
| `#ffffff` | background, text, border | 31 |
| `#3d7cff` | background | 8 |
| `#0fa821` | text, border | 2 |
| `#4d94fb` | background | 1 |

## Typography

### Font Families

- **Inter** — used for body (2346 elements)
- **Matter** — used for all (842 elements)
- **Paper Mono** — used for body (12 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 64px | 4rem | 360 | 64px | -1.28px | h3, span |
| 48px | 3rem | 360 | 48px | -0.96px | h1, h2, span, br |
| 36px | 2.25rem | 570 | 36px | -0.36px | div |
| 26px | 1.625rem | 570 | 28px | -0.52px | div |
| 22px | 1.375rem | 670 | 28px | -0.44px | div |
| 18px | 1.125rem | 400 | 28px | 0.18px | html, head, style, meta |
| 17px | 1.0625rem | 600 | 22px | 0.18px | div |
| 14px | 0.875rem | 400 | 18px | 0.18px | div, span, h4, a |
| 13px | 0.8125rem | 500 | 16px | 0.18px | div |
| 12px | 0.75rem | 400 | 16px | 0.18px | div, svg, path, rect |
| 11px | 0.6875rem | 400 | 16px | 0.18px | div |
| 10px | 0.625rem | 400 | 12px | 0.6px | div |

### Heading Scale

```css
h3 { font-size: 64px; font-weight: 360; line-height: 64px; }
h1 { font-size: 48px; font-weight: 360; line-height: 48px; }
h3 { font-size: 18px; font-weight: 400; line-height: 28px; }
h4 { font-size: 14px; font-weight: 400; line-height: 18px; }
```

### Body Text

```css
body { font-size: 18px; font-weight: 400; line-height: 28px; }
```

### Font Weights in Use

`400` (4586x), `500` (254x), `360` (21x), `600` (21x), `550` (14x), `480` (11x), `670` (10x), `570` (8x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-28 | 28px | 1.75rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-52 | 52px | 3.25rem |
| spacing-60 | 60px | 3.75rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-90 | 90px | 5.625rem |
| spacing-96 | 96px | 6rem |
| spacing-112 | 112px | 7rem |
| spacing-120 | 120px | 7.5rem |
| spacing-146 | 146px | 9.125rem |
| spacing-154 | 154px | 9.625rem |
| spacing-240 | 240px | 15rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 0px | 1 |
| sm | 4px | 129 |
| md | 8px | 43 |
| lg | 12px | 12 |
| xl | 18px | 3 |
| xl | 24px | 1 |
| full | 41px | 12 |
| full | 9999px | 54 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 1px 0px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(128, 128, 128, 0.15) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 93px 26px 0px, rgba(0, 0, 0, 0.01) 0px 59px 24px 0px, rgba(0, 0, 0, 0.05) 0px 33px 20px 0px, rgba(0, 0, 0, 0.09) 0px 15px 15px 0px, rgba(0, 0, 0, 0.1) 0px 4px 8px 0px;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(216, 215, 216) 0px 0px 0px 0.75px inset;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(215, 215, 215) 0px 0px 0px 0.75px inset;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.533) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.533) 0px 0px 1px 1px inset, rgba(0, 0, 0, 0.067) 0px 0.5px 1px 0px, rgba(0, 0, 0, 0.133) 0px 0px 1px 0px, rgba(0, 0, 0, 0.133) 0px 0px 4px -1px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.533) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.533) 0px 0px 1px 1px inset, rgba(0, 0, 0, 0.133) 0px 0px 1px 0px, rgba(0, 0, 0, 0.133) 0px 0px 3px -1px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.667) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.667) 0px 0px 1px 1px inset, rgba(0, 0, 0, 0.133) 0px 0.5px 1px 0px, rgba(0, 0, 0, 0.094) 0px 0px 1px 1px, rgba(0, 0, 0, 0.067) 0px 0px 3px -1px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.533) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.533) 0px 0px 1px 1px inset, rgba(0, 0, 0, 0.35) 0px 2px 4px -2px, rgba(0, 0, 0, 0.3) 0px 0px 1px 0.5px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.12) 0px -1px 0px 0px inset;
```

**md** — blur: 10px
```css
box-shadow: rgba(0, 0, 0, 0.08) 0px 4px 10px 0px, rgba(0, 0, 0, 0.08) 0px 2px 4px -1px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
```

**md** — blur: 10px
```css
box-shadow: rgba(0, 0, 0, 0.12) 0px 4px 10px 0px, rgba(0, 0, 0, 0.12) 0px 2px 4px -1px, rgba(0, 0, 0, 0.12) 0px 0px 4px -1px;
```

**md** — blur: 8px
```css
box-shadow: rgba(0, 0, 0, 0.08) 0px 8px 8px -4px, rgba(0, 0, 0, 0.08) 0px 2px 4px -2px, rgba(0, 0, 0, 0.08) 0px 1px 1px -1px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
```

**xl** — blur: 32px
```css
box-shadow: rgba(0, 0, 0, 0.12) 0px 16px 32px -16px, rgba(0, 0, 0, 0.08) 0px 8px 16px -8px, rgba(0, 0, 0, 0.04) 0px 4px 8px -4px, rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
```

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--color-gray-800: lab(27.9756% 0 0);
--color-paper-50: lab(98.8967% -.385851 1.42193);
--tw-inset-ring-shadow: 0 0 #0000;
--color-focus: lab(69.3174% -2.26048 -37.0102);
--color-selection: color-mix(in oklch,lab(69.3174% -2.26048 -37.0102)50%,transparent);
--color-gray-300: lab(78.0416% -.138372 .510192);
--playlist-accent: lab(58.2618% 2.51451 -55.9466);
--color-blue-link: lab(46.5086% 5.16978 -55.6919);
--playlist-muted: lab(68.8656% 0 -.0000119209);
--color-dark-gray: lab(43.1948% 0 0);
--color-gray-500: lab(59.7944% -.0000298023 0);
--color-root: lab(94.2188% -1.42306 5.34524);
--color-blue-text: lab(58.2618% 2.51451 -55.9466);
--color-gray-900: lab(13.232% 0 0);
--color-gray-50: lab(96.4731% -.395507 1.45847);
--playlist-player-bg: lab(92.6688% -.0000298023 0);
--color-gray-950: lab(8.244% 0 -.00000298023);
--tw-ring-offset-color: #fff;
--color-gray: lab(59.7944% -.0000298023 0);
--color-white: lab(100% 0 0);
--playlist-border: lab(90.16% .431716 -1.60234);
--color-gray-700: lab(38.6592% -.0000149012 0);
--color-gray-400: lab(68.8656% 0 -.0000119209);
--color-gray-600: lab(43.1948% 0 0);
--color-cream: lab(94.2188% -1.42306 5.34524);
--tw-border-style: solid;
--color-gray-100: lab(92.6335% -.395387 1.45856);
--color-background: lab(98.8967% -.385851 1.42193);
--color-light-blue: color-mix(in oklch,lab(69.3174% -2.26048 -37.0102)70%,white);
--tw-ring-offset-width: 0px;
--color-border: lab(85.9644% -.138432 .510156);
--color-gray-200: lab(85.9644% -.138432 .510156);
--color-foreground: lab(8.244% 0 -.00000298023);
--color-blue: lab(69.3174% -2.26048 -37.0102);
--color-black: lab(0% 0 0);
--color-border-dark: lab(13.232% 0 0);
--playlist-accent-soft: color-mix(in oklch,lab(69.3174% -2.26048 -37.0102)70%,white);
--color-paper: lab(98.8967% -.385851 1.42193);
--color-note-surface: color-mix(in srgb,lab(94.2188% -1.42306 5.34524)40%,lab(98.8967% -.385851 1.42193));
--card-padding: 40px;
--color-blue-fill: lab(63.8315% -.601828 -46.527);
--color-paper-100: lab(94.2188% -1.42306 5.34524);
--color-off-black: lab(8.244% 0 -.00000298023);
```

### Spacing

```css
--text-lg--letter-spacing: .005em;
--text-3xl--letter-spacing: -.02em;
--text-xl--letter-spacing: -.015em;
--spacing: 1px;
--content-min-padding: 28px;
--text-2xl--letter-spacing: -.015em;
--spacing-vw: calc(1vw - 0px/100);
--text-base--letter-spacing: .01em;
--text-4xl--letter-spacing: -.02em;
--text-sm--letter-spacing: .015em;
--tw-space-y-reverse: 0;
--text-xs--letter-spacing: .015em;
```

### Typography

```css
--text-2xl: 40px;
--text-lg: 24px;
--text-2xl--line-height: 48px;
--text-base--line-height: 28px;
--font-weight-caption: 430;
--font-mono: "Paper Mono","SFMono-Regular",Menlo,ui-monospace,monospace;
--text-xl--line-height: 38px;
--font-weight-semibold: 550;
--text-sm: 16px;
--font-weight-semilight: 360;
--text-lg--line-height: 32px;
--playlist-text: lab(10.0558% .37308 -1.34099);
--text-4xl: 64px;
--font-weight-bold: 670;
--text-sm--line-height: 24px;
--text-3xl--line-height: 52px;
--text-3xl: 48px;
--text-xs--line-height: 20px;
--default-font-family: Matter,system-ui;
--font-weight-light: 270;
--text-xs: 14px;
--font-weight-normal: 400;
--font-weight-medium: 480;
--text-4xl--line-height: 68px;
--text-xl: 30px;
--text-base: 18px;
```

### Shadows

```css
--tw-inset-shadow-alpha: 100%;
--tw-drop-shadow-alpha: 100%;
--tw-inset-shadow: 0 0 #0000;
--tw-shadow-alpha: 100%;
--tw-shadow: 0 0 #0000;
```

### Other

```css
--device-pixel-ratio: 1;
--playlist-raised: lab(95.7192% .136256 -.51055);
--content-scale: .78;
--tw-outline-style: solid;
--lightningcss-dark: ;
--tw-translate-z: 0;
--content-max: 796px;
--tw-gradient-via: rgba(0, 0, 0, 0);
--tw-scale-y: 1;
--body-min-width: 375px;
--tw-translate-y: 0;
--grid-unit: 120px;
--hairline: 1px;
--container-content: min(round(down,max(375px,100*calc(1vw - 0px/100)),48px) - 28px*2,796px);
--tw-gradient-from: rgba(0, 0, 0, 0);
--tw-content: "";
--tw-gradient-to: rgba(0, 0, 0, 0);
--body-width: max(375px,100*calc(1vw - 0px/100));
--lightningcss-light: ;
--tw-divide-y-reverse: 0;
--tw-scale-z: 1;
--playlist-canvas: lab(90.1168% -.0000298023 0);
--tw-translate-x: 0;
--tw-gradient-via-position: 50%;
--deco-offset: -238px;
--content-min: round(down,max(375px,100*calc(1vw - 0px/100)),48px) - 28px*2;
--tw-scroll-snap-strictness: proximity;
--tw-scale-x: 1;
--tw-gradient-to-position: 100%;
--playlist-surface: lab(100% 0 0);
--tw-gradient-from-position: 0%;
--scrollbar-width: 0px;
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
| sm | 640px | min-width |
| md | 720px | min-width |
| 900px | 900px | min-width |
| 1140px | 1140px | min-width |
| 1471px | 1471px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.1s`, `0.15s`, `1s`, `0.3s`, `0.4s`, `0.55s`, `0.5s`, `0.8s`

### Common Transitions

```css
transition: all;
transition: background-color 0.1s, box-shadow 0.1s;
transition: opacity 0.1s;
transition: opacity 0.15s;
transition: color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to;
transition: colors 0.15s, transform 0.15s;
transition: transform 1s cubic-bezier(0.4, 0, 0, 1);
transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
transition: width 0.4s;
transition: opacity 0.4s, transform 0.4s;
```

### Keyframe Animations

**marquee**
```css
@keyframes marquee {
  0% { transform: translate(0px); }
  100% { transform: translateX(var(--marquee-offset)); }
}
```

**cursor-reveal**
```css
@keyframes cursor-reveal {
  0% { opacity: 0; scale: 0.5; }
  100% { opacity: 1; scale: 1; }
}
```

**cursor-exit**
```css
@keyframes cursor-exit {
  0% { opacity: 1; scale: 1; }
  100% { opacity: 0; scale: 0.5; }
}
```

**enter**
```css
@keyframes enter {
  0% { filter: blur(5px); opacity: 0; transform: translateY(8px); }
}
```

**terminal-chunk-in**
```css
@keyframes terminal-chunk-in {
  0% { opacity: 0; filter: blur(2px); transform: translateY(4px); }
  100% { opacity: 1; filter: blur(); transform: translateY(0px); }
}
```

**doc-video-playback**
```css
@keyframes doc-video-playback {
  0% { opacity: 0; scale: 0.8; }
  20% { opacity: 1; scale: 1; }
  80% { opacity: 1; scale: 1; }
  100% { opacity: 0; scale: 0.8; }
}
```

**index-module_cursor__PQg0P**
```css
@keyframes index-module_cursor__PQg0P {
  50% { opacity: 0; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (20 instances)

```css
.button {
  color: lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (61 instances)

```css
.card {
  background-color: rgb(249, 249, 249);
  border-radius: 5px;
  box-shadow: rgba(255, 255, 255, 0.533) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.533) 0px 0px 1px 1px inset, rgba(0, 0, 0, 0.067) 0px 0.5px 1px 0px, rgba(0, 0, 0, 0.133) 0px 0px 1px 0px, rgba(0, 0, 0, 0.133) 0px 0px 4px -1px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (45 instances)

```css
.link {
  color: lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
}
```

### Navigation (10 instances)

```css
.navigatio {
  color: lab(8.244 0 -0.00000298023);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
  box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 1px 0px 0px;
}
```

### Footer (30 instances)

```css
.foote {
  background-color: lab(98.8967 -0.385851 1.42193);
  color: lab(8.244 0 -0.00000298023);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 18px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 25 instances, 1 variant

**Variant 1** (25 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgba(0, 0, 0, 0.8);
  padding: 0px 0px 0px 0px;
  border-radius: 5px;
  border: 0px solid rgba(0, 0, 0, 0.8);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgba(0, 0, 0, 0.8);
  padding: 0px 0px 0px 0px;
  border-radius: 5px;
  border: 0px solid rgba(0, 0, 0, 0.8);
  font-size: 12px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: lab(8.244 0 -0.00000298023);
  padding: 40px 40px 40px 40px;
  border-radius: 0px;
  border: 0px solid lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: lab(8.244 0 -0.00000298023);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: lab(8.244 0 -0.00000298023);
  padding: 40px 40px 40px 40px;
  border-radius: 0px;
  border: 0px solid lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

### Button — 12 instances, 1 variant

**Variant 1** (12 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: lab(8.244 0 -0.00000298023);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

### Card — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: lab(8.244 0 -0.00000298023);
  padding: 40px 40px 40px 40px;
  border-radius: 0px;
  border: 0px solid lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: lab(8.244 0 -0.00000298023);
  padding: 40px 40px 40px 40px;
  border-radius: 0px;
  border: 0px solid lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: lab(98.8967 -0.385851 1.42193);
  color: lab(8.244 0 -0.00000298023);
  padding: 40px 40px 40px 40px;
  border-radius: 0px;
  border: 0px solid lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: lab(98.8967 -0.385851 1.42193);
  color: lab(8.244 0 -0.00000298023);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: lab(8.244 0 -0.00000298023);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none lab(8.244 0 -0.00000298023);
  font-size: 18px;
  font-weight: 400;
```

## Layout System

**5 grid containers** and **1427 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1080px | 0px |
| 100% | 0px |
| 422px | 0px |
| 427px | 0px |
| 1920px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 3x |
| 3-column | 2x |

### Grid Templates

```css
grid-template-columns: 540.5px 540.5px;
grid-template-columns: 112px 112px 16px;
gap: 8px;
grid-template-columns: 37.3281px 37.3281px 37.3281px;
grid-template-columns: 124px 124px;
gap: 8px;
grid-template-columns: 5px 5px;
gap: 2px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 1044x |
| column/nowrap | 383x |

**Gap values:** `10px`, `12px`, `154px`, `16px`, `18px`, `20px`, `24px`, `28px`, `2px`, `30px`, `32px`, `3px`, `40px`, `44px`, `4px`, `60px`, `6px`, `8px`, `9px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 86/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 65/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 78/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 8 font weights in use — consider standardizing to 3 (regular, medium, bold)
- 25 !important rules — prefer specificity over overrides
- 1057 duplicate CSS declarations

## Gradients

**6 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 90deg | 4 | bold |
| linear | — | 2 | brand |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |

```css
background: linear-gradient(90deg, lab(96.172 0 0) 33%, lab(88.168 0 0) 33%, lab(88.168 0 0) 67%, lab(99.304 -0.0000298023 0) 67%);
background: linear-gradient(oklch(0.776395 0.0894303 257.993), oklch(0.703994 0.126381 257.994));
background: linear-gradient(to right, lab(0 0 0) 1px, rgba(0, 0, 0, 0) 1px);
background: linear-gradient(lab(0 0 0) 1px, rgba(0, 0, 0, 0) 1px);
background: linear-gradient(to right, lab(94.2188 -1.42306 5.34524) 1px, rgba(0, 0, 0, 0) 1px);
```

## Z-Index Map

**9 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | div.r.e.l.a.t.i.v.e. .z.-.1.0. .w.-.f.u.l.l, div.r.e.l.a.t.i.v.e. .z.-.1.0. .h.-.f.u.l.l. .m.i.n.-.w.-.0. .f.l.e.x.-.1, div.r.e.l.a.t.i.v.e. .z.-.1.0. .p.b.-.[.0.p.x.]. .w.i.d.e.:.p.b.-.[.2.4.0.p.x.] |
| base | -1,5 | div.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .b.g.-.[.u.r.l.(.'./.l.a.y.o.u.t./.t.e.x.t.u.r.e...p.n.g.'.).]. .b.g.-.r.e.p.e.a.t. .o.p.a.c.i.t.y.-.5.0. .m.i.x.-.b.l.e.n.d.-.m.u.l.t.i.p.l.y. .d.a.r.k.:.o.p.a.c.i.t.y.-.3.0. .z.-.[.-.1.]. .m.i.n.-.[.8.8.0.p.x.].:.t.r.a.n.s.i.t.i.o.n.-.o.p.a.c.i.t.y. .m.i.n.-.[.8.8.0.p.x.].:.d.u.r.a.t.i.o.n.-.1.0.0. .m.i.n.-.[.8.8.0.p.x.].:.o.p.a.c.i.t.y.-.0, canvas, canvas |

## SVG Icons

**98 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 64 |
| sm | 14 |
| md | 17 |
| xl | 3 |

**Icon colors:** `currentColor`, `#81ACEC`, `var(--pui-workspace-mark)`, `rgb(0, 0, 0)`, `var(--pui-hairline)`, `var(--pui-mark)`, `var(--pui-icon)`, `var(--pui-icon-chevron)`, `var(--pui-icon-layer-fill)`, `var(--pui-icon-muted)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Matter | self-hosted | 400, normal | normal |
| Paper Mono | self-hosted | 400, normal | normal |
| Inter | self-hosted | 400, 500, 600 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 194 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| avatar | 4 | objectFit: cover, borderRadius: 3.35544e+07px, shape: circular |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (191x), 21:9 (3x), 3:2 (3x), 16:9 (2x), 1.98:1 (1x), 2.02:1 (1x), 3.03:1 (1x), 2.77:1 (1x)

## Motion Language

**Feel:** springy · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `800ms` | 800 |

### Easing Families

- **custom** (1 uses) — `cubic-bezier(0.4, 0, 0, 1)`
- **ease-out** (32 uses) — `cubic-bezier(0.16, 1, 0.3, 1)`
- **spring** (5 uses) — `cubic-bezier(0.34, 1.3, 0.64, 1)`
- **ease-in-out** (5 uses) — `ease`

### Spring / Overshoot Easings

- `cubic-bezier(0.34, 1.3, 0.64, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `terminal-chunk-in` | slide-y | opacity, filter, transform | 3 |

## Component Anatomy

### button — 43 instances

**Slots:** label, icon

### card — 18 instances

**Slots:** media

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** all-lowercase (balanced)

### Top CTA Verbs

- **team** (1)

### Button Copy Patterns

- "team@paper.design" (1×)

### Sample Headings

> design incredible
> the connected canvas for
teams shipping with agents
> Introducing Paper Desktop
a fully connected canvas,
a whole new workflow
> finally a continuous loop,
from Paper to code and back
> connect any agent to your canvas
> design incredible
> the connected canvas for
teams shipping with agents

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** Paper is a modern and powerful design tool that helps you create, share, and ship your best work.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → testimonial → testimonial → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | testimonial | design incredible | 0.8 |
| 2 | testimonial | design incredible | 0.8 |
| 3 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.226 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 6 |

## Imagery Style

**Label:** `mixed` (confidence 0.01)
**Counts:** total 204, svg 11, icon 93, screenshot-like 0, photo-like 4
**Dominant aspect:** square-ish
**Radius profile on images:** full

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: tailwindcss (0.3)

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
