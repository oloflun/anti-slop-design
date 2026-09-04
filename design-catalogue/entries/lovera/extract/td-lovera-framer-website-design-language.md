# Design Language: T.D-Lovera

> Extracted from `https://td-lovera.framer.website` on September 4, 2026
> 2096 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ff531f` | rgb(255, 83, 31) | hsl(14, 100%, 56%) | 53 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 476 |
| Accent | `#ff825c` | rgb(255, 130, 92) | hsl(14, 100%, 68%) | 213 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 2397 |
| `#171717` | hsl(0, 0%, 9%) | 772 |
| `#ffffff` | hsl(0, 0%, 100%) | 296 |
| `#767f7a` | hsl(147, 4%, 48%) | 53 |
| `#dddfde` | hsl(150, 3%, 87%) | 30 |
| `#f5f5f5` | hsl(0, 0%, 96%) | 19 |
| `#afb6b4` | hsl(163, 5%, 70%) | 11 |
| `#434645` | hsl(160, 2%, 27%) | 9 |
| `#fff0eb` | hsl(15, 100%, 96%) | 2 |

### Background Colors

Used on large-area elements: `#1e1f1f`, `#f5f5f5`, `#ffffff`, `#171717`, `#fff0eb`, `#ffc8b8`, `#ff9d80`, `#ff825c`, `#000000`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#ffffff`, `#434645`, `#ff531f`, `#171717`, `#ff825c`, `#767f7a`, `#afb6b4`, `#f9fbfb`

### Gradients

```css
background-image: linear-gradient(60deg, rgb(30, 31, 31) 31%, rgb(67, 70, 69) 100%);
```

```css
background-image: radial-gradient(17.86% 56% at 37.8% 29.2%, rgb(255, 240, 235) 0%, rgba(255, 255, 250, 0) 100%);
```

```css
background-image: linear-gradient(rgba(47, 49, 48, 0) 0%, rgba(23, 23, 23, 0.2) 146%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 2397 |
| `#171717` | background, text, border | 772 |
| `#0000ee` | text, border | 476 |
| `#ffffff` | text, border, background | 296 |
| `#ff825c` | text, border, background | 213 |
| `#767f7a` | background, text, border | 53 |
| `#ff531f` | background, text, border | 53 |
| `#dddfde` | background | 30 |
| `#f5f5f5` | background | 19 |
| `#afb6b4` | background, text, border | 11 |
| `#434645` | text, border, background | 9 |
| `#ffc8b8` | background | 3 |
| `#ff9d80` | background | 3 |
| `#fff0eb` | background | 2 |

## Typography

### Font Families

- **Apfel Grotezk** — used for all (430 elements)
- **Oswald** — used for all (39 elements)
- **Times New Roman** — used for body (29 elements)
- **Antonio** — used for body (6 elements)
- **Instrument Sans** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 320px | 20rem | 400 | 320px | -19.2px | h1, p |
| 190px | 11.875rem | 500 | 148.2px | -5.7px | p, span |
| 152px | 9.5rem | 400 | 228px | -4.56px | p |
| 120px | 7.5rem | 500 | 102px | -2.4px | h2, br, span |
| 104.117px | 6.5073rem | 400 | 99.9525px | -4.16469px | span, br |
| 100px | 6.25rem | 500 | 95px | -1px | h2 |
| 98px | 6.125rem | 400 | 88.2px | -2.94px | p |
| 64.855px | 4.0534rem | 400 | 62.2608px | -2.5942px | h2 |
| 48px | 3rem | 500 | 43.2px | -1.44px | p, h3 |
| 36px | 2.25rem | 500 | 36px | -0.36px | h2, span, h3, a |
| 24px | 1.5rem | 400 | 24px | -0.24px | p, h3 |
| 21px | 1.3125rem | 500 | 25.2px | -0.21px | p, a |
| 20px | 1.25rem | 700 | 30px | normal | p |
| 18px | 1.125rem | 500 | 19.8px | normal | p, h2, a |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |

### Heading Scale

```css
h1 { font-size: 320px; font-weight: 400; line-height: 320px; }
h2 { font-size: 120px; font-weight: 500; line-height: 102px; }
h2 { font-size: 100px; font-weight: 500; line-height: 95px; }
h2 { font-size: 64.855px; font-weight: 400; line-height: 62.2608px; }
h3 { font-size: 48px; font-weight: 500; line-height: 43.2px; }
h2 { font-size: 36px; font-weight: 500; line-height: 36px; }
h3 { font-size: 24px; font-weight: 400; line-height: 24px; }
h2 { font-size: 18px; font-weight: 500; line-height: 19.8px; }
```

### Body Text

```css
body { font-size: 36px; font-weight: 500; line-height: 36px; }
```

### Font Weights in Use

`400` (1731x), `500` (359x), `700` (6x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-120 | 120px | 7.5rem |
| spacing-140 | 140px | 8.75rem |
| spacing-150 | 150px | 9.375rem |
| spacing-200 | 200px | 12.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 6px | 1 |
| md | 10px | 1 |
| lg | 16px | 1 |
| xl | 24px | 43 |
| full | 28px | 9 |
| full | 32px | 18 |
| full | 38px | 1 |
| full | 50px | 4 |
| full | 60px | 1 |
| full | 68px | 3 |
| full | 76px | 3 |
| full | 100px | 4 |

## Box Shadows

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(0, 0, 0) 0px 0px 0px 1px inset;
```

**xs** — blur: 1.56569px
```css
box-shadow: rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px;
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
| md | 809px | max-width |
| md | 810px | min-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | max-width |
| 1439px | 1439px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.2s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: color 0.2s cubic-bezier(0.81, 0.12, 0.25, 0.87);
transition: background 0.3s cubic-bezier(0.44, 0, 0.56, 1), box-shadow 0.3s cubic-bezier(0.44, 0, 0.56, 1);
```

### Keyframe Animations

**__framer-loading-spin**
```css
@keyframes __framer-loading-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (2 instances)

```css
.button {
  background-color: rgb(23, 23, 23);
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 8px;
  padding-right: 16px;
  border-radius: 38px;
}
```

### Cards (1 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (26 instances)

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

### Links (49 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 12px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(245, 245, 245);
  color: rgb(0, 0, 0);
  padding-top: 140px;
  padding-bottom: 0px;
  font-size: 12px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Input — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(23, 23, 23);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(23, 23, 23);
  font-size: 16px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(23, 23, 23);
  padding: 10px 0px 10px 0px;
  border-radius: 0px;
  border: 0px none rgb(23, 23, 23);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(23, 23, 23);
  color: rgb(0, 0, 0);
  padding: 8px 16px 8px 16px;
  border-radius: 38px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**3 grid containers** and **677 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1580px | 0px |
| 480px | 0px |
| 100% | 0px |
| 552px | 0px |
| 700px | 32px |
| 600px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 6-column | 1x |
| 2-column | 1x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 594px 594px;
gap: 40px 12px;
grid-template-columns: 320px 320px 320px 320px;
grid-template-columns: 183.328px 183.328px 183.328px 183.328px 183.328px 183.328px;
gap: 20px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 485x |
| row/nowrap | 182x |
| row/wrap | 10x |

**Gap values:** `100px`, `10px`, `12px`, `150px`, `16px`, `1px`, `20px`, `22px`, `24px`, `26px`, `28px`, `2px`, `32px`, `36px`, `40px`, `40px 12px`, `4px`, `4px 12px`, `52px`, `56px`, `60px`, `64px`, `6px`, `80px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 80/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 65/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance

**Issues:**
- 5 font families — consider limiting to 2 (heading + body)
- 17 !important rules — prefer specificity over overrides
- 59% of CSS is unused — consider purging
- 5238 duplicate CSS declarations

## Gradients

**3 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 60deg | 2 | brand |
| radial | — | 3 | bold |
| linear | — | 2 | brand |

```css
background: linear-gradient(60deg, rgb(30, 31, 31) 31%, rgb(67, 70, 69) 100%);
background: radial-gradient(17.86% 56% at 37.8% 29.2%, rgb(255, 240, 235) 0%, rgba(255, 255, 250, 0) 100%);
background: linear-gradient(rgba(47, 49, 48, 0) 0%, rgba(23, 23, 23, 0.2) 146%);
```

## Z-Index Map

**8 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.1.e.u.z.f.1.8.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.1.s.v.d.7.j.h. .h.i.d.d.e.n.-.h.k.h.1.0.i, div.f.r.a.m.e.r.-.1.n.u.7.t.z.p.-.c.o.n.t.a.i.n.e.r |
| base | -1,5 | div.f.r.a.m.e.r.-.1.3.u.8.f.x.7, div.f.r.a.m.e.r.-.5.k.q.g.j.o, div.f.r.a.m.e.r.-.5.k.q.g.j.o |

**Issues:**
- [object Object]

## SVG Icons

**17 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 1 |
| md | 9 |
| xl | 6 |

**Icon colors:** `rgb(0, 0, 0)`, `rgb(255, 130, 92)`, `rgb(23, 23, 23)`, `rgb(255, 83, 31)`, `rgb(255, 255, 255)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Antonio | cdn | 700 | normal |
| Instrument Sans | cdn | 500, 600 | normal |
| Inter | self-hosted | 400, 600, 700, 900 | normal, italic |
| Oswald | self-hosted | 400, 500, 700 | normal |
| JetBrains Mono | self-hosted | 400 | normal |
| Apfel Grotezk | self-hosted | 400, 500, 700 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 20 | objectFit: cover, borderRadius: 30px, shape: pill |
| thumbnail | 11 | objectFit: cover, borderRadius: 8px, shape: rounded |
| hero | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| avatar | 2 | objectFit: cover, borderRadius: 50%, shape: circular |

**Aspect ratios:** 1:1 (12x), 3:4 (9x), 2:3 (7x), 2.59:1 (6x), 9:16 (1x), 3:2 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

### Easing Families

- **custom** (20 uses) — `cubic-bezier(0.81, 0.12, 0.25, 0.87)`, `cubic-bezier(0.44, 0, 0.56, 1)`

## Component Anatomy

### input — 4 instances


### button — 2 instances

**Slots:** label

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **send** (1)

### Button Copy Patterns

- "send" (1×)

### Sample Headings

> LOVERA
> Creative studio
for founders
> We help brands grow with strategic design that’s thoughtful, visually bold, and built to make an impression.
> Thoughtful design that moves the needle
> $4M raised: the strategy behind Tera’s growth
> A streamlined process, executed with methodical care.
> Latest
projects
> Super pro
> Formula vintage
> Fringe sports

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** Lovera is a bold, all-in-one Framer template for creative agencies—ideal for branding, copywriting, web design, and more. Packed with features and flexible sections, it’s built to drive results, boost

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → testimonial → testimonial → content → testimonial → testimonial → testimonial → faq → testimonial → testimonial → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | testimonial | LOVERA | 0.8 |
| 2 | testimonial | We help brands grow with strategic design that’s thoughtful, visually bold, and  | 0.8 |
| 3 | content | Latest
projects | 0.3 |
| 4 | testimonial | Services | 0.8 |
| 5 | testimonial | Flexible
plans | 0.8 |
| 6 | testimonial | Clients | 0.8 |
| 7 | faq | FAQ | 0.85 |
| 8 | testimonial | Process | 0.8 |
| 9 | testimonial | Stats
& facts | 0.8 |
| 10 | content | Latest
news | 0.3 |
| 11 | content | Let's talk shop | 0.3 |
| 12 | footer | Subscribe | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.252 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 3 |

## Imagery Style

**Label:** `photography` (confidence 0.028)
**Counts:** total 36, svg 0, icon 0, screenshot-like 0, photo-like 1
**Dominant aspect:** portrait
**Radius profile on images:** soft

## Component Library

**Detected:** `vuetify` (confidence 0.54)

Evidence:
- 12 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Apfel Grotezk` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
