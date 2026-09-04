# Design Language: Mattis® Studio — Conversion-First Design & Development Agency

> Extracted from `https://mattis.framer.website/` on September 4, 2026
> 1909 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ff4500` | rgb(255, 69, 0) | hsl(16, 100%, 50%) | 10 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 502 |
| Accent | `#d2ff37` | rgb(210, 255, 55) | hsl(74, 100%, 61%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 2217 |
| `#ffffff` | hsl(0, 0%, 100%) | 932 |
| `#0b0b0b` | hsl(0, 0%, 4%) | 262 |
| `#e9e9e9` | hsl(0, 0%, 91%) | 16 |
| `#767676` | hsl(0, 0%, 46%) | 11 |
| `#181818` | hsl(0, 0%, 9%) | 2 |
| `#222222` | hsl(0, 0%, 13%) | 1 |

### Background Colors

Used on large-area elements: `#0b0b0b`, `#ffffff`, `#0d0d0d`, `#000000`, `#ff4500`, `#e9e9e9`, `#181818`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#ffffff`, `#0b0b0b`, `#0e0e0e`

### Gradients

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.78) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 2217 |
| `#ffffff` | background, text, border | 932 |
| `#0000ee` | text, border | 502 |
| `#0b0b0b` | background, text, border | 262 |
| `#e9e9e9` | background | 16 |
| `#767676` | border | 11 |
| `#ff4500` | background | 10 |
| `#181818` | background | 2 |
| `#d2ff37` | background | 1 |
| `#222222` | background | 1 |

## Typography

### Font Families

- **Geist** — used for all (537 elements)
- **Times New Roman** — used for body (31 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 140.498px | 8.7811rem | 600 | 115.208px | -7.02489px | p |
| 100px | 6.25rem | 600 | 82px | -4px | p |
| 92px | 5.75rem | 600 | 75.44px | -4.6px | h1, span, h2, div |
| 78px | 4.875rem | 600 | normal | -5.46px | div, span |
| 64px | 4rem | 500 | normal | -4.48px | div, span |
| 58px | 3.625rem | 600 | normal | -4.06px | div, span |
| 34px | 2.125rem | 600 | 30.6px | -2.04px | p |
| 32px | 2rem | 500 | 35.2px | -0.32px | p, div, span |
| 26px | 1.625rem | 500 | 28.6px | -0.26px | p, a |
| 20px | 1.25rem | 500 | 24px | -0.2px | p, a |
| 18px | 1.125rem | 600 | 14.76px | -0.36px | p |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 15px | 0.9375rem | 700 | 18px | -0.15px | p |
| 14px | 0.875rem | 500 | 18.2px | -0.14px | p, input, select, option |
| 13px | 0.8125rem | 500 | 15.6px | -0.13px | p, span, br |

### Heading Scale

```css
h1 { font-size: 92px; font-weight: 600; line-height: 75.44px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (1377x), `500` (440x), `600` (90x), `700` (2x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-30 | 30px | 1.875rem |
| spacing-36 | 36px | 2.25rem |
| spacing-40 | 40px | 2.5rem |
| spacing-50 | 50px | 3.125rem |
| spacing-60 | 60px | 3.75rem |
| spacing-70 | 70px | 4.375rem |
| spacing-80 | 80px | 5rem |
| spacing-90 | 90px | 5.625rem |
| spacing-100 | 100px | 6.25rem |
| spacing-110 | 110px | 6.875rem |
| spacing-120 | 120px | 7.5rem |
| spacing-130 | 130px | 8.125rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 7px | 4 |
| md | 10px | 5 |
| full | 50px | 16 |
| full | 100px | 11 |

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

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.001s`, `0.2s`

### Common Transitions

```css
transition: overflow 0.001s allow-discrete;
transition: all;
transition: color 0.2s cubic-bezier(0.44, 0, 0.56, 1);
transition: background, box-shadow;
transition: color 0.2s cubic-bezier(0.44, 0, 0.56, 1), text-decoration-color 0.2s cubic-bezier(0.44, 0, 0.56, 1), text-decoration-thickness 0.2s cubic-bezier(0.44, 0, 0.56, 1), text-underline-offset 0.2s cubic-bezier(0.44, 0, 0.56, 1);
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

### Buttons (1 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 20px;
  border-radius: 0px;
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

### Inputs (14 instances)

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

### Links (38 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 12px;
  font-weight: 400;
}
```

### Navigation (2 instances)

```css
.navigatio {
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
  background-color: rgb(233, 233, 233);
  color: rgb(0, 0, 0);
  padding-top: 110px;
  padding-bottom: 70px;
  font-size: 12px;
}
```

### Switches (1 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Input — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 0px 20px 0px 20px;
  border-radius: 0px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**25 grid containers** and **683 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1440px | 0px |
| 570px | 0px |
| 100% | 0px |
| 600px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 16x |
| 12-column | 3x |
| 8-column | 3x |
| 3-column | 2x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px;
gap: 0px 4px;
grid-template-columns: 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px;
gap: 0px 4px;
grid-template-columns: 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px 99.6562px;
gap: 0px 4px;
grid-template-columns: 610px 610px;
grid-template-columns: 610px 610px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 439x |
| row/nowrap | 244x |

**Gap values:** `0px 4px`, `10px`, `12px`, `13px`, `14px`, `15px`, `16px`, `18px`, `1px`, `20px`, `22px`, `24px`, `2px`, `30px`, `32px`, `36px`, `3px`, `40px`, `4px`, `50px`, `5px`, `60px`, `6px`, `70px`, `8px`, `9px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 91/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 82/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 16 !important rules — prefer specificity over overrides
- 52% of CSS is unused — consider purging
- 6014 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |

```css
background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.78) 100%);
```

## Z-Index Map

**9 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,2147483647 | div, div, div |
| base | 0,9 | div.f.r.a.m.e.r.-.3.k.x.c.8.6, div.f.r.a.m.e.r.-.1.u.i.i.z.u.3, div.f.r.a.m.e.r.-.1.o.g.j.g.g.t |

**Issues:**
- [object Object]

## SVG Icons

**20 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 7 |
| md | 2 |
| lg | 2 |
| xl | 9 |

**Icon colors:** `rgb(0, 0, 0)`, `rgb(11, 11, 11)`, `rgb(14, 14, 14)`, `white`, `#0B0B0B`, `#222`, `#171717`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Geist | cdn | 400, 500, 600, 700, 900 | normal |
| Geist Mono | cdn | 500 | normal |
| Inter | self-hosted | 400, 700 | normal, italic |
| Outfit | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| avatar | 5 | objectFit: cover, borderRadius: 50px, shape: circular |
| hero | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 4 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (11x), 3:2 (2x), 16:9 (2x), 3:4 (1x), 2:3 (1x), 4:3 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |
| `sm` | `200ms` | 200 |

### Easing Families

- **custom** (15 uses) — `cubic-bezier(0.44, 0, 0.56, 1)`

## Component Anatomy

### input — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (tight)

### Top CTA Verbs

- **send** (1)

### Button Copy Patterns

- "send message

send message" (1×)

### Sample Headings

> STRATEGY
BEFORE
PIXELS.
> WE
BUILD
WEBSITES.
> BUILT ON
REPUTATION
> EVERY 
RESULT HERE 
STARTED WITH 
A PROBLEM 
WORTH 
SOLVING.
> BEFORE WE
GET STARTED.
> STRATEGY
BEFORE
PIXELS.
> WE
BUILD
WEBSITES.
> BUILT ON
REPUTATION
> EVERY 
RESULT HERE 
STARTED WITH 
A PROBLEM 
WORTH 
SOLVING.
> BEFORE WE
GET STARTED.

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** Strategy, design, and development built around how your customers make decisions. 60+ projects shipped with measurable conversion lift.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → pricing-table → testimonial → nav → content → content → content → testimonials → testimonial → testimonial → faq → testimonial → testimonial → testimonial → footer → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | pricing-table | STRATEGY
BEFORE
PIXELS. | 0.9 |
| 3 | testimonial | — | 0.8 |
| 4 | content | STRATEGY
BEFORE
PIXELS. | 0.3 |
| 5 | content | WE
BUILD
WEBSITES. | 0.3 |
| 6 | content | — | 0.3 |
| 7 | testimonials | BUILT ON
REPUTATION | 0.4 |
| 8 | testimonial | — | 0.8 |
| 9 | testimonial | EVERY 
RESULT HERE 
STARTED WITH 
A PROBLEM 
WORTH 
SOLVING. | 0.8 |
| 10 | faq | BEFORE WE
GET STARTED. | 0.85 |
| 11 | testimonial | PRICING. | 0.8 |
| 12 | testimonial | WHAT OUR 
CLIENTS SAY. | 0.8 |
| 13 | testimonial | NEWS AND
UPDATES. | 0.8 |
| 14 | footer | START A PROJECT. | 0.95 |
| 15 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.278 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `photography` (confidence 0.25)
**Counts:** total 18, svg 0, icon 4, screenshot-like 0, photo-like 9
**Dominant aspect:** square-ish
**Radius profile on images:** soft

## Component Library

**Detected:** `vuetify` (confidence 0.52)

Evidence:
- 11 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Geist` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
