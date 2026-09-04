# Design Language: TOMO

> Extracted from `https://tomoseattle.com/` on September 4, 2026
> 192 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ff6347` | rgb(255, 99, 71) | hsl(9, 100%, 64%) | 2 |
| Secondary | `#eee2d4` | rgb(238, 226, 212) | hsl(32, 43%, 88%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 376 |
| `#ffffff` | hsl(0, 0%, 100%) | 53 |
| `#f0f0f0` | hsl(0, 0%, 94%) | 1 |
| `#1a1a1a` | hsl(0, 0%, 10%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#ff6347`, `#000000`, `#eee2d4`

### Text Colors

Text color palette: `#000000`, `#ffffff`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 376 |
| `#ffffff` | background, text, border | 53 |
| `#ff6347` | background | 2 |
| `#f0f0f0` | background | 1 |
| `#eee2d4` | background | 1 |
| `#1a1a1a` | background | 1 |

## Typography

### Font Families

- **Recife** — used for all (109 elements)
- **Times New Roman** — used for body (80 elements)
- **Icons** — used for all (1 elements)
- **Arial** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 28.8px | 1.8rem | 300 | 28.8px | normal | h1, span, b, br |
| 28px | 1.75rem | 400 | 28px | normal | a |
| 23.04px | 1.44rem | 400 | 23.04px | normal | a, bodycopy, div, img |
| 13.3333px | 0.8333rem | 400 | normal | normal | button |
| 11.52px | 0.72rem | 400 | normal | normal | html, head, script, meta |

### Heading Scale

```css
h1 { font-size: 28.8px; font-weight: 300; line-height: 28.8px; }
```

### Body Text

```css
body { font-size: 28.8px; font-weight: 300; line-height: 28.8px; }
```

### Font Weights in Use

`400` (184x), `300` (8x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-58 | 58px | 3.625rem |
| spacing-99 | 99px | 6.1875rem |
| spacing-116 | 116px | 7.25rem |
| spacing-143 | 143px | 8.9375rem |
| spacing-269 | 269px | 16.8125rem |
| spacing-293 | 293px | 18.3125rem |
| spacing-338 | 338px | 21.125rem |
| spacing-360 | 360px | 22.5rem |
| spacing-369 | 369px | 23.0625rem |
| spacing-415 | 415px | 25.9375rem |
| spacing-474 | 474px | 29.625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| full | 100px | 2 |

## CSS Custom Properties

### Other

```css
--following-width: -400px;
--following-animation-duration: 450ms;
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
| sm | 480px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.2s`

### Common Transitions

```css
transition: all;
transition: max-height 0.2s ease-out;
```

### Keyframe Animations

**fly**
```css
@keyframes fly {
  98.001%, 0% { display: block; transform: translateX(-200%) translateY(100vh) rotateZ(0deg); }
  15% { transform: translateX(100vw) translateY(-100%) rotateZ(180deg); }
  15.001%, 18% { transform: translateX(100vw) translateY(-30%) rotateZ(0deg); }
  40% { transform: translateX(-200%) translateY(3vh) rotateZ(-180deg); }
  40.001%, 43% { transform: translateX(-200%) translateY(-100%) rotateZ(-180deg); }
  65% { transform: translateX(100vw) translateY(50vh) rotateZ(0deg); }
  65.001%, 68% { transform: translateX(20vw) translateY(-200%) rotateZ(180deg); }
  95% { transform: translateX(10vw) translateY(100vh) rotateZ(0deg); }
}
```

**blink**
```css
@keyframes blink {
  0%, 15% { opacity: 0; }
  16%, 100% { opacity: 1; }
}
```

**following-open**
```css
@keyframes following-open {
  0% { transform: translateX(0px); }
  100% { transform: translateX(var(--following-width)); }
}
```

**following-open-inverse**
```css
@keyframes following-open-inverse {
  0% { transform: translateX(0px); }
  100% { transform: translateX(calc(-1 * var(--following-width))); }
}
```

**following-close**
```css
@keyframes following-close {
  0% { transform: translateX(var(--following-width)); }
  100% { transform: translateX(0px); }
}
```

**following-close-inverse**
```css
@keyframes following-close-inverse {
  0% { transform: translateX(calc(-1 * var(--following-width))); }
  100% { transform: translateX(0px); }
}
```

**fade-pulse-in**
```css
@keyframes fade-pulse-in {
  0% { opacity: 0; }
  50% { opacity: 0.5; }
  100% { opacity: 1; }
}
```

**fade-pulse-in**
```css
@keyframes fade-pulse-in {
  0% { opacity: 0; }
  50% { opacity: 0.5; }
  100% { opacity: 1; }
}
```

**pulsate**
```css
@keyframes pulsate {
  0% { opacity: 1; }
  50% { opacity: 0; }
  100% { opacity: 1; }
}
```

**pulsate**
```css
@keyframes pulsate {
  0% { opacity: 1; }
  50% { opacity: 0; }
  100% { opacity: 1; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (1 instances)

```css
.button {
  background-color: rgb(240, 240, 240);
  color: rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
  padding-top: 1px;
  padding-right: 6px;
  border-radius: 0px;
}
```

### Cards (56 instances)

```css
.card {
  background-color: rgba(0, 0, 0, 0.004);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (9 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 23.04px;
  font-weight: 400;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 23.04px;
}
```

### Modals (1 instances)

```css
.modal {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(240, 240, 240);
  color: rgb(0, 0, 0);
  padding: 1px 6px 1px 6px;
  border-radius: 0px;
  border: 2px outset rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

### Link — 7 instances, 1 variant

**Variant 1** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 2.304px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 23.04px;
  font-weight: 400;
```

### Card — 28 instances, 5 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 345.625px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 23.04px;
  font-weight: 400;
```

**Variant 2** (15 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 360.422px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.04px;
  font-weight: 400;
```

**Variant 3** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 99.0781px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.04px;
  font-weight: 400;
```

**Variant 4** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 1017.33px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.04px;
  font-weight: 400;
```

**Variant 5** (6 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 62.1562px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 23.04px;
  font-weight: 400;
```

### Card — 21 instances, 1 variant

**Variant 1** (21 instances)

```css
  background: rgba(0, 0, 0, 0.004);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.04px;
  font-weight: 400;
```

## Layout System

**0 grid containers** and **6 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/wrap | 5x |
| column/nowrap | 1x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#000000` | `#f0f0f0` | 18.43:1 | AAA |

## Design System Score

**Overall: 74/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 55/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- No consistent spacing base unit detected — values appear arbitrary
- 65 !important rules — prefer specificity over overrides
- 86% of CSS is unused — consider purging
- 1050 duplicate CSS declarations

## Z-Index Map

**30 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483637,2147483637 | div |
| dropdown | 100,100 | div.l.o.a.d.i.n.g |
| sticky | 10,28 | script, script, div.g.a.l.l.e.r.y._.c.a.r.d |
| base | 1,9 | a.g.a.l.l.e.r.y._.c.a.r.d, div.t.h.u.m.b.n.a.i.l.s, div.p.a.g.e. .c.o.n.t.a.i.n.e.r. .c.o.n.t.a.i.n.e.r._.w.i.d.t.h |

**Issues:**
- [object Object]

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| DruryLane | self-hosted | normal | normal |
| Recife | self-hosted | 400, bold, normal | normal |
| Icons | self-hosted | 200, 240, 400, 600, 800, normal | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 12 | objectFit: fill, borderRadius: 0px, shape: square |
| thumbnail | 9 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 8 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (10x), 3:4 (5x), 16:9 (2x), 21:9 (2x), 2.84:1 (1x), 3.7:1 (1x), 2.1:1 (1x), 2.66:1 (1x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |

### Easing Families

- **ease-in-out** (1 uses) — `ease`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `fade-pulse-in` | fade | opacity | 1 |
| `fade-pulse-in` | fade | opacity | 1 |
| `spin-loading` | rotate | transform | 1 |
| `spin-loading` | rotate | transform | 1 |

## Component Anatomy

### card — 49 instances

**Slots:** media

### link — 7 instances


## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** unknown (tight)

### Top CTA Verbs

- **close** (1)

### Button Copy Patterns

- "close button" (1×)

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Eclectic fare and serious wine in a former adult video store from Brady Ishiwata Williams. Bring your friends.

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.138 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.115)
**Counts:** total 29, svg 0, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Recife` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
