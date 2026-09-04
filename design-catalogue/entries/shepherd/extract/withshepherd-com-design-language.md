# Design Language: Shepherd

> Extracted from `https://www.withshepherd.com/` on September 4, 2026
> 864 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#fdc331` | rgb(253, 195, 49) | hsl(43, 98%, 59%) | 9 |
| Secondary | `#d6c5b5` | rgb(214, 197, 181) | hsl(29, 29%, 77%) | 2 |
| Accent | `#fa9742` | rgb(250, 151, 66) | hsl(28, 95%, 62%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 1503 |
| `#ffffff` | hsl(0, 0%, 100%) | 125 |
| `#e7e7e7` | hsl(0, 0%, 91%) | 5 |

### Background Colors

Used on large-area elements: `#ffffff`, `#fdc331`, `#d6c5b5`, `#000000`, `#fa9742`, `#e7e7e7`

### Text Colors

Text color palette: `#000000`, `#ffffff`, `#f6c449`

### Gradients

```css
background-image: linear-gradient(90deg, rgb(253, 195, 49) 53%, rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(-90deg, rgb(253, 195, 49), rgba(0, 0, 0, 0));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 1503 |
| `#ffffff` | background, text, border | 125 |
| `#fdc331` | background | 9 |
| `#e7e7e7` | background | 5 |
| `#f6c449` | text, border | 2 |
| `#d6c5b5` | background | 2 |
| `#fa9742` | background | 1 |

## Typography

### Font Families

- **Magistersttrial** — used for all (745 elements)
- **Gt Planar Trial** — used for all (73 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 100px | 6.25rem | 500 | 100px | -3px | div, span |
| 85px | 5.3125rem | 500 | 85px | -4.25px | h1, em, span, br |
| 45px | 2.8125rem | 500 | 45px | -2.25px | h1, h2, h5 |
| 24px | 1.5rem | 400 | 26.4px | -0.714px | div |
| 23.8px | 1.4875rem | 400 | 26.18px | -0.714px | body, div, script, style |
| 18.4px | 1.15rem | 400 | 20.24px | 0.552px | div |
| 16px | 1rem | 400 | normal | normal | html, head, meta, link |
| 15.5px | 0.9688rem | 400 | 17.05px | 0.775px | div, br, h3 |

### Heading Scale

```css
h1 { font-size: 85px; font-weight: 500; line-height: 85px; }
h1 { font-size: 45px; font-weight: 500; line-height: 45px; }
h3 { font-size: 15.5px; font-weight: 400; line-height: 17.05px; }
```

### Body Text

```css
body { font-size: 23.8px; font-weight: 400; line-height: 26.18px; }
```

### Font Weights in Use

`400` (837x), `500` (23x), `700` (4x)

## Spacing

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-40 | 40px | 2.5rem |
| spacing-53 | 53px | 3.3125rem |
| spacing-58 | 58px | 3.625rem |
| spacing-69 | 69px | 4.3125rem |
| spacing-79 | 79px | 4.9375rem |
| spacing-84 | 84px | 5.25rem |
| spacing-92 | 92px | 5.75rem |
| spacing-115 | 115px | 7.1875rem |
| spacing-126 | 126px | 7.875rem |
| spacing-208 | 208px | 13rem |
| spacing-409 | 409px | 25.5625rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 8px | 1 |

## CSS Custom Properties

### Colors

```css
--border-width--main: 1px;
--_theme---heading-accent: var(--swatch--brand);
--_typography---font--primary-family: Magistersttrial,"Times New Roman",sans-serif;
--_typography---font--primary-regular: 400;
--_typography---font--primary-medium: 500;
--_typography---font--primary-bold: 700;
--_theme---border: color-mix(in srgb,var(--_theme---text)50%,transparent);
--_button-style---border: var(--_theme---button-primary--border);
--_button-style---border-hover: var(--_theme---button-primary--border-hover);
--_theme---text-link--border: var(--_theme---border);
--_theme---text-link--border-hover: var(--_theme---text);
--_typography---font--secondary-family: "Gt Planar Trial",Arial,sans-serif;
--_theme---button-primary--background: var(--_theme---text);
--_theme---button-primary--border: var(--_theme---text);
--_theme---button-primary--text: var(--_theme---background);
--_theme---button-primary--background-hover: var(--_theme---background);
--_theme---button-primary--border-hover: var(--_theme---border);
--_theme---button-primary--text-hover: var(--_theme---text);
--_theme---button-secondary--background: var(--swatch--transparent);
--_theme---button-secondary--border: var(--_theme---border);
--_theme---button-secondary--text: var(--_theme---text);
--_theme---button-secondary--background-hover: var(--_theme---text);
--_theme---button-secondary--border-hover: var(--_theme---button-secondary--background-hover);
--_theme---button-secondary--text-hover: var(--_theme---background);
--_typography---font--primary-trim-top: .33em;
--_typography---font--primary-trim-bottom: .38em;
--mantine-color-red-9: #c92a2a;
--mantine-color-dark-9: #141414;
--mantine-color-lime-1: #e9fac8;
--mantine-color-dark-5: #3b3b3b;
--mantine-color-violet-0: #f3f0ff;
--mantine-color-red-8: #e03131;
--mantine-color-pink-light: #ffdeeb;
--mantine-color-violet-filled: #7950f2;
--mantine-color-indigo-4: #748ffc;
--mantine-color-indigo-6: #4c6ef5;
--mantine-color-cyan-light-color: #0b7285;
--mantine-color-pink-3: #faa2c1;
--mantine-color-blue-7: #1c7ed6;
--mantine-color-teal-2: #96f2d7;
--mantine-color-green-6: #40c057;
--mantine-color-grape-0: #f8f0fc;
--mantine-color-green-filled: #40c057;
--mantine-color-anchor: #fab005;
--mantine-color-red-2: #ffc9c9;
--mantine-primary-color-light-hover: #ffec99;
--mantine-primary-color-1: #fff3bf;
--mantine-color-yellow-6: #fab005;
--mantine-color-gray-filled-hover: #495057;
--mantine-color-red-1: #ffe3e3;
--mantine-color-orange-9: #d9480f;
--mantine-color-lime-0: #f4fce3;
--mantine-color-lime-6: #82c91e;
--mantine-color-violet-light-hover: #d0bfff;
--mantine-color-yellow-filled: #fab005;
--mantine-color-indigo-1: #dbe4ff;
--mantine-color-pink-6: #e64980;
--mantine-color-dark-filled: #2e2e2e;
--mantine-color-gray-0: #f8f9fa;
--mantine-color-red-text: #fa5252;
--mantine-color-blue-5: #339af0;
--mantine-color-grape-6: #be4bdb;
--mantine-color-yellow-0: #fff9db;
--mantine-color-pink-5: #f06595;
--mantine-color-orange-1: #ffe8cc;
--mantine-color-dark-filled-hover: #242424;
--mantine-color-blue-3: #74c0fc;
--mantine-color-cyan-outline: #15aabf;
--mantine-color-cyan-7: #1098ad;
--mantine-color-indigo-filled-hover: #4263eb;
--mantine-color-violet-9: #5f3dc4;
--mantine-color-pink-outline-hover: rgba(230,73,128,0.05);
--mantine-color-teal-light-color: #087f5b;
--mantine-color-orange-outline: #fd7e14;
--mantine-color-red-filled: #fa5252;
--mantine-color-cyan-0: #e3fafc;
--mantine-color-orange-filled-hover: #f76707;
--mantine-color-pink-1: #ffdeeb;
--mantine-color-lime-5: #94d82d;
--mantine-color-orange-light: #ffe8cc;
--mantine-color-orange-light-color: #d9480f;
--mantine-primary-color-7: #f59f00;
--mantine-color-dark-1: #b8b8b8;
--mantine-color-dark-light-hover: #828282;
--mantine-color-cyan-filled: #15aabf;
--mantine-color-indigo-8: #3b5bdb;
--mantine-color-violet-3: #b197fc;
--mantine-color-orange-2: #ffd8a8;
--mantine-color-cyan-6: #15aabf;
--mantine-color-default-border: #ced4da;
--mantine-color-lime-9: #5c940d;
--mantine-color-orange-8: #e8590c;
--mantine-color-yellow-light-hover: #ffec99;
--mantine-primary-color-6: #fab005;
--mantine-color-lime-3: #c0eb75;
--mantine-color-orange-5: #ff922b;
--mantine-color-lime-light-color: #5c940d;
--mantine-color-error: #fa5252;
--mantine-color-green-8: #2f9e44;
--mantine-primary-color-filled-hover: #f59f00;
--mantine-color-indigo-9: #364fc7;
--mantine-color-grape-2: #eebefa;
--mantine-primary-color-contrast: #fff;
--mantine-color-dimmed: #868e96;
--mantine-color-gray-light-hover: #e9ecef;
--mantine-color-red-4: #ff8787;
--mantine-color-yellow-4: #ffd43b;
--mantine-color-lime-4: #a9e34b;
--mantine-primary-color-light-color: #e67700;
--mantine-color-green-4: #69db7c;
--mantine-color-lime-outline-hover: rgba(130,201,30,0.05);
--mantine-color-teal-light: #c3fae8;
--mantine-color-green-0: #ebfbee;
--mantine-color-dark-6: #2e2e2e;
--mantine-color-lime-7: #74b816;
--mantine-color-blue-filled: #228be6;
--mantine-color-indigo-3: #91a7ff;
--mantine-color-gray-3: #dee2e6;
--mantine-color-red-light-color: #c92a2a;
--mantine-color-yellow-light: #fff3bf;
--mantine-color-pink-2: #fcc2d7;
--mantine-color-gray-9: #212529;
--mantine-color-teal-outline: #12b886;
--mantine-color-green-7: #37b24d;
--mantine-color-indigo-light-color: #364fc7;
--mantine-color-lime-filled-hover: #74b816;
--mantine-color-blue-outline-hover: rgba(34,139,230,0.05);
--mantine-color-cyan-outline-hover: rgba(21,170,191,0.05);
--mantine-color-disabled: #e9ecef;
--mantine-color-gray-8: #343a40;
--mantine-color-green-text: #40c057;
--mantine-color-indigo-text: #4c6ef5;
--mantine-color-green-light-color: #2b8a3e;
--mantine-color-dark-text: #2e2e2e;
--mantine-color-pink-filled: #e64980;
--mantine-primary-color-9: #e67700;
--mantine-color-blue-9: #1864ab;
--mantine-color-red-filled-hover: #f03e3e;
--mantine-color-cyan-filled-hover: #1098ad;
--mantine-color-lime-filled: #82c91e;
--mantine-color-indigo-5: #5c7cfa;
--mantine-color-red-outline: #fa5252;
--mantine-color-grape-text: #be4bdb;
--mantine-color-orange-outline-hover: rgba(253,126,20,0.05);
--mantine-color-violet-light: #e5dbff;
--mantine-color-violet-4: #9775fa;
--mantine-color-white: #fff;
--mantine-color-blue-6: #228be6;
--mantine-color-teal-light-hover: #96f2d7;
--mantine-color-green-1: #d3f9d8;
--mantine-color-teal-8: #099268;
--mantine-color-indigo-outline-hover: rgba(76,110,245,0.05);
--mantine-color-yellow-8: #f08c00;
--mantine-color-cyan-3: #66d9e8;
--mantine-color-grape-light: #f3d9fa;
--mantine-color-violet-light-color: #5f3dc4;
--mantine-color-yellow-2: #ffec99;
--mantine-color-cyan-1: #c5f6fa;
--mantine-color-green-outline-hover: rgba(64,192,87,0.05);
--mantine-color-cyan-4: #3bc9db;
--mantine-color-violet-8: #6741d9;
--mantine-color-violet-2: #d0bfff;
--mantine-color-lime-2: #d8f5a2;
--mantine-color-default: #fff;
--mantine-primary-color-8: #f08c00;
--mantine-color-grape-outline: #be4bdb;
--mantine-color-cyan-text: #15aabf;
--mantine-color-violet-filled-hover: #7048e8;
--mantine-color-orange-6: #fd7e14;
--mantine-primary-color-0: #fff9db;
--mantine-color-gray-outline-hover: rgba(134,142,150,0.05);
--mantine-color-indigo-7: #4263eb;
--mantine-color-dark-8: #1f1f1f;
--mantine-color-pink-9: #a61e4d;
--mantine-color-grape-outline-hover: rgba(190,75,219,0.05);
--mantine-color-cyan-2: #99e9f2;
--mantine-color-disabled-color: #adb5bd;
--mantine-color-body: #fff;
--mantine-color-violet-1: #e5dbff;
--mantine-color-orange-light-hover: #ffd8a8;
--mantine-color-grape-9: #862e9c;
--mantine-color-gray-outline: #868e96;
--mantine-color-yellow-light-color: #e67700;
--mantine-color-gray-2: #e9ecef;
--mantine-color-text: #000;
--mantine-color-violet-text: #7950f2;
--mantine-color-yellow-outline: #fab005;
--mantine-color-green-outline: #40c057;
--mantine-color-green-light-hover: #b2f2bb;
--mantine-color-violet-6: #7950f2;
--mantine-color-pink-8: #c2255c;
--mantine-color-orange-filled: #fd7e14;
--mantine-color-teal-1: #c3fae8;
--mantine-color-lime-8: #66a80f;
--mantine-color-dark-2: #828282;
--mantine-color-cyan-9: #0b7285;
--mantine-color-orange-0: #fff4e6;
--mantine-color-blue-1: #d0ebff;
--mantine-color-cyan-light-hover: #99e9f2;
--mantine-color-green-3: #8ce99a;
--mantine-color-lime-light: #e9fac8;
--mantine-color-lime-light-hover: #d8f5a2;
--mantine-color-teal-filled: #12b886;
--mantine-z-index-popover: 300;
--mantine-color-gray-6: #868e96;
--mantine-color-yellow-5: #fcc419;
--mantine-color-yellow-9: #e67700;
--mantine-color-success: #099268;
--mantine-color-violet-5: #845ef7;
--mantine-color-gray-filled: #868e96;
--mantine-color-violet-7: #7048e8;
--mantine-color-dark-0: #c9c9c9;
--mantine-color-pink-filled-hover: #d6336c;
--mantine-color-scheme: light;
--mantine-color-grape-filled: #be4bdb;
--mantine-color-blue-2: #a5d8ff;
--mantine-color-red-light: #ffe3e3;
--mantine-color-yellow-7: #f59f00;
--mantine-color-pink-light-hover: #fcc2d7;
--mantine-color-cyan-light: #c5f6fa;
--mantine-color-yellow-3: #ffe066;
--mantine-color-gray-light-color: #212529;
--mantine-color-green-filled-hover: #37b24d;
--mantine-color-teal-outline-hover: rgba(18,184,134,0.05);
--mantine-color-red-light-hover: #ffc9c9;
--mantine-color-grape-8: #9c36b5;
--mantine-primary-color-2: #ffec99;
--mantine-color-disabled-border: #dee2e6;
--mantine-color-grape-1: #f3d9fa;
--mantine-color-grape-7: #ae3ec9;
--mantine-color-blue-text: #228be6;
--mantine-color-violet-outline-hover: rgba(121,80,242,0.05);
--mantine-color-teal-5: #20c997;
--mantine-color-cyan-5: #22b8cf;
--mantine-color-gray-text: #868e96;
--mantine-color-gray-4: #ced4da;
--mantine-color-blue-0: #e7f5ff;
--mantine-color-teal-3: #63e6be;
--mantine-primary-color-5: #fcc419;
--mantine-color-red-5: #ff6b6b;
--mantine-color-dark-outline: #2e2e2e;
--mantine-color-teal-6: #12b886;
--mantine-color-indigo-filled: #4c6ef5;
--mantine-color-teal-4: #38d9a9;
--mantine-color-red-6: #fa5252;
--mantine-color-grape-light-color: #862e9c;
--mantine-color-indigo-outline: #4c6ef5;
--mantine-color-cyan-8: #0c8599;
--mantine-color-indigo-0: #edf2ff;
--mantine-color-orange-3: #ffc078;
--mantine-color-red-0: #fff5f5;
--mantine-color-green-light: #d3f9d8;
--mantine-color-default-hover: #f8f9fa;
--mantine-color-grape-4: #da77f2;
--mantine-color-lime-outline: #82c91e;
--mantine-color-grape-filled-hover: #ae3ec9;
--mantine-color-blue-light: #d0ebff;
--mantine-color-blue-light-hover: #a5d8ff;
--mantine-color-placeholder: #adb5bd;
--mantine-color-dark-light-color: #141414;
--mantine-color-yellow-text: #fab005;
--mantine-color-bright: #000;
--mantine-color-black: #000;
--mantine-primary-color-4: #ffd43b;
--mantine-primary-color-filled: #fab005;
--mantine-color-yellow-1: #fff3bf;
--mantine-color-blue-8: #1971c2;
--mantine-color-grape-3: #e599f7;
--mantine-color-dark-outline-hover: rgba(46,46,46,0.05);
--mantine-color-lime-text: #82c91e;
--mantine-color-green-2: #b2f2bb;
--mantine-color-indigo-light: #dbe4ff;
--mantine-color-orange-text: #fd7e14;
--mantine-color-blue-4: #4dabf7;
--mantine-color-grape-light-hover: #eebefa;
--mantine-color-teal-0: #e6fcf5;
--mantine-color-dark-light: #b8b8b8;
--mantine-color-dark-4: #424242;
--mantine-color-orange-4: #ffa94d;
--mantine-color-red-outline-hover: rgba(250,82,82,0.05);
--mantine-color-blue-light-color: #1864ab;
--mantine-color-dark-7: #242424;
--mantine-color-yellow-outline-hover: rgba(250,176,5,0.05);
--mantine-color-violet-outline: #7950f2;
--mantine-primary-color-light: #fff3bf;
--mantine-color-dark-3: #696969;
--mantine-color-pink-7: #d6336c;
--mantine-color-green-9: #2b8a3e;
--mantine-color-red-7: #f03e3e;
--mantine-color-pink-light-color: #a61e4d;
--mantine-color-teal-filled-hover: #0ca678;
--mantine-color-teal-9: #087f5b;
--mantine-color-pink-0: #fff0f6;
--mantine-color-grape-5: #cc5de8;
--mantine-color-gray-1: #f1f3f5;
--mantine-color-indigo-2: #bac8ff;
--mantine-color-pink-text: #e64980;
--mantine-color-green-5: #51cf66;
--mantine-color-gray-light: #f1f3f5;
--mantine-color-indigo-light-hover: #bac8ff;
--mantine-color-yellow-filled-hover: #f59f00;
--mantine-color-red-3: #ffa8a8;
--mantine-color-pink-4: #f783ac;
--mantine-color-blue-outline: #228be6;
--mantine-color-gray-7: #495057;
--mantine-color-pink-outline: #e64980;
--mantine-color-orange-7: #f76707;
--mantine-color-teal-7: #0ca678;
--mantine-color-gray-5: #adb5bd;
--mantine-color-teal-text: #12b886;
--mantine-primary-color-3: #ffe066;
--mantine-color-blue-filled-hover: #1c7ed6;
--mantine-color-default-color: #000;
```

### Spacing

```css
--_text-style---font-size: var(--_typography---font-size--text-main);
--_text-style---letter-spacing: -.03em;
--_gap---size: var(--site--gutter);
--_spacing---space--5: clamp(1.25*1rem,((1.25 - ((2.5 - 1.25)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((2.5 - 1.25)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),2.5*1rem);
--_spacing---space--3: clamp(.875*1rem,((.875 - ((1 - .875)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((1 - .875)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),1*1rem);
--_text-style---margin-bottom: var(--_spacing---space--4);
--_spacing---space--6: clamp(1.75*1rem,((1.75 - ((2.75 - 1.75)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((2.75 - 1.75)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),2.75*1rem);
--_spacing---space--2: clamp(.625*1rem,((.625 - ((.75 - .625)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((.75 - .625)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),.75*1rem);
--_spacing---section-space--none: 0px;
--_spacing---section-space--small: clamp(2*1rem,((2 - ((2 - 2)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((2 - 2)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),2*1rem);
--_spacing---section-space--main: clamp(3*1rem,((3 - ((4 - 3)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((4 - 3)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),4*1rem);
--_spacing---section-space--large: clamp(8*1rem,((8 - ((10 - 8)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((10 - 8)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),10*1rem);
--site--margin: clamp(1*1rem,((1 - ((1.5 - 1)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((1.5 - 1)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),1.5*1rem);
--_spacing---section-space--page-top: clamp(10*1rem,((10 - ((14 - 10)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((14 - 10)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),14*1rem);
--_spacing---space--8: clamp(3*1rem,((3 - ((6 - 3)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((6 - 3)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),6*1rem);
--_text-style---margin-top: var(--_spacing---space--4);
--_spacing---space--7: clamp(2.5*1rem,((2.5 - ((4 - 2.5)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((4 - 2.5)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),4*1rem);
--_typography---letter-spacing--tight: -.03em;
--_typography---letter-spacing--normal: 0em;
--_spacing---space--1: clamp(.375*1rem,((.375 - ((.5 - .375)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((.5 - .375)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),.5*1rem);
--_spacing---space--4: clamp(1.15*1rem,((1.15 - ((1.75 - 1.15)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((1.75 - 1.15)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),1.75*1rem);
--_typography---font-size--text-large: clamp(1*1rem,((1 - ((1.2 - 1)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((1.2 - 1)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),1.2*1rem);
--button-size--medium: 3rem;
--button-size--large: 5rem;
--nav--spacing-outer-horizontal: var(--site--margin);
--_typography---font-size--text-small: clamp(.875*1rem,((.875 - ((1 - .875)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((1 - .875)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),1*1rem);
--nav--spacing-outer-vertical: var(--site--margin);
--nav--hamburger-gap: var(--_spacing---space--2);
--_typography---font-size--h4: clamp(1.25*1rem,((1.25 - ((2.5 - 1.25)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((2.5 - 1.25)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),2.5*1rem);
--nav--spacing-inner-horizontal: var(--_spacing---space--5);
--_typography---font-size--text-main: clamp(1*1rem,((1 - ((1.65 - 1)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((1.65 - 1)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),1.65*1rem);
--_typography---font-size--h6: clamp(1*1rem,((1 - ((1.125 - 1)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((1.125 - 1)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),1.125*1rem);
--_typography---font-size--h5: clamp(1.25*1rem,((1.25 - ((1.5 - 1.25)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((1.5 - 1.25)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),1.5*1rem);
--_typography---font-size--h3: clamp(1.5*1rem,((1.5 - ((3.25 - 1.5)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((3.25 - 1.5)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),3.25*1rem);
--_typography---font-size--h2: clamp(2.5*1rem,((2.5 - ((5.25 - 2.5)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((5.25 - 2.5)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),5.25*1rem);
--_typography---font-size--h1: clamp(2.5*1rem,((2.5 - ((6.25 - 2.5)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((6.25 - 2.5)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),6.25*1rem);
--_typography---font-size--display: clamp(4*1rem,((4 - ((7 - 4)/(var(--site--viewport-max) - var(--site--viewport-min))*var(--site--viewport-min)))*1rem + ((7 - 4)/(var(--site--viewport-max) - var(--site--viewport-min)))*100vw),7*1rem);
--mantine-h1-font-size: calc(2.125rem * 1);
--mantine-h4-font-size: calc(1.125rem * 1);
--mantine-h2-font-size: calc(1.625rem * 1);
--mantine-spacing-sm: calc(0.75rem * 1);
--mantine-h6-font-size: calc(0.875rem * 1);
--mantine-spacing-xl: calc(2rem * 1);
--mantine-h3-font-size: calc(1.375rem * 1);
--mantine-font-size-sm: calc(0.875rem * 1);
--mantine-font-size-md: calc(1rem * 1);
--mantine-h5-font-size: calc(1rem * 1);
--mantine-spacing-lg: calc(1.25rem * 1);
--mantine-spacing-md: calc(1rem * 1);
--mantine-font-size-xl: calc(1.25rem * 1);
--mantine-font-size-lg: calc(1.125rem * 1);
--mantine-font-family-monospace: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;
--mantine-font-size-xs: calc(0.75rem * 1);
--mantine-spacing-xs: calc(0.625rem * 1);
```

### Typography

```css
--_text-style---font-family: var(--_typography---font--primary-family);
--_theme---text: var(--swatch--dark);
--_text-style---line-height: 1.1;
--_text-style---font-weight: var(--_typography---font--primary-regular);
--_text-style---text-wrap: pretty;
--_text-style---trim-top: var(--_typography---font--primary-trim-top);
--_text-style---trim-bottom: var(--_typography---font--primary-trim-bottom);
--_typography---line-height--small: 1;
--_typography---line-height--medium: 1.1;
--_typography---line-height--large: 1.3;
--_typography---line-height--huge: 1.5;
--_button-style---text: var(--_theme---button-primary--text);
--_button-style---text-hover: var(--_theme---button-primary--text-hover);
--_theme---text-link--text: var(--swatch--pink);
--_theme---text-link--text-hover: var(--_theme---text-link--text);
--_text-style---text-transform: var(--_typography---text-transform--none);
--_typography---text-transform--none: var(--text-transform,none);
--_typography---text-transform--uppercase: uppercase;
--_typography---text-transform--capitalize: capitalize;
--_typography---text-transform--lowercase: lowercase;
--mantine-font-weight-regular: 400;
--mantine-heading-font-weight: 700;
--mantine-h6-font-weight: 700;
--mantine-font-family: ;
--mantine-moz-font-smoothing: grayscale;
--mantine-h5-font-weight: 700;
--mantine-h2-line-height: 1.35;
--mantine-line-height-xs: 1.4;
--mantine-h5-line-height: 1.5;
--mantine-h4-font-weight: 700;
--mantine-font-family-headings: ;
--mantine-font-weight-bold: 700;
--mantine-h4-line-height: 1.45;
--mantine-h2-font-weight: 700;
--mantine-heading-text-wrap: wrap;
--mantine-line-height-md: 1.55;
--mantine-h1-line-height: 1.3;
--mantine-h3-line-height: 1.4;
--mantine-line-height-sm: 1.45;
--mantine-h6-line-height: 1.5;
--mantine-h3-font-weight: 700;
--mantine-line-height-lg: 1.6;
--mantine-webkit-font-smoothing: antialiased;
--mantine-line-height: 1.55;
--mantine-font-weight-medium: 600;
--mantine-line-height-xl: 1.65;
--mantine-h1-font-weight: 700;
```

### Shadows

```css
--mantine-shadow-xs: 0 calc(0.0625rem * 1) calc(0.1875rem * 1) rgba(0,0,0,0.05),0 calc(0.0625rem * 1) calc(0.125rem * 1) rgba(0,0,0,0.1);
--mantine-shadow-sm: 0 calc(0.0625rem * 1) calc(0.1875rem * 1) rgba(0,0,0,0.05),rgba(0,0,0,0.05) 0 calc(0.625rem * 1) calc(0.9375rem * 1) calc(-0.3125rem * 1),rgba(0,0,0,0.04) 0 calc(0.4375rem * 1) calc(0.4375rem * 1) calc(-0.3125rem * 1);
--mantine-shadow-md: 0 calc(0.0625rem * 1) calc(0.1875rem * 1) rgba(0,0,0,0.05),rgba(0,0,0,0.05) 0 calc(1.25rem * 1) calc(1.5625rem * 1) calc(-0.3125rem * 1),rgba(0,0,0,0.04) 0 calc(0.625rem * 1) calc(0.625rem * 1) calc(-0.3125rem * 1);
--mantine-shadow-lg: 0 calc(0.0625rem * 1) calc(0.1875rem * 1) rgba(0,0,0,0.05),rgba(0,0,0,0.05) 0 calc(1.75rem * 1) calc(1.4375rem * 1) calc(-0.4375rem * 1),rgba(0,0,0,0.04) 0 calc(0.75rem * 1) calc(0.75rem * 1) calc(-0.4375rem * 1);
--mantine-shadow-xl: 0 calc(0.0625rem * 1) calc(0.1875rem * 1) rgba(0,0,0,0.05),rgba(0,0,0,0.05) 0 calc(2.25rem * 1) calc(1.75rem * 1) calc(-0.4375rem * 1),rgba(0,0,0,0.04) 0 calc(1.0625rem * 1) calc(1.0625rem * 1) calc(-0.4375rem * 1);
```

### Radii

```css
--radius--small: .5rem;
--radius--main: 1rem;
--radius--round: 100vw;
--nav--radius: var(--radius--small);
--mantine-radius-md: calc(0.5rem * 1);
--mantine-radius-default: calc(0.5rem * 1);
--mantine-radius-xs: calc(0.125rem * 1);
--mantine-radius-lg: calc(1rem * 1);
--mantine-radius-xl: calc(2rem * 1);
--mantine-radius-sm: calc(0.25rem * 1);
```

### Other

```css
--_theme---background: white;
--_column-count---value: 1;
--_theme---background-skeleton<deleted|variable-cc4934e0-a77b-f3f2-b9cf-2a2128b83c04>: color-mix(in lab,currentcolor 10%,transparent);
--swatch--orange: #fa9742;
--max-width--main: calc(var(--site--viewport-max)*1rem);
--max-width--small: 50rem;
--max-width--full: 100%;
--site--gutter: clamp(1*1rem,((1 - ((1 - 1)/(90 - 20)*20))*1rem + ((1 - 1)/(90 - 20))*100vw),1*1rem);
--_theme---background-2<deleted|variable-89fdd2f8-9862-956e-a344-f522b46626b6>: var(--swatch--light);
--swatch--transparent: transparent;
--_trigger---on: 1;
--_trigger---off: 0;
--_button-style---background: var(--_theme---button-primary--background);
--_button-style---background-hover: var(--_theme---button-primary--background-hover);
--swatch--dark: #000;
--swatch--light: #fff;
--_state---false: 0;
--_state---true: 1;
--_responsive---large: 1;
--_responsive---medium: 0;
--_responsive---small: 0;
--_responsive---xsmall: 0;
--focus--offset-inner: calc(var(--focus--width)*-1);
--nav--max-width-outer: var(--max-width--main);
--_theme---nav--background: var(--_theme---background);
--nav--height-total: var(--nav--height);
--nav--height: 4rem;
--nav--max-width-inner: var(--max-width--main);
--nav--hamburger-thickness: var(--border-width--main);
--focus--width: .125rem;
--swatch--grey: #e7e7e7;
--swatch--pink: #da43e7;
--site--viewport-max: 100;
--site--viewport-min: 20;
--_theme---selection-background: color-mix(in srgb,var(--_theme---text)10%,transparent);
--site--column-count: 12;
--focus--offset-outer: .1875rem;
--swatch--brand: #fdc331;
--_alignment---direction: start;
--swatch--beige: #d6c5b5;
--nav--banner-height: 2.4rem;
--nav--menu-open-duration: var(--nav-duration,.4s);
--nav--menu-close-duration: var(--nav-duration,.4s);
--nav--dropdown-open-duration: var(--nav-duration,.4s);
--nav--dropdown-close-duration: var(--nav-duration,.4s);
--site--column-width: calc((min(var(--max-width--main),100% - var(--site--margin)*2) - (var(--site--gutter)*(var(--site--column-count) - 1)))/var(--site--column-count));
--swatch--dark-800<deleted|variable-365b4c66-1363-4e00-8470-ebbf96bc2fde>: #2f2b2d;
--swatch--brand-600<deleted|variable-f4848f9a-e1c5-5c7a-9707-4fe0d1542434>: color-mix(in srgb,var(--swatch--brand-500\<deleted\|variable-5c209bac-cd05-3f37-75d8-4eb87bac274e\>),black 20%);
--swatch--brand-500<deleted|variable-5c209bac-cd05-3f37-75d8-4eb87bac274e>: #c6fb50;
--grid-breakout: [full-start] minmax(0, 1fr) [content-start]
    repeat(var(--site--column-count), minmax(0, var(--site--column-width))) [content-end]
    minmax(0, 1fr) [full-end];
--grid-breakout-single: [full-start] minmax(0, 1fr) [content-start]
    minmax(0, calc(100% - var(--site--margin) * 2)) [content-end] minmax(0, 1fr) [full-end];
--mantine-breakpoint-xl: 88em;
--mantine-breakpoint-lg: 75em;
--mantine-cursor-type: default;
--mantine-scale: 1;
--mantine-z-index-max: 9999;
--mantine-breakpoint-sm: 48em;
--mantine-z-index-app: 100;
--mantine-breakpoint-md: 62em;
--mantine-breakpoint-xs: 36em;
--mantine-z-index-overlay: 400;
--mantine-z-index-modal: 200;
```

### Dependencies

```css
--_text-style---font-family: --_typography---font--primary-family;
--_theme---text: --swatch--dark;
--_text-style---font-size: --_typography---font-size--text-main;
--_text-style---font-weight: --_typography---font--primary-regular;
--_gap---size: --site--gutter;
--_spacing---space--5: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---space--3: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_text-style---margin-bottom: --_spacing---space--4;
--_spacing---space--6: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---space--2: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---section-space--small: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---section-space--main: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---section-space--large: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--site--margin: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---section-space--page-top: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--max-width--main: --site--viewport-max;
--_spacing---space--8: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_text-style---margin-top: --_spacing---space--4;
--_text-style---trim-top: --_typography---font--primary-trim-top;
--_text-style---trim-bottom: --_typography---font--primary-trim-bottom;
--_spacing---space--7: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_theme---heading-accent: --swatch--brand;
--_theme---background-2<deleted|variable-89fdd2f8-9862-956e-a344-f522b46626b6>: --swatch--light;
--_spacing---space--1: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_spacing---space--4: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_theme---border: --_theme---text;
--_typography---font-size--text-large: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_button-style---text: --_theme---button-primary--text;
--_button-style---text-hover: --_theme---button-primary--text-hover;
--_button-style---background: --_theme---button-primary--background;
--_button-style---background-hover: --_theme---button-primary--background-hover;
--_button-style---border: --_theme---button-primary--border;
--_button-style---border-hover: --_theme---button-primary--border-hover;
--_theme---text-link--border: --_theme---border;
--_theme---text-link--border-hover: --_theme---text;
--_theme---text-link--text: --swatch--pink;
--_theme---text-link--text-hover: --_theme---text-link--text;
--focus--offset-inner: --focus--width;
--nav--max-width-outer: --max-width--main;
--nav--spacing-outer-horizontal: --site--margin;
--_typography---font-size--text-small: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_theme---nav--background: --_theme---background;
--nav--radius: --radius--small;
--nav--height-total: --nav--height;
--nav--spacing-outer-vertical: --site--margin;
--nav--max-width-inner: --max-width--main;
--nav--hamburger-thickness: --border-width--main;
--nav--hamburger-gap: --_spacing---space--2;
--_typography---font-size--h4: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_text-style---text-transform: --_typography---text-transform--none;
--_theme---selection-background: --_theme---text;
--_theme---button-primary--background: --_theme---text;
--_theme---button-primary--border: --_theme---text;
--_theme---button-primary--text: --_theme---background;
--_theme---button-primary--background-hover: --_theme---background;
--_theme---button-primary--border-hover: --_theme---border;
--_theme---button-primary--text-hover: --_theme---text;
--_theme---button-secondary--background: --swatch--transparent;
--_theme---button-secondary--border: --_theme---border;
--_theme---button-secondary--text: --_theme---text;
--_theme---button-secondary--background-hover: --_theme---text;
--_theme---button-secondary--border-hover: --_theme---button-secondary--background-hover;
--_theme---button-secondary--text-hover: --_theme---background;
--nav--spacing-inner-horizontal: --_spacing---space--5;
--nav--menu-open-duration: --nav-duration;
--nav--menu-close-duration: --nav-duration;
--nav--dropdown-open-duration: --nav-duration;
--nav--dropdown-close-duration: --nav-duration;
--_typography---font-size--text-main: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h6: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h5: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h3: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h2: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--h1: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--_typography---font-size--display: --site--viewport-max,--site--viewport-min,--site--viewport-min,--site--viewport-max,--site--viewport-min;
--site--column-width: --max-width--main,--site--margin,--site--gutter,--site--column-count,--site--column-count;
--_typography---text-transform--none: --text-transform;
--swatch--brand-600<deleted|variable-f4848f9a-e1c5-5c7a-9707-4fe0d1542434>: --swatch--brand-500;
--grid-breakout: --site--column-count,--site--column-width;
--grid-breakout-single: --site--margin;
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
| sm | 576px | min-width |
| md | 767px | max-width |
| md | 768px | min-width |
| lg | 991px | max-width |
| lg | 992px | min-width |
| 1200px | 1200px | min-width |
| 1408px | 1408px | min-width |
| 1632px | 1632px | min-width |

## Transitions & Animations

**Durations:** `0.2s`, `0.4s`, `0.1s`, `0.3s`, `0.6s`

### Common Transitions

```css
transition: all;
transition: opacity 0.2s;
transition: transform 0.2s;
transition: grid-template-rows 0.4s;
transition: opacity 0.1s;
transition: 0.2s;
transition: opacity 0.4s;
transition: opacity 0.3s;
transition: transform 0.6s;
```

### Keyframe Animations

**m_5d2b3b9d**
```css
@keyframes m_5d2b3b9d {
  0% { transform: scale(0.6); opacity: 0; }
  50%, 100% { transform: scale(1); }
}
```

**m_aac34a1**
```css
@keyframes m_aac34a1 {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(0.6); opacity: 0.5; }
}
```

**m_f8e89c4b**
```css
@keyframes m_f8e89c4b {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

**m_885901b1**
```css
@keyframes m_885901b1 {
  0% { opacity: 0.6; transform: scale(0); }
  100% { opacity: 0; transform: scale(2.8); }
}
```

**m_55dc625a**
```css
@keyframes m_55dc625a {
  0% { transform: translateX(0px); }
  100% { transform: translateX(calc(-100% / var(--marquee-repeat, 4) - var(--marquee-gap, var(--mantine-spacing-md)) / var(--marquee-repeat, 4))); }
}
```

**m_cdef532c**
```css
@keyframes m_cdef532c {
  0% { transform: translateY(0px); }
  100% { transform: translateY(calc(-100% / var(--marquee-repeat, 4) - var(--marquee-gap, var(--mantine-spacing-md)) / var(--marquee-repeat, 4))); }
}
```

**m_81a374bd**
```css
@keyframes m_81a374bd {
  0% { background-position: 0px 0px; }
  100% { background-position: calc(2.5rem * var(--mantine-scale)) 0; }
}
```

**m_e0fb7a86**
```css
@keyframes m_e0fb7a86 {
  0% { background-position: 0px 0px; }
  100% { background-position: 0 calc(2.5rem * var(--mantine-scale)); }
}
```

**m_18d73873**
```css
@keyframes m_18d73873 {
  0% { transform: var(--rn-roll-from); }
  100% { transform: var(--rn-roll-to); }
}
```

**m_299c329c**
```css
@keyframes m_299c329c {
  0%, 100% { opacity: 0.4; }
  50% { opacity: 1; }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (14 instances)

```css
.button {
  color: rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (44 instances)

```css
.card {
  background-color: rgb(0, 0, 0);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (60 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
}
```

### Navigation (175 instances)

```css
.navigatio {
  background-color: rgb(253, 195, 49);
  color: rgb(0, 0, 0);
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
  background-color: rgb(231, 231, 231);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 23.8px;
}
```

### Modals (11 instances)

```css
.modal {
  background-color: rgba(0, 0, 0, 0.15);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Dropdowns (91 instances)

```css
.dropdown {
  background-color: rgb(253, 195, 49);
  border-radius: 0px;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Switches (6 instances)

```css
.switche {
  border-radius: 0px;
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
  font-size: 23.8px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Button — 11 instances, 1 variant

**Variant 1** (11 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Button — 12 instances, 2 variants

**Variant 1** (11 instances)

```css
  background: color(srgb 0 0 0 / 0);
  color: color(srgb 0 0 0);
  padding: 18.4px 40px 18.4px 40px;
  border-radius: 0px;
  border: 1px solid color(srgb 0 0 0 / 0.5);
  font-size: 23.8px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: color(srgb 1 1 1 / 0.4);
  color: rgb(0, 0, 0);
  padding: 18.4px 28px 18.4px 28px;
  border-radius: 0px;
  border: 0px none color(srgb 0 0 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Button — 12 instances, 2 variants

**Variant 1** (11 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: color(srgb 0 0 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none color(srgb 0 0 0);
  font-size: 15.5px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 15.5px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Card — 11 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(214, 197, 181);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

**Variant 2** (10 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Card — 8 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 618px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

**Variant 2** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 35px 35px 35px 35px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 45px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 45px;
  font-weight: 500;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: color(srgb 0.839216 0.772549 0.709804 / 0.25);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(253, 195, 49);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 23.8px;
  font-weight: 400;
```

### Link — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 23.8px;
  font-weight: 400;
```

## Layout System

**20 grid containers** and **191 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1600px | 0px |
| 100% | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 8x |
| 1-column | 6x |
| 2-column | 5x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 610px 610px;
gap: 58px 16px;
grid-template-columns: 618px 618px;
grid-template-columns: 401.328px 401.328px 401.344px;
gap: 16px;
grid-template-columns: 401.328px 401.328px 401.328px;
gap: 16px;
grid-template-columns: 401.328px 401.328px 401.344px;
gap: 16px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 83x |
| row/nowrap | 107x |
| row/wrap | 1x |

**Gap values:** `11.5px`, `126px`, `15.5px`, `16px`, `35px`, `40px`, `40px 16px`, `58px 16px`, `64px`, `7.5px`, `84px`, `8px`, `normal 11.5px`, `normal 15.5px`, `normal 25.6px`, `normal 35px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 88/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 100/100 |
| Spacing System | 70/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 118 !important rules — prefer specificity over overrides
- 83% of CSS is unused — consider purging
- 6620 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 90deg | 2 | brand |
| linear | — | 3 | bold |

```css
background: linear-gradient(90deg, rgb(253, 195, 49) 53%, rgba(0, 0, 0, 0));
background: linear-gradient(-90deg, rgb(253, 195, 49), rgba(0, 0, 0, 0));
```

## Z-Index Map

**10 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1000,1000 | div.n.a.v._.c.o.m.p.o.n.e.n.t. .w.-.v.a.r.i.a.n.t.-.d.d.8.6.6.6.5.9.-.1.d.7.d.-.6.4.4.7.-.6.4.6.1.-.6.6.c.a.8.6.c.a.3.6.7.f. .u.-.t.h.e.m.e.-.b.r.a.n.d |
| sticky | 10,10 | div.n.a.v._.d.r.o.p._.b.a.c.k.d.r.o.p, svg.c.o.r.n.e.r.-.s.v.g, svg.c.o.r.n.e.r.-.s.v.g |
| base | -1000,6 | iframe, div.n.a.v._.m.e.n.u._.b.a.c.k.d.r.o.p, div.u.-.v.i.s.u.a.l.-.b.k |

## SVG Icons

**7 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 2 |
| md | 1 |
| lg | 1 |
| xl | 2 |

**Icon colors:** `currentColor`, `black`, `#DA43E7`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| Gt Planar Trial | self-hosted | 400 | normal |
| Magistersttrial | self-hosted | 400 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 33 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 6 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (32x), 16:9 (5x), 4.55:1 (2x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `600ms` | 600 |

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `menuClose` | custom | clip-path | 1 |
| `menuClose` | custom | clip-path | 1 |
| `scroll` | slide-x | transform | 2 |

## Component Anatomy

### button — 43 instances

**Slots:** label, icon
**Sizes:** small

### card — 37 instances

**Slots:** media
**Sizes:** large

### link — 4 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **learn** (16)
- **contact** (14)
- **about** (7)
- **play** (3)
- **close** (1)
- **build** (1)
- **primary** (1)
- **excess** (1)

### Button Copy Patterns

- "learn more" (10×)
- "contact us" (6×)
- "learn more
learn more" (5×)
- "contact us
contact us" (4×)
- "play video" (3×)
- "about
about" (2×)
- "about" (2×)
- "contact
contact" (2×)
- "contact" (2×)
- "about shepherd" (2×)

### Sample Headings

> Making risk frictionless  
‍Insurance   for the builders and operators shaping   our
physical   world.
> Smarter underwriting powered by data and technology.
> Shepherd Savings
> Insurance solutions built for a changing world.
> Accelerating the world's most important commercial industries.
> A new vision for commercial insurance.
> Essential coverage for annual programs or projects.
> Turn risk management into a competitive advantage.
> PRODUCTS
> INDUSTRIES

## Page Intent

**Type:** `landing` (confidence 0.31)
**Description:** Commercial insurance for construction's middle market with industry leading speed-to-quote

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → nav → nav → nav → nav → nav → logo-wall → nav → nav → nav → nav → nav → testimonial → hero → testimonials → hero → testimonials → content → content → testimonials → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | nav | — | 0.9 |
| 2 | nav | — | 0.9 |
| 3 | nav | — | 0.9 |
| 4 | nav | — | 0.9 |
| 5 | nav | — | 0.9 |
| 6 | nav | — | 0.9 |
| 7 | nav | — | 0.9 |
| 8 | nav | — | 0.9 |
| 9 | nav | — | 0.9 |
| 10 | nav | — | 0.9 |
| 11 | logo-wall | Making risk frictionless  
‍Insurance   for the builders and operators shaping   | 0.85 |
| 12 | testimonial | Smarter underwriting powered by data and technology. | 0.8 |
| 13 | hero | Accelerating the world's most important commercial industries. | 0.4 |
| 14 | testimonials | A new vision for commercial insurance. | 0.4 |
| 15 | hero | Turn risk management into a competitive advantage. | 0.4 |
| 16 | testimonials | PRODUCTS | 0.4 |
| 17 | content | PRODUCTS | 0.3 |
| 18 | content | INDUSTRIES | 0.3 |
| 19 | testimonials | RESOURCES | 0.4 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.343 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 8px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.077)
**Counts:** total 39, svg 0, icon 16, screenshot-like 0, photo-like 6
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `vuetify` (confidence 0.62)

Evidence:
- 16 v-* classes

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Magistersttrial` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
