# Design Language: Webbyrå Göteborg | Prisvärd webbutveckling | Highway Media

> Extracted from `https://highwaymedia.se/webbyra-goteborg/` on September 15, 2026
> 936 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#624058` | rgb(98, 64, 88) | hsl(318, 21%, 32%) | 108 |
| Secondary | `#ec8aa3` | rgb(236, 138, 163) | hsl(345, 72%, 73%) | 9 |
| Accent | `#d4edda` | rgb(212, 237, 218) | hsl(134, 41%, 88%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#232323` | hsl(0, 0%, 14%) | 1439 |
| `#000000` | hsl(0, 0%, 0%) | 206 |
| `#ffffff` | hsl(0, 0%, 100%) | 75 |
| `#495057` | hsl(210, 9%, 31%) | 33 |
| `#929292` | hsl(0, 0%, 57%) | 17 |
| `#656565` | hsl(0, 0%, 40%) | 16 |
| `#dee2e6` | hsl(210, 14%, 89%) | 12 |
| `#cccccc` | hsl(0, 0%, 80%) | 7 |
| `#333333` | hsl(0, 0%, 20%) | 6 |
| `#ffe8ee` | hsl(344, 100%, 95%) | 3 |
| `#4c8076` | hsl(168, 25%, 40%) | 1 |
| `#111111` | hsl(0, 0%, 7%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#000000`, `#f7f7f7`

### Text Colors

Text color palette: `#000000`, `#232323`, `#624058`, `#222222`, `#ec8aa3`, `#ffffff`, `#495057`, `#155724`, `#4a4a4a`, `#333333`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#232323` | text, border, background | 1439 |
| `#000000` | text, border, background | 206 |
| `#624058` | text, border, background | 108 |
| `#ffffff` | background, text, border | 75 |
| `#495057` | text, border | 33 |
| `#929292` | text, border, background | 17 |
| `#656565` | text, border | 16 |
| `#dee2e6` | border | 12 |
| `#ec8aa3` | background, text, border | 9 |
| `#cccccc` | border, background | 7 |
| `#333333` | text, border | 6 |
| `#ffe8ee` | background | 3 |
| `#4c8076` | background | 1 |
| `#111111` | border | 1 |
| `#155724` | text | 1 |
| `#d4edda` | background | 1 |
| `#c3e6cb` | border | 1 |

## Typography

### Font Families

- **Inter** — used for body (770 elements)
- **Outfit** — used for all (72 elements)
- **Open Sans** — used for body (8 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 102.4px | 6.4rem | 600 | 153.6px | normal | li |
| 84px | 5.25rem | 600 | 100.8px | normal | h1 |
| 60px | 3.75rem | 600 | 90px | normal | div |
| 56px | 3.5rem | 600 | 60px | normal | a |
| 54px | 3.375rem | 600 | 64.8px | normal | h2 |
| 42px | 2.625rem | 600 | 50.4px | normal | h3 |
| 34px | 2.125rem | 600 | 40.8px | normal | h4 |
| 30px | 1.875rem | 600 | 45px | normal | div, h5, a, img |
| 26px | 1.625rem | 600 | 39px | normal | p, a, br |
| 25.6px | 1.6rem | 600 | 30.72px | normal | h4 |
| 24px | 1.5rem | 500 | 36px | normal | div, svg, path, span |
| 22px | 1.375rem | 400 | 22px | normal | div, svg, path |
| 20px | 1.25rem | 400 | 30px | normal | body, div, nav, a |
| 18px | 1.125rem | 600 | 27px | normal | li, a, div, span |
| 16px | 1rem | 400 | 18.4px | normal | html, head, meta, title |

### Heading Scale

```css
h1 { font-size: 84px; font-weight: 600; line-height: 100.8px; }
h2 { font-size: 54px; font-weight: 600; line-height: 64.8px; }
h3 { font-size: 42px; font-weight: 600; line-height: 50.4px; }
h4 { font-size: 34px; font-weight: 600; line-height: 40.8px; }
h5 { font-size: 30px; font-weight: 600; line-height: 45px; }
h4 { font-size: 25.6px; font-weight: 600; line-height: 30.72px; }
h4 { font-size: 24px; font-weight: 500; line-height: 36px; }
```

### Body Text

```css
body { font-size: 20px; font-weight: 400; line-height: 30px; }
```

### Font Weights in Use

`400` (785x), `600` (92x), `500` (38x), `700` (21x)

## Spacing

**Base unit:** 5px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-0 | 0px | 0rem |
| spacing-20 | 20px | 1.25rem |
| spacing-25 | 25px | 1.5625rem |
| spacing-28 | 28px | 1.75rem |
| spacing-40 | 40px | 2.5rem |
| spacing-45 | 45px | 2.8125rem |
| spacing-50 | 50px | 3.125rem |
| spacing-60 | 60px | 3.75rem |
| spacing-70 | 70px | 4.375rem |
| spacing-73 | 73px | 4.5625rem |
| spacing-100 | 100px | 6.25rem |
| spacing-106 | 106px | 6.625rem |
| spacing-120 | 120px | 7.5rem |
| spacing-140 | 140px | 8.75rem |
| spacing-200 | 200px | 12.5rem |
| spacing-240 | 240px | 15rem |
| spacing-385 | 385px | 24.0625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 4 |
| md | 10px | 26 |
| lg | 15px | 4 |
| xl | 20px | 18 |
| full | 25px | 4 |
| full | 30px | 3 |
| full | 50px | 16 |
| full | 100px | 1 |

## Box Shadows

**lg** — blur: 29px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 29px -4px;
```

## CSS Custom Properties

### Colors

```css
--primary: #007bff;
--secondary: #6c757d;
--swiper-theme-color: #007aff;
```

### Spacing

```css
--font-family-monospace: SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;
--swiper-navigation-size: 44px;
```

### Typography

```css
--font-family-sans-serif: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;
```

### Other

```css
--blue: #007bff;
--indigo: #6610f2;
--purple: #6f42c1;
--pink: #e83e8c;
--red: #dc3545;
--orange: #fd7e14;
--yellow: #ffc107;
--green: #28a745;
--teal: #20c997;
--cyan: #17a2b8;
--white: #fff;
--gray: #6c757d;
--gray-dark: #343a40;
--success: #28a745;
--info: #17a2b8;
--warning: #ffc107;
--danger: #dc3545;
--light: #f8f9fa;
--dark: #343a40;
--breakpoint-xs: 0;
--breakpoint-sm: 576px;
--breakpoint-md: 768px;
--breakpoint-lg: 992px;
--breakpoint-xl: 1200px;
--c: rgb(35, 35, 35);
--b: rgb(35, 35, 35);
--a: rgb(35, 35, 35);
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
| 400px | 400px | max-width |
| sm | 500px | max-width |
| sm | 576px | max-width |
| md | 767px | max-width |
| md | 768px | min-width |
| 860px | 860px | max-width |
| lg | 991px | max-width |
| lg | 992px | min-width |
| lg | 999px | max-width |
| lg | 1000px | max-width |
| 1200px | 1200px | min-width |
| 1399px | 1399px | max-width |
| 1400px | 1400px | min-width |
| 2xl | 1600px | min-width |
| 1800px | 1800px | max-width |
| 1900px | 1900px | min-width |
| 1920px | 1920px | min-width |
| 2300px | 2300px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.6s`, `0.4s`, `0.1s`, `0.2s`, `1s`, `0.8s`, `0.001s`, `1.2s`, `0.3s`, `0.15s`

### Common Transitions

```css
transition: all;
transition: transform 0.6s, background-color 0.6s;
transition: 0.4s;
transition: 0.1s;
transition: 0.2s;
transition: 0.2s ease-in-out;
transition: max-height 1s cubic-bezier(0, 0.55, 0.45, 1) 0.4s;
transition: transform 0.8s cubic-bezier(0.445, 0.05, 0.55, 0.95);
transition: 0.2s 0.2s;
transition: 0.4s 0.001s;
```

### Keyframe Animations

**fa-spin**
```css
@keyframes fa-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**fa-spin**
```css
@keyframes fa-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**progress-bar-stripes**
```css
@keyframes progress-bar-stripes {
  0% { background-position: 1rem 0px; }
  100% { background-position: 0px 0px; }
}
```

**infiniteScroll**
```css
@keyframes infiniteScroll {
  100% { transform: translateX(-100%); }
}
```

**divider1**
```css
@keyframes divider1 {
  50% { transform: translateX(-50px) translateY(30px); }
  100% { transform: translateX(50px) translateY(0px); }
}
```

**pathAnim-0**
```css
@keyframes pathAnim-0 {
  25% { d: path("M 0 400 L 0 75 C 79.9787 70.4201 159.957 65.8403 233 61 C 306.043 56.1597 372.149 51.0591 445 51 C 517.851 50.9409 597.446 55.9234 652 63 C 706.554 70.0766 736.066 79.2473 788 81 C 839.934 82.7527 914.29 77.0873 1001 73 C 1087.71 68.9127 1186.77 66.4036 1262 67 C 1337.23 67.5964 1388.61 71.2982 1440 75 L 1440 400 L 0 400 Z"); }
  50% { d: path("M 0 400 L 0 75 C 69.5802 64.2855 139.16 53.5709 215 46 C 290.84 38.4291 372.939 34.0017 436 39 C 499.061 43.9983 543.086 58.4222 608 66 C 672.914 73.5778 758.719 74.3095 841 68 C 923.281 61.6905 1002.04 48.3397 1058 58 C 1113.96 67.6603 1147.13 100.332 1207 107 C 1266.87 113.668 1353.43 94.3343 1440 75 L 1440 400 L 0 400 Z"); }
  75% { d: path("M 0 400 L 0 75 C 88.9997 90.1481 177.999 105.296 240 102 C 302.001 98.7039 337.002 76.9636 393 76 C 448.998 75.0364 525.991 94.8495 608 99 C 690.009 103.15 777.033 91.6383 855 78 C 932.967 64.3617 1001.88 48.5974 1060 53 C 1118.12 57.4026 1165.46 81.9722 1227 89 C 1288.54 96.0278 1364.27 85.5139 1440 75 L 1440 400 L 0 400 Z"); }
  100% { d: path("M 0 400 L 0 75 C 65.0045 82.258 130.009 89.516 194 91 C 257.991 92.484 320.969 88.1941 388 91 C 455.031 93.8059 526.116 103.708 593 93 C 659.884 82.2923 722.567 50.9753 793 50 C 863.433 49.0247 941.617 78.3913 1023 81 C 1104.38 83.6087 1188.97 59.4596 1259 54 C 1329.03 48.5404 1384.52 61.7702 1440 75 L 1440 400 L 0 400 Z"); }
}
```

**pathAnim-1**
```css
@keyframes pathAnim-1 {
  25% { d: path("M 0 400 L 0 175 C 87.2587 188.292 174.517 201.583 241 196 C 307.483 190.417 353.189 165.958 403 166 C 452.811 166.042 506.726 190.583 588 186 C 669.274 181.417 777.909 147.71 847 143 C 916.091 138.29 945.64 162.578 1002 173 C 1058.36 183.422 1141.53 179.978 1219 178 C 1296.47 176.022 1368.23 175.511 1440 175 L 1440 400 L 0 400 Z"); }
  50% { d: path("M 0 400 L 0 175 C 63.3322 163.745 126.664 152.49 206 146 C 285.336 139.51 380.675 137.787 442 144 C 503.325 150.213 530.637 164.364 590 175 C 649.363 185.636 740.778 192.758 821 183 C 901.222 173.242 970.252 146.604 1037 152 C 1103.75 157.396 1168.21 194.828 1235 204 C 1301.79 213.172 1370.89 194.086 1440 175 L 1440 400 L 0 400 Z"); }
  75% { d: path("M 0 400 L 0 175 C 60.6396 192.695 121.279 210.39 196 204 C 270.721 197.61 359.522 167.135 432 169 C 504.478 170.865 560.631 205.069 629 208 C 697.369 210.931 777.955 182.59 837 164 C 896.045 145.41 933.551 136.572 1000 148 C 1066.45 159.428 1161.84 191.122 1240 199 C 1318.16 206.878 1379.08 190.939 1440 175 L 1440 400 L 0 400 Z"); }
  100% { d: path("M 0 400 L 0 175 C 61.7252 168.37 123.45 161.74 185 160 C 246.55 158.26 307.924 161.41 387 161 C 466.076 160.59 562.855 156.619 643 159 C 723.145 161.381 786.658 170.112 852 179 C 917.342 187.888 984.515 196.931 1053 198 C 1121.48 199.069 1191.28 192.162 1256 187 C 1320.72 181.838 1380.36 178.419 1440 175 L 1440 400 L 0 400 Z"); }
}
```

**pathAnim-2**
```css
@keyframes pathAnim-2 {
  25% { d: path("M 0 400 L 0 275 C 61.0725 291.054 122.145 307.109 184 299 C 245.855 290.891 308.493 258.62 377 254 C 445.507 249.38 519.885 272.411 595 284 C 670.115 295.589 745.969 295.735 827 292 C 908.031 288.265 994.239 280.648 1058 284 C 1121.76 287.352 1163.07 301.672 1223 302 C 1282.93 302.328 1361.46 288.664 1440 275 L 1440 400 L 0 400 Z"); }
  50% { d: path("M 0 400 L 0 275 C 73.6819 266.36 147.364 257.719 213 266 C 278.636 274.281 336.227 299.482 396 294 C 455.773 288.518 517.729 252.351 588 250 C 658.271 247.649 736.856 279.112 813 283 C 889.144 286.888 962.846 263.201 1024 256 C 1085.15 248.799 1133.76 258.086 1201 264 C 1268.24 269.914 1354.12 272.457 1440 275 L 1440 400 L 0 400 Z"); }
  75% { d: path("M 0 400 L 0 275 C 66.6445 255.452 133.289 235.904 200 238 C 266.711 240.096 333.489 263.835 400 272 C 466.511 280.165 532.756 272.754 611 264 C 689.244 255.246 779.488 245.148 846 255 C 912.512 264.852 955.292 294.652 1011 296 C 1066.71 297.348 1135.35 270.242 1209 262 C 1282.65 253.758 1361.33 264.379 1440 275 L 1440 400 L 0 400 Z"); }
  100% { d: path("M 0 400 L 0 275 C 82.5991 284.977 165.198 294.953 232 299 C 298.802 303.047 349.806 301.164 405 290 C 460.194 278.836 519.577 258.393 592 257 C 664.423 255.607 749.887 273.266 815 282 C 880.113 290.734 924.877 290.544 994 292 C 1063.12 293.456 1156.61 296.559 1235 294 C 1313.39 291.441 1376.7 283.221 1440 275 L 1440 400 L 0 400 Z"); }
}
```

**coworker_box_1**
```css
@keyframes coworker_box_1 {
  25% { top: 0px; left: calc(100% - 100px); }
  50% { top: calc(100% - 100px); left: calc(100% - 100px); }
  75% { top: calc(100% - 100px); left: 0px; }
  100% { top: 0px; left: 0px; }
}
```

**coworker_box_2**
```css
@keyframes coworker_box_2 {
  25% { bottom: 0px; right: calc(100% - 100px); }
  50% { bottom: calc(100% - 100px); right: calc(100% - 100px); }
  75% { bottom: calc(100% - 100px); right: 0px; }
  100% { bottom: 0px; right: 0px; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (12 instances)

```css
.button {
  background-color: rgb(98, 64, 88);
  color: rgb(255, 255, 255);
  font-size: 18px;
  font-weight: 500;
  padding-top: 15px;
  padding-right: 25px;
  border-radius: 50px;
}
```

### Cards (1 instances)

```css
.card {
  background-color: rgb(247, 247, 247);
  border-radius: 25px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 29px -4px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (37 instances)

```css
.input {
  background-color: rgb(255, 255, 255);
  color: rgb(73, 80, 87);
  border-color: rgb(35, 35, 35);
  border-radius: 10px;
  font-size: 16px;
  padding-top: 14px;
  padding-right: 15px;
}
```

### Links (84 instances)

```css
.link {
  color: rgb(35, 35, 35);
  font-size: 20px;
  font-weight: 400;
}
```

### Navigation (6 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(35, 35, 35);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (12 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(35, 35, 35);
  padding-top: 15px;
  padding-bottom: 15px;
  font-size: 20px;
}
```

### Modals (9 instances)

```css
.modal {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (29 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(35, 35, 35);
  padding-top: 0px;
}
```

### Tables (1 instances)

```css
.table {
  border-color: rgb(35, 35, 35);
  cell-style: [object Object];
}
```

### Badges (2 instances)

```css
.badge {
  color: rgb(35, 35, 35);
  font-size: 20px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Switches (4 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(35, 35, 35);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(51, 51, 51);
  padding: 6px 15px 6px 15px;
  border-radius: 30px;
  border: 1px solid rgb(51, 51, 51);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**0 grid containers** and **120 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 800px | 30px |
| 1600px | 15px |
| 50% | 15px |
| 550px | 0px |
| 612px | 50px |

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/wrap | 52x |
| row/nowrap | 67x |
| column/nowrap | 1x |

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 86/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 70/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 21 distinct font sizes — consider a tighter type scale
- 872 !important rules — prefer specificity over overrides
- 95% of CSS is unused — consider purging
- 11617 duplicate CSS declarations

## Z-Index Map

**8 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1500,2147483647 | div, iframe |
| dropdown | 100,100 | div.p.o.p.u.p, div.p.o.p.u.p, div.p.o.p.u.p |
| sticky | 10,10 | div |
| base | -1000,9 | span.s.w.i.p.e.r.-.n.o.t.i.f.i.c.a.t.i.o.n, div.s.h.o.w.c.a.s.e.-.c.o.n.t.a.i.n.e.r. .s.w.i.p.e.r. .s.w.i.p.e.r.-.i.n.i.t.i.a.l.i.z.e.d. .s.w.i.p.e.r.-.h.o.r.i.z.o.n.t.a.l. .s.w.i.p.e.r.-.b.a.c.k.f.a.c.e.-.h.i.d.d.e.n, div.i.n.n.e.r. .s.w.i.p.e.r.-.w.r.a.p.p.e.r |

**Issues:**
- [object Object]

## SVG Icons

**7 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 1 |
| md | 6 |

**Icon colors:** `rgb(35, 35, 35)`, `rgb(0, 0, 0)`, `currentColor`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| flexslider-icon | self-hosted | normal | normal |
| Inter | google-fonts | 100, 200, 300, 400, 500, 600, 700, 800, 900 | normal |
| Outfit | google-fonts | 100, 200, 300, 400, 500, 600, 700, 800, 900 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/css?family=Inter:100,200,300,400,500,600,700,800,900`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 16 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 11 | objectFit: cover, borderRadius: 20px, shape: pill |

**Aspect ratios:** 3:2 (10x), 1:1 (9x), 3.99:1 (2x), 4.47:1 (1x), 3.79:1 (1x), 21:9 (1x), 16:9 (1x), 1.98:1 (1x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `600ms` | 600 |
| `xl` | `800ms` | 800 |

### Easing Families

- **ease-in-out** (34 uses) — `ease`
- **ease-out** (1 uses) — `cubic-bezier(0, 0.55, 0.45, 1)`
- **custom** (1 uses) — `cubic-bezier(0.445, 0.05, 0.55, 0.95)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `infiniteScroll` | slide-x | transform | 2 |

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** unknown (tight)

### Top CTA Verbs

- **till** (1)

### Button Copy Patterns

- "tillåt alla" (1×)

## Page Intent

**Type:** `unknown` (confidence 0)
**Description:** Söker du en webbyrå i Göteborg? Vi erbjuder modern och behovsanpassad webbutveckling som leder till ökad tillväxt. Kontakta oss för kostnadsfri rådgivning!

## Section Roles

Reading order (top→bottom): nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.145 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 100px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.167)
**Counts:** total 27, svg 11, icon 8, screenshot-like 0, photo-like 9
**Dominant aspect:** landscape
**Radius profile on images:** soft

## Component Library

**Detected:** `bootstrap` (confidence 0.6)

Evidence:
- bootstrap utility hits: 3

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
