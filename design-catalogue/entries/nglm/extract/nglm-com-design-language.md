# Design Language: NGLM – Bringing Design to the World at Scale

> Extracted from `https://www.nglm.com` on September 4, 2026
> 686 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1012 |
| `#51585c` | hsl(202, 6%, 34%) | 262 |
| `#fcfcfc` | hsl(0, 0%, 99%) | 117 |
| `#c0c3c3` | hsl(180, 2%, 76%) | 33 |
| `#707575` | hsl(180, 2%, 45%) | 6 |
| `#131516` | hsl(200, 7%, 8%) | 1 |

### Background Colors

Used on large-area elements: `#fcfcfc`, `#000000`, `#131516`

### Text Colors

Text color palette: `#000000`, `#fcfcfc`, `#707575`, `#ffffff`, `#51585c`, `#c0c3c3`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 1012 |
| `#51585c` | text, border | 262 |
| `#fcfcfc` | background, text, border | 117 |
| `#c0c3c3` | background, border, text | 33 |
| `#707575` | text, border | 6 |
| `#131516` | background | 1 |

## Typography

### Font Families

- **GD Gaio VF** — used for all (633 elements)
- **GD Trio Display** — used for all (30 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 140.8px | 8.8rem | 400 | 140.8px | normal | div |
| 102.4px | 6.4rem | 400 | 102.4px | normal | div |
| 83.2px | 5.2rem | 400 | 73.216px | -0.832px | h1 |
| 80px | 5rem | 400 | 76.8px | normal | h2, span |
| 56px | 3.5rem | 400 | 53.76px | normal | h3 |
| 28px | 1.75rem | 400 | 30.8px | normal | p, a |
| 18px | 1.125rem | 600 | 21.6px | normal | p |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14px | 0.875rem | 600 | 16.24px | normal | p, a, div, svg |
| 12px | 0.75rem | 600 | 13.44px | normal | div, br, sup, a |

### Heading Scale

```css
h1 { font-size: 83.2px; font-weight: 400; line-height: 73.216px; }
h2 { font-size: 80px; font-weight: 400; line-height: 76.8px; }
h3 { font-size: 56px; font-weight: 400; line-height: 53.76px; }
h3 { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (489x), `600` (136x), `500` (61x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-104 | 104px | 6.5rem |
| spacing-176 | 176px | 11rem |
| spacing-344 | 344px | 21.5rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 47 |

## Box Shadows

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(252, 252, 252) 0px 0px 0px 1px inset;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(0, 0, 0) 0px 0px 0px 1px inset;
```

**sm** — blur: 4px
```css
box-shadow: rgba(0, 0, 0, 0.2) 0px 0px 4px 0px;
```

## CSS Custom Properties

### Colors

```css
--_sematic---background--primary: var(--primary--white);
--_sematic---text--primary: var(--primary--black);
--_sematic---text--secondary: var(--secondary--titanium);
--_sematic---border--transparent: #0000;
--_sematic---border--teitrary: var(--secondary--aluminium);
--secondary--concrete: #707575;
--secondary--aluminium: #c0c3c3;
--primary--white: #fcfcfc;
--_button---button--border-radius: 2px;
--_sematic---background--secondary: var(--secondary--aluminium);
--_sematic---border--primary: var(--primary--black);
--primary--black: black;
--_sematic---border--secondary: var(--secondary--concrete);
--_button---button--bg-hover: var(--secondary--steel);
--secondary--paper: #e9e9e2;
--secondary--steel: #2f3133;
--secondary--titanium: #51585c;
--secondary--leather: #131516;
```

### Spacing

```css
--_ui---margins--scroll-offset: 2.625rem;
--_ui---margins--main: 1rem;
--_ui---margins--gutter: .75rem;
```

### Typography

```css
--_button---button--text-hover: var(--primary--white);
--_sematic---text--teitrary: var(--secondary--concrete);
--_button---button--text: var(--primary--white);
```

### Other

```css
--_state---interaction: 0;
--_button---button--background: var(--primary--black);
--_sematic---background--teitrary: var(--secondary--concrete);
```

### Dependencies

```css
--_sematic---background--primary: --primary--white;
--_sematic---text--primary: --primary--black;
--_sematic---text--secondary: --secondary--titanium;
--_sematic---border--teitrary: --secondary--aluminium;
--_sematic---background--secondary: --secondary--aluminium;
--_sematic---border--primary: --primary--black;
--_sematic---border--secondary: --secondary--concrete;
--_button---button--background: --primary--black;
--_button---button--bg-hover: --secondary--steel;
--_button---button--text-hover: --primary--white;
--_sematic---text--teitrary: --secondary--concrete;
--_button---button--text: --primary--white;
--_sematic---background--teitrary: --secondary--concrete;
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

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.45s`, `0.4s`, `0.3s`, `0.6s`, `0.55s`, `0.5s`

### Common Transitions

```css
transition: all;
transition: color 0.45s cubic-bezier(0.455, 0.03, 0.515, 0.955);
transition: color 0.4s cubic-bezier(0.515, 0.012, 0.25, 1), border-radius 0.4s, background-color 0.4s;
transition: 0.45s cubic-bezier(0.455, 0.03, 0.515, 0.955);
transition: background-color 0.45s cubic-bezier(0.455, 0.03, 0.515, 0.955);
transition: background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
transition: transform 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
transition: none 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
transition: padding 0.55s cubic-bezier(0.645, 0.045, 0.355, 1);
transition: opacity 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
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

### Buttons (18 instances)

```css
.button {
  background-color: rgb(0, 0, 0);
  color: rgb(252, 252, 252);
  font-size: 14px;
  font-weight: 500;
  padding-top: 12px;
  padding-right: 16px;
  border-radius: 2px;
}
```

### Cards (4 instances)

```css
.card {
  background-color: rgb(252, 252, 252);
  border-radius: 2px;
  box-shadow: rgba(0, 0, 0, 0.2) 0px 0px 4px 0px;
  padding-top: 14px;
  padding-right: 4px;
}
```

### Links (84 instances)

```css
.link {
  color: rgb(81, 88, 92);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (20 instances)

```css
.navigatio {
  background-color: rgb(252, 252, 252);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (19 instances)

```css
.foote {
  background-color: rgb(0, 0, 0);
  color: rgb(192, 195, 195);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (7 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 100%;
}
```

### Dropdowns (82 instances)

```css
.dropdown {
  background-color: rgb(252, 252, 252);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.2) 0px 0px 4px 0px;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Switches (4 instances)

```css
.switche {
  border-radius: 2px;
  border-color: rgb(0, 0, 0);
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
  font-size: 16px;
  font-weight: 400;
```

### Button — 14 instances, 3 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 4px 0px 4px 0px;
  border-radius: 2px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 500;
```

**Variant 2** (1 instance)

```css
  background: rgb(252, 252, 252);
  color: rgb(0, 0, 0);
  padding: 12px 16px 12px 16px;
  border-radius: 2px;
  border: 0px none rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 500;
```

**Variant 3** (12 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(252, 252, 252);
  padding: 12px 16px 12px 16px;
  border-radius: 2px;
  border: 0px none rgb(252, 252, 252);
  font-size: 14px;
  font-weight: 500;
```

## Layout System

**15 grid containers** and **167 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1280px | 0px |
| 1011.2px | 0px |
| 100% | 0px |
| 717.188px | 0px |
| 986.364px | 0px |
| 1434.38px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 16-column | 13x |
| 3-column | 1x |
| 6-column | 1x |

### Grid Templates

```css
grid-template-columns: 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px;
gap: 12px;
grid-template-columns: 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px 68.75px;
gap: 12px;
grid-template-columns: 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px;
gap: 12px;
grid-template-columns: 408px 408px 408px;
gap: 12px;
grid-template-columns: 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px 66.75px;
gap: 12px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 60x |
| column/nowrap | 107x |

**Gap values:** `12px`, `16px`, `24px`, `2px`, `32px`, `40px`, `48px`, `4px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 13 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#fcfcfc` | `#000000` | 20.47:1 | AAA |
| `#000000` | `#fcfcfc` | 20.47:1 | AAA |

## Design System Score

**Overall: 91/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 85/100 |
| Typography Consistency | 92/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- No clear primary brand color detected
- 42 !important rules — prefer specificity over overrides
- 85% of CSS is unused — consider purging
- 3934 duplicate CSS declarations

## Z-Index Map

**9 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9999,9999 | div.c.o.o.k.i.e.-.c.o.n.-.w.r.a.p.p.e.r |
| dropdown | 900,999 | div.t.o.p.n.a.v.-.d.r.o.p.d.o.w.n. .w.-.d.r.o.p.d.o.w.n, div.t.o.p.n.a.v.-.d.r.o.p.d.o.w.n. .w.-.d.r.o.p.d.o.w.n, div.t.o.p.n.a.v.-.d.r.o.p.d.o.w.n. .w.-.d.r.o.p.d.o.w.n |
| sticky | 10,10 | div.d.r.o.p.d.o.w.n._.o.p.e.n._.l.i.s.t, div.d.r.o.p.d.o.w.n._.o.p.e.n._.l.i.s.t, div.d.r.o.p.d.o.w.n._.o.p.e.n._.l.i.s.t |
| base | -1,3 | div.c.m.s._.c.o.m.p.a.n.y._.h.e.r.o, div.c.m.s._.c.o.m.p.a.n.y._.h.e.r.o, div.c.m.s._.c.o.m.p.a.n.y._.h.e.r.o |

## SVG Icons

**2 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| xl | 1 |

**Icon colors:** `black`, `inherit`, `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| GD Trio Display | self-hosted | 400 | normal |
| GD Gaio VF | self-hosted | 400 900 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 35 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 9 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 3 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (30x), 3:2 (8x), 4.89:1 (3x), 11.9:1 (1x), 5.06:1 (1x), 8.72:1 (1x), 5.8:1 (1x), 2:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `300ms` | 300 |
| `lg` | `450ms` | 450 |

### Easing Families

- **custom** (95 uses) — `cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `cubic-bezier(0.515, 0.012, 0.25, 1)`, `cubic-bezier(0.645, 0.045, 0.355, 1)`
- **ease-out** (40 uses) — `cubic-bezier(0.165, 0.84, 0.44, 1)`, `cubic-bezier(0.215, 0.61, 0.355, 1)`

## Component Anatomy

### button — 15 instances

**Slots:** label
**Variants:** link

| variant | count | sample label |
|---|---|---|
| default | 14 | Decline
Accept |
| link | 1 | Decline |

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Title Case (tight)

### Top CTA Verbs

- **read** (7)
- **decline** (2)
- **learn** (2)
- **accept** (1)
- **about** (1)
- **see** (1)
- **contact** (1)

### Button Copy Patterns

- "read more" (7×)
- "decline
accept" (1×)
- "decline" (1×)
- "accept" (1×)
- "about us" (1×)
- "learn more about our talent" (1×)
- "see all news" (1×)
- "learn more about our model" (1×)
- "contact us" (1×)

### Sample Headings

> BUILDING THE NEXT GENERATION OF DESIGN COMPANIES
> Nordiska Galleriet
> Länna Möbler
> Yllw
> Dusty Deco
> KA YO
> KEY FIGURES
> CREATIVES &
ENTREPRENEURS
> PRESS: LATEST
FROM THE GROUP
> CREATING A GLOBAL DESIGN POWERHOUSE THROUGH INDEPENDENCE AND ENTREPRENEURSHIP

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** NGLM is building a global design powerhouse through entrepreneurial independence. Portfolio includes Nordiska Galleriet, Länna Möbler, Yllw, and more.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → nav → nav → nav → testimonial → testimonial → content → content → hero → testimonial → cta → hero → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | nav | — | 0.9 |
| 5 | testimonial | BUILDING THE NEXT GENERATION OF DESIGN COMPANIES | 0.8 |
| 6 | testimonial | Nordiska Galleriet | 0.8 |
| 7 | content | KEY FIGURES | 0.3 |
| 8 | content | — | 0.3 |
| 9 | hero | CREATIVES &
ENTREPRENEURS | 0.4 |
| 10 | testimonial | PRESS: LATEST
FROM THE GROUP | 0.8 |
| 11 | cta | CREATING A GLOBAL DESIGN POWERHOUSE THROUGH INDEPENDENCE AND ENTREPRENEURSHIP | 0.75 |
| 12 | hero | BRINGING DESIGN TO THE
WORLD AT SCALE | 0.4 |
| 13 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.052 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 2px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.436)
**Counts:** total 47, svg 8, icon 2, screenshot-like 0, photo-like 39
**Dominant aspect:** portrait
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.499)

Evidence:
- tailwind-like class density 52%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `GD Gaio VF` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
