# Design Language: Apollo Workspace | Executive Suites & Offices — Edmond, OK

> Extracted from `https://apolloworkspace.com` on September 4, 2026
> 369 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#e97451` | rgb(233, 116, 81) | hsl(14, 78%, 62%) | 97 |
| Secondary | `#2d0f06` | rgb(45, 15, 6) | hsl(14, 76%, 10%) | 3 |
| Accent | `#918037` | rgb(145, 128, 55) | hsl(49, 45%, 39%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#f9f8f0` | hsl(53, 43%, 96%) | 136 |
| `#0c0503` | hsl(13, 60%, 3%) | 38 |
| `#6f675e` | hsl(32, 8%, 40%) | 12 |
| `#e1dccf` | hsl(43, 23%, 85%) | 6 |

### Background Colors

Used on large-area elements: `#e1dccf`, `#0c0503`, `#2d0f06`, `#070100`, `#918037`

### Text Colors

Text color palette: `#3c261c`, `#e97451`, `#f9f8f0`, `#f2efde`, `#0c0503`, `#6f675e`

### Gradients

```css
background-image: linear-gradient(to right, oklab(0.214519 0.0414231 0.032529 / 0.95) 0%, oklab(0.214519 0.0414231 0.032529 / 0.6) 50%, rgba(0, 0, 0, 0) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#3c261c` | text, border, background | 335 |
| `#f9f8f0` | text, border | 136 |
| `#f2efde` | text, border | 116 |
| `#e97451` | text, border, background | 97 |
| `#0c0503` | background, text, border | 38 |
| `#6f675e` | text, border | 12 |
| `#e1dccf` | background | 6 |
| `#2d0f06` | background | 3 |
| `#918037` | background | 1 |

## Typography

### Font Families

- **Mona Sans** — used for all (333 elements)
- **paradigm-pro** — used for all (35 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 72px | 4.5rem | 300 | 75.6px | 0.72px | h2, span |
| 56px | 3.5rem | 300 | 58.8px | 0.56px | h3, span, h2, br |
| 24px | 1.5rem | 300 | 33px | normal | p |
| 18px | 1.125rem | 400 | 29.25px | normal | div, p, li, span |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, link |
| 14px | 0.875rem | 500 | 20px | 1.96px | ul, li, a, div |
| 12px | 0.75rem | 500 | 16px | 1.68px | ul, li, a, h1 |

### Heading Scale

```css
h2 { font-size: 72px; font-weight: 300; line-height: 75.6px; }
h3 { font-size: 56px; font-weight: 300; line-height: 58.8px; }
h1 { font-size: 12px; font-weight: 500; line-height: 16px; }
```

### Body Text

```css
body { font-size: 18px; font-weight: 400; line-height: 29.25px; }
```

### Font Weights in Use

`400` (281x), `500` (52x), `300` (35x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-8 | 8px | 0.5rem |
| spacing-64 | 64px | 4rem |
| spacing-112 | 112px | 7rem |
| spacing-207 | 207px | 12.9375rem |

## CSS Custom Properties

### Colors

```css
--color-terracotta: #e97451;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--color-ink: #3c261c;
--color-linen: #f9f8f0;
--color-espresso-deep: #2d0f06;
--tw-inset-ring-shadow: 0 0 #0000;
--color-espresso: #3c261c;
--tw-ring-offset-color: #fff;
--color-ink-muted: #6f675e;
--color-cream: #f7efc5;
--tw-border-style: solid;
--color-electric: #4a43dd;
--tw-ring-offset-width: 0px;
--color-black: #000;
--color-brick: #71250e;
--color-olive: #918037;
--color-parchment: #e1dccf;
```

### Spacing

```css
--spacing: .25rem;
--tw-space-y-reverse: 0;
```

### Typography

```css
--text-2xl: 1.5rem;
--leading-relaxed: 1.625;
--leading-snug: 1.375;
--text-h2: clamp(2.25rem, 1.65rem + 2.6vw, 3.5rem);
--text-7xl: 4.5rem;
--text-lg: 1.125rem;
--text-5xl--line-height: 1;
--text-2xl--line-height: calc(2 / 1.5);
--text-base--line-height: calc(1.5 / 1);
--text-display: clamp(2.75rem, 1.5rem + 5.4vw, 4.5rem);
--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
--tracking-wide: .025em;
--text-xl--line-height: calc(1.75 / 1.25);
--font-weight-semibold: 600;
--text-sm: .875rem;
--text-lg--line-height: calc(1.75 / 1.125);
--font-sans: "Mona Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
--text-4xl: 2.25rem;
--text-sm--line-height: calc(1.25 / .875);
--text-3xl--line-height: calc(2.25 / 1.875);
--text-5xl: 3rem;
--text-6xl: 3.75rem;
--text-3xl: 1.875rem;
--text-xs--line-height: calc(1 / .75);
--default-font-family: "Mona Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
--font-weight-light: 300;
--font-weight-medium: 500;
--font-weight-normal: 400;
--text-xs: .75rem;
--font-display: "paradigm-pro", "Cormorant Garamond", Georgia, serif;
--text-h3: clamp(1.875rem, 1.55rem + 1.5vw, 2.75rem);
--text-7xl--line-height: 1;
--text-6xl--line-height: 1;
--text-4xl--line-height: calc(2.5 / 2.25);
--text-xl: 1.25rem;
--text-base: 1rem;
--default-mono-font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
```

### Shadows

```css
--tw-inset-shadow-alpha: 100%;
--tw-drop-shadow-alpha: 100%;
--tw-inset-shadow: 0 0 #0000;
--tw-shadow-alpha: 100%;
--tw-shadow: 0 0 #0000;
```

### Radii

```css
--radius-xl: .75rem;
--radius-2xl: 1rem;
--radius-md: .375rem;
```

### Other

```css
--default-transition-timing-function: cubic-bezier(.4, 0, .2, 1);
--tw-outline-style: solid;
--lightningcss-dark: ;
--tw-gradient-via: rgba(0, 0, 0, 0);
--ease-out: cubic-bezier(0, 0, .2, 1);
--tw-divide-x-reverse: 0;
--tw-gradient-from: rgba(0, 0, 0, 0);
--ease-editorial: cubic-bezier(.22, 1, .36, 1);
--tw-gradient-to: rgba(0, 0, 0, 0);
--lightningcss-light: ;
--tw-divide-y-reverse: 0;
--tw-gradient-via-position: 50%;
--tw-gradient-to-position: 100%;
--default-transition-duration: .15s;
--tw-gradient-from-position: 0%;
--blur-sm: 8px;
```

### Semantic

```css
success: [object Object];
warning: [object Object];
error: [object Object];
info: [object Object];
```

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.15s`, `0.3s`

### Common Transitions

```css
transition: all;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.3s cubic-bezier(0.22, 1, 0.36, 1), background-color 0.3s cubic-bezier(0.22, 1, 0.36, 1), border-color 0.3s cubic-bezier(0.22, 1, 0.36, 1), outline-color 0.3s cubic-bezier(0.22, 1, 0.36, 1), text-decoration-color 0.3s cubic-bezier(0.22, 1, 0.36, 1), fill 0.3s cubic-bezier(0.22, 1, 0.36, 1), stroke 0.3s cubic-bezier(0.22, 1, 0.36, 1), --tw-gradient-from 0.3s cubic-bezier(0.22, 1, 0.36, 1), --tw-gradient-via 0.3s cubic-bezier(0.22, 1, 0.36, 1), --tw-gradient-to 0.3s cubic-bezier(0.22, 1, 0.36, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (1 instances)

```css
.button {
  color: rgb(233, 116, 81);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Links (32 instances)

```css
.link {
  color: oklab(0.977696 -0.00194579 0.0104345 / 0.8);
  font-size: 14px;
  font-weight: 400;
}
```

### Navigation (4 instances)

```css
.navigatio {
  background-color: oklab(0.293043 0.0266586 0.0268859 / 0.95);
  color: rgb(249, 248, 240);
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
  background-color: rgb(45, 15, 6);
  color: rgb(249, 248, 240);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

## Layout System

**7 grid containers** and **35 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1200px | 24px |
| 1400px | 40px |
| 471.552px | 0px |
| 544px | 0px |
| 786.24px | 0px |
| 640px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 3x |
| 3-column | 2x |
| 6-column | 1x |
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 418.656px 418.672px 418.656px;
gap: 48px 12px;
grid-template-columns: 560px 560px;
gap: 80px;
grid-template-columns: 480px 560px;
gap: 80px;
grid-template-columns: 662.656px 473.328px;
gap: 64px;
grid-template-columns: 214.391px 214.406px 214.391px 214.406px 214.391px;
gap: 48px 32px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 22x |
| column/nowrap | 13x |

**Gap values:** `12px`, `16px`, `24px`, `32px`, `40px`, `48px 12px`, `48px 32px`, `64px`, `80px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 94/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 100/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 5 !important rules — prefer specificity over overrides
- 337 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | to right | 3 | bold |

```css
background: linear-gradient(to right, oklab(0.214519 0.0414231 0.032529 / 0.95) 0%, oklab(0.214519 0.0414231 0.032529 / 0.6) 50%, rgba(0, 0, 0, 0) 100%);
```

## Z-Index Map

**2 unique z-index values** across 1 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | div.r.e.l.a.t.i.v.e. .z.-.1.0. .f.l.e.x. .w.-.f.u.l.l. .m.a.x.-.w.-.[.1.2.0.0.p.x.]. .f.l.e.x.-.c.o.l. .i.t.e.m.s.-.c.e.n.t.e.r. .p.x.-.6. .t.e.x.t.-.c.e.n.t.e.r, div.r.e.l.a.t.i.v.e. .z.-.1.0. .m.x.-.a.u.t.o. .w.-.f.u.l.l. .m.a.x.-.w.-.[.1.4.0.0.p.x.]. .p.x.-.6. .p.b.-.2.0. .m.d.:.p.x.-.1.0. .m.d.:.p.b.-.2.8, header.f.i.x.e.d. .i.n.s.e.t.-.x.-.0. .t.o.p.-.0. .z.-.5.0 |

## SVG Icons

**1 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| lg | 1 |

**Icon colors:** `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Mona Sans | self-hosted | 400, 500, 600 | normal |
| paradigm-pro | self-hosted | 300 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 8 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 2 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 1 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (6x), 5.24:1 (2x), 1:1 (2x), 2:3 (1x), 3:2 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `md` | `300ms` | 300 |

### Easing Families

- **custom** (25 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (3 uses) — `cubic-bezier(0.22, 1, 0.36, 1)`

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (balanced)

### Sample Headings

> WHERE YOUR BEST WORK HAPPENS
> When Your Space Works, So Do You.
> Apollo is built for
owners & operators
> Work is just one reason to be here
> A Place For Focus, With Room To Move.
> WHERE YOUR BEST WORK HAPPENS
> When Your Space Works, So Do You.
> Apollo is built for
owners & operators
> Work is just one reason to be here
> A Place For Focus, With Room To Move.

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Apollo is a workspace for people who want to work better — private offices, dedicated desks, and meeting rooms in a beautiful, human-scale building in Downtown Edmond, Oklahoma.

Alternates: legal (0.4)

## Section Roles

Reading order (top→bottom): nav → nav → testimonial → content → content → testimonial → pricing → content → pricing → content → footer → nav → nav → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | testimonial | WHERE YOUR BEST WORK HAPPENS | 0.8 |
| 3 | content | WHERE YOUR BEST WORK HAPPENS | 0.3 |
| 4 | content | — | 0.3 |
| 5 | testimonial | When Your Space Works, So Do You. | 0.8 |
| 6 | pricing | Apollo is built for
owners & operators | 0.4 |
| 7 | content | Work is just one reason to be here | 0.3 |
| 8 | pricing | A Place For Focus, With Room To Move. | 0.4 |
| 9 | content | Built for the human experience. | 0.3 |
| 10 | footer | — | 0.95 |
| 11 | nav | — | 0.9 |
| 12 | nav | — | 0.9 |
| 13 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.419 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.083)
**Counts:** total 12, svg 2, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** portrait
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.859)

Evidence:
- tailwind-like class density 82%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Mona Sans` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
