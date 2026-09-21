# Design Language: Digital byrå & webbyrå i Göteborg – Kreativa upplevelser | Hoy

> Extracted from `https://www.hoy.se/` on September 15, 2026
> 560 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fcecba` | rgb(252, 236, 186) | hsl(45, 92%, 86%) | 431 |
| Secondary | `#5124ae` | rgb(81, 36, 174) | hsl(260, 66%, 41%) | 95 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 546 |
| `#000000` | hsl(0, 0%, 0%) | 40 |

### Background Colors

Used on large-area elements: `#5124ae`, `#fcecba`

### Text Colors

Text color palette: `#000000`, `#fcecba`, `#5124ae`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 546 |
| `#fcecba` | text, background, border | 431 |
| `#5124ae` | background, text, border | 95 |
| `#000000` | text | 40 |

## Typography

### Font Families

- **Circular** — used for all (508 elements)
- **Times New Roman** — used for body (52 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 132px | 8.25rem | 400 | 125.4px | -2.64px | span, h2 |
| 88px | 5.5rem | 400 | 96.8px | -1.76px | a |
| 48px | 3rem | 400 | 45.6px | -0.48px | h1, br |
| 32px | 2rem | 400 | 44.8px | -0.32px | a, h2, h3, br |
| 22px | 1.375rem | 400 | 30.8px | normal | a, span, p, br |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, link |
| 14px | 0.875rem | 500 | 23.8px | 1.4px | a, svg, path, span |

### Heading Scale

```css
h2 { font-size: 132px; font-weight: 400; line-height: 125.4px; }
h1 { font-size: 48px; font-weight: 400; line-height: 45.6px; }
h2 { font-size: 32px; font-weight: 400; line-height: 44.8px; }
h3 { font-size: 22px; font-weight: 400; line-height: 30.8px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: 24px; }
```

### Font Weights in Use

`400` (522x), `500` (38x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-0 | 0px | 0rem |
| spacing-64 | 64px | 4rem |
| spacing-96 | 96px | 6rem |
| spacing-120 | 120px | 7.5rem |
| spacing-160 | 160px | 10rem |
| spacing-192 | 192px | 12rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 4 |
| full | 9999px | 29 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px;
```

## CSS Custom Properties

### Colors

```css
--background-color: 0 0 0;
--text-color: 255 255 255;
--swiper-theme-color: #007aff;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-ring-offset-width: 0px;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgb(59 130 246/0.5);
--tw-ring-offset-color: #fff;
```

### Spacing

```css
--tw-contain-size: ;
--tw-numeric-spacing: ;
```

### Shadows

```css
--tw-shadow: 0 0 #0000;
--tw-drop-shadow: ;
```

### Other

```css
--tw-contrast: ;
--tw-backdrop-sepia: ;
--vh: 8px;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-backdrop-blur: ;
--tw-contain-style: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-backdrop-invert: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-brightness: ;
--tw-numeric-fraction: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-skew-y: 0;
--tw-backdrop-brightness: ;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-rotate: 0;
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
| sm | 480px | min-width |
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 975px | max-width |
| lg | 976px | min-width |
| 1440px | 1440px | min-width |
| 2xl | 1600px | min-width |
| 1920px | 1920px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.3s`, `0.15s`, `0.7s`, `0.4s`, `0.2s`, `0.5s`

### Common Transitions

```css
transition: all;
transition: color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.7s;
transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) 0.4s;
transition: color 0.7s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.7s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.7s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.7s cubic-bezier(0.4, 0, 0.2, 1), fill 0.7s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.7s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.7s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.7s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.7s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.7s cubic-bezier(0.4, 0, 0.2, 1), fill 0.7s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.7s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.7s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.7s cubic-bezier(0.4, 0, 0.2, 1), transform 0.7s cubic-bezier(0.4, 0, 0.2, 1), filter 0.7s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.7s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

### Keyframe Animations

**slide-up-enter**
```css
@keyframes slide-up-enter {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**slide-up-leave**
```css
@keyframes slide-up-leave {
  0% { opacity: 1; }
  100% { opacity: 0; }
}
```

**spin-vertically**
```css
@keyframes spin-vertically {
  0% { transform: translateY(0px); }
  40% { transform: translateY(50%); opacity: 0; }
  60% { transform: translateY(-50%); opacity: 0; }
  70% { opacity: 1; }
  100% { transform: translateY(0px); }
}
```

**rotate**
```css
@keyframes rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (8 instances)

```css
.button {
  background-color: rgb(81, 36, 174);
  color: rgb(252, 236, 186);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 2px;
}
```

### Links (42 instances)

```css
.link {
  color: rgb(252, 236, 186);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (9 instances)

```css
.navigatio {
  color: rgb(252, 236, 186);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Footer (1 instances)

```css
.foote {
  color: rgb(252, 236, 186);
  padding-top: 0px;
  padding-bottom: 120px;
  font-size: 16px;
}
```

### Modals (1 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 96px;
  padding-right: 120px;
}
```

### ProgressBars (1 instances)

```css
.progressBar {
  color: rgb(252, 236, 186);
  border-radius: 0px;
  font-size: 16px;
}
```

### Switches (1 instances)

```css
.switche {
  background-color: rgb(81, 36, 174);
  border-radius: 9999px;
  border-color: rgb(252, 236, 186);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(81, 36, 174);
  padding: 0px 0px 0px 0px;
  border-radius: 9999px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(81, 36, 174);
  color: rgb(252, 236, 186);
  padding: 0px 0px 0px 0px;
  border-radius: 9999px;
  border: 1px solid rgb(252, 236, 186);
  font-size: 16px;
  font-weight: 400;
```

### Button — 18 instances, 2 variants

**Variant 1** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(252, 236, 186);
  padding: 0px 32px 0px 32px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(81, 36, 174);
  padding: 0px 32px 0px 32px;
  border-radius: 9999px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 400;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(252, 236, 186);
  padding: 0px 32px 0px 32px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(81, 36, 174);
  padding: 0px 32px 0px 32px;
  border-radius: 9999px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(252, 236, 186);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 500;
```

## Layout System

**24 grid containers** and **65 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 414.656px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 13x |
| 1-column | 7x |
| 7-column | 3x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px;
gap: normal 32px;
grid-template-columns: 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px;
gap: normal 32px;
grid-template-columns: 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px;
gap: normal 32px;
grid-template-columns: 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px;
gap: normal 32px;
grid-template-columns: 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px 57.3281px;
gap: normal 32px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 44x |
| column/nowrap | 15x |
| row-reverse/nowrap | 6x |

**Gap values:** `16px`, `32px normal`, `48px 32px`, `64px`, `8px`, `8px 32px`, `normal 32px`, `normal 7px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 1 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#5124ae` | `#fcecba` | 8.06:1 | AAA |

## Design System Score

**Overall: 96/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 100/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 24 !important rules — prefer specificity over overrides
- 67% of CSS is unused — consider purging
- 782 duplicate CSS declarations

## Z-Index Map

**8 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 20000,20000 | div.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .f.i.x.e.d. .l.e.f.t.-.0. .t.o.p.-.0. .z.-.[.2.0.0.0.0.]. .h.-.s.c.r.e.e.n. .w.-.f.u.l.l. .b.g.-.t.r.a.n.s.p.a.r.e.n.t. .t.r.a.n.s.i.t.i.o.n.-.o.p.a.c.i.t.y |
| dropdown | 100,201 | a.s.c.r.e.e.n. .f.i.x.e.d. .r.i.g.h.t.-.2. .t.o.p.-.2. .z.-.[.1.0.0.]. .f.l.e.x. .i.t.e.m.s.-.e.n.d. .m.d.:.l.e.f.t.-.3. .m.d.:.r.i.g.h.t.-.a.u.t.o. .m.d.:.t.o.p.-.2. .l.g.:.l.e.f.t.-.5. .l.g.:.t.o.p.-.4. .x.l.:.l.e.f.t.-.8. .x.l.:.t.o.p.-.7, ul.z.-.[.1.0.0.]. .h.i.d.d.e.n. .w.-.0. .g.a.p.-.1. .o.v.e.r.f.l.o.w.-.h.i.d.d.e.n. .m.d.:.f.l.e.x. .m.d.:.w.-.a.u.t.o, span.a.b.s.o.l.u.t.e. .b.o.t.t.o.m.-.0. .l.e.f.t.-.0. .z.-.[.1.0.0.]. .h.-.[.c.a.l.c.(.1.0.0.%.+.1.4.p.x.).]. .w.-.[.1.1.0.%.]. .b.g.-.t.e.x.t.-.c.o.l.o.r |
| sticky | 10,50 | a.w.r.a.p.p.e.r. .p.a.r.a.g.r.a.p.h. .p.e.e.r. .f.i.x.e.d. .-.t.o.p.-.f.u.l.l. .z.-.1.0. .f.l.e.x. .w.-.f.u.l.l. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .b.g.-.t.e.x.t.-.c.o.l.o.r. .p.y.-.2. .t.e.x.t.-.b.a.c.k.g.r.o.u.n.d.-.c.o.l.o.r. .f.o.c.u.s.:.t.o.p.-.0, div.s.w.i.p.e.r.-.p.a.g.i.n.a.t.i.o.n. .s.w.i.p.e.r.-.p.a.g.i.n.a.t.i.o.n.-.c.l.i.c.k.a.b.l.e. .s.w.i.p.e.r.-.p.a.g.i.n.a.t.i.o.n.-.b.u.l.l.e.t.s. .s.w.i.p.e.r.-.p.a.g.i.n.a.t.i.o.n.-.h.o.r.i.z.o.n.t.a.l, div.a.b.s.o.l.u.t.e. .l.e.f.t.-.3. .t.o.p.-.1.2. .z.-.5.0. .l.g.:.l.e.f.t.-.5. .l.g.:.t.o.p.-.2.5. .x.l.:.l.e.f.t.-.8. .x.l.:.t.o.p.-.2.0 |
| base | -10,1 | span.b.u.t.t.o.n.-.t.i.m.i.n.g. .a.b.s.o.l.u.t.e. .l.e.f.t.-.0. .t.o.p.-.0. .-.z.-.1.0. .f.l.e.x. .h.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .w.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .t.r.a.n.s.l.a.t.e.-.y.-.f.u.l.l. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .o.v.e.r.f.l.o.w.-.h.i.d.d.e.n. .r.o.u.n.d.e.d.-.f.u.l.l. .p.x.-.4. .t.e.x.t.-.b.a.c.k.g.r.o.u.n.d.-.c.o.l.o.r. .t.r.a.n.s.i.t.i.o.n.-.t.r.a.n.s.f.o.r.m. .d.u.r.a.t.i.o.n.-.3.0.0. .b.e.f.o.r.e.:.a.b.s.o.l.u.t.e. .b.e.f.o.r.e.:.-.l.e.f.t.-.p.x. .b.e.f.o.r.e.:.-.t.o.p.-.p.x. .b.e.f.o.r.e.:.-.z.-.1.0. .b.e.f.o.r.e.:.h.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .b.e.f.o.r.e.:.w.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .b.e.f.o.r.e.:.r.o.u.n.d.e.d.-.t.-.[.c.a.l.c.(.1.0.0.%.*.4.).]. .b.e.f.o.r.e.:.b.g.-.t.e.x.t.-.c.o.l.o.r. .b.e.f.o.r.e.:.t.r.a.n.s.i.t.i.o.n.-.a.l.l. .g.r.o.u.p.-.h.o.v.e.r.:.-.t.r.a.n.s.l.a.t.e.-.y.-.0. .b.e.f.o.r.e.:.g.r.o.u.p.-.h.o.v.e.r.:.r.o.u.n.d.e.d.-.t.-.x.l, span.b.u.t.t.o.n.-.t.i.m.i.n.g. .a.b.s.o.l.u.t.e. .l.e.f.t.-.0. .t.o.p.-.0. .-.z.-.1.0. .f.l.e.x. .h.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .w.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .t.r.a.n.s.l.a.t.e.-.y.-.f.u.l.l. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .o.v.e.r.f.l.o.w.-.h.i.d.d.e.n. .r.o.u.n.d.e.d.-.f.u.l.l. .p.x.-.4. .t.e.x.t.-.b.a.c.k.g.r.o.u.n.d.-.c.o.l.o.r. .t.r.a.n.s.i.t.i.o.n.-.t.r.a.n.s.f.o.r.m. .d.u.r.a.t.i.o.n.-.3.0.0. .b.e.f.o.r.e.:.a.b.s.o.l.u.t.e. .b.e.f.o.r.e.:.-.l.e.f.t.-.p.x. .b.e.f.o.r.e.:.-.t.o.p.-.p.x. .b.e.f.o.r.e.:.-.z.-.1.0. .b.e.f.o.r.e.:.h.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .b.e.f.o.r.e.:.w.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .b.e.f.o.r.e.:.r.o.u.n.d.e.d.-.t.-.[.c.a.l.c.(.1.0.0.%.*.4.).]. .b.e.f.o.r.e.:.b.g.-.t.e.x.t.-.c.o.l.o.r. .b.e.f.o.r.e.:.t.r.a.n.s.i.t.i.o.n.-.a.l.l. .g.r.o.u.p.-.h.o.v.e.r.:.-.t.r.a.n.s.l.a.t.e.-.y.-.0. .b.e.f.o.r.e.:.g.r.o.u.p.-.h.o.v.e.r.:.r.o.u.n.d.e.d.-.t.-.x.l, span.b.u.t.t.o.n.-.t.i.m.i.n.g. .a.b.s.o.l.u.t.e. .l.e.f.t.-.0. .t.o.p.-.0. .-.z.-.1.0. .f.l.e.x. .h.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .w.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .t.r.a.n.s.l.a.t.e.-.y.-.f.u.l.l. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .o.v.e.r.f.l.o.w.-.h.i.d.d.e.n. .r.o.u.n.d.e.d.-.f.u.l.l. .p.x.-.4. .t.e.x.t.-.b.a.c.k.g.r.o.u.n.d.-.c.o.l.o.r. .t.r.a.n.s.i.t.i.o.n.-.t.r.a.n.s.f.o.r.m. .d.u.r.a.t.i.o.n.-.3.0.0. .b.e.f.o.r.e.:.a.b.s.o.l.u.t.e. .b.e.f.o.r.e.:.-.l.e.f.t.-.p.x. .b.e.f.o.r.e.:.-.t.o.p.-.p.x. .b.e.f.o.r.e.:.-.z.-.1.0. .b.e.f.o.r.e.:.h.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .b.e.f.o.r.e.:.w.-.[.c.a.l.c.(.1.0.0.%.+.1.p.x.).]. .b.e.f.o.r.e.:.r.o.u.n.d.e.d.-.t.-.[.c.a.l.c.(.1.0.0.%.*.4.).]. .b.e.f.o.r.e.:.b.g.-.t.e.x.t.-.c.o.l.o.r. .b.e.f.o.r.e.:.t.r.a.n.s.i.t.i.o.n.-.a.l.l. .g.r.o.u.p.-.h.o.v.e.r.:.-.t.r.a.n.s.l.a.t.e.-.y.-.0. .b.e.f.o.r.e.:.g.r.o.u.p.-.h.o.v.e.r.:.r.o.u.n.d.e.d.-.t.-.x.l |

**Issues:**
- [object Object]

## SVG Icons

**4 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| lg | 1 |
| xl | 2 |

**Icon colors:** `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Circular | self-hosted | 400 | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 23 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 6 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (16x), 3:2 (8x), 16:9 (3x), 4:3 (2x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **custom** (69 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `slide-up-enter` | fade | opacity | 1 |

## Component Anatomy

### button — 24 instances

**Slots:** label
**Variants:** outline · link
**Sizes:** md · sm · xl

| variant | count | sample label |
|---|---|---|
| default | 22 | HOPPA ÖVER KARUSELLEN
HOPPA ÖVER KARUSEL |
| outline | 1 | Öppna meny |
| link | 1 | COOKIEINSTÄLLNINGAR |

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Title Case (balanced)

### Top CTA Verbs

- **kontakta** (4)
- **hoppa** (3)
- **v** (2)
- **webbutveckling** (2)
- **design** (2)
- **digitala** (2)
- **apputveckling** (2)
- **projekt** (2)

### Button Copy Patterns

- "kontakta oss" (4×)
- "hoppa över karusellen" (2×)
- "våra tjänster" (2×)
- "webbutveckling" (2×)
- "design" (2×)
- "digitala säljverktyg" (2×)
- "apputveckling" (2×)
- "projekt" (2×)
- "tillbaka till toppen" (2×)
- "öppna meny" (1×)

### Sample Headings

> KREATIV
DIGITAL
BYRÅ
> DIGITALA LÖSNINGAR SOM GÖR AVTRYCK
> UTVALDA PROJEKT
UTVALDA PROJEKT—
UTVALDA PROJEKT—
UTVALDA PROJEKT—
> Kavlås Äng
> Lantmännen Designsystem Webb
> KREATIV
DIGITAL
BYRÅ
> DIGITALA LÖSNINGAR SOM GÖR AVTRYCK
> UTVALDA PROJEKT
UTVALDA PROJEKT—
UTVALDA PROJEKT—
UTVALDA PROJEKT—
> Kavlås Äng
> Lantmännen Designsystem Webb

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Med teknik och design gör vi det svåra enklare och det osynliga synligt. Webb, appar och digitala upplevelser. Hör av dig så pratar vi. 


## Section Roles

Reading order (top→bottom): content → nav → testimonial → nav → feature-grid → feature-grid → testimonial → comparison → feature-grid → feature-grid → feature-grid → feature-grid → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | testimonial | KREATIV
DIGITAL
BYRÅ | 0.8 |
| 3 | content | — | 0.3 |
| 4 | feature-grid | KREATIV
DIGITAL
BYRÅ | 0.8 |
| 5 | feature-grid | DIGITALA LÖSNINGAR SOM GÖR AVTRYCK | 0.8 |
| 6 | testimonial | UTVALDA PROJEKT
UTVALDA PROJEKT—
UTVALDA PROJEKT—
UTVALDA PROJEKT— | 0.8 |
| 7 | comparison | DAGS FÖR NY WEBB?
 | 0.7 |
| 8 | feature-grid | DIGITAL DESIGN SOM GÖR SKILLNAD | 0.8 |
| 9 | feature-grid | DIGITALA SÄLJVERKTYG OCH SHOWROOMS | 0.8 |
| 10 | feature-grid | GÅR NI I APP-TANKAR? | 0.8 |
| 11 | feature-grid | NYFIKEN PÅ VAD VI KAN GÖRA FÖR ER? | 0.8 |
| 12 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.27 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 29, svg 0, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** portrait
**Radius profile on images:** square

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: tailwindcss (0.3)

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Circular` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
