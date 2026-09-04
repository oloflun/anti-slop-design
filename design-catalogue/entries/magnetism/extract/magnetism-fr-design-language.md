# Design Language: Magnetism | Creative Agency

> Extracted from `https://magnetism.fr` on September 4, 2026
> 544 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 538 |
| `#222222` | hsl(0, 0%, 13%) | 390 |
| `#000000` | hsl(0, 0%, 0%) | 77 |
| `#343434` | hsl(0, 0%, 20%) | 34 |
| `#aaaaaa` | hsl(0, 0%, 67%) | 31 |
| `#dbdbdb` | hsl(0, 0%, 86%) | 18 |
| `#cccccc` | hsl(0, 0%, 80%) | 11 |

### Background Colors

Used on large-area elements: `#343434`, `#ececec`

### Text Colors

Text color palette: `#000000`, `#222222`, `#aaaaaa`, `#353535`, `#ececec`, `#343434`, `#dbdbdb`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border, background, text | 538 |
| `#222222` | text, border | 390 |
| `#000000` | text | 77 |
| `#343434` | background, text | 34 |
| `#aaaaaa` | text | 31 |
| `#dbdbdb` | text | 18 |
| `#cccccc` | border, background | 11 |

## Typography

### Font Families

- **TT Hoves Pro Trial** — used for all (458 elements)
- **NeueMontreal** — used for body (5 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 24px | 1.5rem | 400 | 24px | 5.28px | li, span, a |
| 21.3334px | 1.3333rem | 400 | 32.0001px | normal | section, div, p, br |
| 17.7778px | 1.1111rem | 400 | 26.6667px | 1.77778px | h2 |
| 14.2222px | 0.8889rem | 400 | 21.3333px | normal | html, head, meta, title |
| 12.4444px | 0.7778rem | 300 | 18.6666px | normal | div, p |
| 9.77779px | 0.6111rem | 400 | 14.6667px | normal | div |
| 8.88889px | 0.5556rem | 400 | 13.3333px | 1.95556px | div, span, a |
| 8.88883px | 0.5556rem | 400 | 8.88883px | 1.95554px | button, span, svg, use |
| 7.11117px | 0.4444rem | 400 | 10.6668px | 1.56446px | div, p |
| 6px | 0.375rem | 300 | 9px | 1.32px | tspan |

### Heading Scale

```css
h2 { font-size: 17.7778px; font-weight: 400; line-height: 26.6667px; }
h1 { font-size: 14.2222px; font-weight: 400; line-height: 21.3333px; }
h3 { font-size: 8.88883px; font-weight: 400; line-height: 8.88883px; }
```

### Body Text

```css
body { font-size: 8.88883px; font-weight: 400; line-height: 8.88883px; }
```

### Font Weights in Use

`400` (503x), `500` (31x), `300` (6x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-43 | 43px | 2.6875rem |
| spacing-50 | 50px | 3.125rem |
| spacing-57 | 57px | 3.5625rem |
| spacing-71 | 71px | 4.4375rem |
| spacing-89 | 89px | 5.5625rem |
| spacing-114 | 114px | 7.125rem |
| spacing-124 | 124px | 7.75rem |
| spacing-136 | 136px | 8.5rem |
| spacing-160 | 160px | 10rem |
| spacing-382 | 382px | 23.875rem |

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--accent-color: #ececec;
--tw-ring-inset: ;
--tw-border-spacing-x: 0;
--accent-border-color: #ececec;
--tw-ring-color: rgba(59,130,246,.5);
--accent-bg-color: #ececec;
--tw-ring-offset-color: #fff;
--accent-border-hover-color: #ccc;
--tw-ring-offset-width: 0px;
--accent-hover-color: #ececec;
--text-color: #222;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--bg-color: #ececec;
--accent-bg-hover-color: #ccc;
```

### Spacing

```css
--column-spacing: 1.5rem;
--layout-columns-gap: 3.0769230769vw;
--layout-margin: 8.2051282051vw;
--margin-reset-container: -1rem;
--tw-numeric-spacing: ;
```

### Shadows

```css
--tw-drop-shadow: ;
--tw-shadow: 0 0 #0000;
```

### Other

```css
--ease-in-quad: cubic-bezier(0.55,0.085,0.68,0.53);
--ease-in-cubic: cubic-bezier(0.55,0.055,0.675,0.19);
--ease-in-quart: cubic-bezier(0.895,0.03,0.685,0.22);
--ease-in-quint: cubic-bezier(0.755,0.05,0.855,0.06);
--ease-in-expo: cubic-bezier(0.95,0.05,0.795,0.035);
--ease-in-circ: cubic-bezier(0.6,0.04,0.98,0.335);
--ease-out-quad: cubic-bezier(0.25,0.46,0.45,0.94);
--ease-out-cubic: cubic-bezier(0.215,0.61,0.355,1);
--ease-out-quart: cubic-bezier(0.165,0.84,0.44,1);
--ease-out-quint: cubic-bezier(0.23,1,0.32,1);
--ease-out-expo: cubic-bezier(0.19,1,0.22,1);
--ease-out-circ: cubic-bezier(0.075,0.82,0.165,1);
--ease-in-out-quad: cubic-bezier(0.455,0.03,0.515,0.955);
--ease-in-out-cubic: cubic-bezier(0.645,0.045,0.355,1);
--ease-in-out-quart: cubic-bezier(0.77,0,0.175,1);
--ease-in-out-quint: cubic-bezier(0.86,0,0.07,1);
--ease-in-out-expo: cubic-bezier(1,0,0,1);
--ease-in-out-circ: cubic-bezier(0.785,0.135,0.15,0.86);
--vh: 1vh;
--layout-columns-count: 6;
--container-width: 100vw;
--layout-width: calc(var(--container-width) - var(--layout-margin)*2);
--layout-column-width: calc((var(--layout-width) - ((var(--layout-columns-count) - 1)*var(--layout-columns-gap)))/var(--layout-columns-count));
--tw-backdrop-sepia: ;
--transition-easing: cubic-bezier(0.38,0.005,0.215,1);
--tw-sepia: ;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-backdrop-invert: ;
--tw-brightness: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-backdrop-brightness: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-rotate: 0;
--transition-translate: 2rem;
--tw-contrast: ;
--transition-delay: 0s;
--tw-skew-x: 0;
--tw-backdrop-blur: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-numeric-fraction: ;
--transition-duration: .8s;
--tw-skew-y: 0;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--transition-stagger-delay: 0.1s;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-pinch-zoom: ;
```

### Dependencies

```css
--layout-width: --container-width,--layout-margin;
--layout-column-width: --layout-width,--layout-columns-count,--layout-columns-gap,--layout-columns-count;
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
| sm | 460px | min-width |
| sm | 640px | min-width |
| md | 767px | max-width |
| md | 768px | max-width |
| lg | 1024px | min-width |
| 1200px | 1200px | min-width |
| 2400px | 2400px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.8s`, `0.3s`, `0.4s`, `0.2s`, `0.6s`, `1s`, `0.5s`

### Common Transitions

```css
transition: all;
transition: clip-path 0.8s ease-in-out, -webkit-clip-path 0.8s ease-in-out;
transition: opacity 0.3s linear;
transition: clip-path 0.4s cubic-bezier(0.55, 0.055, 0.675, 0.19), -webkit-clip-path 0.4s cubic-bezier(0.55, 0.055, 0.675, 0.19);
transition: opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.6s linear;
transition: transform 0.4s cubic-bezier(0.55, 0.055, 0.675, 0.19);
transition: transform 1s cubic-bezier(0.19, 1, 0.22, 1);
transition: opacity 0.6s cubic-bezier(0.645, 0.045, 0.355, 1);
transition: opacity 0.5s cubic-bezier(0.19, 1, 0.22, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (4 instances)

```css
.button {
  color: rgb(170, 170, 170);
  font-size: 8.88883px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 10.4889px;
  border-radius: 0px;
}
```

### Links (47 instances)

```css
.link {
  color: rgb(34, 34, 34);
  font-size: 8.88883px;
  font-weight: 400;
}
```

### Navigation (50 instances)

```css
.navigatio {
  background-color: rgb(236, 236, 236);
  color: rgb(34, 34, 34);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (8 instances)

```css
.foote {
  background-color: rgb(236, 236, 236);
  color: rgb(34, 34, 34);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 14.2222px;
}
```

### ProgressBars (6 instances)

```css
.progressBar {
  background-color: rgb(52, 52, 52);
  color: rgb(34, 34, 34);
  border-radius: 0px;
  font-size: 8.88883px;
}
```

### Switches (2 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(229, 231, 235);
}
```

## Layout System

**1 grid containers** and **52 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 2400px | 0px |
| 1166.22px | 0px |
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 640px 640px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 4x |
| row/nowrap | 48x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 88/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 85/100 |
| Typography Consistency | 92/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- No clear primary brand color detected
- 6 !important rules — prefer specificity over overrides
- 57% of CSS is unused — consider purging
- 980 duplicate CSS declarations

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 999,999 | div.c.-.c.u.r.s.o.r |
| sticky | 10,91 | section.c.-.h.o.m.e.-.p.r.o.j.e.c.t.s, a.c.-.h.o.m.e.-.p.r.o.j.e.c.t.s.-.i.t.e.m._.l.i.n.k, a.c.-.h.o.m.e.-.p.r.o.j.e.c.t.s.-.i.t.e.m._.l.i.n.k |
| base | 0,0 | svg.c.-.h.o.m.e.-.i.n.t.r.o._.s.h.a.p.e.s |

## SVG Icons

**4 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| md | 1 |
| xl | 3 |

**Icon colors:** `rgb(0, 0, 0)`, `#222222`, `#FF0027`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Anton | google-fonts | 400 | normal |
| Fira Sans | google-fonts | 300, 400 | normal |
| Reenie Beanie | google-fonts | 400 | normal |
| TT Hoves Pro Trial | self-hosted | 300, 400, 500 | normal |
| NeueMontreal | self-hosted | 400, 700 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 16 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 6 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 3 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (13x), 3:4 (6x), 21:9 (4x), 0.33:1 (2x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `800ms` | 800 |

### Easing Families

- **ease-in-out** (8 uses) — `ease`
- **linear** (14 uses) — `linear`
- **ease-in** (3 uses) — `cubic-bezier(0.55, 0.055, 0.675, 0.19)`
- **custom** (11 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`, `cubic-bezier(0.645, 0.045, 0.355, 1)`
- **ease-out** (17 uses) — `cubic-bezier(0.19, 1, 0.22, 1)`

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Title Case (tight)

### Sample Headings

> Magnetism
> CAMPAIGN - RICHARD MILLE
> CAMPAIGN - LOUIS VUITTON
> CAMPAIGN - HENNESSY PARADIS
> CAMPAIGN - RICHARD MILLE
> CAMPAIGN - EVIDENS DE BEAUTÉ
> CAMPAIGN - RICHARD MILLE
> CAMPAIGN - LOUIS VUITTON
> CAMPAIGN - HENNESSY PARADIS
> CAMPAIGN - RICHARD MILLE

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Magnetism - Creative agency, based in Paris, supports brands to make them attractive: strategy, design, advertising and digital.

## Section Roles

Reading order (top→bottom): nav → nav → nav → nav → nav → content → content → content → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | Magnetism | 0.4 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | content | CAMPAIGN - RICHARD MILLE | 0.3 |
| 5 | content | — | 0.3 |
| 6 | content | CAMPAIGN - RICHARD MILLE | 0.3 |
| 7 | content | — | 0.3 |
| 8 | content | MORE PROJECTS | 0.3 |
| 9 | footer | — | 0.95 |
| 10 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.004 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.46)
**Counts:** total 25, svg 1, icon 1, screenshot-like 0, photo-like 21
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `TT Hoves Pro Trial` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
