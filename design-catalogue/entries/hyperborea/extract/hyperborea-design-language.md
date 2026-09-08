# Design Language: Hyperborea Summit MMXXVI — Lund

> Extracted from `http://127.0.0.1:3055/sites/hyperborea.html` on September 8, 2026
> 389 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ff5c0b` | rgb(255, 92, 11) | hsl(20, 100%, 52%) | 37 |
| Secondary | `#730405` | rgb(115, 4, 5) | hsl(359, 93%, 23%) | 1 |
| Accent | `#e3d2b8` | rgb(227, 210, 184) | hsl(36, 43%, 81%) | 354 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 389 |
| `#000102` | hsl(210, 100%, 0%) | 8 |

### Background Colors

Used on large-area elements: `#000102`, `#010205`

### Text Colors

Text color palette: `#e3d2b8`, `#000102`, `#ff5c0b`, `#730405`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 389 |
| `#e3d2b8` | text, background | 354 |
| `#ff5c0b` | background, text | 37 |
| `#000102` | background, text | 8 |
| `#730405` | text | 1 |

## Typography

### Font Families

- **Archivo** — used for body (292 elements)
- **Italiana** — used for all (80 elements)
- **Noto Serif JP** — used for body (5 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 140.8px | 8.8rem | 400 | 129.536px | -0.704px | h1, span |
| 89.6px | 5.6rem | 400 | 85.12px | -0.448px | h2, br, span |
| 69.12px | 4.32rem | 400 | 69.12px | -0.3456px | h2, span, br |
| 64px | 4rem | 400 | 58.88px | -0.704px | span, h2 |
| 60px | 3.75rem | 400 | 60px | -0.3px | div |
| 58.88px | 3.68rem | 400 | 58.88px | -0.2944px | h2, br, span |
| 48px | 3rem | 400 | 48px | -0.24px | div |
| 30px | 1.875rem | 400 | 37.5px | -0.15px | p, br, span, div |
| 24px | 1.5rem | 400 | 32px | -0.12px | span, h3 |
| 19px | 1.1875rem | 400 | 29.45px | normal | p |
| 18px | 1.125rem | 400 | 28px | normal | p |
| 17px | 1.0625rem | 400 | 28.05px | normal | p, a |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |
| 15px | 0.9375rem | 400 | 24.375px | normal | p |
| 14px | 0.875rem | 400 | 20px | normal | ul, li, span, p |

### Heading Scale

```css
h1 { font-size: 140.8px; font-weight: 400; line-height: 129.536px; }
h2 { font-size: 89.6px; font-weight: 400; line-height: 85.12px; }
h2 { font-size: 69.12px; font-weight: 400; line-height: 69.12px; }
h2 { font-size: 64px; font-weight: 400; line-height: 58.88px; }
h2 { font-size: 58.88px; font-weight: 400; line-height: 58.88px; }
h3 { font-size: 30px; font-weight: 400; line-height: 37.5px; }
h3 { font-size: 24px; font-weight: 400; line-height: 32px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 400; line-height: 20px; }
```

### Font Weights in Use

`400` (389x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-112 | 112px | 7rem |
| spacing-176 | 176px | 11rem |

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-offset-width: 0px;
--tw-ring-inset: ;
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

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.15s`, `0.5s`, `1.4s`, `1.2s`

### Common Transitions

```css
transition: all;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.5s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), fill 0.5s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.5s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 1.4s cubic-bezier(0.16, 1, 0.3, 1), transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

### Keyframe Animations

**m**
```css
@keyframes m {
  0% { transform: translateX(0px); }
  100% { transform: translateX(-50%); }
}
```

**rise**
```css
@keyframes rise {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Cards (8 instances)

```css
.card {
  border-radius: 0px;
  padding-top: 24px;
  padding-right: 0px;
}
```

### Links (9 instances)

```css
.link {
  color: oklch(0.94 0.02 80);
  font-size: 10.5px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: oklch(0.94 0.02 80);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Card — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: oklch(0.94 0.02 80);
  padding: 24px 0px 0px 0px;
  border-radius: 0px;
  border: 1px 0px 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**14 grid containers** and **25 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1480px | 32px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 13x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 286px 286px 286px 286px;
gap: 48px 24px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 56px 32px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 23x |
| row/wrap | 1x |
| column/nowrap | 1x |

**Gap values:** `12px`, `16px`, `20px`, `32px`, `36px`, `48px 24px`, `56px 32px`, `80px`, `normal 24px`, `normal 32px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 2 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#000102` | `#ff5c0b` | 6.75:1 | AA |

## Design System Score

**Overall: 91/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 99% of CSS is unused — consider purging
- 1300 duplicate CSS declarations

## Z-Index Map

**1 unique z-index values** across 1 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 40,40 | header.b.o.r.d.e.r.-.b. .b.o.r.d.e.r.-.b.o.n.e./.1.5. .s.t.i.c.k.y. .t.o.p.-.0. .z.-.4.0. .b.g.-.i.n.k./.8.5. .b.a.c.k.d.r.o.p.-.b.l.u.r.-.m.d |

## SVG Icons

**1 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| lg | 1 |

**Icon colors:** `oklch(0.79 0.158 64)`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Archivo | google-fonts | 400, 500, 600 | normal |
| Italiana | google-fonts | 400 | normal |
| Noto Serif JP | google-fonts | 400, 700 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `lg` | `500ms` | 500 |
| `xl` | `1.2s` | 1200 |
| `xxl` | `1.4s` | 1400 |

### Easing Families

- **custom** (8 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (62 uses) — `cubic-bezier(0.16, 1, 0.3, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `m` | slide-x | transform | 1 |
| `rise` | slide-y | transform | 2 |

## Component Anatomy

### card — 8 instances

**Slots:** heading, description, media, footer

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (tight)

### Sample Headings

> Systems
with warmth.
温度のある機械
> Three days. One question.
> Drawing the future
> Creating together
> A long, slow walk back
> Eight of forty,
on the wall.
> Kenji Watanabe
> Astrid Vinge
> Margot Lindqvist
> Ravi Auböck

## Page Intent

**Type:** `blog-post` (confidence 0.23)

Alternates: docs (0.3)

## Section Roles

Reading order (top→bottom): nav → nav → content → content → testimonial → testimonial → content → feature-grid → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | content | Systems
with warmth.
温度のある機械 | 0.3 |
| 3 | content | — | 0.3 |
| 4 | testimonial | Three days. One question. | 0.8 |
| 5 | testimonial | Eight of forty,
on the wall. | 0.8 |
| 6 | content | Sundial,
for forty
conversations. | 0.3 |
| 7 | feature-grid | Attend | 0.8 |
| 8 | content | Write us
a letter,
not a form. | 0.3 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.627 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Component Library

**Detected:** `tailwindcss` (confidence 0.733)

Evidence:
- tailwind-like class density 71%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Archivo` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
