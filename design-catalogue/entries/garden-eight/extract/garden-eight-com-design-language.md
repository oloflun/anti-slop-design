# Design Language: Garden Eight

> Extracted from `https://garden-eight.com/` on September 4, 2026
> 406 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#dbd6d0` | hsl(33, 13%, 84%) | 433 |
| `#1e1f1f` | hsl(180, 2%, 12%) | 406 |

### Background Colors

Used on large-area elements: `#1e1f1f`

### Text Colors

Text color palette: `#dbd6d0`, `#1e1f1f`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#dbd6d0` | text, border, background | 433 |
| `#1e1f1f` | background, text, border | 406 |

## Typography

### Font Families

- **lausanne** — used for all (302 elements)
- **gunsan** — used for body (104 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 191.104px | 11.944rem | 300 | 271.368px | normal | div, svg, use |
| 14.85px | 0.9281rem | 300 | 21.087px | normal | main, div, article, a |
| 13.05px | 0.8156rem | 300 | 18.531px | normal | html, head, meta, title |
| 11.7px | 0.7312rem | 200 | 18.72px | normal | div, a, svg, title |
| 0px | 0rem | 600 | 0px | normal | div |

### Heading Scale

```css
h1 { font-size: 13.05px; font-weight: 300; line-height: 18.531px; }
```

### Body Text

```css
body { font-size: 13.05px; font-weight: 300; line-height: 18.531px; }
```

### Font Weights in Use

`300` (197x), `600` (104x), `200` (102x), `400` (3x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-23 | 23px | 1.4375rem |
| spacing-40 | 40px | 2.5rem |
| spacing-46 | 46px | 2.875rem |
| spacing-53 | 53px | 3.3125rem |
| spacing-76 | 76px | 4.75rem |
| spacing-140 | 140px | 8.75rem |
| spacing-160 | 160px | 10rem |
| spacing-185 | 185px | 11.5625rem |
| spacing-248 | 248px | 15.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| full | 56px | 1 |
| full | 80px | 1 |
| full | 100px | 4 |
| full | 191px | 16 |
| full | 1280px | 1 |

## Box Shadows

**sm (inset)** — blur: 2px
```css
box-shadow: rgb(30, 31, 31) 0px 2px 2px 0px inset, rgb(219, 214, 208) 0px 3px 2px 0px inset, rgb(219, 214, 208) 0px 3px 3px 0px inset;
```

## CSS Custom Properties

### Other

```css
--vh: 1vh;
--col-black: #1e1f1f;
--col-black2: #1c1d1d;
--col-black3: #141414;
--col-gray: #3c3c3c;
--col-white: #dbd6d0;
--col-orange: #dc5648;
--tt-h: 2.5em;
--tt-blur: 9px;
--tt-r: 1.25em;
--form-footer-h: 5em;
--form-h: calc(2.7em + var(--form-footer-h));
--form-w: 40%;
--input-min-h: 2.715rem;
--input-max-h: 10rem;
```

### Dependencies

```css
--form-h: --form-footer-h;
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
| xs | 321px | min-width |
| xs | 370px | max-width |
| sm | 640px | max-width |
| 844px | 844px | max-width |
| 1180px | 1180px | max-width |
| xl | 1280px | max-width |
| 1366px | 1366px | max-width |
| 1680px | 1680px | min-width |
| 1920px | 1920px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.3s`, `0s`, `0.05s`, `0.1s`, `0.15s`, `0.2s`, `0.25s`, `0.6s`, `1.4s`, `0.7s`

### Common Transitions

```css
transition: all;
transition: transform 0.3s cubic-bezier(0.32, 0.94, 0.6, 1);
transition: 0s 0.05s;
transition: 0s 0.1s;
transition: 0s 0.15s;
transition: 0s 0.2s;
transition: 0s 0.25s;
transition: opacity 0.6s cubic-bezier(0.32, 0.94, 0.6, 1);
transition: color 0.3s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.3s cubic-bezier(0.32, 0.94, 0.6, 1);
transition: opacity 1.4s, transform 1.4s;
```

### Keyframe Animations

**hover**
```css
@keyframes hover {
  0% { transform: translate(0px); }
  50% { transform: translate(110%); }
  51% { transform: translate(-110%); }
  100% { transform: translate(0px); }
}
```

**rotate**
```css
@keyframes rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (2 instances)

```css
.button {
  color: rgb(219, 214, 208);
  font-size: 11.7px;
  font-weight: 200;
  padding-top: 1px;
  padding-right: 11.7px;
  border-radius: 1280px;
}
```

### Cards (8 instances)

```css
.card {
  background-color: rgba(220, 215, 209, 0.2);
  border-radius: 191.104px;
  box-shadow: rgb(30, 31, 31) 0px 2px 2px 0px inset, rgb(219, 214, 208) 0px 3px 2px 0px inset, rgb(219, 214, 208) 0px 3px 3px 0px inset;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (24 instances)

```css
.link {
  color: rgb(219, 214, 208);
  font-size: 13.05px;
  font-weight: 300;
}
```

### Navigation (8 instances)

```css
.navigatio {
  color: rgb(30, 31, 31);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (4 instances)

```css
.foote {
  color: rgb(30, 31, 31);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 14.85px;
}
```

### Dropdowns (1 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(219, 214, 208);
  padding-top: 0px;
}
```

### Badges (2 instances)

```css
.badge {
  color: rgb(219, 214, 208);
  font-size: 11.7px;
  font-weight: 200;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### ProgressBars (2 instances)

```css
.progressBar {
  color: rgb(30, 31, 31);
  border-radius: 0px;
  font-size: 13.05px;
}
```

## Layout System

**0 grid containers** and **55 flex containers** detected.

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 52x |
| row/wrap | 2x |
| column/nowrap | 1x |

**Gap values:** `23.4px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 87/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 85/100 |
| Typography Consistency | 90/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- No clear primary brand color detected
- 67 !important rules — prefer specificity over overrides
- 84% of CSS is unused — consider purging
- 1784 duplicate CSS declarations

## Z-Index Map

**7 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 101,999 | a.u.i.-.n.a.m.e. .u.i.-.f.i.x.e.d. .c.l.i.p.-.y. .j.s.-.h.d, div.a.l.e.r.t. .a.l.e.r.t.-.b.r.o.w.s |
| sticky | 10,10 | div.b. .j.s.-.c, div.b. .j.s.-.c, div.b. .j.s.-.c |
| base | 1,6 | div.j.s.-.h. .s.-.w.r.a.p.p.e.r. .i.s.-.c.h.a.t.-.l.o.a.d.e.d. .i.s.-.f.a.q.-.l.o.a.d.e.d, div.o, div.t. .j.s.-.s |

## SVG Icons

**1 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xl | 1 |

**Icon colors:** `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| gunsan | self-hosted | 600 | normal |
| lausanne | self-hosted | 200, 300, 400 | normal |

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `50ms` | 50 |
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `600ms` | 600 |
| `xxl` | `1.4s` | 1400 |

### Easing Families

- **ease-out** (37 uses) — `cubic-bezier(0.32, 0.94, 0.6, 1)`

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Title Case (tight)

### Sample Headings

> GARDEN
ZERO

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Garden Eight is a digital design studio based in Tokyo.

## Section Roles

Reading order (top→bottom): nav → nav → faq

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | GARDEN
ZERO | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | faq | — | 0.85 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.041 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 1280px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `lausanne` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
