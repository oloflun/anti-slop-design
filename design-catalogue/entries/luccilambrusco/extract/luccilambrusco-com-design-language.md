# Design Language: Home | Lucci Lambrusco

> Extracted from `https://www.luccilambrusco.com` on September 4, 2026
> 310 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#efecce` | rgb(239, 236, 206) | hsl(55, 51%, 87%) | 537 |
| Secondary | `#b83529` | rgb(184, 53, 41) | hsl(5, 64%, 44%) | 58 |
| Accent | `#dcd69d` | rgb(220, 214, 157) | hsl(54, 47%, 74%) | 2 |

### Background Colors

Used on large-area elements: `#b83529`, `#efecce`

### Text Colors

Text color palette: `#efecce`, `#b83529`, `#dcd69d`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#efecce` | text, border, background | 537 |
| `#b83529` | background, text, border | 58 |
| `#dcd69d` | text, border | 2 |

## Typography

### Font Families

- **ABC Solar** — used for body (242 elements)
- **ABC Ginto Nord Condensed** — used for all (29 elements)
- **ABC Solar Semibold** — used for body (22 elements)
- **Flatface Script** — used for body (17 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 128px | 8rem | 700 | 96px | -5.12px | h1, span |
| 48px | 3rem | 700 | 40.8px | -1.44px | h3, span |
| 36px | 2.25rem | 700 | 32.4px | -1.08px | h4, span, a |
| 32px | 2rem | 400 | 48px | 0.32px | div, span |
| 28px | 1.75rem | 700 | 25.2px | -0.84px | input |
| 16px | 1rem | 400 | 20px | -0.16px | div, span, button, a |
| 14px | 0.875rem | 400 | 17.5px | 0.14px | input, div, a |
| 10px | 0.625rem | 400 | 15px | normal | html, head, meta, link |

### Heading Scale

```css
h1 { font-size: 128px; font-weight: 700; line-height: 96px; }
h3 { font-size: 48px; font-weight: 700; line-height: 40.8px; }
h4 { font-size: 36px; font-weight: 700; line-height: 32.4px; }
```

### Body Text

```css
body { font-size: 32px; font-weight: 400; line-height: 48px; }
```

### Font Weights in Use

`400` (259x), `700` (29x), `600` (22x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-20 | 20px | 1.25rem |
| spacing-32 | 32px | 2rem |
| spacing-40 | 40px | 2.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-240 | 240px | 15rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 10px | 2 |
| xl | 20px | 11 |
| full | 50px | 7 |

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-color: #fff;
--tw-ring-offset-shadow: 0 0 #0000;
--color-white: #fff;
--tw-ring-shadow: 0 0 #0000;
--tw-border-style: solid;
--color-error: red;
--color-pageBg: #b83529;
--tw-ring-offset-width: 0px;
--color-primary: #b83529;
--color-pageText: #efecce;
--color-black: #000;
--tw-inset-ring-shadow: 0 0 #0000;
--color-secondary: #efecce;
```

### Spacing

```css
--spacing: .1rem;
--tw-space-y-reverse: 0;
```

### Typography

```css
--font-sans: "ABC Solar","sans-serif";
--font-weight-bold: 700;
--font-body-semibold: "ABC Solar Semibold","arial","sans-serif";
--font-body: "ABC Solar","arial","sans-serif";
--text-sm--line-height: 1.42857;
--font-script: "Flatface Script","cursive";
--default-font-family: "ABC Solar","sans-serif";
--font-weight-normal: 400;
--font-mono: "courier","monospace";
--text-xl--line-height: 1.4;
--font-weight-semibold: 600;
--text-xl: 1.25rem;
--text-sm: .875rem;
--font-heading: "ABC Ginto Nord Condensed","serif";
--default-mono-font-family: "courier","monospace";
```

### Shadows

```css
--tw-inset-shadow-alpha: 100%;
--tw-shadow-alpha: 100%;
--tw-drop-shadow-alpha: 100%;
--tw-shadow: 0 0 #0000;
--tw-inset-shadow: 0 0 #0000;
```

### Radii

```css
--radius-2xl: 1rem;
```

### Other

```css
--tw-scale-z: 1;
--default-transition-timing-function: cubic-bezier(.4,0,.2,1);
--tw-translate-x: 0;
--tw-outline-style: solid;
--tw-scale-x: 1;
--tw-translate-z: 0;
--tw-scale-y: 1;
--default-transition-duration: .15s;
--tw-translate-y: 0;
--ease-in-out: cubic-bezier(.4,0,.2,1);
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

**Durations:** `0.5s`, `0.3s`, `0.1s`, `0.2s`, `0.15s`

### Common Transitions

```css
transition: all;
transition: color 0.5s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), fill 0.5s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.5s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1) 0.1s;
transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.2s linear;
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
```

### Keyframe Animations

**marqyL**
```css
@keyframes marqyL {
  0% { transform: translate(0px); }
  100% { transform: translate(-100%); }
}
```

**marqyR**
```css
@keyframes marqyR {
  0% { transform: translate(0px); }
  100% { transform: translate(100%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (9 instances)

```css
.button {
  color: rgb(239, 236, 206);
  font-size: 16px;
  font-weight: 400;
  padding-top: 13px;
  padding-right: 32px;
  border-radius: 50%;
}
```

### Inputs (4 instances)

```css
.input {
  color: rgb(184, 53, 41);
  border-color: rgb(184, 53, 41);
  border-radius: 0px;
  font-size: 28px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (25 instances)

```css
.link {
  color: rgb(239, 236, 206);
  font-size: 10px;
  font-weight: 400;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(184, 53, 41);
  color: rgb(239, 236, 206);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 10px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(184, 53, 41);
  padding: 13px 32px 13px 32px;
  border-radius: 50%;
  border: 1px solid rgb(184, 53, 41);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 236, 206);
  padding: 0px 10px 0px 10px;
  border-radius: 0px;
  border: 0px solid rgb(239, 236, 206);
  font-size: 10px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(239, 236, 206);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(239, 236, 206);
  font-size: 14px;
  font-weight: 400;
```

## Layout System

**12 grid containers** and **32 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 11x |
| 6-column | 1x |

### Grid Templates

```css
grid-template-columns: 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px;
gap: normal 20px;
grid-template-columns: 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6719px 81.6562px 81.6562px 81.6562px 81.6562px;
gap: normal 20px;
grid-template-columns: 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px 81.6562px;
gap: normal 20px;
grid-template-columns: 88.3281px 88.3281px 88.3281px 88.3281px 88.3281px 88.3281px 88.3281px 88.3281px 88.3281px 88.3281px 88.3281px 88.3281px;
gap: normal 20px;
grid-template-columns: 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px 106.656px;
gap: normal 0px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 7x |
| row/nowrap | 25x |

**Gap values:** `normal 0px`, `normal 10px`, `normal 20px`, `normal 32px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 88/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 5 !important rules — prefer specificity over overrides
- 533 duplicate CSS declarations

## Z-Index Map

**5 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,99999 | div.s.c.-.e.q.Y.a.t.C. .e.P.i.p.z.y, section.o.v.e.r.f.l.o.w.-.h.i.d.d.e.n. .b.g.-.s.e.c.o.n.d.a.r.y. .t.e.x.t.-.p.r.i.m.a.r.y. .f.i.x.e.d. .i.n.s.e.t.-.0. .s.i.t.e.-.g.r.i.d.-.c.o.n.t.a.i.n.e.r. .p.y.-.2.4. .p.x.-.2.0. .s.m.:.p.x.-.4.0. .z.-.[.9.9.9.9.9.] |
| dropdown | 999,999 | div.h.i.d.d.e.n. .s.m.:.f.i.x.e.d. .s.m.:.t.o.p.-.0. .s.m.:.l.e.f.t.-.0. .s.m.:.r.i.g.h.t.-.0. .s.m.:.s.i.t.e.-.g.r.i.d.-.c.o.n.t.a.i.n.e.r. .s.e.c.t.i.o.n.-.x.-.s.p.a.c.i.n.g. .p.y.-.1.0. .s.m.:.p.y.-.2.0. .t.e.x.t.-.p.a.g.e.T.e.x.t. .z.-.[.9.9.9.]. .p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e, div.p.y.-.1.0. .p.x.-.4.0. .b.o.r.d.e.r.-.1. .r.o.u.n.d.e.d.-.2.x.l. .t.r.a.n.s.i.t.i.o.n.-.a.l.l. .d.u.r.a.t.i.o.n.-.3.0.0. .d.e.l.a.y.-.1.0.0. .e.a.s.e.-.i.n.-.o.u.t. .f.l.e.x. .i.t.e.m.s.-.c.e.n.t.e.r. .g.a.p.-.x.-.3.2. .z.-.[.9.9.9.]. .p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.a.u.t.o. .b.g.-.p.a.g.e.B.g./.0. .b.o.r.d.e.r.-.t.r.a.n.s.p.a.r.e.n.t, div.s.m.:.h.i.d.d.e.n. .f.i.x.e.d. .t.o.p.-.1.6. .l.e.f.t.-.2.0. .r.i.g.h.t.-.2.0. .s.i.t.e.-.g.r.i.d.-.c.o.n.t.a.i.n.e.r. .p.y.-.1.0. .p.x.-.1.0. .z.-.[.9.9.9.]. .b.o.r.d.e.r.-.1. .r.o.u.n.d.e.d.-.2.x.l. .t.r.a.n.s.i.t.i.o.n.-.a.l.l. .d.u.r.a.t.i.o.n.-.3.0.0. .t.e.x.t.-.p.a.g.e.T.e.x.t. .b.o.r.d.e.r.-.t.r.a.n.s.p.a.r.e.n.t. .b.g.-.p.a.g.e.B.g./.0 |
| sticky | 10,10 | span, div.a.b.s.o.l.u.t.e. .p.x.-.2.0. .w.-.f.u.l.l. .s.m.:.w.-.1./.2. .l.e.f.t.-.1./.2. .-.t.r.a.n.s.l.a.t.e.-.x.-.1./.2. .t.o.p.-.1./.2. .-.t.r.a.n.s.l.a.t.e.-.y.-.1./.2. .z.-.1.0. .t.e.x.t.-.c.e.n.t.e.r, span |
| base | 0,0 | button.m.t.-.2.0. .b.t.n.-.p.r.i.m.a.r.y. .a.l.t. .t.e.x.t.-.b.o.d.y. .t.e.x.t.-.h.5, a.b.t.n.-.p.r.i.m.a.r.y. .i.n.l.i.n.e.-.b.l.o.c.k. .m.t.-.2.0, a.b.t.n.-.p.r.i.m.a.r.y. .a.l.t. .i.n.l.i.n.e.-.b.l.o.c.k. .m.t.-.2.0 |

**Issues:**
- [object Object]

## SVG Icons

**2 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| xl | 1 |

**Icon colors:** `#EFECCE`, `rgb(0, 0, 0)`, `currentColor`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 8 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (12x), 3:2 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **custom** (23 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **linear** (13 uses) — `linear`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `marqyL` | slide | transform | 2 |

## Component Anatomy

### button — 2 instances

**Slots:** label
**Variants:** primary

| variant | count | sample label |
|---|---|---|
| primary | 1 | ENTER |
| default | 1 | Arrow |

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **enter** (1)
- **arrow** (1)

### Button Copy Patterns

- "enter" (1×)
- "arrow" (1×)

### Sample Headings

> WE TRUST YOU BUT STILL NEED TO CHECK
> MEET THE DRY SPARKLING RED WINE, CRAFTED IN EMILIA-ROMAGNA, ITALY
> BUBBLY.BALANCED.FRUIT-FORWARD.
> FALL IN LOVE WITH LAMBRUSCO
> MEET THE WOMAN BEHIND THE BUBBLES
> FOREVERYOCCASION.ORNONEATALL.
> MEET THE DRY SPARKLING RED WINE, CRAFTED IN EMILIA-ROMAGNA, ITALY
> BUBBLY.BALANCED.FRUIT-FORWARD.
> FALL IN LOVE WITH LAMBRUSCO
> MEET THE WOMAN BEHIND THE BUBBLES

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** Co-founded by Ashley Graham, Lucci Lambrusco is a dry sparkling red wine crafted in Emilia-Romagna, Italy. Enjoy responsibly.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): hero → content → testimonial → hero → content → content → content → testimonial → content → testimonial → feature-grid → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | hero | WE TRUST YOU BUT STILL NEED TO CHECK | 0.85 |
| 1 | content | — | 0.3 |
| 2 | testimonial | MEET THE DRY SPARKLING RED WINE, CRAFTED IN EMILIA-ROMAGNA, ITALY | 0.8 |
| 3 | hero | MEET THE DRY SPARKLING RED WINE, CRAFTED IN EMILIA-ROMAGNA, ITALY | 0.85 |
| 4 | content | BUBBLY.BALANCED.FRUIT-FORWARD. | 0.3 |
| 5 | content | FALL IN LOVE WITH LAMBRUSCO | 0.3 |
| 6 | content | — | 0.3 |
| 7 | testimonial | MEET THE WOMAN BEHIND THE BUBBLES | 0.8 |
| 8 | content | FOREVERYOCCASION.ORNONEATALL. | 0.3 |
| 9 | testimonial | — | 0.8 |
| 10 | feature-grid | — | 0.8 |
| 11 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.401 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.115)
**Counts:** total 13, svg 0, icon 0, screenshot-like 0, photo-like 3
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.684)

Evidence:
- tailwind-like class density 67%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `ABC Solar` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
