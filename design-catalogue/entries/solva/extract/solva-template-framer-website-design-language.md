# Design Language: Solva — AI & SaaS Template for Framer

> Extracted from `https://solva-template.framer.website/` on September 4, 2026
> 1917 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#1c1a15` | rgb(28, 26, 21) | hsl(43, 14%, 10%) | 402 |
| Secondary | `#fbfaf6` | rgb(251, 250, 246) | hsl(48, 38%, 97%) | 109 |
| Accent | `#0055ff` | rgb(0, 85, 255) | hsl(220, 100%, 50%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 2954 |
| `#56524a` | hsl(40, 8%, 31%) | 272 |
| `#ece9e0` | hsl(45, 24%, 90%) | 1 |
| `#8c887e` | hsl(43, 6%, 52%) | 1 |

### Background Colors

Used on large-area elements: `#fbfaf6`, `#f4f2ec`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#1c1a15`, `#56524a`, `#fbfaf6`, `#ffffff`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 2954 |
| `#1c1a15` | background, text, border | 402 |
| `#56524a` | text, border, background | 272 |
| `#0000ee` | text, border | 188 |
| `#fbfaf6` | background, text, border | 109 |
| `#ece9e0` | background | 1 |
| `#8c887e` | background | 1 |
| `#0055ff` | background | 1 |

## Typography

### Font Families

- **Onest** — used for all (180 elements)
- **Sentient** — used for all (87 elements)
- **Inter** — used for all (82 elements)
- **Times New Roman** — used for body (31 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 56px | 3.5rem | 300 | 58.8px | -2.8px | h1, span |
| 48px | 3rem | 300 | 50.4px | -2.4px | h2, span, br, code |
| 40px | 2.5rem | 300 | 46px | -2px | h3, p |
| 30px | 1.875rem | 300 | 37.5px | -1.5px | h4, span |
| 28px | 1.75rem | 500 | 36.4px | -0.56px | p |
| 20px | 1.25rem | 500 | 26px | -0.4px | p, h3 |
| 18px | 1.125rem | 400 | 25.2px | normal | h6, p, h3 |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 15px | 0.9375rem | 400 | 19.5px | normal | p |
| 14px | 0.875rem | 500 | 21px | normal | p, h4 |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |

### Heading Scale

```css
h1 { font-size: 56px; font-weight: 300; line-height: 58.8px; }
h2 { font-size: 48px; font-weight: 300; line-height: 50.4px; }
h3 { font-size: 40px; font-weight: 300; line-height: 46px; }
h4 { font-size: 30px; font-weight: 300; line-height: 37.5px; }
h3 { font-size: 20px; font-weight: 500; line-height: 26px; }
h6 { font-size: 18px; font-weight: 400; line-height: 25.2px; }
h4 { font-size: 14px; font-weight: 500; line-height: 21px; }
```

### Body Text

```css
body { font-size: 18px; font-weight: 400; line-height: 25.2px; }
```

### Font Weights in Use

`400` (1720x), `500` (110x), `300` (87x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-16 | 16px | 1rem |
| spacing-20 | 20px | 1.25rem |
| spacing-28 | 28px | 1.75rem |
| spacing-32 | 32px | 2rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-60 | 60px | 3.75rem |
| spacing-64 | 64px | 4rem |
| spacing-72 | 72px | 4.5rem |
| spacing-96 | 96px | 6rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 2 |
| md | 6px | 14 |
| md | 10px | 28 |
| lg | 16px | 37 |
| full | 50px | 8 |

## Box Shadows

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(0, 0, 0) 0px 0px 0px 1px inset;
```

**xs** — blur: 1.56569px
```css
box-shadow: rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px;
```

**sm** — blur: 3px
```css
box-shadow: rgba(0, 0, 0, 0.03) 0px 1px 3px 0px, rgba(0, 0, 0, 0.04) 0px 4px 16px 0px, rgba(255, 255, 255, 0.5) 0px 0px 0px 8px;
```

**sm** — blur: 3px
```css
box-shadow: rgba(0, 85, 255, 0.1) 0px 1px 3px 0px, rgba(0, 85, 255, 0.14) 0px 4px 16px 0px;
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

### Common Transitions

```css
transition: all;
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
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
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

### Links (39 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 12px;
  font-weight: 400;
}
```

### Navigation (5 instances)

```css
.navigatio {
  background-color: rgb(251, 250, 246);
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
  background-color: rgb(244, 242, 236);
  color: rgb(0, 0, 0);
  padding-top: 96px;
  padding-bottom: 32px;
  font-size: 12px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**0 grid containers** and **668 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1200px | 0px |
| 100% | 24px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 432x |
| row/nowrap | 236x |

**Gap values:** `10px`, `12px`, `16px`, `20px`, `24px`, `32px`, `40px`, `48px`, `4px`, `5px`, `60px`, `64px`, `6px`, `72px`, `8px`, `8px 24px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

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
- 4 font families — consider limiting to 2 (heading + body)
- 17 !important rules — prefer specificity over overrides
- 52% of CSS is unused — consider purging
- 4107 duplicate CSS declarations

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.1.k.r.e.1.i.k.-.c.o.n.t.a.i.n.e.r |
| base | -1,9 | div.f.r.a.m.e.r.-.8.8.u.o.5.1, div.f.r.a.m.e.r.-.1.g.4.g.n.5.1, div.f.r.a.m.e.r.-.1.c.k.k.z.q |

**Issues:**
- [object Object]

## SVG Icons

**28 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 3 |
| sm | 14 |
| md | 7 |
| lg | 4 |

**Icon colors:** `rgb(0, 0, 0)`, `rgb(251, 250, 246)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Onest | cdn | 400, 500, 700 | normal |
| Inter | self-hosted | 400, 500, 700 | normal, italic |
| Sentient | self-hosted | 300, 400 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 14 | objectFit: cover, borderRadius: 10px, shape: rounded |
| general | 11 | objectFit: cover, borderRadius: 16px, shape: rounded |
| thumbnail | 10 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:2 (11x), 1:1 (10x), 4:3 (4x), 3.16:1 (3x), 3:4 (1x), 5.12:1 (1x), 3.29:1 (1x), 3:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **company** (1)

### Button Copy Patterns

- "company" (1×)

### Sample Headings

> The support copilot that never sleeps.
> Three ways Solva 
runs your support.
> Resolve in seconds
> Learn from your docs
> Know when to escalate
> The support copilot that never sleeps.
> Three ways Solva 
runs your support.
> Resolve in seconds
> Learn from your docs
> Know when to escalate

## Page Intent

**Type:** `landing` (confidence 0.51)
**Description:** Solva is a light, elegant Framer template built for AI and SaaS products. Responsive, CMS-powered, and ready to launch fast.

Alternates: pricing (0.6), legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → testimonial → testimonial → content → testimonial → testimonial → pricing → testimonials → pricing-table → content → testimonial → testimonial → faq → testimonial → footer → nav → nav → nav → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | testimonial | The support copilot that never sleeps. | 0.8 |
| 2 | testimonial | The support copilot that never sleeps. | 0.8 |
| 3 | content | — | 0.3 |
| 4 | testimonial | Three ways Solva 
runs your support. | 0.8 |
| 5 | testimonial | One inbox. 
Every question, handled. | 0.8 |
| 6 | pricing | One platform. 
Every team it touches. | 0.4 |
| 7 | testimonials | Enterprise-grade security, built in by default. | 0.4 |
| 8 | pricing-table | Simple pricing. 
No surprises. | 0.9 |
| 9 | content | — | 0.3 |
| 10 | testimonial | Big results,
from day one. | 0.8 |
| 11 | testimonial | Less busywork, 
more breathing room. | 0.8 |
| 12 | faq | You have questions. 
We have answers. | 0.85 |
| 13 | testimonial | Give your team
their mornings back. | 0.8 |
| 14 | footer | — | 0.95 |
| 15 | nav | — | 0.9 |
| 16 | nav | — | 0.9 |
| 17 | nav | — | 0.9 |
| 18 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.32 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 36, svg 0, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `vuetify` (confidence 0.54)

Evidence:
- 12 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Onest` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
