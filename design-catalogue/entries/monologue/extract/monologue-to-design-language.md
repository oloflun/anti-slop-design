# Design Language: Monologue — Dictation, voice notes, and bot-free meeting notes

> Extracted from `https://www.monologue.to/` on September 4, 2026
> 1596 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ef8a80` | rgb(239, 138, 128) | hsl(5, 78%, 72%) | 6 |
| Secondary | `#dcca65` | rgb(220, 202, 101) | hsl(51, 63%, 63%) | 6 |
| Accent | `#326ec8` | rgb(50, 110, 200) | hsl(216, 60%, 49%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#f2f0ed` | hsl(36, 16%, 94%) | 1491 |
| `#ffffff` | hsl(0, 0%, 100%) | 1154 |
| `#111111` | hsl(0, 0%, 7%) | 161 |
| `#272727` | hsl(0, 0%, 15%) | 133 |
| `#000000` | hsl(0, 0%, 0%) | 125 |
| `#343434` | hsl(0, 0%, 20%) | 19 |
| `#1b1b1b` | hsl(0, 0%, 11%) | 10 |
| `#909090` | hsl(0, 0%, 56%) | 8 |
| `#777777` | hsl(0, 0%, 47%) | 6 |
| `#b2b2b2` | hsl(0, 0%, 70%) | 4 |
| `#6c6c6c` | hsl(0, 0%, 42%) | 4 |
| `#555555` | hsl(0, 0%, 33%) | 3 |

### Background Colors

Used on large-area elements: `#121212`, `#272727`, `#2c2c2c`, `#ffffff`, `#232323`, `#252525`, `#f7f7f7`, `#101415`, `#0d1719`, `#343434`, `#1c1c1c`, `#393939`, `#101010`

### Text Colors

Text color palette: `#ffffff`, `#f2f0ed`, `#161616`, `#282828`, `#ef8a80`, `#6ed8ba`, `#dcca65`, `#cfcfcf`, `#102b1b`, `#000000`

### Gradients

```css
background-image: linear-gradient(rgba(255, 255, 255, 0.9), rgba(235, 235, 235, 0.9));
```

```css
background-image: linear-gradient(rgb(60, 60, 60) 0%, rgb(41, 41, 41) 100%);
```

```css
background-image: linear-gradient(rgb(182, 176, 164) 0%, rgb(254, 253, 251) 50%, rgb(182, 176, 164) 100%);
```

```css
background-image: linear-gradient(-21.4897deg, rgb(40, 40, 40) 1.6162%, rgb(64, 64, 64) 100.38%);
```

```css
background-image: linear-gradient(rgb(255, 114, 98), rgb(107, 39, 31));
```

```css
background-image: linear-gradient(90deg, rgb(14, 117, 130) 0%, rgb(25, 208, 232) 48.26%, rgb(81, 235, 255) 88.95%, rgb(197, 248, 255) 98.413%);
```

```css
background-image: linear-gradient(rgb(31, 214, 165), rgb(24, 129, 101));
```

```css
background-image: linear-gradient(rgb(220, 187, 21), rgb(122, 102, 2));
```

```css
background-image: linear-gradient(rgb(83, 142, 238), rgb(40, 93, 178));
```

```css
background-image: linear-gradient(rgb(255, 255, 255) 0%, rgb(239, 239, 239) 100%);
```

```css
background-image: linear-gradient(rgb(54, 53, 53), rgb(39, 39, 39) 17%, rgb(32, 32, 32) 100%);
```

```css
background-image: linear-gradient(rgb(255, 255, 255), rgb(209, 209, 209));
```

```css
background-image: linear-gradient(rgb(31, 171, 189) 0%, rgb(16, 123, 137) 100%);
```

```css
background-image: linear-gradient(rgb(168, 240, 185), rgb(115, 217, 141));
```

```css
background-image: linear-gradient(rgb(255, 255, 255) 0%, rgba(255, 255, 255, 0.82) 48%, rgba(0, 0, 0, 0) 100%);
```

```css
background-image: linear-gradient(rgb(54, 53, 53), rgb(39, 39, 39));
```

```css
background-image: linear-gradient(90deg, rgba(2, 10, 12, 0.33), rgba(0, 0, 0, 0) 33%), linear-gradient(rgba(0, 0, 0, 0.32), rgba(0, 0, 0, 0) 28%, rgba(0, 0, 0, 0.24));
```

```css
background-image: linear-gradient(rgba(5, 7, 8, 0.46), rgba(5, 7, 8, 0.58));
```

```css
background-image: radial-gradient(at 54% 91%, rgba(255, 255, 255, 0.05), rgba(0, 0, 0, 0) 39%), linear-gradient(145deg, rgba(255, 255, 255, 0.024), rgba(0, 0, 0, 0) 42%), none;
```

```css
background-image: repeating-linear-gradient(0deg, rgba(0, 0, 0, 0) 0px, rgba(0, 0, 0, 0) 7px, rgba(255, 255, 255, 0.02) 8px, rgba(255, 255, 255, 0.02) 9px), radial-gradient(at 48% 56%, rgba(255, 255, 255, 0.06), rgba(0, 0, 0, 0) 56%);
```

```css
background-image: linear-gradient(145deg, rgba(104, 104, 104, 0.91), rgba(70, 70, 70, 0.92));
```

```css
background-image: linear-gradient(rgb(238, 234, 225), rgb(199, 196, 190));
```

```css
background-image: linear-gradient(rgb(182, 176, 164), rgb(254, 253, 251));
```

```css
background-image: linear-gradient(rgba(52, 52, 52, 0) 18.229%, rgb(52, 52, 52) 100%);
```

```css
background-image: linear-gradient(rgba(0, 0, 0, 0), rgb(52, 52, 52) 75.5%);
```

```css
background-image: linear-gradient(145deg, rgb(91, 230, 124), rgb(28, 190, 83));
```

```css
background-image: linear-gradient(rgba(52, 52, 52, 0), rgb(52, 52, 52) 94.792%);
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0.34), rgba(255, 255, 255, 0.34)), none;
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.1)), none;
```

```css
background-image: linear-gradient(rgb(53, 53, 53), rgb(39, 39, 39));
```

```css
background-image: linear-gradient(rgb(50, 50, 50), rgb(39, 39, 39));
```

```css
background-image: linear-gradient(rgb(228, 228, 228), rgb(177, 177, 177));
```

```css
background-image: linear-gradient(rgb(180, 214, 31), rgb(132, 154, 36));
```

```css
background-image: linear-gradient(rgb(54, 53, 53) 0%, rgb(39, 39, 39) 100%);
```

```css
background-image: linear-gradient(rgb(255, 255, 255) 0%, rgb(209, 209, 209) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#f2f0ed` | text, border, background | 1491 |
| `#ffffff` | text, border, background | 1154 |
| `#111111` | background, text, border | 161 |
| `#272727` | background, text, border | 133 |
| `#000000` | border, background, text | 125 |
| `#343434` | background, text, border | 19 |
| `#1b1b1b` | background | 10 |
| `#909090` | border | 8 |
| `#102b1b` | text, border | 8 |
| `#ef8a80` | text, border | 6 |
| `#6ed8ba` | text, border | 6 |
| `#dcca65` | text, border | 6 |
| `#777777` | text, border | 6 |
| `#b2b2b2` | border | 4 |
| `#6c6c6c` | background | 4 |
| `#555555` | text, border | 3 |
| `#cfcfcf` | text, border | 2 |
| `#999999` | text, border | 2 |
| `#326ec8` | background | 1 |

## Typography

### Font Families

- **geistMono** — used for all (1372 elements)
- **Times New Roman** — used for body (68 elements)
- **monologueSerif** — used for all (61 elements)
- **Arial** — used for body (25 elements)
- **instrumentSerif** — used for body (18 elements)
- **instrumentSerifItalic** — used for body (4 elements)
- **monologueSerifItalic** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 92px | 5.75rem | 400 | 71.76px | -2.76px | h1 |
| 72px | 4.5rem | 400 | 72px | -1.44px | span |
| 52px | 3.25rem | 400 | 49.4px | -1.56px | h2 |
| 48px | 3rem | 400 | 43.2px | -1.44px | h2, br, span, strong |
| 46.44px | 2.9025rem | 400 | 46.44px | -1.44px | span |
| 46px | 2.875rem | 400 | 46px | normal | span |
| 38.095px | 2.3809rem | 400 | 34.2855px | -1.5238px | a, picture, source, img |
| 32px | 2rem | 400 | 30.4px | -0.96px | h2, h3, span, img |
| 28px | 1.75rem | 400 | 28px | -0.98px | h3, span |
| 26px | 1.625rem | 400 | normal | normal | strong |
| 24px | 1.5rem | 400 | 37.2px | -0.72px | h2, p, strong, span |
| 22.291px | 1.3932rem | 500 | normal | -0.6687px | span, img |
| 20px | 1.25rem | 500 | 20px | -0.2px | a, img, span, div |
| 18px | 1.125rem | 600 | normal | -0.54px | span |
| 16px | 1rem | 400 | normal | normal | html, head, meta, link |

### Heading Scale

```css
h1 { font-size: 92px; font-weight: 400; line-height: 71.76px; }
h2 { font-size: 52px; font-weight: 400; line-height: 49.4px; }
h2 { font-size: 48px; font-weight: 400; line-height: 43.2px; }
h2 { font-size: 32px; font-weight: 400; line-height: 30.4px; }
h3 { font-size: 28px; font-weight: 400; line-height: 28px; }
h2 { font-size: 24px; font-weight: 400; line-height: 37.2px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (1427x), `500` (105x), `700` (39x), `600` (21x), `800` (4x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-19 | 19px | 1.1875rem |
| spacing-26 | 26px | 1.625rem |
| spacing-31 | 31px | 1.9375rem |
| spacing-35 | 35px | 2.1875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-47 | 47px | 2.9375rem |
| spacing-50 | 50px | 3.125rem |
| spacing-52 | 52px | 3.25rem |
| spacing-58 | 58px | 3.625rem |
| spacing-60 | 60px | 3.75rem |
| spacing-64 | 64px | 4rem |
| spacing-66 | 66px | 4.125rem |
| spacing-72 | 72px | 4.5rem |
| spacing-75 | 75px | 4.6875rem |
| spacing-80 | 80px | 5rem |
| spacing-104 | 104px | 6.5rem |
| spacing-107 | 107px | 6.6875rem |
| spacing-127 | 127px | 7.9375rem |
| spacing-302 | 302px | 18.875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 1px | 2 |
| sm | 4px | 26 |
| md | 7px | 6 |
| md | 10px | 1 |
| lg | 14px | 12 |
| xl | 18px | 6 |
| xl | 22px | 12 |
| full | 50px | 115 |
| full | 999px | 46 |

## Box Shadows

**xs** — blur: 0.25px
```css
box-shadow: rgba(0, 0, 0, 0.6) 0px 0px 0.25px 0px;
```

**xs (inset)** — blur: 0.184px
```css
box-shadow: rgba(0, 0, 0, 0.16) 0px 0.184px 0.184px 0px, rgba(0, 0, 0, 0.25) 0px 0.092px 5.517px 0px, rgba(255, 255, 255, 0.2) 0px 0.276px 0.276px 0px inset, rgba(0, 0, 0, 0.16) 0px -0.276px 0.552px 0px inset;
```

**xs** — blur: 0.416667px
```css
box-shadow: rgba(255, 255, 255, 0.1) 0px 0px 0.416667px 0.833333px;
```

**xs** — blur: 0.5px
```css
box-shadow: rgba(0, 0, 0, 0.6) 0px 0px 0.5px 1px;
```

**xs** — blur: 0.5px
```css
box-shadow: rgba(255, 255, 255, 0.1) 0px 0px 0.5px 1px;
```

**xs** — blur: 0.5px
```css
box-shadow: rgba(0, 0, 0, 0.6) 0px 0px 0.5px 1px, rgba(0, 0, 0, 0.16) 0px 4px 8px 0px, rgba(0, 0, 0, 0.14) 0px 15px 15px 0px, rgba(0, 0, 0, 0.08) 0px 34px 21px 0px, rgba(0, 0, 0, 0.02) 0px 61px 24px 0px;
```

**xs** — blur: 0.5px
```css
box-shadow: rgba(0, 0, 0, 0.6) 0px 0px 0.5px 1px, rgba(0, 0, 0, 0.16) 0px 4px 8px 0px, rgba(0, 0, 0, 0.14) 0px 15px 15px 0px, rgba(0, 0, 0, 0.08) 0px 34px 21px 0px;
```

**xs (inset)** — blur: 0.5px
```css
box-shadow: rgba(0, 0, 0, 0.6) 0px 0px 0.5px 1px, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.13) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.48) 0px 2px 4px 0px, rgba(0, 0, 0, 0.2) 0px 8px 18px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.8) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.48) 0px 2px 4px 0px, rgba(0, 0, 0, 0.18) 0px 8px 18px 0px;
```

**xs** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.08) 1px 0px 0px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.54) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.28) 0px 1px 4px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.03) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.6) 0px 0px 0.5px 1px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.07) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.2) 0px 10px 25px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.7) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset;
```

**xs** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.25) 0px 1px 0px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.08) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.92) 0px 14px 16px -12px, rgba(0, 0, 0, 0.88) 0px 34px 58px -28px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.09) 0px 1px 0px 0px;
```

**xs** — blur: 0.515px
```css
box-shadow: rgba(0, 0, 0, 0.16) 0px 0.515px 0.515px 0px, rgba(0, 0, 0, 0.25) 0px 0.257px 15.448px 0px;
```

**xs (inset)** — blur: 0.666667px
```css
box-shadow: rgba(255, 255, 255, 0.16) 0.333333px 0.333333px 0.666667px 0px inset, rgba(0, 0, 0, 0.2) -0.333333px -0.333333px 0.666667px 0px inset;
```

**xs (inset)** — blur: 0.8px
```css
box-shadow: rgba(255, 255, 255, 0.16) 0.4px 0.4px 0.8px 0px inset, rgba(0, 0, 0, 0.2) -0.4px -0.4px 0.8px 0px inset;
```

**xs** — blur: 0.5px
```css
box-shadow: rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px;
```

**xs** — blur: 1px
```css
box-shadow: rgba(255, 255, 255, 0.25) -1px 0px 1px 0px, rgba(255, 255, 255, 0.25) 1px 0px 1px 0px;
```

**xs** — blur: 1px
```css
box-shadow: rgba(255, 255, 255, 0.25) 0px -1px 1px 0px;
```

**xs** — blur: 1px
```css
box-shadow: rgba(0, 0, 0, 0.06) 0px 1px 1px 0px;
```

**xs** — blur: 2px
```css
box-shadow: rgba(255, 255, 255, 0.92) 0px 0px 2px 0px;
```

**xs** — blur: 2px
```css
box-shadow: rgba(0, 0, 0, 0.82) 0px 0px 2px 0px;
```

**xs (inset)** — blur: 1px
```css
box-shadow: rgba(255, 255, 255, 0.24) 0px 1px 1px 0px inset, rgba(0, 0, 0, 0.45) 0px -1px 1px 0px;
```

**xs (inset)** — blur: 1px
```css
box-shadow: rgba(255, 255, 255, 0.2) -1px 0px 1px 0px inset, rgba(0, 0, 0, 0.22) 5px 0px 18px 0px;
```

**xs** — blur: 1px
```css
box-shadow: rgba(255, 255, 255, 0.25) 1px 0px 1px 0px;
```

**xs** — blur: 1px
```css
box-shadow: rgba(255, 255, 255, 0.14) 0px 1px 1px 0px;
```

**xs** — blur: 1px
```css
box-shadow: rgba(255, 255, 255, 0.16) -1px 0px 1px 0px, rgba(255, 255, 255, 0.16) 1px 0px 1px 0px;
```

**xs (inset)** — blur: 1px
```css
box-shadow: rgba(255, 255, 255, 0.25) -1px 0px 1px 0px, rgba(255, 255, 255, 0.25) 1px 0px 1px 0px, rgba(255, 255, 255, 0.25) 0px -1px 0.5px 0px inset;
```

**sm (inset)** — blur: 2px
```css
box-shadow: rgba(255, 255, 255, 0.16) 0px 2px 2px 0px inset, rgba(0, 0, 0, 0.22) 0px 5px 12px 0px;
```

**sm (inset)** — blur: 4px
```css
box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 4px 0px inset;
```

**sm (inset)** — blur: 2px
```css
box-shadow: rgba(255, 255, 255, 0.25) 0px 3px 2px 0px inset, rgba(0, 0, 0, 0.08) 0px -4px 1px 0px inset;
```

**sm** — blur: 4px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 4px 0px;
```

**md** — blur: 8px
```css
box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 8px 0px;
```

**md (inset)** — blur: 9.6px
```css
box-shadow: rgba(0, 0, 0, 0.06) -1.6px 1.6px 9.6px 0px, rgba(255, 255, 255, 0.16) 0.4px 0.4px 0.8px 0px inset, rgba(0, 0, 0, 0.2) -0.4px -0.4px 0.8px 0px inset;
```

**md** — blur: 8px
```css
box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 8px 0px, rgba(0, 0, 0, 0.14) 0px 15px 15px 0px, rgba(0, 0, 0, 0.08) 0px 34px 21px 0px, rgba(0, 0, 0, 0.02) 0px 61px 24px 0px;
```

**md** — blur: 8px
```css
box-shadow: rgba(0, 0, 0, 0.19) 0px 4px 8px 0px, rgba(0, 0, 0, 0.17) 0px 15px 15px 0px, rgba(0, 0, 0, 0.1) 0px 34px 20px 0px, rgba(0, 0, 0, 0.03) 0px 60px 24px 0px;
```

**lg** — blur: 16px
```css
box-shadow: rgba(0, 0, 0, 0.32) 0px 8px 16px 0px;
```

**lg** — blur: 18px
```css
box-shadow: rgba(0, 0, 0, 0.42) 0px 12px 18px 0px;
```

**xl** — blur: 24px
```css
box-shadow: rgba(0, 0, 0, 0.03) 0px 60px 24px 0px, rgba(0, 0, 0, 0.1) 0px 34px 20px 0px, rgba(0, 0, 0, 0.17) 0px 15px 15px 0px, rgba(0, 0, 0, 0.19) 0px 4px 8px 0px;
```

**xl** — blur: 38.213px
```css
box-shadow: rgba(0, 0, 0, 0.03) 0px 95.532px 38.213px 0px, rgba(0, 0, 0, 0.1) 0px 54.135px 31.844px 0px, rgba(0, 0, 0, 0.17) 0px 23.883px 23.883px 0px, rgba(0, 0, 0, 0.19) 0px 6.369px 12.738px 0px;
```

**xl (inset)** — blur: 38.213px
```css
box-shadow: rgba(0, 0, 0, 0.03) 0px 95.532px 38.213px 0px, rgba(0, 0, 0, 0.1) 0px 54.135px 31.844px 0px, rgba(0, 0, 0, 0.17) 0px 23.883px 23.883px 0px, rgba(0, 0, 0, 0.19) 0px 6.369px 12.738px 0px, rgba(255, 255, 255, 0.08) 0px 1px 0px 0px inset;
```

**xl** — blur: 83px
```css
box-shadow: rgba(0, 0, 0, 0.04) 0px 208px 83px 0px, rgba(0, 0, 0, 0.14) 0px 117px 70px 0px, rgba(0, 0, 0, 0.23) 0px 52px 52px 0px, rgba(0, 0, 0, 0.27) 0px 13px 29px 0px;
```

## CSS Custom Properties

### Colors

```css
--muted: #ffffffb8;
--card-shadow: 0 0 .5px 1px #0009;
--button-primary-shadow: inset 0 1px #fffc, 0 2px 4px #0000007a, 0 8px 18px #0000002e;
--button-primary-shadow-hover: inset 0 1px #ffffffeb, 0 5px 8px #00000085, 0 16px 30px #00000057;
--button-secondary-shadow: inset 0 1px #ffffff1a, 0 2px 4px #0000007a, 0 8px 18px #0003;
--button-secondary-shadow-hover: inset 0 1px #ffffff29, 0 5px 8px #0000008f, 0 16px 30px #0000005c;
```

### Spacing

```css
--button-padding-inline: 24px;
--button-font-size: 20px;
```

### Typography

```css
--font-instrument-serif-italic: "instrumentSerifItalic", "instrumentSerifItalic Fallback", Georgia, serif;
--font-instrument-serif: "instrumentSerif", "instrumentSerif Fallback", Georgia, serif;
--font-monologue-serif: "monologueSerif", "monologueSerif Fallback", Georgia, serif;
--font-geist-mono: "geistMono", "geistMono Fallback";
--font-monologue-serif-italic: "monologueSerifItalic", "monologueSerifItalic Fallback", Georgia, serif;
```

### Shadows

```css
--horizontal-divider-shadow: 0 1px .5px var(--divider-highlight);
--horizontal-divider-shadow-reverse: 0 -1px 1px var(--divider-highlight);
--horizontal-divider-shadow-inset-top: inset 0 1px .5px var(--divider-highlight);
--horizontal-divider-shadow-inset-bottom: inset 0 -1px .5px var(--divider-highlight);
--vertical-divider-shadow: -1px 0 1px var(--divider-highlight), 1px 0 1px var(--divider-highlight);
--section-shadow: var(--horizontal-divider-shadow);
--header-shadow: var(--line-highlight);
--rail-shadow: var(--vertical-divider-shadow);
```

### Radii

```css
--button-radius: 8px;
```

### Other

```css
--lightningcss-light: ;
--lightningcss-dark: initial;
--page: #121212;
--surface: #272727;
--surface-high: #343434;
--ink: #f2f0ed;
--faint: #ffffff73;
--black-line: #0009;
--frame-stroke: #4e4e4e;
--white-line: #ffffff1a;
--mono: var(--font-geist-mono), "SFMono-Regular", Consolas, monospace;
--display: var(--font-monologue-serif), Georgia, serif;
--display-italic: var(--font-monologue-serif-italic), Georgia, serif;
--wordmark: var(--font-instrument-serif), Georgia, serif;
--wordmark-italic: var(--font-instrument-serif-italic), Georgia, serif;
--content-rail-max: 1200px;
--divider-highlight: #ffffff40;
--line-highlight: var(--horizontal-divider-shadow);
--line-highlight-inset: var(--horizontal-divider-shadow-inset-top);
--glass-blur: 16px;
--glass-blur-elevated: 25.475px;
--button-height: 64px;
```

### Dependencies

```css
--mono: --font-geist-mono;
--display: --font-monologue-serif;
--display-italic: --font-monologue-serif-italic;
--wordmark: --font-instrument-serif;
--wordmark-italic: --font-instrument-serif-italic;
--horizontal-divider-shadow: --divider-highlight;
--horizontal-divider-shadow-reverse: --divider-highlight;
--horizontal-divider-shadow-inset-top: --divider-highlight;
--horizontal-divider-shadow-inset-bottom: --divider-highlight;
--vertical-divider-shadow: --divider-highlight,--divider-highlight;
--line-highlight: --horizontal-divider-shadow;
--line-highlight-inset: --horizontal-divider-shadow-inset-top;
--section-shadow: --horizontal-divider-shadow;
--header-shadow: --line-highlight;
--rail-shadow: --vertical-divider-shadow;
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
| xs | 360px | max-width |
| xs | 361px | min-width |
| sm | 480px | max-width |
| sm | 481px | min-width |
| md | 760px | max-width |
| md | 761px | min-width |
| lg | 960px | max-width |
| 1120px | 1120px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.18s`, `0.22s`, `0.16s`, `0.24s`, `0.32s`, `0.46s`, `0.26s`, `0.04s`, `0.09s`, `0.12s`, `0.07s`, `0.14s`, `0.62s`, `0.28s`

### Common Transitions

```css
transition: all;
transition: background-color 0.18s, border-color 0.18s, box-shadow 0.18s;
transition: width 0.22s cubic-bezier(0.22, 1, 0.36, 1), height 0.22s cubic-bezier(0.22, 1, 0.36, 1), margin-top 0.22s cubic-bezier(0.22, 1, 0.36, 1), border-color 0.18s, border-radius 0.22s cubic-bezier(0.22, 1, 0.36, 1), padding 0.22s cubic-bezier(0.22, 1, 0.36, 1), background-color 0.18s, box-shadow 0.18s;
transition: background-position 0.22s cubic-bezier(0.22, 1, 0.36, 1), border-color 0.18s, box-shadow 0.18s, transform 0.18s;
transition: color 0.18s, text-decoration-color 0.18s;
transition: background-color 0.16s cubic-bezier(0.23, 1, 0.32, 1);
transition: opacity 0.24s cubic-bezier(0.23, 1, 0.32, 1), transform 0.24s cubic-bezier(0.23, 1, 0.32, 1);
transition: background-color 0.22s, filter 0.22s;
transition: opacity 0.16s ease-out, transform 0.16s cubic-bezier(0.22, 1, 0.36, 1);
transition: border-color 0.32s, box-shadow 0.32s;
```

### Keyframe Animations

**product-story-progress**
```css
@keyframes product-story-progress {
  0% { transform: scaleX(0); }
  100% { transform: scaleX(1); }
}
```

**product-story-copy-in**
```css
@keyframes product-story-copy-in {
  0% { opacity: 0; transform: translateY(3px); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**trusted-logo-scroll**
```css
@keyframes trusted-logo-scroll {
  100% { transform: translate(-50%); }
}
```

**work-story-reading-highlight**
```css
@keyframes work-story-reading-highlight {
  0% { color: rgba(255, 255, 255, 0.42); }
  100% { color: rgb(255, 255, 255); }
}
```

**dictation-wave-flow**
```css
@keyframes dictation-wave-flow {
  0% { filter: brightness(0.78) blur(0.15px); transform: translate(-4px) scaleY(0.72); }
  45% { filter: brightness(1.18) blur(); transform: translate(0px) scaleY(1); }
  100% { filter: brightness(0.92) blur(0.1px); transform: translate(4px) scaleY(0.82); }
}
```

**dictation-caret-blink**
```css
@keyframes dictation-caret-blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0.08; }
}
```

**dictation-processing-spin**
```css
@keyframes dictation-processing-spin {
  100% { transform: rotate(360deg); }
}
```

**dictation-listening-glow**
```css
@keyframes dictation-listening-glow {
  0% { box-shadow: rgba(25, 208, 232, 0) 0px 0px; }
  100% { box-shadow: rgba(25, 208, 232, 0.34) 0px 0px 24px; }
}
```

**dictation-paste-in**
```css
@keyframes dictation-paste-in {
  0% { opacity: 0; transform: translateY(8px) scale(0.985); }
  100% { opacity: 1; transform: translateY(0px) scale(1); }
}
```

**dictation-correction-strike**
```css
@keyframes dictation-correction-strike {
  100% { transform: scaleX(1); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (37 instances)

```css
.button {
  background-color: rgb(254, 253, 251);
  color: rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 500;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 8px;
}
```

### Cards (43 instances)

```css
.card {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 8px 0px, rgba(0, 0, 0, 0.14) 0px 15px 15px 0px, rgba(0, 0, 0, 0.08) 0px 34px 21px 0px, rgba(0, 0, 0, 0.02) 0px 61px 24px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (42 instances)

```css
.link {
  color: rgba(255, 255, 255, 0.42);
  font-size: 14px;
  font-weight: 400;
}
```

### Navigation (8 instances)

```css
.navigatio {
  background-color: rgb(39, 39, 39);
  color: rgb(242, 240, 237);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
  box-shadow: rgba(255, 255, 255, 0.13) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px;
}
```

### Footer (13 instances)

```css
.foote {
  background-color: rgb(39, 39, 39);
  color: rgb(242, 240, 237);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Tables (1 instances)

```css
.table {
  border-color: rgb(20, 20, 20);
  background-color: rgb(39, 39, 39);
  cell-style: [object Object];
}
```

### Badges (15 instances)

```css
.badge {
  background-color: rgb(108, 108, 108);
  color: rgb(40, 40, 40);
  font-size: 20px;
  font-weight: 500;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Avatars (3 instances)

```css
.avatar {
  border-radius: 50%;
  background-color: rgb(50, 110, 200);
}
```

### Tabs (31 instances)

```css
.tab {
  background-color: rgba(255, 255, 255, 0.1);
  color: rgb(242, 240, 237);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(255, 255, 255);
  border-radius: 0px;
}
```

### Accordions (10 instances)

```css
.accordion {
  color: rgb(242, 240, 237);
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(242, 240, 237) rgb(242, 240, 237) rgba(0, 0, 0, 0.6);
}
```

### ProgressBars (2 instances)

```css
.progressBar {
  color: rgb(255, 255, 255);
  border-radius: 0px;
  font-size: 14px;
}
```

### Switches (5 instances)

```css
.switche {
  background-color: rgb(44, 44, 44);
  border-radius: 0px;
  border-color: rgb(242, 240, 237);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 8 instances, 3 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 14px 0px 14px;
  border-radius: 9px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 14px;
  font-weight: 500;
```

**Variant 2** (6 instances)

```css
  background: rgb(254, 253, 251);
  color: rgb(40, 40, 40);
  padding: 0px 24px 0px 24px;
  border-radius: 8px;
  border: 1px solid rgb(242, 238, 229);
  font-size: 20px;
  font-weight: 500;
```

**Variant 3** (1 instance)

```css
  background: rgb(39, 39, 39);
  color: rgb(255, 255, 255);
  padding: 0px 24px 0px 24px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 20px;
  font-weight: 500;
```

### Button — 9 instances, 1 variant

**Variant 1** (9 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgba(0, 0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(254, 253, 251);
  color: rgb(40, 40, 40);
  padding: 0px 14px 0px 14px;
  border-radius: 9px;
  border: 1px solid rgb(242, 238, 229);
  font-size: 14px;
  font-weight: 500;
```

### Button — 3 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgba(255, 255, 255, 0.72);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgba(255, 255, 255, 0.72);
  font-size: 14px;
  font-weight: 500;
```

**Variant 2** (1 instance)

```css
  background: rgb(254, 253, 251);
  color: rgb(40, 40, 40);
  padding: 0px 14px 0px 14px;
  border-radius: 9px;
  border: 1px solid rgb(242, 238, 229);
  font-size: 14px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0.1);
  color: rgb(255, 255, 255);
  padding: 5px 16px 5px 16px;
  border-radius: 8px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 5px 16px 5px 16px;
  border-radius: 8px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 400;
```

### Button — 11 instances, 3 variants

**Variant 1** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(242, 240, 237);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(242, 240, 237);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(38, 38, 38);
  padding: 1px 6px 1px 6px;
  border-radius: 9px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  font-size: 24px;
  font-weight: 400;
```

**Variant 3** (2 instances)

```css
  background: rgba(255, 255, 255, 0.1);
  color: rgb(255, 255, 255);
  padding: 0px 8px 0px 8px;
  border-radius: 8px;
  border: 0px none rgb(255, 255, 255);
  font-size: 12px;
  font-weight: 500;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(52, 52, 52);
  color: rgb(242, 240, 237);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 16px;
  font-weight: 400;
```

### Card — 7 instances, 1 variant

**Variant 1** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(242, 240, 237);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(242, 240, 237);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(52, 52, 52);
  color: rgb(242, 240, 237);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(52, 52, 52);
  color: rgb(242, 240, 237);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(52, 52, 52);
  color: rgb(242, 240, 237);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 16px;
  font-weight: 400;
```

### Button — 7 instances, 2 variants

**Variant 1** (6 instances)

```css
  background: rgba(52, 52, 52, 0.78);
  color: rgb(255, 255, 255);
  padding: 12px 12px 12px 12px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  font-size: 20px;
  font-weight: 500;
```

**Variant 2** (1 instance)

```css
  background: rgba(255, 255, 255, 0.1);
  color: rgb(242, 240, 237);
  padding: 5px 16px 5px 16px;
  border-radius: 8px;
  border: 0px none rgb(242, 240, 237);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(52, 52, 52);
  color: rgb(242, 240, 237);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(242, 240, 237);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(242, 240, 237);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgba(0, 0, 0, 0);
  padding: 0px 0px 3px 0px;
  border-radius: 0px;
  border: 0px none rgba(0, 0, 0, 0);
  font-size: 28px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(52, 52, 52);
  color: rgb(242, 240, 237);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 16px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(242, 240, 237);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(242, 240, 237);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(52, 52, 52);
  color: rgb(242, 240, 237);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**102 grid containers** and **257 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1000px | 0px |
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 81x |
| 2-column | 6x |
| 3-column | 3x |
| 17-column | 2x |
| 5-column | 1x |

### Grid Templates

```css
grid-template-columns: 335.328px 335.328px 335.344px;
gap: 20px;
grid-template-columns: 1046px;
grid-template-columns: 490px 490px;
gap: 24px 20px;
grid-template-columns: 373.594px 560.406px;
gap: 72px;
grid-template-columns: 1124px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 152x |
| column/nowrap | 105x |

**Gap values:** `10px`, `11.429px`, `12px`, `14px`, `16px`, `20px`, `24px`, `24px 20px`, `3.862px`, `32px`, `3px`, `4.634px`, `48px`, `4px`, `5px`, `6.3px`, `6px`, `72px`, `7px`, `80px`, `8px`, `9px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 9 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#282828` | `#fefdfb` | 14.5:1 | AAA |
| `#ffffff` | `#272727` | 14.94:1 | AAA |
| `#161616` | `#ffffff` | 18.1:1 | AAA |
| `#cfcfcf` | `#373737` | 7.64:1 | AAA |
| `#ffffff` | `#326ec8` | 5:1 | AA |

## Design System Score

**Overall: 75/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 40/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 50/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 7 font families — consider limiting to 2 (heading + body)
- 26 distinct font sizes — consider a tighter type scale
- 49 unique shadows — consider a 3-level elevation scale (sm/md/lg)
- 30 !important rules — prefer specificity over overrides
- 2760 duplicate CSS declarations

## Gradients

**38 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 3 | bold |
| linear | — | 3 | bold |
| linear | — | 2 | brand |
| linear | 90deg | 4 | bold |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 3 | bold |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 3 | bold |

```css
background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(235, 235, 235, 0.9));
background: linear-gradient(rgb(60, 60, 60) 0%, rgb(41, 41, 41) 100%);
background: linear-gradient(rgb(182, 176, 164) 0%, rgb(254, 253, 251) 50%, rgb(182, 176, 164) 100%);
background: linear-gradient(-21.4897deg, rgb(40, 40, 40) 1.6162%, rgb(64, 64, 64) 100.38%);
background: linear-gradient(rgb(255, 114, 98), rgb(107, 39, 31));
```

## Z-Index Map

**10 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| dropdown | 100,100 | a.s.k.i.p.-.l.i.n.k |
| sticky | 50,50 | header.d.e.s.i.g.n.-.s.e.c.t.i.o.n. .s.i.t.e.-.h.e.a.d.e.r |
| base | -2,5 | img.n.o.t.e.s.-.c.a.r.o.u.s.e.l.-.i.m.a.g.e. .n.o.t.e.s.-.c.a.r.o.u.s.e.l.-.i.m.a.g.e.-.-.c.a.p.t.u.r.e, img.n.o.t.e.s.-.c.a.r.o.u.s.e.l.-.i.m.a.g.e. .n.o.t.e.s.-.c.a.r.o.u.s.e.l.-.i.m.a.g.e.-.-.s.u.m.m.a.r.i.z.e, img.n.o.t.e.s.-.c.a.r.o.u.s.e.l.-.i.m.a.g.e. .n.o.t.e.s.-.c.a.r.o.u.s.e.l.-.i.m.a.g.e.-.-.s.h.a.r.e |

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| geistMono | self-hosted | 400, 500, 600 | normal |
| monologueSerif | self-hosted | 400 | normal |
| monologueSerifItalic | self-hosted | 400 | italic |
| instrumentSerif | self-hosted | 400 | normal |
| instrumentSerifItalic | self-hosted | 400 | italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 131 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 15 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 7 | objectFit: contain, borderRadius: 0px, shape: square |
| hero | 5 | objectFit: cover, borderRadius: 0px, shape: square |
| avatar | 1 | objectFit: cover, borderRadius: 50%, shape: circular |

**Aspect ratios:** 1:1 (96x), 3:4 (21x), 21:9 (4x), 16:9 (3x), 3.65:1 (3x), 4:3 (3x), 6.59:1 (2x), 4.04:1 (2x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `40ms` | 40 |
| `xs` | `90ms` | 90 |
| `sm` | `160ms` | 160 |
| `md` | `260ms` | 260 |
| `lg` | `460ms` | 460 |

### Easing Families

- **ease-out** (69 uses) — `cubic-bezier(0.22, 1, 0.36, 1)`, `cubic-bezier(0.23, 1, 0.32, 1)`, `cubic-bezier(0.16, 1, 0.3, 1)`
- **ease-in-out** (24 uses) — `ease`
- **custom** (5 uses) — `cubic-bezier(0.77, 0, 0.175, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `product-story-progress` | scale | transform | 1 |
| `product-story-copy-in` | slide-y | opacity, transform | 1 |
| `trusted-logo-scroll` | slide | transform | 1 |
| `dictation-caret-blink` | fade | opacity | 4 |
| `feature-app-float` | slide | transform | 12 |
| `feature-app-orbit-clockwise` | rotate | transform | 1 |
| `feature-mode-preview-enter` | slide-y | opacity, transform | 1 |
| `feature-caret-blink` | fade | opacity | 1 |
| `testimonial-enter` | slide-y | opacity, transform | 1 |
| `testimonial-progress` | scale | transform | 1 |

## Component Anatomy

### button — 44 instances

**Slots:** label, icon
**Variants:** secondary · primary · link

| variant | count | sample label |
|---|---|---|
| default | 33 | iPhone, iPad, and Apple Watch |
| primary | 8 | Download for Mac |
| secondary | 2 | Download for iOS |
| link | 1 | App Store |

### card — 24 instances

**Slots:** media

## Brand Voice

**Tone:** neutral · **Pronoun:** we→you · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **download** (9)
- **email** (2)
- **watch** (1)
- **dictation** (1)
- **voice** (1)
- **meetings** (1)
- **mcp** (1)
- **to** (1)

### Button Copy Patterns

- "download for mac" (8×)
- "email" (2×)
- "download for ios" (1×)
- "iphone, ipad, and apple watch" (1×)
- "dictation" (1×)
- "voice notes" (1×)
- "meetings" (1×)
- "mcp, api, and cli" (1×)
- "↑" (1×)
- "to do’s" (1×)

### Sample Headings

> Builders think out loud.
> Speak instead of typing
> Monologue is what happens when you talk through your work instead of typing it.
> Use your voice
wherever you type
> Give your coding agent the whole task
> Builders think out loud.
> Speak instead of typing
> Monologue is what happens when you talk through your work instead of typing it.
> Use your voice
wherever you type
> Give your coding agent the whole task

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** Monologue brings voice dictation, voice notes, and bot-free meeting transcription together in one app for Mac, iPhone, iPad, and Apple Watch.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → pricing → hero → hero → content → content → pricing → sidebar → pricing → nav → nav → nav → hero → feature-grid → hero → testimonial → pricing-table → testimonial → faq → content → testimonials → hero → footer → pricing → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | pricing | Builders think out loud. | 0.4 |
| 3 | hero | Builders think out loud. | 0.85 |
| 4 | hero | Speak instead of typing | 0.4 |
| 5 | content | — | 0.3 |
| 6 | content | Monologue is what happens when you talk through your work instead of typing it. | 0.3 |
| 7 | pricing | Use your voice
wherever you type | 0.4 |
| 8 | nav | — | 0.9 |
| 9 | sidebar | — | 0.4 |
| 10 | pricing | — | 0.4 |
| 11 | nav | — | 0.4 |
| 12 | nav | — | 0.4 |
| 13 | hero | A notes app built for
builders | 0.4 |
| 14 | feature-grid | Monologue adapts to
the way you work | 0.8 |
| 15 | hero | Platforms We Support | 0.4 |
| 16 | testimonial | — | 0.8 |
| 17 | pricing-table | Pricing | 0.9 |
| 18 | testimonial | One app for dictation,
voice notes, and meetings | 0.8 |
| 19 | faq | FAQ | 0.85 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.152 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 999px |
| backdrop-filter in use | no |
| Gradients | 38 |

## Imagery Style

**Label:** `3d-render` (confidence 0.176)
**Counts:** total 159, svg 0, icon 122, screenshot-like 0, photo-like 3
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `geistMono` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
