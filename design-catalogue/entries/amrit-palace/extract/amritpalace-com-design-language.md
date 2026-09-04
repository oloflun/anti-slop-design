# Design Language: Amrit Palace

> Extracted from `https://amritpalace.com` on September 4, 2026
> 1192 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#d49653` | rgb(212, 150, 83) | hsl(31, 60%, 58%) | 7 |
| Secondary | `#d8cbb8` | rgb(216, 203, 184) | hsl(36, 29%, 78%) | 603 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#2c2c2c` | hsl(0, 0%, 17%) | 1673 |
| `#000000` | hsl(0, 0%, 0%) | 74 |
| `#dfdad5` | hsl(30, 14%, 85%) | 49 |
| `#222222` | hsl(0, 0%, 13%) | 12 |
| `#efefef` | hsl(0, 0%, 94%) | 2 |
| `#bfb4a3` | hsl(36, 18%, 69%) | 1 |

### Background Colors

Used on large-area elements: `#d8cbb8`, `#000000`, `#2c2c2c`, `#d49653`, `#bfb4a3`, `#292622`

### Text Colors

Text color palette: `#000000`, `#2c2c2c`, `#d8cbb8`, `#222222`, `#dfdad5`, `#d49653`

### Gradients

```css
background-image: linear-gradient(rgb(16, 16, 16), rgba(16, 16, 16, 0.2));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#2c2c2c` | text, border, background | 1673 |
| `#d8cbb8` | background, text, border | 603 |
| `#000000` | text, border, background | 74 |
| `#dfdad5` | background, text, border | 49 |
| `#222222` | text, border | 12 |
| `#d49653` | background, text, border | 7 |
| `#efefef` | background | 2 |
| `#bfb4a3` | background | 1 |

## Typography

### Font Families

- **Satoshi** — used for body (899 elements)
- **TT Ramillas Variable** — used for all (254 elements)
- **webflow-icons** — used for body (3 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 176.64px | 11.04rem | 500 | 141.312px | -2.82624px | div |
| 102.4px | 6.4rem | 300 | 81.92px | -4.096px | h1, span, br |
| 61.44px | 3.84rem | 300 | 49.152px | -2.4576px | h1, span, h2, br |
| 57.6px | 3.6rem | 300 | 48.96px | -2.304px | h2, span, br |
| 44.8px | 2.8rem | 300 | 40.32px | -1.344px | h3, span, br |
| 37.12px | 2.32rem | 500 | 37.12px | -1.4848px | div |
| 23.04px | 1.44rem | 300 | 27.648px | -0.128px | div |
| 19.2px | 1.2rem | 300 | 19.2px | -0.672px | div |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 13.44px | 0.84rem | 500 | 13.44px | -0.128px | a, img, div |
| 12.8px | 0.8rem | 500 | 12.8px | -0.128px | body, div, link, img |
| 12.096px | 0.756rem | 500 | 16.9344px | -0.128px | div, a |
| 11.52px | 0.72rem | 500 | 16.128px | -0.128px | div, span, a, br |
| 10.88px | 0.68rem | 500 | 10.88px | -0.128px | div, span |
| 10.24px | 0.64rem | 500 | 10.24px | -0.128px | a, div, nav, img |

### Heading Scale

```css
h1 { font-size: 102.4px; font-weight: 300; line-height: 81.92px; }
h1 { font-size: 61.44px; font-weight: 300; line-height: 49.152px; }
h2 { font-size: 57.6px; font-weight: 300; line-height: 48.96px; }
h3 { font-size: 44.8px; font-weight: 300; line-height: 40.32px; }
```

### Body Text

```css
body { font-size: 10.88px; font-weight: 500; line-height: 10.88px; }
```

### Font Weights in Use

`500` (897x), `300` (254x), `400` (39x), `700` (2x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-40 | 40px | 2.5rem |
| spacing-52 | 52px | 3.25rem |
| spacing-62 | 62px | 3.875rem |
| spacing-78 | 78px | 4.875rem |
| spacing-90 | 90px | 5.625rem |
| spacing-128 | 128px | 8rem |
| spacing-147 | 147px | 9.1875rem |
| spacing-174 | 174px | 10.875rem |
| spacing-202 | 202px | 12.625rem |
| spacing-232 | 232px | 14.5rem |
| spacing-245 | 245px | 15.3125rem |
| spacing-250 | 250px | 15.625rem |
| spacing-275 | 275px | 17.1875rem |
| spacing-280 | 280px | 17.5rem |
| spacing-320 | 320px | 20rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 2 |

## CSS Custom Properties

### Colors

```css
--primary: #d49653;
--plyr-color-main: var(--colors--player-color);
```

### Other

```css
--biege: #d8cbb8;
--dark: #2c2c2c;
```

### Dependencies

```css
--plyr-color-main: --colors--player-color;
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
| sm | 480px | min-width |
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 991px | max-width |
| lg | 1024px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.45s`, `0.4s`, `0.35s`

### Common Transitions

```css
transition: all;
transition: 0.45s;
transition: 0.4s;
transition: 0.45s cubic-bezier(0.25, 0.46, 0.45, 0.94);
transition: 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**plyr-progress**
```css
@keyframes plyr-progress {
  100% { background-position: var(--plyr-progress-loading-size,25px) 0; }
}
```

**plyr-popup**
```css
@keyframes plyr-popup {
  0% { opacity: 0.5; transform: translateY(10px); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**plyr-fade-in**
```css
@keyframes plyr-fade-in {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**marquee**
```css
@keyframes marquee {
  0% { transform: translateX(0px); }
  100% { transform: translateX(-50%); }
}
```

**pulseAnim**
```css
@keyframes pulseAnim {
  0% { transform: scale(1); color: inherit; }
  50% { transform: scale(1.2); color: rgb(211, 107, 0); }
  100% { transform: scale(1); color: inherit; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (11 instances)

```css
.button {
  background-color: rgba(239, 239, 239, 0.3);
  color: rgb(44, 44, 44);
  font-size: 11.52px;
  font-weight: 500;
  padding-top: 4px;
  padding-right: 4px;
  border-radius: 0px;
}
```

### Cards (5 instances)

```css
.card {
  background-color: rgb(216, 203, 184);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (45 instances)

```css
.link {
  color: rgb(44, 44, 44);
  font-size: 11.52px;
  font-weight: 500;
}
```

### Navigation (23 instances)

```css
.navigatio {
  background-color: rgb(216, 203, 184);
  color: rgb(44, 44, 44);
  padding-top: 12px;
  padding-bottom: 12px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (54 instances)

```css
.foote {
  background-color: rgb(41, 38, 34);
  color: rgb(216, 203, 184);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 11.52px;
}
```

### Modals (3 instances)

```css
.modal {
  background-color: rgba(0, 0, 0, 0.55);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (87 instances)

```css
.dropdown {
  background-color: rgb(216, 203, 184);
  border-radius: 0px;
  border-color: rgb(44, 44, 44);
  padding-top: 0px;
}
```

### Switches (7 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(216, 203, 184);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(44, 44, 44);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(44, 44, 44);
  font-size: 12.8px;
  font-weight: 500;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(44, 44, 44);
  padding: 4px 4px 4px 4px;
  border-radius: 3px;
  border: 1px solid rgb(216, 203, 184);
  font-size: 11.52px;
  font-weight: 500;
```

### Button — 5 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(216, 203, 184);
  color: rgb(44, 44, 44);
  padding: 16px 42px 16px 42px;
  border-radius: 3px;
  border: 0px none rgb(44, 44, 44);
  font-size: 11.52px;
  font-weight: 500;
```

**Variant 2** (4 instances)

```css
  background: rgb(44, 44, 44);
  color: rgb(216, 203, 184);
  padding: 16px 42px 16px 42px;
  border-radius: 3px;
  border: 0px none rgb(216, 203, 184);
  font-size: 11.52px;
  font-weight: 500;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(216, 203, 184);
  color: rgb(44, 44, 44);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(44, 44, 44);
  font-size: 12.8px;
  font-weight: 500;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(44, 44, 44);
  padding: 52px 28px 32px 28px;
  border-radius: 0px;
  border: 0px none rgb(44, 44, 44);
  font-size: 12.8px;
  font-weight: 500;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(44, 44, 44);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(44, 44, 44);
  font-size: 12.8px;
  font-weight: 500;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(44, 44, 44);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(44, 44, 44);
  font-size: 12.8px;
  font-weight: 500;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(212, 150, 83, 0);
  color: rgb(44, 44, 44);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(44, 44, 44);
  font-size: 12.8px;
  font-weight: 500;
```

## Layout System

**5 grid containers** and **151 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 4x |
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 476.797px 238.391px 476.797px;
gap: 16px;
grid-template-columns: 232px 232px 232px 232px 232px;
gap: 16px;
grid-template-columns: 346.141px 507.703px 346.156px;
gap: 12px;
grid-template-columns: 128.172px 448.641px 102.547px;
gap: 12px;
grid-template-columns: 397.328px 397.328px 397.344px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 68x |
| column/nowrap | 83x |

**Gap values:** `12px`, `16px`, `1px`, `1px normal`, `20px`, `3px`, `4px`, `6px`, `6px normal`, `8px`

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
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 44 !important rules — prefer specificity over overrides
- 87% of CSS is unused — consider purging
- 4388 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |

```css
background: linear-gradient(rgb(16, 16, 16), rgba(16, 16, 16, 0.2));
```

## Z-Index Map

**10 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 900,900 | div.w.-.d.r.o.p.d.o.w.n, div.w.-.d.r.o.p.d.o.w.n, div.d.r.o.p.d.o.w.n._.m.o.b.i.l.e. .w.-.d.r.o.p.d.o.w.n |
| sticky | 10,99 | div.w.r.a.p.p.e.r._.h.e.r.o. .s.p.e.c.i.a.l._.m.a.i.n, section.f.u.l.l.s.i.z.e._.s.e.c.t.i.o.n, section.t.e.s.t.i.m.o.n.i.a.l.s |
| base | 0,9 | div.s.p.l.i.d.e._._.t.r.a.c.k, video.v.i.d.e.o, div.b.a.c.k.g.r.o.u.n.d._.h.e.r.o |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| Satoshi | self-hosted | 400, 500, 700 | normal |
| TT Ramillas Variable | self-hosted | 200 900 | normal |
| Bad Script | google-fonts | 300, 400, 500, 600, 700 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 57 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 3 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (62x), 4:3 (2x), 3:2 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `350ms` | 350 |
| `lg` | `450ms` | 450 |

### Easing Families

- **ease-out** (5 uses) — `cubic-bezier(0.25, 0.46, 0.45, 0.94)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `marquee` | slide-x | transform | 1 |

## Component Anatomy

### button — 14 instances

**Slots:** label

### card — 5 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **about** (3)
- **view** (3)
- **reserve** (3)
- **open** (3)
- **order** (2)

### Button Copy Patterns

- "about us" (3×)
- "view full menu" (3×)
- "reserve a table" (3×)
- "open menu" (3×)
- "order now" (2×)

### Sample Headings

> FLAVORS

> THAT STAY

> THE SPIRIT OF
INDIAN DINING
> SIGNATURE
PLATES
> SIGNATURE DISHES.
CLASSIC ROOTS.
> CATERING
> THE AMRIT WAY
> DRINKS THAT
COMPLETE
THE EXPERIENCE
> GIFT A TASTE
OF TRADITION
> ROOTED IN
EXPERIENCE

## Page Intent

**Type:** `landing` (confidence 0.59)
**Description:** Discover Amrit Palace — a fast-fine Indian restaurant blending authentic flavors with a modern dining experience. Explore our menu, catering, and gift options.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → nav → nav → hero → hero → pricing-table → testimonial → nav → hero → hero → content → testimonial → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | hero | FLAVORS
 | 0.85 |
| 5 | hero | THE SPIRIT OF
INDIAN DINING | 0.4 |
| 6 | pricing-table | SIGNATURE
PLATES | 0.9 |
| 7 | testimonial | CATERING | 0.8 |
| 8 | nav | — | 0.4 |
| 9 | hero | DRINKS THAT
COMPLETE
THE EXPERIENCE | 0.4 |
| 10 | hero | GIFT A TASTE
OF TRADITION | 0.4 |
| 11 | content | ROOTED IN
EXPERIENCE | 0.3 |
| 12 | testimonial | WHAT OUR
GUESTS SAY | 0.8 |
| 13 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.119 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 2px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `photography` (confidence 0.062)
**Counts:** total 65, svg 0, icon 111, screenshot-like 0, photo-like 8
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Satoshi` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
