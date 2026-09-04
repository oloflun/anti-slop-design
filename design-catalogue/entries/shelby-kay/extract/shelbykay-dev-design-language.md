# Design Language: Shelby Kay • Freelance Front-End Developer

> Extracted from `https://shelbykay.dev/` on September 4, 2026
> 621 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#d6b292` | rgb(214, 178, 146) | hsl(28, 45%, 71%) | 1 |
| Secondary | `#efe6d9` | rgb(239, 230, 217) | hsl(35, 41%, 89%) | 32 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#393c2a` | hsl(70, 18%, 20%) | 1185 |
| `#000000` | hsl(0, 0%, 0%) | 56 |
| `#737955` | hsl(70, 17%, 40%) | 28 |
| `#afa199` | hsl(22, 12%, 64%) | 1 |
| `#7b8785` | hsl(170, 5%, 51%) | 1 |

### Background Colors

Used on large-area elements: `#efe6d9`, `#000000`, `#afa199`, `#393c2a`, `#d6b292`, `#7b8785`

### Text Colors

Text color palette: `#393c2a`, `#737955`, `#efe6d9`

### Gradients

```css
background-image: linear-gradient(90deg, rgb(57, 60, 42), rgb(57, 60, 42));
```

```css
background-image: linear-gradient(90deg, rgb(239, 230, 217), rgb(239, 230, 217));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#393c2a` | text, border, background | 1185 |
| `#000000` | background | 56 |
| `#efe6d9` | background, text, border | 32 |
| `#737955` | text, border | 28 |
| `#afa199` | background | 1 |
| `#d6b292` | background | 1 |
| `#7b8785` | background | 1 |

## Typography

### Font Families

- **Switzer** — used for all (598 elements)
- **Ranade** — used for all (23 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 256px | 16rem | 400 | 230.4px | normal | h1, span |
| 140.8px | 8.8rem | 700 | 140.8px | normal | a, span |
| 73.92px | 4.62rem | 700 | 73.92px | normal | span |
| 24px | 1.5rem | 700 | 28.8px | normal | h2 |
| 20px | 1.25rem | 400 | 24px | normal | html, head, meta, link |
| 16px | 1rem | 600 | 20px | normal | p |
| 14px | 0.875rem | 700 | 16.8px | normal | nav, a, span, h3 |
| 11px | 0.6875rem | 700 | 11px | normal | h3 |
| 10px | 0.625rem | 500 | 12px | normal | span |

### Heading Scale

```css
h1 { font-size: 256px; font-weight: 400; line-height: 230.4px; }
h2 { font-size: 24px; font-weight: 700; line-height: 28.8px; }
h3 { font-size: 14px; font-weight: 700; line-height: 16.8px; }
h3 { font-size: 11px; font-weight: 700; line-height: 11px; }
```

### Body Text

```css
body { font-size: 10px; font-weight: 500; line-height: 12px; }
```

### Font Weights in Use

`500` (478x), `700` (73x), `400` (53x), `600` (17x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-6 | 6px | 0.375rem |
| spacing-35 | 35px | 2.1875rem |
| spacing-56 | 56px | 3.5rem |
| spacing-80 | 80px | 5rem |
| spacing-112 | 112px | 7rem |
| spacing-128 | 128px | 8rem |
| spacing-200 | 200px | 12.5rem |
| spacing-248 | 248px | 15.5rem |

## CSS Custom Properties

### Colors

```css
--color-primary: #7b8785;
--color-primary-dark: #454931;
--color-primary-darker: #393c2a;
--color-beige-warm: #d6b292;
--color-beige: #efe6d9;
--color-brown-light: #afa199;
--color-black: #2c1c03;
--color-blue: #7b8785;
```

### Spacing

```css
--margin-side: 12px;
--gap: 4px;
```

### Other

```css
--screen: var(--vh);
--container-width: 1800px;
--columns: 8;
--column: calc(min(100vw, var(--container-width))/var(--columns));
--ease-quart: cubic-bezier(.165,.84,.44,1);
--ease-quart-inout: cubic-bezier(.76,0,.24,1);
--ease-cubic: cubic-bezier(.33,1,.68,1);
--ease-cubic-inout: cubic-bezier(.785,.135,.15,.86);
```

### Dependencies

```css
--screen: --vh;
--column: --container-width,--columns;
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

**Durations:** `0.4s`, `0.1s`, `1.25s`, `0.6s`, `0.5s`, `1.2s`

### Common Transitions

```css
transition: all;
transition: background-size 0.4s cubic-bezier(0.76, 0, 0.24, 1);
transition: transform 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
transition: mask-position 1.25s cubic-bezier(0.76, 0, 0.24, 1), -webkit-mask-position 1.25s cubic-bezier(0.76, 0, 0.24, 1);
transition: opacity 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
transition: opacity 0.6s cubic-bezier(0.165, 0.84, 0.44, 1), filter 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
transition: opacity 0.5s cubic-bezier(0.76, 0, 0.24, 1);
transition: transform 1.2s cubic-bezier(0.76, 0, 0.24, 1);
```

### Keyframe Animations

**svelte-tz8cmd-spreadWordPartX**
```css
@keyframes svelte-tz8cmd-spreadWordPartX {
  100% { transform: translateX(calc(var(--offset)*-1)); }
}
```

**svelte-tz8cmd-spreadWordPartY**
```css
@keyframes svelte-tz8cmd-spreadWordPartY {
  100% { transform: translateY(calc(var(--offset)*1)); }
}
```

**svelte-tz8cmd-fadeIn**
```css
@keyframes svelte-tz8cmd-fadeIn {
  0% { opacity: 0; }
  100% { opacity: 0.1; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Links (95 instances)

```css
.link {
  color: rgb(57, 60, 42);
  font-size: 20px;
  font-weight: 500;
}
```

### Navigation (2 instances)

```css
.navigatio {
  color: rgb(57, 60, 42);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

## Layout System

**77 grid containers** and **13 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1800px | 19.2px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 58x |
| 2-column | 10x |
| 32-column | 3x |
| 3-column | 2x |
| 4-column | 1x |
| 19-column | 1x |
| 14-column | 1x |
| 21-column | 1x |

### Grid Templates

```css
grid-template-columns: 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px;
gap: normal 8px;
grid-template-columns: 231.594px 231.594px 231.594px 231.594px;
gap: 40px;
grid-template-columns: 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0469px 31.0625px;
gap: normal 8px;
grid-template-columns: 1280px;
grid-template-columns: 1241.62px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 4x |
| column/nowrap | 8x |
| row/wrap | 1x |

**Gap values:** `40px`, `8px`, `normal 8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 94/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 90/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 185 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 90deg | 2 | brand |
| linear | 90deg | 2 | brand |

```css
background: linear-gradient(90deg, rgb(57, 60, 42), rgb(57, 60, 42));
background: linear-gradient(90deg, rgb(239, 230, 217), rgb(239, 230, 217));
```

## Z-Index Map

**5 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,100 | h2.t.i.t.l.e. .t.i.t.l.e.-.s.e.c.t.i.o.n. .s.v.e.l.t.e.-.1.f.u.s.9.n.j |
| base | -20,1 | div.s.e.c.t.i.o.n.-.b.g. .s.v.e.l.t.e.-.t.z.8.c.m.d. .i.s.-.w.i.p.i.n.g, div.s.e.c.t.i.o.n.-.b.g. .s.v.e.l.t.e.-.1.f.u.s.9.n.j, div.s.e.c.t.i.o.n.-.b.g. .s.v.e.l.t.e.-.1.x.m.t.h.t.n |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Switzer | self-hosted | 1 999 | normal |
| Ranade | self-hosted | 700 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 30 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 4 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:2 (16x), 4:3 (14x), 1:1 (2x), 1.15:1 (1x), 3:4 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `md` | `400ms` | 400 |
| `lg` | `500ms` | 500 |
| `xl` | `1.2s` | 1200 |
| `xxl` | `1.25s` | 1250 |

### Easing Families

- **custom** (29 uses) — `cubic-bezier(0.76, 0, 0.24, 1)`
- **ease-out** (72 uses) — `cubic-bezier(0.165, 0.84, 0.44, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `svelte-tz8cmd-fadeIn` | fade | opacity | 1 |

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Sample Headings

> SH
E
LB
Y
KA
> WORK
> DP
> LGF
> INT
> SH
E
LB
Y
KA
> WORK
> DP
> LGF
> INT

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** Freelance Front-End Developer based in France and working worldwide remotely. Focusing on crafting digital experiences with an editorial, modern and unique approach.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): testimonial → hero → nav → content → nav → testimonial → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | testimonial | SH
E
LB
Y
KA | 0.8 |
| 1 | hero | SH
E
LB
Y
KA | 0.85 |
| 2 | nav | — | 0.9 |
| 3 | content | WORK | 0.3 |
| 4 | nav | — | 0.9 |
| 5 | testimonial | PROFILE | 0.8 |
| 6 | content | CONTACT | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.175 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.578)
**Counts:** total 34, svg 0, icon 0, screenshot-like 0, photo-like 35
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Switzer` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
