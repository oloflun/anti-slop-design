# Design Language: NotReal | Not Real

> Extracted from `https://notreal.tv/` on September 4, 2026
> 565 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#292a2c` | hsl(220, 4%, 17%) | 579 |
| `#000000` | hsl(0, 0%, 0%) | 496 |
| `#ffffff` | hsl(0, 0%, 100%) | 21 |
| `#999999` | hsl(0, 0%, 60%) | 18 |
| `#f2f2f2` | hsl(0, 0%, 95%) | 4 |
| `#cccccc` | hsl(0, 0%, 80%) | 2 |

### Background Colors

Used on large-area elements: `#f2f2f2`

### Text Colors

Text color palette: `#292a2c`, `#000000`, `#020202`, `#ffffff`, `#999999`, `#cccccc`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#292a2c` | text, border | 579 |
| `#000000` | text, border, background | 496 |
| `#ffffff` | text, border, background | 21 |
| `#999999` | text, border | 18 |
| `#f2f2f2` | background | 4 |
| `#cccccc` | text, border | 2 |

## Typography

### Font Families

- **telegraf** — used for all (461 elements)
- **Open Sans** — used for body (75 elements)
- **ogg** — used for body (14 elements)
- **Arial** — used for body (6 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 38px | 2.375rem | 400 | 41.8px | 0.1px | h1, span |
| 32px | 2rem | 400 | 32px | normal | span |
| 28px | 1.75rem | 400 | 46.6668px | normal | div |
| 25.5px | 1.5938rem | 400 | 38.25px | -0.5px | span |
| 25px | 1.5625rem | 400 | 25px | 1px | span, div, h5 |
| 23.94px | 1.4963rem | 400 | 35.91px | 0.5px | span |
| 22px | 1.375rem | 400 | 22px | normal | a, svg, metadata, sfw |
| 20px | 1.25rem | 400 | 0px | 0.5px | li, a, div, span |
| 18.5395px | 1.1587rem | 400 | 22.2474px | -0.5px | span |
| 18.176px | 1.136rem | 400 | 21.8112px | 0.5px | p |
| 18px | 1.125rem | 400 | 30.0001px | normal | html, head, meta, title |
| 15px | 0.9375rem | 400 | 30.0001px | 0.5px | h6 |
| 13.3333px | 0.8333rem | 400 | normal | normal | button |
| 13px | 0.8125rem | 400 | 61.9999px | normal | div |
| 0px | 0rem | 400 | 0px | normal | div, img, a, video |

### Heading Scale

```css
h1 { font-size: 38px; font-weight: 400; line-height: 41.8px; }
h5 { font-size: 25px; font-weight: 400; line-height: 25px; }
h6 { font-size: 15px; font-weight: 400; line-height: 30.0001px; }
```

### Body Text

```css
body { font-size: 20px; font-weight: 400; line-height: 0px; }
```

### Font Weights in Use

`400` (556x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-63 | 63px | 3.9375rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-110 | 110px | 6.875rem |
| spacing-150 | 150px | 9.375rem |
| spacing-300 | 300px | 18.75rem |
| spacing-400 | 400px | 25rem |
| spacing-410 | 410px | 25.625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 1 |
| full | 50px | 3 |

## Box Shadows

**sm** — blur: 5.00004px
```css
box-shadow: rgba(0, 0, 0, 0.25) 0px 1.99998px 5.00004px 0px;
```

## CSS Custom Properties

### Colors

```css
--wp-block-synced-color: #7a00df;
--wp-block-synced-color--rgb: 122,0,223;
--wp-bound-block-color: var(--wp-block-synced-color);
--wp-admin-theme-color: #007cba;
--wp-admin-theme-color--rgb: 0,124,186;
--wp-admin-theme-color-darker-10: #006ba1;
--wp-admin-theme-color-darker-10--rgb: 0,107,160.5;
--wp-admin-theme-color-darker-20: #005a87;
--wp-admin-theme-color-darker-20--rgb: 0,90,135;
--wp-admin-border-width-focus: 2px;
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
--tpg-primary-color: #0d6efd;
--tpg-secondary-color: #0654c4;
--tpg-primary-light: #c4d0ff;
```

### Spacing

```css
--wp--preset--font-size--normal: 16px;
--wp--preset--font-size--huge: 42px;
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
```

### Shadows

```css
--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);
--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);
--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);
--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);
--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);
```

### Other

```css
--wp-editor-canvas-background: #ddd;
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
```

### Dependencies

```css
--wp-bound-block-color: --wp-block-synced-color;
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
| sm | 500px | max-width |
| sm | 543px | max-width |
| sm | 544px | max-width |
| sm | 600px | max-width |
| md | 767px | max-width |
| md | 768px | max-width |
| md | 769px | min-width |
| 850px | 850px | max-width |
| lg | 990px | max-width |
| lg | 991px | max-width |
| lg | 992px | min-width |
| lg | 993px | min-width |
| lg | 1023px | max-width |
| lg | 1024px | max-width |
| lg | 1080px | max-width |
| 1168px | 1168px | max-width |
| 1169px | 1169px | min-width |
| 1170px | 1170px | max-width |
| 1199px | 1199px | max-width |
| 1200px | 1200px | min-width |
| 1201px | 1201px | min-width |
| xl | 1280px | min-width |
| xl | 1300px | min-width |
| 1366px | 1366px | max-width |
| 1367px | 1367px | min-width |
| 1400px | 1400px | max-width |
| 1440px | 1440px | max-width |
| 1441px | 1441px | max-width |
| 1601px | 1601px | max-width |
| 1640px | 1640px | min-width |
| 1915px | 1915px | max-width |
| 2539px | 2539px | max-width |
| 2540px | 2540px | min-width |
| 2600px | 2600px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.2s`, `0.31s`, `0.3s`, `0.333s`, `0.25s`

### Common Transitions

```css
transition: all;
transition: background-color 0.2s linear;
transition: 0.2s linear;
transition: 0.31s;
transition: box-shadow 0.3s;
transition: 0.3s;
transition: opacity 0.333s cubic-bezier(0.4, 0, 0.22, 1);
transition: opacity 0.2s;
transition: opacity 0.25s ease-out;
transition: transform 0.25s;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**blink**
```css
@keyframes blink {
  0% { opacity: 0; }
  50% { opacity: 1; }
  100% { opacity: 0; }
}
```

**ball-scale-multiple**
```css
@keyframes ball-scale-multiple {
  0% { opacity: 0; transform: scale(0); }
  5% { opacity: 0.75; }
  100% { opacity: 0; transform: scale(1); }
}
```

**ball-clip-rotate**
```css
@keyframes ball-clip-rotate {
  0% { transform: rotate(0deg); }
  50% { transform: rotate(180deg); }
  100% { transform: rotate(1turn); }
}
```

**coverZoom**
```css
@keyframes coverZoom {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.24); }
}
```

**coverZoom**
```css
@keyframes coverZoom {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.24); }
}
```

**sliderPreloader**
```css
@keyframes sliderPreloader {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.11); }
}
```

**clockwise**
```css
@keyframes clockwise {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**donut-rotate**
```css
@keyframes donut-rotate {
  0%, 100% { transform: rotate(0deg); }
  50% { transform: rotate(-140deg); }
}
```

**nprogress-spinner**
```css
@keyframes nprogress-spinner {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (6 instances)

```css
.button {
  color: rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (1 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 1.99998px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 1.99998px 5.00004px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (37 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 0px;
  font-weight: 400;
}
```

### Navigation (6 instances)

```css
.navigatio {
  background-color: rgb(242, 242, 242);
  color: rgb(41, 42, 44);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: absolute;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 20px;
}
```

### Modals (4 instances)

```css
.modal {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 100%;
}
```

### Dropdowns (13 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(41, 42, 44);
  padding-top: 0px;
}
```

### Tooltips (1 instances)

```css
.tooltip {
  background-color: rgb(255, 255, 255);
  color: rgb(41, 42, 44);
  font-size: 18px;
  border-radius: 1.99998px;
  padding-top: 0px;
  padding-right: 0px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 1.99998px 5.00004px 0px;
}
```

## Layout System

**0 grid containers** and **81 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 2648px | 43.9999px |
| 100% | 11px |
| 66.6667% | 11px |
| 33.3333% | 11px |
| 50% | 11px |
| 16.6667% | 11px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 43x |
| row/wrap | 27x |
| column/nowrap | 11x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 83/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 85/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- No clear primary brand color detected
- 4 font families — consider limiting to 2 (heading + body)
- 570 !important rules — prefer specificity over overrides
- 91% of CSS is unused — consider purging
- 6473 duplicate CSS declarations

## Z-Index Map

**11 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1500,2147483647 | div.p.s.w.p, div.p.s.w.p._._.u.i. .p.s.w.p._._.u.i.-.-.h.i.d.d.e.n, div.p.s.w.p._._.s.h.a.r.e.-.m.o.d.a.l. .p.s.w.p._._.s.h.a.r.e.-.m.o.d.a.l.-.-.h.i.d.d.e.n. .p.s.w.p._._.s.i.n.g.l.e.-.t.a.p |
| dropdown | 118,120 | div.b.a.c.k.-.t.o.-.t.o.p, header.n.a.v._.j.f.g.e.w.8.4.d.a. .s.e.m.p.l.i.c.e.-.n.a.v.b.a.r. .a.c.t.i.v.e.-.n.a.v.b.a.r. .s.t.i.c.k.y.-.n.a.v |
| sticky | 10,10 | div.t.h.u.m.b.-.h.o.v.e.r, div.t.h.u.m.b.-.h.o.v.e.r, div.t.h.u.m.b.-.h.o.v.e.r |
| base | -1,1 | div, section.c.o.n.t.e.n.t.-.b.l.o.c.k, div.h.a.m.b.u.r.g.e.r. .n.a.v.b.a.r.-.r.i.g.h.t. .s.e.m.p.l.i.c.e.-.m.e.n.u |

**Issues:**
- [object Object]

## SVG Icons

**1 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xl | 1 |

**Icon colors:** `rgb(0, 0, 0)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| flaticon_the_post_grid | self-hosted | 400, normal | normal |
| telegraf | self-hosted | normal | normal |
| ogg | self-hosted | normal | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 5 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 4 | objectFit: fill, borderRadius: 0px, shape: square |
| thumbnail | 2 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (6x), 16:9 (4x), 4.58:1 (1x)

## Motion Language

**Feel:** mechanical · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

### Easing Families

- **linear** (12 uses) — `linear`
- **custom** (3 uses) — `cubic-bezier(0.4, 0, 0.22, 1)`
- **ease-in-out** (2 uses) — `ease`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `moveSlideshow` | slide-x | transform | 1 |

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Title Case (verbose)

### Sample Headings

> Check out out latest news on instagam → https://www.instagram.com/notreal.tv Check out our latest news on instagram → https://www.instagram.com/notreal.tv Our latest news on instagram → https://www.instagram.com/notreal.tv

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Not Real is a design—driven creative studio focused on art direction, CGI & animation, located in Buenos Aires and Madrid.

## Section Roles

Reading order (top→bottom): nav → nav → nav → content → content → content → testimonial → content → testimonial → content → content → content → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | content | — | 0.3 |
| 4 | content | — | 0.3 |
| 5 | content | — | 0.3 |
| 6 | testimonial | — | 0.8 |
| 7 | content | Check out out latest news on instagam → https://www.instagram.com/notreal.tv Che | 0.3 |
| 8 | testimonial | — | 0.8 |
| 9 | content | — | 0.3 |
| 10 | content | — | 0.3 |
| 11 | content | — | 0.3 |
| 12 | content | — | 0.3 |
| 13 | content | — | 0.3 |
| 14 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.011 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.5)
**Counts:** total 11, svg 2, icon 2, screenshot-like 0, photo-like 9
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `telegraf` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
