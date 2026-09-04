# Design Language: Craft, engineered · wild

> Extracted from `https://craft.wild.as/` on September 4, 2026
> 864 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#d8ff00` | rgb(216, 255, 0) | hsl(69, 100%, 50%) | 1 |
| Secondary | `#f5c518` | rgb(245, 197, 24) | hsl(47, 92%, 53%) | 1 |
| Accent | `#6c4cf1` | rgb(108, 76, 241) | hsl(252, 85%, 62%) | 2 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#ffffff` | hsl(0, 0%, 100%) | 913 |
| `#0a0a0a` | hsl(0, 0%, 4%) | 695 |
| `#2a2a2a` | hsl(0, 0%, 16%) | 77 |
| `#000000` | hsl(0, 0%, 0%) | 51 |
| `#8b8b8b` | hsl(0, 0%, 55%) | 30 |

### Background Colors

Used on large-area elements: `#ffffff`, `#0a0a0a`

### Text Colors

Text color palette: `#000000`, `#0a0a0a`, `#8b8b8b`, `#ffffff`, `#2a2a2a`

### Gradients

```css
background-image: linear-gradient(to top, rgba(10, 10, 10, 0.8) 0px, rgba(10, 10, 10, 0.8) 14px, rgba(10, 10, 10, 0.52) 14px, rgba(10, 10, 10, 0.52) 28px, rgba(10, 10, 10, 0.28) 28px, rgba(10, 10, 10, 0.28) 42px, rgba(10, 10, 10, 0.1) 42px, rgba(10, 10, 10, 0.1) 56px, rgba(10, 10, 10, 0) 56px);
```

```css
background-image: repeating-linear-gradient(90deg, rgb(10, 10, 10) 0px, rgb(10, 10, 10) 8px, rgba(0, 0, 0, 0) 8px, rgba(0, 0, 0, 0) 9px);
```

```css
background-image: repeating-linear-gradient(90deg, rgb(10, 10, 10) 0px, rgb(10, 10, 10) 4px, rgba(0, 0, 0, 0) 4px, rgba(0, 0, 0, 0) 7px);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#ffffff` | background, text, border | 913 |
| `#0a0a0a` | text, border, background | 695 |
| `#2a2a2a` | text, border | 77 |
| `#000000` | text, border | 51 |
| `#8b8b8b` | text, border | 30 |
| `#1c2541` | background | 8 |
| `#e0492a` | background | 3 |
| `#3b5bd9` | background | 2 |
| `#6c4cf1` | background | 2 |
| `#d8ff00` | background | 1 |
| `#f5c518` | background | 1 |

## Typography

### Font Families

- **Sneak** — used for all (660 elements)
- **Arial** — used for all (134 elements)
- **SFMono-Regular** — used for body (45 elements)
- **Times New Roman** — used for body (25 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 66.56px | 4.16rem | 400 | 61.2352px | -2.3296px | h1, span |
| 43.52px | 2.72rem | 400 | 46.1312px | -0.8704px | p, span, h2, br |
| 34px | 2.125rem | 400 | 34px | -0.68px | span |
| 28.16px | 1.76rem | 500 | 42.24px | -0.5632px | p |
| 22px | 1.375rem | 400 | 33px | 1.76px | div |
| 18.56px | 1.16rem | 400 | 21.9008px | -0.1856px | p, span |
| 16px | 1rem | 400 | normal | normal | html, head, script, meta |
| 15.36px | 0.96rem | 500 | 23.04px | -0.1536px | a, span, i, p |
| 15px | 0.9375rem | 400 | 24.3px | normal | p, span, strong, li |
| 14.5px | 0.9063rem | 400 | 21.75px | normal | p |
| 14px | 0.875rem | 400 | 22.68px | normal | p, button, span |
| 13.5px | 0.8438rem | 400 | 20.25px | normal | p |
| 13.3333px | 0.8333rem | 400 | normal | normal | button, svg, path, polyline |
| 13px | 0.8125rem | 400 | 18.85px | normal | p, span |
| 11px | 0.6875rem | 400 | 16.5px | 1.43px | a, svg, path, div |

### Heading Scale

```css
h1 { font-size: 66.56px; font-weight: 400; line-height: 61.2352px; }
h2 { font-size: 43.52px; font-weight: 400; line-height: 46.1312px; }
```

### Body Text

```css
body { font-size: 43.52px; font-weight: 400; line-height: 46.1312px; }
```

### Font Weights in Use

`500` (452x), `400` (412x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-12 | 12px | 0.75rem |
| spacing-26 | 26px | 1.625rem |
| spacing-35 | 35px | 2.1875rem |
| spacing-42 | 42px | 2.625rem |
| spacing-49 | 49px | 3.0625rem |
| spacing-56 | 56px | 3.5rem |
| spacing-98 | 98px | 6.125rem |
| spacing-126 | 126px | 7.875rem |
| spacing-168 | 168px | 10.5rem |
| spacing-356 | 356px | 22.25rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 6px | 6 |
| md | 10px | 1 |

## Box Shadows

**md** — blur: 12px
```css
box-shadow: rgba(10, 10, 10, 0.14) 0px 2px 12px 0px;
```

## CSS Custom Properties

### Colors

```css
--muted: #8b8b8b;
```

### Radii

```css
--radius: 26px;
```

### Other

```css
--paper: #FFFFFF;
--ink: #0A0A0A;
--red: #e0492a;
--neon: #d8ff00;
--line: rgba(10,10,10,.12);
--line-2: rgba(10,10,10,.06);
--cell: 14px;
--gutter: 56px;
--maxw: 1176px;
--readw: 34ch;
--mono: "SFMono-Regular",ui-monospace,Menlo,Consolas,monospace;
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
| 560px | 560px | min-width |
| sm | 680px | max-width |
| md | 720px | max-width |
| 840px | 840px | min-width |
| 860px | 860px | min-width |
| 880px | 880px | min-width |
| 900px | 900px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.35s`, `0.15s`, `0.4s`, `0.2s`, `0.85s`, `0.1s`, `0.5s`, `0.25s`, `0.8s`, `0.12s`, `0.3s`, `0.24s`, `0.36s`, `0.45s`, `0.55s`

### Common Transitions

```css
transition: all;
transition: opacity 0.35s, transform 0.35s;
transition: background 0.15s, border-color 0.15s;
transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s;
transition: transform 0.85s steps(6);
transition: transform 0.85s steps(6) 0.1s;
transition: transform 0.85s steps(6) 0.2s;
transition: transform 0.5s steps(4);
transition: transform 0.5s steps(5);
transition: background 0.2s, opacity 0.25s;
```

### Keyframe Animations

**heroIn**
```css
@keyframes heroIn {
  0% { opacity: 0; transform: translateY(14px); }
  100% { opacity: 1; transform: none; }
}
```

**heroLine**
```css
@keyframes heroLine {
  0% { transform: translateY(115%); }
  100% { transform: translateY(0px); }
}
```

**lineGrowX**
```css
@keyframes lineGrowX {
  100% { transform: scaleX(1); }
}
```

**lineGrowY**
```css
@keyframes lineGrowY {
  100% { transform: scaleY(1); }
}
```

**wSpin**
```css
@keyframes wSpin {
  0% { transform: rotateY(0deg); }
  100% { transform: rotateY(360deg); }
}
```

**smJump**
```css
@keyframes smJump {
  0% { transform: translateY(0px); }
  28% { transform: translateY(-18px); }
  52% { transform: translateY(0px); }
  68% { transform: translateY(-7px); }
  100% { transform: translateY(0px); }
}
```

**smHeart**
```css
@keyframes smHeart {
  0% { opacity: 0; transform: translate(-50%, 0px) scale(0.5); }
  14% { opacity: 1; }
  100% { opacity: 0; transform: translate(-50%, -72px) scale(1.1); }
}
```

**ttOver**
```css
@keyframes ttOver {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (19 instances)

```css
.button {
  background-color: rgb(10, 10, 10);
  color: rgb(255, 255, 255);
  font-size: 13.3333px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Links (17 instances)

```css
.link {
  color: rgb(10, 10, 10);
  font-size: 16px;
  font-weight: 400;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(10, 10, 10);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Badges (2 instances)

```css
.badge {
  color: rgb(10, 10, 10);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(10, 10, 10);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 13.3333px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(10, 10, 10);
  color: rgb(255, 255, 255);
  padding: 16px 36px 16px 36px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 15.36px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(10, 10, 10);
  color: rgb(255, 255, 255);
  padding: 16px 36px 16px 36px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 15.36px;
  font-weight: 500;
```

## Layout System

**29 grid containers** and **55 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1176px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 10x |
| 1-column | 8x |
| 4-column | 2x |
| 23-column | 1x |
| 18-column | 1x |
| 15-column | 1x |

### Grid Templates

```css
grid-template-columns: 444.438px 639.562px;
gap: 0px 84px;
grid-template-columns: 444.438px 639.562px;
gap: 0px 84px;
grid-template-columns: 444.438px 639.562px;
gap: 0px 84px;
grid-template-columns: 692.922px 433.078px;
gap: 42px;
grid-template-columns: 444.438px 639.562px;
gap: 0px 84px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 26x |
| column/nowrap | 25x |
| row/wrap | 4x |

**Gap values:** `0px 84px`, `12px`, `13px`, `14px`, `21px`, `28px`, `42px`, `7px`, `8px`, `9px`

## Accessibility (WCAG 2.1)

**Overall Score: 88%** — 22 passing, 3 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#ffffff` | `#e0492a` | 4.07:1 | FAIL | span (3x) |

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#1c2541` | 15.1:1 | AAA |
| `#0a0a0a` | `#ffffff` | 19.8:1 | AAA |
| `#ffffff` | `#0a0a0a` | 19.8:1 | AAA |
| `#ffffff` | `#3b5bd9` | 5.7:1 | AA |
| `#ffffff` | `#6c4cf1` | 5.33:1 | AA |
| `#0a0a0a` | `#d8ff00` | 17.18:1 | AAA |
| `#0a0a0a` | `#f5c518` | 12.14:1 | AAA |

## Design System Score

**Overall: 83/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 88/100 |
| CSS Tokenization | 75/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 3 WCAG contrast failures
- 511 duplicate CSS declarations

## Gradients

**3 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | to top | 9 | complex |
| repeating-linear | 90deg | 4 | bold |
| repeating-linear | 90deg | 4 | bold |

```css
background: linear-gradient(to top, rgba(10, 10, 10, 0.8) 0px, rgba(10, 10, 10, 0.8) 14px, rgba(10, 10, 10, 0.52) 14px, rgba(10, 10, 10, 0.52) 28px, rgba(10, 10, 10, 0.28) 28px, rgba(10, 10, 10, 0.28) 42px, rgba(10, 10, 10, 0.1) 42px, rgba(10, 10, 10, 0.1) 56px, rgba(10, 10, 10, 0) 56px);
background: repeating-linear-gradient(90deg, rgb(10, 10, 10) 0px, rgb(10, 10, 10) 8px, rgba(0, 0, 0, 0) 8px, rgba(0, 0, 0, 0) 9px);
background: repeating-linear-gradient(90deg, rgb(10, 10, 10) 0px, rgb(10, 10, 10) 4px, rgba(0, 0, 0, 0) 4px, rgba(0, 0, 0, 0) 7px);
```

## Z-Index Map

**9 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 200,200 | div.p.x.c.t.l |
| sticky | 60,60 | a.t.o.p.l.i.n.k |
| base | 0,6 | canvas, section.h.e.r.o, span.p.x.f.x |

## SVG Icons

**5 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 2 |
| xl | 2 |

**Icon colors:** `currentColor`, `#0a0a0a`, `rgb(0, 0, 0)`, `#e0492a`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Sneak | self-hosted | 300, 400, 500 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 3 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 4:3 (3x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `450ms` | 450 |
| `xl` | `800ms` | 800 |

### Easing Families

- **ease-out** (3 uses) — `cubic-bezier(0.16, 1, 0.3, 1)`
- **steps** (53 uses) — `steps(6)`, `steps(4)`, `steps(5)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `heroIn` | slide-y | opacity, transform | 2 |
| `heroLine` | slide-y | transform | 4 |
| `wSpin` | rotate | transform | 1 |
| `ttOver` | fade | opacity | 1 |

## Component Anatomy

### button — 6 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **read** (1)
- **play** (1)

### Button Copy Patterns

- "read the full story" (1×)
- "play" (1×)

### Sample Headings

> CRAFT,
ENGINEERED.
> Born in Vienna, where craft is a discipline.
> AI is good at everything except the last 10 percent.
> Explore. Generate.
Refine. Scale.
> The Brand Context Protocol.
> CRAFT,
ENGINEERED.
> Born in Vienna, where craft is a discipline.
> AI is good at everything except the last 10 percent.
> Explore. Generate.
Refine. Scale.
> The Brand Context Protocol.

## Page Intent

**Type:** `landing` (confidence 0.75)
**Description:** Craft is the constant. Engineering, and now AI, is how we make more of it. A point of view from wild, a design and technology studio born in Vienna.

## Section Roles

Reading order (top→bottom): steps → hero → content → content → content → content → content → hero → content → testimonials → hero → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | steps | CRAFT,
ENGINEERED. | 0.75 |
| 1 | hero | CRAFT,
ENGINEERED. | 0.85 |
| 2 | content | — | 0.3 |
| 3 | content | — | 0.3 |
| 4 | content | Born in Vienna, where craft is a discipline. | 0.3 |
| 5 | content | AI is good at everything except the last 10 percent. | 0.3 |
| 6 | content | Explore. Generate.
Refine. Scale. | 0.3 |
| 7 | hero | The Brand Context Protocol. | 0.4 |
| 8 | content | — | 0.3 |
| 9 | testimonials | Move your organisation up the levels of AI. | 0.4 |
| 10 | hero | The tools are everywhere. The judgment isn't. | 0.4 |
| 11 | content | — | 0.3 |
| 12 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.427 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 10px |
| backdrop-filter in use | no |
| Gradients | 3 |

## Imagery Style

**Label:** `photography` (confidence 0.75)
**Counts:** total 3, svg 0, icon 0, screenshot-like 0, photo-like 3
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Sneak` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
