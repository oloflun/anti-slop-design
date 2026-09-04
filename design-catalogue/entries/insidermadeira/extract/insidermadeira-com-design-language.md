# Design Language: Exclusive Tailor-Made Luxury Travel Experiences in Madeira | Insider

> Extracted from `https://www.insidermadeira.com` on September 4, 2026
> 1352 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ffdede` | rgb(255, 222, 222) | hsl(0, 100%, 94%) | 3 |
| Secondary | `#f1ede5` | rgb(241, 237, 229) | hsl(40, 30%, 92%) | 93 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1481 |
| `#201f1d` | hsl(40, 5%, 12%) | 675 |
| `#ffffff` | hsl(0, 0%, 100%) | 417 |
| `#c6c3bb` | hsl(44, 9%, 75%) | 92 |
| `#333333` | hsl(0, 0%, 20%) | 4 |
| `#dddddd` | hsl(0, 0%, 87%) | 3 |
| `#b8b8b8` | hsl(0, 0%, 72%) | 2 |
| `#6a6a6a` | hsl(0, 0%, 42%) | 2 |
| `#cccccc` | hsl(0, 0%, 80%) | 1 |

### Background Colors

Used on large-area elements: `#f9f9f9`, `#000000`, `#f1ede5`

### Text Colors

Text color palette: `#000000`, `#201f1d`, `#333333`, `#f9f9f9`, `#b8b8b8`, `#ffffff`, `#c6c3bb`, `#383838`, `#f1ede5`, `#6a6a6a`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 1481 |
| `#201f1d` | text, border, background | 675 |
| `#ffffff` | background, text, border | 417 |
| `#f1ede5` | border, background, text | 93 |
| `#c6c3bb` | text, border | 92 |
| `#333333` | text, border | 4 |
| `#dddddd` | background | 3 |
| `#ffdede` | background | 3 |
| `#b8b8b8` | text, border | 2 |
| `#6a6a6a` | text, border | 2 |
| `#cccccc` | border | 1 |

## Typography

### Font Families

- **PP Mori** — used for body (1234 elements)
- **GT Super Display** — used for all (77 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 63.3333px | 3.9583rem | 300 | 63.3333px | normal | h2 |
| 36px | 2.25rem | 300 | 36px | normal | h1, h2 |
| 24px | 1.5rem | 400 | 31.2px | normal | div, svg, path, h4 |
| 23.4667px | 1.4667rem | 300 | 28.16px | normal | h3 |
| 21px | 1.3125rem | 400 | 27.3px | normal | div, svg, path |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14px | 0.875rem | 400 | 14px | normal | a, div, svg, defs |
| 12.8px | 0.8rem | 400 | 16.64px | normal | div, a, img, svg |
| 10.6667px | 0.6667rem | 400 | 13.8667px | normal | body, div, style, noscript |
| 10px | 0.625rem | 400 | 10px | normal | span, div, a |
| 9.33333px | 0.5833rem | 400 | 11.2px | normal | p, div, label |
| 6.66667px | 0.4167rem | 400 | 6.66667px | normal | div |

### Heading Scale

```css
h2 { font-size: 63.3333px; font-weight: 300; line-height: 63.3333px; }
h1 { font-size: 36px; font-weight: 300; line-height: 36px; }
h4 { font-size: 24px; font-weight: 400; line-height: 31.2px; }
h3 { font-size: 23.4667px; font-weight: 300; line-height: 28.16px; }
h3 { font-size: 16px; font-weight: 400; line-height: normal; }
h4 { font-size: 14px; font-weight: 400; line-height: 14px; }
```

### Body Text

```css
body { font-size: 10.6667px; font-weight: 400; line-height: 13.8667px; }
```

### Font Weights in Use

`400` (1227x), `300` (77x), `500` (33x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-24 | 24px | 1.5rem |
| spacing-27 | 27px | 1.6875rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-53 | 53px | 3.3125rem |
| spacing-60 | 60px | 3.75rem |
| spacing-67 | 67px | 4.1875rem |
| spacing-80 | 80px | 5rem |
| spacing-85 | 85px | 5.3125rem |
| spacing-93 | 93px | 5.8125rem |
| spacing-100 | 100px | 6.25rem |
| spacing-103 | 103px | 6.4375rem |
| spacing-149 | 149px | 9.3125rem |
| spacing-297 | 297px | 18.5625rem |
| spacing-333 | 333px | 20.8125rem |
| spacing-461 | 461px | 28.8125rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 30 |
| xl | 20px | 7 |
| full | 50px | 23 |
| full | 100px | 8 |
| full | 640px | 15 |
| full | 999px | 1 |
| full | 1600px | 1 |
| full | 15984px | 1 |

## CSS Custom Properties

### Colors

```css
--base-color-neutral--light: #f9f9f9;
--base-color-brand--black: #201f1d;
--text-color--text-primary<deleted|relume-variable-text-color-1>: var(--base-color-neutral--black\<deleted\|relume-variable-color-neutral-1\>);
--link-color--link-primary<deleted|relume-variable-link-color-1>: var(--base-color-neutral--black\<deleted\|relume-variable-color-neutral-1\>);
--text-color--text-alternate<deleted|relume-variable-text-color-3>: var(--base-color-neutral--white\<deleted\|relume-variable-color-neutral-2\>);
--border-color--border-primary<deleted|relume-variable-border-color-1>: var(--base-color-neutral--black\<deleted\|relume-variable-color-neutral-1\>);
--base-color-neutral--white<deleted|relume-variable-color-neutral-2>: white;
--base-color-neutral--dark: black;
--base-color-brand--white: white;
--base-color-neutral--black<deleted|relume-variable-color-neutral-1>: black;
--base-color-neutral--transparent: #fff0;
--base-color-neutral--darker-beige: #c6c3bb;
--background-color--background-secondary<deleted|relume-variable-background-color-2>: var(--base-color-neutral--transparent);
--background-color--background-alternate<deleted|relume-variable-background-color-4>: var(--base-color-neutral--black\<deleted\|relume-variable-color-neutral-1\>);
--link-color--link-alternate<deleted|relume-variable-link-color-3>: var(--base-color-neutral--white\<deleted\|relume-variable-color-neutral-2\>);
--background-color--background-primary<deleted|relume-variable-background-color-1>: var(--base-color-neutral--white\<deleted\|relume-variable-color-neutral-2\>);
--background-color--background-tertiary<deleted|relume-variable-background-color-3>: var(--base-color-neutral--neutral-light\<deleted\|relume-variable-color-neutral-5\>);
--text-color--text-secondary<deleted|relume-variable-text-color-2>: var(--base-color-neutral--black\<deleted\|relume-variable-color-neutral-1\>);
--background-color--background-success<deleted|relume-variable-background-color-6>: var(--base-color-system--success-green-light\<deleted\|relume-variable-system-color-2\>);
--text-color--text-success<deleted|relume-variable-text-color-4>: var(--base-color-system--success-green\<deleted\|relume-variable-system-color-1\>);
--background-color--background-error<deleted|relume-variable-background-color-8>: var(--base-color-system--error-red-light\<deleted\|relume-variable-system-color-6\>);
--text-color--text-error<deleted|relume-variable-text-color-5>: var(--base-color-system--error-red\<deleted\|relume-variable-system-color-5\>);
--base-color-brand--beige: #f1ede5;
--base-color-neutral--light-grey: #6a6a6a;
--base-color-neutral--light-secondary: #fff3;
--base-color-neutral--neutral-light<deleted|relume-variable-color-neutral-5>: #aaa;
--base-color-system--success-green-light<deleted|relume-variable-system-color-2>: #ecfdf3;
--base-color-system--success-green<deleted|relume-variable-system-color-1>: #027a48;
--base-color-system--error-red-light<deleted|relume-variable-system-color-6>: #fef3f2;
--base-color-system--error-red<deleted|relume-variable-system-color-5>: #b42318;
```

### Other

```css
--black-archive<deleted|variable-dccb7db6>: black;
--dark-grey: #383838;
```

### Dependencies

```css
--text-color--text-primary<deleted|relume-variable-text-color-1>: --base-color-neutral--black;
--link-color--link-primary<deleted|relume-variable-link-color-1>: --base-color-neutral--black;
--text-color--text-alternate<deleted|relume-variable-text-color-3>: --base-color-neutral--white;
--border-color--border-primary<deleted|relume-variable-border-color-1>: --base-color-neutral--black;
--background-color--background-secondary<deleted|relume-variable-background-color-2>: --base-color-neutral--transparent;
--background-color--background-alternate<deleted|relume-variable-background-color-4>: --base-color-neutral--black;
--link-color--link-alternate<deleted|relume-variable-link-color-3>: --base-color-neutral--white;
--background-color--background-primary<deleted|relume-variable-background-color-1>: --base-color-neutral--white;
--background-color--background-tertiary<deleted|relume-variable-background-color-3>: --base-color-neutral--neutral-light;
--text-color--text-secondary<deleted|relume-variable-text-color-2>: --base-color-neutral--black;
--background-color--background-success<deleted|relume-variable-background-color-6>: --base-color-system--success-green-light;
--text-color--text-success<deleted|relume-variable-text-color-4>: --base-color-system--success-green;
--background-color--background-error<deleted|relume-variable-background-color-8>: --base-color-system--error-red-light;
--text-color--text-error<deleted|relume-variable-text-color-5>: --base-color-system--error-red;
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
| md | 768px | max-width |
| lg | 991px | max-width |
| lg | 992px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.5s`, `0.25s`

### Common Transitions

```css
transition: all;
transition: background-color 0.5s ease-in-out, color 0.5s ease-in-out;
transition: transform 0.25s ease-in-out, z-index 0.25s ease-in, background-color 0.25s ease-in;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**translateX**
```css
@keyframes translateX {
  100% { transform: translateX(-100%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (13 instances)

```css
.button {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(32, 31, 29);
  font-size: 10.6667px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (12 instances)

```css
.card {
  background-color: rgb(241, 237, 229);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (24 instances)

```css
.input {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(32, 31, 29);
  border-color: rgb(32, 31, 29);
  border-radius: 0px;
  font-size: 10.6667px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (50 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 10.6667px;
  font-weight: 400;
}
```

### Navigation (12 instances)

```css
.navigatio {
  background-color: rgb(0, 0, 0);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (48 instances)

```css
.foote {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 10.6667px;
}
```

### Modals (3 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (9 instances)

```css
.dropdown {
  background-color: rgb(249, 249, 249);
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Badges (4 instances)

```css
.badge {
  color: rgb(32, 31, 29);
  font-size: 14px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 10.6667px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(249, 249, 249);
  padding: 8px 12px 8px 12px;
  border-radius: 640px;
  border: 1px solid rgb(249, 249, 249);
  font-size: 14px;
  font-weight: 400;
```

### Button — 3 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(184, 184, 184);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(184, 184, 184);
  font-size: 10.6667px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(32, 31, 29);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 31, 29);
  font-size: 10.6667px;
  font-weight: 400;
```

### Button — 3 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 8px 12px 8px 12px;
  border-radius: 640px;
  border: 0px none rgb(241, 237, 229);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(249, 249, 249);
  color: rgb(32, 31, 29);
  padding: 8px 12px 8px 12px;
  border-radius: 640px;
  border: 1px solid rgb(249, 249, 249);
  font-size: 14px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 10.6667px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(241, 237, 229);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 4px;
  border: 0px none rgb(0, 0, 0);
  font-size: 10.6667px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 10.6667px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 9.33333px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(0, 0, 0);
  font-size: 10.6667px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(32, 31, 29);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(32, 31, 29);
  font-size: 14px;
  font-weight: 400;
```

## Layout System

**9 grid containers** and **270 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1226.67px | 0px |
| 760px | 0px |
| 4992px | 0px |
| 1013.33px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 3x |
| 1-column | 2x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 124.078px 211.188px 176.172px;
gap: 48px 40px;
grid-template-columns: 14px;
grid-template-columns: 12.4062px;
grid-template-columns: none;
grid-template-columns: 1fr 1fr;
gap: 26.6667px 33.3333px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 145x |
| column/nowrap | 123x |
| row/wrap | 2x |

**Gap values:** `0px 46.6667px`, `10.6667px normal`, `106.667px normal`, `13.3333px normal`, `16px`, `16px normal`, `20px 13.3333px`, `20px normal`, `26.6667px 33.3333px`, `48px 40px`, `53.3333px normal`, `6.66667px`, `6.66667px normal`, `9.6px`, `normal 10.6667px`, `normal 13.3333px`, `normal 26.6667px`, `normal 3.33333px`, `normal 46.6667px`, `normal 6.66667px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 85/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 92/100 |
| Spacing System | 70/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Clean elevation system, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 235 !important rules — prefer specificity over overrides
- 86% of CSS is unused — consider purging
- 4467 duplicate CSS declarations

## Z-Index Map

**10 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,1000 | div.f.o.r.m.-.m.e.n.u, div.l.o.g.i.n.-.m.e.n.u |
| dropdown | 900,950 | div.n.a.v.b.a.r. .n.a.v.b.a.r.-.2. .w.-.n.a.v, div.f.o.r.m.-.m.o.d.a.l, div.l.o.g.i.n.-.m.o.d.a.l |
| sticky | 10,50 | div.h.o.m.e.-.h.e.r.o.-.w.r.a.p, div.h.s.c.r.o.l.l.-.i.m.g.-.c.o.n.t.a.i.n.e.r, h2.h.o.m.e.-.j.o.u.r.n.e.y.-.h.2 |
| base | -100,5 | video, video, video |

## SVG Icons

**11 unique SVG icons** detected. Dominant style: **duo-tone**.

| Size Class | Count |
|------------|-------|
| xs | 5 |
| md | 1 |
| xl | 5 |

**Icon colors:** `rgb(32,31,29)`, `rgb(0, 0, 0)`, `rgb(249,249,249)`, `rgb(0,0,0)`, `rgb(217,217,217)`, `rgb(241,237,229)`, `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| GT Super Display | self-hosted | 300 | normal |
| PP Mori | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 12 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 7 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (9x), 3:4 (5x), 2:3 (2x), 4.66:1 (1x), 4.69:1 (1x), 16:9 (1x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `250ms` | 250 |
| `lg` | `500ms` | 500 |

### Easing Families

- **ease-in-out** (29 uses) — `ease`

## Component Anatomy

### card — 12 instances

**Slots:** heading, media

### button — 9 instances

**Slots:** label, icon
**Variants:** secondary

| variant | count | sample label |
|---|---|---|
| default | 8 | Plan your trip
Members only |
| secondary | 1 | Plan your trip |

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **plan** (4)
- **members** (2)
- **discover** (2)

### Button Copy Patterns

- "members only" (2×)
- "plan your exclusive journey" (2×)
- "discover our story" (2×)
- "plan your trip
members only" (1×)
- "plan your trip" (1×)

### Sample Headings

> Your Exclusive Gateway to Madeira's Hidden Gems
> The Essence of Our Legacy
> Experience Authenticity, Expertise, and Customization on Every Journey
> Local Expertise
> Authentic Experiences

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** Experience the best of Madeira with Insider’s exclusive, custom-crafted itineraries. Enjoy luxury adventures, cultural immersion, and personalized travel support. Create unforgettable memories with be

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → feature-grid → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | feature-grid | Your Exclusive Gateway to Madeira's Hidden Gems | 0.8 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.03 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 15984px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.158)
**Counts:** total 19, svg 11, icon 10, screenshot-like 0, photo-like 6
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `PP Mori` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
