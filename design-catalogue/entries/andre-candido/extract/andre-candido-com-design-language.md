# Design Language: André Cândido

> Extracted from `https://www.andre-candido.com/` on September 4, 2026
> 339 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#111118` | rgb(17, 17, 24) | hsl(240, 17%, 8%) | 476 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 67 |
| Accent | `#fef199` | rgb(254, 241, 153) | hsl(52, 98%, 80%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#ffffff` | hsl(0, 0%, 100%) | 82 |
| `#000000` | hsl(0, 0%, 0%) | 52 |
| `#222222` | hsl(0, 0%, 13%) | 12 |
| `#333333` | hsl(0, 0%, 20%) | 6 |
| `#7c7c7c` | hsl(0, 0%, 49%) | 4 |
| `#445567` | hsl(211, 20%, 34%) | 1 |
| `#dddddd` | hsl(0, 0%, 87%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#dddddd`, `#fef199`, `#111118`

### Text Colors

Text color palette: `#000000`, `#111118`, `#333333`, `#283338`, `#222222`, `#ffffff`, `#0082f3`, `#0000ee`, `#7c7c7c`

### Gradients

```css
background-image: linear-gradient(to right, rgb(255, 255, 255), rgba(255, 255, 255, 0));
```

```css
background-image: linear-gradient(270deg, rgb(255, 255, 255), rgba(255, 255, 255, 0));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#111118` | text, border, background | 476 |
| `#ffffff` | background, text, border | 82 |
| `#0000ee` | text, border | 67 |
| `#000000` | text, border | 52 |
| `#222222` | text, border | 12 |
| `#333333` | text, border | 6 |
| `#7c7c7c` | text, border | 4 |
| `#0082f3` | text, border | 2 |
| `#fbbf0d` | border | 2 |
| `#445567` | border | 1 |
| `#f7f5f1` | background | 1 |
| `#dddddd` | background | 1 |
| `#fef199` | background | 1 |

## Typography

### Font Families

- **PP Mori** — used for all (305 elements)
- **Editorial New** — used for headings (7 elements)
- **webflow-icons** — used for body (3 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 160px | 10rem | 200 | 176px | normal | h1 |
| 72px | 4.5rem | 200 | 72px | normal | h2 |
| 70.4px | 4.4rem | 200 | 77.44px | normal | h2 |
| 48px | 3rem | 200 | 57.6px | normal | h4 |
| 40px | 2.5rem | 400 | 48px | normal | div |
| 24px | 1.5rem | 400 | 28.8px | normal | div |
| 18px | 1.125rem | 400 | 21.6px | normal | body, div, a, nav |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 15px | 0.9375rem | 400 | 18px | normal | nav |
| 14px | 0.875rem | 400 | 19.6px | normal | div, li, span, p |
| 12.8px | 0.8rem | 400 | 15.36px | normal | div |
| 12px | 0.75rem | 400 | 12px | normal | div, a |

### Heading Scale

```css
h1 { font-size: 160px; font-weight: 200; line-height: 176px; }
h2 { font-size: 72px; font-weight: 200; line-height: 72px; }
h2 { font-size: 70.4px; font-weight: 200; line-height: 77.44px; }
h4 { font-size: 48px; font-weight: 200; line-height: 57.6px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 400; line-height: 19.6px; }
```

### Font Weights in Use

`400` (330x), `200` (8x), `600` (1x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-3 | 3px | 0.1875rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-80 | 80px | 5rem |
| spacing-112 | 112px | 7rem |
| spacing-140 | 140px | 8.75rem |
| spacing-170 | 170px | 10.625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 8px | 13 |
| xl | 24px | 6 |
| full | 50px | 6 |
| full | 80px | 3 |
| full | 100px | 6 |
| full | 150px | 2 |
| full | 800px | 1 |

## Box Shadows

**xs** — blur: 3px
```css
box-shadow: rgba(51, 51, 51, 0.4) 0px 0px 3px 0px;
```

## CSS Custom Properties

### Colors

```css
--accent: #ffed00;
```

### Other

```css
--black: #111118;
--gray: #7c7c7c;
--white: white;
--off-white: #f7f5f1;
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

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.2s`, `0.3s`, `0.1s`, `0.4s`

### Common Transitions

```css
transition: all;
transition: 0.2s;
transition: background-color 0.3s;
transition: background-color 0.1s, color 0.1s;
transition: background-color 0.3s ease-in;
transition: opacity 0.4s;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**slide**
```css
@keyframes slide {
  0% { transform: translateX(calc(0% + 50px)); }
  100% { transform: translateX(-100%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (13 instances)

```css
.button {
  background-color: rgba(255, 255, 255, 0.4);
  color: rgb(17, 17, 24);
  font-size: 12.8px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 100%;
}
```

### Cards (6 instances)

```css
.card {
  background-color: rgba(255, 255, 255, 0.4);
  border-radius: 100%;
  box-shadow: rgba(51, 51, 51, 0.4) 0px 0px 3px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (27 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 18px;
  font-weight: 400;
}
```

### Navigation (30 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(17, 17, 24);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (9 instances)

```css
.foote {
  background-color: rgb(17, 17, 24);
  color: rgb(255, 255, 255);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 18px;
}
```

### Modals (2 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (5 instances)

```css
.dropdown {
  background-color: rgb(17, 17, 24);
  border-radius: 0px;
  border-color: rgb(17, 17, 24);
  padding-top: 0px;
}
```

### Badges (11 instances)

```css
.badge {
  color: rgb(17, 17, 24);
  font-size: 14px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(17, 17, 24);
  color: rgb(255, 255, 255);
  padding: 10px 16px 10px 16px;
  border-radius: 24px;
  border: 1px solid rgb(17, 17, 24);
  font-size: 16px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(17, 17, 24);
  padding: 8px 8px 8px 8px;
  border-radius: 24px;
  border: 1px solid rgb(17, 17, 24);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 24px 0px 24px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 18px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 238);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 238);
  font-size: 18px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(17, 17, 24);
  color: rgb(255, 255, 255);
  padding: 40px 60px 30px 60px;
  border-radius: 150px;
  border: 2px solid rgb(255, 255, 255);
  font-size: 72px;
  font-weight: 200;
```

## Layout System

**5 grid containers** and **54 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1360px | 0px |
| 100% | 0px |
| 940px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 5x |

### Grid Templates

```css
grid-template-columns: 795.188px 170.391px;
gap: 0% 15%;
grid-template-columns: 564px 564px;
gap: 24px;
grid-template-columns: 172.797px 806.391px;
gap: 15%;
grid-template-columns: 172.797px 806.391px;
gap: 15%;
grid-template-columns: 395.188px 395.203px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 16x |
| row/nowrap | 38x |

**Gap values:** `0% 15%`, `0px 64px`, `10px`, `15%`, `16px`, `24px`, `40px`, `48px`, `4px`, `80px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 2 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#111118` | 18.8:1 | AAA |

## Design System Score

**Overall: 86/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 39 !important rules — prefer specificity over overrides
- 87% of CSS is unused — consider purging
- 2488 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | to right | 2 | brand |
| linear | 270deg | 2 | brand |

```css
background: linear-gradient(to right, rgb(255, 255, 255), rgba(255, 255, 255, 0));
background: linear-gradient(270deg, rgb(255, 255, 255), rgba(255, 255, 255, 0));
```

## Z-Index Map

**6 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,1000 | div.n.a.v.i.g.a.t.i.o.n.-.w.r.a.p, div.n.a.v.i.g.a.t.i.o.n.-.m.o.b. .w.-.n.a.v |
| base | 1,9 | div.w.-.s.l.i.d.e.r.-.m.a.s.k, div.a.v.a.i.l.a.b.i.l.i.t.y.-.b.a.d.g.e. .w.-.e.m.b.e.d, div.s.l.i.d.e.-.n.a.v. .w.-.s.l.i.d.e.r.-.n.a.v. .w.-.s.h.a.d.o.w. .w.-.r.o.u.n.d |

## SVG Icons

**1 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| md | 1 |

**Icon colors:** `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | normal | normal |
| Editorial New | self-hosted | 200 | normal |
| PP Mori | self-hosted | 400, 600 | italic, normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 34 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 4 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 3 | objectFit: fill, borderRadius: 0px, shape: square |
| avatar | 1 | objectFit: fill, borderRadius: 800px, shape: circular |

**Aspect ratios:** 3:2 (19x), 1:1 (7x), 4:3 (4x), 2.13:1 (3x), 9:16 (3x), 1.18:1 (3x), 2:3 (3x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

### Easing Families

- **ease-in-out** (14 uses) — `ease`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `slide` | slide-x | transform | 3 |

## Component Anatomy

### button — 8 instances

**Slots:** label
**Variants:** primary

| variant | count | sample label |
|---|---|---|
| default | 7 | About me |
| primary | 1 | Work with me |

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (verbose)

### Top CTA Verbs

- **let's** (2)
- **work** (1)
- **about** (1)
- **see** (1)
- **reach** (1)
- **ready** (1)
- **start** (1)

### Button Copy Patterns

- "work with me" (1×)
- "about me" (1×)
- "see all services" (1×)
- "reach out today" (1×)
- "ready to take your brand to the next level?
let's work together
→" (1×)
- "let's work together
→" (1×)
- "let's work together" (1×)
- "start a project" (1×)

### Sample Headings

> Thoughtful design for brilliant brands
> For over a decade, I've partnered with cross-functional teams in marketing, product, and sales to bring ideas to life.
> I build visual solutions that push brands forward, sparking attention and curiosity while ensuring consistency and scalability across all applications.
> I can help drive your next phase, whether you're launching a startup or evolving an established brand.
> Let's Work Together
> →

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** André Cândido is a visual designer connecting the dots between brand, design and strategy.

## Section Roles

Reading order (top→bottom): nav → nav → nav → content → nav → content → hero → content → hero → testimonial → hero → content → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | content | Thoughtful design for brilliant brands | 0.3 |
| 5 | content | — | 0.3 |
| 6 | hero | For over a decade, I've partnered with cross-functional teams in marketing, prod | 0.4 |
| 7 | content | — | 0.3 |
| 8 | hero | I build visual solutions that push brands forward, sparking attention and curios | 0.4 |
| 9 | testimonial | — | 0.8 |
| 10 | hero | I can help drive your next phase, whether you're launching a startup or evolving | 0.4 |
| 11 | content | Let's Work Together | 0.3 |
| 12 | content | — | 0.3 |

## Material Language

**Label:** `material-you` (confidence 0.45)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.308 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 800px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.425)
**Counts:** total 42, svg 33, icon 0, screenshot-like 0, photo-like 8
**Dominant aspect:** landscape
**Radius profile on images:** soft

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `PP Mori` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
