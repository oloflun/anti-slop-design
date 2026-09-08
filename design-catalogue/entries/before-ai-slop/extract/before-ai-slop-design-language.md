# Design Language: Flowstack — The All-in-One Platform for Modern Teams

> Extracted from `http://127.0.0.1:3055/sites/before-ai-slop.html` on September 8, 2026
> 119 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#0f172a` | rgb(15, 23, 42) | hsl(222, 47%, 11%) | 3 |
| Secondary | `#059669` | rgb(5, 150, 105) | hsl(161, 94%, 30%) | 3 |
| Accent | `#6366f1` | rgb(99, 102, 241) | hsl(239, 84%, 67%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 114 |
| `#ffffff` | hsl(0, 0%, 100%) | 20 |
| `#475569` | hsl(215, 19%, 35%) | 17 |
| `#64748b` | hsl(215, 16%, 47%) | 13 |
| `#94a3b8` | hsl(215, 20%, 65%) | 7 |
| `#eef2ff` | hsl(226, 100%, 97%) | 1 |
| `#334155` | hsl(215, 25%, 27%) | 1 |
| `#ecfdf5` | hsl(152, 81%, 96%) | 1 |

### Background Colors

Used on large-area elements: `#fbfaf7`, `#ffffff`, `#f8fafc`

### Text Colors

Text color palette: `#1f2937`, `#475569`, `#ffffff`, `#4f46e5`, `#334155`, `#64748b`, `#059669`, `#94a3b8`

### Gradients

```css
background-image: linear-gradient(135deg, rgb(99, 102, 241) 0%, rgb(139, 92, 246) 50%, rgb(236, 72, 153) 100%);
```

```css
background-image: linear-gradient(135deg, rgb(30, 64, 175) 0%, rgb(99, 102, 241) 100%);
```

```css
background-image: linear-gradient(to right bottom, rgb(244, 114, 182), rgb(251, 113, 133));
```

```css
background-image: linear-gradient(to right bottom, rgb(251, 191, 36), rgb(251, 146, 60));
```

```css
background-image: linear-gradient(to right bottom, rgb(52, 211, 153), rgb(45, 212, 191));
```

```css
background-image: linear-gradient(to right bottom, rgb(129, 140, 248), rgb(167, 139, 250));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 114 |
| `#1f2937` | text | 63 |
| `#ffffff` | background, text, border | 20 |
| `#475569` | text | 17 |
| `#64748b` | text | 13 |
| `#94a3b8` | text | 7 |
| `#0f172a` | background | 3 |
| `#059669` | text | 3 |
| `#4f46e5` | text | 2 |
| `#eef2ff` | background | 1 |
| `#6366f1` | background | 1 |
| `#334155` | text | 1 |
| `#cbd5e1` | border | 1 |
| `#ecfdf5` | background | 1 |

## Typography

### Font Families

- **Inter** — used for all (108 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 60px | 3.75rem | 700 | 60px | -1.5px | h1, span |
| 48px | 3rem | 700 | 48px | normal | div |
| 36px | 2.25rem | 700 | 40px | normal | h2 |
| 30px | 1.875rem | 700 | 36px | normal | h2 |
| 20px | 1.25rem | 600 | 28px | normal | div |
| 18px | 1.125rem | 400 | 29.25px | normal | p, div, span, h3 |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |
| 14px | 0.875rem | 400 | 20px | normal | div, a, span, p |
| 12px | 0.75rem | 500 | 16px | normal | span, div, p, footer |

### Heading Scale

```css
h1 { font-size: 60px; font-weight: 700; line-height: 60px; }
h2 { font-size: 36px; font-weight: 700; line-height: 40px; }
h2 { font-size: 30px; font-weight: 700; line-height: 36px; }
h3 { font-size: 18px; font-weight: 400; line-height: 29.25px; }
```

### Body Text

```css
body { font-size: 18px; font-weight: 400; line-height: 29.25px; }
```

### Font Weights in Use

`400` (83x), `600` (20x), `700` (9x), `500` (7x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-128 | 128px | 8rem |
| spacing-216 | 216px | 13.5rem |
| spacing-264 | 264px | 16.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 8px | 4 |
| lg | 16px | 4 |
| full | 9999px | 12 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px;
```

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-ring-offset-width: 0px;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgb(59 130 246 / 0.5);
--tw-ring-offset-color: #fff;
```

### Spacing

```css
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
| md | 768px | min-width |

## Transitions & Animations

### Common Transitions

```css
transition: all;
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Cards (1 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 16px;
  box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px;
  padding-top: 24px;
  padding-right: 24px;
}
```

### Links (11 instances)

```css
.link {
  color: rgb(71, 85, 105);
  font-size: 14px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  background-color: rgba(255, 255, 255, 0.9);
  color: rgb(31, 41, 55);
  padding-top: 12px;
  padding-bottom: 12px;
  padding-left: 24px;
  padding-right: 24px;
  position: static;
  box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(100, 116, 139);
  padding-top: 32px;
  padding-bottom: 32px;
  font-size: 12px;
}
```

## Layout System

**4 grid containers** and **16 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1152px | 24px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 4-column | 2x |
| 2-column | 1x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 528px 528px;
gap: 48px;
grid-template-columns: 352px 352px 352px;
gap: 24px;
grid-template-columns: 258px 258px 258px 258px;
gap: 24px;
grid-template-columns: 110.5px 110.5px 110.5px 110.5px;
gap: 12px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 14x |
| row/wrap | 2x |

**Gap values:** `12px`, `24px`, `28px`, `40px`, `48px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 4 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#0f172a` | 17.85:1 | AAA |
| `#4f46e5` | `#eef2ff` | 5.62:1 | AA |

## Design System Score

**Overall: 93/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 90/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 97% of CSS is unused — consider purging
- 147 duplicate CSS declarations

## Gradients

**6 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 135deg | 3 | bold |
| linear | 135deg | 2 | brand |
| linear | to right bottom | 2 | brand |
| linear | to right bottom | 2 | brand |
| linear | to right bottom | 2 | brand |
| linear | to right bottom | 2 | brand |

```css
background: linear-gradient(135deg, rgb(99, 102, 241) 0%, rgb(139, 92, 246) 50%, rgb(236, 72, 153) 100%);
background: linear-gradient(135deg, rgb(30, 64, 175) 0%, rgb(99, 102, 241) 100%);
background: linear-gradient(to right bottom, rgb(244, 114, 182), rgb(251, 113, 133));
background: linear-gradient(to right bottom, rgb(251, 191, 36), rgb(251, 146, 60));
background: linear-gradient(to right bottom, rgb(52, 211, 153), rgb(45, 212, 191));
```

## Z-Index Map

**1 unique z-index values** across 1 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 30,30 | header.s.t.i.c.k.y. .t.o.p.-.4. .z.-.3.0. .m.x.-.a.u.t.o. .m.a.x.-.w.-.5.x.l. .p.x.-.4 |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Inter | google-fonts | 400, 500, 600, 700 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Brand Voice

**Tone:** neutral · **Pronoun:** you-only · **Headings:** Sentence case (tight)

### Sample Headings

> The all-in-one platform for modern teams.
> Everything you need to ship faster
> Lightning fast
> Seamless integrations
> Next-gen automation
> Real results from real teams
> Ready to transform your workflow?

## Page Intent

**Type:** `pricing` (confidence 0.46)

Alternates: blog-post (0.35), auth (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → feature-grid → content → content → testimonials → testimonial → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | feature-grid | The all-in-one platform for modern teams. | 0.8 |
| 3 | content | — | 0.3 |
| 4 | content | Everything you need to ship faster | 0.3 |
| 5 | testimonials | Real results from real teams | 0.4 |
| 6 | testimonial | Ready to transform your workflow? | 0.8 |
| 7 | footer | — | 0.95 |

## Material Language

**Label:** `material-you` (confidence 0.45)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.342 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 6 |

## Component Library

**Detected:** `tailwindcss` (confidence 0.99)

Evidence:
- tailwind-like class density 93%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
