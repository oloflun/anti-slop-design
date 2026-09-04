# Design Language: HappyRobot | Powering the systems that run the world

> Extracted from `https://www.happyrobot.ai` on September 4, 2026
> 912 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#b8aea4` | rgb(184, 174, 164) | hsl(30, 12%, 68%) | 104 |
| Secondary | `#fdfcf4` | rgb(253, 252, 244) | hsl(53, 69%, 97%) | 87 |
| Accent | `#12100e` | rgb(18, 16, 14) | hsl(30, 13%, 6%) | 46 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#2d2928` | hsl(12, 6%, 17%) | 219 |
| `#000000` | hsl(0, 0%, 0%) | 91 |
| `#736f6a` | hsl(33, 4%, 43%) | 82 |
| `#ece8e3` | hsl(33, 19%, 91%) | 15 |

### Background Colors

Used on large-area elements: `#fdfcf4`, `#fcfcfc`, `#b8aea4`, `#ece8e3`

### Text Colors

Text color palette: `#000000`, `#0e0d0c`, `#ffffff`, `#1a1614`, `#12100e`, `#2d2928`, `#fdfcf4`, `#736f6a`, `#d59566`, `#ece8e3`

### Gradients

```css
background-image: linear-gradient(rgba(253, 252, 244, 0.96) 0%, rgba(253, 252, 244, 0.75) 100%);
```

```css
background-image: linear-gradient(rgba(18, 16, 14, 0.05) 40%, rgba(18, 16, 14, 0.88) 100%);
```

```css
background-image: linear-gradient(rgba(18, 16, 14, 0.1) 40%, rgba(18, 16, 14, 0.9) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#1a1614` | text, background | 427 |
| `#2d2928` | text, background | 219 |
| `#b8aea4` | border, background, text | 104 |
| `#000000` | text, background, border | 91 |
| `#fdfcf4` | background, text, border | 87 |
| `#736f6a` | text, background, border | 82 |
| `#12100e` | text, border, background | 46 |
| `#d59566` | background, text | 25 |
| `#ece8e3` | background, text | 15 |

## Typography

### Font Families

- **Suisse Intl** — used for all (897 elements)
- **Helvetica** — used for body (10 elements)
- **Tobias** — used for all (3 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 82px | 5.125rem | 400 | 77.08px | normal | h1 |
| 76px | 4.75rem | 400 | 71.44px | normal | h2, span |
| 46px | 2.875rem | 400 | 49.68px | -0.92px | h2, span |
| 40px | 2.5rem | 400 | 60px | 0.2px | div, span |
| 21px | 1.3125rem | 400 | 24.15px | normal | div, span, h3 |
| 20px | 1.25rem | 400 | 20px | -0.2px | span |
| 19px | 1.1875rem | 400 | 22.8px | normal | div |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, link |
| 15.5px | 0.9688rem | 400 | 25.575px | normal | p |
| 15px | 0.9375rem | 400 | 22.5px | 0.15px | span |
| 14.5px | 0.9063rem | 400 | 23.925px | normal | p |
| 14px | 0.875rem | 400 | 21px | normal | body, div, noscript, nav |
| 13.5px | 0.8438rem | 400 | 20.25px | 0.135px | span |
| 13px | 0.8125rem | 400 | 19.5px | 1.56px | div, button, span, svg |
| 12.5px | 0.7813rem | 400 | 17.1875px | normal | p |

### Heading Scale

```css
h1 { font-size: 82px; font-weight: 400; line-height: 77.08px; }
h2 { font-size: 76px; font-weight: 400; line-height: 71.44px; }
h2 { font-size: 46px; font-weight: 400; line-height: 49.68px; }
h3 { font-size: 21px; font-weight: 400; line-height: 24.15px; }
```

### Body Text

```css
body { font-size: 13px; font-weight: 400; line-height: 19.5px; }
```

### Font Weights in Use

`400` (906x), `700` (3x), `500` (1x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-40 | 40px | 2.5rem |
| spacing-44 | 44px | 2.75rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-61 | 61px | 3.8125rem |
| spacing-64 | 64px | 4rem |
| spacing-72 | 72px | 4.5rem |
| spacing-80 | 80px | 5rem |
| spacing-104 | 104px | 6.5rem |
| spacing-120 | 120px | 7.5rem |
| spacing-142 | 142px | 8.875rem |
| spacing-150 | 150px | 9.375rem |
| spacing-160 | 160px | 10rem |
| spacing-206 | 206px | 12.875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 3 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(184, 174, 164, 0.5) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px;
```

**xl** — blur: 35px
```css
box-shadow: rgba(0, 0, 0, 0.25) 0px 0px 35px 0px;
```

## CSS Custom Properties

### Colors

```css
--hr-muted-heading: #858484;
--hr-border-cta: #4a443c;
--hr-announce-bg: #1a1614;
--hr-cta-solid-bg: #fdfcf4;
--hr-accent: #b8aea4;
--foreground: #0a0a0a;
--card: #f2f3f7;
--card-foreground: #0a0a0a;
--popover: #fff;
--popover-foreground: #0a0a0a;
--primary: #171717;
--primary-foreground: #fafafa;
--secondary: #f5f5f5;
--secondary-foreground: #171717;
--muted: #f5f5f5;
--muted-foreground: #737373;
--accent: #f5f5f5;
--accent-foreground: #171717;
--destructive: #e40014;
--destructive-foreground: #e40014;
--border: #e5e5e5;
--ring: #a1a1a1;
--chart-1: #f05100;
--chart-2: #009588;
--chart-3: #104e64;
--chart-4: #fcbb00;
--chart-5: #f99c00;
--sidebar-foreground: #0a0a0a;
--sidebar-primary: #171717;
--sidebar-primary-foreground: #fafafa;
--sidebar-accent: #f5f5f5;
--sidebar-accent-foreground: #171717;
--sidebar-border: #e5e5e5;
--sidebar-ring: #a1a1a1;
--tw-ring-shadow: 0 0 #0000;
--tw-inset-ring-shadow: 0 0 #0000;
--tw-ring-offset-color: #fff;
--color-white: #fff;
--color-gray-100: lab(96.1596% -.0823438 -1.13575);
--color-red-500: lab(55.4814% 75.0732 48.8528);
--tw-ring-offset-width: 0px;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-border-style: solid;
--color-black: #000;
```

### Spacing

```css
--spacing: .25rem;
--tw-space-y-reverse: 0;
```

### Typography

```css
--text-2xl: 1.5rem;
--text-7xl: 4.5rem;
--text-lg: 1.125rem;
--font-body: "Suisse Intl", Arial, sans-serif;
--text-5xl--line-height: 1;
--text-base--line-height: calc(1.5 / 1);
--tracking-wider: .05em;
--font-mono: "GeistMono", ui-monospace, SFMono-Regular, Roboto Mono, Menlo, Monaco, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
--text-lg--line-height: calc(1.75 / 1.125);
--font-weight-bold: 700;
--font-sans: "Suisse Intl", Arial, sans-serif;
--text-6xl: 3.75rem;
--text-xs--line-height: calc(1 / .75);
--default-font-family: "Suisse Intl", Arial, sans-serif;
--font-weight-light: 300;
--font-geist-mono: "GeistMono", ui-monospace, SFMono-Regular, Roboto Mono, Menlo, Monaco, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
--text-7xl--line-height: 1;
--text-xl: 1.25rem;
--leading-relaxed: 1.625;
--leading-snug: 1.375;
--font-body-book: "Suisse Intl Book", "Suisse Intl", Arial, sans-serif;
--text-2xl--line-height: calc(2 / 1.5);
--tracking-wide: .025em;
--text-xl--line-height: calc(1.75 / 1.25);
--font-weight-semibold: 600;
--text-sm: .875rem;
--leading-tight: 1.25;
--text-4xl: 2.25rem;
--tracking-normal: 0em;
--font-geist-sans: "GeistSans", "GeistSans Fallback";
--text-sm--line-height: calc(1.25 / .875);
--text-3xl--line-height: calc(2.25 / 1.875);
--text-5xl: 3rem;
--text-xs: .75rem;
--text-3xl: 1.875rem;
--font-weight-medium: 500;
--font-weight-normal: 400;
--font-display: "Tobias", Georgia, serif;
--text-6xl--line-height: 1;
--text-4xl--line-height: calc(2.5 / 2.25);
--text-base: 1rem;
--default-mono-font-family: "GeistMono", ui-monospace, SFMono-Regular, Roboto Mono, Menlo, Monaco, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
--tracking-tight: -.025em;
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
--radius: .625rem;
--radius-3xl: 1.5rem;
```

### Other

```css
--hr-hull-white: #fcfcfc;
--hr-anchor-black: #0e0d0c;
--hr-rust: #d59566;
--hr-ocean-blue: #112b42;
--hr-dark-navy: #0a1929;
--hr-cargo-khaki: #ebe6d2;
--hr-deck-green: #a9c59d;
--hr-harbor-gray: #f2f2f2;
--hr-neutral: #cacaca;
--hr-neutral-light: #d9d9d9;
--hr-neutral-dark: #858585;
--hr-neutral-darker: #333;
--hr-sage: #dde8d8;
--hr-cta-green-from: #72ff88;
--hr-cta-green-to: #0abb2d;
--hr-cta-red-from: #ff6b6b;
--hr-cta-red-to: #d12a2a;
--hr-success-green: #027a48;
--hr-error-red: #b42318;
--hr-coal: #1a1614;
--hr-carbon: #2d2928;
--hr-stone: #b8aea4;
--hr-signal: #ece8e3;
--hr-lumen: #fdfcf4;
--hr-canvas: #12100e;
--hr-rust-deep: #b06a38;
--hr-line: #221f1c;
--hr-line-strong: #2a2623;
--hr-line-soft: #262220;
--hr-line-warm: #3a3531;
--hr-ink-1: #c7beb2;
--hr-ink-2: #b0a79c;
--hr-ink-3: #9c9288;
--hr-ink-4: #8f867b;
--hr-ink-5: #7e766b;
--hr-ink-6: #736f6a;
--hr-ink-7: #5f574d;
--hr-success: #5fa46b;
--hr-alert: #d9584b;
--hr-surface: #12100e;
--hr-surface-2: #12100e;
--hr-ink-strong: #fdfcf4;
--hr-cell: #1a1614;
--hr-nav-top: #12100ef0;
--hr-nav-bottom: #12100e9e;
--hr-wordmark: #fdfcf4;
--hr-cta-solid-fg: #12100e;
--background: var(--hr-lumen);
--input: #e5e5e5;
--sidebar: #fafafa;
--success: #76c7cc;
--warning: #ffd294;
--error: #ff847d;
--container-md: 28rem;
--aspect-video: 16 / 9;
--tw-animation-delay: 0s;
--tw-outline-style: solid;
--breakpoint-xl: 80rem;
--tw-animation-direction: normal;
--tw-enter-scale: 1;
--tw-divide-x-reverse: 0;
--tw-gradient-from: rgba(0, 0, 0, 0);
--breakpoint-2xl: 86rem;
--tw-gradient-to: rgba(0, 0, 0, 0);
--tw-exit-rotate: 0;
--tw-scale-z: 1;
--container-sm: 24rem;
--tw-exit-translate-y: 0;
--tw-gradient-via-position: 50%;
--tw-scroll-snap-strictness: proximity;
--container-lg: 32rem;
--tw-gradient-to-position: 100%;
--default-transition-duration: .15s;
--container-xs: 20rem;
--tw-gradient-from-position: 0%;
--default-transition-timing-function: cubic-bezier(.4, 0, .2, 1);
--tw-animation-iteration-count: 1;
--tw-exit-opacity: 1;
--tw-animation-fill-mode: none;
--container-5xl: 64rem;
--tw-exit-blur: 0;
--tw-translate-z: 0;
--tw-gradient-via: rgba(0, 0, 0, 0);
--tw-scale-y: 1;
--container-6xl: 72rem;
--breakpoint-lg: 64rem;
--tw-exit-translate-x: 0;
--container-3xl: 48rem;
--tw-translate-y: 0;
--ease-out: cubic-bezier(0, 0, .2, 1);
--tw-enter-translate-x: 0;
--container-4xl: 56rem;
--tw-divide-y-reverse: 0;
--breakpoint-md: 48rem;
--container-2xl: 42rem;
--tw-exit-scale: 1;
--tw-translate-x: 0;
--tw-enter-rotate: 0;
--tw-scale-x: 1;
--tw-enter-translate-y: 0;
--tw-enter-blur: 0;
--breakpoint-sm: 40rem;
--container-xl: 36rem;
--tw-enter-opacity: 1;
--blur-sm: 8px;
```

### Dependencies

```css
--background: --hr-lumen;
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
| sm | 584px | max-width |
| md | 736px | max-width |
| md | 767px | max-width |
| md | 768px | min-width |
| 928px | 928px | max-width |
| lg | 991px | max-width |
| lg | 1023px | max-width |
| lg | 1024px | min-width |
| 1120px | 1120px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.15s`, `0.35s`, `0.3s`, `0.2s`, `0.42s`, `0.28s`, `0.45s`, `0.6s`

### Common Transitions

```css
transition: all;
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.35s cubic-bezier(0.33, 0, 0.15, 1), color 0.35s cubic-bezier(0.33, 0, 0.15, 1);
transition: transform 0.3s cubic-bezier(0.33, 0, 0.15, 1), translate 0.3s cubic-bezier(0.33, 0, 0.15, 1), scale 0.3s cubic-bezier(0.33, 0, 0.15, 1), rotate 0.3s cubic-bezier(0.33, 0, 0.15, 1);
transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), translate 0.3s cubic-bezier(0.4, 0, 0.2, 1), scale 0.3s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), color 0.2s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.35s cubic-bezier(0.33, 0, 0.15, 1), translate 0.35s cubic-bezier(0.33, 0, 0.15, 1), scale 0.35s cubic-bezier(0.33, 0, 0.15, 1), rotate 0.35s cubic-bezier(0.33, 0, 0.15, 1);
transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: height 0.42s cubic-bezier(0.33, 0, 0.15, 1), opacity 0.42s cubic-bezier(0.33, 0, 0.15, 1);
transition: opacity 0.28s cubic-bezier(0.33, 0, 0.15, 1);
```

### Keyframe Animations

**hero-enter**
```css
@keyframes hero-enter {
  0% { opacity: 0; transform: translateY(16px); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**demoLogoMarquee**
```css
@keyframes demoLogoMarquee {
  0% { transform: translate(0px); }
  100% { transform: translate(-50%); }
}
```

**hr-blink**
```css
@keyframes hr-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.2; }
}
```

**hr-marquee**
```css
@keyframes hr-marquee {
  0% { transform: translate(0px); }
  100% { transform: translate(-50%); }
}
```

**hr-underline-sweep**
```css
@keyframes hr-underline-sweep {
  0% { transform-origin: 100% center; transform: scaleX(1); }
  49% { transform-origin: 100% center; transform: scaleX(0); }
  51% { transform-origin: 0px center; transform: scaleX(0); }
  100% { transform-origin: 0px center; transform: scaleX(1); }
}
```

**demoFadeIn**
```css
@keyframes demoFadeIn {
  0% { opacity: 0; transform: translateY(-5px); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**enter**
```css
@keyframes enter {
  0% { opacity: var(--tw-enter-opacity,1); transform: translate3d(var(--tw-enter-translate-x,0),var(--tw-enter-translate-y,0),0)scale3d(var(--tw-enter-scale,1),var(--tw-enter-scale,1),var(--tw-enter-scale,1))rotate(var(--tw-enter-rotate,0)); filter: blur(var(--tw-enter-blur,0)); }
}
```

**exit**
```css
@keyframes exit {
  100% { opacity: var(--tw-exit-opacity,1); transform: translate3d(var(--tw-exit-translate-x,0),var(--tw-exit-translate-y,0),0)scale3d(var(--tw-exit-scale,1),var(--tw-exit-scale,1),var(--tw-exit-scale,1))rotate(var(--tw-exit-rotate,0)); filter: blur(var(--tw-exit-blur,0)); }
}
```

**go2264125279**
```css
@keyframes go2264125279 {
  0% { transform: scale(0) rotate(45deg); opacity: 0; }
  100% { transform: scale(1) rotate(45deg); opacity: 1; }
}
```

**go3020080000**
```css
@keyframes go3020080000 {
  0% { transform: scale(0); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (14 instances)

```css
.button {
  background-color: rgb(14, 13, 12);
  color: rgb(45, 41, 40);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (1 instances)

```css
.card {
  background-color: rgb(252, 252, 252);
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 0px 35px 0px;
  padding-top: 18px;
  padding-right: 18px;
}
```

### Inputs (1 instances)

```css
.input {
  color: rgb(26, 22, 20);
  border-color: rgb(184, 174, 164);
  border-radius: 0px;
  font-size: 14px;
  padding-top: 13px;
  padding-right: 16px;
}
```

### Links (114 instances)

```css
.link {
  color: rgb(45, 41, 40);
  font-size: 13px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: rgb(26, 22, 20);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(236, 232, 227);
  color: rgb(115, 111, 106);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 14px;
}
```

### Modals (1 instances)

```css
.modal {
  background-color: rgb(252, 252, 252);
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 0px 35px 0px;
  padding-top: 18px;
  padding-right: 18px;
  max-width: 392px;
}
```

### Badges (8 instances)

```css
.badge {
  color: rgb(45, 41, 40);
  font-size: 11.5px;
  font-weight: 400;
  padding-top: 4px;
  padding-right: 10px;
  border-radius: 0px;
}
```

### Tooltips (4 instances)

```css
.tooltip {
  background-color: rgb(14, 13, 12);
  color: rgb(14, 13, 12);
  font-size: 12px;
  border-radius: 3px;
  padding-top: 0px;
  padding-right: 0px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 0px 35px 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(252, 252, 252);
  color: rgb(14, 13, 12);
  padding: 15px 0px 18px 0px;
  border-radius: 0px;
  border: 0px solid lab(90.952 0 -0.0000119209);
  font-size: 12px;
  font-weight: 400;
```

### Button — 3 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(14, 13, 12);
  padding: 0px 0px 0px 0px;
  border-radius: 3px;
  border: 1px solid rgb(14, 13, 12);
  font-size: 12px;
  font-weight: 700;
```

**Variant 2** (2 instances)

```css
  background: rgb(14, 13, 12);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 3px;
  border: 1px solid rgb(14, 13, 12);
  font-size: 12px;
  font-weight: 700;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(45, 41, 40);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid lab(90.952 0 -0.0000119209);
  font-size: 11px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(26, 22, 20);
  padding: 13px 16px 13px 16px;
  border-radius: 0px;
  border: 1px 0px 1px 1px solid rgb(184, 174, 164);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(26, 22, 20);
  color: rgb(253, 252, 244);
  padding: 13px 24px 13px 24px;
  border-radius: 0px;
  border: 0px solid lab(90.952 0 -0.0000119209);
  font-size: 12px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: oklab(0.174657 0.00201744 0.0048485 / 0.45);
  color: rgb(253, 252, 244);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 1px solid oklab(0.98964 -0.00193894 0.0104039 / 0.3);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(26, 22, 20);
  color: rgb(253, 252, 244);
  padding: 14px 24px 14px 24px;
  border-radius: 0px;
  border: 0px solid lab(90.952 0 -0.0000119209);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**20 grid containers** and **190 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1440px | 48px |
| 781.05px | 0px |
| 1155.43px | 0px |
| 100% | 0px |
| 420px | 0px |
| 900px | 0px |
| 520px | 0px |
| 772.16px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 8x |
| 4-column | 3x |
| 2-column | 3x |
| 3-column | 2x |
| 7-column | 1x |
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 507.234px 596.766px;
gap: 80px;
grid-template-columns: 319.25px 319.25px 319.25px 319.25px;
gap: 1px;
grid-template-columns: 700px 420px;
gap: 64px;
grid-template-columns: 168.281px 168.281px 168.281px 168.297px 168.281px 168.281px 168.297px;
gap: 1px;
grid-template-columns: 394px 394px 394px;
gap: 1px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 33x |
| row/nowrap | 145x |
| row/wrap | 12x |

**Gap values:** `10px`, `11px`, `12px`, `14px`, `16px`, `18px`, `1px`, `24px`, `28px`, `2px`, `32px`, `32px 40px`, `40px`, `48px`, `4px`, `56px`, `64px`, `6px`, `80px`, `8px`, `9px`, `normal 40px`, `normal 48px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 4 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#0e0d0c` | 19.42:1 | AAA |
| `#fdfcf4` | `#1a1614` | 17.46:1 | AAA |
| `#fdfcf4` | `#12100e` | 18.45:1 | AAA |

## Design System Score

**Overall: 94/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 12 !important rules — prefer specificity over overrides
- 1524 duplicate CSS declarations

## Gradients

**3 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |

```css
background: linear-gradient(rgba(253, 252, 244, 0.96) 0%, rgba(253, 252, 244, 0.75) 100%);
background: linear-gradient(rgba(18, 16, 14, 0.05) 40%, rgba(18, 16, 14, 0.88) 100%);
background: linear-gradient(rgba(18, 16, 14, 0.1) 40%, rgba(18, 16, 14, 0.9) 100%);
```

## Z-Index Map

**6 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 999999,999999 | div.t.e.r.m.l.y.-.s.t.y.l.e.s.-.r.o.o.t.-.b.0.a.e.b.b. .t.e.r.m.l.y.-.s.t.y.l.e.s.-.t.o.o.l.t.i.p.-.d.3.b.5.4.8. .t.e.r.m.l.y.-.s.t.y.l.e.s.-.c.o.m.p.a.c.t.-.a.f.2.a.7.f. .t.e.r.m.l.y.-.s.t.y.l.e.s.-.t.e.r.m.l.y.-.t.o.o.l.t.i.p.-.c.2.6.e.e.2. .t.e.r.m.l.y.-.s.t.y.l.e.s.-.b.o.t.t.o.m._.l.e.f.t.-.c.5.3.4.7.2. .t.-.c.o.n.s.e.n.t.P.r.o.m.p.t |
| sticky | 60,60 | div.f.i.x.e.d. .i.n.s.e.t.-.x.-.0. .t.o.p.-.0. .z.-.[.6.0.] |
| base | -1,4 | span.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .-.z.-.[.1.]. .o.r.i.g.i.n.-.b.o.t.t.o.m. .s.c.a.l.e.-.y.-.0. .b.g.-.[.#.B.8.A.E.A.4.]. .t.r.a.n.s.i.t.i.o.n.-.t.r.a.n.s.f.o.r.m. .d.u.r.a.t.i.o.n.-.[.3.5.0.m.s.]. .e.a.s.e.-.[.c.u.b.i.c.-.b.e.z.i.e.r.(.0...3.3.,.0.,.0...1.5.,.1.).]. .g.r.o.u.p.-.h.o.v.e.r.:.s.c.a.l.e.-.y.-.1.0.0, span.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .-.z.-.[.1.]. .o.r.i.g.i.n.-.b.o.t.t.o.m. .s.c.a.l.e.-.y.-.0. .b.g.-.[.#.B.8.A.E.A.4.]. .t.r.a.n.s.i.t.i.o.n.-.t.r.a.n.s.f.o.r.m. .d.u.r.a.t.i.o.n.-.[.3.5.0.m.s.]. .e.a.s.e.-.[.c.u.b.i.c.-.b.e.z.i.e.r.(.0...3.3.,.0.,.0...1.5.,.1.).]. .g.r.o.u.p.-.h.o.v.e.r.:.s.c.a.l.e.-.y.-.1.0.0, span.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .-.z.-.[.1.]. .o.r.i.g.i.n.-.b.o.t.t.o.m. .s.c.a.l.e.-.y.-.0. .b.g.-.[.#.B.8.A.E.A.4.]. .t.r.a.n.s.i.t.i.o.n.-.t.r.a.n.s.f.o.r.m. .d.u.r.a.t.i.o.n.-.[.3.5.0.m.s.]. .e.a.s.e.-.[.c.u.b.i.c.-.b.e.z.i.e.r.(.0...3.3.,.0.,.0...1.5.,.1.).]. .g.r.o.u.p.-.h.o.v.e.r.:.s.c.a.l.e.-.y.-.1.0.0 |

**Issues:**
- [object Object]

## SVG Icons

**6 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 3 |
| sm | 1 |
| xl | 2 |

**Icon colors:** `var(--hr-wordmark)`, `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| GeistMono | self-hosted | 100 900 | normal |
| GeistSans | self-hosted | 100 900 | normal |
| Tobias | self-hosted | 400 | normal |
| Suisse Intl | self-hosted | 400 | normal |
| Suisse Intl Book | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 25 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 23 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 2 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (27x), 21:9 (21x), 6.4:1 (1x), 4:3 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `sm` | `200ms` | 200 |
| `md` | `280ms` | 280 |
| `lg` | `420ms` | 420 |

### Easing Families

- **custom** (213 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`, `cubic-bezier(0.33, 0, 0.15, 1)`, `cubic-bezier(0.65, 0, 0.35, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `hero-enter` | slide-y | opacity, transform | 1 |
| `hr-blink` | fade | opacity | 1 |

## Component Anatomy

### button — 10 instances

**Slots:** label
**Variants:** primary · solid · outline
**Sizes:** sm

| variant | count | sample label |
|---|---|---|
| default | 3 | Inställningar
Avvisa
Acceptera |
| primary | 3 | Inställningar |
| outline | 3 | TALK TO A HAPPYROBOT |
| solid | 1 | BOOK A DEMO
→ |

## Brand Voice

**Tone:** friendly · **Pronoun:** we-only · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **inst** (2)
- **avvisa** (1)
- **acceptera** (1)
- **platform** (1)
- **solutions** (1)
- **book** (1)
- **talk** (1)

### Button Copy Patterns

- "inställningar
avvisa
acceptera" (1×)
- "inställningar" (1×)
- "avvisa" (1×)
- "acceptera" (1×)
- "platform" (1×)
- "solutions" (1×)
- "book a demo
→" (1×)
- "talk to a happyrobot" (1×)

### Sample Headings

> Achieving Enterprise Superintelligence
> The limit of what AI can do in your enterprise is not the model. It’s what the model knows about how your enterprise operates. That context is only captured one way: doing the work.
> Deployed in the real world
> Agents need a platform
> One system. Every vertical.
> Achieving Enterprise Superintelligence
> The limit of what AI can do in your enterprise is not the model. It’s what the model knows about how your enterprise operates. That context is only captured one way: doing the work.
> Deployed in the real world
> Agents need a platform
> One system. Every vertical.

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Autonomous AI workers that communicate, coordinate, and operate at scale across the real economy.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): testimonial → hero → nav → logo-wall → content → testimonials → content → testimonial → hero → content → content → cta → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | testimonial | Achieving Enterprise Superintelligence | 0.8 |
| 2 | hero | Achieving Enterprise Superintelligence | 0.85 |
| 3 | logo-wall | — | 0.85 |
| 4 | content | The limit of what AI can do in your enterprise is not the model. It’s what the m | 0.3 |
| 5 | testimonials | Deployed in the real world | 0.4 |
| 6 | content | Agents need a platform | 0.3 |
| 7 | testimonial | One system. Every vertical. | 0.8 |
| 8 | hero | This is Enterprise Superintelligence | 0.4 |
| 9 | content | We handle the work that matters most | 0.3 |
| 10 | content | Help build an entirely new way to work | 0.3 |
| 11 | cta | Put agents to work in complex environments | 0.75 |
| 12 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.15 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 3px |
| backdrop-filter in use | no |
| Gradients | 3 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.02)
**Counts:** total 50, svg 2, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.663)

Evidence:
- tailwind-like class density 65%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Suisse Intl` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
