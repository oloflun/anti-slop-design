# Design Language: Diamond Rose Sanctuary • Nature Retreat & Wellness Center

> Extracted from `https://diamondrosesanctuary.com` on September 4, 2026
> 814 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#dfd7c9` | rgb(223, 215, 201) | hsl(38, 26%, 83%) | 680 |
| Secondary | `#20462b` | rgb(32, 70, 43) | hsl(137, 37%, 20%) | 5 |
| Accent | `#1a3822` | rgb(26, 56, 34) | hsl(136, 37%, 16%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#303030` | hsl(0, 0%, 19%) | 821 |
| `#000000` | hsl(0, 0%, 0%) | 49 |

### Background Colors

Used on large-area elements: `#dfd7c9`, `#f2eada`, `#20462b`, `#112617`

### Text Colors

Text color palette: `#000000`, `#303030`, `#dfd7c9`, `#f2eada`, `#ff5e5e`

### Gradients

```css
background-image: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.08) 51%, rgba(0, 0, 0, 0.6));
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.15) 50%, rgba(0, 0, 0, 0.5));
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, 0.83));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#303030` | text, border, background | 821 |
| `#dfd7c9` | background, text, border | 680 |
| `#f2eada` | background, text, border | 86 |
| `#000000` | text, border | 49 |
| `#20462b` | background | 5 |
| `#ff5e5e` | text, border | 4 |
| `#1a3822` | background | 1 |
| `#112617` | background | 1 |

## Typography

### Font Families

- **Aime** — used for all (539 elements)
- **NM** — used for body (250 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 75.52px | 4.72rem | 300 | 64.192px | -3.776px | h1, span |
| 74.24px | 4.64rem | 300 | 63.104px | -3.712px | h1, span |
| 61.44px | 3.84rem | 300 | 55.296px | -2.4576px | h2, div |
| 58.88px | 3.68rem | 300 | 52.992px | -2.3552px | h2, div |
| 51.2px | 3.2rem | 300 | 46.08px | -2.048px | h1, div, h2 |
| 40.96px | 2.56rem | 300 | 36.864px | -1.2288px | div, img |
| 40.32px | 2.52rem | 300 | 36.288px | -1.2096px | div |
| 39.68px | 2.48rem | 300 | 35.712px | -1.5872px | h2, br, div |
| 35.84px | 2.24rem | 300 | 35.84px | -1.4336px | h2, h3, br |
| 32px | 2rem | 300 | 38.4px | -0.96px | div |
| 26.88px | 1.68rem | 300 | 28.224px | -0.512px | label |
| 19.2px | 1.2rem | 300 | 20.16px | -0.384px | div |
| 16.64px | 1.04rem | 400 | 17.472px | normal | a, span |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 12.8px | 0.8rem | 300 | 13.44px | -0.512px | body, header, div, link |

### Heading Scale

```css
h1 { font-size: 75.52px; font-weight: 300; line-height: 64.192px; }
h1 { font-size: 74.24px; font-weight: 300; line-height: 63.104px; }
h2 { font-size: 61.44px; font-weight: 300; line-height: 55.296px; }
h2 { font-size: 58.88px; font-weight: 300; line-height: 52.992px; }
h1 { font-size: 51.2px; font-weight: 300; line-height: 46.08px; }
h2 { font-size: 39.68px; font-weight: 300; line-height: 35.712px; }
h2 { font-size: 35.84px; font-weight: 300; line-height: 35.84px; }
```

### Body Text

```css
body { font-size: 11.52px; font-weight: 300; line-height: 12.096px; }
```

### Font Weights in Use

`300` (539x), `400` (274x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-24 | 24px | 1.5rem |
| spacing-42 | 42px | 2.625rem |
| spacing-50 | 50px | 3.125rem |
| spacing-73 | 73px | 4.5625rem |
| spacing-77 | 77px | 4.8125rem |
| spacing-86 | 86px | 5.375rem |
| spacing-120 | 120px | 7.5rem |
| spacing-141 | 141px | 8.8125rem |
| spacing-152 | 152px | 9.5rem |
| spacing-182 | 182px | 11.375rem |
| spacing-192 | 192px | 12rem |
| spacing-217 | 217px | 13.5625rem |
| spacing-254 | 254px | 15.875rem |
| spacing-280 | 280px | 17.5rem |
| spacing-313 | 313px | 19.5625rem |
| spacing-320 | 320px | 20rem |
| spacing-379 | 379px | 23.6875rem |
| spacing-384 | 384px | 24rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 11 |
| full | 100px | 8 |

## CSS Custom Properties

### Other

```css
--beige: #dfd7c9;
--black: #303030;
--beige-2nd: #f2eada;
--green: #20462b;
--dark-green: #112617;
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

## Transitions & Animations

**Durations:** `0.4s`, `0.45s`

### Common Transitions

```css
transition: all;
transition: 0.4s;
transition: 0.45s;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**arrows-bounce**
```css
@keyframes arrows-bounce {
  0% { transform: translateY(0px); }
  50% { transform: translateY(10px); }
  100% { transform: translateY(0px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (13 instances)

```css
.button {
  background-color: rgba(223, 215, 201, 0.08);
  color: rgb(48, 48, 48);
  font-size: 10.24px;
  font-weight: 300;
  padding-top: 16px;
  padding-right: 50.4px;
  border-radius: 2px;
}
```

### Cards (4 instances)

```css
.card {
  border-radius: 4px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (2 instances)

```css
.input {
  background-color: rgba(223, 215, 201, 0.15);
  color: rgb(223, 215, 201);
  border-color: rgb(0, 0, 0);
  border-radius: 4px;
  font-size: 12.8px;
  padding-top: 12px;
  padding-right: 16px;
}
```

### Links (39 instances)

```css
.link {
  color: rgb(48, 48, 48);
  font-size: 10.24px;
  font-weight: 300;
}
```

### Navigation (3 instances)

```css
.navigatio {
  background-color: rgb(242, 234, 218);
  color: rgb(48, 48, 48);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (20 instances)

```css
.foote {
  background-color: rgb(17, 38, 23);
  color: rgb(48, 48, 48);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12.8px;
}
```

### Modals (4 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (15 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(48, 48, 48);
  padding-top: 0px;
}
```

### Badges (7 instances)

```css
.badge {
  color: rgb(48, 48, 48);
  font-size: 11.52px;
  font-weight: 300;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(48, 48, 48);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(48, 48, 48);
  font-size: 12.8px;
  font-weight: 300;
```

### Button — 11 instances, 4 variants

**Variant 1** (5 instances)

```css
  background: rgb(26, 56, 34);
  color: rgb(223, 215, 201);
  padding: 0px 30.72px 0px 30.72px;
  border-radius: 0px;
  border: 0px none rgb(223, 215, 201);
  font-size: 10.24px;
  font-weight: 300;
```

**Variant 2** (1 instance)

```css
  background: rgb(242, 234, 218);
  color: rgb(48, 48, 48);
  padding: 0px 30.72px 0px 30.72px;
  border-radius: 0px;
  border: 0px none rgb(48, 48, 48);
  font-size: 10.24px;
  font-weight: 300;
```

**Variant 3** (1 instance)

```css
  background: rgba(223, 215, 201, 0.08);
  color: rgb(223, 215, 201);
  padding: 18.4px 34.4px 18.4px 34.4px;
  border-radius: 2px;
  border: 1px dashed rgba(223, 215, 201, 0.65);
  font-size: 10.24px;
  font-weight: 300;
```

**Variant 4** (4 instances)

```css
  background: rgba(223, 215, 201, 0.08);
  color: rgb(48, 48, 48);
  padding: 16px 50.4px 16px 50.4px;
  border-radius: 2px;
  border: 1px dashed rgb(48, 48, 48);
  font-size: 10.24px;
  font-weight: 300;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(48, 48, 48);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(48, 48, 48);
  font-size: 12.8px;
  font-weight: 300;
```

### Link — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(48, 48, 48);
  padding: 0px 0px 0px 0px;
  border-radius: 4px;
  border: 0px none rgb(48, 48, 48);
  font-size: 12.8px;
  font-weight: 300;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(48, 48, 48);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(48, 48, 48);
  font-size: 12.8px;
  font-weight: 300;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(223, 215, 201, 0.15);
  color: rgb(223, 215, 201);
  padding: 12px 16px 12px 16px;
  border-radius: 4px;
  border: 0px none rgb(0, 0, 0);
  font-size: 12.8px;
  font-weight: 300;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(242, 234, 218);
  color: rgba(242, 234, 218, 0);
  padding: 9px 15px 9px 15px;
  border-radius: 0px;
  border: 0px none rgba(242, 234, 218, 0);
  font-size: 12.8px;
  font-weight: 300;
```

## Layout System

**3 grid containers** and **113 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1280px | 0px |
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 2x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 426.656px 426.672px 426.656px;
grid-template-columns: 206.797px 206.797px;
gap: 16px 12px;
grid-template-columns: 206.797px 206.797px;
gap: 16px 12px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 67x |
| column/nowrap | 46x |

**Gap values:** `10px`, `10px normal`, `16px 12px`, `16px normal`, `4px normal`, `6px normal`, `8px normal`, `normal 10px`, `normal 12px`, `normal 2%`, `normal 24px`, `normal 6px`, `normal 8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 85/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 82/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 44 !important rules — prefer specificity over overrides
- 83% of CSS is unused — consider purging
- 3536 duplicate CSS declarations

## Gradients

**3 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 3 | bold |
| linear | — | 3 | bold |
| linear | — | 3 | bold |

```css
background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.08) 51%, rgba(0, 0, 0, 0.6));
background: linear-gradient(rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.15) 50%, rgba(0, 0, 0, 0.5));
background: linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, 0.83));
```

## Z-Index Map

**9 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,90 | div.o.v.e.r.l.a.y, section.t.h.e._.s.t.o.r.y, section.c.t.a._.b.o.x |
| base | 1,6 | main.h.e.r.o, div.h.e.r.i.t.a.g.e._.i.m.g._.l.e.f.t, div.h.e.r.i.t.a.g.e._.i.m.g._.r.i.g.h.t |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| Aime | self-hosted | 300 | normal |
| NM | self-hosted | 400, 500 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 6 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 4 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (7x), 3:2 (4x), 1:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `400ms` | 400 |
| `lg` | `450ms` | 450 |

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `arrows-bounce` | slide-y | transform | 1 |

## Component Anatomy

### button — 17 instances

**Slots:** label

### link — 2 instances


### card — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **b** (5)
- **d** (5)
- **a** (2)
- **r** (2)
- **discover** (2)
- **c** (1)
- **j** (1)

### Button Copy Patterns

- "b
o
o
k
 
y
o
u
r
 
s
t
a
y" (2×)
- "a
b
o
u
t
 
u
s" (2×)
- "d
e
t
a
i
l
s
r
e
g
i
s
t
e
r" (2×)
- "d
e
t
a
i
l
s" (2×)
- "r
e
g
i
s
t
e
r" (2×)
- "b
o
o
k
 
n
o
w
c
o
n
t
a
c
t
 
u
s" (1×)
- "b
o
o
k
 
n
o
w" (1×)
- "c
o
n
t
a
c
t
 
u
s" (1×)
- "j
o
i
n
 
a
 
r
e
t
r
e
a
t" (1×)
- "b
o
o
k
 
y
o
u
r
 
s
t
a
y
d
i
s
c
o
v
e
r
 
o
n
 
a
i
r
b
n
b" (1×)

### Sample Headings

> DIAMOND ROSE
> SANCTUARY
> A Nature Preserve
to Rest & Rise
> PRESERVED LAND.
OPEN WATER
> THE HOUSE
AWAITS
> HOW THE SPACE IS LIVED IN
> RETREATS WITHIN
THESE WALLS
> FORMING IN
THE LIGHT
> A NEW CHAPTER
BEGINS
> A PURPOSE-BUILT
SPACE FOR HEALING

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** Escape to Diamond Rose Sanctuary, a nature preserve for rest and renewal. Join upcoming retreats, book your stay, or rent our Temple Lotus space.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → hero → testimonial → content → testimonial → pricing-table → testimonial → testimonial → hero → content → cta

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | hero | DIAMOND ROSE | 0.85 |
| 2 | testimonial | — | 0.8 |
| 3 | content | PRESERVED LAND.
OPEN WATER | 0.3 |
| 4 | testimonial | HOW THE SPACE IS LIVED IN | 0.8 |
| 5 | pricing-table | RETREATS WITHIN
THESE WALLS | 0.9 |
| 6 | testimonial | FORMING IN
THE LIGHT | 0.8 |
| 7 | testimonial | FORMING IN
THE LIGHT | 0.8 |
| 8 | hero | REMEMBER HOW
IT FEELS TO BREATHE | 0.4 |
| 9 | content | — | 0.3 |
| 10 | cta | — | 0.75 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.308 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 3 |

## Imagery Style

**Label:** `photography` (confidence 0.417)
**Counts:** total 12, svg 0, icon 1, screenshot-like 0, photo-like 8
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Aime` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
