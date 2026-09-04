# Design Language: Zanzibar - Agancy and Portfolio Premium Framer Template

> Extracted from `https://zanzibar.framer.website` on September 4, 2026
> 1484 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fffaf6` | rgb(255, 250, 246) | hsl(27, 100%, 98%) | 939 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 248 |
| Accent | `#f1efe5` | rgb(241, 239, 229) | hsl(50, 30%, 92%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 958 |
| `#100c08` | hsl(30, 33%, 5%) | 860 |
| `#767676` | hsl(0, 0%, 46%) | 11 |

### Background Colors

Used on large-area elements: `#100c08`, `#000000`, `#f1efe5`, `#fffaf6`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#fffaf6`, `#100c08`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 958 |
| `#fffaf6` | text, border, background | 939 |
| `#100c08` | background, text, border | 860 |
| `#0000ee` | text, border | 248 |
| `#767676` | border | 11 |
| `#f1efe5` | background | 1 |

## Typography

### Font Families

- **Inter** — used for body (816 elements)
- **Libre Caslon Condensed Variable** — used for all (63 elements)
- **Times New Roman** — used for body (29 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 144px | 9rem | 1000 | 158.4px | normal | h1, span, h2 |
| 36px | 2.25rem | 1000 | 43.2px | normal | h2, span |
| 18px | 1.125rem | 400 | 23.4px | -0.36px | p, span |
| 17px | 1.0625rem | 400 | 22.1px | -0.34px | p, span, a |
| 16px | 1rem | 400 | normal | normal | html, head, meta, script |
| 14.4px | 0.9rem | 1000 | 18px | normal | p |
| 14px | 0.875rem | 600 | 16.8px | -0.28px | p, input |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |

### Heading Scale

```css
h1 { font-size: 144px; font-weight: 1000; line-height: 158.4px; }
h2 { font-size: 36px; font-weight: 1000; line-height: 43.2px; }
```

### Body Text

```css
body { font-size: 17px; font-weight: 400; line-height: 22.1px; }
```

### Font Weights in Use

`400` (1410x), `1000` (63x), `500` (6x), `600` (5x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-32 | 32px | 2rem |
| spacing-48 | 48px | 3rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-112 | 112px | 7rem |
| spacing-180 | 180px | 11.25rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 1 |
| md | 7px | 2 |
| md | 10px | 2 |
| lg | 16px | 1 |
| full | 48px | 6 |
| full | 100px | 10 |

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
| 909px | 909px | max-width |
| 910px | 910px | min-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | max-width |
| 2xl | 1511px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.4s`

### Common Transitions

```css
transition: all;
transition: color 0.4s cubic-bezier(0.075, 0.82, 0.165, 1);
transition: background, box-shadow;
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
  padding-top: 12px;
  padding-right: 24px;
  border-radius: 48px;
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

### Inputs (12 instances)

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

### Links (26 instances)

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
  color: rgb(0, 0, 0);
  padding-top: 112px;
  padding-bottom: 0px;
  font-size: 12px;
}
```

### Badges (1 instances)

```css
.badge {
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 250, 246);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 250, 246);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 12px 24px 12px 24px;
  border-radius: 48px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**4 grid containers** and **321 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 480px | 0px |
| 1600px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 3x |
| 10-column | 1x |

### Grid Templates

```css
grid-template-columns: 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px;
grid-template-columns: 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.344px;
grid-template-columns: 107.188px 107.188px 107.203px 107.188px 107.188px 107.188px 107.203px 107.188px 107.188px 107.188px;
gap: 16px;
grid-template-columns: 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 210x |
| row/nowrap | 105x |
| column/wrap | 6x |

**Gap values:** `10px`, `112px`, `12px`, `16px`, `20px`, `24px`, `32px`, `48px`, `4px`, `64px`, `6px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 17 !important rules — prefer specificity over overrides
- 65% of CSS is unused — consider purging
- 3467 duplicate CSS declarations

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,13 | div.f.r.a.m.e.r.-.1.4.3.i.y.x.0.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.J.w.y.X.G. .f.r.a.m.e.r.-.N.e.R.K.y. .f.r.a.m.e.r.-.1.b.y.4.s.x.r. .f.r.a.m.e.r.-.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .f.r.a.m.e.r.-.v.-.1.b.y.4.s.x.r |
| base | -1,8 | div.f.r.a.m.e.r.-.1.3.t.k.7.a.p, div.f.r.a.m.e.r.-.1.q.0.p.9.b.g, div.f.r.a.m.e.r.-.1.3.t.k.7.a.p |

**Issues:**
- [object Object]

## SVG Icons

**5 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xl | 5 |

**Icon colors:** `var(--token-9ce74537-10cc-432a-8c9b-95fac166df5b, rgb(0, 74, 53))`, `white`, `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Mona Sans | cdn | 600 | normal |
| Instrument Serif | cdn | 400 | italic |
| Inter | self-hosted | 400, 500, 600, 700 | normal, italic |
| Libre Caslon Condensed Variable | self-hosted | 1000 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 7 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (3x), 3:2 (3x), 3:4 (3x), 4:3 (2x), 9:16 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `400ms` | 400 |

### Easing Families

- **ease-out** (1 uses) — `cubic-bezier(0.075, 0.82, 0.165, 1)`

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **subscribe** (1)

### Button Copy Patterns

- "subscribe

subscribe" (1×)

### Sample Headings

> Zanzibar
> What We Bring
> About us
> Projects
> Zanzibar
> What We Bring
> About us
> Projects
> Follow

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** The Zanzibar Framer template helps agencies and entrepreneurs showcase their work and convert visitors into clients, featuring pages for home, about, services, contact, and a portfolio collection.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → content → nav → content → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | content | Zanzibar | 0.3 |
| 2 | nav | Zanzibar | 0.4 |
| 3 | content | What We Bring | 0.3 |
| 4 | content | About us | 0.3 |
| 5 | content | Projects | 0.3 |
| 6 | footer | Follow | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.264 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.5)
**Counts:** total 12, svg 0, icon 1, screenshot-like 0, photo-like 10
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `vuetify` (confidence 0.4)

Evidence:
- 5 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
