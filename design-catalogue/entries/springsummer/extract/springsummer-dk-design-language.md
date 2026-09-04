# Design Language: Spring/Summer | Copenhagen based digital first Design & Brand Agency

> Extracted from `https://springsummer.dk/` on September 4, 2026
> 1923 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fe3939` | rgb(254, 57, 57) | hsl(0, 99%, 61%) | 1792 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#ffffff` | hsl(0, 0%, 100%) | 1716 |
| `#000000` | hsl(0, 0%, 0%) | 208 |
| `#dedcd3` | hsl(49, 14%, 85%) | 106 |

### Background Colors

Used on large-area elements: `#dedcd3`

### Text Colors

Text color palette: `#000000`, `#fe3939`, `#ffffff`, `#dedcd3`

### Gradients

```css
background-image: linear-gradient(rgb(254, 57, 57), rgb(254, 57, 57));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#fe3939` | text, border, background | 1792 |
| `#ffffff` | text, border | 1716 |
| `#000000` | text, border | 208 |
| `#dedcd3` | background, text, border | 106 |

## Typography

### Font Families

- **Montreal** — used for body (1571 elements)
- **Supply** — used for all (331 elements)
- **Grotesk** — used for all (3 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 331.84px | 20.74rem | 400 | 248.946px | normal | h1 |
| 146.4px | 9.15rem | 400 | 111.264px | normal | p, h2 |
| 38.4px | 2.4rem | 400 | 42.24px | 0.768px | p |
| 25px | 1.5625rem | 400 | 35px | 0.5px | li, a |
| 20px | 1.25rem | 400 | normal | normal | html, head, meta, title |
| 18px | 1.125rem | 400 | 25.2px | 0.36px | li, a, p, br |
| 14px | 0.875rem | 400 | 21px | 0.28px | body, div, svg, style |
| 13.3333px | 0.8333rem | 400 | normal | normal | button, span, svg, defs |
| 12px | 0.75rem | 400 | 15.6px | 0.276px | header, div, a, span |
| 10px | 0.625rem | 400 | 12.6px | 0.1px | h3, p, div, a |

### Heading Scale

```css
h1 { font-size: 331.84px; font-weight: 400; line-height: 248.946px; }
h2 { font-size: 146.4px; font-weight: 400; line-height: 111.264px; }
h2 { font-size: 12px; font-weight: 400; line-height: 15.6px; }
h3 { font-size: 10px; font-weight: 400; line-height: 12.6px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: 15.6px; }
```

### Font Weights in Use

`400` (1905x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-18 | 18px | 1.125rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-50 | 50px | 3.125rem |
| spacing-60 | 60px | 3.75rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-150 | 150px | 9.375rem |
| spacing-250 | 250px | 15.625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 113 |
| full | 50px | 3 |

## CSS Custom Properties

### Colors

```css
--color-white: 0 0% 100%;
--color-black: 0 0% 0%;
--color-grey: 0 0% 21%;
--color-beige: 43 49% 90%;
--color-yellow: 56 100% 50%;
--swiper-theme-color: #007aff;
```

### Spacing

```css
--sidebar-margin: 1rem;
--grid-margin: 1rem;
--grid-gap: 1rem;
```

### Typography

```css
--font-weight: 400;
```

### Other

```css
--header-height: 2.6rem;
--sidebar-width: 100%;
--white: hsl(var(--color-white));
--black: hsl(var(--color-black));
--grey: hsl(var(--color-grey));
--beige: hsl(var(--color-beige));
--yellow: hsl(var(--color-yellow));
--grotesk: "Grotesk","Impact",sans-serif;
--montreal: "Montreal",sans-serif;
--supply: "Supply",monospace;
--noto: "Noto",sans-serif;
--display: var(--grotesk);
--sans-serif: var(--montreal);
--mono: var(--supply);
--chinese: var(--noto);
--grid-vw: calc((100vw - var(--sidebar-width) - var(--grid-margin))/100);
--ts-h1-exception-fs: calc(var(--grid-vw)*34);
--ts-h1-exception-lh: .78;
--ts-h1-exception-ls: -.01em;
--ts-h1-loader-fs: 40px;
--ts-h1-loader-lh: .75;
--ts-h1-fs: clamp(2.7rem,10.5vw,12.5rem);
--ts-h1-lh: .76;
--ts-h1-ls: -.01em;
--ts-h1-chinese-fs: clamp(1.5rem,14vw,7.5rem);
--ts-h1-chinese-lh: clamp(3rem,19vw,8.5rem);
--ts-h2-fs: clamp(3.5rem,10vw,7rem);
--ts-h2-lh: 1;
--ts-h2-ls: .02em;
--ts-h2-menu-mobile-fs: clamp(2rem,8vw,2.75rem);
--ts-h2-menu-mobile-lh: 100%;
--ts-h2-menu-mobile-ls: .02em;
--ts-body-xl-fs: clamp(1.5rem,3vw,2.5rem);
--ts-body-xl-lh: 1.1;
--ts-body-xl-ls: .02em;
--ts-body-menu-fs: clamp(1rem,2vw,1.25rem);
--ts-body-menu-lh: 1.4;
--ts-body-menu-ls: .02em;
--ts-body-l-fs: clamp(.85rem,2vw,.9rem);
--ts-body-l-lh: 1.38;
--ts-body-l-ls: .02em;
--ts-body-m-fs: .85rem;
--ts-body-m-lh: 1.38;
--ts-body-m-ls: .02em;
--ts-body-s-fs: .7rem;
--ts-body-s-lh: 1.15;
--ts-body-s-ls: .03em;
--ts-body-xs-fs: .7rem;
--ts-body-xs-lh: 1.15;
--ts-body-xs-ls: .03em;
--ts-number-fs: clamp(1rem,2vw,2rem);
--ts-number-lh: clamp(1.1rem,2.2vw,2.2rem);
--ts-number-ls: -.02em;
--ts-label-m-fs: .7rem;
--ts-label-m-lh: .91rem;
--ts-label-m-ls: 0;
--ts-label-s-fs: .6rem;
--ts-label-s-lh: .6rem;
--ts-label-s-ls: 0;
--ts-cta-fs: .6rem;
--ts-cta-lh: .826rem;
--ts-cta-ls: .01em;
--page-width: 1440px;
--grid-cols: 6;
--gutter: var(--grid-gap);
--col: (100vw - var(--grid-margin) * 2 - (var(--grid-cols) - 1) * var(--grid-gap)) /var(--grid-cols);
--cols: calc(var(--col) + var(--gutter));
--mt: 0px;
--mb: 0px;
--pt: 0px;
--pb: 0px;
--page-transition-speed: .45s;
--page-transition-speed-double: .9s;
--br: .2rem;
--ease-out: cubic-bezier(0,.55,.45,1);
--ease-in-out: cubic-bezier(.85,0,.15,1);
--theme-transition-duration: .4s;
--theme-transition-ease: ease-out;
--theme-transition: var(--theme-transition-duration) var(--theme-transition-ease);
--page-transition-duration: .4s;
```

### Dependencies

```css
--white: --color-white;
--black: --color-black;
--grey: --color-grey;
--beige: --color-beige;
--yellow: --color-yellow;
--display: --grotesk;
--sans-serif: --montreal;
--mono: --supply;
--chinese: --noto;
--grid-vw: --sidebar-width,--grid-margin;
--ts-h1-exception-fs: --grid-vw;
--gutter: --grid-gap;
--col: --grid-margin,--grid-cols,--grid-gap,--grid-cols;
--cols: --col,--gutter;
--theme-transition: --theme-transition-duration,--theme-transition-ease;
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
| 899px | 899px | max-width |
| 900px | 900px | min-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | min-width |
| 1399px | 1399px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.4s`, `0.25s`, `0.2s`, `1s`, `0.3s`, `0.5s`, `0.6s`, `0.8s`, `1.3s`

### Common Transitions

```css
transition: all;
transition: color 0.4s ease-out, background-color 0.4s ease-out;
transition: color 0.4s ease-out, background-color 0.4s ease-out, border 0.4s ease-out, transform 0.4s ease-out, opacity 0.4s ease-out;
transition: transform 0.25s ease-in-out;
transition: border-color 0.2s;
transition: scale 1s ease-out;
transition: opacity 0.3s;
transition: scale 0.5s ease-out;
transition: width 0.6s, height 0.6s, top 0.6s;
transition: background-color 0.4s ease-out;
```

### Keyframe Animations

**wave-animation**
```css
@keyframes wave-animation {
  0% { transform: rotate(0deg); }
  15% { transform: rotate(14deg); }
  30% { transform: rotate(-8deg); }
  40% { transform: rotate(14deg); }
  50% { transform: rotate(-4deg); }
  60% { transform: rotate(10deg); }
  70% { transform: rotate(0deg); }
  100% { transform: rotate(0deg); }
}
```

**shake**
```css
@keyframes shake {
  10%, 90% { transform: translate3d(-1px, 0px, 0px); }
  20%, 80% { transform: translate3d(2px, 0px, 0px); }
  30%, 50%, 70% { transform: translate3d(-4px, 0px, 0px); }
  40%, 60% { transform: translate3d(4px, 0px, 0px); }
}
```

**swiper-preloader-spin**
```css
@keyframes swiper-preloader-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

**sweep**
```css
@keyframes sweep {
  100% { transform: translate(min(0px,calc(var(--cols)*var(--grid-cols) - var(--gutter) - 100%))); }
}
```

**slide-enter**
```css
@keyframes slide-enter {
  0% { opacity: 0; transform: translateY(-50%); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**slide-leave**
```css
@keyframes slide-leave {
  0% { opacity: 1; transform: translateY(0px); }
  100% { opacity: 0; transform: translateY(50%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (8 instances)

```css
.button {
  color: rgb(254, 57, 57);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Inputs (1 instances)

```css
.input {
  color: rgb(254, 57, 57);
  border-color: rgba(254, 57, 57, 0.3);
  border-radius: 4px;
  font-size: 10px;
  padding-top: 8px;
  padding-right: 6px;
}
```

### Links (214 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 10px;
  font-weight: 400;
}
```

### Navigation (3 instances)

```css
.navigatio {
  color: rgb(254, 57, 57);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (2 instances)

```css
.foote {
  color: rgb(254, 57, 57);
  padding-top: 52px;
  padding-bottom: 30px;
  font-size: 12px;
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

### Dropdowns (46 instances)

```css
.dropdown {
  background-color: rgba(222, 220, 211, 0.75);
  border-radius: 0px;
  border-color: rgb(254, 57, 57);
  padding-top: 0px;
}
```

### Badges (137 instances)

```css
.badge {
  color: rgb(255, 255, 255);
  font-size: 10px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 3px;
}
```

### Accordions (6 instances)

```css
.accordion {
  color: rgb(254, 57, 57);
  font-size: 12px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(254, 57, 57);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(254, 57, 57);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(254, 57, 57);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(254, 57, 57);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(254, 57, 57);
  font-size: 13.3333px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(254, 57, 57);
  padding: 8px 6px 8px 6px;
  border-radius: 4px;
  border: 1px solid rgba(254, 57, 57, 0.3);
  font-size: 10px;
  font-weight: 400;
```

## Layout System

**19 grid containers** and **528 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 976px | 0px |
| 1280px | 0px |
| 644px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 13x |
| 2-column | 4x |
| 3-column | 1x |
| 6-column | 1x |

### Grid Templates

```css
grid-template-columns: 1280px;
gap: 20px;
grid-template-columns: 976px;
gap: 20px;
grid-template-columns: 478px 478px;
gap: 20px;
grid-template-columns: 976px;
gap: 20px;
grid-template-columns: 152.656px 152.672px 152.672px 152.656px 152.672px 152.672px;
gap: 12px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 37x |
| row/nowrap | 377x |
| row/wrap | 113x |
| column-reverse/nowrap | 1x |

**Gap values:** `10px`, `12px`, `14px`, `20px`, `20px 40px`, `30px 20px`, `40px`, `50px`, `54px`, `5px`, `6px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 91/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 16 !important rules — prefer specificity over overrides
- 73% of CSS is unused — consider purging
- 2377 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |

```css
background: linear-gradient(rgb(254, 57, 57), rgb(254, 57, 57));
```

## Z-Index Map

**6 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 10000,10000 | div.c.u.r.s.o.r.-.f.o.l.l.o.w.e.r |
| dropdown | 210,210 | div.w.i.d.g.e.t.-.e.l.e.m.e.n.t, div.w.i.d.g.e.t.-.e.l.e.m.e.n.t, div.w.i.d.g.e.t.-.e.l.e.m.e.n.t |
| sticky | 20,25 | header.h.e.a.d.e.r. .t.s.-.b.o.d.y.-.s, div.b.a.c.k.d.r.o.p, div.w.i.d.g.e.t.-.b.a.r |
| base | 1,2 | div.f.o.r.e.g.r.o.u.n.d, a.r.o.u.t.e.r.-.l.i.n.k.-.a.c.t.i.v.e. .r.o.u.t.e.r.-.l.i.n.k.-.e.x.a.c.t.-.a.c.t.i.v.e. .h.o.m.e.-.l.i.n.k, button.m.o.b.i.l.e.-.m.e.n.u.-.t.r.i.g.g.e.r. .t.s.-.c.t.a |

**Issues:**
- [object Object]

## SVG Icons

**25 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 6 |
| md | 1 |
| xl | 18 |

**Icon colors:** `currentColor`, `var(--fill, white)`, `rgb(254, 57, 57)`, `rgb(0, 0, 0)`, `#0A0605`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Grotesk | self-hosted | 400, normal | normal |
| Montreal | self-hosted | 400, normal | normal |
| Supply | self-hosted | 400, normal | normal |
| Noto | self-hosted | 400, normal | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 28 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 4 | objectFit: contain, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (29x), 1:1 (2x), 4:3 (1x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `800ms` | 800 |
| `xxl` | `1.3s` | 1300 |

### Easing Families

- **ease-in-out** (186 uses) — `ease`
- **ease-out** (1 uses) — `cubic-bezier(0, 0.55, 0.45, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `sweep` | slide | transform | 1 |

## Component Anatomy

### button — 7 instances

**Slots:** label
**Variants:** link

| variant | count | sample label |
|---|---|---|
| default | 4 | .cls-1 {
        fill: #fff;
      } |
| link | 3 | What we do |

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **cls** (2)
- **what** (1)
- **our** (1)
- **about** (1)

### Button Copy Patterns

- ".cls-1 {
        fill: #fff;
      }" (2×)
- "what we do" (1×)
- "our work" (1×)
- "about us" (1×)

### Sample Headings

> Areas of expertise
> Technologies
> Have you seen
> Industries we help
> Platforms
> Areas of expertise
> Technologies
> Have you seen
> Industries we help
> Platforms

## Page Intent

**Type:** `landing` (confidence 0.59)
**Description:** Strategic digital experiences & brand identities from Copenhagen, Scandinavian design meets innovative technology.

Alternates: legal (0.4)

## Section Roles

Reading order (top→bottom): nav → nav → sidebar → sidebar → nav → content → hero → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | Areas of expertise | 0.4 |
| 1 | nav | Areas of expertise | 0.9 |
| 2 | sidebar | — | 0.4 |
| 3 | nav | — | 0.4 |
| 4 | sidebar | — | 0.4 |
| 5 | content | WE WON | 0.3 |
| 6 | hero | WE WON | 0.85 |
| 7 | footer | Contact us | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.206 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `photography` (confidence 0.573)
**Counts:** total 32, svg 0, icon 0, screenshot-like 0, photo-like 30
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Montreal` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
