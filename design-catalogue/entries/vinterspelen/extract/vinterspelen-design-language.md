# Design Language: Vinterspelen på Vretaholm — operafestival i 1700-talsteatern

> Extracted from `http://127.0.0.1:3055/sites/vinterspelen.html` on September 8, 2026
> 455 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#290d00` | rgb(41, 13, 0) | hsl(19, 100%, 8%) | 7 |
| Secondary | `#b36b13` | rgb(179, 107, 19) | hsl(33, 81%, 39%) | 24 |
| Accent | `#d2c4a9` | rgb(210, 196, 169) | hsl(40, 31%, 74%) | 2 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 444 |
| `#050302` | hsl(20, 43%, 1%) | 180 |
| `#6c6557` | hsl(40, 11%, 38%) | 72 |
| `#b2a285` | hsl(39, 23%, 61%) | 1 |

### Background Colors

Used on large-area elements: `#010304`, `#000102`, `#d2c4a9`, `#010000`, `#b2a285`

### Text Colors

Text color palette: `#000000`, `#d5cbb8`, `#6c6557`, `#b36b13`, `#050302`, `#290d00`

### Gradients

```css
background-image: radial-gradient(120% 78% at 50% 62%, rgba(0, 0, 0, 0) 8%, rgba(9, 14, 16, 0.44) 52%, rgba(6, 10, 12, 0.9) 100%), linear-gradient(rgba(6, 10, 12, 0.86) 0%, rgba(6, 10, 12, 0.28) 24%, rgba(6, 10, 12, 0.3) 58%, rgba(6, 10, 12, 0.93) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 444 |
| `#d5cbb8` | text, background, border | 205 |
| `#050302` | text, background, border | 180 |
| `#6c6557` | text | 72 |
| `#b36b13` | text, border | 24 |
| `#290d00` | text, border | 7 |
| `#d2c4a9` | background | 2 |
| `#b2a285` | background | 1 |

## Typography

### Font Families

- **Newsreader** — used for body (366 elements)
- **Bodoni Moda** — used for all (76 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 101.12px | 6.32rem | 500 | 95.0528px | -1.41568px | h1, em |
| 81.92px | 5.12rem | 400 | 70.4512px | -1.6384px | p |
| 64px | 4rem | 500 | 63.36px | -0.896px | h2 |
| 44.8px | 2.8rem | 400 | 38.528px | -0.896px | p, span |
| 39.04px | 2.44rem | 500 | 41.3824px | -0.54656px | p, h3, em, a |
| 24.32px | 1.52rem | 500 | 28.2112px | -0.34048px | a, p, br, h3 |
| 23px | 1.4375rem | 500 | 23px | normal | span |
| 21px | 1.3125rem | 500 | 31.5px | -0.294px | span |
| 19px | 1.1875rem | 500 | 30.875px | -0.266px | p, br |
| 18px | 1.125rem | 400 | 27px | normal | body, script, noscript, header |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |
| 15.5px | 0.9688rem | 400 | 25.73px | normal | p, ul, li, span |
| 13px | 0.8125rem | 400 | 19.5px | 5.46px | p |
| 12.5px | 0.7813rem | 400 | 19.375px | normal | figcaption, p |
| 11.5px | 0.7188rem | 600 | 17.25px | 2.7025px | a, nav, p |

### Heading Scale

```css
h1 { font-size: 101.12px; font-weight: 500; line-height: 95.0528px; }
h2 { font-size: 64px; font-weight: 500; line-height: 63.36px; }
h3 { font-size: 39.04px; font-weight: 500; line-height: 41.3824px; }
h3 { font-size: 24.32px; font-weight: 500; line-height: 28.2112px; }
```

### Body Text

```css
body { font-size: 15.5px; font-weight: 400; line-height: 25.73px; }
```

### Font Weights in Use

`400` (331x), `600` (73x), `500` (51x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-56 | 56px | 3.5rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-112 | 112px | 7rem |
| spacing-121 | 121px | 7.5625rem |
| spacing-128 | 128px | 8rem |
| spacing-240 | 240px | 15rem |
| spacing-258 | 258px | 16.125rem |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: oklab(0.772 0.0129615 0.123321 / 0.42) 0px 0px 0px 1px;
```

**sm** — blur: 0px
```css
box-shadow: oklab(0.42 0.0327558 0.100812 / 0.45) 0px 0px 0px 1px;
```

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-border-spacing-x: 0;
--tw-ring-color: rgb(59 130 246 / 0.5);
--tw-ring-offset-color: #fff;
--tw-ring-offset-width: 0px;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
```

### Spacing

```css
--tw-numeric-spacing: ;
--tw-contain-size: ;
```

### Typography

```css
--font-titel: "Bodoni Moda",ui-serif,Georgia,serif;
--font-brod: Newsreader,ui-serif,Georgia,serif;
```

### Shadows

```css
--tw-drop-shadow: ;
--tw-shadow: 0 0 #0000;
```

### Other

```css
--sal: oklch(0.213 0.026 208);
--sal2: oklch(0.262 0.028 205);
--sal3: oklch(0.312 0.026 203);
--natt: oklch(0.128 0.016 60);
--papper: oklch(0.918 0.021 86);
--papper2: oklch(0.862 0.026 84);
--tryck: oklch(0.245 0.021 58);
--tryck2: oklch(0.392 0.019 56);
--kalk: oklch(0.928 0.014 84);
--kalk2: oklch(0.735 0.016 84);
--ockra: oklch(0.772 0.124 84);
--ockra-djup: oklch(0.420 0.106 72);
--karmin: oklch(0.487 0.146 26);
--ut: cubic-bezier(.16,1,.3,1);
--in: cubic-bezier(.7,0,.84,0);
--matt: 1480px;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-contain-style: ;
--tw-backdrop-invert: ;
--tw-brightness: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-backdrop-brightness: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-rotate: 0;
--tw-contrast: ;
--tw-skew-x: 0;
--tw-backdrop-blur: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-numeric-fraction: ;
--tw-skew-y: 0;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-pinch-zoom: ;
--tw-contain-paint: ;
--tw-contain-layout: ;
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
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 1024px | min-width |
| xl | 1280px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.15s`, `0.32s`, `0.12s`, `1.3s`, `0.35s`

### Common Transitions

```css
transition: all;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: background-color 0.32s cubic-bezier(0.16, 1, 0.3, 1), color 0.32s cubic-bezier(0.16, 1, 0.3, 1), transform 0.12s cubic-bezier(0.16, 1, 0.3, 1);
transition: opacity 1.3s cubic-bezier(0.16, 1, 0.3, 1), transform 1.3s cubic-bezier(0.16, 1, 0.3, 1);
transition: text-decoration-color 0.35s cubic-bezier(0.16, 1, 0.3, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Links (25 instances)

```css
.link {
  color: oklch(0.928 0.014 84);
  font-size: 11.5px;
  font-weight: 600;
}
```

### Navigation (20 instances)

```css
.navigatio {
  color: oklch(0.735 0.016 84);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 2px;
  padding-right: 2px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: oklch(0.213 0.026 208);
  color: oklch(0.928 0.014 84);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 18px;
}
```

## Layout System

**26 grid containers** and **41 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1480px | 32px |
| 736px | 0px |
| 992px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 23x |
| 3-column | 1x |
| 1-column | 1x |
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 48px 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 40px 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 48px 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 40px 32px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 40x |
| row/wrap | 1x |

**Gap values:** `12px 24px`, `16px`, `16px 32px`, `24px`, `24px 32px`, `32px`, `32px 24px`, `40px`, `40px 32px`, `48px 32px`, `8px normal`, `9.6px`, `normal 32px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 93/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 82/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 9 !important rules — prefer specificity over overrides
- 68% of CSS is unused — consider purging
- 117 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| radial | — | 4 | bold |
| linear | — | 4 | bold |

```css
background: radial-gradient(120% 78% at 50% 62%, rgba(0, 0, 0, 0) 8%, rgba(9, 14, 16, 0.44) 52%, rgba(6, 10, 12, 0.9) 100%);
background: linear-gradient(rgba(6, 10, 12, 0.86) 0%, rgba(6, 10, 12, 0.28) 24%, rgba(6, 10, 12, 0.3) 58%, rgba(6, 10, 12, 0.93) 100%);
```

## Z-Index Map

**2 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 40,40 | header.s.t.i.c.k.y. .t.o.p.-.0. .z.-.4.0. .b.g.-.s.a.l./.9.2. .b.a.c.k.d.r.o.p.-.b.l.u.r.-.m.d. .b.o.r.d.e.r.-.b. .b.o.r.d.e.r.-.k.a.l.k./.1.5 |
| base | 3,3 | div.s.c.e.n.-.t.e.x.t |

## SVG Icons

**1 unique SVG icons** detected. Dominant style: **duo-tone**.

| Size Class | Count |
|------------|-------|
| lg | 1 |

**Icon colors:** `oklch(0.772 0.124 84)`, `oklch(0.928 0.014 84)`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Bodoni Moda | google-fonts | 400, 400 700, 400 800, 700, 800 | italic, normal |
| Newsreader | google-fonts | 300, 300 600, 300 700, 600, 700 | italic, normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 6 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 4 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (4x), 4:3 (3x), 16:9 (1x), 9:16 (1x), 3:2 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `120ms` | 120 |
| `md` | `320ms` | 320 |
| `xxl` | `1.3s` | 1300 |

### Easing Families

- **custom** (5 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (74 uses) — `cubic-bezier(0.16, 1, 0.3, 1)`

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (balanced)

### Sample Headings

> Opera i en sal som aldrig fick elektriskt ljus.
> Vi restaurerar ingenting som fortfarande fungerar.
> Årets program, i den ordning de gavs.
> Orfeo ed Euridice
> Aeneas i Carthago
> Opera i en sal som aldrig fick elektriskt ljus.
> Vi restaurerar ingenting som fortfarande fungerar.
> Årets program, i den ordning de gavs.
> Orfeo ed Euridice
> Aeneas i Carthago

## Page Intent

**Type:** `unknown` (confidence 0)
**Description:** Vinterspelen spelar sjutton kvällar i januari i Vretaholms slottsteater från 1777. Originalmaskineri, salong lyst med vaxljus, orkester på tidstrogna instrument.

## Section Roles

Reading order (top→bottom): nav → nav → nav → content → content → content → content → content → content → steps → content → content → footer → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | content | Opera i en sal som aldrig fick elektriskt ljus. | 0.3 |
| 4 | content | Opera i en sal som aldrig fick elektriskt ljus. | 0.3 |
| 5 | content | Vi restaurerar ingenting som fortfarande fungerar. | 0.3 |
| 6 | content | Årets program, i den ordning de gavs. | 0.3 |
| 7 | content | Fyra par kulisser, en vev, sju sekunder. | 0.3 |
| 8 | content | Ett rum byggt kring det som står under golvet. | 0.3 |
| 9 | steps | Tvåhundrafjorton lågor, och ingenting bakom dem. | 0.75 |
| 10 | content | Parterren | 0.3 |
| 11 | content | Fjorton kilometer norr om Linköping. | 0.3 |
| 12 | footer | — | 0.95 |
| 13 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.412 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.6)
**Counts:** total 10, svg 0, icon 0, screenshot-like 0, photo-like 10
**Dominant aspect:** portrait
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.564)

Evidence:
- tailwind-like class density 57%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Newsreader` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
