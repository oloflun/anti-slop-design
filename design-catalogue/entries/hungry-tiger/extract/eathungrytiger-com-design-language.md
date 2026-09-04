# Design Language: Hungry Tiger — Bold Indian Sauces Made for Real Life

> Extracted from `https://www.eathungrytiger.com/` on September 4, 2026
> 1339 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#faae33` | rgb(250, 174, 51) | hsl(37, 95%, 59%) | 1724 |
| Secondary | `#402011` | rgb(64, 32, 17) | hsl(19, 58%, 16%) | 946 |
| Accent | `#ffdede` | rgb(255, 222, 222) | hsl(0, 100%, 94%) | 3 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 62 |
| `#ffffff` | hsl(0, 0%, 100%) | 48 |
| `#dddddd` | hsl(0, 0%, 87%) | 1 |

### Background Colors

Used on large-area elements: `#823513`, `#281006`, `#faae33`, `#402011`, `#000000`

### Text Colors

Text color palette: `#000000`, `#faae33`, `#402011`, `#ffffff`, `#f7ac32`

### Gradients

```css
background-image: repeating-radial-gradient(circle, rgb(247, 172, 50) 0px, rgb(247, 172, 50) 2px, rgba(0, 0, 0, 0) 2px, rgba(0, 0, 0, 0) 10px);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#faae33` | text, border, background | 1724 |
| `#402011` | text, border, background | 946 |
| `#000000` | text, border, background | 62 |
| `#ffffff` | text, border | 48 |
| `#823513` | background | 13 |
| `#ffdede` | background | 3 |
| `#281006` | background | 3 |
| `#d1255c` | background | 3 |
| `#dddddd` | background | 1 |

## Typography

### Font Families

- **Salmond** — used for all (1270 elements)
- **Graphikx** — used for body (42 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 189.44px | 11.84rem | 700 | 151.552px | -3.7888px | h1 |
| 173.44px | 10.84rem | 700 | 173.44px | -1.7344px | div |
| 128px | 8rem | 700 | 115.2px | -2.56px | h2, span |
| 115.2px | 7.2rem | 700 | 103.68px | -1.8432px | h2, span, br |
| 89.6px | 5.6rem | 700 | 78.848px | -1.4336px | h2, span, br |
| 64px | 4rem | 700 | 57.6px | -1.28px | div |
| 60.16px | 3.76rem | 700 | 55.9488px | -0.6016px | div, span |
| 57.6px | 3.6rem | 700 | 51.84px | -0.288px | h3, span, br |
| 40.32px | 2.52rem | 700 | 36.288px | -0.8064px | div |
| 38.4px | 2.4rem | 500 | 26.88px | -0.384px | div, span |
| 37.12px | 2.32rem | 700 | 35.264px | -0.3712px | div |
| 35.84px | 2.24rem | 700 | 35.84px | -0.7168px | div |
| 27.52px | 1.72rem | 700 | 24.768px | -0.5504px | div, br |
| 25.6px | 1.6rem | 700 | 25.6px | -0.256px | h3 |
| 19.2px | 1.2rem | 500 | 26.88px | normal | div |

### Heading Scale

```css
h1 { font-size: 189.44px; font-weight: 700; line-height: 151.552px; }
h2 { font-size: 128px; font-weight: 700; line-height: 115.2px; }
h2 { font-size: 115.2px; font-weight: 700; line-height: 103.68px; }
h2 { font-size: 89.6px; font-weight: 700; line-height: 78.848px; }
h3 { font-size: 57.6px; font-weight: 700; line-height: 51.84px; }
h3 { font-size: 25.6px; font-weight: 700; line-height: 25.6px; }
```

### Body Text

```css
body { font-size: 115.2px; font-weight: 700; line-height: 103.68px; }
```

### Font Weights in Use

`500` (1057x), `700` (254x), `400` (28x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-23 | 23px | 1.4375rem |
| spacing-28 | 28px | 1.75rem |
| spacing-42 | 42px | 2.625rem |
| spacing-51 | 51px | 3.1875rem |
| spacing-61 | 61px | 3.8125rem |
| spacing-100 | 100px | 6.25rem |
| spacing-112 | 112px | 7rem |
| spacing-122 | 122px | 7.625rem |
| spacing-128 | 128px | 8rem |
| spacing-154 | 154px | 9.625rem |
| spacing-172 | 172px | 10.75rem |
| spacing-178 | 178px | 11.125rem |
| spacing-192 | 192px | 12rem |
| spacing-245 | 245px | 15.3125rem |
| spacing-256 | 256px | 16rem |
| spacing-272 | 272px | 17rem |
| spacing-296 | 296px | 18.5rem |
| spacing-306 | 306px | 19.125rem |
| spacing-448 | 448px | 28rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 5px | 3 |
| md | 8px | 3 |
| lg | 12px | 1 |
| full | 100px | 94 |
| full | 960px | 9 |
| full | 1024px | 8 |
| full | 1088px | 6 |
| full | 1152px | 7 |
| full | 1280px | 2 |

## CSS Custom Properties

### Colors

```css
--primary: #faae33;
```

### Other

```css
--dark-brown: #402011;
--brown: #823513;
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

**Durations:** `0.4s`, `1.5s`, `0.6s`, `0.45s`

### Common Transitions

```css
transition: all;
transition: 0.4s;
transition: 1.5s;
transition: 0.6s;
transition: 0.45s;
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

### Buttons (9 instances)

```css
.button {
  background-color: rgb(250, 174, 51);
  color: rgb(64, 32, 17);
  font-size: 10.24px;
  font-weight: 500;
  padding-top: 20px;
  padding-right: 32px;
  border-radius: 1024px;
}
```

### Cards (3 instances)

```css
.card {
  background-color: rgb(250, 174, 51);
  border-radius: 6px;
  padding-top: 14px;
  padding-right: 14px;
}
```

### Inputs (5 instances)

```css
.input {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(250, 174, 51);
  border-color: rgb(250, 174, 51);
  border-radius: 1088px;
  font-size: 12.8px;
  padding-top: 16px;
  padding-right: 16px;
}
```

### Links (45 instances)

```css
.link {
  color: rgb(64, 32, 17);
  font-size: 11.52px;
  font-weight: 500;
}
```

### Navigation (10 instances)

```css
.navigatio {
  color: rgb(250, 174, 51);
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
  background-color: rgb(40, 16, 6);
  color: rgb(250, 174, 51);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12.8px;
}
```

### Modals (33 instances)

```css
.modal {
  background-color: rgb(64, 32, 17);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 520px;
}
```

### Dropdowns (17 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(250, 174, 51);
  padding-top: 0px;
}
```

### Badges (8 instances)

```css
.badge {
  background-color: rgb(130, 53, 19);
  color: rgb(250, 174, 51);
  font-size: 9.6px;
  font-weight: 500;
  padding-top: 12px;
  padding-right: 12px;
  border-radius: 960px;
}
```

### Tabs (6 instances)

```css
.tab {
  background-color: rgb(64, 32, 17);
  color: rgb(250, 174, 51);
  font-size: 12.8px;
  font-weight: 500;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(250, 174, 51);
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgb(250, 174, 51);
  color: rgb(64, 32, 17);
  padding: 0px 15.552px 0px 15.552px;
  border-radius: 1152px;
  border: 0px none rgb(64, 32, 17);
  font-size: 11.52px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(250, 174, 51);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(250, 174, 51);
  font-size: 12.8px;
  font-weight: 500;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(56, 152, 236, 0);
  color: rgba(255, 255, 255, 0);
  padding: 9px 15px 9px 15px;
  border-radius: 100%;
  border: 0px outset rgb(0, 0, 0);
  font-size: 12.8px;
  font-weight: 500;
```

**Variant 2** (1 instance)

```css
  background: rgb(64, 32, 17);
  color: rgb(250, 174, 51);
  padding: 16px 42px 12px 42px;
  border-radius: 1152px;
  border: 0px none rgb(250, 174, 51);
  font-size: 11.52px;
  font-weight: 500;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(64, 32, 17);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(64, 32, 17);
  font-size: 10.24px;
  font-weight: 700;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(250, 174, 51);
  color: rgb(250, 174, 51);
  padding: 14px 14px 32px 14px;
  border-radius: 6px;
  border: 0px none rgb(250, 174, 51);
  font-size: 12.8px;
  font-weight: 500;
```

### Input — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(64, 32, 17);
  padding: 16px 16px 12px 20px;
  border-radius: 1088px;
  border: 1px solid rgba(64, 32, 17, 0.35);
  font-size: 10.88px;
  font-weight: 500;
```

## Layout System

**15 grid containers** and **292 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 8x |
| 3-column | 4x |
| 4-column | 3x |

### Grid Templates

```css
grid-template-columns: 408px 408px 408px;
grid-template-columns: 397.328px 397.328px 397.344px;
gap: 16px;
grid-template-columns: 397.328px 397.328px 397.344px;
gap: 16px;
grid-template-columns: 290px 290px;
gap: 4px;
grid-template-columns: 152.531px 152.531px 152.531px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 163x |
| column/nowrap | 129x |

**Gap values:** `10px`, `12px`, `14px`, `16px`, `16px 12px`, `20px`, `28px`, `2px`, `4px`, `6px`, `8px 6px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#faae33` | `#402011` | 7.79:1 | AAA |

## Design System Score

**Overall: 85/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 90/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance

**Issues:**
- 24 distinct font sizes — consider a tighter type scale
- 42 !important rules — prefer specificity over overrides
- 83% of CSS is unused — consider purging
- 3535 duplicate CSS declarations

## Gradients

**1 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| repeating-radial | circle | 4 | bold |

```css
background: repeating-radial-gradient(circle, rgb(247, 172, 50) 0px, rgb(247, 172, 50) 2px, rgba(0, 0, 0, 0) 2px, rgba(0, 0, 0, 0) 10px);
```

## Z-Index Map

**13 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1001,1001 | div.w.-.c.o.m.m.e.r.c.e.-.c.o.m.m.e.r.c.e.c.a.r.t.c.o.n.t.a.i.n.e.r.w.r.a.p.p.e.r. .w.-.c.o.m.m.e.r.c.e.-.c.o.m.m.e.r.c.e.c.a.r.t.c.o.n.t.a.i.n.e.r.w.r.a.p.p.e.r.-.-.c.a.r.t.T.y.p.e.-.r.i.g.h.t.D.r.o.p.d.o.w.n. .c.a.r.t._.c.o.n.t.a.i.n.e.r |
| dropdown | 100,999 | section.i.n.s.i.d.e._.s.i.d.e.s, section.t.r.a.d.i.t.i.o.n.s, section.f.u.l.l.s.i.z.e |
| sticky | 10,99 | div.w.r.a.p.p.e.r._.h.e.r.o, div.b.u.y._.n.o.w._.l.i.n.k, div.a.n.g.l.e._.p.a.r.t |
| base | 1,5 | div.b.a.c.k._.c.o.l.o.r._.b.u.t.t.o.n, div.b.a.c.k._.c.o.l.o.r._.b.u.t.t.o.n, div.b.a.c.k.g.r.o.u.n.d._.g.r.a.i.n |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| Salmond | self-hosted | 500, 700 | normal |
| Graphikx | self-hosted | 500 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 14 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 6 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 4 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (10x), 4:3 (7x), 7.12:1 (3x), 2:3 (2x), 1.16:1 (1x), 3:4 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `400ms` | 400 |
| `lg` | `450ms` | 450 |
| `xxl` | `1.5s` | 1500 |

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `spin` | rotate | transform | 1 |

## Component Anatomy

### button — 12 instances

**Slots:** label, icon

### card — 3 instances

**Slots:** media

### input — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **buy** (7)
- **all** (2)
- **this** (1)

### Button Copy Patterns

- "buy now" (7×)
- "all recipes" (2×)
- "this product is out of stock.product is not available in this quantity." (1×)

### Sample Headings

> BOLD FLAVOR
> A NEW ANGLE
OF FLAVOR
> UNWRAP THE ADVENTURE
> A NEW PERSPECTIVE
ON TASTE
> WHAT'S
INSIDE
> TRADITION
& CREATION
> WHY THE JAR
MATTERS
> UNLOCK THE
MAGIC INSIDE
THE JAR
> LET'S GET
COOKING
> EASY CHICKEN TANDOORI

## Page Intent

**Type:** `landing` (confidence 0.59)
**Description:** Bold Indian-inspired sauces made for real life. No shortcuts, no fillers — just deep flavor crafted with heart. Discover the taste of Hungry Tiger.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → testimonial → content → testimonial → hero → content → content → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | testimonial | BOLD FLAVOR | 0.8 |
| 2 | content | WHAT'S
INSIDE | 0.3 |
| 3 | testimonial | TRADITION
& CREATION | 0.8 |
| 4 | hero | UNLOCK THE
MAGIC INSIDE
THE JAR | 0.4 |
| 5 | content | LET'S GET
COOKING | 0.3 |
| 6 | content | — | 0.3 |
| 7 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.465 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 1280px |
| backdrop-filter in use | no |
| Gradients | 1 |

## Imagery Style

**Label:** `photography` (confidence 0.312)
**Counts:** total 24, svg 1, icon 12, screenshot-like 0, photo-like 13
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Salmond` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
