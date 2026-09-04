# Design Language: ALET | ALET Agency is a Copenhagen-based creative studio and production house with storytelling at our core.

> Extracted from `https://aletagency.com/` on September 4, 2026
> 465 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#dc3545` | rgb(220, 53, 69) | hsl(354, 70%, 54%) | 31 |
| Secondary | `#e5ddc4` | rgb(229, 221, 196) | hsl(45, 39%, 83%) | 2 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 867 |
| `#252525` | hsl(0, 0%, 15%) | 36 |
| `#101010` | hsl(0, 0%, 6%) | 16 |
| `#ffffff` | hsl(0, 0%, 100%) | 4 |
| `#454545` | hsl(0, 0%, 27%) | 2 |
| `#a2a093` | hsl(52, 7%, 61%) | 1 |
| `#bfb5ab` | hsl(30, 14%, 71%) | 1 |

### Background Colors

Used on large-area elements: `#e5ddc4`, `#a2a093`, `#dc3545`

### Text Colors

Text color palette: `#000000`, `#252525`, `#101010`, `#ffffff`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border | 867 |
| `#252525` | text, border, background | 36 |
| `#dc3545` | background | 31 |
| `#101010` | text, border | 16 |
| `#ffffff` | text, border | 4 |
| `#e5ddc4` | background | 2 |
| `#454545` | border, background | 2 |
| `#a2a093` | background | 1 |
| `#bfb5ab` | background | 1 |

## Typography

### Font Families

- **WorkSans-Regular** — used for body (460 elements)
- **SilkSerif-Light** — used for all (4 elements)
- **SilkSerif-LightItalic** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 36px | 2.25rem | 400 | 33.84px | 1.62px | p, br, em |
| 20.5632px | 1.2852rem | 400 | 19.3294px | normal | h1, br |
| 12px | 0.75rem | 400 | 13.2px | normal | div, small, span |
| 11.52px | 0.72rem | 400 | 12.672px | normal | span, a |
| 9.6px | 0.6rem | 400 | 11.04px | normal | html, head, meta, title |

### Heading Scale

```css
h1 { font-size: 20.5632px; font-weight: 400; line-height: 19.3294px; }
```

### Body Text

```css
body { font-size: 9.6px; font-weight: 400; line-height: 11.04px; }
```

### Font Weights in Use

`400` (465x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-59 | 59px | 3.6875rem |
| spacing-90 | 90px | 5.625rem |
| spacing-154 | 154px | 9.625rem |
| spacing-186 | 186px | 11.625rem |
| spacing-237 | 237px | 14.8125rem |
| spacing-294 | 294px | 18.375rem |
| spacing-320 | 320px | 20rem |
| spacing-352 | 352px | 22rem |
| spacing-435 | 435px | 27.1875rem |
| spacing-454 | 454px | 28.375rem |
| spacing-474 | 474px | 29.625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 10px | 1 |
| full | 9999px | 1 |

## Box Shadows

**sm** — blur: 3px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;
```

## CSS Custom Properties

### Colors

```css
--primary: #007bff;
--secondary: #6c757d;
```

### Spacing

```css
--font-family-monospace: SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
--font-size-xlg: 9.3312px;
--font-size-xl: 9.6px;
--font-size-sm: 14.4px;
--font-size: 36.48px;
```

### Typography

```css
--font-family-sans-serif: "WorkSans-Regular";
```

### Other

```css
--blue: #007bff;
--indigo: #6610f2;
--purple: #6f42c1;
--pink: #e83e8c;
--red: #dc3545;
--orange: #fd7e14;
--yellow: #ffc107;
--green: #28a745;
--teal: #20c997;
--cyan: #17a2b8;
--white: #fff;
--gray: #6c757d;
--gray-dark: #343a40;
--success: #28a745;
--info: #17a2b8;
--warning: #ffc107;
--danger: #dc3545;
--light: #f8f9fa;
--dark: #343a40;
--breakpoint-xs: 0;
--breakpoint-sm: 576px;
--breakpoint-md: 744px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1200px;
--breakpoint-xlg: 1500px;
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
| sm | 576px | min-width |
| md | 744px | min-width |
| md | 768px | min-width |
| 915px | 915px | max-width |
| lg | 992px | min-width |
| lg | 1024px | min-width |
| 1200px | 1200px | min-width |
| 1400px | 1400px | min-width |
| 2xl | 1500px | min-width |

## Transitions & Animations

**Durations:** `0.4s`, `0.3s`, `4s`, `2s`, `1s`, `0.2s`

### Common Transitions

```css
transition: all;
transition: 0.4s;
transition: color 0.4s;
transition: transform 0.3s;
transition: background-color 4s;
transition: color 2s;
transition: opacity 0.4s;
transition: opacity 1s;
transition: background-color 0.2s, width 0.2s, height 0.2s;
transition: margin 0.2s;
```

### Keyframe Animations

**progress-bar-stripes**
```css
@keyframes progress-bar-stripes {
  0% { background-position: 1rem 0px; }
  100% { background-position: 0px 0px; }
}
```

**spinner-border**
```css
@keyframes spinner-border {
  100% { transform: rotate(1turn); }
}
```

**spinner-grow**
```css
@keyframes spinner-grow {
  0% { transform: scale(0); }
  50% { opacity: 1; transform: none; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (1 instances)

```css
.button {
  color: rgb(37, 37, 37);
  font-size: 9.6px;
  font-weight: 400;
  padding-top: 1px;
  padding-right: 6px;
  border-radius: 0px;
}
```

### Links (5 instances)

```css
.link {
  color: rgb(37, 37, 37);
  font-size: 11.52px;
  font-weight: 400;
}
```

### Navigation (2 instances)

```css
.navigatio {
  color: rgb(37, 37, 37);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: fixed;
}
```

### Modals (1 instances)

```css
.modal {
  background-color: rgb(191, 181, 171);
  border-radius: 0px;
  padding-top: 9.6px;
  padding-right: 20.544px;
}
```

### Badges (2 instances)

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

### Switches (3 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
}
```

## Layout System

**0 grid containers** and **16 flex containers** detected.

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/wrap | 5x |
| row/nowrap | 8x |
| column/nowrap | 3x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 692 !important rules — prefer specificity over overrides
- 89% of CSS is unused — consider purging
- 1637 duplicate CSS declarations

## Z-Index Map

**20 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 10000,10000 | div.d.-.f.l.e.x. .p.o.s.i.t.i.o.n.-.f.i.x.e.d. .o.n.-.t.o.p.t.o.p. .c.e.n.t.e.r.-.x. .b.-.0. .m.b.-.4. .w.-.1.0.0. .j.u.s.t.i.f.y.-.c.o.n.t.e.n.t.-.c.e.n.t.e.r. .a.l.i.g.n.-.i.t.e.m.s.-.c.e.n.t.e.r. .l.h.-.1, div.d.-.f.l.e.x. .p.o.s.i.t.i.o.n.-.f.i.x.e.d. .o.n.-.t.o.p.t.o.p. .c.e.n.t.e.r.-.x. .b.-.0. .m.b.-.2. .a.l.i.g.n.-.i.t.e.m.s.-.c.e.n.t.e.r. .l.h.-.1 |
| dropdown | 100,100 | div.w.a.r.n.i.n.g.-.o.v.e.r.l.a.y. .f.l.e.x.-.c.o.l.u.m.n. .f.l.e.x.-.c.e.n.t.e.r. .p.y.-.1. .p.x.-.2 |
| sticky | 60,99 | div.o.u.t.e.r.-.w.r.a.p.p.e.r. .t.-.0. .w.-.1.0.0. .h.-.1.0.0. .p.e.r.s.p.e.c.t.i.v.e, div.o.u.t.e.r.-.w.r.a.p.p.e.r. .t.-.0. .w.-.1.0.0. .h.-.1.0.0. .p.e.r.s.p.e.c.t.i.v.e, div.o.u.t.e.r.-.w.r.a.p.p.e.r. .t.-.0. .w.-.1.0.0. .h.-.1.0.0. .p.e.r.s.p.e.c.t.i.v.e |
| base | -1,1 | div.c.a.t.e.g.o.r.y. .d.-.f.l.e.x. .f.l.e.x.-.c.o.l.u.m.n. .j.u.s.t.i.f.y.-.c.o.n.t.e.n.t.-.b.e.t.w.e.e.n. .t.o.p.-.i.t.e.m.s. .h.-.1.0.0. .w.-.1.0.0. .d.i.s.a.b.l.e.d. .b.e.h.i.n.d.-.1. .p.o.s.i.t.i.o.n.-.r.e.l.a.t.i.v.e, div.c.o.l.-.6. .d.-.f.l.e.x. .f.l.e.x.-.c.e.n.t.e.r. .e.n.a.b.l.e.d. .j.u.s.t.i.f.y.-.c.o.n.t.e.n.t.-.s.t.a.r.t. .j.u.s.t.i.f.y.-.c.o.n.t.e.n.t.-.x.l.-.c.e.n.t.e.r. .p.o.s.i.t.i.o.n.-.r.e.l.a.t.i.v.e. .z.-.1 |

**Issues:**
- [object Object]

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| SilkSerif-Italic | self-hosted | 400, normal | normal |
| SilkSerif-Light | self-hosted | 400, normal | normal |
| SilkSerif-Regular | self-hosted | 400, normal | normal |
| WorkSans-Regular | self-hosted | 400, normal | normal |
| SilkSerif-LightItalic | self-hosted | 400, normal | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 26 | objectFit: contain, borderRadius: 0px, shape: square |
| general | 12 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (28x), 2:3 (6x), 1:1 (3x), 4.7:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `xl` | `1s` | 1000 |
| `xxl` | `2s` | 2000 |

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Title Case (verbose)

### Sample Headings

> ALET Agency is a Copenhagen-based creative studio and production house
with storytelling at our core.

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** ALET Agency is a Copenhagen-based creative studio and production house with storytelling at our core.

## Section Roles

Reading order (top→bottom): nav → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | content | ALET Agency is a Copenhagen-based creative studio and production house
with stor | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.122 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.184)
**Counts:** total 38, svg 1, icon 5, screenshot-like 0, photo-like 14
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `WorkSans-Regular` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
