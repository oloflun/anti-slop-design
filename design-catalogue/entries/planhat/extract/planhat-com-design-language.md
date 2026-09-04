# Design Language: Planhat

> Extracted from `https://www.planhat.com` on September 4, 2026
> 2003 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#c0ff66` | rgb(192, 255, 102) | hsl(85, 100%, 70%) | 2 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 1312 |
| Accent | `#22c55e` | rgb(34, 197, 94) | hsl(142, 71%, 45%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 2610 |
| `#ffffff` | hsl(0, 0%, 100%) | 138 |
| `#403a35` | hsl(27, 9%, 23%) | 12 |
| `#767676` | hsl(0, 0%, 46%) | 11 |
| `#9e9d9b` | hsl(40, 2%, 61%) | 2 |
| `#575551` | hsl(40, 4%, 33%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#000000`, `#9e9d9b`, `#c0ff66`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#0000ee`, `#403a35`

### Gradients

```css
background-image: conic-gradient(rgba(255, 255, 255, 0.15) 328.157deg, rgb(255, 255, 255) 360deg);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 2610 |
| `#0000ee` | text, border | 1312 |
| `#ffffff` | background, text, border | 138 |
| `#403a35` | text, border, background | 12 |
| `#767676` | border | 11 |
| `#9e9d9b` | background | 2 |
| `#c0ff66` | background | 2 |
| `#575551` | background | 1 |
| `#22c55e` | background | 1 |

## Typography

### Font Families

- **Inter** — used for all (144 elements)
- **Geigy LL Duplex Var Variable Reg** — used for all (127 elements)
- **Times New Roman** — used for body (45 elements)
- **Inter Variable** — used for all (11 elements)
- **.\7f  \7f** — used for body (3 elements)
- **ABC Arizona Flare Regular** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 117.101px | 7.3188rem | 400 | 117.101px | -7.02604px | p |
| 72px | 4.5rem | 400 | 75.6px | -3.6px | p |
| 60px | 3.75rem | 400 | 66px | -1.8px | h2 |
| 48px | 3rem | 400 | 52.8px | -2.16px | h2, p, br, h3 |
| 32px | 2rem | 400 | 38.4px | -1.12px | h5 |
| 24px | 1.5rem | 400 | 31.2px | normal | p |
| 21px | 1.3125rem | 400 | 26.25px | -0.63px | p |
| 20px | 1.25rem | 700 | 20px | 0.28px | p |
| 18px | 1.125rem | 400 | 25.2px | -0.36px | h3, p, h4, span |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 14px | 0.875rem | 400 | 21px | -0.28px | p, button |
| 13px | 0.8125rem | 600 | 21px | 0.28px | a |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |
| 10px | 0.625rem | 400 | 15px | 1px | p, h2, a |

### Heading Scale

```css
h2 { font-size: 60px; font-weight: 400; line-height: 66px; }
h2 { font-size: 48px; font-weight: 400; line-height: 52.8px; }
h5 { font-size: 32px; font-weight: 400; line-height: 38.4px; }
h3 { font-size: 18px; font-weight: 400; line-height: 25.2px; }
h1 { font-size: 12px; font-weight: 400; line-height: normal; }
h2 { font-size: 10px; font-weight: 400; line-height: 15px; }
```

### Body Text

```css
body { font-size: 18px; font-weight: 400; line-height: 25.2px; }
```

### Font Weights in Use

`400` (1996x), `700` (2x), `300` (2x), `500` (2x), `600` (1x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-24 | 24px | 1.5rem |
| spacing-30 | 30px | 1.875rem |
| spacing-36 | 36px | 2.25rem |
| spacing-40 | 40px | 2.5rem |
| spacing-46 | 46px | 2.875rem |
| spacing-64 | 64px | 4rem |
| spacing-72 | 72px | 4.5rem |
| spacing-91 | 91px | 5.6875rem |
| spacing-96 | 96px | 6rem |
| spacing-120 | 120px | 7.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 1px | 2 |
| sm | 4px | 79 |
| md | 8px | 48 |
| full | 50px | 1 |
| full | 100px | 4 |
| full | 999px | 10 |

## Box Shadows

**xs** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0.08) 0px -1px 0px 0px, rgba(0, 0, 0, 0.06) 0px -8px 32px 0px;
```

**md** — blur: 10px
```css
box-shadow: rgba(0, 0, 0, 0.12) 0px 0px 10px 0px;
```

## CSS Custom Properties

### Other

```css
--one-if-corner-shape-supported: 1;
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
| sm | 450px | max-width |
| sm | 500px | max-width |
| sm | 599px | max-width |
| sm | 600px | max-width |
| sm | 601px | min-width |
| sm | 650px | max-width |
| sm | 651px | min-width |
| md | 800px | max-width |
| md | 801px | min-width |
| md | 809px | max-width |
| md | 810px | min-width |
| lg | 980px | max-width |
| lg | 1000px | max-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | max-width |
| 1799px | 1799px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.5s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: opacity 0.5s ease-in-out;
transition: box-shadow 0.3s cubic-bezier(0.44, 0, 0.56, 1), background 0.3s cubic-bezier(0.44, 0, 0.56, 1);
transition: background, box-shadow;
transition: color 0.3s cubic-bezier(0.44, 0, 0.56, 1), text-decoration-color 0.3s cubic-bezier(0.44, 0, 0.56, 1), text-decoration-thickness 0.3s cubic-bezier(0.44, 0, 0.56, 1), text-underline-offset 0.3s cubic-bezier(0.44, 0, 0.56, 1);
transition: 0.3s;
```

### Keyframe Animations

**ch2-bar-bottom-in-2**
```css
@keyframes ch2-bar-bottom-in-2 {
  0% { opacity: 0; transform: translateY(100%); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**__framer-loading-spin**
```css
@keyframes __framer-loading-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (4 instances)

```css
.button {
  background-color: rgb(192, 255, 102);
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 9px;
  padding-right: 14px;
  border-radius: 1px;
}
```

### Inputs (20 instances)

```css
.input {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  border-color: rgb(118, 118, 118);
  border-radius: 0px;
  font-size: 12px;
  padding-top: 1px;
  padding-right: 2px;
}
```

### Links (113 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 12px;
  font-weight: 400;
}
```

### Modals (3 instances)

```css
.modal {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.08) 0px -1px 0px 0px, rgba(0, 0, 0, 0.06) 0px -8px 32px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(192, 255, 102);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 10px;
  border-radius: 0px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 10px 16px 10px 18px;
  border-radius: 4px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 9px 14px 9px 14px;
  border-radius: 1px;
  border: 1px solid rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 500;
```

**Variant 2** (1 instance)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 9px 14px 9px 14px;
  border-radius: 1px;
  border: 1px solid rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 500;
```

## Layout System

**7 grid containers** and **809 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1280px | 40px |
| 1200px | 0px |
| 100% | 0px |
| 600px | 0px |
| 313px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 4x |
| 6-column | 1x |
| 4-column | 1x |
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 357.328px 357.328px 357.328px;
gap: 24px;
grid-template-columns: 357.328px 357.328px 357.344px;
gap: 24px;
grid-template-columns: 600px 600px;
grid-template-columns: 357.328px 357.328px 357.328px;
gap: 24px;
grid-template-columns: 357.328px 357.328px 357.344px;
gap: 64px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 523x |
| row/nowrap | 266x |
| row/wrap | 5x |
| column/wrap | 15x |

**Gap values:** `10px`, `10px 4px`, `120px`, `12px`, `16px`, `17px 18px`, `20px`, `21px 18px`, `24px`, `24px 18px`, `2px`, `30px`, `32px`, `48px`, `4px`, `5px`, `64px`, `6px`, `6px 4px`, `72px`, `8px`, `96px`, `96px 0px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#000000` | 21:1 | AAA |

## Design System Score

**Overall: 84/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 6 font families — consider limiting to 2 (heading + body)
- 237 !important rules — prefer specificity over overrides
- 9773 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| conic | — | 2 | brand |
| linear | — | 2 | brand |

```css
background: conic-gradient(rgba(255, 255, 255, 0.15) 328.157deg, rgb(255, 255, 255) 360deg);
background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 100%);
```

## Z-Index Map

**8 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 700001,2147483647 | div.c.h.2.-.d.i.a.l.o.g. .c.h.2.-.d.i.a.l.o.g.-.b.o.t.t.o.m. .c.h.2.-.v.i.s.i.b.l.e, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.l.l.i.o.7.x, div.f.r.a.m.e.r.-.w.w.s.a.a.z.-.c.o.n.t.a.i.n.e.r |
| base | 0,9 | div.f.r.a.m.e.r.-.6.t.k.j.s.m, div.f.r.a.m.e.r.-.8.4.9.t.t.h.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.1.1.6.5.s.f.y |

**Issues:**
- [object Object]

## SVG Icons

**16 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 5 |
| sm | 2 |
| lg | 2 |
| xl | 7 |

**Icon colors:** `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Fragment Mono | cdn | 400 | normal |
| IBM Plex Mono | cdn | 400 | normal |
| JetBrains Mono | cdn | 400 | normal |
| Geigy LL Duplex Var Variable Reg | self-hosted | 400 | normal |
| ABC Arizona Flare Regular | self-hosted | 400 | normal |
| Times Now SemiLight | self-hosted | 400, normal | normal |
| Times Now Light Italic | self-hosted | 300, 400, normal | normal, italic |
| Aeonik Extended SemiBold | self-hosted | 600 | normal |
| GT Super Text Book | self-hosted | 350 | normal |
| Aeonik Medium | self-hosted | 500 | normal |
| .\7f  \7f  | self-hosted | 400 | normal |
| Inter | self-hosted | 300, 400, 500, 700, 900 | normal, italic |
| Inter Variable | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 6 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 2 | objectFit: contain, borderRadius: 4px, shape: rounded |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 2.08:1 (4x), 1:1 (3x), 3:2 (1x), 16:9 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **ease-in-out** (4 uses) — `ease`
- **custom** (4 uses) — `cubic-bezier(0.44, 0, 0.56, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `ch2-bar-bottom-in-2` | slide-y | opacity, transform | 1 |

## Component Anatomy

### button — 4 instances

**Slots:** label, icon
**Variants:** primary

| variant | count | sample label |
|---|---|---|
| default | 3 | GET TICKETS |
| primary | 1 | Accept Cookies |

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **get** (1)
- **subscribe** (1)
- **manage** (1)
- **accept** (1)

### Button Copy Patterns

- "get tickets" (1×)
- "subscribe to our newsletter" (1×)
- "manage preferences" (1×)
- "accept cookies" (1×)

### Sample Headings

> Automate commercial processes across your teams
> Assemble your GTM under one roof
> Deploy agents with confidence
> Stay in-the-loop
> THE LEADING CUSTOMER PLATFORM

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** A customer platform where commercial teams work better. We build and deploy frontier technologies—integrating data, AI and collaboration—that empower industry leaders to acquire and grow lifelong reve

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): testimonials

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | testimonials | Automate commercial processes across your teams | 0.4 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.299 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 999px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.389)
**Counts:** total 9, svg 0, icon 0, screenshot-like 0, photo-like 5
**Dominant aspect:** landscape
**Radius profile on images:** square

## Component Library

**Detected:** `vuetify` (confidence 0.78)

Evidence:
- 24 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
