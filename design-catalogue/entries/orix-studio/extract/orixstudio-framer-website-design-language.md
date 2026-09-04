# Design Language: Orix-Studio® | Creative Agency Template

> Extracted from `https://orixstudio.framer.website/` on September 4, 2026
> 1518 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#df0203` | rgb(223, 2, 3) | hsl(360, 98%, 44%) | 1 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 542 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 2139 |
| `#ffffff` | hsl(0, 0%, 100%) | 342 |
| `#646464` | hsl(0, 0%, 39%) | 108 |
| `#767676` | hsl(0, 0%, 46%) | 11 |
| `#3d3d3d` | hsl(0, 0%, 24%) | 6 |
| `#d6d6d6` | hsl(0, 0%, 84%) | 6 |

### Background Colors

Used on large-area elements: `#ffffff`, `#000000`, `#3d3d3d`, `#f7f7f7`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#ffffff`, `#3d3d3d`, `#646464`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 2139 |
| `#0000ee` | text, border | 542 |
| `#ffffff` | background, text, border | 342 |
| `#646464` | text, border, background | 108 |
| `#767676` | border | 11 |
| `#3d3d3d` | text, border, background | 6 |
| `#d6d6d6` | background | 6 |
| `#df0203` | background | 1 |

## Typography

### Font Families

- **Inter Display** — used for all (250 elements)
- **Instrument Sans** — used for body (230 elements)
- **Times New Roman** — used for body (30 elements)
- **Open Sauce One** — used for all (24 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 180px | 11.25rem | 500 | 162px | -12.6px | h1 |
| 178.579px | 11.1612rem | 500 | 160.721px | -10.7148px | h1 |
| 42px | 2.625rem | 500 | normal | normal | div, span |
| 32px | 2rem | 500 | 44.8px | -1.28px | span, h3, div |
| 28px | 1.75rem | 500 | 36.4px | -1.68px | p, h4 |
| 24px | 1.5rem | 500 | 33.6px | normal | h5 |
| 20px | 1.25rem | 500 | 30px | normal | p, span |
| 18px | 1.125rem | 500 | 21.6px | 0.72px | p |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 14px | 0.875rem | 500 | 21px | -0.28px | p, input, textarea |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |

### Heading Scale

```css
h1 { font-size: 180px; font-weight: 500; line-height: 162px; }
h1 { font-size: 178.579px; font-weight: 500; line-height: 160.721px; }
h3 { font-size: 32px; font-weight: 500; line-height: 44.8px; }
h4 { font-size: 28px; font-weight: 500; line-height: 36.4px; }
h5 { font-size: 24px; font-weight: 500; line-height: 33.6px; }
```

### Body Text

```css
body { font-size: 32px; font-weight: 500; line-height: 44.8px; }
```

### Font Weights in Use

`400` (1014x), `500` (500x), `600` (4x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-20 | 20px | 1.25rem |
| spacing-32 | 32px | 2rem |
| spacing-54 | 54px | 3.375rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-130 | 130px | 8.125rem |
| spacing-200 | 200px | 12.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 10px | 1 |
| lg | 16px | 2 |
| full | 50px | 36 |
| full | 999px | 18 |

## Box Shadows

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(0, 0, 0) 0px 0px 0px 1px inset;
```

**xs** — blur: 0.711334px
```css
box-shadow: rgba(0, 0, 0, 0.14) 0px 0.711334px 0.711334px -0.55px, rgba(0, 0, 0, 0.14) 0px 1.93715px 1.93715px -1.1px, rgba(0, 0, 0, 0.13) 0px 4.25328px 4.25328px -1.65px, rgba(0, 0, 0, 0.13) 0px 9.44132px 9.44132px -2.2px, rgba(0, 0, 0, 0.11) 0px 24px 24px -2.75px;
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
| md | 767px | max-width |
| md | 768px | min-width |
| md | 810px | max-width |
| md | 820px | max-width |
| xl | 1239px | max-width |
| xl | 1240px | max-width |
| 1349px | 1349px | max-width |

## Transitions & Animations

### Common Transitions

```css
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

### Links (43 instances)

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
  background-color: rgba(0, 0, 0, 0.25);
  color: rgb(0, 0, 0);
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 25px;
  padding-right: 25px;
  position: relative;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding-top: 64px;
  padding-bottom: 22px;
  font-size: 12px;
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

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

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
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**7 grid containers** and **475 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1240px | 25px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 3x |
| 3-column | 2x |
| 4-column | 1x |
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 404.5px 404.5px;
gap: 24px;
grid-template-columns: 404.5px 404.5px;
gap: 24px;
grid-template-columns: 380.656px 380.672px 380.656px;
gap: 24px;
grid-template-columns: 583px 583px;
gap: 64px 24px;
grid-template-columns: 279.5px 279.5px 279.5px 279.5px;
gap: 24px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 258x |
| row/nowrap | 217x |

**Gap values:** `100px`, `10px`, `12px`, `130px`, `14px`, `16px`, `1px`, `200px`, `20px`, `24px`, `2px`, `32px`, `3px`, `54px`, `5px`, `64px 24px`, `6px`, `80px`, `8px`

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
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 17 !important rules — prefer specificity over overrides
- 71% of CSS is unused — consider purging
- 5270 duplicate CSS declarations

## Z-Index Map

**7 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div, iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.c.b.b.7.x.8.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.1.7.7.n.q.a.f.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.6.a.s.4.z.y.-.c.o.n.t.a.i.n.e.r |
| base | 0,5 | div, div.f.r.a.m.e.r.-.3.c.g.1.7.a, div.f.r.a.m.e.r.-.1.j.4.l.9.v.g |

**Issues:**
- [object Object]

## SVG Icons

**11 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 4 |
| md | 6 |

**Icon colors:** `rgb(0, 0, 0)`, `rgb(255, 255, 255)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Instrument Sans | cdn | 500 | normal |
| Inter | self-hosted | 400, 600 | normal |
| Inter Display | self-hosted | 500, 600, 700 | normal, italic |
| Open Sauce One | self-hosted | 500 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| avatar | 13 | objectFit: cover, borderRadius: 50px, shape: circular |
| general | 12 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 7 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (23x), 4:3 (8x), 1.17:1 (3x), 3:2 (2x), 3:4 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

## Component Anatomy

### input — 3 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (verbose)

### Top CTA Verbs

- **send** (1)

### Button Copy Patterns

- "send message" (1×)

### Sample Headings

> ORIX-STUDIO®
> Explore Orix services designed to elevate brands. From creative design to digital solutions, we craft impactful results that drive growth, build strong identities, and deliver long-lasting success for every client.
> Discover flexible pricing plans designed to suit every need. At Orix, we provide clear, transparent packages that deliver exceptional value, ensuring your brand receives professional design solutions without compromise.
> $29
> Ready to take your brand to the next level? Partner with Orix today and access professional design solutions crafted to deliver lasting impact, creativity, and measurable growth for your business.
> ORIX-STUDIO®

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** A modern creative agency website template crafted for designers, studios, and digital brands. Orix helps showcase work, present services, and build lasting trust with clients effectively.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → content → content → content → content → content → content → testimonials → pricing → content → faq → hero → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | ORIX-STUDIO® | 0.4 |
| 2 | content | — | 0.3 |
| 3 | content | — | 0.3 |
| 4 | content | — | 0.3 |
| 5 | content | Explore Orix services designed to elevate brands. From creative design to digita | 0.3 |
| 6 | content | — | 0.3 |
| 7 | content | — | 0.3 |
| 8 | testimonials | — | 0.4 |
| 9 | pricing | Discover flexible pricing plans designed to suit every need. At Orix, we provide | 0.4 |
| 10 | content | — | 0.3 |
| 11 | faq | — | 0.85 |
| 12 | hero | Ready to take your brand to the next level? Partner with Orix today and access p | 0.4 |
| 13 | footer | ORIX-STUDIO® | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.249 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.095)
**Counts:** total 37, svg 0, icon 4, screenshot-like 0, photo-like 7
**Dominant aspect:** square-ish
**Radius profile on images:** rounded

## Component Library

**Detected:** `vuetify` (confidence 0.46)

Evidence:
- 8 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter Display` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
