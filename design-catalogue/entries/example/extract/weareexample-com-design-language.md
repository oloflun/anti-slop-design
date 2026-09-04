# Design Language: We Are Example | Brand Strategy, PR & Placemaking Agency | Sydney & Dubai

> Extracted from `https://www.weareexample.com` on September 4, 2026
> 2780 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#2cc9ff` | rgb(44, 201, 255) | hsl(195, 100%, 59%) | 26 |
| Secondary | `#ff0000` | rgb(255, 0, 0) | hsl(0, 100%, 50%) | 4 |
| Accent | `#ffdede` | rgb(255, 222, 222) | hsl(0, 100%, 94%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#f3f3f0` | hsl(60, 11%, 95%) | 3290 |
| `#000000` | hsl(0, 0%, 0%) | 97 |
| `#424242` | hsl(0, 0%, 26%) | 37 |
| `#1f1f1f` | hsl(0, 0%, 12%) | 8 |
| `#ffffff` | hsl(0, 0%, 100%) | 4 |
| `#dddddd` | hsl(0, 0%, 87%) | 1 |
| `#111111` | hsl(0, 0%, 7%) | 1 |

### Background Colors

Used on large-area elements: `#f3f3f0`, `#f8f8ef`, `#ffffff`, `#000000`, `#16181b`

### Text Colors

Text color palette: `#000000`, `#0e1623`, `#f3f3f0`, `#ebebeb`, `#2cc9ff`

### Gradients

```css
background-image: linear-gradient(0deg, rgb(248, 248, 239), rgb(243, 243, 240));
```

```css
background-image: linear-gradient(0deg, rgb(243, 243, 240), rgb(248, 248, 239));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#f3f3f0` | background, text, border | 3290 |
| `#0e1623` | text, border, background | 2184 |
| `#000000` | text, border, background | 97 |
| `#424242` | border, background | 37 |
| `#2cc9ff` | text, border | 26 |
| `#1f1f1f` | background | 8 |
| `#ff0000` | border, background | 4 |
| `#ffffff` | background | 4 |
| `#0051ff` | border | 1 |
| `#dddddd` | background | 1 |
| `#ffdede` | background | 1 |
| `#111111` | background | 1 |
| `#ffff00` | background | 1 |
| `#0000ff` | background | 1 |

## Typography

### Font Families

- **American Grotesk** — used for all (1389 elements)
- **American Grotesk Compressed** — used for all (1200 elements)
- **Ppeditorialnew** — used for body (26 elements)
- **Menlo** — used for body (4 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 230.4px | 14.4rem | 900 | 179.712px | -0.552px | div |
| 184.32px | 11.52rem | 900 | 147.456px | normal | span, div, br |
| 182.4px | 11.4rem | 900 | 145.92px | normal | h1, div, h2 |
| 166.4px | 10.4rem | 900 | 133.12px | normal | h2, div |
| 140.8px | 8.8rem | 900 | 112.64px | normal | h1, div |
| 102.4px | 6.4rem | 900 | 81.92px | normal | h2 |
| 96px | 6rem | 900 | 79.36px | -0.552px | div |
| 72px | 4.5rem | 900 | 57.6px | normal | h2, div, br |
| 64px | 4rem | 900 | 51.2px | normal | h5, div, h3, h2 |
| 38.4px | 2.4rem | 900 | 30.72px | normal | h5, div |
| 35.84px | 2.24rem | 900 | 28.672px | normal | h5 |
| 32px | 2rem | 900 | 25.6px | normal | h5, div |
| 23.04px | 1.44rem | 900 | 18.432px | normal | h5 |
| 20.48px | 1.28rem | 900 | 21.504px | 0.2048px | a, img, div |
| 19.2px | 1.2rem | 400 | 22.08px | -0.576px | h2, div, p, br |

### Heading Scale

```css
h1 { font-size: 182.4px; font-weight: 900; line-height: 145.92px; }
h2 { font-size: 166.4px; font-weight: 900; line-height: 133.12px; }
h1 { font-size: 140.8px; font-weight: 900; line-height: 112.64px; }
h2 { font-size: 102.4px; font-weight: 900; line-height: 81.92px; }
h2 { font-size: 72px; font-weight: 900; line-height: 57.6px; }
h5 { font-size: 64px; font-weight: 900; line-height: 51.2px; }
h5 { font-size: 38.4px; font-weight: 900; line-height: 30.72px; }
h5 { font-size: 35.84px; font-weight: 900; line-height: 28.672px; }
h5 { font-size: 32px; font-weight: 900; line-height: 25.6px; }
h5 { font-size: 23.04px; font-weight: 900; line-height: 18.432px; }
h2 { font-size: 19.2px; font-weight: 400; line-height: 22.08px; }
h6 { font-size: 17.92px; font-weight: 900; line-height: 17.92px; }
h5 { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Body Text

```css
body { font-size: 19.2px; font-weight: 400; line-height: 22.08px; }
```

### Font Weights in Use

`900` (1174x), `400` (1058x), `500` (489x), `200` (38x), `300` (13x), `600` (7x), `700` (1x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-10 | 10px | 0.625rem |
| spacing-12 | 12px | 0.75rem |
| spacing-24 | 24px | 1.5rem |
| spacing-32 | 32px | 2rem |
| spacing-36 | 36px | 2.25rem |
| spacing-38 | 38px | 2.375rem |
| spacing-51 | 51px | 3.1875rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-102 | 102px | 6.375rem |
| spacing-104 | 104px | 6.5rem |
| spacing-126 | 126px | 7.875rem |
| spacing-128 | 128px | 8rem |
| spacing-140 | 140px | 8.75rem |
| spacing-192 | 192px | 12rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 38 |
| md | 6px | 37 |

## CSS Custom Properties

### Colors

```css
--_theme---button-primary--border<deleted|variable-a87e3064-5c4a-69d7-92b9-965bb3c7ff4e>: var(--swatch--example-ink);
--_theme---button-primary--background<deleted|variable-7854a355-6f26-135f-85dc-f6a60918d8cb>: var(--swatch--example-ink);
--_theme---button-primary--text<deleted|variable-6c906087-13b9-c243-736f-8e9d67df4dec>: var(--swatch--example-canvas);
--_theme---button-primary--border-hover<deleted|variable-d7733e9f-9216-e30a-de13-7132697cb2f7>: var(--_brand---color\<deleted\|variable-c816ef1c-1865-958b-4065-9cb21c63c512\>);
--_theme---button-primary--background-hover<deleted|variable-b111ed68-b24b-df31-e2e8-8d11cf0b80cd>: var(--_brand---color\<deleted\|variable-c816ef1c-1865-958b-4065-9cb21c63c512\>);
--_theme---button-primary--text-hover<deleted|variable-8bff32c4-7a72-9992-c763-f8968e78242d>: var(--_brand---text\<deleted\|variable-35d5a4aa-4191-cef6-d3a9-dbb3b7073ee4\>);
--_theme---text-secondary<deleted|variable-3d23388c-7f2a-c4ff-d440-16c04baf3d55>: var(--swatch--dark-secondary\<deleted\|variable-2a9d4f1d-42c1-d4ca-25b3-ed8599375376\>);
--_theme---color: white;
--_theme---button--color: white;
--_theme---button-primary--color: white;
--_brand---color<deleted|variable-c816ef1c-1865-958b-4065-9cb21c63c512>: var(--swatch--brand-1\<deleted\|variable-d7eac856-7587-f2f2-437c-16e1d155ca87\>);
--swatch--dark-secondary<deleted|variable-2a9d4f1d-42c1-d4ca-25b3-ed8599375376>: #3f2b88;
```

### Spacing

```css
--_text-style---letter-spacing<deleted|variable-6238be08-c266-d112-a212-309c40703952>: -.03em;
--_responsive---font-size--h1: 10vw;
--_responsive---font-size--h2: 8vw;
--_responsive---font-size--h3: 5vw;
--_responsive---font-size--h4: 4vw;
--_responsive---font-size--h5: 2.8vw;
--_responsive---font-size--h6: 1.4vw;
--_responsive---margins--padding-vertical: 5vw;
--_responsive---margins--padding-horizontal: 1.5vw;
--_responsive---margins--padding-horizontal-tight: .5vw;
--_text-style---font-size<deleted|variable-eb545b15-d1a3-826d-7423-64942a7b6b25>: var(--_responsive---font-size--main);
--_responsive---font-size--link_button: 1.4vw;
--_responsive---font-size--label: 1.2vw;
--_responsive---font-size--corners: .5vw;
--_responsive---font-size--para-spacing: 0vw;
--_responsive---font-size--main: 1.2vw;
--_responsive---font-size--display: 14.25vw;
```

### Typography

```css
--_theme---text: var(--swatch--example-ink);
--_text-style---number: 0;
--_brand---text<deleted|variable-35d5a4aa-4191-cef6-d3a9-dbb3b7073ee4>: var(--swatch--example-canvas);
```

### Other

```css
--_theme---background<deleted|variable-87df2d4f-56e9-8fe5-9db7-daff1403bdd4>: var(--swatch--example-canvas);
--max-width--main: 100vw;
--swatch--example-ink: #0e1623;
--swatch--example-canvas: #f3f3f0;
--swatch--example-ink-grey: #16181b;
--swatch--brand-1<deleted|variable-d7eac856-7587-f2f2-437c-16e1d155ca87>: #7957ff;
--swatch--brand-2<deleted|variable-984ff473-d605-fc54-7763-67fb10e8be8f>: #d9e45a;
--swatch--brand-3<deleted|variable-e52a593c-42bf-c170-4f65-91e668f14914>: #f4c7eb;
```

### Dependencies

```css
--_theme---background<deleted|variable-87df2d4f-56e9-8fe5-9db7-daff1403bdd4>: --swatch--example-canvas;
--_theme---text: --swatch--example-ink;
--_theme---button-primary--border<deleted|variable-a87e3064-5c4a-69d7-92b9-965bb3c7ff4e>: --swatch--example-ink;
--_theme---button-primary--background<deleted|variable-7854a355-6f26-135f-85dc-f6a60918d8cb>: --swatch--example-ink;
--_theme---button-primary--text<deleted|variable-6c906087-13b9-c243-736f-8e9d67df4dec>: --swatch--example-canvas;
--_theme---button-primary--border-hover<deleted|variable-d7733e9f-9216-e30a-de13-7132697cb2f7>: --_brand---color;
--_theme---button-primary--background-hover<deleted|variable-b111ed68-b24b-df31-e2e8-8d11cf0b80cd>: --_brand---color;
--_theme---button-primary--text-hover<deleted|variable-8bff32c4-7a72-9992-c763-f8968e78242d>: --_brand---text;
--_theme---text-secondary<deleted|variable-3d23388c-7f2a-c4ff-d440-16c04baf3d55>: --swatch--dark-secondary;
--_text-style---font-size<deleted|variable-eb545b15-d1a3-826d-7423-64942a7b6b25>: --_responsive---font-size--main;
--_brand---color<deleted|variable-c816ef1c-1865-958b-4065-9cb21c63c512>: --swatch--brand-1;
--_brand---text<deleted|variable-35d5a4aa-4191-cef6-d3a9-dbb3b7073ee4>: --swatch--example-canvas;
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
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 991px | max-width |
| 1440px | 1440px | min-width |

## Transitions & Animations

**Durations:** `0.2s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: opacity 0.2s;
transition: border-color 0.3s;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (18 instances)

```css
.button {
  background-color: rgba(56, 152, 236, 0);
  color: rgb(14, 22, 35);
  font-size: 17.92px;
  font-weight: 900;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Inputs (25 instances)

```css
.input {
  background-color: rgb(66, 66, 66);
  color: rgb(44, 201, 255);
  border-color: rgb(44, 201, 255);
  border-radius: 2px;
  font-size: 11px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (142 instances)

```css
.link {
  color: rgb(14, 22, 35);
  font-size: 16.64px;
  font-weight: 400;
}
```

### Navigation (120 instances)

```css
.navigatio {
  color: rgb(14, 22, 35);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 6.4px;
  position: static;
}
```

### Footer (18 instances)

```css
.foote {
  background-color: rgb(22, 24, 27);
  color: rgb(243, 243, 240);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 18.4px;
}
```

### Modals (1 instances)

```css
.modal {
  background-color: rgba(0, 0, 0, 0.15);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (16 instances)

```css
.dropdown {
  background-color: rgb(243, 243, 240);
  border-radius: 0px;
  border-color: rgb(14, 22, 35);
  padding-top: 0px;
}
```

### ProgressBars (2 instances)

```css
.progressBar {
  background-color: rgba(243, 243, 240, 0.1);
  color: rgb(14, 22, 35);
  border-radius: 0px;
  font-size: 18.4px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(56, 152, 236, 0);
  color: rgb(14, 22, 35);
  padding: 0px 0px 0px 17.92px;
  border-radius: 0px;
  border: 0px none rgb(14, 22, 35);
  font-size: 17.92px;
  font-weight: 900;
```

### Button — 6 instances, 2 variants

**Variant 1** (4 instances)

```css
  background: rgba(56, 152, 236, 0);
  color: rgb(14, 22, 35);
  padding: 0px 0px 0px 17.92px;
  border-radius: 0px;
  border: 0px none rgb(14, 22, 35);
  font-size: 17.92px;
  font-weight: 900;
```

**Variant 2** (2 instances)

```css
  background: rgba(56, 152, 236, 0);
  color: rgb(243, 243, 240);
  padding: 0px 0px 0px 17.92px;
  border-radius: 0px;
  border: 0px none rgb(243, 243, 240);
  font-size: 17.92px;
  font-weight: 900;
```

### Input — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0.05);
  color: rgb(14, 22, 35);
  padding: 8px 12px 8px 12px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 14.08px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(34, 35, 37);
  color: rgb(243, 243, 240);
  padding: 8px 12px 8px 12px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 14.08px;
  font-weight: 400;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(56, 152, 236, 0);
  color: rgb(14, 22, 35);
  padding: 0px 0px 0px 17.92px;
  border-radius: 0px;
  border: 0px none rgb(14, 22, 35);
  font-size: 17.92px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(56, 152, 236, 0);
  color: rgb(243, 243, 240);
  padding: 0px 0px 0px 17.92px;
  border-radius: 0px;
  border: 0px none rgb(243, 243, 240);
  font-size: 17.92px;
  font-weight: 400;
```

## Layout System

**5 grid containers** and **233 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 656px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 2x |
| 8-column | 2x |
| 12-column | 1x |

### Grid Templates

```css
grid-template-columns: 85.875px 85.875px 85.8906px 85.875px 85.875px 85.8906px 85.875px 85.875px 85.8906px 85.875px 85.875px 85.8906px;
gap: 179.2px 19.2px;
grid-template-columns: 632px 632px;
gap: 16px;
grid-template-columns: 138.406px 138.422px 138.406px 138.422px 138.406px 138.422px 138.406px 138.422px;
gap: 19.2px;
grid-template-columns: 320px 320px;
gap: 16px;
grid-template-columns: 138.406px 138.422px 138.406px 138.422px 138.406px 138.422px 138.406px 138.422px;
gap: 19.2px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 114x |
| row/nowrap | 119x |

**Gap values:** `0px 128px`, `102.4px`, `12.8px`, `128px`, `15.36px`, `16px`, `179.2px 19.2px`, `19.2px`, `192px`, `2.56px`, `24px`, `25.6px`, `32px`, `38.4px`, `51.2px`, `6.4px`, `64px`, `64px 0px`, `80px`, `8px`, `normal 64px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 81/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 40/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 26 distinct font sizes — consider a tighter type scale
- 47 !important rules — prefer specificity over overrides
- 74% of CSS is unused — consider purging
- 3256 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 0deg | 2 | brand |
| linear | 0deg | 2 | brand |

```css
background: linear-gradient(0deg, rgb(248, 248, 239), rgb(243, 243, 240));
background: linear-gradient(0deg, rgb(243, 243, 240), rgb(248, 248, 239));
```

## Z-Index Map

**14 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,99999 | div.n.a.v, div.n.a.v. .m.o.b, div.m.o.b.i.l.e._.m.e.n.u |
| sticky | 10,10 | div.h.o.m.e.-.h.e.r.o.-.s.u.b, div.p.o.l.-.m.a.s.k. .s.t.a.r.t.-.v.i.s.i.b.l.e, div.p.o.l.-.m.a.s.k. .s.t.a.r.t.-.v.i.s.i.b.l.e |
| base | -2,5 | div.w.e.b.g.l._.h.o.l.d.e.r, div.w.e.b.g.l. .w.-.e.m.b.e.d, canvas.w.e.b.g.l |

**Issues:**
- [object Object]

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| lil-gui | self-hosted | 400, normal | normal |
| webflow-icons | self-hosted | normal | normal |
| American Grotesk | self-hosted | 300, 400, 500 | normal |
| American Grotesk Compressed | self-hosted | 900 | normal |
| Ppeditorialnew | self-hosted | 200 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 45 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 9 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 4 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (33x), 8.48:1 (7x), 3:2 (5x), 4:3 (4x), 2:3 (3x), 21:9 (3x), 20.64:1 (3x), 3:4 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

## Component Anatomy

### button — 9 instances

**Slots:** label
**Variants:** link

| variant | count | sample label |
|---|---|---|
| link | 5 | WHAT WE DO |
| default | 4 | VIEW ON APPLE |

### input — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **read** (3)
- **what** (1)
- **all** (1)
- **view** (1)
- **hello** (1)

### Button Copy Patterns

- "read" (3×)
- "what we do" (1×)
- "all work" (1×)
- "view on apple" (1×)
- "hello@weareexample.com" (1×)

### Sample Headings

> Brand Strategy, Design and PR for Hospitality, F&B and consumer brands across Australia, The Middle East & Asia Pacific
> WE
MAKE BRANDS
AND PLACES
FAMOUS
> we make BRANDS AND PLACES FAMOUS
> Brand Strategy, Design and PR for Hospitality, F&B and consumer brands across Australia, The Middle East & Asia Pacific
> DESTINATIONS & PLACEMAKING
> DESTINATIONS & PLACEMAKING
> DESTINATIONS & PLACEMAKING
> DESTINATIONS & PLACEMAKING
> DESTINATIONS & PLACEMAKING
> MORE VALUABLE

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** We Are Example makes brands and places famous. Independent brand strategy, PR and placemaking agency working with luxury hospitality, drinks brands and destinations across Australia, the Middle East a

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): hero → feature-grid → content → hero → gallery → content → content → content → content → feature-grid → testimonial → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | hero | Brand Strategy, Design and PR for Hospitality, F&B and consumer brands across Au | 0.85 |
| 1 | hero | we make BRANDS AND PLACES FAMOUS | 0.85 |
| 2 | gallery | DESTINATIONS & PLACEMAKING | 0.7 |
| 3 | content | MORE VALUABLE | 0.3 |
| 4 | content | MORE VALUABLE | 0.3 |
| 5 | feature-grid | — | 0.8 |
| 6 | content | — | 0.3 |
| 7 | content | — | 0.3 |
| 8 | content | — | 0.3 |
| 9 | feature-grid | FOR EXAMPLE | 0.8 |
| 10 | testimonial | FINE FORM PODCAST | 0.8 |
| 11 | content | The best client relationships start with good conversation | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.398 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 6px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.131)
**Counts:** total 60, svg 39, icon 32, screenshot-like 0, photo-like 14
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `American Grotesk` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
