# Design Language: Pa'lais | The Plant Kitchen | Plant-based & organic spread cheeses and creamy sauces

> Extracted from `https://www.palais.bio/` on September 4, 2026
> 844 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#234386` | rgb(35, 67, 134) | hsl(221, 59%, 33%) | 180 |
| Secondary | `#61a229` | rgb(97, 162, 41) | hsl(92, 60%, 40%) | 1 |
| Accent | `#00578a` | rgb(0, 87, 138) | hsl(202, 100%, 27%) | 2 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#000000` | hsl(0, 0%, 0%) | 796 |
| `#ffffff` | hsl(0, 0%, 100%) | 172 |
| `#212529` | hsl(210, 11%, 15%) | 114 |
| `#333333` | hsl(0, 0%, 20%) | 104 |
| `#f3f5f7` | hsl(210, 20%, 96%) | 19 |
| `#3a4856` | hsl(210, 19%, 28%) | 6 |
| `#e3e1e8` | hsl(257, 13%, 90%) | 5 |
| `#898989` | hsl(0, 0%, 54%) | 2 |
| `#111111` | hsl(0, 0%, 7%) | 2 |

### Background Colors

Used on large-area elements: `#ffffff`, `#fbf9f6`, `#6aa8dc`, `#a2d3a6`, `#234386`

### Text Colors

Text color palette: `#000000`, `#0000ee`, `#ffffff`, `#234386`, `#ed7328`, `#305787`, `#898989`, `#212529`, `#333333`, `#111111`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#000000` | text, border, background | 796 |
| `#0000ee` | text, border | 364 |
| `#234386` | text, border, background | 180 |
| `#ffffff` | text, border, background | 172 |
| `#212529` | text, border | 114 |
| `#333333` | text, border | 104 |
| `#f3f5f7` | background | 19 |
| `#3a4856` | background | 6 |
| `#305787` | text, border, background | 5 |
| `#e3e1e8` | background | 5 |
| `#ed7328` | text, border | 4 |
| `#00578a` | background | 2 |
| `#6aa8dc` | background | 2 |
| `#898989` | text, border | 2 |
| `#111111` | text, border | 2 |
| `#a2d3a6` | background | 1 |
| `#61a229` | background | 1 |

## Typography

### Font Families

- **Times New Roman** — used for all (618 elements)
- **Lucida Grande** — used for body (58 elements)
- **Sonder Sans Black Rough** — used for all (47 elements)
- **Arial** — used for body (25 elements)
- **Delivery Note DEMO** — used for all (24 elements)
- **hwt-artz** — used for all (23 elements)
- **Axiforma** — used for body (23 elements)
- **ITC Avant Garde Std Bk** — used for body (16 elements)
- **Sandman_Fill** — used for all (8 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 73px | 4.5625rem | 400 | 54px | normal | h1, br |
| 72px | 4.5rem | 400 | 56px | normal | h1, br, h2, span |
| 50px | 3.125rem | 400 | 44px | normal | h2, br |
| 48px | 3rem | 400 | 40px | normal | span |
| 46px | 2.875rem | 400 | 40px | normal | h3 |
| 33px | 2.0625rem | 400 | 39px | normal | h2 |
| 32px | 2rem | 400 | 32px | 1.6px | span, p |
| 28px | 1.75rem | 400 | 32px | normal | span |
| 24px | 1.5rem | 400 | normal | 2px | h1, p |
| 17px | 1.0625rem | 400 | 17px | 1px | div |
| 16px | 1rem | 400 | normal | normal | p, h3, span, h4 |
| 15px | 0.9375rem | 400 | 24px | normal | p, div, span |
| 14.6667px | 0.9167rem | 400 | 18px | normal | div |
| 14.4px | 0.9rem | 400 | 24px | 2px | p |
| 14px | 0.875rem | 600 | normal | 2px | a, div, ul, li |

### Heading Scale

```css
h1 { font-size: 73px; font-weight: 400; line-height: 54px; }
h1 { font-size: 72px; font-weight: 400; line-height: 56px; }
h2 { font-size: 50px; font-weight: 400; line-height: 44px; }
h3 { font-size: 46px; font-weight: 400; line-height: 40px; }
h2 { font-size: 33px; font-weight: 400; line-height: 39px; }
h1 { font-size: 24px; font-weight: 400; line-height: normal; }
h3 { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Body Text

```css
body { font-size: 8px; font-weight: 400; line-height: normal; }
```

### Font Weights in Use

`400` (829x), `600` (6x), `700` (5x), `300` (2x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-30 | 30px | 1.875rem |
| spacing-37 | 37px | 2.3125rem |
| spacing-48 | 48px | 3rem |
| spacing-64 | 64px | 4rem |
| spacing-70 | 70px | 4.375rem |
| spacing-80 | 80px | 5rem |
| spacing-90 | 90px | 5.625rem |
| spacing-100 | 100px | 6.25rem |
| spacing-104 | 104px | 6.5rem |
| spacing-110 | 110px | 6.875rem |
| spacing-120 | 120px | 7.5rem |
| spacing-128 | 128px | 8rem |
| spacing-144 | 144px | 9rem |
| spacing-150 | 150px | 9.375rem |
| spacing-160 | 160px | 10rem |
| spacing-176 | 176px | 11rem |
| spacing-180 | 180px | 11.25rem |
| spacing-200 | 200px | 12.5rem |
| spacing-211 | 211px | 13.1875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 1 |
| sm | 5px | 6 |
| md | 8px | 3 |
| lg | 12px | 1 |
| lg | 16px | 15 |
| full | 30px | 1 |
| full | 34px | 5 |
| full | 50px | 13 |

## Box Shadows

**sm** — blur: 5px
```css
box-shadow: rgb(22, 22, 22) 2px 2px 5px 2px;
```

**md** — blur: 10px
```css
box-shadow: rgba(172, 171, 171, 0.3) 0px -1px 10px 0px;
```

**xl** — blur: 24px
```css
box-shadow: rgba(12, 25, 51, 0.08) 4px 8px 24px 0px;
```

**xl** — blur: 26px
```css
box-shadow: rgba(0, 0, 0, 0.13) 10px 10px 26px 0px;
```

**xl** — blur: 27px
```css
box-shadow: rgba(0, 0, 0, 0.05) 0px 20px 27px 0px;
```

**xl** — blur: 49px
```css
box-shadow: rgba(0, 0, 0, 0.16) -14px 10px 49px 0px;
```

## CSS Custom Properties

### Colors

```css
--wp-block-synced-color: #7a00df;
--wp-block-synced-color--rgb: 122,0,223;
--wp-bound-block-color: var(--wp-block-synced-color);
--wp-admin-theme-color: #007cba;
--wp-admin-theme-color--rgb: 0,124,186;
--wp-admin-theme-color-darker-10: #006ba1;
--wp-admin-theme-color-darker-10--rgb: 0,107,160.5;
--wp-admin-theme-color-darker-20: #005a87;
--wp-admin-theme-color-darker-20--rgb: 0,90,135;
--wp-admin-border-width-focus: 2px;
--ss-primary-color: #5897fb;
--ss-bg-color: #ffffff;
--ss-font-color: #4d4d4d;
--ss-font-placeholder-color: #8d8d8d;
--ss-disabled-color: #dcdee2;
--ss-border-color: #dcdee2;
--ss-highlight-color: #fffb8c;
--ss-success-color: #00b755;
--ss-error-color: #dc3545;
--ss-focus-color: #5897fb;
--ss-border-radius: 4px;
--sb-color-gray-600: #4a5565;
--sb-color-gray-700: #364153;
--sb-color-wp-light-blue-600: #007ca8;
--sb-fg-muted: var(--sb-color-gray-700);
--sb-focus-ring: var(--sb-color-wp-light-blue-600);
--sb-text-secondary: var(--sb-fg-muted);
--wp--preset--color--black: #000;
--wp--preset--color--cyan-bluish-gray: #abb8c3;
--wp--preset--color--white: #fff;
--wp--preset--color--pale-pink: #f78da7;
--wp--preset--color--vivid-red: #cf2e2e;
--wp--preset--color--luminous-vivid-orange: #ff6900;
--wp--preset--color--luminous-vivid-amber: #fcb900;
--wp--preset--color--light-green-cyan: #7bdcb5;
--wp--preset--color--vivid-green-cyan: #00d084;
--wp--preset--color--pale-cyan-blue: #8ed1fc;
--wp--preset--color--vivid-cyan-blue: #0693e3;
--wp--preset--color--vivid-purple: #9b51e0;
--swiper-theme-color: #007aff;
```

### Spacing

```css
--wp--preset--font-size--normal: 16px;
--wp--preset--font-size--huge: 42px;
--ss-spacing-l: 7px;
--ss-spacing-m: 5px;
--ss-spacing-s: 3px;
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
--swiper-navigation-size: 44px;
```

### Typography

```css
--sb-text-tertiary: var(--sb-fg-subtle);
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
--wp-editor-canvas-background: #ddd;
--ss-main-height: 30px;
--ss-content-height: 300px;
--ss-animation-timing: 0.2s;
--sb-duration-75: 75ms;
--sb-duration-100: 100ms;
--sb-duration-150: 150ms;
--sb-duration-200: 200ms;
--sb-duration-300: 300ms;
--sb-duration-500: 500ms;
--sb-duration-700: 700ms;
--sb-duration-1000: 1000ms;
--sb-opacity-disabled: 0.5;
--sb-fg-subtle: var(--sb-color-gray-600);
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
```

### Dependencies

```css
--wp-bound-block-color: --wp-block-synced-color;
--sb-fg-muted: --sb-color-gray-700;
--sb-fg-subtle: --sb-color-gray-600;
--sb-focus-ring: --sb-color-wp-light-blue-600;
--sb-text-secondary: --sb-fg-muted;
--sb-text-tertiary: --sb-fg-subtle;
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
| xs | 340px | min-width |
| xs | 345px | min-width |
| xs | 350px | min-width |
| xs | 360px | min-width |
| xs | 363px | min-width |
| xs | 364px | min-width |
| xs | 367px | min-width |
| xs | 380px | min-width |
| 393px | 393px | min-width |
| 400px | 400px | min-width |
| sm | 420px | min-width |
| sm | 424px | min-width |
| sm | 425px | min-width |
| sm | 436px | min-width |
| sm | 440px | min-width |
| sm | 446px | min-width |
| sm | 450px | min-width |
| sm | 468px | min-width |
| sm | 470px | min-width |
| sm | 472px | min-width |
| sm | 479px | max-width |
| sm | 480px | min-width |
| sm | 496px | min-width |
| sm | 500px | min-width |
| sm | 510px | min-width |
| sm | 520px | min-width |
| sm | 530px | min-width |
| sm | 540px | min-width |
| sm | 543px | min-width |
| sm | 544px | min-width |
| 562px | 562px | min-width |
| sm | 576px | min-width |
| sm | 600px | min-width |
| sm | 601px | min-width |
| sm | 620px | min-width |
| sm | 640px | max-width |
| sm | 646px | min-width |
| sm | 700px | max-width |
| md | 750px | max-width |
| md | 767px | max-width |
| md | 768px | min-width |
| md | 769px | min-width |
| md | 781px | max-width |
| md | 782px | max-width |
| md | 783px | min-width |
| md | 800px | max-width |
| 847px | 847px | min-width |
| 868px | 868px | min-width |
| 900px | 900px | max-width |
| lg | 960px | min-width |
| lg | 985px | max-width |
| lg | 992px | min-width |
| lg | 1024px | max-width |
| lg | 1025px | min-width |
| lg | 1080px | min-width |
| xl | 1230px | min-width |
| xl | 1249px | max-width |
| xl | 1340px | min-width |
| xl | 1341px | min-width |
| 2xl | 1500px | min-width |
| 2xl | 1520px | min-width |
| 2xl | 1600px | min-width |
| 1684px | 1684px | min-width |
| 1700px | 1700px | min-width |
| 1708px | 1708px | min-width |
| 1750px | 1750px | min-width |
| 1800px | 1800px | min-width |
| 1875px | 1875px | min-width |
| 1880px | 1880px | min-width |
| 1900px | 1900px | min-width |
| 2000px | 2000px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0s`, `1s`, `0.35s`, `0.3s`, `0.5s`, `0.15s`, `0.2s`, `0.4s`

### Common Transitions

```css
transition: all;
transition: height 0s 1s, opacity 0.35s ease-in-out, transform 0.35s ease-in-out;
transition: 0.3s cubic-bezier(0.3, 0.95, 0.33, 0.98);
transition: transform;
transition: 0.5s;
transition: transform 0.5s ease-in-out, -webkit-transform 0.5s ease-in-out;
transition: 0.5s ease-in;
transition: max-height 0.15s ease-out;
transition: background-color 0.2s ease-out 0.3s, color 0.2s ease-out;
transition: opacity 0.15s linear;
```

### Keyframe Animations

**blob-turn**
```css
@keyframes blob-turn {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**blob-skew**
```css
@keyframes blob-skew {
  0% { transform: skewY(0deg); }
  13% { transform: skewY(calc( (1.8deg) * var(--amount, 2))); }
  18% { transform: skewY(calc( (2.2deg) * var(--amount, 2))); }
  24% { transform: skewY(calc( (2.48deg) * var(--amount, 2))); }
  25% { transform: skewY(calc( (2.5deg) * var(--amount, 2))); }
  26% { transform: skewY(calc( (2.48deg) * var(--amount, 2))); }
  32% { transform: skewY(calc( (2.2deg) * var(--amount, 2))); }
  37% { transform: skewY(calc( (1.8deg) * var(--amount, 2))); }
  50% { transform: skewY(0deg); }
  63% { transform: skewY(calc( (-1.8deg) * var(--amount, 2))); }
  68% { transform: skewY(calc( (-2.2deg) * var(--amount, 2))); }
  74% { transform: skewY(calc( (-2.48deg) * var(--amount, 2))); }
  75% { transform: skewY(calc( (-2.5deg) * var(--amount, 2))); }
  76% { transform: skewY(calc( (-2.48deg) * var(--amount, 2))); }
  82% { transform: skewY(calc( (-2.2deg) * var(--amount, 2))); }
  87% { transform: skewY(calc( (-1.8deg) * var(--amount, 2))); }
  100% { transform: skewY(0deg); }
}
```

**blob-scale**
```css
@keyframes blob-scale {
  0% { transform: scaleX(0.9) scaleY(1); }
  25% { transform: scaleX(0.9) scaleY(0.9); }
  50% { transform: scaleX(1) scaleY(0.9); }
  75% { transform: scaleX(0.9) scaleY(0.9); }
  100% { transform: scaleX(0.9) scaleY(1); }
}
```

**blob**
```css
@keyframes blob {
  33% { d: path("M 197.866 12.3979 C 195.766 12.4978 19.1967 1.09981 10.3982 7.39872 C 0.599896 14.2975 5.99896 74.3871 6.09895 141.676 C 3.09946 159.472 1.19979 174.77 0 188.667 V 281.551 C 0.799862 299.448 1.39976 319.145 1.09981 343.541 C 2.19962 355.739 1.39976 370.136 0 384.534 V 455.821 C 49.2915 469.919 282.051 458.721 307.347 455.021 C 321.544 452.922 445.823 469.719 453.522 461.92 C 455.221 460.22 456.721 457.021 457.921 452.722 C 457.921 452.722 461.82 364.837 457.921 288.45 C 455.421 239.159 448.722 192.467 450.022 179.369 C 453.322 145.875 457.921 29.5949 457.921 29.5949 C 456.321 15.2974 453.822 5.59903 450.222 3.59938 C 445.523 0.999827 424.527 0 395.632 0 C 338.442 0 197.866 12.3979 197.866 12.3979 Z"); }
  66% { d: path("M 208 4 C 205.9 4.09998 39.7985 23.296 31 29.5949 C 21.2017 36.4937 14.999 74.3871 15.0989 141.676 C 12.0995 159.472 10.1998 174.77 9 188.667 V 281.551 C 9.79986 299.448 10.3998 319.145 10.0998 343.541 C 11.1996 355.739 10.3998 370.136 9 384.534 L 0.5 461.92 C 49.7915 476.018 212.204 465.62 237.5 461.92 C 251.698 459.821 437.301 472.299 445 464.5 C 446.7 462.8 471.8 436.799 473 432.5 C 473 432.5 470.82 364.837 466.921 288.45 C 464.421 239.159 457.722 192.467 459.022 179.369 C 462.322 145.875 466.921 29.5949 466.921 29.5949 C 465.321 15.2974 462.822 5.59903 459.222 3.59938 C 454.523 0.999827 433.527 0 404.632 0 C 347.442 0 208 4 208 4 Z"); }
}
```

**bounce**
```css
@keyframes bounce {
  0% { transform: translateY(-50%) translateX(-50%); }
  5.55556% { transform: translateY(-50%) translateX(-50%); }
  11.1111% { transform: translateY(-50%) translateX(-50%); }
  22.2222% { transform: translateY(-30%) translateX(-50%); }
  27.7778% { transform: translateY(-50%) translateX(-50%); }
  33.3333% { transform: translateY(-30%) translateX(-50%); }
  44.4444% { transform: translateY(-50%) translateX(-50%); }
  100% { transform: translateY(-50%) translateX(-50%); }
}
```

**shape**
```css
@keyframes shape {
  0% { clip-path: url("#shape--start"); }
  100% { clip-path: url("#shape--end"); }
}
```

**WaveCards**
```css
@keyframes WaveCards {
  0% { transform: translateX(0px) rotate(0deg) scale(1); }
  2% { transform: translateX(-10px) rotate(0deg) scale(1); }
  4% { transform: translateX(0px) rotate(0deg) scale(1); }
  100% { transform: translateX(0px) rotate(0deg) scale(1); }
}
```

**WaveCards2**
```css
@keyframes WaveCards2 {
  0% { transform: translateX(0px) rotate(0deg) scale(1); }
  3% { transform: translateX(0px) rotate(0deg) scale(1); }
  5% { transform: translateX(-10px) rotate(0deg) scale(1); }
  7% { transform: translateX(0px) rotate(0deg) scale(1); }
  100% { transform: translateX(0px) rotate(0deg) scale(1); }
}
```

**WaveCards3**
```css
@keyframes WaveCards3 {
  0% { transform: translateX(0px) rotate(0deg) scale(1); }
  6% { transform: translateX(0px) rotate(0deg) scale(1); }
  8% { transform: translateX(-10px) rotate(0deg) scale(1); }
  10% { transform: translateX(0px) rotate(0deg) scale(1); }
  100% { transform: translateX(0px) rotate(0deg) scale(1); }
}
```

**animateHighlighted**
```css
@keyframes animateHighlighted {
  0% { transform: translate(-37px, -18px) rotate(-16deg) scale(1); }
  5% { transform: translate(-37px, -18px) rotate(-16deg) scale(1.05); }
  10% { transform: translate(-37px, -18px) rotate(-16deg) scale(1); }
  15% { transform: translate(-37px, -18px) rotate(-16deg) scale(1.05); }
  50% { transform: translate(-37px, -18px) rotate(-16deg) scale(1); }
  100% { transform: translate(-37px, -18px) rotate(-16deg) scale(1); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (16 instances)

```css
.button {
  background-color: rgb(247, 247, 247);
  color: rgb(0, 0, 0);
  font-size: 14px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (6 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 8px 8px 0px 0px;
  box-shadow: rgba(0, 0, 0, 0.16) -14px 10px 49px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (19 instances)

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

### Links (90 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 8px;
  font-weight: 400;
}
```

### Navigation (35 instances)

```css
.navigatio {
  background-color: rgb(242, 242, 242);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (14 instances)

```css
.foote {
  background-color: rgb(35, 67, 134);
  color: rgb(0, 0, 0);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 8px;
}
```

### Modals (8 instances)

```css
.modal {
  background-color: rgb(0, 0, 0);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 645px;
}
```

### Dropdowns (37 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  box-shadow: rgba(12, 25, 51, 0.08) 4px 8px 24px 0px;
  border-color: rgb(0, 0, 0);
  padding-top: 0px;
}
```

### Tables (2 instances)

```css
.table {
  border-color: rgb(51, 51, 51);
  background-color: rgb(243, 245, 247);
  cell-style: [object Object];
}
```

### Tabs (28 instances)

```css
.tab {
  background-color: rgb(242, 242, 242);
  color: rgb(33, 37, 41);
  font-size: 8px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-color: rgb(33, 37, 41);
  border-radius: 0px;
}
```

### ProgressBars (4 instances)

```css
.progressBar {
  background-color: rgb(0, 87, 138);
  color: rgb(0, 0, 0);
  border-radius: 0px;
  font-size: 8px;
}
```

### Switches (5 instances)

```css
.switche {
  border-radius: 0px;
  border-color: rgb(33, 37, 41);
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 8px;
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
  font-size: 8px;
  font-weight: 400;
```

### Input — 2 instances, 2 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(35, 67, 134);
  padding: 0px 16px 0px 16px;
  border-radius: 0px;
  border: 0px none rgb(35, 67, 134);
  font-size: 13.3333px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 0px 16px 0px 16px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 0);
  font-size: 13.3333px;
  font-weight: 400;
```

### Button — 3 instances, 3 variants

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(48, 87, 135);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(48, 87, 135);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(247, 247, 247);
  color: rgb(137, 137, 137);
  padding: 8px 14px 9px 14px;
  border-radius: 0px;
  border: 0px none rgb(137, 137, 137);
  font-size: 14px;
  font-weight: 400;
```

**Variant 3** (1 instance)

```css
  background: rgb(48, 87, 135);
  color: rgb(255, 255, 255);
  padding: 8px 14px 9px 14px;
  border-radius: 0px;
  border: 0px none rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **73 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 447px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 140px 140px 140px 140px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 54x |
| column/nowrap | 14x |
| row-reverse/nowrap | 2x |
| row/wrap | 3x |

**Gap values:** `0px 2%`

## Accessibility (WCAG 2.1)

**Overall Score: 79%** — 15 passing, 4 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#ed7328` | `#ffffff` | 2.96:1 | FAIL | a (2x) |
| `#898989` | `#f7f7f7` | 3.27:1 | FAIL | a (1x) |
| `#ffffff` | `#61a229` | 3.13:1 | FAIL | a (1x) |

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#234386` | `#ffffff` | 9.47:1 | AAA |
| `#ffffff` | `#3a4856` | 9.37:1 | AAA |
| `#ffffff` | `#234386` | 9.47:1 | AAA |
| `#ffffff` | `#305787` | 7.4:1 | AAA |

## Design System Score

**Overall: 77/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 40/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 90/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 79/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Good CSS variable tokenization

**Issues:**
- 9 font families — consider limiting to 2 (heading + body)
- 24 distinct font sizes — consider a tighter type scale
- 4 WCAG contrast failures
- 560 !important rules — prefer specificity over overrides
- 82% of CSS is unused — consider purging
- 17634 duplicate CSS declarations

## Z-Index Map

**16 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 1040,9999999 | div.c.l.i.-.m.o.d.a.l.-.b.a.c.k.d.r.o.p. .c.l.i.-.f.a.d.e. .c.l.i.-.s.e.t.t.i.n.g.s.-.o.v.e.r.l.a.y, div.c.l.i.-.m.o.d.a.l.-.b.a.c.k.d.r.o.p. .c.l.i.-.f.a.d.e. .c.l.i.-.p.o.p.u.p.b.a.r.-.o.v.e.r.l.a.y, div.p.a.c.e.-.p.r.o.g.r.e.s.s |
| dropdown | 888,999 | ul, ul, ul.o.p.t.i.o.n.s |
| sticky | 10,99 | div.t.o.p.b.a.r.-.m.a.i.n.-.h.e.a.d.e.r.-.m.o.b.i.l.e, div.t.o.p.b.a.r.-.m.a.i.n.-.h.e.a.d.e.r.-.d.e.s.k.t.o.p, div.a.l.l.e.r.g.e.n.-.c.o.n.t.a.i.n.e.r |
| base | -1000,6 | span.s.w.i.p.e.r.-.n.o.t.i.f.i.c.a.t.i.o.n, div.h.o.m.e.-.b.l.o.b.-.w.r.a.p.p.e.r, img.a.t.t.a.c.h.m.e.n.t.-.t.h.u.m.b.n.a.i.l.-.r.e.c.e.t.t.e. .s.i.z.e.-.t.h.u.m.b.n.a.i.l.-.r.e.c.e.t.t.e |

**Issues:**
- [object Object]

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| hwt-artz | self-hosted | 700 | normal |
| Clearface | self-hosted | bold | normal |
| Delivery Note DEMO | self-hosted | normal | normal |
| Sandman_Fill | self-hosted | 500 | normal |
| ITC Avant Garde Std Bk | self-hosted | 300 | normal |
| Sonder Sans Rough | self-hosted | normal | normal |
| Sonder Sans Bold Rough | self-hosted | 500 | normal |
| Sonder Sans Black Rough | self-hosted | bold | normal |
| Axiforma | self-hosted | normal | normal |
| Axiforma ExtraBold | self-hosted | 800 | normal |
| swiper-icons | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 86 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 18 | objectFit: cover, borderRadius: 0px, shape: square |
| general | 8 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (90x), 3.28:1 (12x), 4:3 (4x), 3:4 (3x), 3:2 (1x), 16:9 (1x), 2.17:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **ease-in-out** (16 uses) — `ease`
- **ease-out** (21 uses) — `cubic-bezier(0.3, 0.95, 0.33, 0.98)`
- **linear** (6 uses) — `linear`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `WaveCards` | slide-x | transform | 1 |
| `WaveCards2` | slide-x | transform | 1 |
| `WaveCards3` | slide-x | transform | 1 |
| `WaveCards` | slide-x | transform | 1 |
| `WaveCards2` | slide-x | transform | 1 |
| `WaveCards3` | slide-x | transform | 1 |

## Component Anatomy

### button — 6 instances

**Slots:** label
**Sizes:** large

### input — 2 instances


## Brand Voice

**Tone:** friendly · **Pronoun:** you-only · **Headings:** Sentence case (balanced)

### Top CTA Verbs

- **submit** (1)
- **cookie** (1)
- **reject** (1)
- **accept** (1)

### Button Copy Patterns

- "submit" (1×)
- "cookie settings" (1×)
- "reject" (1×)
- "accept" (1×)

### Sample Headings

> Grow your
plant kitchen
> Grow your
plant kitchen
> The future
of cooking - today
> Incredible recipes that will take your taste buds to heaven and back
> Incredible recipes


that will take your taste buds to heaven and back
> Spready, saucyand non-dairy!
> Pa'lais Spreads
> Pa'lais Cuisine
>  You arePa'lais
> You are
Pa'lais

## Page Intent

**Type:** `landing` (confidence 0.51)
**Description:** Discover our vegan spread-cheeses and sauces made entirely out of plants. Lactose-free, gluten-free, soy-free, sugar-free and additive-free.

Alternates: blog-post (0.6), legal (0.4)

## Section Roles

Reading order (top→bottom): feature-grid → feature-grid → nav → hero → feature-grid → nav → content → content → content → content → content → faq → hero → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | feature-grid | — | 0.8 |
| 1 | feature-grid | — | 0.8 |
| 2 | nav | — | 0.9 |
| 3 | feature-grid | — | 0.8 |
| 4 | nav | — | 0.9 |
| 5 | hero | Grow your
plant kitchen | 0.85 |
| 6 | content | — | 0.3 |
| 7 | content | Incredible recipes that will take your taste buds to heaven and back | 0.3 |
| 8 | content | Spready, saucyand non-dairy! | 0.3 |
| 9 | content | Pa'lais Spreads | 0.3 |
| 10 | content |  You arePa'lais | 0.3 |
| 11 | faq | PA'LAIS finder | 0.85 |
| 12 | hero | You probably don't want another newsletter in your mailbox,
but then you'd miss  | 0.4 |
| 13 | footer | MENU | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.369 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 50px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.089)
**Counts:** total 112, svg 81, icon 17, screenshot-like 0, photo-like 17
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Times New Roman` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
