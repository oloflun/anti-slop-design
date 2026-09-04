# Design Language: DIABLA OUTDOOR | Funky contract, outdoor & indoor furniture

> Extracted from `https://www.diablaoutdoor.com/en/` on September 4, 2026
> 1327 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fcf0f3` | rgb(252, 240, 243) | hsl(345, 67%, 96%) | 23 |
| Secondary | `#007aff` | rgb(0, 122, 255) | hsl(211, 100%, 50%) | 16 |
| Accent | `#ff4f55` | rgb(255, 79, 85) | hsl(358, 100%, 65%) | 4 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 155 |
| `#ffffff` | hsl(0, 0%, 100%) | 17 |
| `#333333` | hsl(0, 0%, 20%) | 16 |
| `#808080` | hsl(0, 0%, 50%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#fcf0f3`

### Text Colors

Text color palette: `#000000`, `#ed2e38`, `#808080`, `#007aff`, `#ffffff`, `#333333`, `#ff4f55`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#ed2e38` | text, border | 2458 |
| `#000000` | text, border | 155 |
| `#fcf0f3` | background | 23 |
| `#ffffff` | background, text, border | 17 |
| `#007aff` | text, border | 16 |
| `#333333` | text, border | 16 |
| `#ff4f55` | text, border | 4 |
| `#808080` | text | 1 |

## Typography

### Font Families

- **LinotypeHelveticaNeueLTStdRoman** — used for all (1237 elements)
- **Times New Roman** — used for body (64 elements)
- **Arial** — used for all (20 elements)
- **LinotypeHelveticaNeueLTStdLt** — used for headings (6 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 90px | 5.625rem | 400 | 80px | normal | h1 |
| 60px | 3.75rem | 400 | 50px | normal | h2 |
| 30px | 1.875rem | 400 | 30px | normal | span |
| 28px | 1.75rem | 400 | 31px | normal | div, a, input |
| 20px | 1.25rem | 400 | 22px | normal | a, div, span, form |
| 19.2px | 1.2rem | 400 | 18px | normal | a |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 14px | 0.875rem | 400 | 28px | normal | label, abbr |
| 13.3333px | 0.8333rem | 400 | normal | normal | button, span |
| 12px | 0.75rem | 400 | 18px | normal | div, svg, path, details |
| 10px | 0.625rem | 400 | 12px | normal | label, a, div, br |

### Heading Scale

```css
h1 { font-size: 90px; font-weight: 400; line-height: 80px; }
h2 { font-size: 60px; font-weight: 400; line-height: 50px; }
h1 { font-size: 16px; font-weight: 400; line-height: normal; }
h3 { font-size: 12px; font-weight: 400; line-height: 18px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: 18px; }
```

### Font Weights in Use

`400` (1297x), `500` (30x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-15 | 15px | 0.9375rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-52 | 52px | 3.25rem |
| spacing-60 | 60px | 3.75rem |
| spacing-80 | 80px | 5rem |
| spacing-100 | 100px | 6.25rem |
| spacing-150 | 150px | 9.375rem |
| spacing-326 | 326px | 20.375rem |
| spacing-382 | 382px | 23.875rem |
| spacing-480 | 480px | 30rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| lg | 12px | 4 |
| full | 50px | 15 |
| full | 100px | 1 |

## CSS Custom Properties

### Colors

```css
--main-color: #ED2E38;
--secondary-color: #FCF0F3;
--third-color: #F9C2CC;
--fourth-color: #A39D9C;
--plyr-color-main: #ED2E38;
--plyr-tooltip-color: #ED2E38;
--swiper-theme-color: #007aff;
--wpforms-field-border-radius: 3px;
--wpforms-field-border-style: solid;
--wpforms-field-border-size: 1px;
--wpforms-field-background-color: #ffffff;
--wpforms-field-border-color: rgba( 0, 0, 0, 0.25 );
--wpforms-field-border-color-spare: rgba( 0, 0, 0, 0.25 );
--wpforms-field-text-color: rgba( 0, 0, 0, 0.7 );
--wpforms-field-menu-color: #ffffff;
--wpforms-label-color: rgba( 0, 0, 0, 0.85 );
--wpforms-label-sublabel-color: rgba( 0, 0, 0, 0.55 );
--wpforms-label-error-color: #d63637;
--wpforms-button-border-radius: 3px;
--wpforms-button-border-style: none;
--wpforms-button-border-size: 1px;
--wpforms-button-background-color: #066aab;
--wpforms-button-border-color: #066aab;
--wpforms-button-text-color: #ffffff;
--wpforms-page-break-color: #066aab;
--wpforms-background-color: rgba( 0, 0, 0, 0 );
--wpforms-container-border-style: none;
--wpforms-container-border-width: 1px;
--wpforms-container-border-color: #000000;
--wpforms-container-border-radius: 3px;
--cmplz_banner_background_color: #fcf0f3;
--cmplz_banner_border_color: #ed2e38;
--cmplz_banner_border_width: 0px 0px 0px 0px;
--cmplz_banner_border_radius: 12px 12px 12px 12px;
--cmplz_text_color: #ed2e38;
--cmplz_hyperlink_color: #ed2e38;
--cmplz_button_accept_background_color: #fcf0f3;
--cmplz_button_accept_border_color: #ed2e38;
--cmplz_button_accept_text_color: #ed2e38;
--cmplz_button_deny_background_color: #fcf0f3;
--cmplz_button_deny_border_color: #ed2e38;
--cmplz_button_deny_text_color: #ed2e38;
--cmplz_button_settings_background_color: #fcf0f3;
--cmplz_button_settings_border_color: #ed2e38;
--cmplz_button_settings_text_color: #ed2e38;
--cmplz_button_border_radius: 14px 14px 14px 14px;
--cmplz_category_header_always_active_color: green;
--cmplz_slider_active_color: #ed2e38;
--cmplz_slider_inactive_color: #fcf0f3;
--cmplz_slider_bullet_color: #ffffff;
```

### Spacing

```css
--wp--preset--font-size--normal: 16px;
--wp--preset--font-size--huge: 42px;
--main-padding-space: 32px;
--plyr-font-size-base: 11px;
--plyr-font-size-small: 11px;
--plyr-font-size-large: 11px;
--plyr-font-size-xlarge: 11px;
--swiper-navigation-size: 44px;
--wpforms-background-size: cover;
--wpforms-container-padding: 0px;
--wpforms-field-size-input-height: 43px;
--wpforms-field-size-input-spacing: 15px;
--wpforms-field-size-font-size: 16px;
--wpforms-field-size-line-height: 19px;
--wpforms-field-size-padding-h: 14px;
--wpforms-field-size-checkbox-size: 16px;
--wpforms-field-size-sublabel-spacing: 5px;
--wpforms-field-size-icon-size: 1;
--wpforms-label-size-font-size: 16px;
--wpforms-label-size-line-height: 19px;
--wpforms-label-size-sublabel-font-size: 14px;
--wpforms-label-size-sublabel-line-height: 17px;
--wpforms-button-size-font-size: 17px;
--wpforms-button-size-height: 41px;
--wpforms-button-size-padding-h: 15px;
--wpforms-button-size-margin-top: 10px;
--wpforms-container-shadow-size-box-shadow: none;
--cmplz_banner_margin: 10px;
--cmplz_title_font_size: 15px;
--cmplz_text_font_size: 12px;
--cmplz_link_font_size: 12px;
--cmplz_category_body_font_size: 12px;
--cmplz_button_font_size: 15px;
--cmplz_category_header_title_font_size: 14px;
--cmplz_category_header_active_font_size: 12px;
```

### Typography

```css
--plyr-font-family: 'LinotypeHelveticaNeueLTStdLt', sans-serif;
--cmplz_text_line_height: calc(var(--cmplz_text_font_size) * 1.5);
```

### Shadows

```css
--plyr-range-thumb-shadow: none;
--plyr-range-thumb-active-shadow-width: 0;
--plyr-tooltip-shadow: none;
```

### Radii

```css
--plyr-tooltip-radius: 0;
```

### Other

```css
--plyr-video-controls-background: transparent;
--plyr-range-thumb-height: 10px;
--plyr-range-track-height: 2px;
--wpforms-background-image: none;
--wpforms-background-position: center center;
--wpforms-background-repeat: no-repeat;
--wpforms-background-width: 100px;
--wpforms-background-height: 100px;
--wpforms-background-url: none;
--cmplz_banner_width: 640px;
--cmplz_categories-height: 216px;
--cmplz-manage-consent-height: 50px;
--cmplz-manage-consent-offset: -35px;
```

### Dependencies

```css
--cmplz_text_line_height: --cmplz_text_font_size;
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
| xs | 350px | min-width |
| sm | 425px | max-width |
| sm | 576px | min-width |
| sm | 600px | min-width |
| md | 740px | max-width |
| md | 741px | min-width |
| md | 768px | max-width |
| md | 781px | max-width |
| md | 782px | min-width |
| lg | 960px | max-width |
| lg | 992px | min-width |
| 1200px | 1200px | min-width |
| 1370px | 1370px | max-width |
| 1371px | 1371px | min-width |
| 1680px | 1680px | max-width |
| 1920px | 1920px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.5s`, `0.4s`, `0.8s`, `0.3s`, `0.35s`, `0.6s`

### Common Transitions

```css
transition: all;
transition: 0.5s;
transition: 0.4s;
transition: filter 0.8s cubic-bezier(0.645, 0.045, 0.355, 1);
transition: 0.8s cubic-bezier(0.645, 0.045, 0.355, 1);
transition: transform;
transition: opacity;
transition: opacity 0.4s, top 0.4s;
transition: opacity 0.4s;
transition: opacity 0.3s cubic-bezier(0.645, 0.045, 0.355, 1), width 0.3s cubic-bezier(0.645, 0.045, 0.355, 1), height 0.3s cubic-bezier(0.645, 0.045, 0.355, 1), background 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
```

### Keyframe Animations

**cmplz-fadein**
```css
@keyframes cmplz-fadein {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**swiper-preloader-spin**
```css
@keyframes swiper-preloader-spin {
  100% { transform: rotate(360deg); }
}
```

**bounce**
```css
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { bottom: 50px; }
  40% { bottom: 20px; }
  60% { bottom: 35px; }
}
```

**bounce**
```css
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { bottom: 50px; }
  40% { bottom: 20px; }
  60% { bottom: 35px; }
}
```

**mc_slideIn**
```css
@keyframes mc_slideIn {
  100% { bottom: 0px; }
}
```

**mc_slideIn**
```css
@keyframes mc_slideIn {
  100% { bottom: 0px; }
}
```

**mc_slideOut**
```css
@keyframes mc_slideOut {
  100% { bottom: var(--cmplz-manage-consent-offset); }
}
```

**mc_slideOut**
```css
@keyframes mc_slideOut {
  100% { bottom: var(--cmplz-manage-consent-offset); }
}
```

**fadeIn**
```css
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**fadeIn**
```css
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (51 instances)

```css
.button {
  background-color: rgb(252, 240, 243);
  color: rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 25px;
  border-radius: 14px;
}
```

### Inputs (41 instances)

```css
.input {
  background-color: rgb(255, 255, 255);
  color: rgb(237, 46, 56);
  border-color: rgb(237, 46, 56);
  border-radius: 0px;
  font-size: 12px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (128 instances)

```css
.link {
  color: rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
}
```

### Navigation (16 instances)

```css
.navigatio {
  color: rgb(237, 46, 56);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (4 instances)

```css
.foote {
  color: rgb(237, 46, 56);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 12px;
}
```

### Modals (2 instances)

```css
.modal {
  background-color: rgb(252, 240, 243);
  border-radius: 12px;
  padding-top: 15px;
  padding-right: 20px;
  max-width: 100%;
}
```

### Dropdowns (11 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(237, 46, 56);
  padding-top: 0px;
}
```

### Accordions (16 instances)

```css
.accordion {
  color: rgb(237, 46, 56);
  font-size: 12px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(237, 46, 56);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(237, 46, 56);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
```

### Button — 8 instances, 3 variants

**Variant 1** (3 instances)

```css
  background: rgb(252, 240, 243);
  color: rgb(237, 46, 56);
  padding: 0px 5px 0px 5px;
  border-radius: 14px;
  border: 1px solid rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 500;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

**Variant 3** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(237, 46, 56);
  padding: 0px 25px 0px 25px;
  border-radius: 14px;
  border: 1px solid rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
```

### Input — 10 instances, 1 variant

**Variant 1** (10 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(237, 46, 56);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px 0px 1px none none solid rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
```

### Button — 29 instances, 1 variant

**Variant 1** (29 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(237, 46, 56);
  padding: 0px 25px 0px 25px;
  border-radius: 14px;
  border: 1px solid rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
```

### Button — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 122, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 122, 255);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(237, 46, 56);
  padding: 10px 20px 10px 20px;
  border-radius: 14px;
  border: 3px solid rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(237, 46, 56);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(237, 46, 56);
  padding: 10px 20px 10px 20px;
  border-radius: 14px;
  border: 0px none rgb(237, 46, 56);
  font-size: 12px;
  font-weight: 400;
```

## Layout System

**28 grid containers** and **48 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 20px |
| 90% | 0px |
| 600px | 100px |
| 1200px | 150px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 11x |
| 1-column | 6x |
| 12-column | 2x |
| 5-column | 1x |
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 183.969px 183.984px;
gap: 16px;
grid-template-columns: 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px;
grid-template-columns: 193.328px 193.328px 193.328px;
gap: 10px;
grid-template-columns: 243.188px 243.203px 243.203px 243.203px 243.188px;
grid-template-columns: 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px 101.328px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 46x |
| row/wrap | 2x |

**Gap values:** `10px`, `16px`

## Accessibility (WCAG 2.1)

**Overall Score: 0%** — 0 passing, 12 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#ed2e38` | `#fcf0f3` | 3.74:1 | FAIL | button, a (12x) |

## Design System Score

**Overall: 69/100 (Grade: D)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 0/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 12 WCAG contrast failures
- 337 !important rules — prefer specificity over overrides
- 88% of CSS is unused — consider purging
- 3111 duplicate CSS declarations

## Z-Index Map

**7 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2000,99999 | div.t.r.a.n.s.i.t.i.o.n. .o.p.e.n.e.d. .c.l.o.s.e.d, button.c.m.p.l.z.-.b.t.n. .c.m.p.l.z.-.m.a.n.a.g.e.-.c.o.n.s.e.n.t. .m.a.n.a.g.e.-.c.o.n.s.e.n.t.-.1. .c.m.p.l.z.-.d.i.s.m.i.s.s.e.d, button.c.m.p.l.z.-.b.t.n. .c.m.p.l.z.-.h.i.d.d.e.n. .c.m.p.l.z.-.m.a.n.a.g.e.-.c.o.n.s.e.n.t. .m.a.n.a.g.e.-.c.o.n.s.e.n.t.-.1 |
| sticky | 10,25 | header.t.r.a.n.s.i.t.i.o.n. .n.o.s.e.l.e.c.t, div.s.w.i.p.e.r.-.b.u.t.t.o.n.-.p.r.e.v. .t.r.a.n.s.i.t.i.o.n, div.s.w.i.p.e.r.-.b.u.t.t.o.n.-.n.e.x.t. .t.r.a.n.s.i.t.i.o.n |
| base | 1,2 | input.c.m.p.l.z.-.c.o.n.s.e.n.t.-.c.h.e.c.k.b.o.x. .c.m.p.l.z.-.f.u.n.c.t.i.o.n.a.l, input.c.m.p.l.z.-.c.o.n.s.e.n.t.-.c.h.e.c.k.b.o.x. .c.m.p.l.z.-.p.r.e.f.e.r.e.n.c.e.s, input.c.m.p.l.z.-.c.o.n.s.e.n.t.-.c.h.e.c.k.b.o.x. .c.m.p.l.z.-.s.t.a.t.i.s.t.i.c.s |

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
| LinotypeHelveticaNeueLTStdLt | self-hosted | 400, normal | normal |
| LinotypeHelveticaNeueLTStdRoman | self-hosted | 400, normal | normal |
| swiper-icons | self-hosted | 400 | normal |
| UserRegistration | self-hosted | normal | normal |
| dashicons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 39 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 9 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 4 | objectFit: contain, borderRadius: 0px, shape: square |
| thumbnail | 1 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (18x), 1:1 (18x), 3:2 (9x), 2:3 (4x), 4:3 (2x), 16:9 (2x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `800ms` | 800 |

### Easing Families

- **custom** (10 uses) — `cubic-bezier(0.645, 0.045, 0.355, 1)`
- **ease-in-out** (2 uses) — `ease`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `bounce` | custom | bottom | 1 |
| `bounce` | custom | bottom | 1 |
| `mc_slideOut` | custom | bottom | 2 |
| `mc_slideOut` | custom | bottom | 2 |
| `slideIn` | custom | bottom | 2 |
| `slideIn` | custom | bottom | 2 |

## Component Anatomy

### button — 49 instances

**Slots:** label

### input — 10 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **more** (3)
- **accept** (2)
- **harbor** (2)
- **xaloc** (2)
- **lace** (2)
- **classe** (2)
- **accessories** (2)
- **loungers** (2)

### Button Copy Patterns

- "more info" (3×)
- "harbor" (2×)
- "xaloc" (2×)
- "lace" (2×)
- "classe" (2×)
- "accessories" (2×)
- "loungers" (2×)
- "seating" (2×)
- "tables" (2×)
- "easy" (2×)

### Sample Headings

> 
			
				

	
	


			
		
> THE PULSE OF LIVING
> NATURE VIBES
> THE PULSE OF LIVING
> THE PULSE OF LIVING
> NATURE VIBES
> THE PULSE OF LIVING
> HARBOR
> XALOC
> LACE

## Page Intent

**Type:** `legal` (confidence 0.28)
**Description:** DIABLA OUTDOOR | Discover our proposals to enjoy your spaces 365 days a year with a Diabla attitude. Outdoor and indoor furniture, accessories, and complements with a carefree and lightweight design f

Alternates: landing (0.3)

## Section Roles

Reading order (top→bottom): sidebar → nav → sidebar → content → gallery → sidebar → content → sidebar → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | sidebar | — | 0.4 |
| 2 | content | THE PULSE OF LIVING | 0.3 |
| 3 | gallery | THE PULSE OF LIVING | 0.7 |
| 4 | content | HARBOR | 0.3 |
| 5 | sidebar | Alejandra Gandia-Blasco | 0.4 |
| 6 | footer | — | 0.95 |
| 7 | sidebar | — | 0.4 |
| 8 | sidebar | — | 0.4 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.318 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.472)
**Counts:** total 53, svg 5, icon 0, screenshot-like 0, photo-like 48
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `LinotypeHelveticaNeueLTStdRoman` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
