# Design Language: dope.security – The Fly-Direct Secure Web Gateway with AI DLP

> Extracted from `https://dope.security` on September 4, 2026
> 5000 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#edc3c4` | rgb(237, 195, 196) | hsl(359, 54%, 85%) | 3 |
| Secondary | `#f7f9fa` | rgb(247, 249, 250) | hsl(200, 23%, 97%) | 9140 |
| Accent | `#af50ff` | rgb(175, 80, 255) | hsl(273, 100%, 66%) | 3 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#f0f0f0` | hsl(0, 0%, 94%) | 348 |
| `#000000` | hsl(0, 0%, 0%) | 124 |
| `#090909` | hsl(0, 0%, 4%) | 48 |
| `#333333` | hsl(0, 0%, 20%) | 13 |
| `#475467` | hsl(216, 18%, 34%) | 5 |
| `#344054` | hsl(218, 24%, 27%) | 3 |
| `#dae0e8` | hsl(214, 23%, 88%) | 1 |
| `#d0d5dd` | hsl(217, 16%, 84%) | 1 |
| `#878787` | hsl(0, 0%, 53%) | 1 |

### Background Colors

Used on large-area elements: `#090909`, `#ffffff`, `#000000`

### Text Colors

Text color palette: `#000000`, `#333333`, `#f7f9fa`, `#475467`, `#ffffff`, `#344054`, `#af50ff`, `#f0f0f0`, `#090909`

### Gradients

```css
background-image: linear-gradient(135deg, rgb(102, 126, 234) 0%, rgb(118, 75, 162) 100%);
```

```css
background-image: linear-gradient(rgba(16, 21, 27, 0.7), rgba(16, 21, 27, 0.7));
```

```css
background-image: radial-gradient(circle closest-corner at 10% 50%, rgb(108, 75, 214), rgba(0, 0, 0, 0) 55%);
```

```css
background-image: linear-gradient(90deg, rgba(9, 9, 9, 0.75), rgba(0, 0, 0, 0) 51%), linear-gradient(0deg, rgb(9, 9, 9), rgba(0, 0, 0, 0) 21%);
```

```css
background-image: linear-gradient(90deg, rgba(9, 9, 9, 0.75), rgba(0, 0, 0, 0) 51%), linear-gradient(0deg, rgb(9, 9, 9) 2%, rgba(0, 0, 0, 0) 32%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0) 83%, rgba(0, 0, 0, 0.78));
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.05)), linear-gradient(rgba(16, 21, 27, 0.7), rgba(16, 21, 27, 0.7));
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0));
```

```css
background-image: url("https://cdn.prod.website-files.com/623381c2c01066b228a1670b/66a84f0d684fecbb44da24bf_timeline-4-background-radial-gradient.webp");
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#f7f9fa` | text, border, background | 9140 |
| `#f0f0f0` | text, border | 348 |
| `#000000` | text, border, background | 124 |
| `#090909` | background, text, border | 48 |
| `#333333` | text, border | 13 |
| `#475467` | text, border | 5 |
| `#344054` | text, border | 3 |
| `#af50ff` | text, border | 3 |
| `#edc3c4` | background | 3 |
| `#dae0e8` | border | 1 |
| `#d0d5dd` | border | 1 |
| `#7f56d9` | border | 1 |
| `#878787` | background | 1 |

## Typography

### Font Families

- **Whyte Inktrap** — used for all (4561 elements)
- **Whyte Inktrap Mono** — used for all (351 elements)
- **GrandSlang** — used for body (6 elements)
- **Karla** — used for body (2 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 88px | 5.5rem | 500 | 70.4px | -2.64px | h1, span, br |
| 80px | 5rem | 700 | 72px | -5.6px | h2, div, span, svg |
| 64px | 4rem | 400 | 57.6px | 12.8px | h3, span |
| 48px | 3rem | 400 | 57.6px | normal | h2 |
| 40px | 2.5rem | 400 | 40px | normal | div, br, span |
| 32px | 2rem | 400 | 38.4px | normal | h3 |
| 28px | 1.75rem | 700 | 33.6px | -0.28px | p, br, div |
| 24px | 1.5rem | 400 | 36px | normal | div, a, script |
| 20px | 1.25rem | 700 | 20px | 0.08px | span, p, br, div |
| 18.4px | 1.15rem | 400 | 24.84px | 0.12px | div |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14px | 0.875rem | 300 | 21px | normal | div, p, script |
| 13.6px | 0.85rem | 300 | 19.04px | 1.12px | h4 |
| 12px | 0.75rem | 700 | 0px | normal | sup, div |
| 11.2px | 0.7rem | 400 | 11.2px | normal | div, a, svg, path |

### Heading Scale

```css
h1 { font-size: 88px; font-weight: 500; line-height: 70.4px; }
h2 { font-size: 80px; font-weight: 700; line-height: 72px; }
h3 { font-size: 64px; font-weight: 400; line-height: 57.6px; }
h2 { font-size: 48px; font-weight: 400; line-height: 57.6px; }
h3 { font-size: 32px; font-weight: 400; line-height: 38.4px; }
h4 { font-size: 13.6px; font-weight: 300; line-height: 19.04px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (4923x), `700` (31x), `300` (25x), `600` (6x), `500` (4x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-24 | 24px | 1.5rem |
| spacing-32 | 32px | 2rem |
| spacing-38 | 38px | 2.375rem |
| spacing-45 | 45px | 2.8125rem |
| spacing-64 | 64px | 4rem |
| spacing-72 | 72px | 4.5rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-128 | 128px | 8rem |
| spacing-136 | 136px | 8.5rem |
| spacing-160 | 160px | 10rem |
| spacing-208 | 208px | 13rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 4 |
| md | 8px | 39 |
| lg | 11px | 2 |
| xl | 19px | 13 |
| xl | 24px | 1 |
| full | 50px | 1 |
| full | 100px | 1 |
| full | 1584px | 4 |

## Box Shadows

**xs (inset)** — blur: 0px
```css
box-shadow: rgb(175, 80, 255) -0.5px -0.5px 0px 0px inset, rgb(175, 80, 255) -1px 2px 0px -2px inset, rgb(175, 80, 255) -1px 0px 0px -0.1px inset;
```

**xs** — blur: 1px
```css
box-shadow: rgba(16, 24, 40, 0.06) 0px 1px 1px 0px, rgba(16, 24, 40, 0.1) 0px 1px 2px 0px;
```

**xs** — blur: 2px
```css
box-shadow: rgba(16, 24, 40, 0.05) 0px 1px 2px 0px;
```

**sm** — blur: 3.2px
```css
box-shadow: rgba(0, 0, 0, 0.25) 0px 3.2px 3.2px 0px;
```

**lg** — blur: 20px
```css
box-shadow: rgba(102, 126, 234, 0.3) 0px 4px 20px 0px;
```

**lg** — blur: 16px
```css
box-shadow: rgba(0, 0, 0, 0.08) 0px 12px 16px -4px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px;
```

## CSS Custom Properties

### Colors

```css
--nav-bg-color: #333248b3;
--untitled-ui--primary600: #7f56d9;
--untitled-ui--primary700: #6941c6;
--untitled-ui--primary100: #f4ebff;
--swiper-theme-color: #007aff;
```

### Spacing

```css
--spacing-layout--row-col-gap: 40px;
--spacing-layout--row-col-gap-sm: 32px;
--grid-gap-split: calc(var(--spacing-layout--row-col-gap)/2);
--swiper-navigation-size: 44px;
```

### Other

```css
--white: white;
--white-a75: #ffffffbf;
--white-a40: #fff6;
--grape: #373160;
--white-a10: #ffffff1a;
--almost-white: #f7f9fa;
--white-a20: #fff3;
--bright-pink: #fe2357;
--almost-black: #10151b;
--dark: #1b1b1b;
--bright-purple: #af50ff;
--black: black;
--bright-gray: #919699;
--dot-yellow: #facc39;
--dot-salmon: #ff685f;
--dot-turquoise: #5ed9c3;
--dot-salmon-a20: #ff685f33;
--dot-yellow-a20: #facc3933;
--dot-turquoise-a20: #5ed9c333;
--dark-indigo: #262a31;
--links: #00aeea;
--emerald: #00d37e;
--medium-gray: #5e6366;
--silver: #c5c5c5;
--indigo-grey: #333248;
--transparent: #fff0;
--nn--background: #090909;
--untitled-ui--white: white;
--untitled-ui--gray600: #475467;
--untitled-ui--gray50: #f9fafb;
--untitled-ui--gray700: #344054;
--untitled-ui--gray300: #d0d5dd;
--untitled-ui--gray800: #1d2939;
--untitled-ui--gray100: #f2f4f7;
--untitled-ui--success50: #ecfdf3;
--untitled-ui--success700: #027a48;
--untitled-ui--gray200: #eaecf0;
--untitled-ui--gray500: #667085;
--untitled-ui--gray900: #101828;
--black-a20: #0003;
--nn--white: white;
--type-weight--100: 100;
--type-weight--200: 200;
--type-weight--300: 300;
--type-weight--400: 400;
--type-weight--500: 500;
--type-weight--600: 600;
--type-weight--700: 700;
--type-weight--800: 800;
--type-weight--900: 900;
```

### Dependencies

```css
--grid-gap-split: --spacing-layout--row-col-gap;
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
| sm | 480px | min-width |
| sm | 600px | max-width |
| md | 767px | max-width |
| md | 768px | max-width |
| lg | 991px | max-width |
| lg | 992px | min-width |
| xl | 1280px | min-width |
| 1440px | 1440px | min-width |
| 1920px | 1920px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.15s`, `0.3s`, `0.1s`, `0.2s`, `0.6s`

### Common Transitions

```css
transition: all;
transition: 0.15s;
transition: 0.3s;
transition: 0.1s;
transition: 0.2s;
transition: background-color 0.6s cubic-bezier(0.23, 1, 0.32, 1);
transition: background-color 0.15s, box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1);
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**ds-cta-pulse**
```css
@keyframes ds-cta-pulse {
  0% { transform: scale(1); }
  35% { transform: scale(1.045); }
  100% { transform: scale(1); }
}
```

**pulse-click-now**
```css
@keyframes pulse-click-now {
  100% { box-shadow: rgba(232, 76, 61, 0) 0px 0px 0px 18px; }
}
```

**pulse-click-now**
```css
@keyframes pulse-click-now {
  100% { box-shadow: rgba(232, 76, 61, 0) 0px 0px 0px 18px; }
}
```

**shimmer**
```css
@keyframes shimmer {
  0% { background-position: -100% 0px; }
  100% { background-position: 200% 0px; }
}
```

**sparkle**
```css
@keyframes sparkle {
  0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); }
  50% { opacity: 0.7; transform: scale(1.15) rotate(10deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (11 instances)

```css
.button {
  background-color: rgba(237, 195, 196, 0.05);
  color: rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 600;
  padding-top: 10px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (47 instances)

```css
.card {
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 3.2px 3.2px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (44 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (88 instances)

```css
.navigatio {
  background-color: rgba(255, 255, 255, 0.1);
  color: rgb(247, 249, 250);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
  box-shadow: rgba(0, 0, 0, 0.08) 0px 12px 16px -4px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px;
}
```

### Modals (4 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (54 instances)

```css
.dropdown {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.08) 0px 12px 16px -4px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px;
  border-color: rgb(247, 249, 250);
  padding-top: 0px;
}
```

### Badges (3 instances)

```css
.badge {
  background-color: rgba(247, 249, 250, 0.08);
  color: rgb(247, 249, 250);
  font-size: 12px;
  font-weight: 400;
  padding-top: 9px;
  padding-right: 15px;
  border-radius: 6px;
}
```

### Switches (2 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(71, 84, 103);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0.1);
  color: rgb(255, 255, 255);
  padding: 10px 18px 10px 18px;
  border-radius: 4px;
  border: 0px none rgb(127, 86, 217);
  font-size: 16px;
  font-weight: 600;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(71, 84, 103);
  padding: 10px 18px 10px 18px;
  border-radius: 4px;
  border: 1px solid rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 600;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 24px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Other — 9 instances, 1 variant

**Variant 1** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 19.2px;
  border: 1px solid rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 5 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgba(247, 249, 250, 0.25);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgba(247, 249, 250, 0.25);
  font-size: 88px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 19.2px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 249, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 249, 250);
  font-size: 16px;
  font-weight: 400;
```

### Link — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 21.125px 21.125px 21.125px 21.125px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**14 grid containers** and **71 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 2240px | 64px |
| 45% | 20px |
| 50% | 20px |
| 100% | 20px |
| 768px | 64px |
| 700.96px | 0px |
| 754.88px | 0px |
| 2150.4px | 0px |
| 800px | 0px |
| 384px | 0px |
| 1280px | 64px |
| 657.6px | 0px |
| 1600px | 64px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 9x |
| 2-column | 5x |

### Grid Templates

```css
grid-template-columns: 1152px;
gap: 128px;
grid-template-columns: 700.953px;
gap: 128px;
grid-template-columns: 700.953px;
gap: 128px;
grid-template-columns: 652.172px;
gap: 128px;
grid-template-columns: 700.953px;
gap: 128px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 53x |
| row/wrap | 6x |
| column/nowrap | 12x |

**Gap values:** `0px 16px`, `0px 24px`, `0px 64px`, `10px`, `128px`, `12px`, `15px`, `16px`, `24px`, `32px`, `64px`, `72px`, `8px 24px`, `normal 8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 82/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 90/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 607 !important rules — prefer specificity over overrides
- 94% of CSS is unused — consider purging
- 28005 duplicate CSS declarations

## Gradients

**10 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 135deg | 2 | brand |
| linear | — | 2 | brand |
| radial | circle closest-corner at 10% 50% | 2 | brand |
| linear | 90deg | 2 | brand |
| linear | 0deg | 2 | brand |
| linear | 0deg | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 1 | subtle |

```css
background: linear-gradient(135deg, rgb(102, 126, 234) 0%, rgb(118, 75, 162) 100%);
background: linear-gradient(rgba(16, 21, 27, 0.7), rgba(16, 21, 27, 0.7));
background: radial-gradient(circle closest-corner at 10% 50%, rgb(108, 75, 214), rgba(0, 0, 0, 0) 55%);
background: linear-gradient(90deg, rgba(9, 9, 9, 0.75), rgba(0, 0, 0, 0) 51%);
background: linear-gradient(0deg, rgb(9, 9, 9), rgba(0, 0, 0, 0) 21%);
```

## Z-Index Map

**15 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,900 | div.h.e.r.o._.s.t.r.i.p. .c.o.n.t.a.i.n.e.r._.n.e.w, div.c.u.s.t.o.m._.c.u.r.s.o.r.-.w.r.a.p, div.u.u.i.-.n.a.v.b.a.r.0.8._.m.e.n.u.-.d.r.o.p.d.o.w.n. .w.-.d.r.o.p.d.o.w.n |
| sticky | 10,99 | div.s.c.r.o.l.l.e.r.-.s.e.c.t.i.o.n._._.p.a.t.h. .w.-.e.m.b.e.d, div.s.c.r.o.l.l.e.r.-.s.e.c.t.i.o.n._._.s.t.i.c.k.y.-.c.o.n.t.e.n.t. .t.0, div.s.c.r.o.l.l.e.r.-.s.e.c.t.i.o.n._._.s.t.i.c.k.y.-.c.o.n.t.e.n.t |
| base | -100,9 | video, div.n.a.v.-.b.l.u.r.-.d.i.v, div.n.a.v.-.b.l.u.r.-.d.i.v._.t.e.s.t |

## SVG Icons

**15 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 2 |
| md | 1 |
| lg | 1 |
| xl | 10 |

**Icon colors:** `currentColor`, `rgb(0, 0, 0)`, `white`, `#F7F9FA`, `#E1BDFF`, `#090909`, `#D4A0FF`, `#AF50FF`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | normal | normal |
| Cositimes roman | self-hosted | 400 | normal |
| Whyte Inktrap | self-hosted | 300, 400, 500, 700 | normal |
| Acumin Pro Wide Bold | self-hosted | 700 | normal |
| GrandSlang | self-hosted | 400 | italic, normal |
| Whyte Inktrap Mono | self-hosted | 400 | normal |
| Fontawesome 6 Pro Solid | self-hosted | 400 | normal |
| ballinger-mono | self-hosted | 400, 700 | normal |
| Karla | google-fonts | 300, 400, 500, 600, 700 | normal |
| swiper-icons | self-hosted | 400 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 7 | objectFit: contain, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: contain, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (2x), 1:1 (2x), 11.5:1 (1x), 2.63:1 (1x), 0.15:1 (1x), 16:9 (1x), 3.93:1 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `600ms` | 600 |

### Easing Families

- **ease-out** (9 uses) — `cubic-bezier(0.23, 1, 0.32, 1)`, `cubic-bezier(0.165, 0.84, 0.44, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `sparkle` | reveal | opacity, transform | 1 |

## Component Anatomy

### card — 31 instances

**Slots:** media

### other — 9 instances


### button — 4 instances

**Slots:** label
**Variants:** tertiary

| variant | count | sample label |
|---|---|---|
| default | 3 | BOOK A DEMO
LOG IN |
| tertiary | 1 | LOG IN |

### link — 4 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Title Case (tight)

### Top CTA Verbs

- **book** (2)
- **log** (1)
- **see** (1)
- **data** (1)
- **complex** (1)
- **blocking** (1)
- **outages** (1)

### Button Copy Patterns

- "book a demo
log in" (1×)
- "book a demo" (1×)
- "log in" (1×)
- "see how in 140s" (1×)
- "data center
downtime alert
vs. zscaler
01" (1×)
- "complex 15-step
configuration
vs. netskope
02" (1×)
- "blocking at
the dns level
vs. cisco umbrella
03" (1×)
- "outages
galore
vs. forcepoint
04" (1×)

### Sample Headings

> Your new Secure Web Gateway
withAI DLP

> Features
> SSL INSPECTION
> SSL INSPECTION
> URL FILTERING
> URL FILTERING
> Features
> SSL INSPECTION
> SSL INSPECTION
> URL FILTERING

## Page Intent

**Type:** `landing` (confidence 0.59)
**Description:** The next-gen Secure Web Gateway: on-device proxy with local SSL inspection, AI DLP monitoring, and SSE capabilities for secure direct internet access.

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): logo-wall → nav → nav → hero → content → nav → comparison → content → content → content → content → comparison

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | logo-wall | — | 0.85 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | hero | Your new Secure Web Gateway
withAI DLP
 | 0.85 |
| 5 | comparison | Features | 0.7 |
| 6 | content | Features | 0.3 |
| 7 | content | — | 0.3 |
| 8 | content | — | 0.3 |
| 9 | content | Whether your company is small or large, we provide a first-class experience. | 0.3 |
| 10 | content | Experience
the
Trilogy | 0.3 |
| 11 | comparison | How we compare | 0.7 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.176 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 1584px |
| backdrop-filter in use | no |
| Gradients | 10 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.278)
**Counts:** total 9, svg 5, icon 2, screenshot-like 0, photo-like 1
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Component Library

**Detected:** `bootstrap` (confidence 0.6)

Evidence:
- bootstrap utility hits: 3

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Whyte Inktrap` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
