# Design Language: Modern Business Intelligence | Better data, better decisions

> Extracted from `https://mode.com` on September 4, 2026
> 2727 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#c8f169` | rgb(200, 241, 105) | hsl(78, 83%, 68%) | 86 |
| Secondary | `#043f2e` | rgb(4, 63, 46) | hsl(163, 88%, 13%) | 1291 |
| Accent | `#1863dc` | rgb(24, 99, 220) | hsl(217, 80%, 48%) | 13 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1846 |
| `#212121` | hsl(0, 0%, 13%) | 1737 |
| `#fcfcfc` | hsl(0, 0%, 99%) | 129 |
| `#f4f4f4` | hsl(0, 0%, 96%) | 21 |
| `#d0d5d2` | hsl(144, 6%, 83%) | 5 |

### Background Colors

Used on large-area elements: `#ffffff`, `#c8f169`, `#043f2e`, `#eef2e3`, `#2a6f2b`, `#78c51c`, `#1f1f1f`

### Text Colors

Text color palette: `#000000`, `#212121`, `#1863dc`, `#ffffff`, `#008000`, `#293c5b`, `#043f2e`, `#c8f169`, `#2a6f2b`, `#eef2e3`

### Gradients

```css
background-image: linear-gradient(rgba(255, 255, 255, 0) 0%, rgb(255, 255, 255) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 1846 |
| `#212121` | text, border, background | 1737 |
| `#043f2e` | text, border, background | 1291 |
| `#eef2e3` | border, background, text | 395 |
| `#fcfcfc` | background, text, border | 129 |
| `#c8f169` | background, text, border | 86 |
| `#2a6f2b` | text, border, background | 38 |
| `#f4f4f4` | border, background | 21 |
| `#1863dc` | text, border, background | 13 |
| `#293c5b` | text, border | 6 |
| `#78c51c` | background, text, border | 6 |
| `#d0d5d2` | background | 5 |
| `#008000` | text, border | 2 |
| `#0056a7` | background | 1 |
| `#cecafa` | background | 1 |
| `#bbd1fb` | background | 1 |
| `#ffbbbe` | background | 1 |

## Typography

### Font Families

- **Times New Roman** — used for body (2033 elements)
- **Grenette** — used for all (366 elements)
- **Graphik** — used for body (319 elements)
- **--fonts-sans** — used for body (9 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 153.6px | 9.6rem | 400 | 153.6px | -3.072px | h1, div |
| 96px | 6rem | 400 | 86.4px | -1.92px | h1, div |
| 72px | 4.5rem | 400 | 79.2px | -1.44px | h2 |
| 70px | 4.375rem | 400 | 77px | -2.1px | p |
| 56px | 3.5rem | 400 | 67.2px | -1.12px | p, h2 |
| 36px | 2.25rem | 400 | 37.08px | -0.36px | p, h2 |
| 24px | 1.5rem | 500 | 28.8px | 0% | button, span, div, a |
| 22px | 1.375rem | 400 | 26.84px | -3% | h5, div |
| 18px | 1.125rem | 700 | 24px | normal | p, span, button, div |
| 16px | 1rem | 400 | normal | normal | html, head, meta, style |
| 14px | 0.875rem | 400 | 24px | normal | div, p, button, span |
| 12px | 0.75rem | 400 | 24px | normal | ul, li, div, a |

### Heading Scale

```css
h1 { font-size: 153.6px; font-weight: 400; line-height: 153.6px; }
h1 { font-size: 96px; font-weight: 400; line-height: 86.4px; }
h2 { font-size: 72px; font-weight: 400; line-height: 79.2px; }
h2 { font-size: 56px; font-weight: 400; line-height: 67.2px; }
h2 { font-size: 36px; font-weight: 400; line-height: 37.08px; }
h5 { font-size: 22px; font-weight: 400; line-height: 26.84px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: 24px; }
```

### Font Weights in Use

`400` (2296x), `600` (238x), `500` (185x), `700` (8x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-8 | 8px | 0.5rem |
| spacing-36 | 36px | 2.25rem |
| spacing-40 | 40px | 2.5rem |
| spacing-50 | 50px | 3.125rem |
| spacing-55 | 55px | 3.4375rem |
| spacing-60 | 60px | 3.75rem |
| spacing-90 | 90px | 5.625rem |
| spacing-100 | 100px | 6.25rem |
| spacing-120 | 120px | 7.5rem |
| spacing-130 | 130px | 8.125rem |
| spacing-200 | 200px | 12.5rem |
| spacing-240 | 240px | 15rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 6 |
| sm | 5px | 5 |
| md | 8px | 4 |
| lg | 16px | 43 |
| full | 50px | 6 |

## Box Shadows

**md** — blur: 10px
```css
box-shadow: rgba(172, 171, 171, 0.3) 0px -1px 10px 0px;
```

**xl** — blur: 68px
```css
box-shadow: rgba(0, 0, 0, 0.3) 0px 32px 68px 0px;
```

## CSS Custom Properties

### Colors

```css
--colors-g2: #C8F169;
--colors-b2: #7EA6F3;
--colors-gray7: #80827D;
--colors-gray3: #E7E7E6;
--colors-g4: #2A6F2B;
--colors-p3: #6A4BC5;
--colors-g3: #78C51C;
--colors-gray6: #B7B8B5;
--colors-gray2: #F3F3F3;
--colors-r1: #FFBBBE;
--colors-gray5: #CECFCD;
--colors-g5: #043F2E;
--colors-p2: #A68FFF;
--colors-gray8: #6B6D68;
--colors-p1: #CECAFA;
--colors-b3: #3166CE;
--colors-r3: #DB4049;
--colors-gray1: #F8F8F8;
--colors-gray9: #5A5C58;
--colors-g1: #EEF2E3;
--colors-r2: #FB848B;
--colors-white: #FCFCFC;
--colors-b1: #BBD1FB;
--colors-gray4: #DFDFDE;
--colors-gray10: #242423;
```

### Spacing

```css
--space-base: 8px;
--space-xxxs: 16px;
--fontSizes-quoteMobile: 20px;
--fontSizes-h1: 72px;
--fontSizes-h2: 56px;
--space-xl: 304px;
--fontSizes-p2: 16px;
--letterSpacings-6: 0.06em;
--space-xxxxs: 12px;
--letterSpacings-1: 0.01em;
--space-xxs: 24px;
--space-lg: 200px;
--space-xs: 32px;
--fontSizes-p3: 14px;
--fontSizes-p4: 12px;
--fontSizes-h3: 36px;
--letterSpacings-minus3: -0.02em;
--space-md: 120px;
--fontSizes-quote: 36px;
--fontSizes-p1: 18px;
--letterSpacings-zero: 0%;
--letterSpacings-minus4: -0.04em;
--fontSizes-h4: 24px;
--space-sm: 56px;
--fontSizes-h4Mobile: 20px;
--fontSizes-h0: 120px;
--letterSpacings-minus1: -0.01em;
--space-atom: 4px;
```

### Typography

```css
--fonts-serif: Grenette;
--fonts-sans: Graphik;
```

### Other

```css
--radii-6: 6px;
--transitions-modeEase: cubic-bezier(1, 0, 0, 1);
--lineHeights-100: 100%;
--lineHeights-130: 130%;
--lineHeights-120: 120%;
--lineHeights-90: 90%;
--radii-20: 20px;
--lineHeights-115: 115%;
--vh: 8px;
--lineHeights-160: 160%;
--radii-4: 4px;
--radii-16: 16px;
--lineHeights-quote: 103%;
--lineHeights-110: 110%;
--radii-8: 8px;
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
| xs | 352px | max-width |
| sm | 425px | max-width |
| sm | 440px | max-width |
| sm | 480px | max-width |
| sm | 576px | max-width |
| md | 768px | max-width |
| md | 800px | max-width |
| 845px | 845px | max-width |
| lg | 975px | max-width |
| lg | 992px | min-width |
| 1200px | 1200px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.15s`, `0.25s`, `0.5s`, `0.4s`, `1s`, `0.2s`, `0.35s`

### Common Transitions

```css
transition: all;
transition: opacity 0.15s;
transition: color 0.25s ease-in-out;
transition: transform 0.5s;
transition: 0.4s;
transition: 0.4s cubic-bezier(0.75, 0, 0.29, 1.01);
transition: opacity 0.5s ease-in-out, height 0.5s ease-in-out;
transition: max-height 1s ease-out;
transition: background-color 0.25s ease-in-out, color 0.25s ease-in-out;
transition: background 0.2s ease-in-out;
```

### Keyframe Animations

**calendly-bouncedelay**
```css
@keyframes calendly-bouncedelay {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1); }
}
```

**calendly-bouncedelay**
```css
@keyframes calendly-bouncedelay {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1); }
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

### Buttons (40 instances)

```css
.button {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(4, 63, 46);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (2 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 6px;
  box-shadow: rgba(172, 171, 171, 0.3) 0px -1px 10px 0px;
  padding-top: 20px;
  padding-right: 26px;
}
```

### Inputs (5 instances)

```css
.input {
  background-color: rgb(208, 213, 210);
  color: rgb(33, 33, 33);
  border-color: rgb(33, 33, 33);
  border-radius: 50px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (105 instances)

```css
.link {
  color: rgb(238, 242, 227);
  font-size: 14px;
  font-weight: 500;
}
```

### Navigation (21 instances)

```css
.navigatio {
  color: rgb(33, 33, 33);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (3 instances)

```css
.foote {
  background-color: rgb(4, 63, 46);
  color: rgb(33, 33, 33);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (23 instances)

```css
.modal {
  background-color: rgba(31, 31, 31, 0.4);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.3) 0px 32px 68px 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 640px;
}
```

### Accordions (49 instances)

```css
.accordion {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(33, 33, 33);
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(33, 33, 33);
}
```

### Switches (10 instances)

```css
.switche {
  background-color: rgb(208, 213, 210);
  border-radius: 0px;
  border-color: rgb(33, 33, 33);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 14 instances, 5 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(24, 99, 220);
  padding: 8px 8px 8px 8px;
  border-radius: 2px;
  border: 2px solid rgb(24, 99, 220);
  font-size: 14px;
  font-weight: 500;
```

**Variant 2** (5 instances)

```css
  background: rgb(24, 99, 220);
  color: rgb(255, 255, 255);
  padding: 8px 8px 8px 8px;
  border-radius: 2px;
  border: 2px solid rgb(24, 99, 220);
  font-size: 14px;
  font-weight: 500;
```

**Variant 3** (1 instance)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(24, 99, 220);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgba(255, 255, 255, 0);
  font-size: 14px;
  font-weight: 400;
```

**Variant 4** (6 instances)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(33, 33, 33);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(33, 33, 33);
  font-size: 16px;
  font-weight: 700;
```

**Variant 5** (1 instance)

```css
  background: rgb(238, 242, 227);
  color: rgb(4, 63, 46);
  padding: 17px 30px 16px 30px;
  border-radius: 4px;
  border: 1px solid rgb(238, 242, 227);
  font-size: 14px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(33, 33, 33);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(33, 33, 33);
  font-size: 16px;
  font-weight: 400;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 16px 0px 16px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(4, 63, 46);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(4, 63, 46);
  font-size: 14px;
  font-weight: 500;
```

### Button — 4 instances, 3 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(4, 63, 46);
  padding: 17px 30px 16px 30px;
  border-radius: 4px;
  border: 1px solid rgb(4, 63, 46);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(4, 63, 46);
  color: rgb(200, 241, 105);
  padding: 17px 30px 16px 30px;
  border-radius: 4px;
  border: 1px solid rgb(4, 63, 46);
  font-size: 16px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgb(4, 63, 46);
  color: rgb(0, 0, 0);
  padding: 2px 36px 2px 36px;
  border-radius: 4px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **378 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1250px | 24px |
| 1248px | 24px |
| 800px | 0px |
| 1200px | 0px |
| 450px | 0px |
| 500px | 0px |
| 400px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 180px 246px 180px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 343x |
| row/wrap | 13x |
| column/nowrap | 21x |
| column/wrap | 1x |

**Gap values:** `16px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 10 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#1863dc` | 5.44:1 | AA |
| `#043f2e` | `#c8f169` | 9.25:1 | AAA |
| `#043f2e` | `#eef2e3` | 10.51:1 | AAA |

## Design System Score

**Overall: 83/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 26 !important rules — prefer specificity over overrides
- 75% of CSS is unused — consider purging
- 3141 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |

```css
background: linear-gradient(rgba(255, 255, 255, 0) 0%, rgb(255, 255, 255) 100%);
```

## Z-Index Map

**17 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,999999999 | header.s.c.-.a.X.Z.V.g. .d.X.q.e.e.x. .s.c.-.i.M.T.n.T.L. .e.b.T.c.N.q, header.s.c.-.a.X.Z.V.g. .d.X.q.e.e.x. .s.c.-.b.p.U.B.K.d. .e.x.T.U.G.n, div.m.o.d.a.l._.b.a.c.k.d.r.o.p |
| dropdown | 100,500 | div.c.-.f.u.o.K.m.z, div.s.c.-.f.i.C.w.l.c. .c.x.h.j.V.T |
| sticky | 10,50 | div.c.-.P.J.L.V. .c.-.P.J.L.V.-.i.d.d.x.g.S.L.-.c.s.s, div.c.-.d.C.E.M.Y.e. .c.-.d.C.E.M.Y.e.-.k.i.T.O.B.U.-.p.o.s.i.t.i.o.n.-.t.o.p.L.e.f.t. .c.-.d.C.E.M.Y.e.-.i.b.E.a.G.X.Z.-.c.s.s, div.c.-.d.C.E.M.Y.e. .c.-.d.C.E.M.Y.e.-.b.x.g.Y.W.h.-.p.o.s.i.t.i.o.n.-.b.o.t.t.o.m.R.i.g.h.t. .c.-.d.C.E.M.Y.e.-.i.b.E.a.G.X.Z.-.c.s.s |
| base | 0,6 | div.c.-.P.J.L.V. .c.-.P.J.L.V.-.i.b.m.q.s.f.B.-.c.s.s, div.c.-.j.F.A.e.A.y, div.c.-.d.C.E.M.Y.e. .c.-.d.C.E.M.Y.e.-.k.n.u.U.x.U.-.p.o.s.i.t.i.o.n.-.t.o.p.R.i.g.h.t. .c.-.d.C.E.M.Y.e.-.i.f.X.q.M.p.p.-.c.s.s |

**Issues:**
- [object Object]

## SVG Icons

**3 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| md | 1 |
| xl | 1 |

**Icon colors:** `#043F2E`, `#FFF`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Graphik | self-hosted | 400, 500, 600 | normal, italic |
| Grenette | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 21 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (9x), 3:2 (4x), 21:9 (2x), 6:1 (1x), 7.5:1 (1x), 4.82:1 (1x), 3.03:1 (1x), 4.44:1 (1x)

## Motion Language

**Feel:** springy · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `sm` | `200ms` | 200 |
| `md` | `350ms` | 350 |
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **ease-in-out** (102 uses) — `ease`
- **spring** (3 uses) — `cubic-bezier(0.75, 0, 0.29, 1.01)`

### Spring / Overshoot Easings

- `cubic-bezier(0.75, 0, 0.29, 1.01)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `scroll` | slide-x | transform | 2 |

## Component Anatomy

### button — 26 instances

**Slots:** label
**Variants:** primary

| variant | count | sample label |
|---|---|---|
| default | 25 | Customise |
| primary | 1 | Try for free |

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **try** (3)
- **reject** (2)
- **accept** (2)
- **customise** (1)
- **show** (1)
- **necessary** (1)
- **functional** (1)
- **analytics** (1)

### Button Copy Patterns

- "try for free" (3×)
- "reject all" (2×)
- "accept all" (2×)
- "customise" (1×)
- "show more" (1×)
- "necessary" (1×)
- "functional" (1×)
- "analytics" (1×)
- "performance" (1×)
- "advertisement" (1×)

### Sample Headings

> Business Intelligence
> built around
> Business Intelligence built around data teams
> data teams
> Capabilities you can count on
> Capabilities you can count on
> Clear the path from data to insights, together
> The intelligence layer for your modern data stack

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Mode is a collaborative data platform that combines SQL, R, Python, and visual analytics in one place. Connect, analyze, and share, faster.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → content → nav → nav → pricing → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.4 |
| 3 | nav | — | 0.9 |
| 4 | pricing | Business Intelligence | 0.4 |
| 5 | content | Capabilities you can count on | 0.3 |
| 6 | content | Clear the path from data to insights, together | 0.3 |
| 7 | content | The intelligence layer for your modern data stack | 0.3 |
| 8 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.425 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `mixed` (confidence 0.019)
**Counts:** total 26, svg 5, icon 8, screenshot-like 0, photo-like 1
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Times New Roman` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
