# Design Language: Snapifye - Webflow HTML website template

> Extracted from `https://snapifye.webflow.io/` on September 4, 2026
> 919 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f9dcc5` | rgb(249, 220, 197) | hsl(27, 81%, 87%) | 172 |
| Secondary | `#701e1f` | rgb(112, 30, 31) | hsl(359, 58%, 28%) | 807 |
| Accent | `#ff2f2f` | rgb(255, 47, 47) | hsl(0, 100%, 59%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#ffffff` | hsl(0, 0%, 100%) | 80 |
| `#000000` | hsl(0, 0%, 0%) | 54 |
| `#161616` | hsl(0, 0%, 9%) | 7 |
| `#474747` | hsl(0, 0%, 28%) | 6 |
| `#222222` | hsl(0, 0%, 13%) | 3 |

### Background Colors

Used on large-area elements: `#f9dcc5`, `#701e1f`, `#ec7672`, `#401714`

### Text Colors

Text color palette: `#000000`, `#701e1f`, `#f9dcc5`, `#401714`, `#ffffff`, `#ec7672`, `#161616`

### Gradients

```css
background-image: linear-gradient(25deg, rgb(77, 245, 164), rgb(225, 255, 44));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#701e1f` | text, border, background | 807 |
| `#ec7672` | background, text, border | 486 |
| `#401714` | text, border, background | 299 |
| `#f9dcc5` | background, text, border | 172 |
| `#ffffff` | text, border, background | 80 |
| `#000000` | text, border | 54 |
| `#161616` | text, border | 7 |
| `#474747` | background | 6 |
| `#222222` | background | 3 |
| `#ff2f2f` | background | 1 |
| `#172b1d` | background | 1 |
| `#293c2f` | background | 1 |

## Typography

### Font Families

- **Gt Walsheim Trial** — used for all (862 elements)
- **Librecaslontext** — used for body (23 elements)
- **PT Sans** — used for body (5 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 184px | 11.5rem | 900 | 147.2px | -0.8px | div, h1, strong |
| 158.113px | 9.8821rem | 900 | 158.113px | normal | a, div, svg, path |
| 133.334px | 8.3334rem | 900 | 106.667px | normal | h1, div, h2 |
| 113.208px | 7.0755rem | 900 | 90.5664px | normal | h2, span, div |
| 66.792px | 4.1745rem | 400 | 58.109px | normal | div |
| 60px | 3.75rem | 700 | 60px | normal | a |
| 47.5462px | 2.9716rem | 700 | 47.5462px | normal | h2, span |
| 46.5875px | 2.9117rem | 700 | 51.2463px | normal | blockquote, em |
| 24px | 1.5rem | 400 | 24px | normal | div, a, img |
| 23.4336px | 1.4646rem | 400 | 23.4336px | normal | body, div, svg, circle |
| 23.2458px | 1.4529rem | 700 | 23.2458px | normal | p |
| 20px | 1.25rem | 400 | 20px | normal | div |
| 18px | 1.125rem | 400 | 18px | normal | div, a |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14px | 0.875rem | 400 | 14px | normal | div, a, img |

### Heading Scale

```css
h1 { font-size: 184px; font-weight: 900; line-height: 147.2px; }
h1 { font-size: 133.334px; font-weight: 900; line-height: 106.667px; }
h2 { font-size: 113.208px; font-weight: 900; line-height: 90.5664px; }
h2 { font-size: 47.5462px; font-weight: 700; line-height: 47.5462px; }
```

### Body Text

```css
body { font-size: 23.4336px; font-weight: 400; line-height: 23.4336px; }
```

### Font Weights in Use

`400` (698x), `900` (179x), `700` (30x), `500` (10x)

## Spacing

**Base unit:** 5px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-40 | 40px | 2.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-115 | 115px | 7.1875rem |
| spacing-120 | 120px | 7.5rem |
| spacing-140 | 140px | 8.75rem |
| spacing-175 | 175px | 10.9375rem |
| spacing-180 | 180px | 11.25rem |
| spacing-203 | 203px | 12.6875rem |
| spacing-265 | 265px | 16.5625rem |
| spacing-420 | 420px | 26.25rem |
| spacing-440 | 440px | 27.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 4 |
| md | 8px | 5 |
| lg | 12px | 36 |
| lg | 16px | 2 |
| xl | 20px | 4 |
| xl | 24px | 6 |
| full | 40px | 16 |
| full | 50px | 4 |
| full | 60px | 4 |
| full | 99px | 2 |

## CSS Custom Properties

### Colors

```css
--color--secondary: #f9dcc5;
--color--primary: #701e1f;
--color--transparent: transparent;
--_size-variables---border-radius--radius-24: 24px;
--color--grey: #f7f7f7;
--_size-variables---border-radius--radius-32: 32px;
--color--white: white;
--color--tertiary: #401714;
--color--black: black;
--_size-variables---border-radius--radius-10: 10px;
--color--sage-green: #1a683f;
--color--salmon: #ec7672;
--_size-variables---border-radius--radius-16: 16px;
--color-white-2<deleted|variable-669e398d-e0b9-4945-dd67-db7a47faee68>: white;
--color--golden-olive: #c4b84e;
--_size-variables---border-radius--radius-40: 40px;
--_size-variables---border-radius--radius-12: 12px;
--_size-variables---border-radius--radius-8: 8px;
--_size-variables---border-radius--radius-20: 20px;
--_size-variables---border-radius--radius-4: 4px;
--_size-variables---border-radius--radius-6: 6px;
```

### Spacing

```css
--_size-variables---spacing--spacing-12: 12px;
--_size-variables---section-padding--padding-80: 80px;
--_size-variables---section-padding--padding-180: 180px;
--_size-variables---section-padding--padding-100: 100px;
--_size-variables---section-padding--padding-60: 60px;
--_size-variables---section-padding--padding-140: 140px;
--_size-variables---section-padding--padding-160: 160px;
--_size-variables---spacing--spacing-48: 48px;
--_size-variables---spacing--spacing-24: 24px;
--_size-variables---spacing--spacing-80: 80px;
--_size-variables---spacing--spacing-32: 32px;
--_size-variables---spacing--spacing-40: 40px;
--_size-variables---spacing--spacing-60: 60px;
--_size-variables---section-padding--padding-120: 120px;
--_size-variables---spacing--spacing-28: 28px;
--_size-variables---spacing--spacing-16: 16px;
--_size-variables---spacing--spacing-20: 20px;
--_size-variables---spacing--spacing-8: 8px;
--_size-variables---spacing--spacing-44: 44px;
--_size-variables---spacing--spacing-4: 4px;
--_size-variables---section-padding--padding-150: 150px;
--_size-variables---spacing--spacing-36: 36px;
--_size-variables---spacing--spacing-52: 52px;
--_size-variables---spacing--spacing-56: 56px;
--_size-variables---spacing--spacing-64: 64px;
--_size-variables---spacing--spacing-68: 68px;
--_size-variables---spacing--spacing-72: 72px;
--_size-variables---spacing--spacing-76: 76px;
```

### Typography

```css
--font-family--body: "Gt Walsheim Trial", Arial, sans-serif;
--font-family--heading: "Gt Walsheim Trial", Arial, sans-serif;
--font-family--italic-style: Librecaslontext, Arial, sans-serif;
```

### Other

```css
--white-2<deleted|variable-5d68e527-7ed7-8628-2256-8ab60621eac4>: white;
--white<deleted|variable-16ce4c6c>: white;
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
| lg | 992px | min-width |
| xl | 1280px | min-width |
| 1440px | 1440px | min-width |
| 1920px | 1920px | min-width |

## Transitions & Animations

**Durations:** `0.25s`, `0.1s`, `0.3s`, `0.35s`

### Common Transitions

```css
transition: all;
transition: text-decoration-color 0.25s;
transition: background-color 0.1s, color 0.1s;
transition: text-decoration-color 0.3s;
transition: color 0.3s;
transition: background-color 0.35s;
transition: color 0.35s, background-color 0.35s;
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

### Buttons (24 instances)

```css
.button {
  background-color: rgba(34, 34, 34, 0.4);
  color: rgb(236, 118, 114);
  font-size: 23.4336px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (46 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 12px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (61 instances)

```css
.link {
  color: rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
}
```

### Navigation (36 instances)

```css
.navigatio {
  background-color: rgb(236, 118, 114);
  color: rgb(112, 30, 31);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (11 instances)

```css
.foote {
  background-color: rgb(64, 23, 20);
  color: rgb(236, 118, 114);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 23.4336px;
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

### Dropdowns (22 instances)

```css
.dropdown {
  background-color: rgb(249, 220, 197);
  border-radius: 0px;
  border-color: rgb(112, 30, 31);
  padding-top: 0px;
}
```

### Tooltips (12 instances)

```css
.tooltip {
  background-color: rgb(71, 71, 71);
  color: rgb(255, 255, 255);
  font-size: 23.4336px;
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 26 instances, 2 variants

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

**Variant 2** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 184px;
  font-weight: 900;
```

### Button — 18 instances, 2 variants

**Variant 1** (17 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 24px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(64, 23, 20);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(64, 23, 20);
  font-size: 158.113px;
  font-weight: 900;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(249, 220, 197);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

### Button — 17 instances, 1 variant

**Variant 1** (17 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

### Button — 52 instances, 3 variants

**Variant 1** (20 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 184px;
  font-weight: 900;
```

**Variant 2** (10 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(64, 23, 20);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(64, 23, 20);
  font-size: 23.4336px;
  font-weight: 400;
```

**Variant 3** (22 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(236, 118, 114);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(236, 118, 114);
  font-size: 23.4336px;
  font-weight: 400;
```

### Other — 38 instances, 2 variants

**Variant 1** (16 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 900;
```

**Variant 2** (22 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(236, 118, 114);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(236, 118, 114);
  font-size: 23.4336px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

### Link — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(112, 30, 31);
  padding: 0px 0px 0px 0px;
  border-radius: 40px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(64, 23, 20);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(64, 23, 20);
  font-size: 23.4336px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(64, 23, 20);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(64, 23, 20);
  font-size: 158.113px;
  font-weight: 900;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(112, 30, 31);
  padding: 16px 30px 16px 30px;
  border-radius: 99px;
  border: 0px none rgb(112, 30, 31);
  font-size: 23.4336px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 23.4336px;
  font-weight: 400;
```

## Layout System

**2 grid containers** and **180 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1440px | 0px |
| 370px | 0px |
| 100% | 0px |
| 380px | 0px |
| 1380px | 0px |
| 405px | 0px |
| 319px | 0px |
| 850px | 0px |
| 447px | 0px |
| 653px | 0px |
| 440px | 0px |
| 1050px | 0px |
| 1100px | 0px |
| 680px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 2x |

### Grid Templates

```css
grid-template-columns: 389.328px 389.328px 389.344px;
gap: 16px;
grid-template-columns: 1fr 1fr 1fr;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 123x |
| column/nowrap | 48x |
| row/wrap | 9x |

**Gap values:** `0px 25.6px`, `100px`, `10px`, `12px`, `16px`, `20px`, `23.04px`, `24px`, `25.6px`, `40px`, `44px`, `48px`, `8px`, `8px 25.6px`, `normal 25.6px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 88/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 40 !important rules — prefer specificity over overrides
- 84% of CSS is unused — consider purging
- 3561 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 25deg | 2 | brand |

```css
background: linear-gradient(25deg, rgb(77, 245, 164), rgb(225, 255, 44));
```

## Z-Index Map

**12 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div.n.a.v.b.a.r. .w.-.n.a.v |
| dropdown | 990,999 | div.s.a.l.e.s.-.c.t.a._.w.r.a.p, div.c.u.r.s.o.r.-.a.n.i.m.a.t.i.o.n.-.w.r.a.p, div.n.a.v.b.a.r.-.o.p.e.n.-.b.o.t.t.o.m |
| sticky | 10,99 | div.p.a.g.e.-.w.r.a.p.p.e.r, div.s.e.r.v.i.c.e.-.l.i.n.k.s, div.c.o.v.e.r.-.c.a.r.d.s._.a.n.i.m.a.t.i.o.n._.c.o.n.t.r.o.l.l.e.r |
| base | -100,6 | video, div.w.-.n.a.v.-.o.v.e.r.l.a.y, section.s.e.c.t.i.o.n.-.g.l.o.b.a.l.-.c.a.m.e.r.a.-.b.u.t.t.o.n |

**Issues:**
- [object Object]

## SVG Icons

**8 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| md | 1 |
| xl | 6 |

**Icon colors:** `white`, `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | normal | normal |
| Librecaslontext | self-hosted | 400 | normal, italic |
| Gt Walsheim Trial | self-hosted | 700, 900 | normal, italic |
| Inter Variable | self-hosted | 100 900 | normal |
| Open Sans | cdn | 300, 400, 600, 700, 800 | italic, normal |
| PT Sans | google-fonts | 400, 700 | italic, normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 13 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 8 | objectFit: cover, borderRadius: 0px, shape: square |
| avatar | 3 | objectFit: cover, borderRadius: 50%, shape: circular |
| thumbnail | 3 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (19x), 1:1 (6x), 3:2 (1x), 4:3 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `250ms` | 250 |
| `md` | `300ms` | 300 |

## Component Anatomy

### button — 120 instances

**Slots:** label
**Variants:** link · secondary
**Sizes:** small

| variant | count | sample label |
|---|---|---|
| default | 103 | Close |
| secondary | 16 | WEDDING
WEDDING |
| link | 1 | G
G
O
O
for click
&
&
S
S
H
H
A
A
R
R
E
 |

### other — 38 instances


### card — 16 instances

**Slots:** media

### link — 4 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** we-only · **Headings:** Title Case (verbose)

### Top CTA Verbs

- **e** (8)
- **g** (6)
- **o** (6)
- **s** (6)
- **explore** (6)
- **h** (4)
- **r** (4)
- **wedding** (4)

### Button Copy Patterns

- "e
e" (4×)
- "e" (4×)
- "explore all pages
explore all pages" (4×)
- "close" (3×)
- "o
o" (3×)
- "o" (3×)
- "404" (2×)
- "g
g
o
o
for click
&
&
s
s
h
h
a
a
r
r
e
e" (2×)
- "s
s" (2×)
- "s" (2×)

### Sample Headings

> V
I
N
T
A
G
E
> T
H
R
O
U
G
H
> L
E
N
S
> AT SNAPIFYE, WE ARE PASSIONATE STORYTELLERS, & CAPTURING TIMELESS MOMENTS WITH A TOUCH OF VINTAGE ELEGANCE.
> PHOTOGRAPHY AGENCY ✦ CREATIVE STUDIO ✦ BRANDING EXPERTS ✦ PHOTO & VIDEO SERVICES ✦ VISUAL STORYTELLERS ✦ PHOTOGRAPHY AGENCY
> PHOTOGRAPHY AGENCY ✦ CREATIVE STUDIO ✦ BRANDING EXPERTS ✦ PHOTO & VIDEO SERVICES ✦ VISUAL STORYTELLERS ✦ PHOTOGRAPHY AGENCY
> AT SNAPIFYE, OUR PHILOSOPHY CENTERS ON TRANSFORMING THE DIGITAL LANDSCAPE
> AT SNAPIFYE, WE ARE PASSIONATE STORYTELLERS, & CAPTURING TIMELESS MOMENTS WITH A TOUCH OF VINTAGE ELEGANCE.
> PHOTOGRAPHY AGENCY ✦ CREATIVE STUDIO ✦ BRANDING EXPERTS ✦ PHOTO & VIDEO SERVICES ✦ VISUAL STORYTELLERS ✦ PHOTOGRAPHY AGENCY
> PHOTOGRAPHY AGENCY ✦ CREATIVE STUDIO ✦ BRANDING EXPERTS ✦ PHOTO & VIDEO SERVICES ✦ VISUAL STORYTELLERS ✦ PHOTOGRAPHY AGENCY

## Page Intent

**Type:** `landing` (confidence 0.75)
**Description:** Snapifye is a modern Webflow photography template by Flowfye — designed for photographers to showcase portfolios with style, speed, and elegant motion.

## Section Roles

Reading order (top→bottom): nav → nav → hero → testimonial → content → content → content → content → feature-grid → content → hero → testimonial → content → content → pricing → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | hero | V
I
N
T
A
G
E | 0.85 |
| 3 | testimonial | AT SNAPIFYE, WE ARE PASSIONATE STORYTELLERS, & CAPTURING TIMELESS MOMENTS WITH A | 0.8 |
| 4 | content | AT SNAPIFYE, WE ARE PASSIONATE STORYTELLERS, & CAPTURING TIMELESS MOMENTS WITH A | 0.3 |
| 5 | content | — | 0.3 |
| 6 | content | — | 0.3 |
| 7 | content | — | 0.3 |
| 8 | feature-grid | — | 0.8 |
| 9 | content | PHOTOGRAPHY AGENCY ✦ CREATIVE STUDIO ✦ BRANDING EXPERTS ✦ PHOTO & VIDEO SERVICES | 0.3 |
| 10 | hero | AT SNAPIFYE, OUR PHILOSOPHY CENTERS ON TRANSFORMING THE DIGITAL LANDSCAPE | 0.85 |
| 11 | testimonial | — | 0.8 |
| 12 | content | — | 0.3 |
| 13 | content | — | 0.3 |
| 14 | pricing | we're a photo
S
H
O
O
T
I
N
G
A
N
D
V
I
N
T
A
G
E
V
I
S
U
A
L
S
T
U
D
I
O | 0.4 |
| 15 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.312 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 99px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `photography` (confidence 0.426)
**Counts:** total 27, svg 3, icon 4, screenshot-like 0, photo-like 21
**Dominant aspect:** portrait
**Radius profile on images:** soft

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Gt Walsheim Trial` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
