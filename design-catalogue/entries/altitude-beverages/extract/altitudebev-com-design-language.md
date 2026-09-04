# Design Language: Altitude Beverages | Premium Non-Alcoholic Drinks with Functional Ingredients

> Extracted from `https://altitudebev.com` on September 4, 2026
> 741 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#fafafa` | hsl(0, 0%, 98%) | 1273 |
| `#000000` | hsl(0, 0%, 0%) | 73 |
| `#53606e` | hsl(211, 14%, 38%) | 36 |
| `#808080` | hsl(0, 0%, 50%) | 30 |

### Background Colors

Used on large-area elements: `#808080`, `#000000`

### Text Colors

Text color palette: `#000000`, `#fafafa`, `#07060b`, `#53606e`, `#ffffff`

### Gradients

```css
background-image: linear-gradient(rgb(135, 142, 154) 25.88%, rgb(144, 131, 142) 131.14%);
```

```css
background-image: linear-gradient(rgba(217, 217, 217, 0) 0%, rgba(168, 43, 58, 0.7) 100%);
```

```css
background-image: linear-gradient(rgb(132, 152, 153) 0%, rgb(141, 157, 141) 100%);
```

```css
background-image: linear-gradient(rgba(217, 217, 217, 0) 0%, rgba(190, 193, 58, 0.7) 100%);
```

```css
background-image: linear-gradient(rgb(137, 143, 147) 0%, rgb(150, 135, 130) 100%);
```

```css
background-image: linear-gradient(rgb(217, 217, 217) 0%, rgba(199, 76, 23, 0.7) 100%);
```

```css
background-image: linear-gradient(rgb(6, 5, 10) 0%, rgb(12, 12, 20) 5.43%, rgb(25, 29, 45) 12.1%, rgb(34, 40, 62) 18.86%, rgb(53, 68, 91) 25%, rgb(69, 96, 117) 32.3%, rgb(87, 119, 140) 38.7%, rgb(104, 137, 156) 44.45%, rgb(121, 150, 164) 50%, rgb(140, 162, 175) 56.05%, rgb(160, 178, 188) 62.3%, rgb(173, 190, 198) 68.4%, rgb(187, 200, 206) 75%, rgb(202, 212, 214) 80.62%, rgb(214, 219, 222) 86.41%, rgb(235, 237, 236) 93.78%, rgb(245, 246, 241) 100%);
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#fafafa` | text, border, background | 1273 |
| `#000000` | text, border, background | 73 |
| `#53606e` | text, border | 36 |
| `#808080` | background | 30 |

## Typography

### Font Families

- **DepartureMono** — used for all (73 elements)
- **HelveticaNowDisplay** — used for body (24 elements)
- **EditorialNew** — used for all (23 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 160px | 10rem | 800 | 160px | -8px | p |
| 60px | 3.75rem | 200 | 63.6px | -1.5px | p, h1 |
| 40px | 2.5rem | 200 | 42.4px | -1px | p |
| 18px | 1.125rem | 500 | 16.2px | -0.9px | p |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |
| 14px | 0.875rem | 400 | 20px | normal | p, br, a, span |
| 12px | 0.75rem | 400 | 28px | normal | input |
| 11.2px | 0.7rem | 400 | 20px | normal | p, a |
| 11px | 0.6875rem | 400 | 11px | -0.55px | p |

### Heading Scale

```css
h1 { font-size: 60px; font-weight: 200; line-height: 63.6px; }
h3 { font-size: 14px; font-weight: 400; line-height: 20px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 400; line-height: 20px; }
```

### Font Weights in Use

`400` (685x), `200` (23x), `800` (21x), `500` (12x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-36 | 36px | 2.25rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-64 | 64px | 4rem |
| spacing-78 | 78px | 4.875rem |
| spacing-85 | 85px | 5.3125rem |
| spacing-96 | 96px | 6rem |
| spacing-125 | 125px | 7.8125rem |
| spacing-265 | 265px | 16.5625rem |
| spacing-288 | 288px | 18rem |
| spacing-320 | 320px | 20rem |
| spacing-333 | 333px | 20.8125rem |
| spacing-495 | 495px | 30.9375rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| full | 32px | 4 |
| full | 44px | 29 |
| full | 100px | 30 |
| full | 110px | 1 |

## CSS Custom Properties

### Colors

```css
--color-purple-200: #e9d5ff;
--color-purple-300: #d8b4fe;
--color-zinc-100: #f4f4f5;
--color-zinc-200: #e4e4e7;
--color-rose-200: #fecdd3;
--color-slate-200: #e2e8f0;
--color-sky-500: #0ea5e9;
--color-pink-500: #ec4899;
--color-violet-600: #7c3aed;
--color-orange-600: #ea580c;
--color-red-900: #7f1d1d;
--color-orange-800: #9a3412;
--color-neutral-600: #525252;
--color-teal-400: #2dd4bf;
--color-pink-950: #500724;
--color-blue-700: #1d4ed8;
--color-neutral-300: #d4d4d4;
--color-slate-500: #64748b;
--color-purple-800: #6b21a8;
--color-orange-900: #7c2d12;
--color-pricklypear-500: #a82b3a;
--tw-inset-ring-shadow: 0 0 #0000;
--color-orange-50: #fff7ed;
--color-neutral-200: #e5e5e5;
--color-cyan-700: #0e7490;
--color-blue-300: #93c5fd;
--color-gray-300: #d1d5db;
--color-yellow-400: #facc15;
--color-slate-300: #cbd5e1;
--color-cyan-200: #a5f3fc;
--color-amber-300: #fcd34d;
--color-gray-500: #6b7280;
--color-zinc-50: #fafafa;
--color-green-500: #226d37;
--color-white: #fafafa;
--color-sky-600: #0284c7;
--color-gray-400: #9ca3af;
--color-blue-400: #60a5fa;
--color-pink-50: #fdf2f8;
--color-slate-400: #94a3b8;
--color-stone-900: #1c1917;
--color-yellow-300: #fde047;
--color-zinc-950: #09090b;
--color-gray-100: #f3f4f6;
--color-teal-950: #042f2e;
--color-tiny-header: #ffffff3d;
--color-emerald-200: #a7f3d0;
--color-purple-600: #9333ea;
--color-teal-900: #134e4a;
--color-violet-800: #5b21b6;
--color-zinc-700: #3f3f46;
--color-neutral-700: #404040;
--color-violet-500: #8b5cf6;
--color-varietypack-500: #191d2d;
--color-fuchsia-600: #c026d3;
--color-sky-50: #f0f9ff;
--color-border-hover: #fff6;
--color-lime-200: #d9f99d;
--color-fuchsia-200: #f5d0fe;
--color-green-900: #14532d;
--color-rose-950: #4c0519;
--color-pink-100: #fce7f3;
--color-blue-800: #1e40af;
--color-neutral-900: #171717;
--color-light: #fff;
--color-cyan-50: #ecfeff;
--color-neutral-100: #f5f5f5;
--color-blue-100: #dbeafe;
--color-green-600: #16a34a;
--color-green-950: #052e16;
--color-yellow-950: #422006;
--color-violet-950: #2e1065;
--color-violet-300: #c4b5fd;
--color-zinc-900: #18181b;
--color-red-300: #fca5a5;
--color-cyan-500: #06b6d4;
--color-orange-500: #df5f38;
--color-slate-800: #1e293b;
--color-lime-800: #3f6212;
--color-rosemary-500: #c74c17;
--color-emerald-900: #064e3b;
--color-sky-400: #38bdf8;
--color-sky-300: #7dd3fc;
--color-beige-500: #d7cdc3;
--color-slate-600: #475569;
--color-pink-600: #db2777;
--color-pink-200: #fbcfe8;
--color-stone-600: #57534e;
--color-dark: #000;
--color-rose-900: #881337;
--color-green-400: #4ade80;
--color-emerald-500: #10b981;
--color-yellow-50: #fefce8;
--color-gray-950: #030712;
--color-rose-700: #be123c;
--color-amber-700: #b45309;
--color-gray: #ddfcff;
--color-amber-900: #78350f;
--color-emerald-50: #ecfdf5;
--color-darkblue-500: #122c77;
--color-zinc-600: #52525b;
--color-indigo-500: #6366f1;
--color-violet-200: #ddd6fe;
--color-gray-600: #4b5563;
--color-orange-100: #ffedd5;
--color-purple-400: #c084fc;
--color-yellow-200: #fef08a;
--color-blue-600: #2563eb;
--color-green-200: #bbf7d0;
--tw-border-style: solid;
--color-cyan-900: #164e63;
--color-red-600: #dc2626;
--color-blue-50: #eff6ff;
--color-stone-700: #44403c;
--color-indigo-700: #4338ca;
--color-neutral-950: #0a0a0a;
--color-black: #07060b;
--color-neutral-400: #a3a3a3;
--tw-border-spacing-y: 0px;
--color-fuchsia-300: #f0abfc;
--color-amber-100: #fef3c7;
--color-stone-800: #292524;
--color-window-glass: #8080804d;
--color-indigo-100: #e0e7ff;
--color-emerald-800: #065f46;
--color-violet-50: #f5f3ff;
--color-teal-100: #ccfbf1;
--color-indigo-300: #a5b4fc;
--color-cyan-300: #67e8f9;
--color-amber-400: #fbbf24;
--tw-ring-shadow: 0 0 #0000;
--color-indigo-400: #818cf8;
--color-orange-200: #fed7aa;
--color-purple-500: #a855f7;
--color-emerald-300: #6ee7b7;
--color-yellow-600: #ca8a04;
--color-pink-300: #f9a8d4;
--tw-inset-shadow-colored: 0 0 #0000;
--color-slate-700: #334155;
--color-lime-950: #1a2e05;
--color-cyan-400: #22d3ee;
--color-neutral-500: #737373;
--color-amber-600: #d97706;
--color-yellow-800: #854d0e;
--color-pink-400: #f472b6;
--color-slate-900: #0f172a;
--color-stone-400: #a8a29e;
--color-green-100: #dcfce7;
--color-emerald-700: #047857;
--tw-border-spacing-x: 0px;
--color-teal-50: #f0fdfa;
--color-red-200: #fecaca;
--color-indigo-800: #3730a3;
--color-purple-900: #581c87;
--color-violet-900: #4c1d95;
--color-sky-800: #075985;
--color-lightgray-500: #e5e4e2;
--color-pink-800: #9d174d;
--color-teal-800: #115e59;
--color-gray-50: #f9fafb;
--color-emerald-600: #059669;
--color-stone-950: #0c0a09;
--color-violet-400: #a78bfa;
--color-lime-600: #65a30d;
--color-purple-100: #f3e8ff;
--tw-ring-offset-color: #fff;
--color-red-400: #f87171;
--color-maitai-500: #bec13a;
--color-pink-900: #831843;
--color-fuchsia-50: #fdf4ff;
--color-indigo-50: #eef2ff;
--color-lime-300: #bef264;
--color-teal-600: #0d9488;
--color-rose-100: #ffe4e6;
--color-fuchsia-800: #86198f;
--color-emerald-100: #d1fae5;
--color-red-800: #991b1b;
--color-red-500: #9e100f;
--color-rose-400: #fb7185;
--tw-ring-offset-width: 0px;
--color-zinc-300: #d4d4d8;
--color-purple-950: #3b0764;
--color-rose-800: #9f1239;
--color-indigo-600: #4f46e5;
--color-amber-800: #92400e;
--tw-shadow-colored: 0 0 #0000;
--color-fuchsia-500: #d946ef;
--color-neutral-50: #fafafa;
--color-lime-500: #84cc16;
--color-sky-700: #0369a1;
--color-cyan-800: #155e75;
--color-slate-50: #f8fafc;
--color-orange-300: #fdba74;
--color-yellow-100: #fef9c3;
--color-violet-700: #6d28d9;
--tw-ring-offset-shadow: 0 0 #0000;
--color-gray-800: #1f2937;
--color-stone-100: #f5f5f4;
--color-zinc-500: #71717a;
--color-orange-700: #c2410c;
--color-green-50: #f0fdf4;
--color-teal-700: #0f766e;
--color-lime-700: #4d7c0f;
--color-indigo-950: #1e1b4b;
--color-zinc-800: #27272a;
--color-lime-900: #365314;
--color-sky-100: #e0f2fe;
--color-stone-500: #78716c;
--color-lime-50: #f7fee7;
--color-rose-50: #fff1f2;
--color-orange-950: #431407;
--color-emerald-950: #022c22;
--color-amber-500: #f59e0b;
--color-orange-400: #fb923c;
--color-sky-900: #0c4a6e;
--color-cyan-100: #cffafe;
--color-yellow-700: #a16207;
--color-violet-100: #ede9fe;
--color-rose-300: #fda4af;
--color-slate-950: #020617;
--color-brown-500: #44372e;
--color-green-800: #166534;
--color-rose-500: #f43f5e;
--color-red-700: #b91c1c;
--color-slate-100: #f1f5f9;
--color-fuchsia-950: #4a044e;
--color-indigo-200: #c7d2fe;
--color-rose-600: #e11d48;
--color-blue-500: #217ec9;
--color-gray-900: #111827;
--color-pink-700: #be185d;
--color-blue-900: #1e3a8a;
--color-sky-950: #082f49;
--color-zinc-400: #a1a1aa;
--color-yellow-900: #713f12;
--color-gray-700: #374151;
--color-lime-100: #ecfccb;
--color-cyan-600: #0891b2;
--color-teal-300: #5eead4;
--color-purple-50: #faf5ff;
--color-red-100: #fee2e2;
--color-amber-950: #451a03;
--color-stone-200: #e7e5e4;
--color-red-50: #fef2f2;
--color-blue-200: #bfdbfe;
--color-lime-400: #a3e635;
--color-gray-200: #e5e7eb;
--color-green-300: #86efac;
--color-red-950: #450a0a;
--color-teal-200: #99f6e4;
--color-emerald-400: #34d399;
--color-fuchsia-900: #701a75;
--color-indigo-900: #312e81;
--color-green-700: #15803d;
--color-fuchsia-400: #e879f9;
--color-fuchsia-100: #fae8ff;
--color-purple-700: #7e22ce;
--color-neutral-800: #262626;
--color-teal-500: #14b8a6;
--color-cyan-950: #083344;
--color-yellow-500: #e1ed81;
--color-sky-200: #bae6fd;
--color-blue-950: #172554;
--color-amber-50: #fffbeb;
--color-stone-300: #d6d3d1;
--color-stone-50: #fafaf9;
--color-amber-200: #fde68a;
--color-fuchsia-700: #a21caf;
```

### Spacing

```css
--font-size-lg--line-height: 1.75rem;
--spacing-3_5: .875rem;
--spacing-12: 3rem;
--font-size-5xl--line-height: 1;
--font-size-base--line-height: 1.5rem;
--spacing-80: 20rem;
--font-size-3xl--line-height: 2.25rem;
--font-size-4xl: 2.25rem;
--spacing-px: 1px;
--spacing-1_5: .375rem;
--spacing-96: 24rem;
--tw-space-x-reverse: 0;
--spacing-5: 1.25rem;
--font-size-xs: .75rem;
--font-size-8xl--line-height: 1;
--spacing-4: 1rem;
--spacing-1: .25rem;
--spacing-36: 9rem;
--spacing-48: 12rem;
--spacing-6: 1.5rem;
--font-size-2xl: 1.5rem;
--spacing-0: 0px;
--font-size-5xl: 3rem;
--spacing-0_5: .125rem;
--font-size-3xl: 1.875rem;
--font-size-lg: 1.125rem;
--letter-spacing-tight: -.025em;
--font-size-9xl: 8rem;
--spacing-24: 6rem;
--tw-space-y-reverse: 0;
--font-size-xl--line-height: 1.75rem;
--spacing-60: 15rem;
--font-size-6xl--line-height: 1;
--spacing-52: 13rem;
--gap-sm: max(.25rem,.27778vw);
--spacing-32: 8rem;
--spacing-2_5: .625rem;
--spacing-8: 2rem;
--font-size-9xl--line-height: 1;
--spacing-20: 5rem;
--letter-spacing-widest: .1em;
--spacing-44: 11rem;
--spacing-3: .75rem;
--font-size-base: 1rem;
--spacing-28: 7rem;
--letter-spacing-normal: 0em;
--font-size-8xl: 6rem;
--spacing-40: 10rem;
--spacing-10: 2.5rem;
--font-size-2xl--line-height: 2rem;
--font-size-sm--line-height: 1.25rem;
--font-size-7xl: 4.5rem;
--spacing-9: 2.25rem;
--font-size-6xl: 3.75rem;
--spacing-64: 16rem;
--font-size-sm: .875rem;
--letter-spacing-wide: .025em;
--font-size-xs--line-height: 1rem;
--font-size-4xl--line-height: 2.5rem;
--spacing-56: 14rem;
--spacing-14: 3.5rem;
--padding-sm: max(.25rem,.27778vw);
--spacing-72: 18rem;
--spacing-2: .5rem;
--font-size-7xl--line-height: 1;
--font-size-xl: 1.25rem;
--spacing-11: 2.75rem;
--letter-spacing-wider: .05em;
--letter-spacing-tighter: -.05em;
--spacing-7: 1.75rem;
--spacing-16: 4rem;
```

### Typography

```css
--default-font-feature-settings: ;
--font-family-helveticanow: "HelveticaNowDisplay",sans-serif;
--font-family-serif: ui-serif,Georgia,Cambria,"Times New Roman",Times,serif;
--default-font-variation-settings: ;
--font-family-mono: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
--line-height-8: 2rem;
--font-family-sans: ui-sans-serif,system-ui,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
--line-height-normal: 1.5;
--line-height-5: 1.25rem;
--line-height-relaxed: 1.625;
--font-family-departure: "DepartureMono",sans-serif;
--line-height-10: 2.5rem;
--line-height-7: 1.75rem;
--font-family-editorial: "EditorialNew",sans-serif;
--line-height-3: .75rem;
--line-height-tight: 1.25;
--line-height-none: 1;
--default-font-family: ui-sans-serif,system-ui,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
--line-height-snug: 1.375;
--line-height-9: 2.25rem;
--line-height-4: 1rem;
--default-mono-font-variation-settings: ;
--line-height-6: 1.5rem;
--line-height-loose: 2;
--default-mono-font-feature-settings: ;
--default-mono-font-family: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
```

### Shadows

```css
--shadow-xs: 0 1px #0000000d;
--tw-inset-shadow: 0 0 #0000;
--drop-shadow-lg: 0 10px 8px #0000000a,0 4px 3px #0000001a;
--shadow-xl: 0 20px 25px -5px #0000001a,0 8px 10px -6px #0000001a;
--drop-shadow-sm: 0 1px 1px #0000000d;
--drop-shadow-xl: 0 20px 13px #00000008,0 8px 5px #00000014;
--inset-shadow-xs: inset 0 1px #0000000d;
--shadow-md: 0 4px 6px -1px #0000001a,0 2px 4px -2px #0000001a;
--inset-shadow-sm: inset 0 1px 1px #0000000d;
--inset-shadow: inset 0 2px 4px #0000000d;
--drop-shadow-2xl: 0 25px 25px #00000026;
--shadow-sm: 0 1px 2px 0 #0000000d;
--shadow-lg: 0 10px 15px -3px #0000001a,0 4px 6px -4px #0000001a;
--shadow-2xl: 0 25px 50px -12px #00000040;
--drop-shadow-md: 0 4px 3px #00000012,0 2px 2px #0000000f;
--shadow: 0 1px 3px 0 #0000001a,0 1px 2px -1px #0000001a;
--shadow-inner: inset 0 2px 4px 0 #0000000d;
--tw-shadow: 0 0 #0000;
--drop-shadow: 0 1px 2px #0000001a,0 1px 1px #0000000f;
```

### Radii

```css
--radius-4xl: 2rem;
--radius-sm: .125rem;
--radius-standard: 2.75rem;
--radius-2xl: 1rem;
--radius-md: .375rem;
--radius-cart-2xl: max(3.25rem,2.71vw);
--radius-lg: .5rem;
--radius-button: max(100px,6.944vw);
--radius-standard-2xl: max(2.7vw,3.25rem);
--radius: .25rem;
--radius-3xl: 1.5rem;
--radius-cart: 1.75rem;
--radius-xl: .75rem;
```

### Other

```css
--header-height: 64px;
--cart-aside-summary-height-with-discount: 300px;
--blur-lg: 16px;
--background-image-home-gradient: linear-gradient(180deg,#06050a 0%,#0c0c14 5.43%,#191d2d 12.1%,#22283e 18.86%,#35445b 25%,#456075 32.3%,#57778c 38.7%,#68899c 44.45%,#7996a4 50%,#8ca2af 56.05%,#a0b2bc 62.3%,#adbec6 68.4%,#bbc8ce 75%,#cad4d6 80.62%,#d6dbde 86.41%,#ebedec 93.78%,#f5f6f1 100%);
--width-7xl: 80rem;
--width-3xs: 16rem;
--width-md: 28rem;
--p3: 57%;
--perspective-normal: 500px;
--blur-2xl: 40px;
--transition-timing-function-in: cubic-bezier(.4,0,1,1);
--tw-rotate-x: rotateX(0deg);
--tw-rotate-z: rotate(0deg);
--width-prose: 65ch;
--default-transition-duration: .15s;
--animate-pulse: pulse 2s cubic-bezier(.4,0,.6,1)infinite;
--width-xl: 36rem;
--default-transition-timing-function: cubic-bezier(.4,0,.2,1);
--perspective-dramatic: 100px;
--tw-translate-z: 0px;
--p2: 41%;
--tw-scale-y: 1;
--breakpoint-lg: 64rem;
--tw-translate-y: 0px;
--width-5xl: 64rem;
--transition-timing-function-out: cubic-bezier(0,0,.2,1);
--findus2: 100%;
--tw-content: "";
--tw-rotate-y: rotateY(0deg);
--transition-timing-function-linear: linear;
--tw-translate-x: 0px;
--animate-bounce: bounce 1s infinite;
--findus3: 90%;
--aside-width: 400px;
--transition-timing-function-in-out: cubic-bezier(.4,0,.2,1);
--breakpoint-xl: 80rem;
--animate-ping: ping 1s cubic-bezier(0,0,.2,1)infinite;
--width-3xl: 48rem;
--width-2xl: 42rem;
--blur-xl: 24px;
--width-lg: 32rem;
--breakpoint-2xl: 120rem;
--blur-3xl: 64px;
--tw-scale-z: 1;
--cart-aside-summary-height: 250px;
--grid-item-width: 355px;
--perspective-midrange: 800px;
--tw-skew-y: skewY(0deg);
--width-4xl: 56rem;
--findus4: 100%;
--p4: 100%;
--perspective-distant: 1200px;
--width-xs: 20rem;
--blur-md: 12px;
--animate-spin: spin 1s linear infinite;
--tw-skew-x: skew(0deg);
--perspective-near: 300px;
--width-6xl: 72rem;
--breakpoint-md: 48rem;
--width-2xs: 18rem;
--width-sm: 24rem;
--p1: 0%;
--tw-scale-x: 1;
--findus1: 100%;
--blur: 8px;
--breakpoint-sm: 40rem;
--blur-sm: 4px;
```

### Semantic

```css
success: [object Object];
warning: [object Object];
error: [object Object];
info: [object Object];
```

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `0.5s`, `0.15s`

### Common Transitions

```css
transition: all;
transition: opacity 0.5s;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (31 instances)

```css
.button {
  background-color: rgba(128, 128, 128, 0.3);
  color: rgb(250, 250, 250);
  font-size: 14px;
  font-weight: 400;
  padding-top: 16px;
  padding-right: 28px;
  border-radius: 100px;
}
```

### Inputs (1 instances)

```css
.input {
  color: rgb(250, 250, 250);
  border-color: rgb(250, 250, 250);
  border-radius: 0px;
  font-size: 12px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (41 instances)

```css
.link {
  color: rgb(250, 250, 250);
  font-size: 14px;
  font-weight: 400;
}
```

### Navigation (17 instances)

```css
.navigatio {
  background-color: rgba(128, 128, 128, 0.3);
  color: rgb(250, 250, 250);
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
  color: rgb(250, 250, 250);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Modals (2 instances)

```css
.modal {
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 13 instances, 3 variants

**Variant 1** (7 instances)

```css
  background: rgb(250, 250, 250);
  color: rgb(7, 6, 11);
  padding: 16px 28px 16px 28px;
  border-radius: 100px;
  border: 0px solid rgb(250, 250, 250);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(128, 128, 128, 0.3);
  color: color(srgb 0.980392 0.980392 0.980392 / 0.5);
  padding: 17px 28px 17px 28px;
  border-radius: 100px;
  border: 0px solid rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 400;
```

**Variant 3** (5 instances)

```css
  background: rgba(128, 128, 128, 0.3);
  color: rgb(250, 250, 250);
  padding: 17px 28px 17px 28px;
  border-radius: 100px;
  border: 0px solid rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: color(srgb 0.501961 0.501961 0.501961 / 0.120784);
  color: color(srgb 0.980392 0.980392 0.980392 / 0.5);
  padding: 0px 0px 0px 0px;
  border-radius: 100px;
  border: 0px solid rgba(0, 0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(128, 128, 128, 0.3);
  color: color(srgb 0.980392 0.980392 0.980392 / 0.5);
  padding: 17px 28px 17px 28px;
  border-radius: 100px;
  border: 0px solid rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: color(srgb 0.980392 0.980392 0.980392 / 0.9);
  padding: 0px 24px 0px 24px;
  border-radius: 100px;
  border: 0px solid rgba(0, 0, 0, 0);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(250, 250, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 3.35544e+07px;
  border: 0px solid rgb(250, 250, 250);
  font-size: 16px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(250, 250, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(250, 250, 250);
  font-size: 12px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(250, 250, 250);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px solid rgb(250, 250, 250);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**1 grid containers** and **81 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1024px | 48px |
| 100% | 0px |
| 1280px | 0px |
| 1248px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: 400px 400px 400px;
gap: 20px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 32x |
| row/nowrap | 36x |
| row/wrap | 13x |

**Gap values:** `12px`, `16px`, `20px`, `36px`, `48px 20px`, `4px`, `6px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 10 passing, 0 failing color pairs

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#07060b` | `#fafafa` | 19.35:1 | AAA |

## Design System Score

**Overall: 87/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 85/100 |
| Typography Consistency | 80/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- No clear primary brand color detected
- 32 !important rules — prefer specificity over overrides
- 504 duplicate CSS declarations

## Gradients

**7 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 17 | complex |

```css
background: linear-gradient(rgb(135, 142, 154) 25.88%, rgb(144, 131, 142) 131.14%);
background: linear-gradient(rgba(217, 217, 217, 0) 0%, rgba(168, 43, 58, 0.7) 100%);
background: linear-gradient(rgb(132, 152, 153) 0%, rgb(141, 157, 141) 100%);
background: linear-gradient(rgba(217, 217, 217, 0) 0%, rgba(190, 193, 58, 0.7) 100%);
background: linear-gradient(rgb(137, 143, 147) 0%, rgb(150, 135, 130) 100%);
```

## Z-Index Map

**7 unique z-index values** across 4 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9999,9999 | div |
| dropdown | 100,100 | div.z.-.5.0. .f.i.x.e.d. .g.r.o.u.p. .t.o.p.-.0. .b.o.t.t.o.m.-.0. .l.e.f.t.-.0. .r.i.g.h.t.-.0. .p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .h.-.d.v.h. .i.n.v.i.s.i.b.l.e. .o.p.a.c.i.t.y.-.0. .[.&.[.d.a.t.a.-.e.x.p.a.n.d.e.d.]._.a.s.i.d.e.].:.t.r.a.n.s.l.a.t.e.-.x.-.[.c.a.l.c.(.v.a.r.(.-.-.a.s.i.d.e.-.w.i.d.t.h.).*.-.1.).]. .z.-.[.1.0.0.] |
| sticky | 10,50 | a.s.m.:.p.x.-.6. .z.-.1.0. .2.x.l.:.p.x.-.[.m.a.x.(.1...1.2.5.v.w.,.1...5.r.e.m.).]. .!.d.e.c.o.r.a.t.i.o.n.-.w.h.i.t.e./.9.0. .!.d.e.c.o.r.a.t.i.o.n.-.2. .r.e.l.a.t.i.v.e. .o.p.a.c.i.t.y.-.0. .t.r.a.n.s.l.a.t.e.-.y.-.[.2.0.%.]. .m.d.:.o.p.a.c.i.t.y.-.1.0.0. .m.d.:.t.r.a.n.s.l.a.t.e.-.y.-.0. .a.s.i.d.e.-.c.h.i.l.d. .h.-.f.u.l.l. .t.e.x.t.-.c.e.n.t.e.r. .f.l.e.x. .i.t.e.m.s.-.c.e.n.t.e.r, a.s.m.:.p.x.-.6. .z.-.1.0. .2.x.l.:.p.x.-.[.m.a.x.(.1...1.2.5.v.w.,.1...5.r.e.m.).]. .!.d.e.c.o.r.a.t.i.o.n.-.w.h.i.t.e./.9.0. .!.d.e.c.o.r.a.t.i.o.n.-.2. .r.e.l.a.t.i.v.e. .o.p.a.c.i.t.y.-.0. .t.r.a.n.s.l.a.t.e.-.y.-.[.2.0.%.]. .m.d.:.o.p.a.c.i.t.y.-.1.0.0. .m.d.:.t.r.a.n.s.l.a.t.e.-.y.-.0. .a.s.i.d.e.-.c.h.i.l.d. .h.-.f.u.l.l. .t.e.x.t.-.c.e.n.t.e.r. .f.l.e.x. .i.t.e.m.s.-.c.e.n.t.e.r, a.s.m.:.p.x.-.6. .z.-.1.0. .2.x.l.:.p.x.-.[.m.a.x.(.1...1.2.5.v.w.,.1...5.r.e.m.).]. .!.d.e.c.o.r.a.t.i.o.n.-.w.h.i.t.e./.9.0. .!.d.e.c.o.r.a.t.i.o.n.-.2. .r.e.l.a.t.i.v.e. .o.p.a.c.i.t.y.-.0. .t.r.a.n.s.l.a.t.e.-.y.-.[.2.0.%.]. .m.d.:.o.p.a.c.i.t.y.-.1.0.0. .m.d.:.t.r.a.n.s.l.a.t.e.-.y.-.0. .a.s.i.d.e.-.c.h.i.l.d. .h.-.f.u.l.l. .t.e.x.t.-.c.e.n.t.e.r. .f.l.e.x. .i.t.e.m.s.-.c.e.n.t.e.r |
| base | 0,1 | div.f.l.e.x. .a.b.s.o.l.u.t.e. .t.o.p.-.0. .l.e.f.t.-.0. .i.t.e.m.s.-.e.n.d. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .s.m.:.j.u.s.t.i.f.y.-.s.t.a.r.t. .h.-.f.u.l.l. .w.-.f.u.l.l. .z.-.0, div.f.l.e.x. .a.b.s.o.l.u.t.e. .t.o.p.-.0. .l.e.f.t.-.0. .i.t.e.m.s.-.e.n.d. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .s.m.:.j.u.s.t.i.f.y.-.s.t.a.r.t. .h.-.f.u.l.l. .w.-.f.u.l.l. .z.-.0, div.a.b.s.o.l.u.t.e. .t.o.p.-.0. .l.e.f.t.-.0. .z.-.0. .w.-.f.u.l.l. .h.-.f.u.l.l |

## SVG Icons

**4 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| md | 1 |
| lg | 2 |
| xl | 1 |

**Icon colors:** `#fafafa`, `#DDFCFF`, `white`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 7 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 4 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 9:16 (6x), 1:1 (4x), 3:2 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `150ms` | 150 |
| `lg` | `500ms` | 500 |

### Easing Families

- **custom** (1 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`

## Component Anatomy

### button — 18 instances

**Slots:** label
**Sizes:** lg · sm · md

## Brand Voice

**Tone:** friendly · **Pronoun:** third-person · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **shop** (7)
- **continue** (1)
- **close** (1)
- **read** (1)
- **talk** (1)
- **instagram** (1)
- **tiktok** (1)
- **policies** (1)

### Button Copy Patterns

- "shop" (6×)
- "continue shopping" (1×)
- "close" (1×)
- "shop
about
find us
cart (0)" (1×)
- "read more" (1×)
- "talk(at)altitude.bev" (1×)
- "instagram" (1×)
- "tiktok" (1×)
- "policies" (1×)
- "account" (1×)

### Sample Headings

> talk@altitude.bev
> Instagram
> TikTok
> Policies
> Account
> talk@altitude.bev
> Instagram
> TikTok
> Policies
> Account

## Page Intent

**Type:** `landing` (confidence 0.45)
**Description:** Discover Altitude’s line of non-alcoholic beverages crafted with L-Theanine, Lion’s Mane, and Magnesium. Functional ingredients, and a balanced approach to meeting the moment

## Section Roles

Reading order (top→bottom): sidebar → content → nav → nav → nav → content → nav → nav → footer → nav → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | sidebar | talk@altitude.bev | 0.4 |
| 1 | content | talk@altitude.bev | 0.3 |
| 2 | nav | talk@altitude.bev | 0.9 |
| 3 | nav | talk@altitude.bev | 0.9 |
| 4 | nav | Menu | 0.4 |
| 5 | nav | — | 0.9 |
| 6 | nav | Menu | 0.9 |
| 7 | content | An Invigorated Classic Prickly Pear Margarita | 0.3 |
| 8 | footer | — | 0.95 |
| 9 | nav | — | 0.9 |
| 10 | nav | — | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.061 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 110px |
| backdrop-filter in use | no |
| Gradients | 7 |

## Imagery Style

**Label:** `photography` (confidence 0.182)
**Counts:** total 11, svg 1, icon 0, screenshot-like 0, photo-like 4
**Dominant aspect:** tall
**Radius profile on images:** square

## Component Library

**Detected:** `tailwindcss` (confidence 0.699)

Evidence:
- tailwind-like class density 68%

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `DepartureMono` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
