# Design Language: Dovetail

> Extracted from `https://dovetail.no/` on September 4, 2026
> 255 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f9e5b1` | rgb(249, 229, 177) | hsl(43, 86%, 84%) | 5 |
| Secondary | `#ede5dc` | rgb(237, 229, 220) | hsl(32, 32%, 90%) | 5 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 241 |
| `#1d1e21` | hsl(225, 6%, 12%) | 172 |
| `#000000` | hsl(0, 0%, 0%) | 58 |
| `#fef9f3` | hsl(33, 85%, 97%) | 28 |

### Background Colors

Used on large-area elements: `#f9e5b1`, `#dfe4f3`, `#1d1e21`

### Text Colors

Text color palette: `#000000`, `#1d1e21`, `#fef9f3`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border, background | 241 |
| `#1d1e21` | text, background, border | 172 |
| `#000000` | text | 58 |
| `#fef9f3` | text | 28 |
| `#f9e5b1` | background | 5 |
| `#ede5dc` | background | 5 |

## Typography

### Font Families

- **Lausanne** — used for all (255 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 72px | 4.5rem | 400 | 72px | -0.72px | p |
| 48px | 3rem | 400 | 56.16px | -0.24px | p, ul, li, span |
| 32px | 2rem | 400 | 48px | -0.16px | p, br, a, figcaption |
| 28px | 1.75rem | 600 | 28px | 0.2px | a |
| 22px | 1.375rem | 700 | 29.92px | 0.11008px | h2, p, a, span |
| 20px | 1.25rem | 400 | 28px | 0.2px | body, div, main, header |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, link |

### Heading Scale

```css
h2 { font-size: 22px; font-weight: 700; line-height: 29.92px; }
h1 { font-size: 20px; font-weight: 400; line-height: 28px; }
```

### Body Text

```css
body { font-size: 48px; font-weight: 400; line-height: 56.16px; }
```

### Font Weights in Use

`400` (225x), `700` (19x), `600` (11x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-3 | 3px | 0.1875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-56 | 56px | 3.5rem |
| spacing-65 | 65px | 4.0625rem |
| spacing-72 | 72px | 4.5rem |
| spacing-80 | 80px | 5rem |
| spacing-90 | 90px | 5.625rem |
| spacing-112 | 112px | 7rem |
| spacing-127 | 127px | 7.9375rem |
| spacing-160 | 160px | 10rem |
| spacing-310 | 310px | 19.375rem |
| spacing-374 | 374px | 23.375rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| lg | 16px | 11 |
| xl | 24px | 2 |
| full | 91px | 5 |
| full | 9999px | 2 |

## CSS Custom Properties

### Colors

```css
--bg: #fef9f3;
--accent-default: #f9e5b1;
--accent-blue: #b0c5f3;
--accent-red: #f8b7aa;
--bg-accent: #F9E5B1;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-offset-width: 0px;
--tw-ring-inset: ;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: #3b82f680;
--tw-ring-offset-color: #fff;
```

### Spacing

```css
--gap: 1.5rem;
--scroll-margin-top: 94px;
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
--gutter: 1rem;
--footerHeight: 374px;
--tw-contrast: ;
--tw-backdrop-sepia: ;
--tw-numeric-figure: ;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-contain-style: ;
--tw-backdrop-blur: ;
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
| sm | 520px | min-width |
| sm | 640px | min-width |
| md | 768px | min-width |
| lg | 1024px | min-width |
| xl | 1280px | min-width |
| 2xl | 1536px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.2s`, `0.15s`

### Common Transitions

```css
transition: 0.2s ease-in;
transition: all;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (3 instances)

```css
.button {
  color: rgb(29, 30, 33);
  font-size: 20px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 9999px;
}
```

### Links (23 instances)

```css
.link {
  color: rgb(29, 30, 33);
  font-size: 20px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: rgb(29, 30, 33);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: absolute;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(254, 249, 243);
  padding-top: 28px;
  padding-bottom: 28px;
  font-size: 20px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(29, 30, 33);
  padding: 0px 0px 0px 0px;
  border-radius: 9999px;
  border: 1px solid rgb(29, 30, 33);
  font-size: 20px;
  font-weight: 400;
```

## Layout System

**7 grid containers** and **16 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1440px | 32px |
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 7x |

### Grid Templates

```css
grid-template-columns: 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3438px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3438px;
gap: 0px 24px;
grid-template-columns: 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px;
gap: 0px 24px;
grid-template-columns: 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px;
gap: 0px 24px;
grid-template-columns: 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px;
gap: 0px 24px;
grid-template-columns: 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3438px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px 79.3281px;
gap: 0px 24px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 11x |
| column/nowrap | 5x |

**Gap values:** `0px 24px`, `24px`, `32px`, `4px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 3 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#fef9f3` | `#1d1e21` | 15.92:1 | AAA |

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
- 174 duplicate CSS declarations

## Z-Index Map

**3 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | header.f.i.x.e.d. .t.o.p.-.0. .l.e.f.t.-.0. .r.i.g.h.t.-.0. .z.-.1.0. .b.g.-.a.c.c.e.n.t, p.t.e.x.t.-.b.a.s.e. .l.e.a.d.i.n.g.-.5. .s.m.:.t.e.x.t.-.m.d. .f.o.n.t.-.b.o.l.d. .s.m.:.c.o.l.-.s.t.a.r.t.-.1. .s.m.:.c.o.l.-.s.p.a.n.-.6. .s.m.:.r.o.w.-.s.t.a.r.t.-.2. .z.-.1.0, div.r.e.l.a.t.i.v.e. .c.o.n.t.e.n.t. .z.-.5.0 |
| base | -10,-10 | div.j.s.x.-.1.1.6.5.2.4.7.2.4.7. .f.i.x.e.d. .w.-.f.u.l.l. .b.o.t.t.o.m.-.0. .-.z.-.1.0. .b.g.-.b.l.a.c.k. .t.e.x.t.-.w.h.i.t.e |

## SVG Icons

**4 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| md | 1 |
| lg | 1 |
| xl | 2 |

**Icon colors:** `currentColor`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Lausanne | self-hosted | 300, 600 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 10 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 16:9 (5x), 4:3 (2x), 3:2 (2x), 1:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `sm` | `200ms` | 200 |

### Easing Families

- **ease-in-out** (1 uses) — `ease`
- **custom** (10 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`

## Component Anatomy

### button — 2 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **previous** (1)
- **next** (1)

### Button Copy Patterns

- "previous slide" (1×)
- "next slide" (1×)

### Sample Headings

> Dovetail
> About us
> Our portfolio
> Our investment focus
> Our team
> Dovetail
> About us
> Our portfolio
> Our investment focus
> Our team

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** We invest in tech-enabled companies, and place them on the path to sustainable success

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): content → nav → nav → footer → content → cta → content → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | content | Dovetail | 0.3 |
| 1 | nav | Dovetail | 0.4 |
| 2 | nav | — | 0.9 |
| 3 | content | About us | 0.3 |
| 4 | cta | Our portfolio | 0.75 |
| 5 | content | Our investment focus | 0.3 |
| 6 | content | Our team | 0.3 |
| 7 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.092 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 10, svg 0, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** landscape
**Radius profile on images:** soft

## Component Library

**Detected:** `tailwindcss` (confidence 0.766)

Evidence:
- tailwind-like class density 74%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Lausanne` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
