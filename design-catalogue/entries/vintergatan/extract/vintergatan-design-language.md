# Design Language: Vintergatan · Antikvariat och bokbinderi i Uppsala

> Extracted from `http://127.0.0.1:3055/sites/vintergatan.html` on September 8, 2026
> 271 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#3b0604` | rgb(59, 6, 4) | hsl(2, 87%, 12%) | 2 |
| Secondary | `#751510` | rgb(117, 21, 16) | hsl(3, 76%, 26%) | 1 |
| Accent | `#e7dec4` | rgb(231, 222, 196) | hsl(45, 42%, 84%) | 2 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 271 |
| `#040201` | hsl(20, 60%, 1%) | 104 |
| `#1c1611` | hsl(27, 24%, 9%) | 61 |

### Background Colors

Used on large-area elements: `#e7dec4`, `#040202`, `#040201`

### Text Colors

Text color palette: `#040201`, `#1c1611`, `#dfd4b7`, `#93611c`, `#3b0604`

### Gradients

```css
background-image: linear-gradient(oklch(0.21 0.02 55 / 0.38), oklch(0.21 0.02 55 / 0.32) 38%, oklch(0.21 0.02 55 / 0.7) 72%, oklch(0.21 0.02 55 / 0.88)), url("https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=2400&q=80");
```

```css
background-image: linear-gradient(to right, oklch(0.215 0.02 45 / 0.55), oklch(0.215 0.02 45 / 0) 45%), url("https://images.unsplash.com/photo-1589998059171-988d887df646?auto=format&fit=crop&w=1600&q=80");
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 271 |
| `#dfd4b7` | text, background | 108 |
| `#040201` | text, background | 104 |
| `#1c1611` | text | 61 |
| `#93611c` | text | 6 |
| `#e7dec4` | background | 2 |
| `#3b0604` | text | 2 |
| `#751510` | background | 1 |

## Typography

### Font Families

- **EB Garamond** — used for body (119 elements)
- **IBM Plex Mono** — used for body (76 elements)
- **Cormorant Garamond** — used for all (63 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 153.6px | 9.6rem | 400 | 147.456px | -2.304px | h2, span |
| 121.6px | 7.6rem | 400 | 114.304px | -1.824px | h1, br, span |
| 89.6px | 5.6rem | 400 | 85.12px | -1.344px | h2, br, span |
| 70.4px | 4.4rem | 400 | 68.992px | -1.056px | h2, span |
| 53.76px | 3.36rem | 400 | 58.0608px | -0.8064px | p |
| 51.2px | 3.2rem | 400 | 53.76px | -0.768px | h2, span |
| 43.52px | 2.72rem | 400 | 48.7424px | -0.6528px | p |
| 36px | 2.25rem | 500 | 40px | -0.9px | a |
| 30px | 1.875rem | 400 | 36px | -0.45px | h3, div |
| 24px | 1.5rem | 400 | 32px | normal | div, span |
| 20px | 1.25rem | 400 | 28px | -0.3px | span |
| 17.5px | 1.0938rem | 400 | 26.25px | normal | body, div, header, section |
| 17px | 1.0625rem | 400 | 26.35px | normal | p |
| 16.5px | 1.0313rem | 400 | 27.225px | normal | div |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |

### Heading Scale

```css
h2 { font-size: 153.6px; font-weight: 400; line-height: 147.456px; }
h1 { font-size: 121.6px; font-weight: 400; line-height: 114.304px; }
h2 { font-size: 89.6px; font-weight: 400; line-height: 85.12px; }
h2 { font-size: 70.4px; font-weight: 400; line-height: 68.992px; }
h2 { font-size: 51.2px; font-weight: 400; line-height: 53.76px; }
h3 { font-size: 30px; font-weight: 400; line-height: 36px; }
```

### Body Text

```css
body { font-size: 10.5px; font-weight: 400; line-height: 15.75px; }
```

### Font Weights in Use

`400` (270x), `500` (1x)

## Spacing

**Base unit:** 4px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-4 | 4px | 0.25rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-128 | 128px | 8rem |

## CSS Custom Properties

### Colors

```css
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-ring-offset-width: 0px;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgb(59 130 246 / 0.5);
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
--c-papper: oklch(0.955 0.018 92);
--c-black: oklch(0.21 0.02 55);
--c-oxblod: oklch(0.42 0.125 28);
--c-guld: oklch(0.74 0.10 85);
--c-benvit: oklch(0.94 0.02 90);
--c-mork: oklch(0.215 0.02 45);
--f-display: "Cormorant Garamond", ui-serif, Georgia, serif;
--f-body: "EB Garamond", ui-serif, Georgia, serif;
--f-mono: "IBM Plex Mono", ui-monospace, monospace;
--tw-contrast: ;
--tw-backdrop-sepia: ;
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
--tw-contain-layout: ;
--tw-contain-paint: ;
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
| sm | 640px | min-width |
| md | 768px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `1.25s`, `1.4s`

### Common Transitions

```css
transition: all;
transition: opacity 1.25s cubic-bezier(0.16, 1, 0.3, 1), transform 1.25s cubic-bezier(0.16, 1, 0.3, 1);
transition: transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Links (6 instances)

```css
.link {
  color: oklch(0.45 0.022 70);
  font-size: 10.5px;
  font-weight: 400;
}
```

### Navigation (1 instances)

```css
.navigatio {
  color: oklch(0.45 0.022 70);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

## Layout System

**23 grid containers** and **14 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1480px | 32px |
| 659.313px | 0px |
| 571.853px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 23x |

### Grid Templates

```css
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 48px 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: normal 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 40px 32px;
grid-template-columns: 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px 72px;
gap: 48px 32px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 14x |

**Gap values:** `12px`, `16px 32px`, `24px`, `40px 32px`, `48px 32px`, `8px normal`, `normal 24px`, `normal 32px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 91/100 (Grade: A)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 80/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 88% of CSS is unused — consider purging
- 301 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 4 | bold |
| linear | to right | 2 | brand |

```css
background: linear-gradient(oklch(0.21 0.02 55 / 0.38), oklch(0.21 0.02 55 / 0.32) 38%, oklch(0.21 0.02 55 / 0.7) 72%, oklch(0.21 0.02 55 / 0.88));
background: linear-gradient(to right, oklch(0.215 0.02 45 / 0.55), oklch(0.215 0.02 45 / 0) 45%);
```

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Cormorant Garamond | google-fonts | 400, 500, 600 | italic, normal |
| EB Garamond | google-fonts | 400, 500 | italic, normal |
| IBM Plex Mono | google-fonts | 400, 500 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| gallery | 5 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 1 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 4:3 (3x), 16:9 (1x), 3:4 (1x), 21:9 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xxl` | `1.25s` | 1250 |

### Easing Families

- **ease-out** (46 uses) — `cubic-bezier(0.16, 1, 0.3, 1)`

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Sample Headings

> Ett antikvariat
med verkstaden kvar.
> Fem band ur veckans förvärv.
> Linné, Flora Svecica
> Bellman, Fredmans epistlar
> Busser, Utkast till beskrifning om Upsala
> Boye, Kallocain
> Sytt.
Lagat.
Förgyllt.
> Ett band ska tåla hundra år till.
> Brevet
> Genomgången

## Page Intent

**Type:** `unknown` (confidence 0)
**Description:** Antikvariat med eget bokbinderi på Svartbäcksgatan i Uppsala. Äldre tryck framme i butiken, handbundna och lagade band i verkstaden bakom.

## Section Roles

Reading order (top→bottom): nav → nav → content → content → content → content → content → content → content → content → content → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | content | Ett antikvariat
med verkstaden kvar. | 0.3 |
| 3 | content | — | 0.3 |
| 4 | content | — | 0.3 |
| 5 | content | Fem band ur veckans förvärv. | 0.3 |
| 6 | content | — | 0.3 |
| 7 | content | Sytt.
Lagat.
Förgyllt. | 0.3 |
| 8 | content | Ett band ska tåla hundra år till. | 0.3 |
| 9 | content | Lär dig binda själv. | 0.3 |
| 10 | content | — | 0.3 |
| 11 | content | Kom in,
eller skriv. | 0.3 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.513 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 0px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `mixed` (confidence 0)
**Counts:** total 6, svg 0, icon 0, screenshot-like 0, photo-like 0
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.643)

Evidence:
- tailwind-like class density 64%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `EB Garamond` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
