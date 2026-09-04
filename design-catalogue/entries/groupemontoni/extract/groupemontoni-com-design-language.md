# Design Language: Accueil | Groupe Montoni

> Extracted from `https://groupemontoni.com` on September 4, 2026
> 616 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#008057` | rgb(0, 128, 87) | hsl(161, 100%, 25%) | 1 |
| Secondary | `#123f4e` | rgb(18, 63, 78) | hsl(195, 63%, 19%) | 5 |
| Accent | `#b99c6a` | rgb(185, 156, 106) | hsl(38, 36%, 57%) | 14 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 273 |
| `#0d0d0d` | hsl(0, 0%, 5%) | 70 |
| `#ffffff` | hsl(0, 0%, 100%) | 1 |
| `#81907a` | hsl(101, 9%, 52%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#0d0d0d`, `#000000`, `#efeee1`, `#008057`, `#123f4e`, `#81907a`

### Text Colors

Text color palette: `#000000`, `#0d0d0d`, `#efeee1`, `#123f4e`, `#b99c6a`

### Gradients

```css
background-image: linear-gradient(rgba(13, 13, 13, 0.1), rgba(13, 13, 13, 0.8));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#efeee1` | text, border, background | 852 |
| `#000000` | text, border, background | 273 |
| `#0d0d0d` | text, border, background | 70 |
| `#b99c6a` | text, border | 14 |
| `#123f4e` | text, border, background | 5 |
| `#ffffff` | background | 1 |
| `#008057` | background | 1 |
| `#81907a` | background | 1 |

## Typography

### Font Families

- **studiopro** — used for all (452 elements)
- **fkroman** — used for all (16 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 57.6px | 3.6rem | 500 | 63.36px | -1.152px | div |
| 25.6px | 1.6rem | 500 | 28.16px | -0.512px | h3, p |
| 20.8px | 1.3rem | 500 | 22.88px | -0.416px | h2, div, ul, li |
| 19.2px | 1.2rem | 400 | 28.8px | -0.256px | body, noscript, div, a |
| 16px | 1rem | 500 | 24px | -0.32px | div, p, input |
| 12.8px | 0.8rem | 400 | 12.8px | normal | span, p, div, svg |
| 11.2px | 0.7rem | 400 | 11.2px | normal | span, a, h3, p |
| 9.6px | 0.6rem | 600 | 9.6px | normal | span, div, a, iframe |
| 8px | 0.5rem | 400 | 12px | normal | html, head, meta, link |

### Heading Scale

```css
h3 { font-size: 25.6px; font-weight: 500; line-height: 28.16px; }
h2 { font-size: 20.8px; font-weight: 500; line-height: 22.88px; }
h1 { font-size: 19.2px; font-weight: 400; line-height: 28.8px; }
h2 { font-size: 12.8px; font-weight: 400; line-height: 12.8px; }
h3 { font-size: 11.2px; font-weight: 400; line-height: 11.2px; }
```

### Body Text

```css
body { font-size: 12.8px; font-weight: 400; line-height: 12.8px; }
```

### Font Weights in Use

`400` (516x), `600` (44x), `700` (27x), `500` (17x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-19 | 19px | 1.1875rem |
| spacing-26 | 26px | 1.625rem |
| spacing-32 | 32px | 2rem |
| spacing-38 | 38px | 2.375rem |
| spacing-61 | 61px | 3.8125rem |
| spacing-80 | 80px | 5rem |
| spacing-102 | 102px | 6.375rem |
| spacing-128 | 128px | 8rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 6px | 29 |
| full | 9999px | 2 |

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-bg-opacity: 1;
--tw-ring-inset: ;
--tw-ring-offset-width: 0px;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgba(59,130,246,.5);
--tw-ring-offset-color: #fff;
```

### Spacing

```css
--tw-numeric-spacing: ;
```

### Shadows

```css
--tw-shadow: 0 0 #0000;
--tw-drop-shadow: ;
```

### Other

```css
--viewport-desktop: 1600;
--factor-desktop: 1vw;
--viewport-mobile: 800;
--factor-mobile: 2vw;
--viewport: var(--viewport-mobile);
--factor: var(--factor-mobile);
--viewport-ratio: calc(1000/var(--viewport)*var(--factor));
--tw-contrast: ;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-backdrop-blur: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-backdrop-invert: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--motion-translateY: 0px;
--tw-gradient-to-position: ;
--tw-brightness: ;
--tw-numeric-fraction: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-skew-y: 0;
--tw-backdrop-brightness: ;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-rotate: 0;
--tw-pinch-zoom: ;
```

### Dependencies

```css
--viewport: --viewport-mobile;
--factor: --factor-mobile;
--viewport-ratio: --viewport,--factor;
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
| xs | 360px | min-width |
| sm | 430px | min-width |
| sm | 620px | min-width |
| md | 760px | min-width |
| md | 800px | min-width |
| 890px | 890px | min-width |
| 1120px | 1120px | min-width |
| 1360px | 1360px | min-width |
| 2xl | 1560px | min-width |
| 2xl | 1600px | min-width |
| 1920px | 1920px | min-width |
| 2048px | 2048px | min-width |
| 3840px | 3840px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.5s`, `0s`, `0.7s`, `0.15s`, `1s`

### Common Transitions

```css
transition: all;
transition: color 0.5s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), fill 0.5s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.5s cubic-bezier(0.4, 0, 0.2, 1);
transition: visibility 0s linear 0.7s;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 1s cubic-bezier(0.19, 1, 0.22, 1);
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

### Keyframe Animations

**svelte-9zvq9v-marquee**
```css
@keyframes svelte-9zvq9v-marquee {
  0% { transform: translate(0px); }
  100% { transform: translate(calc(-100% - var(--gap))); }
}
```

**svelte-9zvq9v-marqueeVertical**
```css
@keyframes svelte-9zvq9v-marqueeVertical {
  0% { transform: translateY(0px); }
  100% { transform: translateY(calc(-100% - var(--gap))); }
}
```

**svelte-wk5np-spin**
```css
@keyframes svelte-wk5np-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(359deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (6 instances)

```css
.button {
  color: rgb(239, 238, 225);
  font-size: 19.2px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (26 instances)

```css
.card {
  background-color: rgb(239, 238, 225);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (1 instances)

```css
.input {
  color: rgb(239, 238, 225);
  border-color: rgb(239, 238, 225);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (44 instances)

```css
.link {
  color: rgb(239, 238, 225);
  font-size: 19.2px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: rgb(239, 238, 225);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 25.6px;
  padding-right: 25.6px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(13, 13, 13);
  color: rgb(239, 238, 225);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 19.2px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 238, 225);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(239, 238, 225);
  font-size: 19.2px;
  font-weight: 400;
```

### Card — 19 instances, 3 variants

**Variant 1** (15 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 238, 225);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(239, 238, 225);
  font-size: 19.2px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgb(239, 238, 225);
  color: rgb(185, 156, 106);
  padding: 0px 0px 0px 0px;
  border-radius: 6.4px;
  border: 0px solid rgb(185, 156, 106);
  font-size: 19.2px;
  font-weight: 400;
```

**Variant 3** (2 instances)

```css
  background: rgb(0, 128, 87);
  color: rgb(239, 238, 225);
  padding: 0px 0px 0px 0px;
  border-radius: 6.4px;
  border: 0px solid rgb(239, 238, 225);
  font-size: 19.2px;
  font-weight: 400;
```

### Card — 3 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 238, 225);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(239, 238, 225);
  font-size: 19.2px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgb(239, 238, 225);
  color: rgb(13, 13, 13);
  padding: 12.8px 12.8px 12.8px 12.8px;
  border-radius: 6.4px;
  border: 0px solid rgb(13, 13, 13);
  font-size: 20.8px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 238, 225);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(239, 238, 225);
  font-size: 19.2px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 238, 225);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(239, 238, 225);
  font-size: 19.2px;
  font-weight: 400;
```

## Layout System

**32 grid containers** and **76 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 27x |
| 2-column | 3x |
| 3-column | 2x |

### Grid Templates

```css
grid-template-columns: 612.812px 612.812px;
gap: 3.2px;
grid-template-columns: 407.469px 407.484px 407.469px;
gap: 3.2px;
grid-template-columns: 1280px;
grid-template-columns: 1280px;
grid-template-columns: 793.625px 352px;
gap: 51.2px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 63x |
| column/nowrap | 13x |

**Gap values:** `12.8px`, `19.2px`, `25.6px`, `3.2px`, `38.4px`, `44.8px`, `48px`, `51.2px`, `6.4px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 2 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#123f4e` | `#efeee1` | 9.74:1 | AAA |

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 90/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 72 !important rules — prefer specificity over overrides
- 79% of CSS is unused — consider purging
- 943 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |

```css
background: linear-gradient(rgba(13, 13, 13, 0.1), rgba(13, 13, 13, 0.8));
```

## Z-Index Map

**4 unique z-index values** across 1 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | div.f.l.e.x. .f.l.e.x.-.c.o.l. .g.a.p.-.1.0.0. .p.x.-.4.0. .b.p.:.h.i.d.d.e.n. .s.v.e.l.t.e.-.w.5.o.2.o.k, div._.t.e.x.t.1. .h.i.d.d.e.n. .w.-.6.9.2. .s.e.l.f.-.c.e.n.t.e.r. .b.p.:.b.l.o.c.k. .s.v.e.l.t.e.-.w.5.o.2.o.k, div._.t.e.x.t.2. .h.i.d.d.e.n. .s.e.l.f.-.e.n.d. .p.b.-.3.2. .t.e.x.t.-.2.0. .b.p.:.b.l.o.c.k. .s.v.e.l.t.e.-.w.5.o.2.o.k |

## SVG Icons

**6 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 2 |
| sm | 3 |
| xl | 1 |

**Icon colors:** `currentColor`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| fkroman | self-hosted | 100 900 | normal |
| studiopro | self-hosted | 400, 500, 600, 700 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 2 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 2 | objectFit: cover, borderRadius: 6.4px, shape: rounded |

**Aspect ratios:** 3:4 (8x), 1:1 (2x), 2.56:1 (1x), 2:3 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **custom** (18 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **linear** (2 uses) — `linear`
- **ease-out** (5 uses) — `cubic-bezier(0.19, 1, 0.22, 1)`

## Component Anatomy

### card — 22 instances

**Slots:** media
**Sizes:** xl

### button — 6 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **menu** (1)
- **available** (1)
- **careers** (1)
- **submit** (1)

### Button Copy Patterns

- "menu" (1×)
- "available spaces
31" (1×)
- "careers
12" (1×)
- "submit" (1×)

### Sample Headings

> Groupe Montoni - Home
> Discover Quartier Molson
> Écoparc Laval 15
> Our ESG report 2023-2024
> Condos Industriels Châteauguay
> Discover Quartier Molson
> Écoparc Laval 15
> Our ESG report 2023-2024
> Condos Industriels Châteauguay
> Discover Quartier Molson

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Pioneer of sustainable buildings in Canada. Discover our LEED and BCZ (Zero Carbon Building) certified projects.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → content → content → content → content → content → hero → footer → sidebar

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | content | Groupe Montoni - Home | 0.3 |
| 3 | content | Discover Quartier Molson | 0.3 |
| 4 | content | Building today for the business of tomorrow | 0.3 |
| 5 | content | Building today for the business of tomorrow | 0.3 |
| 6 | content | Our people at the heart of our success | 0.3 |
| 7 | hero | Latest news and articles | 0.4 |
| 8 | footer | Join our mailing list | 0.95 |
| 9 | sidebar | Join our mailing list | 0.4 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.301 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 12, svg 0, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** portrait
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.672)

Evidence:
- tailwind-like class density 66%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `studiopro` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
