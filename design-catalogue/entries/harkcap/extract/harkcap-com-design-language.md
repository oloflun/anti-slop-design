# Design Language: Hark Capital

> Extracted from `https://www.harkcap.com` on September 4, 2026
> 1389 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#114167` | rgb(17, 65, 103) | hsl(207, 72%, 24%) | 57 |
| Secondary | `#00f2e5` | rgb(0, 242, 229) | hsl(177, 100%, 47%) | 60 |
| Accent | `#235e80` | rgb(35, 94, 128) | hsl(202, 57%, 32%) | 15 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#181818` | hsl(0, 0%, 9%) | 1910 |
| `#ffffff` | hsl(0, 0%, 100%) | 560 |
| `#f3f3f3` | hsl(0, 0%, 95%) | 67 |
| `#919598` | hsl(206, 3%, 58%) | 63 |
| `#000000` | hsl(0, 0%, 0%) | 45 |
| `#232323` | hsl(0, 0%, 14%) | 25 |
| `#d4d4d4` | hsl(0, 0%, 83%) | 19 |

### Background Colors

Used on large-area elements: `#ffffff`, `#f3f3f3`, `#d4d4d4`, `#235e80`, `#181818`, `#232323`

### Text Colors

Text color palette: `#000000`, `#181818`, `#ffffff`, `#062541`, `#114167`, `#232323`, `#919598`, `#00f2e5`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#181818` | text, border, background | 1910 |
| `#ffffff` | background, text, border | 560 |
| `#062541` | text, border | 144 |
| `#f3f3f3` | background | 67 |
| `#919598` | border, background, text | 63 |
| `#00f2e5` | text, border | 60 |
| `#114167` | background, text, border | 57 |
| `#000000` | text, border, background | 45 |
| `#232323` | text, border, background | 25 |
| `#d4d4d4` | background, border | 19 |
| `#235e80` | background | 15 |

## Typography

### Font Families

- **Aeonikpro** — used for body (1342 elements)
- **Suisseworks Webs** — used for body (23 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 229.231px | 14.3269rem | 400 | 229.231px | normal | div |
| 86.3077px | 5.3942rem | 400 | 77.6769px | normal | div |
| 53.2308px | 3.3269rem | 400 | 58.5538px | normal | div |
| 44.3077px | 2.7692rem | 400 | 44.3077px | normal | a, div |
| 28.6154px | 1.7885rem | 400 | 31.4769px | normal | div |
| 21.8462px | 1.3654rem | 400 | 26.2154px | normal | div |
| 17.8462px | 1.1154rem | 400 | 24.9846px | normal | body, div, style, nav |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14px | 0.875rem | 400 | 18.2px | normal | p, div, a |
| 12px | 0.75rem | 400 | 16.8px | normal | div |

### Body Text

```css
body { font-size: 14px; font-weight: 400; line-height: 18.2px; }
```

### Font Weights in Use

`400` (1379x), `500` (8x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-36 | 36px | 2.25rem |
| spacing-42 | 42px | 2.625rem |
| spacing-58 | 58px | 3.625rem |
| spacing-63 | 63px | 3.9375rem |
| spacing-74 | 74px | 4.625rem |
| spacing-86 | 86px | 5.375rem |
| spacing-110 | 110px | 6.875rem |
| spacing-115 | 115px | 7.1875rem |
| spacing-131 | 131px | 8.1875rem |
| spacing-177 | 177px | 11.0625rem |
| spacing-196 | 196px | 12.25rem |
| spacing-457 | 457px | 28.5625rem |
| spacing-473 | 473px | 29.5625rem |
| spacing-490 | 490px | 30.625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 24 |
| md | 6px | 2 |
| full | 1280px | 7 |

## CSS Custom Properties

### Colors

```css
--_theme---heading-accent: var(--swatch--brand-600);
--_typography---font--primary-family: Aeonikpro, Arial, sans-serif;
--_typography---font--primary-regular: 400;
--_typography---font--primary-medium: 500;
--_typography---font--primary-bold: 700;
--border-width--main: .094rem;
--_theme---border: var(--swatch--dark-900-o20);
--_button-style---border: var(--_theme---button-primary--border);
--_button-style---border-hover: var(--_theme---button-primary--border-hover);
--_theme---text-link--border: var(--_theme---border);
--_theme---text-link--border-hover: var(--_theme---text);
--_typography---font--secondary-family: "Suisseworks Webs", Georgia, sans-serif;
--_typography---font-size--text-accent: var(--sizes--2-5rem);
--_theme---button-primary--text-hover: var(--_theme---background);
--_theme---button-primary--background: var(--swatch--brand-cobalt);
--_theme---button-primary--border: var(--_theme---button-primary--background);
--_theme---button-primary--text: var(--swatch--brand-text);
--_theme---button-primary--background-hover: var(--_theme---text);
--_theme---button-primary--border-hover: var(--_theme---button-primary--background-hover);
--_theme---button-secondary--background: var(--swatch--transparent);
--_theme---button-secondary--border: var(--_theme---border);
--_theme---button-secondary--text: var(--_theme---text);
--_theme---button-secondary--background-hover: var(--_theme---text);
--_theme---button-secondary--border-hover: var(--_theme---button-secondary--background-hover);
--_theme---button-secondary--text-hover: var(--_theme---background);
--_typography---font--primary-trim-top: .49em;
--_typography---font--primary-trim-bottom: .35em;
--_typography---font--secondary-trim-top: .36em;
--_typography---font--secondary-trim-bottom: .35em;
--_typography---font--secondary-regular: 400;
--swiper-theme-color: #007aff;
```

### Spacing

```css
--_text-style---font-size: var(--_typography---font-size--text-main);
--_text-style---letter-spacing: var(--_typography---letter-spacing--0em);
--sizes--1-125rem: clamp(.95 * 1rem, ((.95 - ((1.125 - .95) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.125 - .95) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.125 * 1rem);
--_gap---size: var(--site--gutter);
--sizes--1rem: clamp(1 * 1rem, ((1 - ((1 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1 * 1rem);
--sizes--0rem: 0rem;
--_text-style---margin-top: var(--_spacing---space--4);
--_text-style---margin-bottom: var(--_spacing---space--4);
--_spacing---space--6: clamp(2 * 1rem, ((2 - ((2.5 - 2) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((2.5 - 2) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 2.5 * 1rem);
--_spacing---space--7: clamp(2.25 * 1rem, ((2.25 - ((3 - 2.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((3 - 2.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 3 * 1rem);
--site--margin: clamp(1 * 1rem, ((1 - ((1.875 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.875 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.875 * 1rem);
--_spacing---section-space--none: 0px;
--_spacing---section-space--small: clamp(1 * 1rem, ((1 - ((1.875 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.875 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.875 * 1rem);
--_spacing---section-space--main: clamp(2 * 1rem, ((2 - ((3.75 - 2) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((3.75 - 2) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 3.75 * 1rem);
--_spacing---section-space--large: clamp(4 * 1rem, ((4 - ((7.5 - 4) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((7.5 - 4) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 7.5 * 1rem);
--_spacing---section-space--page-top: clamp(7 * 1rem, ((7 - ((14 - 7) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((14 - 7) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 14 * 1rem);
--_spacing---space--2: clamp(.625 * 1rem, ((.625 - ((.75 - .625) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((.75 - .625) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), .75 * 1rem);
--_spacing---space--1: clamp(.375 * 1rem, ((.375 - ((.5 - .375) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((.5 - .375) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), .5 * 1rem);
--_spacing---space--3: clamp(.875 * 1rem, ((.875 - ((1 - .875) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1 - .875) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1 * 1rem);
--_spacing---space--4: clamp(1.25 * 1rem, ((1.25 - ((1.5 - 1.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.5 - 1.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.5 * 1rem);
--_spacing---space--5: clamp(1.75 * 1rem, ((1.75 - ((2 - 1.75) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((2 - 1.75) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 2 * 1rem);
--_spacing---space--8: clamp(2.5 * 1rem, ((2.5 - ((4 - 2.5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((4 - 2.5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 4 * 1rem);
--_typography---font-size--text-fine: var(--sizes--0-875rem);
--_typography---font-size--text-cat: var(--sizes--0-75rem);
--_typography---font-size--text-graphic-2: var(--sizes--6-5rem);
--_typography---font-size--text-graphic-title: var(--sizes--4rem);
--sizes--1-25rem: clamp(1.125 * 1rem, ((1.125 - ((1.25 - 1.125) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.25 - 1.125) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.25 * 1rem);
--sizes--1-5rem: clamp(1.25 * 1rem, ((1.25 - ((1.5 - 1.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.5 - 1.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.5 * 1rem);
--sizes--13rem: clamp(6.25 * 1rem, ((6.25 - ((13 - 6.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((13 - 6.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 13 * 1rem);
--sizes--3rem: clamp(2.25 * 1rem, ((2.25 - ((3 - 2.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((3 - 2.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 3 * 1rem);
--sizes--3-5rem: clamp(2.5 * 1rem, ((2.5 - ((3.5 - 2.5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((3.5 - 2.5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 3.5 * 1rem);
--sizes--16rem: clamp(9 * 1rem, ((9 - ((16 - 9) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((16 - 9) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 16 * 1rem);
--sizes--0-875rem: .875rem;
--sizes--0-625rem: .625rem;
--sizes--0-5rem: .5rem;
--sizes--0-125rem: .125rem;
--sizes--0-75rem: .75rem;
--sizes--1-75rem: clamp(1.5 * 1rem, ((1.5 - ((1.75 - 1.5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.75 - 1.5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.75 * 1rem);
--sizes--2-25rem: clamp(1.825 * 1rem, ((1.825 - ((2.25 - 1.825) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((2.25 - 1.825) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 2.25 * 1rem);
--sizes--7-5rem: clamp(4.25 * 1rem, ((4.25 - ((7.5 - 4.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((7.5 - 4.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 7.5 * 1rem);
--sizes--5rem: clamp(3 * 1rem, ((3 - ((5 - 3) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((5 - 3) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 5 * 1rem);
--sizes--14rem: clamp(6.5 * 1rem, ((6.5 - ((14 - 6.5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((14 - 6.5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 14 * 1rem);
--sizes--3-75rem: clamp(2.625 * 1rem, ((2.625 - ((3.75 - 2.625) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((3.75 - 2.625) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 3.75 * 1rem);
--sizes--1-875rem: clamp(1.625 * 1rem, ((1.625 - ((1.875 - 1.625) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.875 - 1.625) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.875 * 1rem);
--sizes--2-75rem: clamp(2.125 * 1rem, ((2.125 - ((2.75 - 2.125) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((2.75 - 2.125) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 2.75 * 1rem);
--_typography---font-size--text-main: clamp(1 * 1rem, ((1 - ((1.25 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.25 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.25 * 1rem);
--sizes--2rem: clamp(1.75 * 1rem, ((1.75 - ((2 - 1.75) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((2 - 1.75) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 2 * 1rem);
--sizes--4rem: clamp(2.75 * 1rem, ((2.75 - ((4 - 2.75) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((4 - 2.75) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 4 * 1rem);
--sizes--0-375rem: .375rem;
--sizes--0-25rem: .25rem;
--sizes--2-5rem: clamp(2 * 1rem, ((2 - ((2.5 - 2) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((2.5 - 2) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 2.5 * 1rem);
--sizes--4-5rem: clamp(2.875 * 1rem, ((2.875 - ((4.5 - 2.875) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((4.5 - 2.875) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 4.5 * 1rem);
--sizes--1-625rem: clamp(1.325 * 1rem, ((1.325 - ((1.625 - 1.325) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.625 - 1.325) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.625 * 1rem);
--sizes--11rem: clamp(5.75 * 1rem, ((5.75 - ((11 - 5.75) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((11 - 5.75) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 11 * 1rem);
--sizes--9-5rem: clamp(5.25 * 1rem, ((5.25 - ((9.5 - 5.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((9.5 - 5.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 9.5 * 1rem);
--sizes--6rem: clamp(3.5 * 1rem, ((3.5 - ((6 - 3.5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((6 - 3.5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 6 * 1rem);
--sizes--7rem: clamp(4 * 1rem, ((4 - ((7 - 4) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((7 - 4) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 7 * 1rem);
--sizes--6-5rem: clamp(3.75 * 1rem, ((3.75 - ((6.5 - 3.75) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((6.5 - 3.75) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 6.5 * 1rem);
--sizes--8rem: clamp(4.5 * 1rem, ((4.5 - ((8 - 4.5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((8 - 4.5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 8 * 1rem);
--sizes--5-5rem: clamp(3.25 * 1rem, ((3.25 - ((5.5 - 3.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((5.5 - 3.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 5.5 * 1rem);
--sizes--3-25rem: clamp(2.375 * 1rem, ((2.375 - ((3.25 - 2.375) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((3.25 - 2.375) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 3.25 * 1rem);
--sizes--9rem: clamp(5 * 1rem, ((5 - ((9 - 5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((9 - 5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 9 * 1rem);
--sizes--10rem: clamp(5.5 * 1rem, ((5.5 - ((10 - 5.5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((10 - 5.5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 10 * 1rem);
--sizes--1-375rem: clamp(1.25 * 1rem, ((1.25 - ((1.375 - 1.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.375 - 1.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.375 * 1rem);
--_spacing---section-space--x-large: clamp(6 * 1rem, ((6 - ((11.25 - 6) / (90 - 20) * 20)) * 1rem + ((11.25 - 6) / (90 - 20)) * 100vw), 11.25 * 1rem);
--_typography---letter-spacing--0-03em: -.03em;
--_typography---letter-spacing--0em: 0em;
--_typography---font-size--text-small: clamp(1 * 1rem, ((1 - ((1 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1 - 1) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1 * 1rem);
--_typography---font-size--text-large: clamp(1.25 * 1rem, ((1.25 - ((1.5 - 1.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((1.5 - 1.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 1.5 * 1rem);
--_typography---font-size--h6: clamp(1.5 * 1rem, ((1.5 - ((2.125 - 1.5) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((2.125 - 1.5) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 2.125 * 1rem);
--_typography---font-size--h5: clamp(3 * 1rem, ((3 - ((5.25 - 3) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((5.25 - 3) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 5.25 * 1rem);
--_typography---font-size--h4: clamp(2 * 1rem, ((2 - ((3.75 - 2) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((3.75 - 2) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 3.75 * 1rem);
--_typography---font-size--h3: clamp(2.25 * 1rem, ((2.25 - ((3.375 - 2.25) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((3.375 - 2.25) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 3.375 * 1rem);
--_typography---font-size--h2: clamp(3.375 * 1rem, ((3.375 - ((7.75 - 3.375) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((7.75 - 3.375) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 7.75 * 1rem);
--_typography---font-size--h1: clamp(6 * 1rem, ((6 - ((10 - 6) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((10 - 6) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 10 * 1rem);
--_typography---font-size--display: clamp(10 * 1rem, ((10 - ((19.375 - 10) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((19.375 - 10) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 19.375 * 1rem);
--sizes--8-5rem: clamp(4.75 * 1rem, ((4.75 - ((8.5 - 4.75) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((8.5 - 4.75) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 8.5 * 1rem);
--sizes--12rem: clamp(6 * 1rem, ((6 - ((12 - 6) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((12 - 6) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 12 * 1rem);
--sizes--15rem: clamp(6.75 * 1rem, ((6.75 - ((15 - 6.75) / (var(--site--viewport-max)  - var(--site--viewport-min)) * var(--site--viewport-min))) * 1rem + ((15 - 6.75) / (var(--site--viewport-max)  - var(--site--viewport-min))) * 100vw), 15 * 1rem);
--column-margin--1: calc(var(--column-width--plus-gutter) * 1);
--column-margin--2: calc(var(--column-width--plus-gutter) * 2);
--column-margin--3: calc(var(--column-width--plus-gutter) * 3);
--column-margin--4: calc(var(--column-width--plus-gutter) * 4);
--column-margin--5: calc(var(--column-width--plus-gutter) * 5);
--column-margin--6: calc(var(--column-width--plus-gutter) * 6);
--column-margin--7: calc(var(--column-width--plus-gutter) * 7);
--column-margin--8: calc(var(--column-width--plus-gutter) * 8);
--column-margin--9: calc(var(--column-width--plus-gutter) * 9);
--column-margin--10: calc(var(--column-width--plus-gutter) * 10);
--column-margin--11: calc(var(--column-width--plus-gutter) * 11);
--column-margin--12: calc(var(--column-width--plus-gutter) * 12);
--swiper-navigation-size: 44px;
```

### Typography

```css
--_text-style---font-family: var(--_typography---font--primary-family);
--_theme---text: var(--swatch--charcoal);
--_text-style---line-height: var(--_typography---line-height--1-4);
--_text-style---font-weight: var(--_typography---font--primary-regular);
--_text-style---text-wrap: pretty;
--_typography---line-height--1: 1;
--_button-style---text: var(--_theme---button-primary--text);
--_button-style---text-hover: var(--_theme---button-primary--text-hover);
--_theme---text-link--text: var(--_theme---text);
--_theme---text-link--text-hover: var(--_theme---text-link--text);
--_typography---line-height--1-2: 1.2;
--_typography---line-height--1-1: 1.1;
--_typography---line-height--1-3: 1.3;
--swatch--brand-text: var(--swatch--charcoal);
--_text-style---text-transform: var(--_typography---text-transform--none);
--_text-style---trim-top: var(--_typography---font--primary-trim-top);
--_text-style---trim-bottom: var(--_typography---font--primary-trim-bottom);
--_theme---selection--text: var(--swatch--brand-text);
--swatch--brand-text-o20: color-mix(in srgb, var(--swatch--brand-text) 20%, transparent);
--_typography---line-height--0-9: .9;
--_typography---line-height--1-4: 1.4;
--_typography---line-height--1-5: 1.5;
--_typography---text-transform--none: var(--text-transform, none);
--_typography---text-transform--uppercase: uppercase;
--_typography---text-transform--capitalize: capitalize;
--_typography---text-transform--lowercase: lowercase;
```

### Radii

```css
--radius--small: .5rem;
--radius--main: 1rem;
--radius--round: 100vw;
--radius--x-small: .3125rem;
--radius--xx-small: .1875rem;
```

### Other

```css
--_theme---background: var(--swatch--hark-white);
--_column-count---value: 1;
--max-width--main: calc(var(--site--viewport-max) * 1rem);
--max-width--small: 50rem;
--max-width--full: 100%;
--site--gutter: var(--sizes--0-625rem);
--_theme---background-2: var(--swatch--gray);
--swatch--transparent: transparent;
--_button-style---background: var(--_theme---button-primary--background);
--_button-style---background-hover: var(--_theme---button-primary--background-hover);
--swatch--gray-2: #d4d4d4;
--swatch--black: black;
--swatch--brand-inkwell: #062541;
--swatch--gray: #f3f3f3;
--swatch--hark-white: white;
--swatch--light-100-o20: color-mix(in srgb, var(--swatch--hark-white) 20%, transparent);
--swatch--brand-cerulean: #114167;
--swatch--brand-cobalt: #235e80;
--swatch--brand-laguna: #00f2e5;
--swatch--gray-3: #d4d4d480;
--swatch--brand-cobalt-10: #235e8066;
--swatch--brand-cobalt-50: #235e8080;
--swatch--charcoal: #181818;
--swatch--pewter: #919598;
--swatch--charcoal-light: #232323;
--swatch--dark-900-o20: color-mix(in srgb, var(--swatch--charcoal) 20%, transparent);
--swatch--brand-600: color-mix(in srgb, var(--swatch--brand-cobalt), black 20%);
--site--viewport-max: 150;
--site--viewport-min: 20;
--_theme---selection--background: var(--swatch--brand-300);
--site--column-count: 12;
--focus--width: .125rem;
--focus--offset-inner: -.125rem;
--focus--offset-outer: .1875rem;
--swatch--brand-400: color-mix(in srgb, var(--swatch--brand-cobalt), white 20%);
--swatch--brand-300: color-mix(in srgb, var(--swatch--brand-cobalt), white 40%);
--_alignment---direction: start;
--swatch--brand-cobalt-5: #235e800d;
--site--column-width: calc((min(var(--max-width--main), 100% - var(--site--margin) * 2)  - (var(--site--gutter) * (var(--site--column-count)  - 1))) / var(--site--column-count));
--transition-smooth: all 400ms ease-out;
--grid-breakout: [full-start] minmax(0, 1fr) [content-start] repeat(var(--site--column-count), minmax(0, var(--site--column-width))) [content-end] minmax(0, 1fr) [full-end];
--grid-breakout-single: [full-start] minmax(0, 1fr) [content-start] minmax(0, calc(100% - var(--site--margin) * 2)) [content-end] minmax(0, 1fr) [full-end];
--site--gutter-total: calc(var(--site--gutter) * (var(--site--column-count) - 1));
--column-width--1: calc((var(--container--main) - var(--site--gutter-total)) / var(--site--column-count));
--column-width--plus-gutter: calc(var(--column-width--1) + var(--site--gutter));
--column-width--2: calc(var(--column-width--plus-gutter) * 2 - var(--site--gutter));
--column-width--3: calc(var(--column-width--plus-gutter) * 3 - var(--site--gutter));
--column-width--4: calc(var(--column-width--plus-gutter) * 4 - var(--site--gutter));
--column-width--5: calc(var(--column-width--plus-gutter) * 5 - var(--site--gutter));
--column-width--6: calc(var(--column-width--plus-gutter) * 6 - var(--site--gutter));
--column-width--7: calc(var(--column-width--plus-gutter) * 7 - var(--site--gutter));
--column-width--8: calc(var(--column-width--plus-gutter) * 8 - var(--site--gutter));
--column-width--9: calc(var(--column-width--plus-gutter) * 9 - var(--site--gutter));
--column-width--10: calc(var(--column-width--plus-gutter) * 10 - var(--site--gutter));
--column-width--11: calc(var(--column-width--plus-gutter) * 11 - var(--site--gutter));
--column-width--12: calc(var(--column-width--plus-gutter) * 12 - var(--site--gutter));
```

### Dependencies

```css
--_theme---background: --swatch--hark-white;
--_text-style---font-family: --_typography---font--primary-family;
--_theme---text: --swatch--charcoal;
--_text-style---font-size: --_typography---font-size--text-main;
--_text-style---line-height: --_typography---line-height--1-4;
--_text-style---font-weight: --_typography---font--primary-regular;
--_text-style---letter-spacing: --_typography---letter-spacing--0em;
--sizes--1-125rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_gap---size: --site--gutter;
--sizes--1rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_text-style---margin-top: --_spacing---space--4;
--_text-style---margin-bottom: --_spacing---space--4;
--_spacing---space--6: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---space--7: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--max-width--main: --site--viewport-max;
--site--margin: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---section-space--small: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---section-space--main: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---section-space--large: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---section-space--page-top: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_theme---heading-accent: --swatch--brand-600;
--_spacing---space--2: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--site--gutter: --sizes--0-625rem;
--_theme---background-2: --swatch--gray;
--_spacing---space--1: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---space--3: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---space--4: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---space--5: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---space--8: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_theme---border: --swatch--dark-900-o20;
--_button-style---border: --_theme---button-primary--border;
--_button-style---background: --_theme---button-primary--background;
--_button-style---text: --_theme---button-primary--text;
--_button-style---border-hover: --_theme---button-primary--border-hover;
--_button-style---background-hover: --_theme---button-primary--background-hover;
--_button-style---text-hover: --_theme---button-primary--text-hover;
--_theme---text-link--border: --_theme---border;
--_theme---text-link--text: --_theme---text;
--_theme---text-link--border-hover: --_theme---text;
--_theme---text-link--text-hover: --_theme---text-link--text;
--_typography---font-size--text-fine: --sizes--0-875rem;
--_typography---font-size--text-cat: --sizes--0-75rem;
--_typography---font-size--text-graphic-2: --sizes--6-5rem;
--_typography---font-size--text-graphic-title: --sizes--4rem;
--_typography---font-size--text-accent: --sizes--2-5rem;
--sizes--1-25rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--1-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--13rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--3rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--3-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--16rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--swatch--light-100-o20: --swatch--hark-white;
--_theme---button-primary--text-hover: --_theme---background;
--sizes--1-75rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--2-25rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--7-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--14rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--3-75rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--1-875rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--2-75rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--text-main: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--2rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--swatch--brand-text: --swatch--charcoal;
--sizes--4rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--2-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--4-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--1-625rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--11rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--9-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--6rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--7rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--6-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--8rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--5-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--3-25rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--9rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_text-style---text-transform: --_typography---text-transform--none;
--sizes--10rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--swatch--dark-900-o20: --swatch--charcoal;
--sizes--1-375rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--swatch--brand-600: --swatch--brand-cobalt;
--_text-style---trim-top: --_typography---font--primary-trim-top;
--_text-style---trim-bottom: --_typography---font--primary-trim-bottom;
--_theme---selection--background: --swatch--brand-300;
--_theme---selection--text: --swatch--brand-text;
--swatch--brand-text-o20: --swatch--brand-text;
--swatch--brand-400: --swatch--brand-cobalt;
--swatch--brand-300: --swatch--brand-cobalt;
--_theme---button-primary--background: --swatch--brand-cobalt;
--_theme---button-primary--border: --_theme---button-primary--background;
--_theme---button-primary--text: --swatch--brand-text;
--_theme---button-primary--background-hover: --_theme---text;
--_theme---button-primary--border-hover: --_theme---button-primary--background-hover;
--_theme---button-secondary--background: --swatch--transparent;
--_theme---button-secondary--border: --_theme---border;
--_theme---button-secondary--text: --_theme---text;
--_theme---button-secondary--background-hover: --_theme---text;
--_theme---button-secondary--border-hover: --_theme---button-secondary--background-hover;
--_theme---button-secondary--text-hover: --_theme---background;
--_typography---font-size--text-small: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--text-large: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h6: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h5: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h4: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h3: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h2: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h1: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--display: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--site--column-width: --max-width--main,--site--margin,--site--gutter,--site--column-count,--site--column-count;
--_typography---text-transform--none: --text-transform;
--sizes--8-5rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--12rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--sizes--15rem: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--grid-breakout: --site--column-count,--site--column-width;
--grid-breakout-single: --site--margin;
--site--gutter-total: --site--gutter,--site--column-count;
--column-width--1: --container--main,--site--gutter-total,--site--column-count;
--column-width--plus-gutter: --column-width--1,--site--gutter;
--column-width--2: --column-width--plus-gutter,--site--gutter;
--column-width--3: --column-width--plus-gutter,--site--gutter;
--column-width--4: --column-width--plus-gutter,--site--gutter;
--column-width--5: --column-width--plus-gutter,--site--gutter;
--column-width--6: --column-width--plus-gutter,--site--gutter;
--column-width--7: --column-width--plus-gutter,--site--gutter;
--column-width--8: --column-width--plus-gutter,--site--gutter;
--column-width--9: --column-width--plus-gutter,--site--gutter;
--column-width--10: --column-width--plus-gutter,--site--gutter;
--column-width--11: --column-width--plus-gutter,--site--gutter;
--column-width--12: --column-width--plus-gutter,--site--gutter;
--column-margin--1: --column-width--plus-gutter;
--column-margin--2: --column-width--plus-gutter;
--column-margin--3: --column-width--plus-gutter;
--column-margin--4: --column-width--plus-gutter;
--column-margin--5: --column-width--plus-gutter;
--column-margin--6: --column-width--plus-gutter;
--column-margin--7: --column-width--plus-gutter;
--column-margin--8: --column-width--plus-gutter;
--column-margin--9: --column-width--plus-gutter;
--column-margin--10: --column-width--plus-gutter;
--column-margin--11: --column-width--plus-gutter;
--column-margin--12: --column-width--plus-gutter;
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
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 991px | max-width |
| lg | 992px | min-width |
| lg | 1024px | max-width |
| lg | 1025px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.001s`, `0.4s`, `0.2s`, `0.3s`

### Common Transitions

```css
transition: overflow 0.001s allow-discrete;
transition: all;
transition: 0.4s ease-out;
transition: 0.2s ease-out;
transition: 0.3s ease-out;
transition: opacity 0.2s ease-out;
transition: opacity 0.3s;
transition: transform 0.3s ease-out;
transition: opacity 0.3s ease-out;
transition: transform;
```

### Keyframe Animations

**spin**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**move-out**
```css
@keyframes move-out {
  0% { opacity: 1; }
  100% { opacity: 0.4; }
}
```

**move-in**
```css
@keyframes move-in {
  0% { clip-path: polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%); }
  100% { clip-path: polygon(0% 100%, 100% 100%, 100% 0%, 0% 0%); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (16 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(6, 37, 65);
  font-size: 17.8462px;
  font-weight: 400;
  padding-top: 16px;
  padding-right: 16px;
  border-radius: 3px;
}
```

### Cards (40 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (62 instances)

```css
.link {
  color: rgb(6, 37, 65);
  font-size: 17.8462px;
  font-weight: 400;
}
```

### Navigation (67 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(24, 24, 24);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (54 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(145, 149, 152);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 17.8462px;
}
```

### Modals (144 instances)

```css
.modal {
  background-color: rgb(243, 243, 243);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (51 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(255, 255, 255);
  padding-top: 0px;
}
```

### Badges (20 instances)

```css
.badge {
  background-color: rgba(212, 212, 212, 0.5);
  color: rgb(24, 24, 24);
  font-size: 17.8462px;
  font-weight: 400;
  padding-top: 6px;
  padding-right: 16px;
  border-radius: 3px;
}
```

### Switches (7 instances)

```css
.switche {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  border-color: rgb(24, 24, 24);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(24, 24, 24);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(24, 24, 24);
  font-size: 17.8462px;
  font-weight: 400;
```

### Card — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 16px 27.8462px 58px 27.8462px;
  border-radius: 5px;
  border: 1px solid color(srgb 1 1 1 / 0.2);
  font-size: 17.8462px;
  font-weight: 400;
```

### Card — 8 instances, 1 variant

**Variant 1** (8 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 53.2308px;
  font-weight: 400;
```

## Layout System

**11 grid containers** and **426 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 2400px | 0px |
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 12-column | 10x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 89.2812px 89.2812px 89.2812px 89.2812px 89.2812px 89.2812px 89.2812px 89.2812px 89.2812px 89.2812px 89.2812px 89.2812px;
gap: 10px;
grid-template-columns: 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.7656px;
gap: 10px;
grid-template-columns: 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.7656px 93.75px 93.75px 93.75px;
gap: 10px;
grid-template-columns: 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.7656px 93.75px 93.75px 93.75px;
gap: 10px;
grid-template-columns: 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.75px 93.7656px 93.75px 93.75px 93.75px;
gap: 10px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 204x |
| row/wrap | 3x |
| row/nowrap | 219x |

**Gap values:** `10px`, `12px`, `130.769px`, `14px`, `16.4923px`, `16px`, `18.9231px`, `195.692px`, `21.8462px`, `23.4154px`, `25.8462px`, `27.8462px`, `29.8462px`, `29.8462px normal`, `35.6923px`, `41.5385px`, `47.3846px`, `4px`, `50.3077px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 92/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 88 !important rules — prefer specificity over overrides
- 78% of CSS is unused — consider purging
- 5469 duplicate CSS declarations

## Z-Index Map

**12 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2000,2000 | div.g.u.i.d.e._.w.r.a.p |
| dropdown | 100,200 | nav.n.a.v._.c.o.m.p.o.n.e.n.t, div.c.l.o.s.e._.t.e.x.t. .u.-.t.e.x.t.-.s.t.y.l.e.-.s.m.a.l.l, div.m.i.c.r.o.-.t.o.p |
| sticky | 50,50 | div.t.r.a.n.s.-.i.t.e.m._.i.n.f.o._.c.o.n.t.a.i.n, div.t.r.a.n.s.-.i.t.e.m._.i.n.f.o._.c.o.n.t.a.i.n, div.t.r.a.n.s.-.i.t.e.m._.i.n.f.o._.c.o.n.t.a.i.n |
| base | -1000,6 | span.s.w.i.p.e.r.-.n.o.t.i.f.i.c.a.t.i.o.n, video, div.v.i.d.-.f.i.l.l._.h.e.r.o. .w.-.b.a.c.k.g.r.o.u.n.d.-.v.i.d.e.o. .w.-.b.a.c.k.g.r.o.u.n.d.-.v.i.d.e.o.-.a.t.o.m |

## SVG Icons

**8 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 5 |
| md | 1 |
| xl | 2 |

**Icon colors:** `currentColor`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | normal | normal |
| Aeonikpro | self-hosted | 400, 500 | normal |
| Suisseworks Webs | self-hosted | 400 | normal |
| Suisseworks Webxl | self-hosted | 400 | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 6 | objectFit: cover, borderRadius: 5px, shape: rounded |
| hero | 2 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 1 | objectFit: contain, borderRadius: 0px, shape: square |

**Aspect ratios:** 3:4 (6x), 3:2 (2x), 3.29:1 (1x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `1ms` | 1 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |

### Easing Families

- **ease-in-out** (186 uses) — `ease`

## Component Anatomy

### card — 16 instances

**Slots:** description

## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** unknown (tight)

### Top CTA Verbs

- **our** (1)

### Button Copy Patterns

- "our story
our solutions" (1×)

## Page Intent

**Type:** `landing` (confidence 0.61)
**Description:** We specialize in non-dilutive NAV loans and GP financings to financial sponsors. Dedicated NAV-based loan provider.

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → hero → content → content → stats → testimonial → content → pricing-table → content → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | hero | — | 0.85 |
| 2 | content | — | 0.3 |
| 3 | content | — | 0.3 |
| 4 | stats | — | 0.85 |
| 5 | testimonial | — | 0.8 |
| 6 | content | — | 0.3 |
| 7 | pricing-table | — | 0.9 |
| 8 | content | — | 0.3 |
| 9 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.32 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 1280px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.574)
**Counts:** total 9, svg 0, icon 0, screenshot-like 0, photo-like 8
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Aeonikpro` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
