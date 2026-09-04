# Design Language: PAYÁ • Film Haus

> Extracted from `https://paya.ar` on September 4, 2026
> 677 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#eaff62` | rgb(234, 255, 98) | hsl(68, 100%, 69%) | 486 |
| Secondary | `#377648` | rgb(55, 118, 72) | hsl(136, 36%, 34%) | 439 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 306 |

### Background Colors

Used on large-area elements: `#377648`

### Text Colors

Text color palette: `#000000`, `#eaff62`, `#377648`, `#367648`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#eaff62` | text, border | 486 |
| `#377648` | background, text, border | 439 |
| `#000000` | text, border | 306 |

## Typography

### Font Families

- **Annuario** — used for all (553 elements)
- **Times New Roman** — used for body (57 elements)
- **Tuppence** — used for body (4 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 18px | 1.125rem | 400 | 18px | 1.8px | a, h2, svg, path |
| 16px | 1rem | 400 | 16px | normal | html, head, meta, link |
| 14px | 0.875rem | 500 | 14px | 0.25px | span |
| 11px | 0.6875rem | 400 | 11px | normal | text, tspan |

### Heading Scale

```css
h2 { font-size: 18px; font-weight: 400; line-height: 18px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 500; line-height: 14px; }
```

### Font Weights in Use

`400` (598x), `700` (12x), `500` (4x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-192 | 192px | 12rem |
| spacing-272 | 272px | 17rem |
| spacing-483 | 483px | 30.1875rem |

## CSS Custom Properties

### Colors

```css
--wp-block-synced-color: #7a00df;
--wp-block-synced-color--rgb: 122,0,223;
--wp-bound-block-color: var(--wp-block-synced-color);
--wp-admin-theme-color: #007cba;
--wp-admin-theme-color--rgb: 0,124,186;
--wp-admin-theme-color-darker-10: #006ba1;
--wp-admin-theme-color-darker-10--rgb: 0,107,160.5;
--wp-admin-theme-color-darker-20: #005a87;
--wp-admin-theme-color-darker-20--rgb: 0,90,135;
--wp-admin-border-width-focus: 2px;
--wp--preset--color--black: #000000;
--wp--preset--color--cyan-bluish-gray: #abb8c3;
--wp--preset--color--white: #ffffff;
--wp--preset--color--pale-pink: #f78da7;
--wp--preset--color--vivid-red: #cf2e2e;
--wp--preset--color--luminous-vivid-orange: #ff6900;
--wp--preset--color--luminous-vivid-amber: #fcb900;
--wp--preset--color--light-green-cyan: #7bdcb5;
--wp--preset--color--vivid-green-cyan: #00d084;
--wp--preset--color--pale-cyan-blue: #8ed1fc;
--wp--preset--color--vivid-cyan-blue: #0693e3;
--wp--preset--color--vivid-purple: #9b51e0;
```

### Spacing

```css
--wp--preset--font-size--normal: 16px;
--wp--preset--font-size--huge: 42px;
--wp--preset--font-size--small: 13px;
--wp--preset--font-size--medium: 20px;
--wp--preset--font-size--large: 36px;
--wp--preset--font-size--x-large: 42px;
--wp--preset--spacing--20: 0.44rem;
--wp--preset--spacing--30: 0.67rem;
--wp--preset--spacing--40: 1rem;
--wp--preset--spacing--50: 1.5rem;
--wp--preset--spacing--60: 2.25rem;
--wp--preset--spacing--70: 3.38rem;
--wp--preset--spacing--80: 5.06rem;
--fg-carousel-navigation-size: 48px;
--fg-carousel-pagination-size: 14px;
--fg-carousel-progress-size: 4px;
```

### Shadows

```css
--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);
--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);
--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);
--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);
--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);
```

### Other

```css
--wp-editor-canvas-background: #ddd;
--wp--preset--aspect-ratio--square: 1;
--wp--preset--aspect-ratio--4-3: 4/3;
--wp--preset--aspect-ratio--3-4: 3/4;
--wp--preset--aspect-ratio--3-2: 3/2;
--wp--preset--aspect-ratio--2-3: 2/3;
--wp--preset--aspect-ratio--16-9: 16/9;
--wp--preset--aspect-ratio--9-16: 9/16;
--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);
--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);
--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);
--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);
--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);
--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);
--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);
--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);
--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);
--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);
--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);
--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);
--fg-carousel-perspective: 150px;
--fg-carousel-navigation-opacity: 0.3;
--fg-carousel-transition-speed: 650ms;
--fg-carousel-ui-speed: 300ms;
--amarillo: #EAFF62;
--verde: #377648;
--lila: #A983BF;
--blanco: #F9F5F1;
```

### Dependencies

```css
--wp-bound-block-color: --wp-block-synced-color;
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
| xs | 320px | max-width |
| sm | 480px | max-width |
| sm | 600px | max-width |
| sm | 601px | min-width |
| md | 720px | max-width |
| md | 782px | max-width |
| lg | 1024px | max-width |
| xl | 1280px | max-width |
| 2xl | 1600px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.5s`, `0.4s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: background-color 0.5s;
transition: transform 0.4s;
transition: 0.3s;
transition: 0.5s cubic-bezier(0.56, 0.56, 0.4, 1.13);
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**loading-default**
```css
@keyframes loading-default {
  0% { transform: translateX(-50%) translateY(-50%) rotate(0deg); }
  100% { transform: translateX(-50%) translateY(-50%) rotate(360deg); }
}
```

**loading-bars**
```css
@keyframes loading-bars {
  0%, 100%, 80% { box-shadow: 0px 0px; height: 3.2em; }
  40% { box-shadow: 0px -1.6em; height: 4em; }
}
```

**loading-trail-1**
```css
@keyframes loading-trail-1 {
  0% { box-shadow: 0px -3.32em 0px -1.6em, 0px -3.32em 0px -1.68em, 0px -3.32em 0px -1.76em, 0px -3.32em 0px -1.84em, 0px -3.32em 0px -1.908em; }
  5%, 95% { box-shadow: 0px -3.32em 0px -1.6em, 0px -3.32em 0px -1.68em, 0px -3.32em 0px -1.76em, 0px -3.32em 0px -1.84em, 0px -3.32em 0px -1.908em; }
  10%, 59% { box-shadow: 0px -3.32em 0px -1.6em, -0.348em -3.3em 0px -1.68em, -0.692em -3.248em 0px -1.76em, -1.024em -3.156em 0px -1.84em, -0.891em -3.1em 0px -1.908em; }
  20% { box-shadow: 0px -3.32em 0px -1.6em, -1.352em -3.032em 0px -1.68em, -2.2em -2.486em 0px -1.76em, -2.684em -1.952em 0px -1.84em, -2.996em -1.36em 0px -1.908em; }
  38% { box-shadow: 0px -3.32em 0px -1.6em, -1.508em -2.96em 0px -1.68em, -2.58em -2.088em 0px -1.76em, -3.1em -0.891em 0px -1.84em, -3.28em -0.36em 0px -1.908em; }
  100% { box-shadow: 0px -3.32em 0px -1.6em, 0px -3.32em 0px -1.68em, 0px -3.32em 0px -1.76em, 0px -3.32em 0px -1.84em, 0px -3.32em 0px -1.908em; }
}
```

**loading-trail-2**
```css
@keyframes loading-trail-2 {
  0% { transform: translateX(-50%) translateY(-50%) rotate(0deg); }
  100% { transform: translateX(-50%) translateY(-50%) rotate(360deg); }
}
```

**loading-pulse**
```css
@keyframes loading-pulse {
  0%, 100%, 80% { box-shadow: 0px 1.6em 0px -0.8em; }
  40% { box-shadow: 0px 1.6em 0px 0px; }
}
```

**loading-dots**
```css
@keyframes loading-dots {
  0%, 100% { box-shadow: 0px -2.4em 0px 0.16em, 1.6em -1.6em 0px 0px, 2.4em 0px 0px -0.8em, 1.6em 1.6em 0px -0.8em, 0px 2.4em 0px -0.8em, -1.6em 1.6em 0px -0.8em, -2.4em 0px 0px -0.8em, -1.6em -1.6em 0px 0px; }
  12.5% { box-shadow: 0px -2.4em 0px 0px, 1.6em -1.6em 0px 0.16em, 2.4em 0px 0px 0px, 1.6em 1.6em 0px -0.8em, 0px 2.4em 0px -0.8em, -1.6em 1.6em 0px -0.8em, -2.4em 0px 0px -0.8em, -1.6em -1.6em 0px -0.8em; }
  25% { box-shadow: 0px -2.4em 0px -0.4em, 1.6em -1.6em 0px 0px, 2.4em 0px 0px 0.16em, 1.6em 1.6em 0px 0px, 0px 2.4em 0px -0.8em, -1.6em 1.6em 0px -0.8em, -2.4em 0px 0px -0.8em, -1.6em -1.6em 0px -0.8em; }
  37.5% { box-shadow: 0px -2.4em 0px -0.8em, 1.6em -1.6em 0px -0.8em, 2.4em 0px 0px 0px, 1.6em 1.6em 0px 0.16em, 0px 2.4em 0px 0px, -1.6em 1.6em 0px -0.8em, -2.4em 0px 0px -0.8em, -1.6em -1.6em 0px -0.8em; }
  50% { box-shadow: 0px -2.4em 0px -0.8em, 1.6em -1.6em 0px -0.8em, 2.4em 0px 0px -0.8em, 1.6em 1.6em 0px 0px, 0px 2.4em 0px 0.16em, -1.6em 1.6em 0px 0px, -2.4em 0px 0px -0.8em, -1.6em -1.6em 0px -0.8em; }
  62.5% { box-shadow: 0px -2.4em 0px -0.8em, 1.6em -1.6em 0px -0.8em, 2.4em 0px 0px -0.8em, 1.6em 1.6em 0px -0.8em, 0px 2.4em 0px 0px, -1.6em 1.6em 0px 0.16em, -2.4em 0px 0px 0px, -1.6em -1.6em 0px -0.8em; }
  75% { box-shadow: 0px -2.4em 0px -0.8em, 1.6em -1.6em 0px -0.8em, 2.4em 0px 0px -0.8em, 1.6em 1.6em 0px -0.8em, 0px 2.4em 0px -0.8em, -1.6em 1.6em 0px 0px, -2.4em 0px 0px 0.16em, -1.6em -1.6em 0px 0px; }
  87.5% { box-shadow: 0px -2.4em 0px 0px, 1.6em -1.6em 0px -0.8em, 2.4em 0px 0px -0.8em, 1.6em 1.6em 0px -0.8em, 0px 2.4em 0px -0.8em, -1.6em 1.6em 0px 0px, -2.4em 0px 0px 0px, -1.6em -1.6em 0px 0.16em; }
}
```

**loading-partial**
```css
@keyframes loading-partial {
  0% { transform: translateX(-50%) translateY(-50%) rotate(0deg); }
  100% { transform: translateX(-50%) translateY(-50%) rotate(360deg); }
}
```

**button-loading**
```css
@keyframes button-loading {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**button-loading**
```css
@keyframes button-loading {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (8 instances)

```css
.button {
  color: rgba(0, 0, 0, 0.8);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Links (77 instances)

```css
.link {
  color: rgb(234, 255, 98);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (3 instances)

```css
.navigatio {
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(0, 0, 0);
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

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(234, 255, 98);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(234, 255, 98);
  font-size: 16px;
  font-weight: 400;
```

### Button — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgba(0, 0, 0, 0.8);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgba(0, 0, 0, 0.8);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**0 grid containers** and **13 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/wrap | 1x |
| row/nowrap | 12x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 87/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 125 !important rules — prefer specificity over overrides
- 96% of CSS is unused — consider purging
- 2782 duplicate CSS declarations

## Z-Index Map

**7 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 99999,99999 | div.l.o.a.d.i.n.g |
| dropdown | 100,100 | svg.s.m.a.l.l._.l.o.g.o, div.l.i.n.k. .l.i.n.k.-.s.e.r.v.i.c.i.o.s, div.l.i.n.k. .l.i.n.k.-.a.r.c.h.i.v.o |
| base | -999,8 | div.c.o.n.t.a.c.t.o, div.s.p.l.i.d.e._._.t.r.a.c.k. .s.p.l.i.d.e._._.t.r.a.c.k.-.-.l.o.o.p. .s.p.l.i.d.e._._.t.r.a.c.k.-.-.l.t.r. .s.p.l.i.d.e._._.t.r.a.c.k.-.-.d.r.a.g.g.a.b.l.e, img |

**Issues:**
- [object Object]

## SVG Icons

**6 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| lg | 2 |
| xl | 3 |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Inter | self-hosted | 100 900 | normal |
| Tuppence | self-hosted | 200 700 | normal |
| Annuario | self-hosted | 200 700 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 63 | objectFit: contain, borderRadius: 0px, shape: square |
| thumbnail | 3 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 1 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 4:3 (64x), 1:1 (2x), 3:2 (1x)

## Motion Language

**Feel:** springy · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **spring** (1 uses) — `cubic-bezier(0.56, 0.56, 0.4, 1.13)`

### Spring / Overshoot Easings

- `cubic-bezier(0.56, 0.56, 0.4, 1.13)`

## Component Anatomy

### button — 9 instances

**Slots:** label, icon
**Variants:** link

| variant | count | sample label |
|---|---|---|
| default | 8 |  |
| link | 1 | CONTACTO |

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **contacto** (1)

### Button Copy Patterns

- "contacto" (1×)

### Sample Headings

>  COBERTURA DEPORTIVA
>  REALIZACIÓN AUDIOVISUAL
>  EDICIÓN & ANIMACIÓN
>  CONTENIDO DIGITAL
>  COBERTURA DEPORTIVA
>  REALIZACIÓN AUDIOVISUAL
>  EDICIÓN & ANIMACIÓN
>  CONTENIDO DIGITAL

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Cobertura especializada en eventos y producción de contenidos junto a marcas globales.

## Section Roles

Reading order (top→bottom): nav → nav → content → content → hero → footer → hero → hero → hero

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | content |  COBERTURA DEPORTIVA | 0.3 |
| 3 | content | — | 0.3 |
| 4 | hero |  COBERTURA DEPORTIVA | 0.4 |
| 5 | hero |  REALIZACIÓN AUDIOVISUAL | 0.4 |
| 6 | hero |  EDICIÓN & ANIMACIÓN | 0.4 |
| 7 | hero |  CONTENIDO DIGITAL | 0.4 |
| 8 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.383 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.485)
**Counts:** total 67, svg 3, icon 3, screenshot-like 0, photo-like 63
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Annuario` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
