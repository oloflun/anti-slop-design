# Design Language: Real Estate Investment Management Platform | GoCanopy

> Extracted from `https://gocanopy.tech` on September 4, 2026
> 434 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#00ffbb` | rgb(0, 255, 187) | hsl(164, 100%, 50%) | 219 |
| Secondary | `#14323a` | rgb(20, 50, 58) | hsl(193, 49%, 15%) | 213 |
| Accent | `#00ff7f` | rgb(0, 255, 127) | hsl(150, 100%, 50%) | 7 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#f6f5f3` | hsl(40, 14%, 96%) | 231 |
| `#000000` | hsl(0, 0%, 0%) | 114 |
| `#ffffff` | hsl(0, 0%, 100%) | 43 |
| `#979797` | hsl(0, 0%, 59%) | 40 |
| `#cecece` | hsl(0, 0%, 81%) | 32 |
| `#e2dfdf` | hsl(0, 5%, 88%) | 3 |

### Background Colors

Used on large-area elements: `#1a4145`, `#000000`, `#14323a`, `#f6f5f3`, `#02080b`, `#ebe9e5`, `#c5f7e7`, `#94f9dd`, `#62fbd1`, `#00ff7f`

### Text Colors

Text color palette: `#000000`, `#f6f5f3`, `#14323a`, `#00ffbb`, `#ffffff`, `#cecece`, `#e2dfdf`, `#979797`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#f6f5f3` | text, border, background | 231 |
| `#00ffbb` | background, text, border | 219 |
| `#14323a` | text, border, background | 213 |
| `#000000` | text, border, background | 114 |
| `#ffffff` | border, text, background | 43 |
| `#979797` | text, border | 40 |
| `#cecece` | text, border | 32 |
| `#00ff7f` | border, background | 7 |
| `#041b19` | border, background | 6 |
| `#e2dfdf` | background, text, border | 3 |
| `#1a4145` | background | 2 |
| `#c5f7e7` | background | 1 |
| `#94f9dd` | background | 1 |
| `#62fbd1` | background | 1 |

## Typography

### Font Families

- **Season Sans** — used for all (383 elements)
- **Test Sohne Mono** — used for all (29 elements)
- **Season Serif** — used for all (22 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 81px | 5.0625rem | 400 | 89.1px | -2.187px | h1 |
| 53px | 3.3125rem | 400 | 60px | -1.325px | h2, div, br |
| 36px | 2.25rem | 400 | 64px | -0.9px | div |
| 24px | 1.5rem | 400 | 31.2px | normal | h3, br |
| 20px | 1.25rem | 400 | 20px | normal | span, p, br, i |
| 18px | 1.125rem | 500 | 18px | normal | span |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |
| 14px | 0.875rem | 500 | 20px | normal | a, div, button, svg |
| 12px | 0.75rem | 500 | 16px | normal | div, br, span |
| 11px | 0.6875rem | 400 | 16px | normal | div, span, ul, li |

### Heading Scale

```css
h1 { font-size: 81px; font-weight: 400; line-height: 89.1px; }
h2 { font-size: 53px; font-weight: 400; line-height: 60px; }
h3 { font-size: 24px; font-weight: 400; line-height: 31.2px; }
h6 { font-size: 16px; font-weight: 400; line-height: 24px; }
h5 { font-size: 14px; font-weight: 500; line-height: 20px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 500; line-height: 20px; }
```

### Font Weights in Use

`400` (308x), `500` (124x), `600` (2x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-24 | 24px | 1.5rem |
| spacing-36 | 36px | 2.25rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-60 | 60px | 3.75rem |
| spacing-64 | 64px | 4rem |
| spacing-71 | 71px | 4.4375rem |
| spacing-80 | 80px | 5rem |
| spacing-88 | 88px | 5.5rem |
| spacing-112 | 112px | 7rem |
| spacing-128 | 128px | 8rem |
| spacing-160 | 160px | 10rem |
| spacing-175 | 175px | 10.9375rem |
| spacing-241 | 241px | 15.0625rem |
| spacing-320 | 320px | 20rem |
| spacing-350 | 350px | 21.875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 1 |
| md | 8px | 5 |
| lg | 12px | 3 |
| lg | 16px | 14 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 4.16px 6.24px -4.16px, rgba(0, 0, 0, 0.1) 0px 10.4px 15.6px -3.12px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.35) 0px 16px 40px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.298003 -0.0303611 -0.0234222 / 0.05) 0px 1px 3px 0px, oklab(0.298003 -0.0303611 -0.0234222 / 0.05) 0px 1px 2px -1px;
```

## CSS Custom Properties

### Colors

```css
--color-foreground-alt: #1a4145;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--color-green-600: oklch(62.7% .194 149.214);
--color-accent-2: #94f9dd;
--tw-inset-ring-shadow: 0 0 #0000;
--color-secondary: #e2dfdf;
--color-brand: #235c58;
--color-ice: #eaebe6;
--tw-ring-offset-color: #fff;
--color-muted: #979797;
--color-white: #fff;
--tw-border-style: solid;
--color-background: #f6f5f3;
--color-red-500: oklch(63.7% .237 25.331);
--tw-ring-offset-width: 0px;
--color-primary: #0fb;
--color-black: #000;
--color-foreground: #14323a;
--color-accent-3: #62fbd1;
--color-accent-1: #c5f7e7;
```

### Spacing

```css
--spacing: .25rem;
```

### Typography

```css
--text-2xl: 1.5rem;
--leading-snug: 1.375;
--text-lg: 1.125rem;
--text-5xl--line-height: 1;
--text-2xl--line-height: 1.33333;
--leading-normal: 1.5;
--text-base--line-height: 1.5;
--font-mono: "Test Sohne Mono",serif;
--tracking-wider: .05em;
--text-xl--line-height: 1.4;
--font-weight-semibold: 600;
--text-sm: .875rem;
--text-lg--line-height: 1.55556;
--leading-tight: 1.25;
--font-sans: "Season Sans",serif;
--text-4xl: 2.25rem;
--text-sm--line-height: 1.42857;
--text-3xl--line-height: 1.2;
--text-5xl: 3rem;
--text-3xl: 1.875rem;
--text-xs: .75rem;
--text-xs--line-height: 1.33333;
--default-font-family: "Season Sans",serif;
--font-weight-medium: 500;
--font-weight-normal: 400;
--font-display: "Season Serif",serif;
--text-xl: 1.25rem;
--text-4xl--line-height: 1.11111;
--leading-loose: 2;
--text-base: 1rem;
--default-mono-font-family: "Test Sohne Mono",serif;
```

### Shadows

```css
--tw-inset-shadow-alpha: 100%;
--drop-shadow-md: 0 3px 3px #0000001f;
--tw-drop-shadow-alpha: 100%;
--tw-inset-shadow: 0 0 #0000;
--tw-shadow-alpha: 100%;
--tw-shadow: 0 0 #0000;
```

### Radii

```css
--radius-xl: .75rem;
--radius-2xl: 1rem;
--radius-md: .375rem;
--radius-lg: .5rem;
```

### Other

```css
--container-md: 28rem;
--aspect-video: 16/9;
--default-transition-timing-function: cubic-bezier(.4,0,.2,1);
--container-5xl: 64rem;
--tw-translate-z: 0;
--tw-scale-y: 1;
--container-3xl: 48rem;
--tw-translate-y: 0;
--blur-md: 12px;
--ease-out: cubic-bezier(0,0,.2,1);
--tw-divide-y-reverse: 0;
--tw-scale-z: 1;
--container-sm: 24rem;
--tw-translate-x: 0;
--tw-scale-x: 1;
--default-transition-duration: .15s;
--container-xl: 36rem;
--blur-sm: 8px;
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
| md | 768px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.15s`, `0.3s`, `0.4s`, `0.5s`

### Common Transitions

```css
transition: all;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.3s cubic-bezier(0, 0, 0.2, 1);
transition: transform 0.3s cubic-bezier(0, 0, 0.2, 1), translate 0.3s cubic-bezier(0, 0, 0.2, 1), scale 0.3s cubic-bezier(0, 0, 0.2, 1), rotate 0.3s cubic-bezier(0, 0, 0.2, 1);
transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), translate 0.3s cubic-bezier(0.4, 0, 0.2, 1), scale 0.3s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.3s cubic-bezier(0.4, 0, 0.2, 1), filter 0.3s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.3s cubic-bezier(0.4, 0, 0.2, 1), display 0.3s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.3s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.3s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.4s;
transition: 0.3s;
transition: 0.5s;
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (8 instances)

```css
.button {
  background-color: oklab(0 0 0 / 0.35);
  color: rgb(246, 245, 243);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (14 instances)

```css
.card {
  background-color: rgb(20, 50, 58);
  border-radius: 16px;
  box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.298003 -0.0303611 -0.0234222 / 0.05) 0px 1px 3px 0px, oklab(0.298003 -0.0303611 -0.0234222 / 0.05) 0px 1px 2px -1px;
  padding-top: 16px;
  padding-right: 12px;
}
```

### Links (31 instances)

```css
.link {
  color: rgb(246, 245, 243);
  font-size: 14px;
  font-weight: 500;
}
```

### Navigation (2 instances)

```css
.navigatio {
  color: rgb(246, 245, 243);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (2 instances)

```css
.foote {
  background-color: rgb(20, 50, 58);
  color: rgb(246, 245, 243);
  padding-top: 0px;
  padding-bottom: 659px;
  font-size: 16px;
}
```

### Accordions (2 instances)

```css
.accordion {
  color: rgb(151, 151, 151);
  font-size: 14px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(151, 151, 151);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(20, 50, 58);
  padding: 0px 0px 0px 0px;
  border-radius: 3.35544e+07px;
  border: 0px solid rgb(20, 50, 58);
  font-size: 16px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(246, 245, 243);
  padding: 8px 8px 8px 8px;
  border-radius: 0px;
  border: 0px solid rgb(246, 245, 243);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: oklab(0 0 0 / 0.35);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 12px;
  border: 0px solid rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 255, 187);
  padding: 12px 18px 12px 18px;
  border-radius: 0px;
  border: 0px solid rgb(0, 255, 187);
  font-size: 14px;
  font-weight: 500;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(20, 50, 58);
  padding: 12px 0px 12px 0px;
  border-radius: 0px;
  border: 0px solid rgb(20, 50, 58);
  font-size: 20px;
  font-weight: 500;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(197, 247, 231);
  color: rgb(20, 50, 58);
  padding: 40px 50px 36px 50px;
  border-radius: 16px;
  border: 0px solid rgb(20, 50, 58);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 255, 187);
  padding: 48px 32px 32px 32px;
  border-radius: 16px;
  border: 1px solid rgb(0, 255, 187);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 255, 187);
  padding: 48px 32px 32px 32px;
  border-radius: 16px;
  border: 1px solid rgb(0, 255, 187);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(206, 206, 206);
  padding: 16px 12px 16px 12px;
  border-radius: 16px;
  border: 1px solid rgb(0, 255, 187);
  font-size: 16px;
  font-weight: 500;
```

## Layout System

**5 grid containers** and **96 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1440px | 40px |
| 886px | 0px |
| 768px | 0px |
| 590px | 0px |
| 400px | 0px |
| 544px | 0px |
| 1280px | 0px |
| 650px | 0px |
| 668px | 0px |
| 501px | 0px |
| 588px | 0px |
| 1020px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 2x |
| 1-column | 1x |
| 12-column | 1x |
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 472px 472px 472px;
gap: 32px;
grid-template-columns: 378.656px 378.672px 378.656px;
gap: 32px;
grid-template-columns: 98px 98px 98px 98px 98px 98px 98px 98px 98px 98px 98px 98px;
grid-template-columns: 155px 155px;
gap: 80px;
grid-template-columns: 24px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 61x |
| column/nowrap | 35x |

**Gap values:** `10px`, `112px`, `12px`, `16px`, `20px`, `243px`, `24px`, `28px`, `30px`, `32px`, `36px`, `40px`, `64px`, `6px`, `71px`, `80px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 92/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 90/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 18 !important rules — prefer specificity over overrides
- 616 duplicate CSS declarations

## Z-Index Map

**6 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | div.r.e.l.a.t.i.v.e. .z.-.1.0. .m.x.-.4. .m.y.-.6. .r.o.u.n.d.e.d.-.l.g. .w.-.f.u.l.l. .b.g.-.f.o.r.e.g.r.o.u.n.d. .t.e.x.t.-.b.a.c.k.g.r.o.u.n.d. .o.v.e.r.f.l.o.w.-.h.i.d.d.e.n. .s.h.a.d.o.w.-.2.x.l. .b.o.r.d.e.r. .b.o.r.d.e.r.-.p.r.i.m.a.r.y./.1.0, header.w.-.f.u.l.l. .f.i.x.e.d. .t.o.p.-.4. .m.d.:.t.o.p.-.6. .i.n.s.e.t.-.x.-.0. .z.-.3.0. .w.i.l.l.-.c.h.a.n.g.e.-.t.r.a.n.s.f.o.r.m, div.f.i.x.e.d. .i.n.s.e.t.-.0. .z.-.4.0. .o.p.a.c.i.t.y.-.0. .p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .f.l.e.x. .i.t.e.m.s.-.e.n.d |
| base | -10,0 | div.a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .-.z.-.1.0. .s.i.z.e.-.f.u.l.l. .b.g.-.f.o.r.e.g.r.o.u.n.d, img.a.b.s.o.l.u.t.e. .s.i.z.e.-.f.u.l.l. .i.n.s.e.t.-.0. .-.z.-.1.0, div.a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .-.z.-.1.0 |

## SVG Icons

**13 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 3 |
| md | 1 |
| lg | 4 |
| xl | 5 |

**Icon colors:** `#F6F5F3`, `white`, `currentColor`, `#00FFBB`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Season Serif | self-hosted | 400 | normal |
| Season Sans | self-hosted | 400, 500, 600 | normal |
| Test Sohne Mono | self-hosted | 400, 500 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 7 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 3 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 3 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (5x), 3:4 (3x), 5.5:1 (2x), 0.03:1 (1x), 9:16 (1x), 3:2 (1x), 16:9 (1x), 5.01:1 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **custom** (8 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (16 uses) — `cubic-bezier(0, 0, 0.2, 1)`

## Component Anatomy

### card — 10 instances

**Slots:** heading, description, footer
**Variants:** primary
**Sizes:** md · xl

| variant | count | sample label |
|---|---|---|
| primary | 7 | Decision-ready
intelligence
FROM FIRST P |
| default | 3 | 1
Ingest and Structure

Upload any deal  |

### button — 7 instances

**Slots:** label
**Variants:** outline · primary
**Sizes:** xl · sm

| variant | count | sample label |
|---|---|---|
| default | 5 | × |
| outline | 1 | Click to play |
| primary | 1 | Download Executive Summary |

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **download** (2)
- **click** (1)

### Button Copy Patterns

- "download executive summary" (2×)
- "×" (1×)
- "click to play" (1×)

### Sample Headings

> From scattered data to institutional intelligence
> Trusted by
leading companies
> When fragmented data hides the full picture
> Turn fragmented sources into institutional intelligence
> Ingest and Structure
> From scattered data to institutional intelligence
> Trusted by
leading companies
> When fragmented data hides the full picture
> Turn fragmented sources into institutional intelligence
> Ingest and Structure

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** AI-native investment platform for institutional real estate teams. Automate workflows, preserve institutional memory, and make faster, defensible decisions.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): content → hero → cta → nav → nav → logo-wall → content → content → content → testimonial → content → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | cta | — | 0.75 |
| 2 | nav | — | 0.9 |
| 3 | content | From scattered data to institutional intelligence | 0.3 |
| 4 | hero | From scattered data to institutional intelligence | 0.85 |
| 5 | logo-wall | Trusted by
leading companies | 0.85 |
| 6 | content | When fragmented data hides the full picture | 0.3 |
| 7 | content | Turn fragmented sources into institutional intelligence | 0.3 |
| 8 | content | Evidence from
institutional investors | 0.3 |
| 9 | testimonial | "GoCanopy delivers instant, consultant-grade analysis with verifiable sources th | 0.8 |
| 10 | content | Security | 0.3 |
| 11 | content | Turn fragmented data into complete, consistent, and defensible intelligence | 0.3 |
| 12 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.384 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 16px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `mixed` (confidence 0.2)
**Counts:** total 15, svg 9, icon 6, screenshot-like 0, photo-like 6
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: tailwindcss (0.3)

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Season Sans` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
