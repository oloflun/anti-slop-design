# Design Language: AI Networking for Women & Female Founders | Kinhive

> Extracted from `https://kinhive.com` on September 4, 2026
> 636 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f8f9b8` | rgb(248, 249, 184) | hsl(61, 84%, 85%) | 43 |
| Secondary | `#f7f7f5` | rgb(247, 247, 245) | hsl(60, 11%, 96%) | 4 |
| Accent | `#fd8143` | rgb(253, 129, 67) | hsl(20, 98%, 63%) | 44 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 716 |
| `#22201f` | hsl(20, 5%, 13%) | 253 |
| `#777777` | hsl(0, 0%, 47%) | 124 |
| `#ffffff` | hsl(0, 0%, 100%) | 104 |
| `#646464` | hsl(0, 0%, 39%) | 8 |
| `#d8d7d3` | hsl(48, 6%, 84%) | 4 |
| `#0f0e0e` | hsl(0, 3%, 6%) | 3 |
| `#eeedeb` | hsl(40, 8%, 93%) | 2 |
| `#e0e0e0` | hsl(0, 0%, 88%) | 2 |
| `#555555` | hsl(0, 0%, 33%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#f8f9b8`, `#22201f`, `#8fb8c8`, `#fd8143`, `#d8d7d3`, `#f7f7f5`, `#eeedeb`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#22201f`, `#fd8143`, `#777777`, `#646464`, `#f8f9b8`, `#1a1a1a`, `#0f0e0e`, `#555555`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 716 |
| `#22201f` | text, border, background | 253 |
| `#777777` | text, border | 124 |
| `#ffffff` | background, text, border | 104 |
| `#fd8143` | background, text, border | 44 |
| `#f8f9b8` | background, text, border | 43 |
| `#646464` | text, border | 8 |
| `#d8d7d3` | border, background | 4 |
| `#f7f7f5` | background | 4 |
| `#0f0e0e` | text, border, background | 3 |
| `#eeedeb` | background | 2 |
| `#e0e0e0` | border | 2 |
| `#8fb8c8` | background | 1 |
| `#555555` | text | 1 |

## Typography

### Font Families

- **Helvetica** — used for body (233 elements)
- **FigtreeKH** — used for all (231 elements)
- **Times New Roman** — used for body (104 elements)
- **Arial** — used for body (48 elements)
- **Affairs** — used for all (20 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 96px | 6rem | 400 | 96px | -1.5px | div, em |
| 72px | 4.5rem | 400 | 79.2px | -2px | h2 |
| 48px | 3rem | 400 | 52.8px | -1.5px | div, em |
| 44px | 2.75rem | 400 | 44px | -0.5px | div |
| 40px | 2.5rem | 400 | 48px | -0.75px | div, h3, h2, em |
| 32px | 2rem | 400 | 38.4px | -0.65px | h2 |
| 24px | 1.5rem | 400 | 0px | -0.65px | sup |
| 20px | 1.25rem | 400 | 30px | normal | div |
| 18px | 1.125rem | 400 | 27px | normal | div, h3, a, span |
| 16px | 1rem | 400 | normal | normal | html, head, meta, title |
| 15px | 0.9375rem | 400 | 22.5px | normal | div, button |
| 14px | 0.875rem | 500 | 16.8px | normal | button, span, a, div |
| 13.3333px | 0.8333rem | 400 | normal | normal | button, svg, use |
| 13px | 0.8125rem | 400 | 19.5px | normal | div, u, a, p |
| 12px | 0.75rem | 600 | 12px | normal | div, span |

### Heading Scale

```css
h2 { font-size: 72px; font-weight: 400; line-height: 79.2px; }
h3 { font-size: 40px; font-weight: 400; line-height: 48px; }
h2 { font-size: 32px; font-weight: 400; line-height: 38.4px; }
h3 { font-size: 18px; font-weight: 400; line-height: 27px; }
h1 { font-size: 16px; font-weight: 400; line-height: normal; }
h2 { font-size: 14px; font-weight: 500; line-height: 16.8px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 600; line-height: 12px; }
```

### Font Weights in Use

`400` (524x), `600` (59x), `500` (53x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-24 | 24px | 1.5rem |
| spacing-30 | 30px | 1.875rem |
| spacing-39 | 39px | 2.4375rem |
| spacing-48 | 48px | 3rem |
| spacing-63 | 63px | 3.9375rem |
| spacing-69 | 69px | 4.3125rem |
| spacing-80 | 80px | 5rem |
| spacing-120 | 120px | 7.5rem |
| spacing-144 | 144px | 9rem |
| spacing-187 | 187px | 11.6875rem |
| spacing-245 | 245px | 15.3125rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 16 |
| md | 8px | 12 |
| lg | 12px | 2 |
| full | 50px | 1 |
| full | 100px | 2 |
| full | 900px | 14 |

## Box Shadows

**xl** — blur: 32px
```css
box-shadow: rgba(0, 0, 0, 0.15) 0px 8px 32px 0px;
```

## CSS Custom Properties

### Colors

```css
--color_primary_default: rgba(2, 5, 211, 1);
--color_primary_default_rgb: 2, 5, 211;
--color_primary_contrast_default: rgba(255, 255, 255, 1);
--color_primary_contrast_default_rgb: 255, 255, 255;
--color_text_default: rgba(9, 23, 71, 1);
--color_text_default_rgb: 9, 23, 71;
--color_surface_default: rgba(255, 255, 255, 1);
--color_surface_default_rgb: 255, 255, 255;
--color_background_default: rgba(255, 255, 255, 0);
--color_background_default_rgb: 255, 255, 255;
--color_destructive_default: rgba(255, 0, 0, 1);
--color_destructive_default_rgb: 255, 0, 0;
--color_success_default: rgba(23, 219, 78, 1);
--color_success_default_rgb: 23, 219, 78;
--color_alert_default: rgba(250, 181, 21, 1);
--color_alert_default_rgb: 250, 181, 21;
--color_danger_default_rgb: rgba(176, 32, 12, 1);
--color_bTHBi_default: #0205D3;
--color_bTOCT_default: rgba(213,239,2,1);
--color_bTHCB_default_rgb: 0205;
--color_cmXqS_default_rgb: 0205;
--color_bTNHh_default: rgba(143,184,200,1);
--color_bTMJp_default_rgb: 52,114,196;
--color_bTJVR_default_rgb: 238,238,235;
--color_cmXqS_default: #0205D3;
--color_bTHKh_default_rgb: 1,49,34;
--color_bTHBn_default: #0205D3;
--color_bTGyQ_default_rgb: 238,237,235;
--color_bTGyQ_default: rgba(238,237,235,1);
--color_bTHBJ_default: #0205D3;
--color_bTGLo_default_rgb: 0205;
--color_bTLDY_default_rgb: 100,100,100;
--color_bTMJp_default: rgba(52,114,196,1);
--color_bTILm_default_rgb: 18,22,21;
--color_cmXpD_default_rgb: 0205;
--color_bTHBF_default_rgb: 0205;
--color_bTHKh_default: rgba(1,49,34,1);
--color_bTHRY_default: rgba(106,152,201,1);
--color_bTJnN_default_rgb: 250,249,245;
--color_bTHAZ_default: #0205D3;
--color_bTGLo_default: #0205D3;
--color_bTHPB_default: #0205D3;
--color_bTNJy_default: rgba(248,249,184,1);
--color_bTGyP_default_rgb: 216,215,211;
--color_bTHRL_default: rgba(4,40,90,1);
--color_bTHAT_default: #0205D3;
--color_bTHAZ_default_rgb: 0205;
--color_bTNHW_default_rgb: 34,32,31;
--color_bTHHP_default: #0205D3;
--color_bTHBF_default: #0205D3;
--color_bTJVR_default: rgba(238,238,235,1);
--color_bTHgY_default: #0205D3;
--color_bTILm_default: rgba(18,22,21,1);
--color_bTGyP_default: rgba(216,215,211,1);
--color_bTHBo_default: rgba(119,119,119,1);
--color_bTHQP_default: rgba(149,6,6,1);
--color_bTHgY_default_rgb: 0205;
--color_bTOCT_default_rgb: 213,239,2;
--color_bTHBL0_default_rgb: 0205;
--color_bTHBL0_default: #0205D3;
--color_bTHBJ_default_rgb: 0205;
--color_bTLDY_default: rgba(100,100,100,1);
--color_bTHBo_default_rgb: 119,119,119;
--color_bTHAT_default_rgb: 0205;
--color_bTHBP0_default_rgb: 126,126,126;
--color_bTHCB_default: #0205D3;
--color_bTHPl_default: rgba(227,227,223,1);
--color_bTJnN_default: rgba(250,249,245,1);
--color_bTHRL_default_rgb: 4,40,90;
--color_bTNHh_default_rgb: 143,184,200;
--color_bTNJy_default_rgb: 248,249,184;
--color_bTHQP_default_rgb: 149,6,6;
--color_cmXpD_default: #0205D3;
--color_bTKJr_default: #0205D3;
--color_bTHPB_default_rgb: 0205;
--color_bTHBP0_default: rgba(126,126,126,1);
--color_bTHft_default_rgb: 0205;
--color_bTHPl_default_rgb: 227,227,223;
--color_bTHBi_default_rgb: 0205;
--color_bTHHP_default_rgb: 0205;
--color_bTNHV_default_rgb: 253,129,67;
--color_bTNHW_default: rgba(34,32,31,1);
--color_bTHRY_default_rgb: 106,152,201;
--color_bTHBn_default_rgb: 0205;
--color_bTNHV_default: rgba(253,129,67,1);
--color_bTHft_default: #0205D3;
--color_bTKJr_default_rgb: 0205;
```

### Typography

```css
--font_default: 'Lato';
--font_bTHEn_default: "Gantari";
--font_cmXpc_default: "Open Sans";
--font_bTHFe_default: "MADE Outer Sans";
--font_bTHBo_default: "Open Sans";
--font_bTHAz_default: "Affairs";
--font_bTIjU_default: "Open Sans";
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
| sm | 480px | max-width |
| sm | 680px | max-width |
| md | 720px | max-width |
| md | 767px | max-width |
| md | 768px | max-width |

## Transitions & Animations

**Durations:** `0.3s`, `0.2s`, `0.25s`

### Common Transitions

```css
transition: all;
transition: background 0.3s, padding-top 0.2s, padding-bottom 0.2s;
transition: background 0.2s;
transition: color 0.2s;
transition: color 0.2s, border-color 0.2s, background 0.2s;
transition: transform 0.25s;
```

### Keyframe Animations

**highlight-in**
```css
@keyframes highlight-in {
  0% { background-color: rgb(200, 0, 0); }
}
```

**fa-spin**
```css
@keyframes fa-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(359deg); }
}
```

**fa-spin**
```css
@keyframes fa-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(359deg); }
}
```

**custom-marquee-anim**
```css
@keyframes custom-marquee-anim {
  0% { transform: translate3d(0px, 0px, 0px); }
  100% { transform: translate3d(-50%, 0px, 0px); }
}
```

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**flipCycleLoop**
```css
@keyframes flipCycleLoop {
  0%, 47% { opacity: 0; visibility: hidden; transform: rotateY(-90deg); }
  53% { opacity: 1; visibility: visible; transform: rotateY(0deg); }
  53.1%, 95.1% { opacity: 1; visibility: visible; transform: rotateY(0deg); }
  100% { opacity: 0; visibility: hidden; transform: rotateY(90deg); }
}
```

**opacity-70-25-0-13**
```css
@keyframes opacity-70-25-0-13 {
  0% { opacity: 0.25; }
  0.01% { opacity: 0.25; }
  0.02% { opacity: 1; }
  70.01% { opacity: 0.25; }
  100% { opacity: 0.25; }
}
```

**opacity-70-25-1-13**
```css
@keyframes opacity-70-25-1-13 {
  0% { opacity: 0.25; }
  7.70231% { opacity: 0.25; }
  7.71231% { opacity: 1; }
  77.7023% { opacity: 0.25; }
  100% { opacity: 0.25; }
}
```

**opacity-70-25-2-13**
```css
@keyframes opacity-70-25-2-13 {
  0% { opacity: 0.25; }
  15.3946% { opacity: 0.25; }
  15.4046% { opacity: 1; }
  85.3946% { opacity: 0.25; }
  100% { opacity: 0.25; }
}
```

**opacity-70-25-3-13**
```css
@keyframes opacity-70-25-3-13 {
  0% { opacity: 0.25; }
  23.0869% { opacity: 0.25; }
  23.0969% { opacity: 1; }
  93.0869% { opacity: 0.25; }
  100% { opacity: 0.25; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (29 instances)

```css
.button {
  background-color: rgb(34, 32, 31);
  color: rgb(119, 119, 119);
  font-size: 13.3333px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 4px;
}
```

### Cards (1 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 12px;
  box-shadow: rgba(0, 0, 0, 0.15) 0px 8px 32px 0px;
  padding-top: 14px;
  padding-right: 18px;
}
```

### Inputs (3 instances)

```css
.input {
  color: rgb(34, 32, 31);
  border-color: rgb(34, 32, 31);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 12px;
}
```

### Links (27 instances)

```css
.link {
  color: rgb(34, 32, 31);
  font-size: 14px;
  font-weight: 400;
}
```

### Navigation (13 instances)

```css
.navigatio {
  background-color: rgb(34, 32, 31);
  color: rgb(253, 129, 67);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: relative;
}
```

### Modals (1 instances)

```css
.modal {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Badges (1 instances)

```css
.badge {
  color: rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 500;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Accordions (18 instances)

```css
.accordion {
  color: rgb(0, 0, 0);
  font-size: 16px;
  padding-top: 20px;
  padding-right: 20px;
  border-color: rgb(0, 0, 0);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 500;
```

### Input — 3 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(34, 32, 31);
  padding: 0px 12px 0px 16px;
  border-radius: 0px;
  border: 0px none rgb(34, 32, 31);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px 0px 1px none none solid rgb(255, 255, 255) rgb(255, 255, 255) rgb(248, 249, 184);
  font-size: 16px;
  font-weight: 400;
```

### Button — 5 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgb(34, 32, 31);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 900px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 600;
```

**Variant 2** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 15px;
  font-weight: 400;
```

### Button — 7 instances, 5 variants

**Variant 1** (2 instances)

```css
  background: rgb(247, 247, 245);
  color: rgb(34, 32, 31);
  padding: 12px 16px 12px 16px;
  border-radius: 900px;
  border: 0px none rgb(34, 32, 31);
  font-size: 16px;
  font-weight: 500;
```

**Variant 2** (2 instances)

```css
  background: rgb(34, 32, 31);
  color: rgb(255, 255, 255);
  padding: 12px 16px 12px 16px;
  border-radius: 900px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 500;
```

**Variant 3** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(85, 85, 85);
  padding: 10px 14px 10px 14px;
  border-radius: 8px;
  border: 1px solid rgb(224, 224, 224);
  font-size: 13px;
  font-weight: 500;
```

**Variant 4** (1 instance)

```css
  background: rgb(240, 240, 240);
  color: rgb(26, 26, 26);
  padding: 10px 14px 10px 14px;
  border-radius: 8px;
  border: 0px none rgb(26, 26, 26);
  font-size: 13px;
  font-weight: 500;
```

**Variant 5** (1 instance)

```css
  background: rgb(15, 14, 14);
  color: rgb(255, 255, 255);
  padding: 10px 14px 10px 14px;
  border-radius: 8px;
  border: 0px none rgb(255, 255, 255);
  font-size: 13px;
  font-weight: 500;
```

### Button — 16 instances, 1 variant

**Variant 1** (16 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(119, 119, 119);
  padding: 0px 0px 0px 0px;
  border-radius: 4px;
  border: 0px none rgb(119, 119, 119);
  font-size: 13.3333px;
  font-weight: 400;
```

## Layout System

**14 grid containers** and **221 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1400px | 0px |
| 540px | 32px |
| 100% | 0px |
| 800px | 0px |
| 1000px | 0px |
| 480px | 0px |
| 1200px | 0px |
| 700px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 13x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 1088px;
gap: 12px;
grid-template-columns: 1280px;
grid-template-columns: 368px 368px 368px;
gap: 40px;
grid-template-columns: 640px;
grid-template-columns: 800px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 122x |
| row/wrap | 40x |
| row/nowrap | 59x |

**Gap values:** `0px normal`, `12px`, `12px 48px`, `12px normal`, `16px`, `16px normal`, `20px normal`, `24px`, `24px normal`, `30px`, `40px`, `40px normal`, `48px`, `48px 60px`, `48px normal`, `4px`, `4px normal`, `60px normal`, `6px`, `6px normal`, `72px normal`, `80px normal`, `8px`, `8px normal`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 6 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#22201f` | 16.22:1 | AAA |
| `#22201f` | `#f7f7f5` | 15.12:1 | AAA |
| `#22201f` | `#f8f9b8` | 14.86:1 | AAA |
| `#1a1a1a` | `#f0f0f0` | 15.27:1 | AAA |
| `#ffffff` | `#0f0e0e` | 19.28:1 | AAA |

## Design System Score

**Overall: 79/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 70/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 5 font families — consider limiting to 2 (heading + body)
- 272 !important rules — prefer specificity over overrides
- 68% of CSS is unused — consider purging
- 13891 duplicate CSS declarations

## Z-Index Map

**22 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2002,2147483646 | div.g.r.e.y.o.u.t. .b.a.T.a.L.a.K.a.N, div.b.u.b.b.l.e.-.e.l.e.m.e.n.t. .P.o.p.u.p. .b.a.T.a.L.a.K.a.N. .b.u.b.b.l.e.-.r.-.c.o.n.t.a.i.n.e.r. .f.l.e.x. .c.o.l.u.m.n, div.g.r.e.y.o.u.t. .b.a.T.a.Q.z.f |
| sticky | 10,18 | div.b.u.b.b.l.e.-.e.l.e.m.e.n.t. .G.r.o.u.p. .b.a.T.i.p.e. .b.u.b.b.l.e.-.r.-.c.o.n.t.a.i.n.e.r. .f.l.e.x. .r.o.w, div.b.u.b.b.l.e.-.e.l.e.m.e.n.t. .C.u.s.t.o.m.E.l.e.m.e.n.t. .b.a.T.i.p.p. .b.u.b.b.l.e.-.r.-.c.o.n.t.a.i.n.e.r. .f.l.e.x. .c.o.l.u.m.n, div.b.u.b.b.l.e.-.e.l.e.m.e.n.t. .G.r.o.u.p. .b.a.T.a.S.a.G.a.F.1. .b.u.b.b.l.e.-.r.-.c.o.n.t.a.i.n.e.r. .f.l.e.x. .c.o.l.u.m.n |
| base | 0,9 | div.b.u.b.b.l.e.-.r.-.c.o.n.t.a.i.n.e.r. .f.l.e.x. .c.o.l.u.m.n, div.b.u.b.b.l.e.-.r.-.c.o.n.t.a.i.n.e.r. .f.l.e.x. .c.o.l.u.m.n, div.b.u.b.b.l.e.-.r.-.c.o.n.t.a.i.n.e.r. .f.l.e.x. .c.o.l.u.m.n |

**Issues:**
- [object Object]

## SVG Icons

**6 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| sm | 1 |
| md | 5 |

**Icon colors:** `rgb(255, 255, 255)`, `rgb(119, 119, 119)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| FontAwesome | self-hosted | normal | normal |
| Figtree | google-fonts | 400, 500 | normal |
| Merriweather | cdn | 400 | normal |
| Tiny5 | cdn | 400 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/css?family=Figtree:regular%7CFigtree:500%7CMerriweather:regular%7CTiny5:regular`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 5 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 4 | objectFit: cover, borderRadius: 8px, shape: rounded |

**Aspect ratios:** 1:1 (3x), 3:2 (3x), 6.54:1 (1x), 3.05:1 (1x), 6.34:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `custom-marquee-anim` | slide | transform | 1 |
| `spin` | rotate | transform | 1 |
| `spin` | rotate | transform | 1 |

## Component Anatomy

### button — 29 instances

**Slots:** label, icon
**Variants:** tertiary · secondary · primary

| variant | count | sample label |
|---|---|---|
| default | 26 | Features |
| tertiary | 1 | Preferences |
| secondary | 1 | Reject Optional |
| primary | 1 | Accept All |

### input — 3 instances


## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** unknown (tight)

### Top CTA Verbs

- **start** (3)
- **features** (1)
- **join** (1)
- **preferences** (1)
- **reject** (1)
- **accept** (1)

### Button Copy Patterns

- "features" (1×)
- "start with basic" (1×)
- "start with pro" (1×)
- "start with premium" (1×)
- "join the newsletter" (1×)
- "preferences" (1×)
- "reject optional" (1×)
- "accept all" (1×)

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Kinhive is an AI-powered networking platform for women. Meet the co-founders, collaborators, and peers you should know—with a reason for every match.

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.106 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 900px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.259)
**Counts:** total 9, svg 6, icon 0, screenshot-like 0, photo-like 3
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Component Library

**Detected:** `bootstrap` (confidence 0.6)

Evidence:
- bootstrap utility hits: 3

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Helvetica` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
