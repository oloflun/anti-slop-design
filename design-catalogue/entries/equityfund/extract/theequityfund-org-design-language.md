# Design Language: Home | The Climate Equity Fund

> Extracted from `https://theequityfund.org` on September 4, 2026
> 537 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#c4b3e0` | rgb(196, 179, 224) | hsl(263, 42%, 79%) | 94 |
| Secondary | `#500c20` | rgb(80, 12, 32) | hsl(342, 74%, 18%) | 235 |
| Accent | `#fcf6ed` | rgb(252, 246, 237) | hsl(36, 71%, 96%) | 9 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 505 |
| `#000000` | hsl(0, 0%, 0%) | 253 |

### Background Colors

Used on large-area elements: `#fcf6ed`, `#c4b3e0`, `#500c20`

### Text Colors

Text color palette: `#000000`, `#500c20`, `#c4b3e0`, `#fcf6ed`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 505 |
| `#000000` | text | 253 |
| `#500c20` | text, border, background | 235 |
| `#c4b3e0` | text, background, border | 94 |
| `#fcf6ed` | background, text | 9 |

## Typography

### Font Families

- **Metrify Narrow** — used for all (473 elements)
- **Feature Text** — used for all (39 elements)
- **Judge** — used for headings (19 elements)
- **Metrify** — used for all (4 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 204.8px | 12.8rem | 500 | 204.8px | normal | h1 |
| 100px | 6.25rem | 700 | 100px | normal | span |
| 60px | 3.75rem | 500 | 72px | normal | h2, a |
| 41.6px | 2.6rem | 500 | 45.76px | -0.52px | h2 |
| 36px | 2.25rem | 500 | 50.4px | 0.36px | dd, h3, a |
| 28px | 1.75rem | 400 | 33.6px | normal | h3 |
| 24px | 1.5rem | 400 | 28.8px | normal | button, p, span |
| 20px | 1.25rem | 400 | 28px | normal | a, p, span |
| 18px | 1.125rem | 400 | 27px | normal | body, noscript, a, span |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |

### Heading Scale

```css
h1 { font-size: 204.8px; font-weight: 500; line-height: 204.8px; }
h2 { font-size: 60px; font-weight: 500; line-height: 72px; }
h2 { font-size: 41.6px; font-weight: 500; line-height: 45.76px; }
h3 { font-size: 36px; font-weight: 500; line-height: 50.4px; }
h3 { font-size: 28px; font-weight: 400; line-height: 33.6px; }
h2 { font-size: 18px; font-weight: 400; line-height: 27px; }
```

### Body Text

```css
body { font-size: 18px; font-weight: 400; line-height: 27px; }
```

### Font Weights in Use

`400` (509x), `500` (19x), `700` (6x), `300` (3x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-64 | 64px | 4rem |
| spacing-96 | 96px | 6rem |
| spacing-120 | 120px | 7.5rem |
| spacing-144 | 144px | 9rem |
| spacing-208 | 208px | 13rem |
| spacing-311 | 311px | 19.4375rem |
| spacing-329 | 329px | 20.5625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| full | 9999px | 2 |

## CSS Custom Properties

### Colors

```css
--wp--preset--color--black: #000000;
--wp--preset--color--cyan-bluish-gray: #abb8c3;
--wp--preset--color--white: #ffffff;
--wp--preset--color--pale-pink: #f78da7;
--wp--preset--color--vivid-red: #cf2e2e;
--wp--preset--color--luminous-vivid-orange: #ff6900;
--wp--preset--color--luminous-vivid-amber: #fcb900;
--wp--preset--color--light-green-cyan: #7bdcb5;
--wp--preset--color--vivid-green-cyan: #00d084;
--wp--preset--color--pale-cyan-blue: #8ed1fc;
--wp--preset--color--vivid-cyan-blue: #0693e3;
--wp--preset--color--vivid-purple: #9b51e0;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-border-spacing-x: 0;
--tw-ring-color: rgba(59,130,246,.5);
--tw-ring-offset-color: #fff;
--tw-ring-offset-width: 0px;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
```

### Spacing

```css
--wp--preset--font-size--small: 13px;
--wp--preset--font-size--medium: 20px;
--wp--preset--font-size--large: 36px;
--wp--preset--font-size--x-large: 42px;
--wp--preset--spacing--20: 0.44rem;
--wp--preset--spacing--30: 0.67rem;
--wp--preset--spacing--40: 1rem;
--wp--preset--spacing--50: 1.5rem;
--wp--preset--spacing--60: 2.25rem;
--wp--preset--spacing--70: 3.38rem;
--wp--preset--spacing--80: 5.06rem;
--wp--style--global--content-size: 800px;
--wp--style--global--wide-size: 1000px;
--wp--style--block-gap: 2rem;
--tw-numeric-spacing: ;
--tw-contain-size: ;
```

### Shadows

```css
--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);
--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);
--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);
--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);
--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);
--tw-drop-shadow: ;
--tw-shadow: 0 0 #0000;
```

### Other

```css
--wp--preset--aspect-ratio--square: 1;
--wp--preset--aspect-ratio--4-3: 4/3;
--wp--preset--aspect-ratio--3-4: 3/4;
--wp--preset--aspect-ratio--3-2: 3/2;
--wp--preset--aspect-ratio--2-3: 2/3;
--wp--preset--aspect-ratio--16-9: 16/9;
--wp--preset--aspect-ratio--9-16: 9/16;
--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);
--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);
--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);
--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);
--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);
--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);
--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);
--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);
--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);
--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);
--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);
--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-contain-style: ;
--tw-backdrop-invert: ;
--tw-brightness: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-backdrop-brightness: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-rotate: 0;
--tw-contrast: ;
--tw-skew-x: 0;
--tw-backdrop-blur: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-numeric-fraction: ;
--tw-skew-y: 0;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-pinch-zoom: ;
--tw-contain-paint: ;
--tw-contain-layout: ;
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
| sm | 425px | min-width |
| sm | 640px | min-width |
| md | 768px | min-width |
| lg | 1024px | min-width |
| xl | 1280px | min-width |
| 2xl | 1536px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.15s`, `0.1s`

### Common Transitions

```css
transition: all;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.1s;
transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: grid-template-rows 0.15s cubic-bezier(0.4, 0, 0.2, 1), -ms-grid-rows 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (7 instances)

```css
.button {
  background-color: rgb(80, 12, 32);
  color: rgb(80, 12, 32);
  font-size: 18px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Links (51 instances)

```css
.link {
  color: rgb(80, 12, 32);
  font-size: 18px;
  font-weight: 400;
}
```

### Navigation (6 instances)

```css
.navigatio {
  color: rgb(80, 12, 32);
  padding-top: 6px;
  padding-bottom: 6px;
  padding-left: 24px;
  padding-right: 24px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(80, 12, 32);
  color: rgb(196, 179, 224);
  padding-top: 32px;
  padding-bottom: 32px;
  font-size: 18px;
}
```

### Modals (1 instances)

```css
.modal {
  background-color: rgb(196, 179, 224);
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
  background: rgb(80, 12, 32);
  color: rgb(196, 179, 224);
  padding: 0px 0px 0px 0px;
  border-radius: 9999px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 18px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(80, 12, 32);
  color: rgb(252, 246, 237);
  padding: 12px 16px 8px 16px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 700;
```

## Layout System

**6 grid containers** and **47 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 800px | 0px |
| 1024px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 2-column | 3x |
| 3-column | 2x |

### Grid Templates

```css
grid-template-columns: 584px 584px;
gap: 48px;
grid-template-columns: 378.656px 378.672px 378.656px;
gap: 40px;
grid-template-columns: 592px 592px;
gap: 32px;
grid-template-columns: 384px 384px 384px;
gap: 32px;
grid-template-columns: 592px 592px;
gap: 32px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 31x |
| column/nowrap | 16x |

**Gap values:** `12px`, `16px`, `24px`, `32px`, `40px`, `48px`, `8px`, `8px 24px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 5 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#500c20` | `#c4b3e0` | 7.69:1 | AAA |
| `#fcf6ed` | `#500c20` | 13.82:1 | AAA |

## Design System Score

**Overall: 83/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 221 !important rules — prefer specificity over overrides
- 64% of CSS is unused — consider purging
- 1218 duplicate CSS declarations

## Z-Index Map

**4 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,100 | a.[.&.:.n.o.t.(.:.f.o.c.u.s.).].:.s.r.-.o.n.l.y. .a.b.s.o.l.u.t.e. .t.o.p.-.4. .l.e.f.t.-.4. .b.g.-.c.r.e.a.m. .p.x.-.4. .p.y.-.3. .f.l.e.x. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .z.-.[.1.0.0.] |
| sticky | 10,50 | header.p.x.-.s.i.t.e.-.p.a.d.d.i.n.g. .a.b.s.o.l.u.t.e. .t.o.p.-.w.p.-.a.d.m.i.n.-.b.a.r. .i.n.s.e.t.-.x.-.0. .z.-.1.0. .p.a.l.e.t.t.e.-.l.a.v.e.n.d.e.r. .t.e.x.t.-.f.o.r.e.g.r.o.u.n.d, ul.a.b.s.o.l.u.t.e. .z.-.2.0. .t.o.p.-.f.u.l.l. .l.e.f.t.-.0. .b.o.r.d.e.r.-.2. .b.o.r.d.e.r.-.f.o.r.e.g.r.o.u.n.d. .d.i.v.i.d.e.-.y.-.2. .d.i.v.i.d.e.-.f.o.r.e.g.r.o.u.n.d. .t.e.x.t.-.l.e.f.t. .m.i.n.-.w.-.[.1.0.0.%.], div.f.i.x.e.d. .i.n.s.e.t.-.x.-.0. .b.o.t.t.o.m.-.0. .t.o.p.-.w.p.-.a.d.m.i.n.-.b.a.r. .h.-.f.u.l.l. .w.-.f.u.l.l. .o.v.e.r.f.l.o.w.-.s.c.r.o.l.l. .t.e.x.t.-.f.o.r.e.g.r.o.u.n.d. .b.g.-.b.a.c.k.g.r.o.u.n.d. .z.-.5.0. .p.a.l.e.t.t.e.-.l.a.v.e.n.d.e.r |

## SVG Icons

**19 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| lg | 3 |
| xl | 15 |

**Icon colors:** `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Judge | self-hosted | 400, 500 | normal |
| Feature Deck | self-hosted | 400, 700 | normal, italic |
| Feature Text | self-hosted | 400, 700 | normal, italic |
| Metrify Narrow | self-hosted | 400, 500, 700 | normal, italic |
| Metrify | self-hosted | 400, 500, 700 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 16:9 (6x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |

### Easing Families

- **custom** (37 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`

## Component Anatomy

### button — 3 instances

**Slots:** label, icon
**Sizes:** sm

## Brand Voice

**Tone:** friendly · **Pronoun:** we-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **toggle** (1)
- **our** (1)
- **read** (1)

### Button Copy Patterns

- "toggle menu for work" (1×)
- "our work" (1×)
- "read more" (1×)

### Sample Headings

> HOW WE WIN
> WHAT WE DO
> STRATEGIC GRANTMAKING
> PHILANTHROPIC ADVOCACY
> POLICY EXPERTISE
> HOW WE WIN
> WHAT WE DO
> STRATEGIC GRANTMAKING
> PHILANTHROPIC ADVOCACY
> POLICY EXPERTISE

## Page Intent

**Type:** `pricing` (confidence 0.42)
**Description:** The Climate and Clean Energy Equity Fund is building a broad and powerful base of popular support for equitable climate action, state by state.

Alternates: landing (0.45), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → pricing-table → nav → pricing-table → content → content → hero → footer → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | pricing-table | HOW WE WIN | 0.9 |
| 3 | nav | HOW WE WIN | 0.4 |
| 4 | pricing-table | — | 0.9 |
| 5 | content | WHAT WE DO | 0.3 |
| 6 | content | WHERE WE WORK | 0.3 |
| 7 | hero | WRITING MINNESOTA’S NEXT CHAPTER | 0.4 |
| 8 | footer | — | 0.95 |
| 9 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.227 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.667)
**Counts:** total 6, svg 0, icon 0, screenshot-like 0, photo-like 6
**Dominant aspect:** landscape
**Radius profile on images:** square

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: tailwindcss (0.3)

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Metrify Narrow` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
