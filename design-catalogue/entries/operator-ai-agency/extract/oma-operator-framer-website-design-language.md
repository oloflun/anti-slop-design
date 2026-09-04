# Design Language: Operator — AI Agent Agency | Custom AI Agents for Business

> Extracted from `https://oma-operator.framer.website/` on September 4, 2026
> 4112 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 582 |
| Secondary | `#0eea8e` | rgb(14, 234, 142) | hsl(155, 89%, 49%) | 43 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 7061 |
| `#74797d` | hsl(207, 4%, 47%) | 163 |
| `#fafafa` | hsl(0, 0%, 98%) | 162 |
| `#d4d6d8` | hsl(210, 5%, 84%) | 104 |
| `#f4f5f5` | hsl(180, 5%, 96%) | 103 |
| `#08090a` | hsl(210, 11%, 4%) | 63 |
| `#a1a5aa` | hsl(213, 5%, 65%) | 50 |
| `#181a1b` | hsl(200, 6%, 10%) | 17 |
| `#e4e6e7` | hsl(200, 6%, 90%) | 12 |
| `#52575b` | hsl(207, 5%, 34%) | 10 |
| `#666666` | hsl(0, 0%, 40%) | 2 |

### Background Colors

Used on large-area elements: `#08090a`, `#0d0f0f`, `#181a1b`

### Text Colors

Text color palette: `#000000`, `#08090a`, `#0000ee`, `#f4f5f5`, `#e4e6e7`, `#fafafa`, `#d4d6d8`, `#74797d`, `#52575b`, `#a1a5aa`

### Gradients

```css
background-image: linear-gradient(rgba(8, 9, 10, 0) 0%, rgb(8, 9, 10) 95%, rgb(8, 9, 10) 126%);
```

```css
background-image: radial-gradient(126.412% 304.103% at -28.2813% -57.4751%, rgb(24, 26, 27) 0%, rgba(24, 26, 27, 0) 100%);
```

```css
background-image: radial-gradient(110.913% 118.397% at -1.61597% 1.88277e-06%, rgb(24, 26, 27) 0%, rgba(24, 26, 27, 0) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 7061 |
| `#0000ee` | text, border | 582 |
| `#74797d` | text, border | 163 |
| `#fafafa` | background, text, border | 162 |
| `#d4d6d8` | text, border | 104 |
| `#f4f5f5` | text, border, background | 103 |
| `#08090a` | background, text, border | 63 |
| `#a1a5aa` | text, border | 50 |
| `#0eea8e` | background, text, border | 43 |
| `#181a1b` | background | 17 |
| `#e4e6e7` | text, border | 12 |
| `#52575b` | text, border | 10 |
| `#666666` | text, border | 2 |

## Typography

### Font Families

- **Uncut Sans Medium** — used for all (242 elements)
- **Times New Roman** — used for body (31 elements)
- **Geist Mono** — used for body (31 elements)
- **Uncut Sans Variable** — used for body (4 elements)
- **Uncut Sans Regular** — used for body (1 elements)
- **Inter** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 64px | 4rem | 500 | 64px | -3.84px | h1, div, h3 |
| 45px | 2.8125rem | 500 | 47.25px | -2.25px | h2, span |
| 37px | 2.3125rem | 500 | 40.7px | -1.665px | h3 |
| 31px | 1.9375rem | 500 | 35.65px | -1.24px | h4 |
| 26px | 1.625rem | 500 | 32.5px | -0.91px | h5 |
| 22px | 1.375rem | 500 | 28.6px | -0.66px | p, span, div |
| 20px | 1.25rem | 500 | 20px | -0.4px | p |
| 18px | 1.125rem | 500 | 24.3px | -0.54px | p |
| 16px | 1rem | 400 | normal | normal | html, head, meta, script |
| 15px | 0.9375rem | 500 | 21px | -0.3px | p, span |
| 14px | 0.875rem | 400 | 16.8px | normal | input, p |
| 13px | 0.8125rem | 500 | 18.85px | -0.195px | p |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |
| 11px | 0.6875rem | 500 | 11px | 0.11px | p, span |

### Heading Scale

```css
h1 { font-size: 64px; font-weight: 500; line-height: 64px; }
h2 { font-size: 45px; font-weight: 500; line-height: 47.25px; }
h3 { font-size: 37px; font-weight: 500; line-height: 40.7px; }
h4 { font-size: 31px; font-weight: 500; line-height: 35.65px; }
h5 { font-size: 26px; font-weight: 500; line-height: 32.5px; }
```

### Body Text

```css
body { font-size: 15px; font-weight: 500; line-height: 21px; }
```

### Font Weights in Use

`400` (3835x), `500` (276x), `600` (1x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-32 | 32px | 2rem |
| spacing-48 | 48px | 3rem |
| spacing-61 | 61px | 3.8125rem |
| spacing-80 | 80px | 5rem |
| spacing-99 | 99px | 6.1875rem |
| spacing-120 | 120px | 7.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 16 |
| md | 8px | 6 |
| lg | 11px | 2 |
| full | 36px | 7 |
| full | 50px | 1 |
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

**xs** — blur: 3px
```css
box-shadow: rgba(255, 255, 255, 0.3) 0px 0px 3px 0px, rgba(255, 255, 255, 0.2) 0px 2px 7px 0px;
```

**xs** — blur: 3px
```css
box-shadow: rgba(46, 255, 157, 0.3) 0px 0px 3px 0px, rgba(255, 255, 255, 0.2) 0px 2px 7px 0px;
```

**md** — blur: 10px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 10px 0px;
```

**xl** — blur: 141px
```css
box-shadow: rgba(0, 0, 0, 0.37) -62px 16px 141px 0px, rgba(0, 0, 0, 0.32) -247px 64px 250px 0px, rgba(0, 0, 0, 0.19) -557px 145px 250px 0px, rgba(0, 0, 0, 0.06) -990px 257px 250px 0px, rgba(0, 0, 0, 0.01) -1546px 402px 250px 0px;
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

**Durations:** `0.001s`

### Common Transitions

```css
transition: overflow 0.001s allow-discrete;
transition: all;
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
  background-color: rgb(244, 245, 245);
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 7.5px;
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

### Links (45 instances)

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
  background-color: rgb(8, 9, 10);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
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

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(212, 214, 216);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(212, 214, 216);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(244, 245, 245);
  color: rgb(0, 0, 0);
  padding: 7.5px 20px 7.5px 20px;
  border-radius: 0px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**3 grid containers** and **971 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1400px | 0px |
| 100% | 0px |
| 867px | 0px |
| 280px | 0px |
| 721px | 0px |
| 40% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 4-column | 2x |
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 560px 560px;
grid-template-columns: 280px 280px 280px 280px;
grid-template-columns: 280px 280px 280px 280px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 670x |
| row/wrap | 1x |
| row/nowrap | 300x |

**Gap values:** `100px`, `10px`, `12px`, `16px`, `20px`, `24px`, `32px`, `36px`, `40px`, `48px`, `4px`, `6px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 76/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 75/100 |
| Shadow Consistency | 90/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 6 font families — consider limiting to 2 (heading + body)
- 18 !important rules — prefer specificity over overrides
- 70% of CSS is unused — consider purging
- 8803 duplicate CSS declarations

## Gradients

**3 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 3 | bold |
| radial | — | 3 | bold |
| radial | — | 3 | bold |

```css
background: linear-gradient(rgba(8, 9, 10, 0) 0%, rgb(8, 9, 10) 95%, rgb(8, 9, 10) 126%);
background: radial-gradient(126.412% 304.103% at -28.2813% -57.4751%, rgb(24, 26, 27) 0%, rgba(24, 26, 27, 0) 100%);
background: radial-gradient(110.913% 118.397% at -1.61597% 1.88277e-06%, rgb(24, 26, 27) 0%, rgba(24, 26, 27, 0) 100%);
```

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,30 | div.f.r.a.m.e.r.-.q.t.n.y.l.1.-.c.o.n.t.a.i.n.e.r, div, div |
| base | -1,3 | div.f.r.a.m.e.r.-.2.v.f.6.t.1.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.4.z.j.b.q.w.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.y.k.h.m.e.o.-.c.o.n.t.a.i.n.e.r |

**Issues:**
- [object Object]

## SVG Icons

**42 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 2 |
| sm | 8 |
| md | 32 |

**Icon colors:** `rgb(244, 245, 245)`, `rgb(0, 0, 0)`, `white`, `#74797D`, `#0EEB8F`, `#FAFAFA`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Fragment Mono | cdn | 400 | normal |
| Geist Mono | cdn | 400, 500, 700 | normal |
| Uncut Sans Medium | self-hosted | 500 | normal |
| Uncut Sans Bold | self-hosted | 700 | normal |
| Uncut Sans Bold Italic | self-hosted | 700 | italic |
| Uncut Sans Regular | self-hosted | 400 | normal |
| Inter | self-hosted | 400, 600, 700 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 42 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 20 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 8 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 7 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (27x), 14:1 (13x), 16:9 (8x), 3:4 (5x), 3:2 (4x), 3.27:1 (4x), 2:3 (4x), 4:3 (2x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** all-lowercase (tight)

### Top CTA Verbs

- **submit** (1)

### Button Copy Patterns

- "submit" (1×)

### Sample Headings

> Scale your operations without scaling your team
> 94%
> 60h
> 4.9
> Scale your operations without scaling your team
> 94%
> 60h
> 4.9
> RetailNest stopped losing leads and hours to manual support
> 60+ 

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** We design, build, and deploy custom AI agents that automate support, qualify leads, and streamline operations 24/7. Get your first agent live in weeks, not months.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → comparison → testimonial → logo-wall → testimonial → content → testimonials → content → testimonial → content → testimonial → testimonial → testimonial → pricing → content → faq → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | comparison | Scale your operations without scaling your team | 0.7 |
| 2 | testimonial | Scale your operations without scaling your team | 0.8 |
| 3 | logo-wall | — | 0.85 |
| 4 | testimonial | — | 0.8 |
| 5 | content | — | 0.3 |
| 6 | testimonials | — | 0.4 |
| 7 | content | — | 0.3 |
| 8 | testimonial | — | 0.8 |
| 9 | content | — | 0.3 |
| 10 | testimonial | — | 0.8 |
| 11 | testimonial | — | 0.8 |
| 12 | testimonial | — | 0.8 |
| 13 | pricing | — | 0.4 |
| 14 | content | Practical insights on AI agents and automation | 0.3 |
| 15 | faq | — | 0.85 |
| 16 | footer | Ready to Deploy Your First AI Agent | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.193 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 3 |

## Imagery Style

**Label:** `photography` (confidence 0.026)
**Counts:** total 77, svg 1, icon 18, screenshot-like 0, photo-like 4
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Uncut Sans Medium` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
