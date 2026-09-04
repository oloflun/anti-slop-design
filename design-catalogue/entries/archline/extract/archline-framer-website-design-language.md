# Design Language: Archline® | Interior & Architecture Studio

> Extracted from `https://archline.framer.website/` on September 4, 2026
> 2230 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fffcf3` | rgb(255, 252, 243) | hsl(45, 100%, 98%) | 330 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 728 |
| Accent | `#33261f` | rgb(51, 38, 31) | hsl(21, 24%, 16%) | 7 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 2190 |
| `#252324` | hsl(330, 3%, 14%) | 1313 |

### Background Colors

Used on large-area elements: `#000000`, `#fffdfa`, `#252324`, `#fffcf3`, `#faf2df`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#fffcf3`, `#252324`, `#33261f`, `#faf2df`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 2190 |
| `#252324` | text, border, background | 1313 |
| `#0000ee` | text, border | 728 |
| `#fffcf3` | text, border, background | 330 |
| `#33261f` | text, border, background | 7 |
| `#faf2df` | background, text, border | 3 |

## Typography

### Font Families

- **Inter Display** — used for all (698 elements)
- **Times New Roman** — used for body (28 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 100px | 6.25rem | 400 | 70px | -0.2px | div |
| 72px | 4.5rem | 500 | 82.8px | -0.3px | h1, span |
| 64px | 4rem | 400 | normal | normal | div, span |
| 40px | 2.5rem | 400 | 52px | -0.1px | h2, div |
| 32px | 2rem | 400 | 44.8px | -0.1px | h4 |
| 28px | 1.75rem | 400 | 39.2px | -0.2px | p |
| 24px | 1.5rem | 400 | normal | normal | p, span |
| 20px | 1.25rem | 400 | 28px | normal | p |
| 18.08px | 1.13rem | 500 | 25.312px | normal | p |
| 16px | 1rem | 400 | normal | normal | html, head, meta, script |
| 14.08px | 0.88rem | 500 | 18.304px | normal | p, a |
| 12.96px | 0.81rem | 500 | 16.848px | normal | p |
| 12px | 0.75rem | 400 | normal | normal | body, script, div, style |

### Heading Scale

```css
h1 { font-size: 72px; font-weight: 500; line-height: 82.8px; }
h2 { font-size: 40px; font-weight: 400; line-height: 52px; }
h4 { font-size: 32px; font-weight: 400; line-height: 44.8px; }
```

### Body Text

```css
body { font-size: 24px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (1894x), `500` (316x), `600` (20x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-120 | 120px | 7.5rem |
| spacing-136 | 136px | 8.5rem |
| spacing-150 | 150px | 9.375rem |
| spacing-156 | 156px | 9.75rem |
| spacing-164 | 164px | 10.25rem |
| spacing-200 | 200px | 12.5rem |
| spacing-240 | 240px | 15rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 1 |
| md | 8px | 1 |
| lg | 11px | 2 |
| full | 40px | 3 |
| full | 50px | 5 |
| full | 80px | 72 |
| full | 100px | 4 |

## Box Shadows

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(0, 0, 0) 0px 0px 0px 1px inset;
```

**xs** — blur: 1.56569px
```css
box-shadow: rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px;
```

## CSS Custom Properties

### Other

```css
--one-if-corner-shape-supported: 1;
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
| md | 809px | max-width |
| md | 810px | min-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | max-width |

## Transitions & Animations

**Durations:** `0.001s`

### Common Transitions

```css
transition: overflow 0.001s allow-discrete;
transition: all;
```

### Keyframe Animations

**__framer-loading-spin**
```css
@keyframes __framer-loading-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (7 instances)

```css
.button {
  background-color: rgba(255, 252, 243, 0.12);
  color: rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
  padding-top: 8px;
  padding-right: 4px;
  border-radius: 0px;
}
```

### Cards (1 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (57 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 12px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: rgb(0, 0, 0);
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 32px;
  padding-right: 32px;
  position: relative;
}
```

### Footer (2 instances)

```css
.foote {
  background-color: rgb(255, 253, 250);
  color: rgb(0, 0, 0);
  padding-top: 64px;
  padding-bottom: 20px;
  font-size: 12px;
}
```

### Switches (1 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(255, 252, 243, 0.12);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 40px;
  border: 0px none rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

### Button — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 8px 4px 8px 8px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**3 grid containers** and **628 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 816px | 0px |
| 100% | 0px |
| 596px | 0px |
| 456px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 2x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 296.5px 296.5px 296.5px 296.5px;
gap: 10px;
grid-template-columns: 224px 224px;
gap: 16px;
grid-template-columns: 224px 224px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 383x |
| row/nowrap | 245x |

**Gap values:** `100px`, `10px`, `12px`, `136px`, `14px`, `156px`, `164px`, `16px`, `18px`, `20px`, `24px`, `2px`, `32px`, `36px`, `3px`, `40px`, `48px`, `4px`, `5px`, `64px`, `64px 16px`, `6px`, `80px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 92/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 92/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 50/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance

**Issues:**
- 16 !important rules — prefer specificity over overrides
- 64% of CSS is unused — consider purging
- 4092 duplicate CSS declarations

## Z-Index Map

**6 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483647,2147483647 | div |
| sticky | 10,10 | div.f.r.a.m.e.r.-.1.2.o.q.y.9.o.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.4.y.b.p.4.u.-.c.o.n.t.a.i.n.e.r, div.f.r.a.m.e.r.-.1.i.o.o.n.r.n.-.c.o.n.t.a.i.n.e.r |
| base | 0,5 | div.f.r.a.m.e.r.-.1.l.t.0.o.d.0, div.f.r.a.m.e.r.-.1.v.p.7.p.1.d, div.f.r.a.m.e.r.-.1.5.7.2.b.b.7 |

**Issues:**
- [object Object]

## SVG Icons

**4 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 2 |
| md | 2 |

**Icon colors:** `rgb(37, 35, 36)`, `rgb(255, 252, 243)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Inter | self-hosted | 400, 600, 700 | normal, italic |
| Inter Display | self-hosted | 400, 500, 600, 700 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| hero | 26 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 23 | objectFit: cover, borderRadius: 0px, shape: square |
| avatar | 20 | objectFit: cover, borderRadius: 80px, shape: circular |
| general | 9 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 3 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (32x), 3:2 (22x), 4:3 (5x), 7:1 (3x), 3:4 (2x), 4.13:1 (2x), 4.21:1 (2x), 3.4:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |

## Component Anatomy

### button — 7 instances

**Slots:** label, icon

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (verbose)

### Sample Headings

> Harmony shaped by light, material, and space.
> Archline® was founded with a vision to craft spaces that tell stories, evoke emotion, and embody timeless elegance — blending architecture, artistry, and human experience into meaningful design that transcends trends and celebrates quiet sophistication.
> Our Featured Projects
> We bring bold visions to life through a fusion of strategy, design, and storytelling. We partner with brands, founders, and creators to shape identities.
> Designing Experiences That Resonate and Scale
> We bring bold visions to life through a fusion of strategy, design, and storytelling. We partner with brands, founders, and creators to shape identities.
> Your Answers To Popular Questions

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** A boutique studio dedicated to creating sophisticated interiors and architectural experiences that reflect elegance, harmony, and individuality, crafting timeless spaces where beauty meets function an

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → testimonial → footer → testimonial → content → testimonial → faq → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | testimonial | Harmony shaped by light, material, and space. | 0.8 |
| 2 | testimonial | We bring bold visions to life through a fusion of strategy, design, and storytel | 0.8 |
| 3 | content | — | 0.3 |
| 4 | testimonial | — | 0.8 |
| 5 | faq | Your Answers To Popular Questions | 0.85 |
| 6 | content | — | 0.3 |
| 7 | footer | — | 0.95 |
| 8 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.267 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.062)
**Counts:** total 81, svg 0, icon 1, screenshot-like 0, photo-like 10
**Dominant aspect:** square-ish
**Radius profile on images:** soft

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter Display` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
