# Design Language: Shaping Extraordinary | Geon

> Extracted from `https://geon.au/` on September 4, 2026
> 594 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f2eeea` | rgb(242, 238, 234) | hsl(30, 24%, 93%) | 943 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#867c73` | hsl(28, 8%, 49%) | 177 |
| `#000000` | hsl(0, 0%, 0%) | 106 |
| `#34312e` | hsl(30, 6%, 19%) | 14 |
| `#6c645c` | hsl(30, 8%, 39%) | 11 |
| `#5e5853` | hsl(27, 6%, 35%) | 7 |
| `#474340` | hsl(26, 5%, 26%) | 3 |
| `#ffffff` | hsl(0, 0%, 100%) | 1 |

### Background Colors

Used on large-area elements: `#867c73`, `#353330`, `#000000`, `#f2eeea`, `#5e5853`, `#474340`, `#34312e`, `#6c645c`

### Text Colors

Text color palette: `#000000`, `#f2eeea`, `#867c73`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#f2eeea` | text, border, background | 943 |
| `#867c73` | background, text, border | 177 |
| `#000000` | text, border, background | 106 |
| `#34312e` | background | 14 |
| `#6c645c` | background | 11 |
| `#5e5853` | background | 7 |
| `#474340` | background | 3 |
| `#ffffff` | border | 1 |

## Typography

### Font Families

- **Monument Grotesk** — used for all (539 elements)
- **Times New Roman** — used for body (33 elements)
- **GT Super Text** — used for body (21 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 65px | 4.0625rem | 500 | 55.25px | -0.65px | p |
| 33px | 2.0625rem | 500 | 33px | -0.99px | p, div |
| 24px | 1.5rem | 500 | normal | -0.24px | a, span, h4, div |
| 18px | 1.125rem | 400 | 18px | 1.08px | div, button, p, span |
| 16px | 1rem | 400 | normal | normal | html, head, meta, style |
| 15px | 0.9375rem | 400 | normal | 0.15px | body, div, p, iframe |
| 13px | 0.8125rem | 400 | normal | 0.15px | a |
| 12px | 0.75rem | 400 | normal | 0.72px | button, p, a, span |
| 11px | 0.6875rem | 500 | normal | 0.66px | p, a, div |

### Heading Scale

```css
h4 { font-size: 24px; font-weight: 500; line-height: normal; }
h4 { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (483x), `500` (110x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-79 | 79px | 4.9375rem |
| spacing-108 | 108px | 6.75rem |
| spacing-146 | 146px | 9.125rem |
| spacing-225 | 225px | 14.0625rem |
| spacing-272 | 272px | 17rem |
| spacing-308 | 308px | 19.25rem |
| spacing-427 | 427px | 26.6875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 1px | 6 |
| sm | 5px | 33 |
| md | 10px | 28 |
| full | 100px | 1 |
| full | 1280px | 2 |

## CSS Custom Properties

### Colors

```css
--swiper-theme-color: #007aff;
```

### Spacing

```css
--swiper-navigation-size: 44px;
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
| 400px | 400px | max-width |
| sm | 650px | max-width |
| md | 768px | max-width |
| 920px | 920px | max-width |
| lg | 970px | max-width |
| lg | 1024px | max-width |
| 1200px | 1200px | max-width |
| xl | 1270px | max-width |
| xl | 1300px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.85s`, `0.3s`, `0.5s`, `1.2s`, `0.25s`, `0.65s`, `1.25s`, `0.2s`, `1s`

### Common Transitions

```css
transition: all;
transition: transform 0.85s;
transition: color 0.3s;
transition: opacity 0.5s;
transition: transform 1.2s;
transition: background-color 0.25s;
transition: opacity 0.25s;
transition: color 0.25s ease-in-out, background-color 0.25s ease-in-out;
transition: background 0.3s;
transition: opacity 0.5s linear;
```

### Keyframe Animations

**fadeIn**
```css
@keyframes fadeIn {
  0% { opacity: 0; transform: translateY(-20px); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**fadeOut**
```css
@keyframes fadeOut {
  0% { opacity: 1; transform: translateY(0px); }
  100% { opacity: 0; transform: translateY(20px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (12 instances)

```css
.button {
  background-color: rgba(236, 231, 228, 0.1);
  color: rgb(242, 238, 234);
  font-size: 18px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Inputs (17 instances)

```css
.input {
  color: rgb(134, 124, 115);
  border-color: rgba(135, 124, 115, 0.082);
  border-radius: 5px;
  font-size: 15px;
  padding-top: 10px;
  padding-right: 15px;
}
```

### Links (44 instances)

```css
.link {
  color: rgb(242, 238, 234);
  font-size: 15px;
  font-weight: 400;
}
```

### Footer (2 instances)

```css
.foote {
  color: rgb(242, 238, 234);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 15px;
}
```

### Modals (3 instances)

```css
.modal {
  background-color: rgb(53, 51, 48);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (15 instances)

```css
.dropdown {
  background-color: rgb(53, 51, 48);
  border-radius: 0px;
  border-color: rgb(134, 124, 115) rgb(134, 124, 115) rgba(255, 255, 255, 0.1);
  padding-top: 0px;
}
```

### Badges (5 instances)

```css
.badge {
  background-color: rgba(0, 0, 0, 0.1);
  color: rgb(242, 238, 234);
  font-size: 11px;
  font-weight: 500;
  padding-top: 10px;
  padding-right: 10px;
  border-radius: 5px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 6 instances, 2 variants

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(242, 238, 234);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(242, 238, 234);
  font-size: 12px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgba(236, 231, 228, 0.1);
  color: rgb(242, 238, 234);
  padding: 10px 15px 10px 15px;
  border-radius: 5px;
  border: 0px none rgb(242, 238, 234);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0.1);
  color: rgb(242, 238, 234);
  padding: 0px 0px 0px 0px;
  border-radius: 100%;
  border: 0px none rgb(242, 238, 234);
  font-size: 15px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(134, 124, 115);
  padding: 10px 15px 10px 20px;
  border-radius: 5px;
  border: 1px solid rgba(135, 124, 115, 0.082);
  font-size: 15px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(134, 124, 115);
  padding: 20px 15px 10px 20px;
  border-radius: 5px;
  border: 1px solid rgba(135, 124, 115, 0.082);
  font-size: 15px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(242, 238, 234);
  padding: 10px 15px 10px 20px;
  border-radius: 5px;
  border: 1px solid rgba(236, 232, 228, 0.16);
  font-size: 15px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **116 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1800px | 0px |
| 1400px | 0px |
| 100% | 0px |
| 2041px | 0px |
| 1920px | 0px |
| 2494px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 600px 600px;
gap: 20px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/wrap | 3x |
| row/nowrap | 94x |
| column/nowrap | 19x |

**Gap values:** `10px`, `12px`, `20px`, `30px`, `50px`, `60px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 85/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 8 !important rules — prefer specificity over overrides
- 68% of CSS is unused — consider purging
- 767 duplicate CSS declarations

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9999,99998 | div.i.n.n.e.r. .f.a.d.e.-.-.i.n, header.m.a.s.t.h.e.a.d, div.o.v.e.r.l.a.y.-.-.b.g |
| dropdown | 222,222 | div.c.h.e.c.k.m.a.r.k |
| base | 0,4 | video.f.o.o.t.e.r.-.v.i.d.e.o. .b.g.-.i.m.a.g.e. .f.i.x.e.d.-.b.g. .b.r.-.0.8, button.l.i.n.k. .b.u.t.t.o.n. .e.n.q.u.i.r.e.-.b.t.n, main.p.a.g.e.-.-.t.r.a.n.s.i.t.i.o.n |

**Issues:**
- [object Object]

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| swiper-icons | self-hosted | 400 | normal |
| GT Super Text | self-hosted | 400 | normal |
| Monument Grotesk | self-hosted | 400, 500 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 18 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 9 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 2 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (13x), 16:9 (9x), 3:2 (8x)

## Motion Language

**Feel:** mechanical · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `850ms` | 850 |
| `xxl` | `1.25s` | 1250 |

### Easing Families

- **ease-in-out** (3 uses) — `ease`
- **linear** (38 uses) — `linear`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `fadeIn` | slide-y | opacity, transform | 1 |

## Component Anatomy

### button — 9 instances

**Slots:** label
**Variants:** link
**Sizes:** sm

| variant | count | sample label |
|---|---|---|
| default | 7 | CLOSE |
| link | 2 | ENQUIRE |

### input — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** unknown (tight)

### Top CTA Verbs

- **close** (1)
- **phone** (1)
- **email** (1)
- **enquire** (1)
- **menu** (1)

### Button Copy Patterns

- "close" (1×)
- "phone" (1×)
- "email" (1×)
- "enquire" (1×)
- "menu" (1×)

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Shaping the Extraordinary

Alternates: legal (0.4)

## Section Roles

Reading order (top→bottom): nav → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | content | — | 0.3 |
| 2 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.082 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 1280px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.25)
**Counts:** total 30, svg 15, icon 0, screenshot-like 0, photo-like 11
**Dominant aspect:** landscape
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Monument Grotesk` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
