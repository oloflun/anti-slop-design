# Design Language: Your sustainable cabins in Germany and Austria | Raus

> Extracted from `https://www.raus.life/` on September 4, 2026
> 436 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#23212c` | rgb(35, 33, 44) | hsl(251, 14%, 15%) | 723 |
| Secondary | `#dd5000` | rgb(221, 80, 0) | hsl(22, 100%, 43%) | 17 |
| Accent | `#a6dfff` | rgb(166, 223, 255) | hsl(202, 100%, 83%) | 2 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#ffffff` | hsl(0, 0%, 100%) | 93 |
| `#fdf9ed` | hsl(45, 80%, 96%) | 1 |
| `#000000` | hsl(0, 0%, 0%) | 1 |

### Background Colors

Used on large-area elements: `#fdf9ed`, `#000000`, `#a6dfff`, `#ffffff`, `#fcbd1c`

### Text Colors

Text color palette: `#23212c`, `#dd5000`, `#ffffff`, `#006434`, `#0000ee`, `#b218a4`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#23212c` | text, border, background | 723 |
| `#ffffff` | text, border, background | 93 |
| `#0000ee` | text, border | 30 |
| `#006434` | text, border | 24 |
| `#dd5000` | text, border, background | 17 |
| `#b218a4` | text, border | 4 |
| `#a6dfff` | background | 2 |
| `#fdf9ed` | background | 1 |
| `#000000` | background | 1 |
| `#fcbd1c` | background | 1 |

## Typography

### Font Families

- **neue-haas-unica** — used for all (427 elements)
- **fonts** — used for all (9 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 84px | 5.25rem | 300 | 76px | -2.52px | li, a |
| 40px | 2.5rem | 300 | 38px | -0.8px | h2 |
| 36px | 2.25rem | 300 | 36px | -0.54px | h1, h3 |
| 28px | 1.75rem | 300 | 30px | -0.42px | h4 |
| 22px | 1.375rem | 400 | 26px | -0.22px | li, a, div, span |
| 18px | 1.125rem | 400 | 22px | -0.18px | p, a, span, svg |
| 16px | 1rem | 400 | 18.4px | normal | html, head, style, meta |
| 14px | 0.875rem | 400 | 18px | -0.14px | select, option, h4, p |
| 12px | 0.75rem | 400 | 16px | -0.06px | label, span |

### Heading Scale

```css
h2 { font-size: 40px; font-weight: 300; line-height: 38px; }
h1 { font-size: 36px; font-weight: 300; line-height: 36px; }
h4 { font-size: 28px; font-weight: 300; line-height: 30px; }
h4 { font-size: 14px; font-weight: 400; line-height: 18px; }
```

### Body Text

```css
body { font-size: 18px; font-weight: 400; line-height: 22px; }
```

### Font Weights in Use

`400` (415x), `300` (21x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-32 | 32px | 2rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-53 | 53px | 3.3125rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-120 | 120px | 7.5rem |
| spacing-192 | 192px | 12rem |
| spacing-211 | 211px | 13.1875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 4 |
| lg | 12px | 12 |
| lg | 16px | 1 |
| xl | 20px | 8 |
| full | 40px | 1 |
| full | 64px | 2 |
| full | 72px | 3 |
| full | 99px | 2 |

## CSS Custom Properties

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
| xs | 330px | max-width |
| xs | 360px | max-width |
| 390px | 390px | max-width |
| 400px | 400px | max-width |
| sm | 420px | max-width |
| sm | 480px | max-width |
| sm | 576px | min-width |
| md | 768px | min-width |
| lg | 992px | min-width |
| 1200px | 1200px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.5s`, `0.2s`, `0.25s`, `1s`, `0.4s`, `0.1s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: opacity 0.5s;
transition: 0.2s;
transition: transform 0.2s ease-out;
transition: 0.25s;
transition: background 0.2s ease-out;
transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 1s ease-out;
transition: 0.4s cubic-bezier(0.665, 0.425, 0.44, 1.105) 0.1s;
transition: opacity 0.2s cubic-bezier(0.665, 0.425, 0.44, 1.105) 0.3s;
```

### Keyframe Animations

**rotate-spinner**
```css
@keyframes rotate-spinner {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

**cvc-indicate-location**
```css
@keyframes cvc-indicate-location {
  0% { opacity: 1; }
  100% { opacity: 0.3; }
}
```

**card-bounce**
```css
@keyframes card-bounce {
  0% { animation-timing-function: cubic-bezier(0.17, 0.17, 0.32, 1); translate: 0px -60%; }
  9.70874% { animation-timing-function: cubic-bezier(0.41, 0, 0.49, 1); translate: 0px 8.5%; }
  23.4466% { animation-timing-function: cubic-bezier(0.29, 0, 0.26, 1); translate: 0px -22.5%; }
  47.7184% { translate: 0px; }
  63.8835% { animation-timing-function: cubic-bezier(1, 0, 0.78, 1); translate: 0px; }
  86.5534% { translate: 0px 40.7%; }
  100% { translate: 0px 40.7%; }
}
```

**card-fade-100**
```css
@keyframes card-fade-100 {
  0% { animation-timing-function: linear; opacity: 0; }
  8.1068% { opacity: 1; }
  78.4466% { opacity: 1; }
  86.5534% { opacity: 0; }
  100% { opacity: 0; }
}
```

**card-fade-60**
```css
@keyframes card-fade-60 {
  0% { animation-timing-function: linear; opacity: 0; }
  8.1068% { opacity: 0.6; }
  78.4466% { opacity: 0.6; }
  86.5534% { opacity: 0; }
  100% { opacity: 0; }
}
```

**card-fade-20**
```css
@keyframes card-fade-20 {
  0% { animation-timing-function: linear; opacity: 0; }
  8.1068% { opacity: 0.2; }
  78.4466% { opacity: 0.2; }
  86.5534% { opacity: 0; }
  100% { opacity: 0; }
}
```

**hVJUYp**
```css
@keyframes hVJUYp {
  0% { transform: var(--origin); opacity: 0; }
  100% { transform: translateY(0px); opacity: 1; }
}
```

**hVJUYp**
```css
@keyframes hVJUYp {
  0% { transform: var(--origin); opacity: 0; }
  100% { transform: translateY(0px); opacity: 1; }
}
```

**jBwdVX**
```css
@keyframes jBwdVX {
  0% { transform: translateY(100%); }
  100% { transform: translateX(0px); }
}
```

**jBwdVX**
```css
@keyframes jBwdVX {
  0% { transform: translateY(100%); }
  100% { transform: translateX(0px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (9 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(35, 33, 44);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Inputs (2 instances)

```css
.input {
  color: rgb(35, 33, 44);
  border-color: rgb(35, 33, 44);
  border-radius: 0px;
  font-size: 14px;
  padding-top: 0px;
  padding-right: 16px;
}
```

### Links (66 instances)

```css
.link {
  color: rgb(35, 33, 44);
  font-size: 18px;
  font-weight: 400;
}
```

### Navigation (2 instances)

```css
.navigatio {
  color: rgb(35, 33, 44);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 26px;
  padding-right: 26px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(35, 33, 44);
  padding-top: 32px;
  padding-bottom: 24px;
  font-size: 16px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(221, 80, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 12px;
  border: 0px none rgb(221, 80, 0);
  font-size: 18px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(35, 33, 44);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(35, 33, 44);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(35, 33, 44);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(35, 33, 44);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(178, 24, 164);
  padding: 0px 8px 0px 8px;
  border-radius: 64px;
  border: 0px none rgb(178, 24, 164);
  font-size: 22px;
  font-weight: 400;
```

## Layout System

**0 grid containers** and **45 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 34x |
| row/wrap | 11x |

**Gap values:** `16px`, `4px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 92/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance

**Issues:**
- 100% of CSS is unused — consider purging
- 1358 duplicate CSS declarations

## Z-Index Map

**7 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,2147483630 | div.s.c.-.3.6.d.d.7.d.5.9.-.2. .t.K.z.y.w. .h.e.a.d.r.o.o.m.-.w.r.a.p.p.e.r, div.s.c.-.5.6.9.a.d.6.9.7.-.0. .s.c.-.e.1.6.6.2.d.9.1.-.2. .h.q.y.r.O.r. .b.L.T.P.i.a, div.s.c.-.5.6.9.a.d.6.9.7.-.0. .f.a.Y.z.S.U |
| sticky | 10,10 | div.s.c.-.5.6.9.a.d.6.9.7.-.0. .k.L.w.i.c.d, div.s.c.-.5.6.9.a.d.6.9.7.-.0. .k.L.w.i.c.d, div.s.c.-.5.6.9.a.d.6.9.7.-.0. .k.L.w.i.c.d |
| base | 1,1 | div.h.e.a.d.r.o.o.m. .h.e.a.d.r.o.o.m.-.-.u.n.f.i.x.e.d |

**Issues:**
- [object Object]

## SVG Icons

**8 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 7 |

**Icon colors:** `currentColor`, `rgb(255, 255, 255)`, `rgb(221, 80, 0)`, `rgb(35, 33, 44)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| fonts | self-hosted | 300 | normal |
| neue-haas-unica | self-hosted | 300, 400, 500, 600 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 6 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 4 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (6x), 3:2 (2x), 16:9 (2x), 1:1 (1x)

## Motion Language

**Feel:** springy · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **ease-in-out** (5 uses) — `ease`
- **custom** (4 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **spring** (4 uses) — `cubic-bezier(0.665, 0.425, 0.44, 1.105)`

### Spring / Overshoot Easings

- `cubic-bezier(0.665, 0.425, 0.44, 1.105)`

## Component Anatomy

### button — 5 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **all** (1)
- **date** (1)
- **guests** (1)
- **book** (1)

### Button Copy Patterns

- "all regions" (1×)
- "date
date" (1×)
- "2 guests" (1×)
- "book your stay" (1×)

### Sample Headings

> Book restful space outside your daily routine.
> Take a break from big city life in smart cabins close to your home.
> From our journal
> Anne-Christin shares: her time in a design cabin
> Beatrice shares: From a dog-friendly getaway
> Book restful space outside your daily routine.
> Take a break from big city life in smart cabins close to your home.
> From our journal
> Anne-Christin shares: her time in a design cabin
> Beatrice shares: From a dog-friendly getaway

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** Escape everyday life and embark on an adventure: enjoy relaxing days in idyllic cabins ▶ Book your holiday in Germany or Austria now

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → nav → content → content → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.4 |
| 2 | nav | — | 0.9 |
| 3 | content | Book restful space outside your daily routine. | 0.3 |
| 4 | content | Book restful space outside your daily routine. | 0.3 |
| 5 | content | Take a break from big city life in smart cabins close to your home. | 0.3 |
| 6 | content | From our journal | 0.3 |
| 7 | footer | Sign up for updates & special deals and get 10% off your next stay! | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.542 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 99px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.182)
**Counts:** total 11, svg 0, icon 0, screenshot-like 0, photo-like 4
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `neue-haas-unica` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
