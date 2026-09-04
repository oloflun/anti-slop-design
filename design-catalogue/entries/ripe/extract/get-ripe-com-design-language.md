# Design Language: RIPE - Leadership Is a Lifestyle

> Extracted from `https://www.get-ripe.com/` on September 4, 2026
> 1804 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#0a1714` | rgb(10, 23, 20) | hsl(166, 39%, 6%) | 1993 |
| Secondary | `#fff7eb` | rgb(255, 247, 235) | hsl(36, 100%, 96%) | 343 |
| Accent | `#fff8bb` | rgb(255, 248, 187) | hsl(54, 100%, 87%) | 12 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1165 |
| `#61805b` | hsl(110, 17%, 43%) | 47 |
| `#ffffff` | hsl(0, 0%, 100%) | 12 |
| `#767676` | hsl(0, 0%, 46%) | 11 |
| `#bbd0b7` | hsl(110, 21%, 77%) | 2 |

### Background Colors

Used on large-area elements: `#efe5d4`, `#fff7eb`, `#0a1714`, `#61805b`, `#fae2cd`, `#fff8bb`

### Text Colors

Text color palette: `#000000`, `#0a1714`, `#0000ee`, `#fff7eb`, `#61805b`, `#eecbe6`

### Gradients

```css
background-image: linear-gradient(90deg, rgb(239, 229, 212) 0%, rgba(245, 234, 218, 0) 100%);
```

```css
background-image: linear-gradient(270deg, rgb(239, 229, 212) 0%, rgba(245, 234, 218, 0) 100%);
```

```css
background-image: linear-gradient(0deg, rgba(10, 23, 20, 0) 0%, rgba(10, 23, 20, 0.64) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#0a1714` | text, border, background | 1993 |
| `#000000` | text, border | 1165 |
| `#fff7eb` | background, text, border | 343 |
| `#0000ee` | text, border | 112 |
| `#61805b` | text, border, background | 47 |
| `#efe5d4` | background | 16 |
| `#fff8bb` | background | 12 |
| `#ffffff` | background | 12 |
| `#767676` | border | 11 |
| `#eecbe6` | background, text, border | 4 |
| `#bbd0b7` | background | 2 |
| `#d2e7fb` | background | 2 |
| `#ed7538` | background | 1 |

## Typography

### Font Families

- **Inter** — used for all (1014 elements)
- **BN Nautic Grotesk Bold** — used for all (139 elements)
- **Times New Roman** — used for body (35 elements)
- **SeriouslyNostalgic Condensed** — used for headings (27 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 128px | 8rem | 700 | 104px | normal | h1, span, h2 |
| 96px | 6rem | 700 | 80px | normal | div, h2 |
| 88px | 5.5rem | 400 | 84px | 2px | h2 |
| 72px | 4.5rem | 700 | 56px | normal | h2, span |
| 64px | 4rem | 400 | 64px | 1px | h2 |
| 48px | 3rem | 400 | 48px | 1px | h3 |
| 32px | 2rem | 600 | 32px | normal | a, svg, path |
| 20px | 1.25rem | 600 | 28px | -0.25px | h3 |
| 18px | 1.125rem | 400 | 28px | normal | p, span |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 14px | 0.875rem | 700 | 12px | 1.25px | p |
| 13px | 0.8125rem | 400 | 20px | normal | p, a |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |

### Heading Scale

```css
h1 { font-size: 128px; font-weight: 700; line-height: 104px; }
h2 { font-size: 96px; font-weight: 700; line-height: 80px; }
h2 { font-size: 88px; font-weight: 400; line-height: 84px; }
h2 { font-size: 72px; font-weight: 700; line-height: 56px; }
h2 { font-size: 64px; font-weight: 400; line-height: 64px; }
h3 { font-size: 48px; font-weight: 400; line-height: 48px; }
h3 { font-size: 20px; font-weight: 600; line-height: 28px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (1574x), `700` (167x), `600` (63x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-32 | 32px | 2rem |
| spacing-37 | 37px | 2.3125rem |
| spacing-48 | 48px | 3rem |
| spacing-53 | 53px | 3.3125rem |
| spacing-61 | 61px | 3.8125rem |
| spacing-80 | 80px | 5rem |
| spacing-120 | 120px | 7.5rem |
| spacing-160 | 160px | 10rem |
| spacing-200 | 200px | 12.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| lg | 16px | 9 |
| xl | 24px | 60 |
| full | 32px | 15 |
| full | 100px | 3 |

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
| lg | 1023px | max-width |
| lg | 1024px | min-width |
| 1439px | 1439px | max-width |
| 1440px | 1440px | max-width |

## Transitions & Animations

**Durations:** `0.4s`

### Common Transitions

```css
transition: all;
transition: opacity 0.4s;
transition: transform 0.4s;
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

### Buttons (3 instances)

```css
.button {
  background-color: rgba(255, 247, 235, 0);
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 16px;
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

### Links (30 instances)

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
  background-color: rgb(239, 229, 212);
  color: rgb(0, 0, 0);
  padding-top: 160px;
  padding-bottom: 32px;
  font-size: 12px;
}
```

### Modals (8 instances)

```css
.modal {
  background-color: rgba(10, 23, 20, 0.48);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(255, 247, 235, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 16px;
  border: 0px none rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(10, 23, 20, 0.08);
  color: rgb(0, 0, 0);
  padding: 0px 16px 0px 16px;
  border-radius: 32px;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(10, 23, 20);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(10, 23, 20);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**2 grid containers** and **361 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1440px | 0px |
| 868px | 0px |
| 1144px | 0px |
| 448px | 0px |
| 100% | 0px |
| 968px | 0px |
| 480px | 0px |
| 680px | 0px |
| 918px | 0px |
| 798px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 4-column | 2x |

### Grid Templates

```css
grid-template-columns: 306.125px 306.141px 306.141px 306.141px;
gap: 16px;
grid-template-columns: 306.125px 306.141px 306.141px 306.141px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 228x |
| row/nowrap | 133x |

**Gap values:** `10px`, `12px`, `160px`, `16px`, `20px`, `24px`, `24px normal`, `32px`, `40px`, `48px`, `4px`, `4px normal`, `53px`, `61px`, `64px`, `80px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 80/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 18 !important rules — prefer specificity over overrides
- 3845 duplicate CSS declarations

## Gradients

**3 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 90deg | 2 | brand |
| linear | 270deg | 2 | brand |
| linear | 0deg | 2 | brand |

```css
background: linear-gradient(90deg, rgb(239, 229, 212) 0%, rgba(245, 234, 218, 0) 100%);
background: linear-gradient(270deg, rgb(239, 229, 212) 0%, rgba(245, 234, 218, 0) 100%);
background: linear-gradient(0deg, rgba(10, 23, 20, 0) 0%, rgba(10, 23, 20, 0.64) 100%);
```

## Z-Index Map

**7 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | iframe.s.t.a.t.u.s._.h.i.d.d.e.n |
| sticky | 10,10 | div.f.r.a.m.e.r.-.1.4.t.g.n.3.3.-.c.o.n.t.a.i.n.e.r |
| base | 0,8 | div.f.r.a.m.e.r.-.1.m.0.c.3.l.b, div.f.r.a.m.e.r.-.1.m.0.c.3.l.b, div.f.r.a.m.e.r.-.1.m.0.c.3.l.b |

**Issues:**
- [object Object]

## SVG Icons

**2 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 1 |
| lg | 1 |

**Icon colors:** `rgb(0, 0, 0)`, `var(--token-b15cc266-f93b-4773-ab8b-688355e14153, rgb(255, 247, 235))`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| BN Nautic Grotesk Bold | self-hosted | 700 | normal |
| SeriouslyNostalgic Condensed | self-hosted | 400 | normal |
| Rebel Rush Bold | self-hosted | 700 | normal |
| Inter | self-hosted | 400, 600, 700, 900 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 8 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 7 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 5 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (16x), 1:1 (4x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `400ms` | 400 |

## Component Anatomy

### button — 3 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (verbose)

### Top CTA Verbs

- **stay** (1)

### Button Copy Patterns

- "stay ripe" (1×)

### Sample Headings

> LEADERSHIP IS A LIFESTYLE.
> WE MEET YOU WHERE YOU ARE. THEN WE PUSH YOU FURTHER.
> Get Your Mind Ripe
> OYP Executive Membership
> Workshops & Gatherings
> LEADERSHIP IS A LIFESTYLE.
> WE MEET YOU WHERE YOU ARE. THEN WE PUSH YOU FURTHER.
> Get Your Mind Ripe
> OYP Executive Membership
> Workshops & Gatherings

## Page Intent

**Type:** `landing` (confidence 0.59)
**Description:** Leadership tools, executive coaching, and performance programs for individuals and companies ready to lead at the highest level.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): testimonial → content → nav → nav → testimonial → testimonials → testimonial → testimonial → testimonial → content → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | testimonial | LEADERSHIP IS A LIFESTYLE. | 0.8 |
| 3 | content | LEADERSHIP IS A LIFESTYLE. | 0.3 |
| 4 | testimonial | WE MEET YOU WHERE YOU ARE. THEN WE PUSH YOU FURTHER. | 0.8 |
| 5 | testimonials | High-performing teams aren't born. They're coached. | 0.4 |
| 6 | testimonial | THE RESOURCE WE NEEDED DIDN'T EXIST, SO WE MADE IT. | 0.8 |
| 7 | testimonial | When leadership becomes a way of being in the world, everything shifts. | 0.8 |
| 8 | testimonial | — | 0.8 |
| 9 | content | FOLLOW US | 0.3 |
| 10 | content | — | 0.3 |
| 11 | content | — | 0.3 |
| 12 | footer | A newsletter that respects your time and pushes you to your potential.  | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.27 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 3 |

## Imagery Style

**Label:** `photography` (confidence 0.4)
**Counts:** total 20, svg 3, icon 0, screenshot-like 0, photo-like 14
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
