# Design Language: Customer.io: AI-Powered Customer Engagement Platform

> Extracted from `https://customer.io` on September 4, 2026
> 1331 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fff8e9` | rgb(255, 248, 233) | hsl(41, 100%, 96%) | 16 |
| Secondary | `#01090b` | rgb(1, 9, 11) | hsl(192, 83%, 2%) | 1136 |
| Accent | `#c3e7ff` | rgb(195, 231, 255) | hsl(204, 100%, 88%) | 28 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#d4d4d4` | hsl(0, 0%, 83%) | 726 |
| `#ffffff` | hsl(0, 0%, 100%) | 336 |
| `#5a8990` | hsl(188, 23%, 46%) | 218 |
| `#f4f4f4` | hsl(0, 0%, 96%) | 5 |

### Background Colors

Used on large-area elements: `#000405`, `#ffffff`, `#f4f4f4`, `#d4d4d4`, `#000203`, `#01090b`, `#fadecf`, `#c3e7ff`

### Text Colors

Text color palette: `#000000`, `#000506`, `#01090b`, `#ffffff`, `#000405`, `#3d1e00`, `#280c83`, `#d42a09`, `#0127c9`, `#76052c`

### Gradients

```css
background-image: radial-gradient(circle, oklab(0.228 -0.0319411 -0.0166062 / 0.7) 1px, rgba(0, 0, 0, 0) 1px);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#01090b` | text, border, background | 1136 |
| `#d4d4d4` | border, background | 726 |
| `#ffffff` | background, text | 336 |
| `#5a8990` | text | 218 |
| `#3d1e00` | text | 73 |
| `#0e2b30` | text | 34 |
| `#fadecf` | background, border | 28 |
| `#c3e7ff` | background, border | 28 |
| `#3d0c03` | text, border | 27 |
| `#020b3f` | text, border | 27 |
| `#68ff6c` | text, border | 22 |
| `#7f4001` | text | 18 |
| `#fff8e9` | background | 16 |
| `#4ddc53` | text | 9 |
| `#d1fbcd` | background | 6 |
| `#f4f4f4` | background | 5 |
| `#9bc4c9` | text | 3 |
| `#280c83` | text | 1 |
| `#d42a09` | text | 1 |
| `#0127c9` | text | 1 |
| `#76052c` | text | 1 |
| `#c16301` | text | 1 |
| `#0d5c15` | text | 1 |
| `#791805` | background | 1 |
| `#021677` | background | 1 |

## Typography

### Font Families

- **saansFont** — used for all (1331 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 96px | 6rem | 475 | 96px | 0.2px | h1, br, span, div |
| 64px | 4rem | 475 | 64px | 0.2px | h2 |
| 40px | 2.5rem | 475 | 45px | 0.2px | p, span, h2, br |
| 36px | 2.25rem | 600 | 40.5px | 0.2px | p |
| 30px | 1.875rem | 475 | 33.75px | 0.2px | h3 |
| 24px | 1.5rem | 475 | 27px | 0.2px | h3, p |
| 20px | 1.25rem | 475 | 27.5px | 0.2px | p, h3 |
| 18px | 1.125rem | 475 | 24.75px | 0.2px | p, h3 |
| 16px | 1rem | 400 | 22px | normal | html, head, link, script |
| 14px | 0.875rem | 600 | 19.25px | 0.2px | a, span, p, strong |
| 12px | 0.75rem | 475 | 16.5px | 0.2px | ul, li, span, svg |
| 10px | 0.625rem | 500 | 13.75px | 0.2px | span |

### Heading Scale

```css
h1 { font-size: 96px; font-weight: 475; line-height: 96px; }
h2 { font-size: 64px; font-weight: 475; line-height: 64px; }
h2 { font-size: 40px; font-weight: 475; line-height: 45px; }
h3 { font-size: 30px; font-weight: 475; line-height: 33.75px; }
h3 { font-size: 24px; font-weight: 475; line-height: 27px; }
h3 { font-size: 20px; font-weight: 475; line-height: 27.5px; }
h3 { font-size: 18px; font-weight: 475; line-height: 24.75px; }
h3 { font-size: 16px; font-weight: 400; line-height: 22px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 600; line-height: 19.25px; }
```

### Font Weights in Use

`475` (1062x), `600` (149x), `400` (82x), `500` (34x), `700` (4x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-120 | 120px | 7.5rem |
| spacing-128 | 128px | 8rem |
| spacing-160 | 160px | 10rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 35 |
| md | 6px | 1 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: oklch(0.9263 0.136 145.2) 0px 0px 0px 4px;
```

**sm** — blur: 0px
```css
box-shadow: oklch(0.97 0 0) 0px 0px 0px 4px;
```

## CSS Custom Properties

### Colors

```css
--border: oklch(94% 0 0);
--color-wave-500: oklch(55.67% .201 258);
--color-cta-stroke-hover: oklch(24.5% .042 207.2);
--evergreen-muted: 187 60% 15%;
--accent-lime: 94 75% 50%;
--color-red-900: oklch(39.6% .141 25.723);
--color-neutral-600: oklch(43.9% 0 0);
--color-on-subtle: oklch(90% .024 204.8);
--accent-blue: 212 100% 50%;
--color-surface-inverse-subtle: oklch(30.68% .046 206.34);
--color-cta-flare-inverse: oklch(30.68% .046 206.34);
--color-stroke-strong: oklch(88.5% 0 0);
--tw-inset-ring-shadow: 0 0 #0000;
--color-cta-surface-hover: oklch(24.5% .042 207.2);
--color-verdant-600: oklch(63.5% .149 146.7);
--cta-border-hover: oklch(24.5% .042 207.2);
--color-gray-500: oklch(55.1% .027 264.364);
--color-charcoal-900: oklch(12% 0 0);
--color-green-500: oklch(72.3% .219 149.579);
--color-stroke-interactive-inverse-hover: oklch(92.63% .136 145.2);
--color-white: oklch(100% 0 0);
--color-surface-strong: oklch(97% 0 0);
--color-accent: oklch(51.57% .1045 80.95);
--color-wave-600: oklch(46.48% .17 260);
--pink-light-muted: 291 100% 96%;
--color-wave-700: oklch(37.29% .138 262);
--color-nova-200: oklch(80.88% .0891 296.36);
--color-verdant-300: oklch(92.63% .136 145.2);
--color-stroke-interactive-hover: oklch(88.5% 0 0);
--color-on-ink: oklch(100% 0 0);
--color-mustard-600: oklch(66.139% .13453 82.252);
--color-zest-500: oklch(68.37% .168 44.65);
--color-charcoal-25: oklch(98.5% 0 0);
--color-nova-50: oklch(88.55% .0327 297.76);
--color-mustard-700: oklch(51.57% .1045 80.95);
--color-charcoal-300: oklch(81% 0 0);
--color-charcoal-50: oklch(97% 0 0);
--accent: 163 75% 40%;
--color-stroke-subtle: oklch(97% 0 0);
--color-zest-600: oklch(56.75% .139 44);
--color-ink: oklch(24.5% .042 207.2);
--color-stroke-inverse-strong: oklch(42% .05 206.32);
--color-wave-50: oklch(95.8% .025 237.5);
--color-zest-200: oklch(87.44% .067 46.5);
--color-nova-600: oklch(42.05% .1781 295.36);
--color-highlight-mustard: oklch(76.37% .1548 83.03);
--color-verdant-200: oklch(94.7% .115 144.7);
--surface-accent: oklch(92.63% .136 145.2);
--color-charcoal-700: oklch(31.5% 0 0);
--color-charcoal-200: oklch(88.5% 0 0);
--foreground-light: 185 60% 20%;
--color-highlight-verdant: oklch(63.5% .149 146.7);
--aqua-dark-muted: 69 63% 13%;
--color-surface-accent: oklch(92.63% .136 145.2);
--cta-border: oklch(30.68% .046 206.34);
--fg-muted: color-mix(in oklab,oklch(22.8% .036 207.47),transparent 30%);
--yellow-light-muted: 50 100% 88%;
--color-stroke-inverse-accent: oklch(92.63% .136 145.2);
--color-surface: oklch(100% 0 0);
--color-gray-600: oklch(44.6% .03 256.802);
--tw-border-style: solid;
--color-surface-subtle: oklch(98.5% 0 0);
--color-red-600: oklch(57.7% .245 27.325);
--accent-teal: 183 71% 57%;
--color-link-on: oklch(100% 0 0);
--color-spruce-975: oklch(17.594% .02644 204.091);
--color-subtle: color-mix(in oklab,oklch(22.8% .036 207.47),transparent 20%);
--color-black: oklch(0% 0 0);
--color-stroke-inverse: oklch(30.68% .046 206.34);
--color-cta-stroke-inverse-hover: oklch(87.5% .144 145.6);
--ash-muted: 30 7% 95%;
--stroke-accent: oklch(92.63% .136 145.2);
--color-on-muted: oklch(79% .036 205.6);
--color-link-hover: oklch(24.5% .042 207.2);
--color-charcoal-500: oklch(60% 0 0);
--foreground-dark: 187 65% 10%;
--color-link-visited: oklch(30.68% .046 206.34);
--accent-gold: 38 89% 61%;
--color-link: oklch(22.8% .036 207.47);
--color-highlight-zest: oklch(68.37% .168 44.65);
--color-verdant-50: oklch(95.5% .06 143.4);
--tw-ring-shadow: 0 0 #0000;
--color-surface-inverse-strong: oklch(22.8% .036 207.47);
--color-wave-100: oklch(90% .05 240);
--color-link-on-hover: oklch(95.5% .016 203.8);
--color-red-200: oklch(88.5% .062 18.334);
--color-spruce-200: oklch(79% .036 205.6);
--fg-accent: oklch(51.57% .1045 80.95);
--color-spruce-700: oklch(30.68% .046 206.34);
--color-spruce-900: oklch(22.8% .036 207.47);
--color-surface-stronger: oklch(94% 0 0);
--color-highlight-nova: oklch(49.17% .1903 295.87);
--ring: 163 75% 40%;
--color-mustard-500: oklch(76.37% .1548 83.03);
--color-surface-inverse: oklch(24.5% .042 207.2);
--tw-ring-offset-color: #fff;
--color-highlight-wave: oklch(55.67% .201 258);
--color-red-400: oklch(70.4% .191 22.216);
--accent-raspberry: 331 88% 32%;
--color-spruce-500: oklch(52% .052 206.3);
--color-surface-inverse-stronger: oklch(19.478% .03329 205.326);
--color-red-800: oklch(44.4% .177 26.899);
--color-red-500: oklch(63.7% .237 25.331);
--color-stroke-inverse-subtle: oklch(24.5% .042 207.2);
--yellow-dark-muted: 18 15% 13%;
--tw-ring-offset-width: 0px;
--pink-dark-muted: 331 69% 14%;
--aqua-light-muted: 180 100% 89%;
--purple-light-muted: 237 100% 92%;
--color-wave-200: oklch(81% .086 244);
--color-mustard-25: oklch(99.11% .0098 85.85);
--color-zest-50: oklch(96.28% .017 50);
--color-cta-surface-inverse: oklch(92.63% .136 145.2);
--foreground-darker: 187 61% 5%;
--color-cta-stroke-inverse: oklch(92.63% .136 145.2);
--color-spruce-50: oklch(95.5% .016 203.8);
--color-nova-500: oklch(49.17% .1903 295.87);
--color-stroke-accent: oklch(92.63% .136 145.2);
--tw-ring-offset-shadow: 0 0 #0000;
--color-surface-inverse-accent: oklch(92.63% .136 145.2);
--color-verdant-400: oklch(87.5% .144 145.6);
--color-zest-700: oklch(45.14% .11 43);
--color-wave-900: oklch(18.91% .075 266);
--color-mustard-50: oklch(97.15% .0278 85.45);
--color-stroke: oklch(94% 0 0);
--color-cta-flare-subtle: oklch(97% 0 0);
--color-spruce-950: oklch(19.478% .03329 205.326);
--verdant-muted: 93 97% 93%;
--color-spruce-100: oklch(90% .024 204.8);
--color-spruce-800: oklch(24.5% .042 207.2);
--color-surface-brand: oklch(30.68% .046 206.34);
--color-on-accent: oklch(94.7% .115 144.7);
--color-link-on-visited: oklch(90% .024 204.8);
--color-muted: color-mix(in oklab,oklch(22.8% .036 207.47),transparent 30%);
--foreground-muted: 187 60% 15%;
--color-highlight-blush: oklch(52.38% .191 353.17);
--color-red-100: oklch(93.6% .032 17.717);
--purple-dark-muted: 259 63% 22%;
--accent-purple: 256 63% 53%;
--accent-orange: 18 98% 61%;
--color-verdant-25: oklch(97.5% .035 142.8);
--color-blush-500: oklch(52.38% .191 353.17);
--charcoal-muted: 0 0% 8%;
--color-nova-700: oklch(35.118% .15757 294.663);
--accent-emerald: 163 75% 40%;
--color-cta-flare: oklch(92.63% .136 145.2);
--color-charcoal-100: oklch(94% 0 0);
--color-blush-600: oklch(44.5% .18 352.7);
--color-cta-stroke: oklch(30.68% .046 206.34);
--foreground-lighter: 183 60% 28%;
--color-yellow-500: oklch(79.5% .184 86.047);
--color-verdant-500: oklch(75% .153 146.1);
--color-spruce-600: oklch(42% .05 206.32);
--color-cta-surface-inverse-hover: oklch(87.5% .144 145.6);
--color-cta-surface: oklch(30.68% .046 206.34);
--color-stroke-brand: oklch(30.68% .046 206.34);
--foreground: 187 69% 14%;
```

### Spacing

```css
--tw-space-x-reverse: 0;
--spacing: .25rem;
--spacing-post-hero: 100svh;
--spacing-header: 64px;
--tw-space-y-reverse: 0;
--spacing-toolbar: 64px;
--spacing-header-toolbar: calc(64px + 64px);
--spacing-announcement: 32px;
--spacing-18: 72px;
```

### Typography

```css
--text-base--line-height: 1.375;
--font-mono: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
--tracking-wider: .05em;
--text-9xl--line-height: 1.125;
--font-weight-bold: 700;
--text-xs--line-height: 1.375;
--text-7_5xl: 5rem;
--text-xl: 1.25rem;
--leading-heading: 1.125;
--leading-reading: 1.625;
--leading-relaxed: 1.625;
--leading-snug: 1.375;
--text-9xl: 8rem;
--text-2xl--line-height: 1.125;
--text-8xl: 6rem;
--text-sm: .875rem;
--text-underline-offset-3: 3px;
--text-xl--line-height: 1.375;
--leading-tight: 1.25;
--text-4xl--line-height: 1.125;
--tracking-tight: -.025em;
--text-2xl: 1.5rem;
--text-decoration-thickness-1_5: 1.5px;
--text-7xl: 4rem;
--text-lg: 1.125rem;
--text-8xl--line-height: 1.125;
--text-5xl--line-height: 1.125;
--leading-normal: 1.5;
--cta-text: oklch(100% 0 0);
--text-lg--line-height: 1.375;
--font-sans: ;
--leading-body: 1.375;
--text-6xl: 3.75rem;
--default-font-family: ;
--font-weight-light: 300;
--text-7_5xl--line-height: 1.125;
--text-7xl--line-height: 1.125;
--text-4_5xl: 2.5rem;
--tracking-wide: .025em;
--font-weight-semibold: 600;
--tracking-body: .0125em;
--leading-base: 1;
--text-4xl: 2.25rem;
--tracking-normal: 0em;
--text-sm--line-height: 1.375;
--text-3xl--line-height: 1.125;
--text-5xl: 3rem;
--text-3xl: 1.875rem;
--text-xs: .75rem;
--tracking-widest: .1em;
--font-weight-medium: 500;
--font-weight-normal: 475;
--text-6xl--line-height: 1.125;
--text-base: 1rem;
--default-mono-font-family: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
```

### Shadows

```css
--tw-inset-shadow-alpha: 100%;
--tw-inset-shadow: 0 0 #0000;
--tw-shadow-alpha: 100%;
--tw-drop-shadow-alpha: 100%;
--drop-shadow-xs: 0 1px 1px #0000000d;
--tw-shadow: 0 0 #0000;
```

### Radii

```css
--radius-sm: .25rem;
--radius-md: .375rem;
--radius-lg: .5rem;
--radius-xs: .125rem;
--radius-xl: .75rem;
```

### Other

```css
--container-md: 28rem;
--pink-dark-300: 331 43% 26%;
--aspect-video: 16/9;
--fg-subtle: color-mix(in oklab,oklch(22.8% .036 207.47),transparent 20%);
--evergreen-500: 187 69% 14%;
--blur-lg: 16px;
--charcoal-300: 0 1% 30%;
--link-visited: oklch(30.68% .046 206.34);
--ash-600: 30 13% 80%;
--verdant-700: 93 100% 84%;
--aqua-dark-400: 69 63% 16%;
--background-lighter: 118 94% 88%;
--aqua-dark-500: 69 63% 13%;
--tw-outline-style: solid;
--pink-dark-600: 331 68% 11%;
--link-hover: oklch(24.5% .042 207.2);
--aqua-light-400: 180 100% 93%;
--highlight: 118 94% 88%;
--link: oklch(22.8% .036 207.47);
--tw-gradient-from: rgba(0, 0, 0, 0);
--yellow-dark-400: 18 15% 17%;
--tw-gradient-to: rgba(0, 0, 0, 0);
--surface-strong: oklch(97% 0 0);
--yellow-dark-500: 18 15% 13%;
--black: 0 0% 0%;
--yellow-light-700: 50 88% 80%;
--purple-dark-700: 259 58% 14%;
--tw-gradient-via-position: 50%;
--container-site: 1320px;
--pink-light-500: 291 100% 96%;
--tw-gradient-to-position: 100%;
--charcoal-100: 0 1% 42%;
--stroke: oklch(94% 0 0);
--default-transition-duration: .2s;
--animate-pulse: pulse 2s cubic-bezier(.4,0,.6,1) infinite;
--purple-dark-400: 259 59% 26%;
--container-reading: 700px;
--surface: oklch(100% 0 0);
--purple-dark-600: 259 59% 18%;
--evergreen-200: 184 60% 24%;
--pink-dark-500: 331 69% 14%;
--aqua-light-600: 180 90% 84%;
--aqua-dark-700: 69 56% 7%;
--verdant-500: 118 94% 88%;
--surface-stronger: oklch(94% 0 0);
--yellow-dark-600: 18 14% 10%;
--yellow-dark-300: 18 14% 21%;
--charcoal-200: 0 1% 36%;
--default-transition-timing-function: cubic-bezier(0,0,.35,1);
--evergreen-300: 185 60% 20%;
--white: 0 0% 100%;
--surface-subtle: oklch(98.5% 0 0);
--background-dark: 30 13% 96%;
--charcoal-800: 0 0% 11%;
--background: 0 0% 100%;
--tw-translate-z: 0;
--aqua-light-700: 180 79% 79%;
--background-darker: 30 13% 93%;
--tw-gradient-via: rgba(0, 0, 0, 0);
--tw-scale-y: 1;
--container-6xl: 72rem;
--breakpoint-lg: 64rem;
--purple-light-300: 237 100% 98%;
--container-3xl: 48rem;
--blur-xs: 4px;
--tw-translate-y: 0;
--ease-out: cubic-bezier(0,0,.2,1);
--charcoal-600: 0 1% 18%;
--yellow-light-400: 50 100% 92%;
--tw-content: "";
--ash-700: 30 13% 75%;
--aqua-light-500: 180 100% 89%;
--pink-light-600: 291 80% 93%;
--purple-light-600: 237 100% 93%;
--tw-translate-x: 0;
--aqua-dark-600: 69 57% 10%;
--stroke-subtle: oklch(97% 0 0);
--purple-dark-300: 259 58% 30%;
--pink-dark-400: 331 49% 21%;
--stroke-strong: oklch(88.5% 0 0);
--stroke-brand: oklch(30.68% .046 206.34);
--ash-400: 30 13% 90%;
--cta-surface-hover: oklch(24.5% .042 207.2);
--yellow-light-500: 50 100% 88%;
--yellow-light-300: 50 100% 96%;
--cta-flare-subtle: oklch(97% 0 0);
--verdant-800: 93 100% 78%;
--pink-light-700: 291 61% 89%;
--breakpoint-xl: 80rem;
--verdant-100: 93 100% 98%;
--evergreen-400: 186 65% 17%;
--evergreen-100: 183 60% 28%;
--yellow-light-600: 50 93% 84%;
--verdant-300: 93 100% 94%;
--ash-100: 30 17% 98%;
--ash-900: 30 13% 65%;
--evergreen-900: 187 61% 5%;
--ash-300: 30 13% 93%;
--charcoal-500: 0 1% 22%;
--ash-800: 30 13% 70%;
--tw-scale-z: 1;
--container-sm: 24rem;
--yellow-dark-700: 18 11% 7%;
--purple-light-500: 237 100% 95%;
--tw-gradient-from-position: 0px;
--purple-light-700: 237 100% 91%;
--ease-in-out: cubic-bezier(.4,0,.2,1);
--evergreen-800: 187 63% 8%;
--charcoal-400: 0 1% 26%;
--verdant-600: 93 100% 86%;
--stroke-hover: oklch(88.5% 0 0);
--pink-light-400: 291 100% 97%;
--cta-surface: oklch(30.68% .046 206.34);
--verdant-200: 93 100% 96%;
--verdant-400: 93 100% 92%;
--charcoal-900: 0 0% 8%;
--background-light: 93 100% 94%;
--ease-in-fast: cubic-bezier(.19,1,.22,1);
--container-5xl: 64rem;
--fg: oklch(24.5% .042 207.2);
--purple-light-400: 237 100% 96%;
--pink-dark-700: 331 67% 8%;
--ease-out-fast: cubic-bezier(.19,1,.22,1);
--evergreen-600: 187 67% 12%;
--purple-dark-500: 259 63% 22%;
--verdant-900: 93 100% 74%;
--blur-md: 12px;
--container-4xl: 56rem;
--ash-200: 30 13% 96%;
--ash-500: 30 13% 85%;
--aqua-light-300: 180 100% 96%;
--pink-light-300: 291 100% 98%;
--charcoal-700: 0 0% 14%;
--container-2xl: 42rem;
--cta-flare: oklch(92.63% .136 145.2);
--input: 0 0% 0%;
--tw-scale-x: 1;
--aqua-dark-300: 69 63% 19%;
--evergreen-700: 187 65% 10%;
--blur-sm: 8px;
--charcoal-950: 0 0% 5%;
```

### Semantic

```css
success: [object Object];
warning: [object Object];
error: [object Object];
info: [object Object];
```

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.2s`, `0.4s`

### Common Transitions

```css
transition: all;
transition: 0.2s cubic-bezier(0.19, 1, 0.22, 1);
transition: cubic-bezier(0, 0, 0.35, 1);
transition: 0.2s cubic-bezier(0, 0, 0.35, 1);
transition: 0.2s cubic-bezier(0, 0, 0.2, 1);
transition: color 0.2s cubic-bezier(0, 0, 0.35, 1), background-color 0.2s cubic-bezier(0, 0, 0.35, 1), border-color 0.2s cubic-bezier(0, 0, 0.35, 1), outline-color 0.2s cubic-bezier(0, 0, 0.35, 1), text-decoration-color 0.2s cubic-bezier(0, 0, 0.35, 1), fill 0.2s cubic-bezier(0, 0, 0.35, 1), stroke 0.2s cubic-bezier(0, 0, 0.35, 1), --tw-gradient-from 0.2s cubic-bezier(0, 0, 0.35, 1), --tw-gradient-via 0.2s cubic-bezier(0, 0, 0.35, 1), --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.35, 1);
transition: transform 0.2s cubic-bezier(0, 0, 0.35, 1), translate 0.2s cubic-bezier(0, 0, 0.35, 1), scale 0.2s cubic-bezier(0, 0, 0.35, 1), rotate 0.2s cubic-bezier(0, 0, 0.35, 1);
transition: flex-grow 0.4s cubic-bezier(0, 0, 0.2, 1);
transition: opacity 0.2s cubic-bezier(0, 0, 0.35, 1);
transition: grid-template-rows 0.2s cubic-bezier(0, 0, 0.2, 1), opacity 0.2s cubic-bezier(0, 0, 0.2, 1);
```

### Keyframe Animations

**accordion-down**
```css
@keyframes accordion-down {
  0% { height: 0px; }
  100% { height: var(--radix-accordion-content-height); }
}
```

**accordion-up**
```css
@keyframes accordion-up {
  0% { height: var(--radix-accordion-content-height); }
  100% { height: 0px; }
}
```

**text-gradient**
```css
@keyframes text-gradient {
  0%, 100% { background-position: 0px 0px; background-size: 470% 200%; }
  50% { background-position: 100% 0px; background-size: 470% 200%; }
}
```

**gradient**
```css
@keyframes gradient {
  100% { background-position: var(--bg-size) 0; }
}
```

**meteor**
```css
@keyframes meteor {
  0% { opacity: 1; transform: rotate(215deg) translate(0px); }
  70% { opacity: 1; }
  100% { opacity: 0; transform: rotate(215deg) translate(-500px); }
}
```

**shine**
```css
@keyframes shine {
  0% { background-position: 0px 0px; }
  50% { background-position: 100% 100%; }
  100% { background-position: 0px 0px; }
}
```

**border-beam**
```css
@keyframes border-beam {
  100% { offset-distance: 100%; }
}
```

**spin**
```css
@keyframes spin {
  100% { transform: rotate(1turn); }
}
```

**pulse**
```css
@keyframes pulse {
  50% { opacity: 0.5; }
}
```

**scroll**
```css
@keyframes scroll {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-100%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (39 instances)

```css
.button {
  background-color: oklch(0.9911 0.0098 85.85);
  color: oklch(0.5157 0.1045 80.95);
  font-size: 16px;
  font-weight: 600;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 2px;
}
```

### Links (72 instances)

```css
.link {
  color: oklch(0.79 0.036 205.6);
  font-size: 16px;
  font-weight: 475;
}
```

### Navigation (7 instances)

```css
.navigatio {
  background-color: oklch(1 0 0);
  color: oklch(0.245 0.042 207.2);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 16px;
  padding-right: 8px;
  position: relative;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: oklch(0.19478 0.03329 205.326);
  color: oklch(1 0 0);
  padding-top: 64px;
  padding-bottom: 64px;
  font-size: 16px;
}
```

### Badges (16 instances)

```css
.badge {
  background-color: oklch(0.9911 0.0098 85.85);
  color: oklch(0.5157 0.1045 80.95);
  font-size: 12px;
  font-weight: 475;
  padding-top: 4px;
  padding-right: 8px;
  border-radius: 2px;
}
```

### Tabs (3 instances)

```css
.tab {
  color: oklab(0.228 -0.0319411 -0.0166062 / 0.7);
  font-size: 16px;
  font-weight: 500;
  padding-top: 16px;
  padding-right: 0px;
  border-color: oklch(0.94 0 0);
  border-radius: 0px;
}
```

### ProgressBars (3 instances)

```css
.progressBar {
  background-color: oklch(0.94 0 0);
  color: oklab(0.228 -0.0319411 -0.0166062 / 0.7);
  border-radius: 0px;
  font-size: 16px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 10 instances, 2 variants

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: oklch(0.245 0.042 207.2);
  padding: 0px 8px 0px 16px;
  border-radius: 0px;
  border: 0px solid oklch(0.94 0 0);
  font-size: 16px;
  font-weight: 600;
```

**Variant 2** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: oklch(1 0 0);
  padding: 0px 0px 0px 0px;
  border-radius: 3.35544e+07px;
  border: 0px solid oklch(0.94 0 0);
  font-size: 16px;
  font-weight: 600;
```

### Button — 16 instances, 1 variant

**Variant 1** (16 instances)

```css
  background: oklch(0.9911 0.0098 85.85);
  color: oklch(0.5157 0.1045 80.95);
  padding: 4px 8px 4px 8px;
  border-radius: 2px;
  border: 0px solid oklch(0.94 0 0);
  font-size: 12px;
  font-weight: 475;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: oklch(0.3068 0.046 206.34);
  color: oklch(1 0 0);
  padding: 0px 0px 0px 0px;
  border-radius: 3.35544e+07px;
  border: 0px solid oklch(0.3068 0.046 206.34);
  font-size: 16px;
  font-weight: 600;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: oklab(0.228 -0.0319411 -0.0166062 / 0.7);
  padding: 16px 0px 16px 0px;
  border-radius: 0px;
  border: 0px 0px 1px solid oklch(0.94 0 0);
  font-size: 16px;
  font-weight: 500;
```

## Layout System

**17 grid containers** and **427 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1320px | 32px |
| 100% | 0px |
| 975.84px | 0px |
| 1680px | 32px |
| 376px | 32px |
| 657.408px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 5x |
| 3-column | 4x |
| 12-column | 3x |
| 2-column | 3x |
| 5-column | 1x |
| 10-column | 1x |

### Grid Templates

```css
grid-template-columns: 1214px;
gap: 1px;
grid-template-columns: 576px 576px;
gap: 64px;
grid-template-columns: 606.5px 606.5px;
gap: 1px;
grid-template-columns: 606.5px 606.5px;
gap: 1px;
grid-template-columns: 121.594px 121.594px 121.594px 121.594px 121.594px 121.594px 121.594px 121.594px 121.594px 121.594px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 100x |
| row/nowrap | 326x |
| row-reverse/nowrap | 1x |

**Gap values:** `10px`, `12px`, `16px`, `1px`, `24px`, `32px`, `40px`, `48px`, `4px`, `5px`, `64px`, `80px`, `8px`, `96px`, `normal 10px`, `normal 40px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 5 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#68ff6c` | `#000203` | 15.95:1 | AAA |

## Design System Score

**Overall: 94/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 90/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 41 !important rules — prefer specificity over overrides
- 1648 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| radial | circle | 2 | brand |

```css
background: radial-gradient(circle, oklab(0.228 -0.0319411 -0.0166062 / 0.7) 1px, rgba(0, 0, 0, 0) 1px);
```

## Z-Index Map

**6 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | div.r.e.l.a.t.i.v.e. .z.-.1.0. .c.o.n.t.a.i.n.e.r, div.z.-.1.0. .f.l.e.x. .f.l.e.x.-.c.o.l. .g.a.p.-.2. .o.v.e.r.f.l.o.w.-.c.l.i.p, div.z.-.1.0. .f.l.e.x. .f.l.e.x.-.c.o.l. .g.a.p.-.2. .o.v.e.r.f.l.o.w.-.c.l.i.p |
| base | 0,3 | img.a.b.s.o.l.u.t.e. .z.-.0. .a.s.p.e.c.t.-.v.i.d.e.o. .o.b.j.e.c.t.-.c.o.v.e.r, img.z.-.0. .o.b.j.e.c.t.-.c.o.v.e.r, img.z.-.0. .o.b.j.e.c.t.-.c.o.v.e.r |

## SVG Icons

**18 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 5 |
| sm | 1 |
| md | 10 |
| lg | 1 |
| xl | 1 |

**Icon colors:** `currentColor`, `freeze`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| saansFont | self-hosted | 100 800 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 57 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 10 | objectFit: fill, borderRadius: 6px 6px 0px 0px, shape: rounded |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (13x), 4.17:1 (8x), 3.43:1 (8x), 16:9 (7x), 9:16 (5x), 4.35:1 (4x), 5.75:1 (4x), 3.92:1 (4x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `400ms` | 400 |

### Easing Families

- **ease-out** (184 uses) — `cubic-bezier(0.19, 1, 0.22, 1)`, `cubic-bezier(0, 0, 0.35, 1)`, `cubic-bezier(0, 0, 0.2, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `marquee` | slide-x | transform | 8 |
| `marquee` | slide-x | transform | 8 |

## Component Anatomy

### button — 34 instances

**Slots:** label, icon
**Variants:** outline
**Sizes:** xs · md · medium · sm

| variant | count | sample label |
|---|---|---|
| outline | 18 | Platform |
| default | 16 | case study |

## Brand Voice

**Tone:** neutral · **Pronoun:** you-only · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **case** (16)
- **platform** (1)
- **solutions** (1)
- **resources** (1)
- **build** (1)
- **get** (1)
- **discover** (1)

### Button Copy Patterns

- "case study" (16×)
- "platform" (1×)
- "solutions" (1×)
- "resources" (1×)
- "build automations in a conversation

go from a single prompt to a fully configured automation with triggers, content, timing, and logic, so you can launch more" (1×)
- "analyze performance instantly

ask how any campaign is doing and get clear, data-grounded recommendations." (1×)
- "find a smarter path to better outcomes

discover opportunities, validate them through real tests, and build on what performs best." (1×)

### Sample Headings

> More impact
from every 
p
u
s
h
> Intelligence that compounds
> Orchestration that scales
> Built for agents, not just humans
> Everything you need to
engage customers
> More impact
from every 
p
u
s
h
> Intelligence that compounds
> Orchestration that scales
> Built for agents, not just humans
> Everything you need to
engage customers

## Page Intent

**Type:** `landing` (confidence 0.27)
**Description:** Customer.io is a customer engagement platform for creating personalized journeys across email, push, SMS, and in-app messaging.

Alternates: docs (0.45), legal (0.4)

## Section Roles

Reading order (top→bottom): cta → nav → logo-wall → testimonials → pricing → pricing → content → logo-wall → testimonials → testimonials → testimonials → testimonials → testimonial → pricing → content → footer → feature-grid → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | cta | — | 0.75 |
| 1 | nav | — | 0.9 |
| 2 | pricing | More impact
from every 
p
u
s
h | 0.4 |
| 3 | pricing | More impact
from every 
p
u
s
h | 0.4 |
| 4 | logo-wall | — | 0.85 |
| 5 | content | — | 0.3 |
| 6 | logo-wall | — | 0.85 |
| 7 | testimonials | Intelligence that compounds | 0.4 |
| 8 | testimonials | Everything you need to
engage customers | 0.4 |
| 9 | testimonials | Support every stage of the
customer journey | 0.4 |
| 10 | testimonials | Infrastructure built for teams and the
agents that support them | 0.4 |
| 11 | testimonial | Trusted to power billions of
customer interactions | 0.8 |
| 12 | testimonials | Trusted to power billions of customer interactions | 0.4 |
| 13 | pricing | Optimize your messaging | 0.4 |
| 14 | content | — | 0.3 |
| 15 | footer | — | 0.95 |
| 16 | feature-grid | — | 0.8 |
| 17 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.627 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 6px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.019)
**Counts:** total 69, svg 48, icon 5, screenshot-like 0, photo-like 0
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: tailwindcss (0.3)

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `saansFont` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
