# Design Language: INDOEK – Indoek Shop

> Extracted from `https://indoek.com` on September 4, 2026
> 1162 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#135eab` | rgb(19, 94, 171) | hsl(210, 80%, 37%) | 857 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 1301 |
| `#000000` | hsl(0, 0%, 0%) | 178 |
| `#ffffff` | hsl(0, 0%, 100%) | 1 |

### Background Colors

Used on large-area elements: `#efebe3`, `#135eab`

### Text Colors

Text color palette: `#000000`, `#135eab`, `#ffffff`, `#efebe3`

### Gradients

```css
background-image: linear-gradient(rgb(255, 255, 255), rgb(255, 255, 255));
```

```css
background-image: linear-gradient(rgb(19, 94, 171), rgb(19, 94, 171));
```

```css
background-image: linear-gradient(rgb(239, 235, 227), rgb(239, 235, 227));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | background, text, border | 1301 |
| `#135eab` | text, border, background | 857 |
| `#000000` | text, background | 178 |
| `#ffffff` | text | 1 |

## Typography

### Font Families

- **Calibre** — used for all (1160 elements)
- **GTStandard-M** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 64px | 4rem | 400 | 64px | normal | ul, li, a, div |
| 40px | 2.5rem | 400 | 40px | normal | div, p, span, br |
| 34px | 2.125rem | 400 | 34px | normal | a, svg, path, button |
| 28px | 1.75rem | 400 | 33.6px | normal | ul, li, a, span |
| 24px | 1.5rem | 400 | 28.8px | normal | div, a, span, p |
| 20px | 1.25rem | 700 | 28px | normal | a |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, link |

### Heading Scale

```css
h1 { font-size: 16px; font-weight: 400; line-height: 24px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: 24px; }
```

### Font Weights in Use

`400` (1161x), `700` (1x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-80 | 80px | 5rem |
| spacing-101 | 101px | 6.3125rem |
| spacing-130 | 130px | 8.125rem |
| spacing-144 | 144px | 9rem |
| spacing-163 | 163px | 10.1875rem |
| spacing-185 | 185px | 11.5625rem |
| spacing-208 | 208px | 13rem |
| spacing-273 | 273px | 17.0625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 8px | 1 |
| full | 9999px | 6 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 1000px inset;
```

## CSS Custom Properties

### Colors

```css
--theme-foreground: #135EAB;
--swiper-theme-color: #007aff;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-ring-offset-width: 0px;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgb(59 130 246 / .5);
--tw-ring-offset-color: #fff;
```

### Spacing

```css
--site-divider-size: 3px;
--tw-contain-size: ;
--tw-numeric-spacing: ;
```

### Shadows

```css
--tw-shadow: 0 0 #0000;
--tw-drop-shadow: ;
```

### Other

```css
--test-css-var: '10px';
--header-height: 110px;
--theme-background: #EFEBE3;
--tw-contrast: ;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-backdrop-blur: ;
--tw-contain-style: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-backdrop-invert: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-brightness: ;
--tw-numeric-fraction: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-skew-y: 0;
--tw-backdrop-brightness: ;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-rotate: 0;
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
| sm | 576px | max-width |
| sm | 640px | min-width |
| md | 768px | min-width |
| lg | 1024px | min-width |
| xl | 1280px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.15s`

### Common Transitions

```css
transition: all;
transition: background-size 0.3s;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: max-height 0.3s ease-in-out;
transition: background-size 0.3s 0.3s;
transition: transform;
transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

### Keyframe Animations

**shopify-rotator**
```css
@keyframes shopify-rotator {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(270deg); }
}
```

**shopify-dash**
```css
@keyframes shopify-dash {
  0% { stroke-dashoffset: 280px; }
  50% { stroke-dashoffset: 75px; transform: rotate(135deg); }
  100% { stroke-dashoffset: 280px; transform: rotate(450deg); }
}
```

**acceleratedCheckoutLoadingSkeleton**
```css
@keyframes acceleratedCheckoutLoadingSkeleton {
  50% { opacity: var(--shopify-accelerated-checkout-skeleton-animation-opacity-start,1); }
  75% { opacity: var(--shopify-accelerated-checkout-skeleton-animation-opacity-end,.5); }
  100% { opacity: var(--shopify-accelerated-checkout-skeleton-animation-opacity-start,1); }
}
```

**spin**
```css
@keyframes spin {
  100% { transform: rotate(360deg); }
}
```

**swiper-preloader-spin**
```css
@keyframes swiper-preloader-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (26 instances)

```css
.button {
  background-color: rgb(19, 94, 171);
  color: rgb(19, 94, 171);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Inputs (6 instances)

```css
.input {
  color: rgb(239, 235, 227);
  border-color: rgb(229, 231, 235);
  border-radius: 0px;
  font-size: 24px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (109 instances)

```css
.link {
  color: rgb(19, 94, 171);
  font-size: 34px;
  font-weight: 400;
}
```

### Navigation (24 instances)

```css
.navigatio {
  background-color: rgb(19, 94, 171);
  color: rgb(19, 94, 171);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(19, 94, 171);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (2 instances)

```css
.modal {
  background-color: rgb(239, 235, 227);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 386px;
}
```

### Dropdowns (5 instances)

```css
.dropdown {
  background-color: rgb(19, 94, 171);
  border-radius: 0px;
  border-color: rgb(229, 231, 235);
  padding-top: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(19, 94, 171);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(19, 94, 171);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(19, 94, 171);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 64px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(19, 94, 171);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235) rgb(229, 231, 235) rgb(19, 94, 171);
  font-size: 64px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(19, 94, 171);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 235, 227);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px 0px 3px solid rgb(229, 231, 235) rgb(229, 231, 235) rgb(239, 235, 227);
  font-size: 24px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 235, 227);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 24px;
  font-weight: 400;
```

## Layout System

**49 grid containers** and **85 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 17x |
| 1-column | 15x |
| 3-column | 11x |
| 8-column | 4x |
| 2-column | 2x |

### Grid Templates

```css
grid-template-columns: 102.656px 102.656px 102.656px 102.656px 102.656px 102.656px 102.656px 102.656px 102.656px 102.656px 102.656px 102.656px;
grid-template-columns: 1280px;
grid-template-columns: 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px;
grid-template-columns: 1280px;
grid-template-columns: 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 50x |
| column/nowrap | 23x |
| row/wrap | 12x |

**Gap values:** `16px`, `16px normal`, `24px 80px`, `48px`, `4px`, `8px`, `normal 16px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#000000` | 21:1 | AAA |

## Design System Score

**Overall: 90/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 100/100 |
| Spacing System | 70/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 17 !important rules — prefer specificity over overrides
- 79% of CSS is unused — consider purging
- 737 duplicate CSS declarations

## Gradients

**3 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |

```css
background: linear-gradient(rgb(255, 255, 255), rgb(255, 255, 255));
background: linear-gradient(rgb(19, 94, 171), rgb(19, 94, 171));
background: linear-gradient(rgb(239, 235, 227), rgb(239, 235, 227));
```

## Z-Index Map

**12 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,100 | div.m.i.n.i.c.a.r.t.-.w.r.a.p.p.e.r. .b.g.-.b.a.c.k.g.r.o.u.n.d. .b.o.r.d.e.r.-.l.-.s.i.t.e. .b.o.r.d.e.r.-.l.-.f.o.r.e.g.r.o.u.n.d. .h.-.[.1.0.0.d.v.h.]. .w.-.f.u.l.l. .m.a.x.-.w.-.[.7.5.%.]. .m.d.:.m.a.x.-.w.-.[.3.8.6.p.x.], div.m.o.b.i.l.e.-.m.e.n.u.-.w.r.a.p.p.e.r. .b.g.-.f.o.r.e.g.r.o.u.n.d. .t.e.x.t.-.b.a.c.k.g.r.o.u.n.d. .h.-.[.1.0.0.d.v.h.]. .w.-.f.u.l.l. .m.a.x.-.w.-.[.1.0.0.%.]. .m.d.:.h.i.d.d.e.n |
| sticky | 10,50 | a.c.u.r.s.o.r.-.p.o.i.n.t.e.r. .s.c.r.e.e.n.-.l.i.n.k. .z.-.[.1.0.], a.c.u.r.s.o.r.-.p.o.i.n.t.e.r. .s.c.r.e.e.n.-.l.i.n.k. .z.-.[.1.0.], a.c.u.r.s.o.r.-.p.o.i.n.t.e.r. .s.c.r.e.e.n.-.l.i.n.k. .z.-.[.1.0.] |
| base | -100,9 | div, div.r.e.l.a.t.i.v.e. .w.-.f.u.l.l. .h.-.f.u.l.l. .s.w.i.p.e.r. .c.a.r.o.u.s.e.l.-.s.w.i.p.e.r. .s.w.i.p.e.r.-.i.n.i.t.i.a.l.i.z.e.d. .s.w.i.p.e.r.-.h.o.r.i.z.o.n.t.a.l. .s.w.i.p.e.r.-.b.a.c.k.f.a.c.e.-.h.i.d.d.e.n, div.w.-.f.u.l.l. .h.-.f.u.l.l. .s.w.i.p.e.r.-.w.r.a.p.p.e.r |

## SVG Icons

**4 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| md | 2 |
| xl | 2 |

**Icon colors:** `currentColor`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Calibre | self-hosted | 400, 600 | normal, italic |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 14 | objectFit: contain, borderRadius: 0px, shape: square |
| hero | 9 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 4 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (16x), 16:9 (6x), 1:1 (5x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `md` | `300ms` | 300 |

### Easing Families

- **custom** (6 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-in-out** (2 uses) — `ease`

## Component Anatomy

### button — 11 instances

**Slots:** label, icon
**Sizes:** md · xl

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **current** (2)
- **view** (1)
- **past** (1)
- **events** (1)
- **submit** (1)

### Button Copy Patterns

- "view cart" (1×)
- "current exhibit
past exhibits
events" (1×)
- "current exhibit" (1×)
- "past exhibits" (1×)
- "events" (1×)
- "submit" (1×)

### Sample Headings

> Indoek

## Page Intent

**Type:** `landing` (confidence 0.51)
**Description:** Celebrating Coastal Creative Culture

Alternates: pricing (0.6), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → pricing-table → content → hero → pricing-table → pricing-table → pricing-table → gallery → pricing-table → gallery → pricing-table → pricing-table → pricing-table → pricing-table → pricing-table → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | Indoek | 0.4 |
| 1 | pricing-table | — | 0.9 |
| 2 | content | — | 0.3 |
| 3 | hero | — | 0.85 |
| 4 | pricing-table | — | 0.9 |
| 5 | pricing-table | — | 0.9 |
| 6 | pricing-table | — | 0.9 |
| 7 | gallery | — | 0.7 |
| 8 | pricing-table | — | 0.9 |
| 9 | gallery | — | 0.7 |
| 10 | pricing-table | — | 0.9 |
| 11 | pricing-table | — | 0.9 |
| 12 | pricing-table | — | 0.9 |
| 13 | pricing-table | — | 0.9 |
| 14 | pricing-table | — | 0.9 |
| 15 | content | — | 0.3 |
| 16 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.229 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 3 |

## Imagery Style

**Label:** `photography` (confidence 0.537)
**Counts:** total 27, svg 0, icon 0, screenshot-like 0, photo-like 27
**Dominant aspect:** portrait
**Radius profile on images:** square

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: tailwindcss (0.3)

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Calibre` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
