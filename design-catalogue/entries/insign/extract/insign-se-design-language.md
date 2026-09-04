# Design Language: Insign Fullservicebyrå - Sveriges högst rankade webbyrå

> Extracted from `https://www.insign.se` on September 4, 2026
> 2641 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#ff7f4c` | rgb(255, 127, 76) | hsl(17, 100%, 65%) | 5 |
| Secondary | `#008000` | rgb(0, 128, 0) | hsl(120, 100%, 25%) | 8 |
| Accent | `#0073aa` | rgb(0, 115, 170) | hsl(199, 100%, 33%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 4147 |
| `#1a1819` | hsl(330, 4%, 10%) | 569 |
| `#ffffff` | hsl(0, 0%, 100%) | 303 |
| `#828282` | hsl(0, 0%, 51%) | 184 |
| `#181d27` | hsl(220, 24%, 12%) | 94 |
| `#8c8c8c` | hsl(0, 0%, 55%) | 37 |
| `#ecf1f7` | hsl(213, 41%, 95%) | 23 |
| `#c6c6c6` | hsl(0, 0%, 78%) | 14 |
| `#334155` | hsl(215, 25%, 27%) | 12 |
| `#414651` | hsl(221, 11%, 29%) | 11 |
| `#4b5563` | hsl(215, 14%, 34%) | 10 |
| `#d4dae3` | hsl(216, 21%, 86%) | 8 |

### Background Colors

Used on large-area elements: `#ffffff`, `#1a1819`, `#222222`, `#eaf585`, `#dac6fb`, `#ff7f4c`, `#eef1f5`, `#ecf1f7`

### Text Colors

Text color palette: `#000000`, `#1a1819`, `#008000`, `#ffffff`, `#f7f7f7`, `#0a0a0a`, `#111111`, `#0b161e`, `#eaf585`, `#007aff`

### Gradients

```css
background-image: linear-gradient(-45deg, rgba(255, 255, 255, 0.4) 25%, rgba(0, 0, 0, 0) 0px, rgba(0, 0, 0, 0) 50%, rgba(255, 255, 255, 0.4) 0px, rgba(255, 255, 255, 0.4) 75%, rgba(0, 0, 0, 0) 0px, rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(rgba(26, 24, 25, 0.86) 0%, rgba(26, 24, 25, 0.86) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 4147 |
| `#1a1819` | text, border, background | 569 |
| `#ffffff` | background, text, border | 303 |
| `#828282` | text, border | 184 |
| `#181d27` | background, text, border | 94 |
| `#8c8c8c` | text, border | 37 |
| `#ecf1f7` | border, background | 23 |
| `#c6c6c6` | text, border, background | 14 |
| `#334155` | text, border | 12 |
| `#0b161e` | background, text, border | 11 |
| `#414651` | text, border | 11 |
| `#4b5563` | text, border | 10 |
| `#e3e8ef` | border, background | 9 |
| `#008000` | text, border | 8 |
| `#d4dae3` | border, background | 8 |
| `#666c76` | text, border | 6 |
| `#ff7f4c` | background | 5 |
| `#333333` | border, background | 4 |
| `#007aff` | text, border | 4 |
| `#0a0a0a` | text, border | 2 |
| `#eaf585` | background, text | 2 |
| `#0073aa` | background | 1 |
| `#dac6fb` | background | 1 |
| `#fff300` | border | 1 |

## Typography

### Font Families

- **Neue Haas Grotesk RoundDots - 55 Roman** — used for all (1975 elements)
- **Times New Roman** — used for body (105 elements)
- **Helvetica** — used for all (41 elements)
- **Neue Haas Grotesk RoundDots - 45 Light** — used for headings (5 elements)
- **none** — used for body (1 elements)
- **ETmodules** — used for body (1 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 80px | 5rem | 400 | 80px | normal | div, span |
| 76.8px | 4.8rem | 400 | 76.8px | 1.3px | h1 |
| 67.2px | 4.2rem | 400 | 73.92px | 0.6px | h2 |
| 50px | 3.125rem | 400 | 24px | normal | div |
| 40px | 2.5rem | 400 | 48px | 0.6px | h3 |
| 36px | 2.25rem | 400 | 54px | normal | div |
| 30px | 1.875rem | 400 | normal | normal | span, svg, path |
| 28px | 1.75rem | 400 | 33.6px | 0.6px | h4, span |
| 20px | 1.25rem | 400 | 20px | normal | div, svg, path, h5 |
| 18px | 1.125rem | 400 | 21.6px | 1px | h4, span |
| 17px | 1.0625rem | 500 | 28.9px | normal | a, h6 |
| 16px | 1rem | 400 | normal | normal | html, head, meta, style |
| 15px | 0.9375rem | 500 | 24px | normal | div, button, a, p |
| 14px | 0.875rem | 400 | 21px | normal | div, p, span, a |
| 13.3333px | 0.8333rem | 400 | normal | normal | input, button, span, svg |

### Heading Scale

```css
h1 { font-size: 76.8px; font-weight: 400; line-height: 76.8px; }
h2 { font-size: 67.2px; font-weight: 400; line-height: 73.92px; }
h3 { font-size: 40px; font-weight: 400; line-height: 48px; }
h4 { font-size: 28px; font-weight: 400; line-height: 33.6px; }
h5 { font-size: 20px; font-weight: 400; line-height: 20px; }
h4 { font-size: 18px; font-weight: 400; line-height: 21.6px; }
h6 { font-size: 17px; font-weight: 500; line-height: 28.9px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (2432x), `500` (162x), `600` (41x), `10` (3x), `700` (1x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-12 | 12px | 0.75rem |
| spacing-14 | 14px | 0.875rem |
| spacing-20 | 20px | 1.25rem |
| spacing-22 | 22px | 1.375rem |
| spacing-24 | 24px | 1.5rem |
| spacing-29 | 29px | 1.8125rem |
| spacing-32 | 32px | 2rem |
| spacing-36 | 36px | 2.25rem |
| spacing-40 | 40px | 2.5rem |
| spacing-46 | 46px | 2.875rem |
| spacing-50 | 50px | 3.125rem |
| spacing-67 | 67px | 4.1875rem |
| spacing-78 | 78px | 4.875rem |
| spacing-80 | 80px | 5rem |
| spacing-83 | 83px | 5.1875rem |
| spacing-100 | 100px | 6.25rem |
| spacing-178 | 178px | 11.125rem |
| spacing-267 | 267px | 16.6875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 1px | 1 |
| sm | 4px | 2 |
| md | 8px | 77 |
| lg | 12px | 3 |
| xl | 20px | 10 |
| full | 40px | 1 |
| full | 50px | 16 |
| full | 75px | 1 |
| full | 100px | 69 |
| full | 160px | 1 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgb(26, 24, 25) 0px 0px 0px 1px;
```

**sm** — blur: 0px
```css
box-shadow: rgb(65, 70, 81) 0px 0px 0px 1px;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgba(10, 13, 18, 0.18) 0px 0px 0px 1px inset, rgba(10, 13, 18, 0.05) 0px -2px 0px 0px inset, rgba(10, 13, 18, 0.05) 0px 1px 2px 0px;
```

**xs** — blur: 2px
```css
box-shadow: rgba(10, 13, 18, 0.05) 0px 1px 2px 0px;
```

**sm** — blur: 5px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 2px 5px 0px;
```

**sm** — blur: 4px
```css
box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 4px 0px;
```

**sm** — blur: 4px
```css
box-shadow: rgba(0, 0, 0, 0.02) 0px 4px 4px 0px;
```

**lg** — blur: 20px
```css
box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px 0px, rgba(0, 0, 0, 0.23) 0px 6px 6px 0px;
```

**xl** — blur: 60px
```css
box-shadow: rgba(0, 0, 0, 0.2) 2px 8px 60px -2px;
```

## CSS Custom Properties

### Colors

```css
--wp--preset--color--black: #000000;
--wp--preset--color--cyan-bluish-gray: #abb8c3;
--wp--preset--color--white: #ffffff;
--wp--preset--color--pale-pink: #f78da7;
--wp--preset--color--vivid-red: #cf2e2e;
--wp--preset--color--luminous-vivid-orange: #ff6900;
--wp--preset--color--luminous-vivid-amber: #fcb900;
--wp--preset--color--light-green-cyan: #7bdcb5;
--wp--preset--color--vivid-green-cyan: #00d084;
--wp--preset--color--pale-cyan-blue: #8ed1fc;
--wp--preset--color--vivid-cyan-blue: #0693e3;
--wp--preset--color--vivid-purple: #9b51e0;
--dipi-vb-module-selection-icon-color: #ffffff;
--dipi-vb-module-selection-text-color: #ffffff;
--dipi-vb-module-selection-background-color: #232931;
--dipi-vb-module-selection-border-color: #40464f;
--cmplz_banner_background_color: #ffffff;
--cmplz_banner_border_color: #f2f2f2;
--cmplz_banner_border_width: 0px 0px 0px 0px;
--cmplz_banner_border_radius: 20px 20px 20px 20px;
--cmplz_text_color: #1a1819;
--cmplz_hyperlink_color: #1a1819;
--cmplz_button_accept_background_color: #1a1819;
--cmplz_button_accept_border_color: #1a1819;
--cmplz_button_accept_text_color: #ffffff;
--cmplz_button_deny_background_color: #ffffff;
--cmplz_button_deny_border_color: #1a1819;
--cmplz_button_deny_text_color: #1a1819;
--cmplz_button_settings_background_color: #ffffff;
--cmplz_button_settings_border_color: #1a1819;
--cmplz_button_settings_text_color: #1a1819;
--cmplz_button_border_radius: 50px 50px 50px 50px;
--cmplz_category_header_always_active_color: green;
--cmplz_slider_active_color: #1a1819;
--cmplz_slider_inactive_color: #fba861;
--cmplz_slider_bullet_color: #ffffff;
--swiper-theme-color: #007aff;
```

### Spacing

```css
--wp--preset--font-size--small: 13px;
--wp--preset--font-size--medium: 20px;
--wp--preset--font-size--large: 36px;
--wp--preset--font-size--x-large: 42px;
--wp--preset--spacing--20: 0.44rem;
--wp--preset--spacing--30: 0.67rem;
--wp--preset--spacing--40: 1rem;
--wp--preset--spacing--50: 1.5rem;
--wp--preset--spacing--60: 2.25rem;
--wp--preset--spacing--70: 3.38rem;
--wp--preset--spacing--80: 5.06rem;
--wp--style--global--content-size: 823px;
--wp--style--global--wide-size: 1080px;
--cmplz_banner_margin: 10px;
--cmplz_title_font_size: 15px;
--cmplz_text_font_size: 14px;
--cmplz_link_font_size: 14px;
--cmplz_category_body_font_size: 14px;
--cmplz_button_font_size: 15px;
--cmplz_category_header_title_font_size: 14px;
--cmplz_category_header_active_font_size: 12px;
--swiper-navigation-size: 44px;
```

### Typography

```css
--background-text-content: "";
--cmplz_text_line_height: calc(var(--cmplz_text_font_size) * 1.5);
```

### Shadows

```css
--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);
--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);
--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);
--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);
--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);
```

### Other

```css
--wp--preset--aspect-ratio--square: 1;
--wp--preset--aspect-ratio--4-3: 4/3;
--wp--preset--aspect-ratio--3-4: 3/4;
--wp--preset--aspect-ratio--3-2: 3/2;
--wp--preset--aspect-ratio--2-3: 2/3;
--wp--preset--aspect-ratio--16-9: 16/9;
--wp--preset--aspect-ratio--9-16: 9/16;
--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);
--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);
--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);
--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);
--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);
--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);
--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);
--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);
--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);
--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);
--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);
--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);
--dipi-ig-popup-speed: 500ms;
--cmplz_banner_width: 526px;
--cmplz_categories-height: 163px;
--cmplz-manage-consent-height: 50px;
--cmplz-manage-consent-offset: -35px;
```

### Dependencies

```css
--cmplz_text_line_height: --cmplz_text_font_size;
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
| xs | 320px | min-width |
| xs | 350px | min-width |
| 399px | 399px | max-width |
| sm | 420px | max-width |
| sm | 425px | max-width |
| sm | 479px | max-width |
| sm | 480px | max-width |
| sm | 481px | max-width |
| sm | 576px | min-width |
| sm | 600px | max-width |
| md | 767px | max-width |
| md | 768px | max-width |
| md | 782px | max-width |
| md | 800px | max-width |
| 900px | 900px | max-width |
| lg | 980px | max-width |
| lg | 981px | min-width |
| lg | 992px | min-width |
| 1725px | 1725px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.5s`, `0.4s`, `0.15s`, `0.275s`, `0.2s`, `0.3s`, `0.1s`, `4.001s`, `1s`, `0.6s`, `0.75s`, `0.35s`

### Common Transitions

```css
transition: all;
transition: 0.5s;
transition: background-color 0.4s, color 0.4s, transform 0.4s, opacity 0.4s ease-in-out, -webkit-transform 0.4s;
transition: 0.4s ease-in-out;
transition: opacity 0.4s ease-in-out, background-color 0.4s ease-in-out;
transition: opacity 0.15s linear, filter 0.15s linear;
transition: transform 0.275s cubic-bezier(0.68, -0.55, 0.265, 1.55);
transition: opacity 0.2s ease-in-out, background-color 0.2s ease-in-out;
transition: display 0.3s;
transition: 0.15s ease-in;
```

### Keyframe Animations

**scale**
```css
@keyframes scale {
  0%, 80% { transform: scale(1); opacity: 1; }
  45% { transform: scale(0.1); opacity: 0.7; }
}
```

**scale**
```css
@keyframes scale {
  0%, 80% { transform: scale(1); opacity: 1; }
  45% { transform: scale(0.1); opacity: 0.7; }
}
```

**ball-pulse-sync**
```css
@keyframes ball-pulse-sync {
  33% { transform: translateY(10px); }
  66% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}
```

**ball-pulse-sync**
```css
@keyframes ball-pulse-sync {
  33% { transform: translateY(10px); }
  66% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}
```

**ball-scale**
```css
@keyframes ball-scale {
  0% { transform: scale(0); }
  100% { transform: scale(1); opacity: 0; }
}
```

**ball-scale**
```css
@keyframes ball-scale {
  0% { transform: scale(0); }
  100% { transform: scale(1); opacity: 0; }
}
```

**rotate**
```css
@keyframes rotate {
  0% { transform: rotate(0deg); }
  50% { transform: rotate(180deg); }
  100% { transform: rotate(360deg); }
}
```

**rotate**
```css
@keyframes rotate {
  0% { transform: rotate(0deg); }
  50% { transform: rotate(180deg); }
  100% { transform: rotate(360deg); }
}
```

**scale**
```css
@keyframes scale {
  30% { transform: scale(0.3); }
  100% { transform: scale(1); }
}
```

**rotate**
```css
@keyframes rotate {
  0% { transform: rotate(0deg) scale(1); }
  50% { transform: rotate(180deg) scale(0.6); }
  100% { transform: rotate(360deg) scale(1); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (124 instances)

```css
.button {
  background-color: rgba(255, 255, 255, 0);
  color: rgb(17, 17, 17);
  font-size: 14px;
  font-weight: 500;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (9 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 20px;
  box-shadow: rgba(0, 0, 0, 0.02) 0px 4px 4px 0px;
  padding-top: 24px;
  padding-right: 24px;
}
```

### Inputs (12 instances)

```css
.input {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  border-color: rgb(0, 0, 0);
  border-radius: 0px;
  font-size: 13.3333px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (347 instances)

```css
.link {
  color: rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
}
```

### Navigation (13 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
  box-shadow: rgba(0, 0, 0, 0.2) 2px 8px 60px -2px;
}
```

### Footer (26 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (286 instances)

```css
.modal {
  background-color: rgba(10, 0, 0, 0.45);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px 0px, rgba(0, 0, 0, 0.23) 0px 6px 6px 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 100%;
}
```

### Dropdowns (25 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 2px 5px 0px;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Switches (17 instances)

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
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 5 instances, 3 variants

**Variant 1** (2 instances)

```css
  background: rgb(26, 24, 25);
  color: rgb(255, 255, 255);
  padding: 10px 10px 10px 10px;
  border-radius: 50px;
  border: 1px solid rgb(26, 24, 25);
  font-size: 15px;
  font-weight: 500;
```

**Variant 2** (2 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(26, 24, 25);
  padding: 10px 10px 10px 10px;
  border-radius: 50px;
  border: 1px solid rgb(26, 24, 25);
  font-size: 15px;
  font-weight: 500;
```

**Variant 3** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 16px;
  font-weight: 400;
```

### Button — 7 instances, 1 variant

**Variant 1** (7 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 33 instances, 5 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(26, 24, 25);
  padding: 3px 20px 3px 40px;
  border-radius: 100px;
  border: 1px solid rgb(26, 24, 25);
  font-size: 15px;
  font-weight: 500;
```

**Variant 2** (4 instances)

```css
  background: rgb(26, 24, 25);
  color: rgb(234, 245, 133);
  padding: 4.8px 30px 4.8px 30px;
  border-radius: 100px;
  border: 1px solid rgb(26, 24, 25);
  font-size: 16px;
  font-weight: 500;
```

**Variant 3** (18 instances)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(26, 24, 25);
  padding: 0px 0px 0px 24px;
  border-radius: 100px;
  border: 0px solid rgb(26, 24, 25);
  font-size: 15px;
  font-weight: 500;
```

**Variant 4** (4 instances)

```css
  background: rgb(255, 127, 76);
  color: rgb(26, 24, 25);
  padding: 0px 0px 0px 24px;
  border-radius: 100px;
  border: 0px solid rgb(26, 24, 25);
  font-size: 15px;
  font-weight: 500;
```

**Variant 5** (6 instances)

```css
  background: rgba(255, 255, 255, 0);
  color: rgb(255, 255, 255);
  padding: 4.5px 20px 4.5px 24px;
  border-radius: 100px;
  border: 1px solid rgb(255, 255, 255);
  font-size: 15px;
  font-weight: 500;
```

### Button — 32 instances, 1 variant

**Variant 1** (32 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 10px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
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
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 2px solid rgba(0, 0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(211, 203, 203, 0.2);
  color: rgb(255, 255, 255);
  padding: 8px 14px 8px 8px;
  border-radius: 160px;
  border: 0px none rgb(255, 255, 255);
  font-size: 13.3333px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0.1);
  color: rgb(255, 255, 255);
  padding: 8px 8px 8px 8px;
  border-radius: 75px;
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 15px;
  font-weight: 400;
```

### Button — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(26, 24, 25);
  color: rgb(26, 24, 25);
  padding: 0px 0px 0px 0px;
  border-radius: 100px;
  border: 0px none rgb(26, 24, 25);
  font-size: 16px;
  font-weight: 400;
```

### Button — 21 instances, 1 variant

**Variant 1** (21 instances)

```css
  background: rgb(248, 250, 252);
  color: rgb(0, 0, 0);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(248, 250, 252);
  color: rgb(0, 0, 0);
  padding: 24px 24px 24px 24px;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

## Layout System

**6 grid containers** and **312 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 20px |
| 2560px | 0px |
| 1800px | 0px |
| 832px | 0px |
| 1000px | 0px |
| 1900px | 0px |
| 1500px | 0px |
| 580px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 6x |

### Grid Templates

```css
grid-template-columns: 155.328px 155.328px 155.328px;
gap: 10px;
grid-template-columns: 100px 286px 100px;
grid-template-columns: 1fr auto 15px;
gap: 10px;
grid-template-columns: 1fr auto 15px;
gap: 10px;
grid-template-columns: 1fr auto 15px;
gap: 10px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 115x |
| column/wrap | 5x |
| column/nowrap | 63x |
| row/wrap | 47x |
| row-reverse/wrap | 82x |

**Gap values:** `10px`, `14px`, `15px`, `16px`, `46px`, `4px`, `8px`, `normal 10px`

## Interaction States

### Button States

**"Acceptera"**
```css
/* Focus */
outline: rgb(255, 255, 255) none 3px → rgb(255, 255, 255) none 0px;
```

**"Neka"**
```css
/* Focus */
outline: rgb(26, 24, 25) none 3px → rgb(26, 24, 25) none 0px;
```

**"Visa preferenser"**
```css
/* Focus */
outline: rgb(26, 24, 25) none 3px → rgb(26, 24, 25) none 0px;
```

### Link Hover

```css
background-color: rgba(0, 0, 0, 0) → rgba(0, 0, 0, 0.004);
```

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 18 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#1a1819` | 17.67:1 | AAA |
| `#1a1819` | `#ffffff` | 17.67:1 | AAA |
| `#1a1819` | `#ff7f4c` | 7.06:1 | AAA |
| `#414651` | `#ffffff` | 9.46:1 | AAA |
| `#eaf585` | `#1a1819` | 15.06:1 | AAA |

## Design System Score

**Overall: 79/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 50/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 90/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 6 font families — consider limiting to 2 (heading + body)
- 2908 !important rules — prefer specificity over overrides
- 88% of CSS is unused — consider purging
- 12212 duplicate CSS declarations

## Gradients

**2 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 8 | complex |
| linear | — | 2 | brand |

```css
background: linear-gradient(-45deg, rgba(255, 255, 255, 0.4) 25%, rgba(0, 0, 0, 0) 0px, rgba(0, 0, 0, 0) 50%, rgba(255, 255, 255, 0.4) 0px, rgba(255, 255, 255, 0.4) 75%, rgba(0, 0, 0, 0) 0px, rgba(0, 0, 0, 0));
background: linear-gradient(rgba(26, 24, 25, 0.86) 0%, rgba(26, 24, 25, 0.86) 100%);
```

## Z-Index Map

**16 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9998,2147483647 | button.c.m.p.l.z.-.b.t.n. .c.m.p.l.z.-.m.a.n.a.g.e.-.c.o.n.s.e.n.t. .m.a.n.a.g.e.-.c.o.n.s.e.n.t.-.1. .c.m.p.l.z.-.d.i.s.m.i.s.s.e.d, ul.s.u.b.-.m.e.n.u, ul.e.t._.m.o.b.i.l.e._.m.e.n.u |
| dropdown | 999,999 | div.a.c.c.e.s.s.i.b.i.l.i.t.y.-.s.t.a.t.u.s.-.t.e.x.t, div.b.o.x.-.h.i.d.e.-.d.u.r.a.t.i.o.n, div.o.n.e.t.a.p.-.b.o.x.-.f.u.n.c.t.i.o.n.s |
| sticky | 10,99 | span.m.e.j.s.-.t.i.m.e.-.h.o.v.e.r.e.d. .n.o.-.h.o.v.e.r, div.s.w.i.p.e.r.-.b.u.t.t.o.n.-.n.e.x.t. .s.w.i.p.e.r.-.a.r.r.o.w.-.b.u.t.t.o.n. .d.i.p.i.-.s.b.n.0, div.s.w.i.p.e.r.-.b.u.t.t.o.n.-.p.r.e.v. .s.w.i.p.e.r.-.a.r.r.o.w.-.b.u.t.t.o.n. .d.i.p.i.-.s.b.p.0 |
| base | -1000,3 | span.s.w.i.p.e.r.-.n.o.t.i.f.i.c.a.t.i.o.n, div.e.t._.p.b._.s.e.c.t.i.o.n. .e.t._.p.b._.s.e.c.t.i.o.n._.1. .e.t._.p.b._.s.t.i.c.k.y._.m.o.d.u.l.e. .e.t._.p.b._.s.e.c.t.i.o.n._.v.i.d.e.o. .e.t._.p.b._.w.i.t.h._.b.a.c.k.g.r.o.u.n.d. .e.t._.s.e.c.t.i.o.n._.r.e.g.u.l.a.r, div.m.e.j.s.-.m.e.d.i.a.e.l.e.m.e.n.t |

**Issues:**
- [object Object]

## SVG Icons

**26 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 1 |
| md | 1 |
| xl | 23 |

**Icon colors:** `currentColor`, `rgb(0, 0, 0)`, `rgb(255, 255, 255)`, `#FFFFFF`, `rgb(26, 24, 25)`, `white`, `rgb(17, 17, 17)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Neue Haas Grotesk RoundDots - 55 Roman | self-hosted | 400, normal | normal |
| OpenDyslexic | self-hosted | 400, 700, 900 | normal, italic |
| Roboto | self-hosted | 100, 300, 400, 500, 700, 900 | normal, italic |
| divipixel | self-hosted | normal | normal |
| FontAwesome | self-hosted | 400, 900 | normal |
| ETmodules | self-hosted | 400 | normal |
| Neue Haas Grotesk RoundDots - 45 Light | self-hosted | 400, normal | normal |
| swiper-icons | self-hosted | 400 | normal |
| Open Sans | google-fonts | 300, 400, 500, 600, 700, 800 | italic, normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 40 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 5 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 2 | objectFit: fill, borderRadius: 0px, shape: square |
| avatar | 1 | objectFit: fill, borderRadius: 50%, shape: circular |

**Aspect ratios:** 2.75:1 (33x), 3:2 (7x), 1:1 (6x), 3.92:1 (1x), 16:9 (1x)

## Motion Language

**Feel:** springy · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `275ms` | 275 |
| `lg` | `500ms` | 500 |
| `xl` | `750ms` | 750 |
| `xxl` | `4.001s` | 4001.0000000000005 |

### Easing Families

- **ease-in-out** (121 uses) — `ease`
- **linear** (2 uses) — `linear`
- **spring** (1 uses) — `cubic-bezier(0.68, -0.55, 0.265, 1.55)`
- **ease-in** (1 uses) — `cubic-bezier(0.44, 0, 1, 1)`
- **custom** (33 uses) — `cubic-bezier(0.2, 0, 0.3, 1)`
- **ease-out** (1 uses) — `cubic-bezier(0.23, 1, 0.32, 1)`

### Spring / Overshoot Easings

- `cubic-bezier(0.68, -0.55, 0.265, 1.55)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `ball-scale-multiple` | reveal | transform, opacity | 6 |
| `ball-scale-multiple` | reveal | transform, opacity | 6 |
| `dipi_fade` | fade | opacity | 2 |
| `fadeIn` | fade | opacity | 1 |
| `fadeIn` | fade | opacity | 1 |
| `mc_slideOut` | custom | bottom | 1 |
| `mc_slideOut` | custom | bottom | 1 |
| `fadeIn` | fade | opacity | 1 |
| `fadeIn` | fade | opacity | 1 |
| `fadeIn` | fade | opacity | 1 |
| `fadeIn` | fade | opacity | 1 |
| `a` | rotate | transform | 1 |
| `a` | rotate | transform | 1 |
| `b` | custom | background-position | 1 |
| `b` | custom | background-position | 1 |
| `fadeIn` | fade | opacity | 1 |
| `fadeIn` | fade | opacity | 1 |

## Component Anatomy

### button — 114 instances

**Slots:** label, icon

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (verbose)

### Top CTA Verbs

- **visa** (11)
- **l** (6)
- **projektarkivet** (4)
- **fullservice** (4)
- **google** (4)
- **varum** (4)
- **ring** (4)
- **instagram** (4)

### Button Copy Patterns

- "visa alla tjänster" (4×)
- "5/5 baserat på 130+ omdömen" (2×)
- "mer om webbdesign" (2×)
- "projektarkivet
support & service
hosting
domännamn
så fungerar seo" (2×)
- "projektarkivet" (2×)
- "support & service" (2×)
- "hosting" (2×)
- "domännamn" (2×)
- "så fungerar seo" (2×)
- "fullservice som tjänst
sociala medier
google ads
seo-analys
nyhetsbrev
google recensioner" (2×)

### Sample Headings

> Har du en fråga, en idé eller ett projekt du vill ha hjälp med?

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Som Sveriges högst rankade webbyrå står vi redo att stötta din verksamhet, vare sig du är i startgroparna eller leder ett etablerat företag

Alternates: legal (0.4)

## Section Roles

Reading order (top→bottom): faq → nav → content → nav → footer → nav → footer → content

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | faq | — | 0.85 |
| 1 | nav | — | 0.9 |
| 2 | footer | Har du en fråga, en idé eller ett projekt du vill ha hjälp med? | 0.95 |
| 3 | content | — | 0.3 |
| 4 | nav | — | 0.9 |
| 5 | content | — | 0.3 |
| 6 | nav | — | 0.4 |
| 7 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.317 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 160px |
| backdrop-filter in use | no |
| Gradients | 2 |

## Imagery Style

**Label:** `photography` (confidence 0.073)
**Counts:** total 48, svg 5, icon 36, screenshot-like 0, photo-like 7
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Component Screenshots

3 retina crops written to `screenshots/`. Index: `*-screenshots.json`.

| Cluster | Variant | Size (px) | File |
|---------|---------|-----------|------|
| button--default | 0 | 486 × 45 | `screenshots/button-default-0.png` |
| button--default | 1 | 155 × 45 | `screenshots/button-default-1.png` |
| button--default | 2 | 155 × 45 | `screenshots/button-default-2.png` |

Full-page: `screenshots/full-page.png`

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Neue Haas Grotesk RoundDots - 55 Roman` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
