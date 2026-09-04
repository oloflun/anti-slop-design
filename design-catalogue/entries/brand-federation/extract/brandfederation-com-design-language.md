# Design Language: Brand Federation: Strategic Consultancy for Brands

> Extracted from `https://www.brandfederation.com/` on September 4, 2026
> 823 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f56b20` | rgb(245, 107, 32) | hsl(21, 91%, 54%) | 445 |
| Secondary | `#12273e` | rgb(18, 39, 62) | hsl(211, 55%, 16%) | 187 |
| Accent | `#083a74` | rgb(8, 58, 116) | hsl(212, 87%, 24%) | 24 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#333333` | hsl(0, 0%, 20%) | 770 |
| `#ffffff` | hsl(0, 0%, 100%) | 132 |
| `#000000` | hsl(0, 0%, 0%) | 66 |
| `#edecee` | hsl(270, 6%, 93%) | 51 |
| `#222222` | hsl(0, 0%, 13%) | 36 |
| `#a397af` | hsl(270, 13%, 64%) | 12 |
| `#717d8b` | hsl(212, 10%, 49%) | 10 |
| `#dddddd` | hsl(0, 0%, 87%) | 2 |

### Background Colors

Used on large-area elements: `#ffffff`, `#edecee`, `#12273e`, `#f56b20`

### Text Colors

Text color palette: `#000000`, `#333333`, `#f56b20`, `#ffffff`, `#edecee`, `#222222`, `#12273e`, `#717d8b`, `#a397af`, `#083a74`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#333333` | text, border | 770 |
| `#f56b20` | background, text, border | 445 |
| `#12273e` | background, text, border | 187 |
| `#ffffff` | background, text, border | 132 |
| `#000000` | text, border | 66 |
| `#edecee` | text, border, background | 51 |
| `#222222` | text, border | 36 |
| `#083a74` | text, border | 24 |
| `#a397af` | text, border | 12 |
| `#717d8b` | text, border | 10 |
| `#dddddd` | background | 2 |

## Typography

### Font Families

- **Arial** — used for body (594 elements)
- **Inter** — used for body (139 elements)
- **Manrope** — used for all (55 elements)
- **webflow-icons** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 67.0476px | 4.1905rem | 400 | 80.4571px | normal | a, h1 |
| 36.5714px | 2.2857rem | 400 | 43.8857px | normal | div, br |
| 30.4762px | 1.9048rem | 400 | 39.619px | normal | h4, h3 |
| 24.381px | 1.5238rem | 400 | 34.1333px | normal | h5, br, p |
| 21.3333px | 1.3333rem | 400 | 27.7333px | normal | div |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 15.4286px | 0.9643rem | 400 | 19.2857px | -0.26px | div |
| 13.7143px | 0.8571rem | 400 | 17.1429px | -0.26px | div, a, img, br |
| 12.1905px | 0.7619rem | 400 | 20px | normal | body, div, noscript, style |
| 9.14286px | 0.5714rem | 600 | 20px | 0.8px | div |
| 8.22857px | 0.5143rem | 600 | 20px | 0.8px | div |

### Heading Scale

```css
h1 { font-size: 67.0476px; font-weight: 400; line-height: 80.4571px; }
h4 { font-size: 30.4762px; font-weight: 400; line-height: 39.619px; }
h5 { font-size: 24.381px; font-weight: 400; line-height: 34.1333px; }
```

### Body Text

```css
body { font-size: 13.7143px; font-weight: 400; line-height: 17.1429px; }
```

### Font Weights in Use

`400` (792x), `600` (28x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-6 | 6px | 0.375rem |
| spacing-24 | 24px | 1.5rem |
| spacing-37 | 37px | 2.3125rem |
| spacing-48 | 48px | 3rem |
| spacing-53 | 53px | 3.3125rem |
| spacing-61 | 61px | 3.8125rem |
| spacing-69 | 69px | 4.3125rem |
| spacing-79 | 79px | 4.9375rem |
| spacing-85 | 85px | 5.3125rem |
| spacing-98 | 98px | 6.125rem |
| spacing-104 | 104px | 6.5rem |
| spacing-107 | 107px | 6.6875rem |
| spacing-128 | 128px | 8rem |
| spacing-158 | 158px | 9.875rem |
| spacing-192 | 192px | 12rem |
| spacing-195 | 195px | 12.1875rem |
| spacing-256 | 256px | 16rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| lg | 12px | 12 |
| xl | 20px | 1 |
| full | 30px | 16 |
| full | 37px | 8 |
| full | 49px | 3 |
| full | 80px | 2 |
| full | 90px | 7 |
| full | 98px | 3 |
| full | 200px | 30 |
| full | 300px | 2 |
| full | 2000px | 5 |

## CSS Custom Properties

### Other

```css
--deep-navy: #12273e;
--slate-grey: #083a74;
--bright-orange: #f56b20;
--soft-grey: #edecee;
--white-smoke: white;
--deep-plum: #742579;
--transparent: #edecee00;
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
| sm | 479px | max-width |
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 991px | max-width |
| 1680px | 1680px | min-width |

## Transitions & Animations

**Durations:** `0.2s`, `0.325s`, `0.35s`

### Common Transitions

```css
transition: all;
transition: color 0.2s;
transition: border-color 0.325s;
transition: transform 0.2s;
transition: background-color 0.35s;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (16 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(245, 107, 32);
  font-size: 12.1905px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 50px;
}
```

### Links (89 instances)

```css
.link {
  color: rgb(245, 107, 32);
  font-size: 12.1905px;
  font-weight: 400;
}
```

### Navigation (24 instances)

```css
.navigatio {
  background-color: rgb(221, 221, 221);
  color: rgb(51, 51, 51);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (14 instances)

```css
.foote {
  background-color: rgb(18, 39, 62);
  color: rgb(51, 51, 51);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12.1905px;
}
```

### Dropdowns (30 instances)

```css
.dropdown {
  background-color: rgb(245, 107, 32);
  border-radius: 0px;
  border-color: rgb(34, 34, 34);
  padding-top: 0px;
}
```

### Avatars (15 instances)

```css
.avatar {
  border-radius: 0px 0px 0px 50px;
}
```

### Tabs (27 instances)

```css
.tab {
  background-color: rgba(221, 221, 221, 0);
  color: rgb(51, 51, 51);
  font-size: 12.1905px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(51, 51, 51);
  border-radius: 0px;
}
```

### Switches (4 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(34, 34, 34);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 6 instances, 4 variants

**Variant 1** (2 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(245, 107, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 80px;
  border: 0px none rgb(245, 107, 32);
  font-size: 12.1905px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgb(18, 39, 62);
  color: rgb(255, 255, 255);
  padding: 0px 20.5714px 0px 20.5714px;
  border-radius: 50px;
  border: 0px none rgb(255, 255, 255);
  font-size: 13.7143px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(255, 255, 255);
  padding: 0px 24px 0px 24px;
  border-radius: 50px;
  border: 1px solid rgb(237, 236, 238);
  font-size: 13.7143px;
  font-weight: 400;
```

**Variant 4** (1 instance)

```css
  background: rgb(245, 107, 32);
  color: rgb(255, 255, 255);
  padding: 0px 20.5714px 0px 20.5714px;
  border-radius: 50px;
  border: 0px none rgb(255, 255, 255);
  font-size: 13.7143px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(245, 107, 32);
  color: rgb(245, 107, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 200px;
  border: 0px none rgb(245, 107, 32);
  font-size: 12.1905px;
  font-weight: 400;
```

### Button — 20 instances, 3 variants

**Variant 1** (18 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(245, 107, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 200px;
  border: 0px none rgb(245, 107, 32);
  font-size: 12.1905px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(245, 107, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 200px;
  border: 0px none rgb(245, 107, 32);
  font-size: 12.1905px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 13.7143px;
  font-weight: 400;
```

### Button — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(245, 107, 32);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(245, 107, 32);
  font-size: 12.1905px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(51, 51, 51);
  padding: 1px 6px 1px 6px;
  border-radius: 300px;
  border: 0px none rgb(51, 51, 51);
  font-size: 12.1905px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(245, 107, 32);
  padding: 0px 24px 0px 24px;
  border-radius: 50px;
  border: 0px none rgb(245, 107, 32);
  font-size: 12.1905px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **245 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1219.05px | 0px |
| 1680px | 30.4762px |
| 594.286px | 0px |
| 390.095px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 298.75px 298.766px 298.766px 298.766px;
gap: 8px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 88x |
| row/nowrap | 145x |
| row/wrap | 7x |
| column/wrap | 5x |

**Gap values:** `104px normal`, `16px`, `24px`, `32px normal`, `6.09524px normal`, `64px normal`, `8px`, `normal 16px`, `normal 8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 72/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 55/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 65/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 75/100 |

**Strengths:** Tight, disciplined color palette, Clean elevation system, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- No consistent spacing base unit detected — values appear arbitrary
- 40 !important rules — prefer specificity over overrides
- 83% of CSS is unused — consider purging
- 4190 duplicate CSS declarations

## Z-Index Map

**11 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 100000,100000 | div.m.e.n.u.-.c.o.n.t.e.n.t.s |
| dropdown | 900,900 | div.d.r.o.p.d.o.w.n.-.l.i.n.k. .w.-.d.r.o.p.d.o.w.n, div.d.r.o.p.d.o.w.n.-.l.i.n.k. .w.-.d.r.o.p.d.o.w.n |
| sticky | 11,11 | div.c.o.n.t.a.i.n.e.r. .i.s.-.-.f.u.l.l. .c.u.s.t.o.m.e.r.-.-.s.t.o.r.i.e.s, div.s.p.l.i.d.e.-.-.c.o.n.t.a.i.n.e.r, div.w.r.a.p.p.e.r. .i.s.-.-.c.o.n.t.e.n.t. .n.e.w.s.-.-.g.r.i.d. .i.s.-.-.s.p.l.i.d.e |
| base | -100,9 | video, div.h.o.m.e.-.v.i.d.e.o.-.e.m.b.e.d.-.2. .w.-.e.m.b.e.d, div.s.e.c.t.i.o.n. .i.s.-.-.f.o.o.t.e.r. .d.i.v.-.b.l.o.c.k |

**Issues:**
- [object Object]

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | normal | normal |
| Inter | self-hosted | 100, 200, 300, 400, 500, 600, 700, 800, 900 | normal |
| Manrope | self-hosted | 200, 300, 400, 500, 600, 700, 800 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 88 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 7 | objectFit: cover, borderRadius: 0px 0px 36.5714px, shape: square |

**Aspect ratios:** 4:3 (19x), 1:1 (8x), 16:9 (5x), 4.85:1 (3x), 21:9 (3x), 4.92:1 (3x), 6.67:1 (3x), 3.36:1 (2x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `325ms` | 325 |

## Component Anatomy

### button — 38 instances

**Slots:** label, icon
**Variants:** link · outline

| variant | count | sample label |
|---|---|---|
| link | 25 | Our Services |
| default | 11 | Contact Us |
| outline | 2 | View All |

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** unknown (tight)

### Top CTA Verbs

- **read** (6)
- **view** (2)
- **build** (2)
- **contact** (1)
- **get** (1)
- **our** (1)
- **meet** (1)

### Button Copy Patterns

- "read more" (6×)
- "view all" (2×)
- "let's build your brand" (2×)
- "contact us" (1×)
- "get started" (1×)
- "our services" (1×)
- "meet the federation" (1×)

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Brand Federation is a consultancy of nationally-recognized brand strategists backed by a global network of the world’s best independent specialists.

## Section Roles

Reading order (top→bottom): nav → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.258 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 2000px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.084)
**Counts:** total 95, svg 17, icon 12, screenshot-like 0, photo-like 4
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Arial` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
