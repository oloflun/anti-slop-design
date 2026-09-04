# Design Language: The Content Operating System for the AI era | Sanity

> Extracted from `https://www.sanity.io` on September 4, 2026
> 1925 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#0052ef` | rgb(0, 82, 239) | hsl(219, 100%, 47%) | 4 |
| Secondary | `#9ecbff` | rgb(158, 203, 255) | hsl(212, 100%, 81%) | 116 |
| Accent | `#ff5500` | rgb(255, 85, 0) | hsl(20, 100%, 50%) | 6 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#ffffff` | hsl(0, 0%, 100%) | 1259 |
| `#0b0b0b` | hsl(0, 0%, 4%) | 1054 |
| `#e1e4e8` | hsl(214, 13%, 90%) | 582 |
| `#000000` | hsl(0, 0%, 0%) | 384 |
| `#797979` | hsl(0, 0%, 47%) | 122 |
| `#b9b9b9` | hsl(0, 0%, 73%) | 112 |
| `#353535` | hsl(0, 0%, 21%) | 20 |
| `#212121` | hsl(0, 0%, 13%) | 18 |
| `#6a737d` | hsl(212, 8%, 45%) | 8 |
| `#4a4a4a` | hsl(0, 0%, 29%) | 4 |
| `#d6d6d6` | hsl(0, 0%, 84%) | 3 |
| `#ededed` | hsl(0, 0%, 93%) | 2 |

### Background Colors

Used on large-area elements: `#ffffff`, `#121923`, `#0b0b0b`

### Text Colors

Text color palette: `#000000`, `#0b0b0b`, `#ffffff`, `#797979`, `#b9b9b9`, `#e1e4e8`, `#f97583`, `#9ecbff`, `#79b8ff`, `#b392f0`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#ffffff` | background, text, border | 1259 |
| `#0b0b0b` | text, border, background | 1054 |
| `#e1e4e8` | text, border | 582 |
| `#000000` | text, border | 384 |
| `#f97583` | text, border | 128 |
| `#797979` | text, border | 122 |
| `#9ecbff` | text, border | 116 |
| `#b9b9b9` | text, border | 112 |
| `#79b8ff` | text, border | 50 |
| `#b392f0` | text, border | 40 |
| `#353535` | border, background | 20 |
| `#212121` | border, background | 18 |
| `#ffab70` | text, border | 10 |
| `#6a737d` | text, border | 8 |
| `#ff5500` | background | 6 |
| `#0052ef` | background, border, text | 4 |
| `#4a4a4a` | text, border | 4 |
| `#007800` | text, border | 4 |
| `#d6d6d6` | border | 3 |
| `#ededed` | background | 2 |
| `#121923` | background | 1 |
| `#acabab` | border | 1 |

## Typography

### Font Families

- **Waldenburg-75357948a2b6a39b** — used for all (1141 elements)
- **IBM Plex Mono-c20ba633a65a8c57** — used for all (758 elements)
- **Helvetica** — used for body (19 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 112px | 7rem | 400 | 112px | -4.48px | h1 |
| 72px | 4.5rem | 400 | 72px | -2.88px | h2, div |
| 60px | 3.75rem | 400 | 48px | normal | a, astro-island, video |
| 48px | 3rem | 400 | 51.6px | -1.68px | h3, h2 |
| 38px | 2.375rem | 400 | 41.8px | -1.14px | h3, p |
| 32px | 2rem | 425 | 35.2px | -0.32px | p, span, a, div |
| 24px | 1.5rem | 400 | 26.4px | -0.24px | span, div, a, button |
| 20px | 1.25rem | 400 | 22px | -0.2px | p |
| 18px | 1.125rem | 400 | 23.4px | -0.18px | p, blockquote |
| 16px | 1rem | 400 | 24px | normal | html, head, style, meta |
| 15px | 0.9375rem | 400 | 19.5px | -0.15px | input, textarea, p, span |
| 13px | 0.8125rem | 400 | 16.9px | normal | a, span, button, p |
| 12px | 0.75rem | 400 | 18px | normal | span, div, pre, code |
| 11px | 0.6875rem | 400 | 16.5px | normal | span |
| 10px | 0.625rem | 400 | 13px | normal | p, span, h3 |

### Heading Scale

```css
h1 { font-size: 112px; font-weight: 400; line-height: 112px; }
h2 { font-size: 72px; font-weight: 400; line-height: 72px; }
h3 { font-size: 48px; font-weight: 400; line-height: 51.6px; }
h3 { font-size: 38px; font-weight: 400; line-height: 41.8px; }
h3 { font-size: 24px; font-weight: 400; line-height: 26.4px; }
h2 { font-size: 16px; font-weight: 400; line-height: 24px; }
h3 { font-size: 10px; font-weight: 400; line-height: 13px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: 18px; }
```

### Font Weights in Use

`400` (1909x), `425` (6x), `500` (3x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-32 | 32px | 2rem |
| spacing-48 | 48px | 3rem |
| spacing-64 | 64px | 4rem |
| spacing-90 | 90px | 5.625rem |
| spacing-103 | 103px | 6.4375rem |
| spacing-116 | 116px | 7.25rem |
| spacing-127 | 127px | 7.9375rem |
| spacing-148 | 148px | 9.25rem |
| spacing-161 | 161px | 10.0625rem |
| spacing-233 | 233px | 14.5625rem |
| spacing-256 | 256px | 16rem |
| spacing-278 | 278px | 17.375rem |
| spacing-340 | 340px | 21.25rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 3px | 7 |
| md | 6px | 1 |
| lg | 11px | 2 |
| full | 99999px | 54 |

## Box Shadows

**sm (inset)** — blur: 0px
```css
box-shadow: rgb(53, 53, 53) 0px 0px 0px 1px inset;
```

## CSS Custom Properties

### Colors

```css
--osano-button-border-color: #fff;
--osano-button-background-color: #f36458;
--osano-button-foreground-color: #121923;
--osano-dialog-background-color: #121923;
--osano-dialog-foreground-color: #afbaca;
--osano-info-dialog-overlay-color: rgba(18,25,35,0.2);
--osano-link-color: #f68b82;
--osano-toggle-off-track-color: #3c4758;
--osano-toggle-off-thumb-color: #ffffff;
--osano-toggle-on-track-color: #206ee9;
--osano-toggle-on-thumb-color: #ffffff;
--osano-widget-color: #37cd8f;
--osano-widget-outline-color: #29246a;
--osano-widget-fill-color: #fff;
--osano-focus-outline-color: Highlight;
--osano-button-close-color: var(--osano-dialog-foreground-color);
--osano-button-accept-background-color: var(--osano-button-background-color);
--osano-button-accept-border-color: var(--osano-button-border-color, var(--osano-button-foreground-color));
--osano-button-accept-foreground-color: var(--osano-button-foreground-color);
--osano-button-deny-background-color: #121923;
--osano-button-deny-border-color: var(--osano-button-border-color, var(--osano-button-foreground-color));
--osano-button-deny-foreground-color: #afbaca;
--osano-button-reject-all-background-color: var(--osano-button-background-color);
--osano-button-reject-all-background-color-hover: var(--osano-button-background-color-hover, var(--osano-button-background-color-contrast));
--osano-button-reject-all-border-color: var(--osano-button-border-color, var(--osano-button-foreground-color));
--osano-button-reject-all-foreground-color: var(--osano-button-foreground-color);
--osano-button-manage-background-color: var(--osano-button-background-color);
--osano-button-manage-border-color: var(--osano-button-border-color, var(--osano-button-foreground-color));
--osano-button-manage-foreground-color: var(--osano-button-foreground-color);
--osano-info-dialog-link-color: var(--osano-link-color);
--osano-info-dialog-button-close-color: var(--osano-info-dialog-foreground-color, var(--osano-dialog-foreground-color));
--osano-info-dialog-toggle-off-track-color: var(--osano-toggle-off-track-color);
--osano-info-dialog-toggle-off-thumb-color: var(--osano-toggle-off-thumb-color);
--osano-info-dialog-toggle-on-track-color: var(--osano-toggle-on-track-color);
--osano-info-dialog-toggle-on-thumb-color: var(--osano-toggle-on-thumb-color);
--osano-info-dialog-button-background-color: var(--osano-button-background-color);
--osano-info-dialog-button-border-color: var(--osano-info-dialog-button-foreground-color, var(--osano-button-foreground-color));
--osano-info-dialog-button-foreground-color: var(--osano-button-foreground-color);
--osano-dialog-gpc-background-color: var(--osano-dialog-background-color);
--osano-dialog-gpc-border-color: var(--osano-dialog-foreground-color);
--osano-dialog-gpc-foreground-color: var(--osano-dialog-foreground-color);
--osano-dialog-gpc-color: #37cd84;
--osano-info-dialog-gpc-background-color: var(--osano-info-dialog-background-color, var(--osano-dialog-background-color));
--osano-info-dialog-gpc-border-color: var(--osano-info-dialog-foreground-color, var(--osano-dialog-foreground-color));
--osano-info-dialog-gpc-foreground-color: var(--osano-info-dialog-foreground-color, var(--osano-dialog-foreground-color));
--osano-info-dialog-gpc-color: var(--osano-dialog-gpc-color);
--osano-gpc-background-color: #ffffff;
--osano-gpc-border-color: #058a5e;
--osano-gpc-foreground-color: #058a5e;
--osano-gpc-color: #37cd84;
--osano-gpc-background-color-hover: #ffffff;
--osano-info-dialog-background-color: #121923;
--osano-info-dialog-foreground-color: #afbaca;
--osano-toggle-off-background-color: #d2cfff;
--osano-toggle-button-off-color: #ffffff;
--osano-toggle-on-background-color: #37cd8f;
--osano-toggle-button-on-color: #f4f4f4;
--osano-button-background-color-contrast: #df5044;
--osano-button-foreground-color-contrast: #262d37;
--osano-button-deny-background-color-contrast: #262d37;
--osano-button-deny-foreground-color-contrast: #9ba6b6;
--osano-dialog-background-color-contrast: #262d37;
--osano-dialog-foreground-color-contrast: #9ba6b6;
--osano-link-color-contrast: #e2776e;
--osano-toggle-off-track-color-contrast: #505b6c;
--osano-toggle-off-track-color-disabled: #7c8798;
--osano-toggle-off-thumb-color-contrast: #ebebeb;
--osano-toggle-off-thumb-color-disabled: #bfbfbf;
--osano-toggle-on-track-color-contrast: #3482fd;
--osano-toggle-on-track-color-disabled: #60aeff;
--osano-toggle-on-thumb-color-contrast: #ebebeb;
--osano-toggle-on-thumb-color-disabled: #bfbfbf;
--osano-gpc-background-color-contrast: #ebebeb;
--osano-button-background-color-hover: var(--osano-button-background-color-contrast, #df5044);
--osano-button-foreground-color-hover: var(--osano-button-foreground-color-contrast, #262d37);
--osano-button-background-color-focus: var(--osano-button-foreground-color-hover, var(--osano-button-foreground-color-contrast));
--osano-button-foreground-color-focus: var(--osano-button-background-color-hover, var(--osano-button-background-color-contrast));
--osano-toggle-off-track-color-hover: var(--osano-toggle-off-track-color-contrast, #505b6c);
--osano-toggle-off-thumb-color-hover: var(--osano-toggle-off-thumb-color-contrast, #ebebeb);
--osano-toggle-off-track-color-focus: var(--osano-toggle-off-thumb-color-hover, var(--osano-toggle-off-thumb-color-contrast));
--osano-toggle-off-thumb-color-focus: var(--osano-toggle-off-track-color-hover, var(--osano-toggle-off-track-color-contrast));
--osano-toggle-on-track-color-hover: var(--osano-toggle-on-track-color-contrast, #3482fd);
--osano-toggle-on-thumb-color-hover: var(--osano-toggle-on-thumb-color-contrast, #ebebeb);
--osano-toggle-on-track-color-focus: var(--osano-toggle-on-thumb-color-hover, var(--osano-toggle-on-thumb-color-contrast));
--osano-toggle-on-thumb-color-focus: var(--osano-toggle-on-track-color-hover, var(--osano-toggle-on-track-color-contrast));
--osano-button-accept-background-color-contrast: var(--osano-button-background-color-contrast, #df5044);
--osano-button-accept-foreground-color-contrast: var(--osano-button-foreground-color-contrast, #262d37);
--osano-button-accept-background-color-hover: var(--osano-button-background-color-hover, var(--osano-button-background-color-contrast));
--osano-button-accept-foreground-color-hover: var(--osano-button-accept-foreground-color-contrast, var(--osano-button-foreground-color-contrast));
--osano-button-accept-background-color-focus: var(--osano-button-accept-foreground-color-hover, var(--osano-button-accept-foreground-color-contrast));
--osano-button-accept-foreground-color-focus: var(--osano-button-accept-background-color-hover, var(--osano-button-background-color-hover));
--osano-button-deny-background-color-hover: var(--osano-button-background-color-hover, var(--osano-button-background-color-contrast));
--osano-button-deny-foreground-color-hover: var(--osano-button-deny-foreground-color-contrast, #9ba6b6);
--osano-button-deny-background-color-focus: var(--osano-button-deny-foreground-color-hover, var(--osano-button-deny-foreground-color-contrast));
--osano-button-deny-foreground-color-focus: var(--osano-button-deny-background-color-hover, var(--osano-button-background-color-hover));
--osano-button-reject-all-background-color-contrast: var(--osano-button-background-color-contrast, #df5044);
--osano-button-reject-all-foreground-color-contrast: var(--osano-button-foreground-color-contrast, #262d37);
--osano-button-reject-all-foreground-color-hover: var(--osano-button-reject-all-foreground-color-contrast, var(--osano-button-foreground-color-contrast));
--osano-button-reject-all-background-color-focus: var(--osano-button-reject-all-foreground-color-hover, var(--osano-button-reject-all-foreground-color-contrast));
--osano-button-reject-all-foreground-color-focus: var(--osano-button-reject-all-background-color-hover, var(--osano-button-background-color-hover));
--osano-button-manage-background-color-contrast: var(--osano-button-background-color-contrast, #df5044);
--osano-button-manage-foreground-color-contrast: var(--osano-button-foreground-color-contrast, #262d37);
--osano-button-manage-background-color-hover: var(--osano-button-background-color-hover, var(--osano-button-background-color-contrast));
--osano-button-manage-foreground-color-hover: var(--osano-button-manage-foreground-color-contrast, var(--osano-button-foreground-color-contrast));
--osano-button-manage-background-color-focus: var(--osano-button-manage-foreground-color-hover, var(--osano-button-manage-foreground-color-contrast));
--osano-button-manage-foreground-color-focus: var(--osano-button-manage-background-color-hover, var(--osano-button-background-color-hover));
--osano-info-dialog-button-background-color-contrast: var(--osano-button-background-color-contrast, #df5044);
--osano-info-dialog-button-foreground-color-contrast: var(--osano-button-foreground-color-contrast, #262d37);
--osano-info-dialog-button-background-color-hover: var(--osano-button-background-color-hover, var(--osano-button-background-color-contrast));
--osano-info-dialog-button-foreground-color-hover: var(--osano-info-dialog-button-foreground-color-contrast, var(--osano-button-foreground-color-contrast));
--osano-info-dialog-button-background-color-focus: var(--osano-info-dialog-button-foreground-color-hover, var(--osano-info-dialog-button-foreground-color-contrast));
--osano-info-dialog-button-foreground-color-focus: var(--osano-info-dialog-button-background-color-hover, var(--osano-button-background-color-hover));
--osano-info-dialog-toggle-off-track-color-contrast: var(--osano-toggle-off-track-color-contrast, #505b6c);
--osano-info-dialog-toggle-off-thumb-color-contrast: var(--osano-toggle-off-thumb-color-contrast, #ebebeb);
--osano-info-dialog-toggle-off-track-color-hover: var(--osano-info-dialog-toggle-off-track-color-contrast, var(--osano-toggle-off-track-color-contrast));
--osano-info-dialog-toggle-off-thumb-color-hover: var(--osano-info-dialog-toggle-off-thumb-color-contrast, var(--osano-toggle-off-thumb-color-contrast));
--osano-info-dialog-toggle-off-track-color-focus: var(--osano-info-dialog-toggle-off-thumb-color-hover, var(--osano-info-dialog-toggle-off-thumb-color-contrast));
--osano-info-dialog-toggle-off-thumb-color-focus: var(--osano-info-dialog-toggle-off-track-color-hover, var(--osano-info-dialog-toggle-off-track-color-contrast));
--osano-info-dialog-toggle-off-track-color-disabled: var(--osano-toggle-off-track-color-disabled, #7c8798);
--osano-info-dialog-toggle-off-thumb-color-disabled: var(--osano-toggle-off-thumb-color-disabled, #bfbfbf);
--osano-info-dialog-toggle-on-track-color-contrast: var(--osano-toggle-on-track-color-contrast, #3482fd);
--osano-info-dialog-toggle-on-thumb-color-contrast: var(--osano-toggle-on-thumb-color-contrast, #ebebeb);
--osano-info-dialog-toggle-on-track-color-hover: var(--osano-info-dialog-toggle-on-track-color-contrast, var(--osano-toggle-on-track-color-contrast));
--osano-info-dialog-toggle-on-thumb-color-hover: var(--osano-info-dialog-toggle-on-thumb-color-contrast, var(--osano-toggle-on-thumb-color-contrast));
--osano-info-dialog-toggle-on-track-color-focus: var(--osano-info-dialog-toggle-on-thumb-color-hover, var(--osano-info-dialog-toggle-on-thumb-color-contrast));
--osano-info-dialog-toggle-on-thumb-color-focus: var(--osano-info-dialog-toggle-on-track-color-hover, var(--osano-info-dialog-toggle-on-track-color-contrast));
--osano-info-dialog-toggle-on-track-color-disabled: var(--osano-toggle-on-track-color-disabled, #60aeff);
--osano-info-dialog-toggle-on-thumb-color-disabled: var(--osano-toggle-on-thumb-color-disabled, #bfbfbf);
--osano-info-dialog-link-color-contrast: var(--osano-link-color-contrast, #e2776e);
--color-black: #0b0b0b;
--color-white: #fff;
--color-brand: #ff560a;
--color-gray-100: #ededed;
--color-gray-200: #d6d6d6;
--color-gray-300: #b9b9b9;
--color-gray-500: #797979;
--color-gray-700: #4a4a4a;
--color-gray-800: #353535;
--color-gray-900: #212121;
--color-blue-100: #afe3ff;
--color-blue-300: #55beff;
--color-blue-500: #0084f8;
--color-blue-700: #0052ef;
--color-green-100: #96ff6f;
--color-green-300: #45ff00;
--color-green-500: #00fe00;
--color-green-700: #19d600;
--color-magenta-100: #fcb9ff;
--color-magenta-300: #fa84ff;
--color-magenta-500: #ff23fc;
--color-magenta-700: #f500ff;
--color-yellow-100: #fcffd6;
--color-yellow-300: #ffff9f;
--color-yellow-500: #fdfe00;
--color-yellow-700: #fff500;
--focus-ring-width: 2px;
--focus-ring-offset: 2px;
--focus-ring-style: dotted;
--tw-mask-bottom-to-color: transparent;
--color-fg-error: #d00;
--color-fg-accent-green: color(display-p3 .270588 1 0);
--tw-mask-bottom-from-color: black;
--tw-inset-ring-shadow: 0 0 #0000;
--color-fg-accent-magenta: color(display-p3 .960784 0 1);
--color-yellow-400: #f9bc15;
--color-bg-accent-blue-dim: #afe3ff;
--color-border-accent-green: #19d600;
--color-border-accent-blue: #0052ef;
--color-fg-inverse-faint: #797979;
--color-border-base: #0b0b0b;
--color-cyan-50: #e7fefe;
--color-bg-base: #fff;
--color-bg-inverse-base: #0b0b0b;
--color-yellow-950: #181410;
--color-red-300: #fdada5;
--color-fg-accent-blue: color(display-p3 .007843 .498039 1);
--color-yellow-50: #fefae1;
--color-fg-inverse-base: #fff;
--color-yellow-200: #f9e994;
--tw-border-style: solid;
--color-border-dim: #d6d6d6;
--tw-ring-shadow: 0 0 #0000;
--color-fg-dim: #4a4a4a;
--color-yellow-800: #3b220c;
--color-red-200: #ffdedc;
--color-fg-inverse-dim: #b9b9b9;
--color-bg-accent-green-base: color(display-p3 .270588 1 0);
--color-border-faint: #ededed;
--tw-ring-offset-color: #fff;
--color-bg-accent-green-dim: #96ff6f;
--color-border-accent-yellow: #fff500;
--color-red-800: #4d1714;
--tw-ring-offset-width: 0px;
--color-border-accent-magenta: #f500ff;
--color-bg-accent-magenta-dim: #fcb9ff;
--color-fg-base: #0b0b0b;
--color-bg-accent-blue-base: color(display-p3 .007843 .498039 1);
--color-bg-inverse-dim: #212121;
--color-fg-accent-yellow: color(display-p3 1 1 0);
--color-border-inverse-base: #fff;
--tw-ring-offset-shadow: 0 0 #0000;
--color-bg-accent-magenta-base: color(display-p3 .960784 0 1);
--color-bg-accent-yellow-base: color(display-p3 1 1 0);
--color-bg-accent-yellow-dim: #fcffd6;
--color-fg-accent-red: ;
--color-bg-dim: #ededed;
--color-yellow-900: #271a11;
--color-fg-faint: #797979;
--color-focus-ring: #0b0b0b;
```

### Spacing

```css
--spacing-icon-lg: calc((25 / 16) * 1rem);
--spacing-icon-md: calc((21 / 16) * 1rem);
--spacing-icon-sm: calc((19 / 16) * 1rem);
--spacing-widget-xs: calc((19 / 16) * 1rem);
--spacing-widget-sm: calc((25 / 16) * 1rem);
--spacing-widget-md: calc((35 / 16) * 1rem);
--spacing-widget-lg: calc((45 / 16) * 1rem);
--spacing-widget-xl: calc((73 / 16) * 1rem);
--spacing-0: 0rem;
--spacing-2: .125rem;
--spacing-4: .25rem;
--spacing-6: .375rem;
--spacing-8: .5rem;
--spacing-12: .75rem;
--spacing-16: 1rem;
--spacing-20: 1.125rem;
--spacing-24: 1.51rem;
--spacing-32: 2rem;
--spacing-40: 2.5rem;
--spacing-48: 3rem;
--spacing-64: 4rem;
--spacing-80: 5rem;
--spacing-96: 6rem;
--spacing-128: 8rem;
--section-padding-x: 1.5rem;
--margin-x-min: 24px;
--margin-x: max(var(--margin-x-min), calc((100vw - var(--max-width)) / 2));
--tw-space-x-reverse: 0;
--tw-space-y-reverse: 0;
```

### Typography

```css
--font-sans: Waldenburg-75357948a2b6a39b,"Waldenburg-75357948a2b6a39b fallback: Arial",ui-sans-serif,system-ui,sans-serif;
--font-mono: "IBM Plex Mono-c20ba633a65a8c57","IBM Plex Mono-c20ba633a65a8c57 fallback: Courier New",ui-monospace,monospace;
--sanity-id-heading-font-features: "ss07" on, "cv01" on, "cv11" on, "cv12" on, "cv13" on;
--sanity-id-texture-dots-grid-base-small-light: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-dense-small-dark: url("data:image/svg+xml,%3Csvg width='6' height='6' viewBox='0 0 6 6' fill='none' opacity='0.6' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%23ffffff' /%3E%3Ccircle cx='3.75' cy='3.75' r='0.75' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-dense-small-light: url("data:image/svg+xml,%3Csvg width='4' height='4' viewBox='0 0 4 4' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%230B0B0B'/%3E%3C/svg%3E");
--font-weight-bold: 700;
--sanity-id-texture-dots-grid-spread-large-light: url("data:image/svg+xml,%3Csvg width='15' height='15' viewBox='0 0 15 15' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1.5' cy='1.5' r='1.5' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-dense-medium-dark: url("data:image/svg+xml,%3Csvg width='6' height='6' viewBox='0 0 6 6' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-spread-small-light: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%230B0B0B'/%3E%3Ccircle cx='6.75' cy='6.75' r='0.75' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-lines-horizontal-medium-light: url("data:image/svg+xml,%3Csvg width='4' height='8' viewBox='0 0 4 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0.25H4' stroke='%230B0B0B' stroke-width='0.5'/%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-dense-large-light: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1.5' cy='1.5' r='1.5' fill='%230B0B0B' /%3E%3Ccircle cx='7.5' cy='7.5' r='1.5' fill='%230B0B0B' /%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-spread-small-light: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-lines-horizontal-large-dark: url("data:image/svg+xml,%3Csvg width='4' height='12' viewBox='0 0 4 12' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0.25H4' stroke='%23ffffff' stroke-width='0.5' /%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-base-medium-light: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-spread-medium-dark: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-spread-small-dark: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-dense-small-light: url("data:image/svg+xml,%3Csvg width='6' height='6' viewBox='0 0 6 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%230B0B0B'/%3E%3Ccircle cx='3.75' cy='3.75' r='0.75' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-spread-large-dark: url("data:image/svg+xml,%3Csvg width='15' height='15' viewBox='0 0 15 15' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1.5' cy='1.5' r='1.5' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-base-small-dark: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-dense-large-light: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1.5' cy='1.5' r='1.5' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-lines-grid-medium-dark: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cg clip-path='url(%23clip0_1361_1234)'%3E%3Cpath d='M0.25 0L0.25 12' stroke='%23ffffff' stroke-width='0.5' /%3E%3Cpath d='M0 0.25H12' stroke='%23ffffff' stroke-width='0.5' /%3E%3C/g%3E%3Cdefs%3E%3CclipPath id='clip0_1361_1234'%3E%3Crect width='12' height='12' fill='white' /%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-base-medium-dark: url("data:image/svg+xml,%3Csvg width='10' height='10' viewBox='0 0 10 10' fill='none' opacity='0.6' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%23ffffff' /%3E%3Ccircle cx='6' cy='6' r='1' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-dense-medium-dark: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' fill='none' opacity='0.6' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%23ffffff' /%3E%3Ccircle cx='5' cy='5' r='1' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-dense-large-dark: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' fill='none' opacity='0.6' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1.5' cy='1.5' r='1.5' fill='%23ffffff' /%3E%3Ccircle cx='7.5' cy='7.5' r='1.5' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-dense-small-dark: url("data:image/svg+xml,%3Csvg width='4' height='4' viewBox='0 0 4 4' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-base-small-dark: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' fill='none' opacity='0.6' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%23ffffff' /%3E%3Ccircle cx='4.75' cy='4.75' r='0.75' fill='%23ffffff' /%3E%3C/svg%3E");
--default-font-family: Waldenburg-75357948a2b6a39b,"Waldenburg-75357948a2b6a39b fallback: Arial",ui-sans-serif,system-ui,sans-serif;
--sanity-id-texture-lines-grid-small-dark: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cg clip-path='url(%23clip0_1361_1244)'%3E%3Cpath d='M0.25 0L0.25 8' stroke='%23ffffff' stroke-width='0.5' /%3E%3Cpath d='M0 0.25H8' stroke='%23ffffff' stroke-width='0.5' /%3E%3C/g%3E%3Cdefs%3E%3CclipPath id='clip0_1361_1244'%3E%3Crect width='8' height='8' fill='white' /%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-base-medium-light: url("data:image/svg+xml,%3Csvg width='10' height='10' viewBox='0 0 10 10' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%230B0B0B'/%3E%3Ccircle cx='6' cy='6' r='1' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-base-small-light: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%230B0B0B'/%3E%3Ccircle cx='4.75' cy='4.75' r='0.75' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-spread-medium-light: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-base-medium-dark: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-grid-dense-medium-light: url("data:image/svg+xml,%3Csvg width='6' height='6' viewBox='0 0 6 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%230B0B0B'/%3E%3C/svg%3E");
--sanity-id-texture-lines-grid-medium-light: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cg clip-path='url(%23clip0_1361_1234)'%3E%3Cpath d='M0.25 0L0.25 12' stroke='%230B0B0B' stroke-width='0.5'/%3E%3Cpath d='M0 0.25H12' stroke='%230B0B0B' stroke-width='0.5'/%3E%3C/g%3E%3Cdefs%3E%3CclipPath id='clip0_1361_1234'%3E%3Crect width='12' height='12' fill='white'/%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-dense-medium-light: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='1' fill='%230B0B0B'/%3E%3Ccircle cx='5' cy='5' r='1' fill='%230B0B0B'/%3E%3C/svg%3E");
--font-weight-semibold: 600;
--sanity-id-texture-dots-grid-dense-large-dark: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1.5' cy='1.5' r='1.5' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-dots-hex-spread-small-dark: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 12 12' fill='none' opacity='0.6' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='0.75' cy='0.75' r='0.75' fill='%23ffffff' /%3E%3Ccircle cx='6.75' cy='6.75' r='0.75' fill='%23ffffff' /%3E%3C/svg%3E");
--sanity-id-texture-lines-horizontal-medium-dark: url("data:image/svg+xml,%3Csvg width='4' height='8' viewBox='0 0 4 8' opacity='0.6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0.25H4' stroke='%23ffffff' stroke-width='0.5' /%3E%3C/svg%3E");
--font-weight-extrabold: 800;
--sanity-id-texture-lines-horizontal-large-light: url("data:image/svg+xml,%3Csvg width='4' height='12' viewBox='0 0 4 12' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0.25H4' stroke='%230B0B0B' stroke-width='0.5'/%3E%3C/svg%3E");
--sanity-id-texture-lines-grid-small-light: url("data:image/svg+xml,%3Csvg width='8' height='8' viewBox='0 0 8 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cg clip-path='url(%23clip0_1361_1244)'%3E%3Cpath d='M0.25 0L0.25 8' stroke='%230B0B0B' stroke-width='0.5'/%3E%3Cpath d='M0 0.25H8' stroke='%230B0B0B' stroke-width='0.5'/%3E%3C/g%3E%3Cdefs%3E%3CclipPath id='clip0_1361_1244'%3E%3Crect width='8' height='8' fill='white'/%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E");
--font-weight-medium: 500;
--font-weight-normal: 400;
--default-mono-font-family: "IBM Plex Mono-c20ba633a65a8c57","IBM Plex Mono-c20ba633a65a8c57 fallback: Courier New",ui-monospace,monospace;
```

### Shadows

```css
--tw-inset-shadow-alpha: 100%;
--tw-inset-shadow: 0 0 #0000;
--tw-shadow-alpha: 100%;
--drop-shadow-lg: 0 4px 4px #00000026;
--tw-drop-shadow-alpha: 100%;
--tw-shadow: 0 0 #0000;
```

### Radii

```css
--radius-none: 0;
--radius-full: 99999px;
```

### Other

```css
--osano-clear-dialog-background: rgba(18,25,35,0);
--osano-dialog-type: box;
--osano-display-position: "bottom-left";
--osano-info-dialog-position: right;
--osano-widget-position: right;
--osano-opt-out-widget-position: left;
--announcement-banner-height: 0px;
--draft-mode-banner-height: 0px;
--navbar-height: 67px;
--header-min-height: calc(var(--navbar-height) + var(--draft-mode-banner-height));
--header-height: calc(var(--navbar-height) + var(--announcement-banner-height) + var(--draft-mode-banner-height));
--gutter: 4px;
--max-width: 1920px;
--default-width: 78rem;
--content-width: min(var(--max-width), calc(100vw - (var(--margin-x-min) * 2)));
--columns-1: calc((var(--content-width) - (var(--gutter) * 11)) / 12);
--columns-2: calc((var(--columns-1) * 2) + (var(--gutter) * 1));
--columns-3: calc((var(--columns-1) * 3) + (var(--gutter) * 2));
--columns-4: calc((var(--columns-1) * 4) + (var(--gutter) * 3));
--columns-5: calc((var(--columns-1) * 5) + (var(--gutter) * 4));
--columns-6: calc((var(--columns-1) * 6) + (var(--gutter) * 5));
--columns-7: calc((var(--columns-1) * 7) + (var(--gutter) * 6));
--columns-8: calc((var(--columns-1) * 8) + (var(--gutter) * 7));
--columns-9: calc((var(--columns-1) * 9) + (var(--gutter) * 8));
--columns-10: calc((var(--columns-1) * 10) + (var(--gutter) * 9));
--columns-11: calc((var(--columns-1) * 11) + (var(--gutter) * 10));
--columns-12: calc((var(--columns-1) * 12) + (var(--gutter) * 11));
--columns-half: calc(var(--columns-1) / 2);
--aspect-video: 16 / 9;
--tw-mask-conic: linear-gradient(#fff, #fff);
--tw-outline-style: solid;
--tw-gradient-from: rgba(0, 0, 0, 0);
--tw-gradient-to: rgba(0, 0, 0, 0);
--blur-2xl: 40px;
--tw-gradient-via-position: 50%;
--tw-mask-right: linear-gradient(#fff, #fff);
--tw-gradient-to-position: 100%;
--default-transition-duration: .15s;
--default-transition-timing-function: cubic-bezier(.4, 0, .2, 1);
--tw-translate-z: 0;
--tw-gradient-via: rgba(0, 0, 0, 0);
--tw-scale-y: 1;
--tw-mask-radial: linear-gradient(#fff, #fff);
--container-3xl: 48rem;
--tw-translate-y: 0;
--ease-out: cubic-bezier(0, 0, .2, 1);
--tw-mask-top: linear-gradient(#fff, #fff);
--tw-content: "";
--tw-translate-x: 0;
--tw-mask-linear: linear-gradient(#fff, #fff);
--animate-caret-blink: caret-blink 1s step-end infinite;
--tw-mask-bottom-to-position: 100%;
--blur-3xl: 64px;
--tw-scale-z: 1;
--tw-scroll-snap-strictness: proximity;
--tw-gradient-from-position: 0%;
--ease-in-out: cubic-bezier(.4, 0, .2, 1);
--blur-md: 12px;
--animate-spin: spin 1s linear infinite;
--tw-mask-left: linear-gradient(#fff, #fff);
--tw-mask-bottom-from-position: 0%;
--container-2xl: 42rem;
--tw-scale-x: 1;
--tw-mask-bottom: linear-gradient(#fff, #fff);
--blur-sm: 8px;
```

### Dependencies

```css
--osano-button-close-color: --osano-dialog-foreground-color;
--osano-button-accept-background-color: --osano-button-background-color;
--osano-button-accept-border-color: --osano-button-border-color,--osano-button-foreground-color;
--osano-button-accept-foreground-color: --osano-button-foreground-color;
--osano-button-deny-border-color: --osano-button-border-color,--osano-button-foreground-color;
--osano-button-reject-all-background-color: --osano-button-background-color;
--osano-button-reject-all-background-color-hover: --osano-button-background-color-hover,--osano-button-background-color-contrast;
--osano-button-reject-all-border-color: --osano-button-border-color,--osano-button-foreground-color;
--osano-button-reject-all-foreground-color: --osano-button-foreground-color;
--osano-button-manage-background-color: --osano-button-background-color;
--osano-button-manage-border-color: --osano-button-border-color,--osano-button-foreground-color;
--osano-button-manage-foreground-color: --osano-button-foreground-color;
--osano-info-dialog-link-color: --osano-link-color;
--osano-info-dialog-button-close-color: --osano-info-dialog-foreground-color,--osano-dialog-foreground-color;
--osano-info-dialog-toggle-off-track-color: --osano-toggle-off-track-color;
--osano-info-dialog-toggle-off-thumb-color: --osano-toggle-off-thumb-color;
--osano-info-dialog-toggle-on-track-color: --osano-toggle-on-track-color;
--osano-info-dialog-toggle-on-thumb-color: --osano-toggle-on-thumb-color;
--osano-info-dialog-button-background-color: --osano-button-background-color;
--osano-info-dialog-button-border-color: --osano-info-dialog-button-foreground-color,--osano-button-foreground-color;
--osano-info-dialog-button-foreground-color: --osano-button-foreground-color;
--osano-dialog-gpc-background-color: --osano-dialog-background-color;
--osano-dialog-gpc-border-color: --osano-dialog-foreground-color;
--osano-dialog-gpc-foreground-color: --osano-dialog-foreground-color;
--osano-info-dialog-gpc-background-color: --osano-info-dialog-background-color,--osano-dialog-background-color;
--osano-info-dialog-gpc-border-color: --osano-info-dialog-foreground-color,--osano-dialog-foreground-color;
--osano-info-dialog-gpc-foreground-color: --osano-info-dialog-foreground-color,--osano-dialog-foreground-color;
--osano-info-dialog-gpc-color: --osano-dialog-gpc-color;
--osano-button-background-color-hover: --osano-button-background-color-contrast;
--osano-button-foreground-color-hover: --osano-button-foreground-color-contrast;
--osano-button-background-color-focus: --osano-button-foreground-color-hover,--osano-button-foreground-color-contrast;
--osano-button-foreground-color-focus: --osano-button-background-color-hover,--osano-button-background-color-contrast;
--osano-toggle-off-track-color-hover: --osano-toggle-off-track-color-contrast;
--osano-toggle-off-thumb-color-hover: --osano-toggle-off-thumb-color-contrast;
--osano-toggle-off-track-color-focus: --osano-toggle-off-thumb-color-hover,--osano-toggle-off-thumb-color-contrast;
--osano-toggle-off-thumb-color-focus: --osano-toggle-off-track-color-hover,--osano-toggle-off-track-color-contrast;
--osano-toggle-on-track-color-hover: --osano-toggle-on-track-color-contrast;
--osano-toggle-on-thumb-color-hover: --osano-toggle-on-thumb-color-contrast;
--osano-toggle-on-track-color-focus: --osano-toggle-on-thumb-color-hover,--osano-toggle-on-thumb-color-contrast;
--osano-toggle-on-thumb-color-focus: --osano-toggle-on-track-color-hover,--osano-toggle-on-track-color-contrast;
--osano-button-accept-background-color-contrast: --osano-button-background-color-contrast;
--osano-button-accept-foreground-color-contrast: --osano-button-foreground-color-contrast;
--osano-button-accept-background-color-hover: --osano-button-background-color-hover,--osano-button-background-color-contrast;
--osano-button-accept-foreground-color-hover: --osano-button-accept-foreground-color-contrast,--osano-button-foreground-color-contrast;
--osano-button-accept-background-color-focus: --osano-button-accept-foreground-color-hover,--osano-button-accept-foreground-color-contrast;
--osano-button-accept-foreground-color-focus: --osano-button-accept-background-color-hover,--osano-button-background-color-hover;
--osano-button-deny-background-color-hover: --osano-button-background-color-hover,--osano-button-background-color-contrast;
--osano-button-deny-foreground-color-hover: --osano-button-deny-foreground-color-contrast;
--osano-button-deny-background-color-focus: --osano-button-deny-foreground-color-hover,--osano-button-deny-foreground-color-contrast;
--osano-button-deny-foreground-color-focus: --osano-button-deny-background-color-hover,--osano-button-background-color-hover;
--osano-button-reject-all-background-color-contrast: --osano-button-background-color-contrast;
--osano-button-reject-all-foreground-color-contrast: --osano-button-foreground-color-contrast;
--osano-button-reject-all-foreground-color-hover: --osano-button-reject-all-foreground-color-contrast,--osano-button-foreground-color-contrast;
--osano-button-reject-all-background-color-focus: --osano-button-reject-all-foreground-color-hover,--osano-button-reject-all-foreground-color-contrast;
--osano-button-reject-all-foreground-color-focus: --osano-button-reject-all-background-color-hover,--osano-button-background-color-hover;
--osano-button-manage-background-color-contrast: --osano-button-background-color-contrast;
--osano-button-manage-foreground-color-contrast: --osano-button-foreground-color-contrast;
--osano-button-manage-background-color-hover: --osano-button-background-color-hover,--osano-button-background-color-contrast;
--osano-button-manage-foreground-color-hover: --osano-button-manage-foreground-color-contrast,--osano-button-foreground-color-contrast;
--osano-button-manage-background-color-focus: --osano-button-manage-foreground-color-hover,--osano-button-manage-foreground-color-contrast;
--osano-button-manage-foreground-color-focus: --osano-button-manage-background-color-hover,--osano-button-background-color-hover;
--osano-info-dialog-button-background-color-contrast: --osano-button-background-color-contrast;
--osano-info-dialog-button-foreground-color-contrast: --osano-button-foreground-color-contrast;
--osano-info-dialog-button-background-color-hover: --osano-button-background-color-hover,--osano-button-background-color-contrast;
--osano-info-dialog-button-foreground-color-hover: --osano-info-dialog-button-foreground-color-contrast,--osano-button-foreground-color-contrast;
--osano-info-dialog-button-background-color-focus: --osano-info-dialog-button-foreground-color-hover,--osano-info-dialog-button-foreground-color-contrast;
--osano-info-dialog-button-foreground-color-focus: --osano-info-dialog-button-background-color-hover,--osano-button-background-color-hover;
--osano-info-dialog-toggle-off-track-color-contrast: --osano-toggle-off-track-color-contrast;
--osano-info-dialog-toggle-off-thumb-color-contrast: --osano-toggle-off-thumb-color-contrast;
--osano-info-dialog-toggle-off-track-color-hover: --osano-info-dialog-toggle-off-track-color-contrast,--osano-toggle-off-track-color-contrast;
--osano-info-dialog-toggle-off-thumb-color-hover: --osano-info-dialog-toggle-off-thumb-color-contrast,--osano-toggle-off-thumb-color-contrast;
--osano-info-dialog-toggle-off-track-color-focus: --osano-info-dialog-toggle-off-thumb-color-hover,--osano-info-dialog-toggle-off-thumb-color-contrast;
--osano-info-dialog-toggle-off-thumb-color-focus: --osano-info-dialog-toggle-off-track-color-hover,--osano-info-dialog-toggle-off-track-color-contrast;
--osano-info-dialog-toggle-off-track-color-disabled: --osano-toggle-off-track-color-disabled;
--osano-info-dialog-toggle-off-thumb-color-disabled: --osano-toggle-off-thumb-color-disabled;
--osano-info-dialog-toggle-on-track-color-contrast: --osano-toggle-on-track-color-contrast;
--osano-info-dialog-toggle-on-thumb-color-contrast: --osano-toggle-on-thumb-color-contrast;
--osano-info-dialog-toggle-on-track-color-hover: --osano-info-dialog-toggle-on-track-color-contrast,--osano-toggle-on-track-color-contrast;
--osano-info-dialog-toggle-on-thumb-color-hover: --osano-info-dialog-toggle-on-thumb-color-contrast,--osano-toggle-on-thumb-color-contrast;
--osano-info-dialog-toggle-on-track-color-focus: --osano-info-dialog-toggle-on-thumb-color-hover,--osano-info-dialog-toggle-on-thumb-color-contrast;
--osano-info-dialog-toggle-on-thumb-color-focus: --osano-info-dialog-toggle-on-track-color-hover,--osano-info-dialog-toggle-on-track-color-contrast;
--osano-info-dialog-toggle-on-track-color-disabled: --osano-toggle-on-track-color-disabled;
--osano-info-dialog-toggle-on-thumb-color-disabled: --osano-toggle-on-thumb-color-disabled;
--osano-info-dialog-link-color-contrast: --osano-link-color-contrast;
--header-min-height: --navbar-height,--draft-mode-banner-height;
--header-height: --navbar-height,--announcement-banner-height,--draft-mode-banner-height;
--margin-x: --margin-x-min,--max-width;
--content-width: --max-width,--margin-x-min;
--columns-1: --content-width,--gutter;
--columns-2: --columns-1,--gutter;
--columns-3: --columns-1,--gutter;
--columns-4: --columns-1,--gutter;
--columns-5: --columns-1,--gutter;
--columns-6: --columns-1,--gutter;
--columns-7: --columns-1,--gutter;
--columns-8: --columns-1,--gutter;
--columns-9: --columns-1,--gutter;
--columns-10: --columns-1,--gutter;
--columns-11: --columns-1,--gutter;
--columns-12: --columns-1,--gutter;
--columns-half: --columns-1;
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
| xs | 376px | min-width |
| md | 768px | min-width |
| 1200px | 1200px | max-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.1s`, `0.2s`, `0s`, `0.4s`, `0.15s`, `0.3s`, `0.5s`, `0.6s`, `1s`

### Common Transitions

```css
transition: all;
transition: transform 0.1s linear, opacity 0.2s linear, visibility linear;
transition: opacity 0.2s, visibility 0s 0.2s;
transition: transform 0.2s ease-out, color 0.2s ease-out, background-color 0.2s ease-out, stroke 0.2s ease-out, stroke-width 0.2s ease-out;
transition: transform 0.4s;
transition: color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
```

### Keyframe Animations

**delay-overflow**
```css
@keyframes delay-overflow {
  0% { overflow: hidden auto; }
}
```

**osano-load-scale**
```css
@keyframes osano-load-scale {
  0% { transform: translate(0px, -50%) scale(0); }
  100% { transform: translate(0px, -50%) scale(1); opacity: 0; }
}
```

**osano-opt-out-honored-exit**
```css
@keyframes osano-opt-out-honored-exit {
  100% { opacity: 0; pointer-events: none; display: none; }
}
```

**live-recording-blink**
```css
@keyframes live-recording-blink {
  0% { opacity: 1; }
  60% { opacity: 0; }
}
```

**spin**
```css
@keyframes spin {
  100% { transform: rotate(360deg); }
}
```

**caret-blink**
```css
@keyframes caret-blink {
  0%, 100% { border-color: currentcolor; }
  50% { border-color: rgba(0, 0, 0, 0); }
}
```

**homepage-customers-countdown**
```css
@keyframes homepage-customers-countdown {
  0% { transform: scaleX(1); }
  100% { transform: scaleX(0); }
}
```

**marquee-scroll**
```css
@keyframes marquee-scroll {
  0% { transform: translate(0px); }
  100% { transform: translate(-50%); }
}
```

**_1b6o2se0**
```css
@keyframes _1b6o2se0 {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (60 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(255, 255, 255);
  font-size: 13px;
  font-weight: 400;
  padding-top: 4px;
  padding-right: 0px;
  border-radius: 99999px;
}
```

### Inputs (8 instances)

```css
.input {
  background-color: rgb(11, 11, 11);
  color: rgb(255, 255, 255);
  border-color: rgb(255, 255, 255);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 12px;
}
```

### Links (141 instances)

```css
.link {
  color: rgb(255, 255, 255);
  font-size: 13px;
  font-weight: 400;
}
```

### Navigation (11 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(11, 11, 11);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(11, 11, 11);
  color: rgb(255, 255, 255);
  padding-top: 24.16px;
  padding-bottom: 24.16px;
  font-size: 16px;
}
```

### Modals (9 instances)

```css
.modal {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 320px;
}
```

### Badges (64 instances)

```css
.badge {
  background-color: rgb(255, 255, 255);
  color: rgb(255, 255, 255);
  font-size: 13px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 12 instances, 3 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(11, 11, 11);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(11, 11, 11);
  font-size: 0px;
  font-weight: 400;
```

**Variant 2** (10 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(185, 185, 185);
  padding: 0px 0px 0px 0px;
  border-radius: 5px;
  border: 0px solid rgb(185, 185, 185);
  font-size: 16px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgb(33, 33, 33);
  color: rgb(11, 11, 11);
  padding: 0px 0px 0px 0px;
  border-radius: 3px;
  border: 0px solid rgb(11, 11, 11);
  font-size: 16px;
  font-weight: 400;
```

### Button — 19 instances, 1 variant

**Variant 1** (19 instances)

```css
  background: rgb(0, 82, 239);
  color: rgb(255, 255, 255);
  padding: 4px 12px 4px 12px;
  border-radius: 99999px;
  border: 1px solid rgb(0, 82, 239);
  font-size: 13px;
  font-weight: 400;
```

### Button — 13 instances, 4 variants

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 4px 12px 4px 12px;
  border-radius: 99999px;
  border: 0px solid rgb(255, 255, 255);
  font-size: 13px;
  font-weight: 400;
```

**Variant 2** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 8px 0px 8px 0px;
  border-radius: 0px;
  border: 0px 0px 1px solid rgb(255, 255, 255);
  font-size: 13px;
  font-weight: 400;
```

**Variant 3** (2 instances)

```css
  background: rgb(33, 33, 33);
  color: rgb(121, 121, 121);
  padding: 0px 12px 0px 12px;
  border-radius: 5px;
  border: 0px solid rgb(121, 121, 121);
  font-size: 13px;
  font-weight: 400;
```

**Variant 4** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(11, 11, 11);
  padding: 4px 0px 4px 0px;
  border-radius: 0px;
  border: 0px solid rgb(11, 11, 11);
  font-size: 13px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 8px 32px 8px 32px;
  border-radius: 99999px;
  border: 1px solid rgb(255, 255, 255);
  font-size: 24px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(185, 185, 185);
  padding: 0px 12px 0px 12px;
  border-radius: 3px;
  border: 0px solid rgb(185, 185, 185);
  font-size: 15px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(11, 11, 11);
  color: rgb(185, 185, 185);
  padding: 8px 12px 8px 12px;
  border-radius: 3px;
  border: 1px solid rgb(33, 33, 33);
  font-size: 15px;
  font-weight: 400;
```

### Button — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(11, 11, 11);
  padding: 8px 8px 8px 8px;
  border-radius: 0px;
  border: 0px solid rgb(11, 11, 11);
  font-size: 13px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(11, 11, 11);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(11, 11, 11);
  font-size: 13px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(255, 255, 255);
  font-size: 13px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: color(display-p3 1 0.3333 0);
  color: rgb(11, 11, 11);
  padding: 24.16px 24.16px 24.16px 24.16px;
  border-radius: 99999px;
  border: 0px solid color(display-p3 1 0.3333 0);
  font-size: 60px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(33, 33, 33);
  color: rgb(255, 255, 255);
  padding: 4px 16px 4px 12px;
  border-radius: 99999px;
  border: 1px solid rgb(33, 33, 33);
  font-size: 13px;
  font-weight: 400;
```

## Layout System

**24 grid containers** and **435 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 320px | 24px |
| 100% | 0px |
| 1166.59px | 0px |
| 833.28px | 0px |
| 90% | 0px |
| 1296px | 24px |
| 1920px | 0px |
| 1680px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 11x |
| 2-column | 5x |
| 3-column | 3x |
| 12-column | 3x |
| 4-column | 2x |

### Grid Templates

```css
grid-template-columns: 99px 99px 99px 99px 99px 99px 99px 99px 99px 99px 99px 99px;
gap: normal 4px;
grid-template-columns: 410.562px 410.562px 410.562px;
grid-template-columns: 426.656px 426.672px 426.656px;
grid-template-columns: 177.453px 177.453px 177.453px 177.469px;
gap: 24.16px;
grid-template-columns: 304.922px 304.922px 304.922px 304.922px;
gap: 4px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row-reverse/nowrap | 4x |
| row/nowrap | 327x |
| column/nowrap | 99x |
| row/wrap | 4x |
| column/wrap | 1x |

**Gap values:** `0px normal`, `12px`, `12px normal`, `16px`, `16px 8px`, `16px normal`, `24.16px`, `24.16px 48px`, `24.16px normal`, `2px`, `32px 24.16px`, `48px`, `48px normal`, `4px`, `4px normal`, `6px`, `8px`, `8px normal`, `normal 12px`, `normal 16px`, `normal 24.16px`, `normal 2px`, `normal 48px`, `normal 4px`, `normal 6px`, `normal 8px`

## Accessibility (WCAG 2.1)

**Overall Score: 96%** — 22 passing, 1 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#797979` | `#212121` | 3.7:1 | FAIL | button (1x) |

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#0b0b0b` | 19.68:1 | AAA |
| `#0b0b0b` | `#ffffff` | 19.68:1 | AAA |
| `#ffffff` | `#212121` | 16.1:1 | AAA |
| `#ffffff` | `#0052ef` | 6.08:1 | AA |
| `#b9b9b9` | `#212121` | 8.21:1 | AAA |

## Design System Score

**Overall: 89/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 80/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 96/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 1 WCAG contrast failures
- 283 !important rules — prefer specificity over overrides
- 3230 duplicate CSS declarations

## Z-Index Map

**11 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 2147483636,2147483638 | button.o.s.a.n.o.-.c.m.-.w.i.n.d.o.w._._.w.i.d.g.e.t. .o.s.a.n.o.-.c.m.-.w.i.d.g.e.t. .o.s.a.n.o.-.c.m.-.w.i.d.g.e.t.-.-.h.i.d.d.e.n. .o.s.a.n.o.-.c.m.-.w.i.d.g.e.t.-.-.p.o.s.i.t.i.o.n._.r.i.g.h.t, div.o.s.a.n.o.-.c.m.-.w.i.n.d.o.w, div.o.s.a.n.o.-.c.m.-.w.i.n.d.o.w._._.i.n.f.o.-.d.i.a.l.o.g. .o.s.a.n.o.-.c.m.-.i.n.f.o.-.d.i.a.l.o.g. .o.s.a.n.o.-.c.m.-.i.n.f.o.-.d.i.a.l.o.g.-.-.h.i.d.d.e.n |
| dropdown | 200,200 | header.h.e.a.d.e.r. .e.a.s.e.-.i.n.-.o.u.t. .t.r.a.n.s.i.t.i.o.n.-.c.o.l.o.r.s. .s.t.i.c.k.y. .t.o.p.-.0. .z.-.2.0.0. .b.o.x.-.b.o.r.d.e.r. .f.l.e.x. .h.-.(.-.-.n.a.v.b.a.r.-.h.e.i.g.h.t.). .i.t.e.m.s.-.c.e.n.t.e.r. .b.g.-.b.g.-.b.a.s.e. .p.x.-.m.a.r.g.i.n.-.x. .d.u.r.a.t.i.o.n.-.2.0.0 |
| sticky | 10,50 | div.p.x.-.m.a.r.g.i.n.-.x. .r.e.l.a.t.i.v.e. .z.-.1.0, div.a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .z.-.1.0. .c.u.r.s.o.r.-.p.o.i.n.t.e.r. .t.o.u.c.h.-.p.a.n.-.x, div.a.b.s.o.l.u.t.e. .i.n.s.e.t.-.0. .z.-.1.0. .c.u.r.s.o.r.-.p.o.i.n.t.e.r. .t.o.u.c.h.-.p.a.n.-.x |
| base | -10,5 | div.w.-.s.c.r.e.e.n. .h.-.s.c.r.e.e.n. .a.b.s.o.l.u.t.e. .t.o.p.-.0. .-.z.-.1.0. .b.g.-.b.l.a.c.k. .o.p.a.c.i.t.y.-.2.0. .p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e, img.a.b.s.o.l.u.t.e. .t.o.p.-.0. .l.e.f.t.-.0. .-.z.-.1.0. .h.-.f.u.l.l. .w.-.f.u.l.l. .d.a.r.k.:.h.i.d.d.e.n, img.a.b.s.o.l.u.t.e. .t.o.p.-.0. .l.e.f.t.-.0. .-.z.-.1.0. .h.-.f.u.l.l. .w.-.f.u.l.l. .l.i.g.h.t.:.h.i.d.d.e.n |

**Issues:**
- [object Object]

## SVG Icons

**27 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 6 |
| sm | 3 |
| md | 17 |
| xl | 1 |

**Icon colors:** `currentColor`, `rgb(0, 0, 0)`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Waldenburg-75357948a2b6a39b | self-hosted | 400, 600 | normal, italic |
| IBM Plex Mono-c20ba633a65a8c57 | self-hosted | 400, 700 | normal, italic |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 63 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 10 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 5 | objectFit: contain, borderRadius: 0px, shape: square |
| avatar | 3 | objectFit: fill, borderRadius: 99999px, shape: circular |
| general | 1 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (16x), 4:3 (6x), 16:9 (5x), 21:9 (5x), 3:4 (5x), 2.94:1 (4x), 2.09:1 (4x), 2.72:1 (4x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **linear** (16 uses) — `linear`
- **ease-in-out** (2 uses) — `ease`
- **custom** (97 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `delay-overflow` | custom | overflow | 1 |
| `homepage-customers-countdown` | scale | transform | 1 |
| `marquee-scroll` | slide | transform | 1 |

## Component Anatomy

### button — 53 instances

**Slots:** label, icon
**Variants:** outline
**Sizes:** sm · md · xs · lg

| variant | count | sample label |
|---|---|---|
| default | 52 | Close Cookie Preferences |
| outline | 1 | Run Release |

### input — 2 instances

**Variants:** outline
**Sizes:** md

## Brand Voice

**Tone:** neutral · **Pronoun:** you-only · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **contact** (2)
- **get** (2)
- **create** (2)
- **book** (2)
- **how** (2)
- **content** (2)
- **sanity** (2)
- **close** (1)

### Button Copy Patterns

- "contact sales" (2×)
- "npm create sanity@latest" (2×)
- "book a demo" (2×)
- "close cookie preferences" (1×)
- "skip to content" (1×)
- "products" (1×)
- "solutions" (1×)
- "resources" (1×)
- "docs" (1×)
- "enterprise" (1×)

### Sample Headings

> The Content Operations Platform
> Mirror how your content operations team works
> Page title
> Content Operations without the busywork
> Power anything. One API, every platform
> The Content Operations Platform
> Mirror how your content operations team works
> Page title
> Content Operations without the busywork
> Power anything. One API, every platform

## Page Intent

**Type:** `landing` (confidence 0.27)
**Description:** Sanity is the back-end built for AI content operations. Power web, mobile, and agentic applications at scale.

Alternates: docs (0.45), blog-post (0.35)

## Section Roles

Reading order (top→bottom): cta → nav → pricing-table → logo-wall → pricing-table → testimonials → nav → nav → nav → nav → nav → nav → testimonials → cta → feature-grid → feature-grid → feature-grid → feature-grid → feature-grid → feature-grid → pricing-table → feature-grid → cta → footer → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | cta | — | 0.75 |
| 1 | nav | — | 0.9 |
| 2 | pricing-table | The Content Operations Platform | 0.9 |
| 3 | logo-wall | The Content Operations Platform | 0.85 |
| 4 | pricing-table | — | 0.9 |
| 5 | testimonials | Mirror how your content operations team works | 0.4 |
| 6 | nav | — | 0.4 |
| 7 | nav | — | 0.9 |
| 8 | nav | — | 0.9 |
| 9 | nav | — | 0.9 |
| 10 | nav | — | 0.4 |
| 11 | nav | — | 0.4 |
| 12 | testimonials | Content Operations without the busywork | 0.4 |
| 13 | cta | Power anything. One API, every platform | 0.75 |
| 14 | feature-grid | Everything your team needs in one place | 0.8 |
| 15 | feature-grid | The database optimized for content operations | 0.8 |
| 16 | feature-grid | Content workflows that mirror how you work | 0.8 |
| 17 | feature-grid | An agent to run content operations at scale | 0.8 |
| 18 | feature-grid | Programmable automation | 0.8 |
| 19 | feature-grid | Power web, mobile, or your own agent | 0.8 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.276 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 99999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.061)
**Counts:** total 82, svg 0, icon 12, screenshot-like 0, photo-like 10
**Dominant aspect:** ultra-wide
**Radius profile on images:** rounded

## Component Library

**Detected:** `tailwindcss` (confidence 0.704)

Evidence:
- tailwind-like class density 69%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Waldenburg-75357948a2b6a39b` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
