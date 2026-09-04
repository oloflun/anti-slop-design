# Design Language: Caractère Bois | Ébénisterie d'Art & Créations Modernes

> Extracted from `https://www.caractere-bois.fr` on September 4, 2026
> 664 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f4300f` | rgb(244, 48, 15) | hsl(9, 91%, 51%) | 448 |
| Secondary | `#0000ee` | rgb(0, 0, 238) | hsl(240, 100%, 47%) | 94 |
| Accent | `#9cc4ff` | rgb(156, 196, 255) | hsl(216, 100%, 81%) | 2 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#333333` | hsl(0, 0%, 20%) | 376 |
| `#eaeaea` | hsl(0, 0%, 92%) | 165 |
| `#000000` | hsl(0, 0%, 0%) | 79 |
| `#ffffff` | hsl(0, 0%, 100%) | 5 |

### Background Colors

Used on large-area elements: `#ffffff`, `#eaeaea`, `#f4300f`, `#9cc4ff`, `#540a04`

### Text Colors

Text color palette: `#000000`, `#333333`, `#eaeaea`, `#0000ee`, `#540a04`, `#ffffff`, `#f4300f`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#f4300f` | background, text, border | 448 |
| `#333333` | text, border | 376 |
| `#540a04` | text, border, background | 181 |
| `#eaeaea` | background, text, border | 165 |
| `#0000ee` | text, border | 94 |
| `#000000` | text, border | 79 |
| `#ffffff` | background, text, border | 5 |
| `#9cc4ff` | background | 2 |

## Typography

### Font Families

- **Arial** — used for all (310 elements)
- **PP Migra** — used for all (192 elements)
- **studiofeixensans** — used for all (65 elements)
- **PP migra** — used for body (57 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 136px | 8.5rem | 400 | 125.12px | normal | h5 |
| 100px | 6.25rem | 400 | 92px | normal | a, br, span, div |
| 51.2px | 3.2rem | 400 | 47.104px | normal | h2, div, span, h3 |
| 40px | 2.5rem | 400 | 40px | normal | div |
| 16px | 1rem | 400 | normal | normal | html, head, style, meta |
| 14px | 0.875rem | 400 | 20px | normal | body, section, div, svg |

### Heading Scale

```css
h5 { font-size: 136px; font-weight: 400; line-height: 125.12px; }
h2 { font-size: 100px; font-weight: 400; line-height: 92px; }
h2 { font-size: 51.2px; font-weight: 400; line-height: 47.104px; }
h1 { font-size: 16px; font-weight: 400; line-height: normal; }
```

### Body Text

```css
body { font-size: 100px; font-weight: 400; line-height: 92px; }
```

### Font Weights in Use

`400` (658x), `700` (4x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-58 | 58px | 3.625rem |
| spacing-82 | 82px | 5.125rem |
| spacing-370 | 370px | 23.125rem |
| spacing-478 | 478px | 29.875rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 8px | 1 |

## CSS Custom Properties

### Other

```css
--shop-pay-button-width: 100%;
--bleu_ciel: #9cc4ff;
--brun: #540a04;
--brun-50: #540a0480;
--scrollbar-width: 0px;
--orange: #f4300f;
--ciment: #eaeaea;
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

## Transitions & Animations

**Easing functions:** `[object Object]`

**Durations:** `1s`, `0.2s`, `0.4s`

### Common Transitions

```css
transition: all;
transition: opacity 1s ease-in-out;
transition: 0.2s;
transition: transform 0.4s;
transition: opacity 0.4s;
transition: color 0.4s, fill 0.4s, stroke 0.4s;
```

### Keyframe Animations

**dialog-fade-in**
```css
@keyframes dialog-fade-in {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

**dialog-slide-in-right**
```css
@keyframes dialog-slide-in-right {
  0% { transform: translate(100%); }
  100% { transform: translate(0px); }
}
```

**dialog-slide-in-top**
```css
@keyframes dialog-slide-in-top {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(0px); }
}
```

**dialog-slide-in-bottom**
```css
@keyframes dialog-slide-in-bottom {
  0% { transform: translateY(100%); }
  100% { transform: translateY(0px); }
}
```

**dialog-slide-in-left**
```css
@keyframes dialog-slide-in-left {
  0% { transform: translate(-100%); }
  100% { transform: translate(0px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (5 instances)

```css
.button {
  color: rgb(234, 234, 234);
  font-size: 14px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 0px;
}
```

### Cards (25 instances)

```css
.card {
  background-color: rgb(234, 234, 234);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (5 instances)

```css
.input {
  background-color: rgb(234, 234, 234);
  color: rgb(84, 10, 4);
  border-color: rgb(0, 0, 0) rgb(0, 0, 0) rgba(84, 10, 4, 0.5);
  border-radius: 0px;
  font-size: 14px;
  padding-top: 16px;
  padding-right: 8px;
}
```

### Links (32 instances)

```css
.link {
  color: rgb(0, 0, 238);
  font-size: 14px;
  font-weight: 400;
}
```

### Navigation (13 instances)

```css
.navigatio {
  background-color: rgb(244, 48, 15);
  color: rgb(234, 234, 234);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (9 instances)

```css
.foote {
  background-color: rgb(84, 10, 4);
  color: rgb(51, 51, 51);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 14px;
}
```

### Dropdowns (3 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(51, 51, 51);
  padding-top: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(234, 234, 234);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(234, 234, 234);
  font-size: 16px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(84, 10, 4);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(84, 10, 4);
  font-size: 14px;
  font-weight: 400;
```

### Button — 6 instances, 2 variants

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(84, 10, 4);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(84, 10, 4);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(234, 234, 234);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(234, 234, 234);
  font-size: 14px;
  font-weight: 400;
```

### Button — 4 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(234, 234, 234);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(234, 234, 234);
  font-size: 14px;
  font-weight: 400;
```

**Variant 2** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(84, 10, 4);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(84, 10, 4);
  font-size: 14px;
  font-weight: 400;
```

### Link — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 238);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 238);
  font-size: 14px;
  font-weight: 400;
```

### Card — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 238);
  padding: 16px 16px 16px 16px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 238);
  font-size: 14px;
  font-weight: 400;
```

### Card — 10 instances, 1 variant

**Variant 1** (10 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 238);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 238);
  font-size: 14px;
  font-weight: 400;
```

### Card — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgb(234, 234, 234);
  color: rgb(0, 0, 238);
  padding: 0px 0px 84.0625px 0px;
  border-radius: 0px;
  border: 0px none rgb(0, 0, 238);
  font-size: 14px;
  font-weight: 400;
```

### Input — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(234, 234, 234);
  color: rgb(84, 10, 4);
  padding: 16px 8px 16px 8px;
  border-radius: 0px;
  border: 0px 0px 1px solid rgb(0, 0, 0) rgb(0, 0, 0) rgba(84, 10, 4, 0.5);
  font-size: 14px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(234, 234, 234);
  color: rgb(84, 10, 4);
  padding: 16px 8px 16px 8px;
  border-radius: 0px;
  border: 0px 0px 1px solid rgb(0, 0, 0) rgb(0, 0, 0) rgba(84, 10, 4, 0.5);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(84, 10, 4);
  padding: 0px 0px 0px 20px;
  border-radius: 0px;
  border: 0px none rgb(84, 10, 4);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**2 grid containers** and **76 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 100% | 0px |
| 1270px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 13-column | 1x |
| 4-column | 1x |

### Grid Templates

```css
grid-template-columns: 280.25px 280.25px 280.25px 280.25px;
gap: 32px;
grid-template-columns: 172px 152.156px 152.172px 152.172px 152.156px 152.172px 152.156px 152.156px 152.172px 152.156px 152.156px 152.172px 152.172px;
gap: 40px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 51x |
| column/nowrap | 25x |

**Gap values:** `16px`, `24px`, `2px`, `32px`, `40px`, `48px`, `58px`, `7px`, `8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 83/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 85/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 75/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 4 font families — consider limiting to 2 (heading + body)
- 96 !important rules — prefer specificity over overrides
- 78% of CSS is unused — consider purging
- 1453 duplicate CSS declarations

## Z-Index Map

**11 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9999,99999 | div.e.r.r.o.r. .w.-.f.o.r.m.-.f.a.i.l, div.p.a.n.i.e.r.-.c.o.n.t.a.i.n.e.r |
| dropdown | 990,999 | nav.n.a.v.b.a.r. .w.-.v.a.r.i.a.n.t.-.2.b.6.b.7.e.e.5.-.1.f.7.5.-.6.9.8.3.-.c.f.9.d.-.2.f.b.d.6.e.3.7.4.a.c.7, section.s.e.c.t.i.o.n._.t.r.a.n.s.i.t.i.o.n, div.m.e.n.u |
| base | -100,3 | video, img.i.m.a.g.e._.c.a.r.d._.p.r.o.d.u.c.t, img.i.m.a.g.e._.c.a.r.d._.p.r.o.d.u.c.t |

**Issues:**
- [object Object]

## SVG Icons

**7 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 2 |
| lg | 1 |
| xl | 4 |

**Icon colors:** `currentColor`, `#fff`, `white`, `#540A04`, `#F4300F`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| webflow-icons | self-hosted | 400 | normal |
| studiofeixensans | self-hosted | 400 | normal |
| PP Migra | self-hosted | 400 | italic |
| PP migra | self-hosted | 400 | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 10 | objectFit: cover, borderRadius: 0px, shape: square |
| gallery | 5 | objectFit: fill, borderRadius: 0px, shape: square |
| hero | 2 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 2:3 (10x), 3:4 (5x), 3:2 (2x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `sm` | `200ms` | 200 |
| `md` | `400ms` | 400 |
| `xl` | `1s` | 1000 |

### Easing Families

- **ease-in-out** (1 uses) — `ease`

## Component Anatomy

### card — 20 instances

**Slots:** description, media

### button — 13 instances

**Slots:** label

### link — 5 instances


### input — 3 instances


## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Sentence case (verbose)

### Top CTA Verbs

- **le** (3)
- **tous** (2)
- **fermer** (1)
- **propos** (1)
- **nous** (1)
- **la** (1)
- **table** (1)

### Button Copy Patterns

- "fermer" (1×)
- "à propos" (1×)
- "tous les projets" (1×)
- "nous contacter" (1×)
- "tous les articles" (1×)
- "la petite frêne
36 x 18 x 2,5
30
€" (1×)
- "le mini billot
50
€" (1×)
- "le petit banc
58 x 23 x 45
190
€" (1×)
- "le banc origine
100 x 25 x 45
250
€" (1×)
- "table croisée
55 x 55 x 55
450
€" (1×)

### Sample Headings

> MATIÈRE PREMIÈRE
& MANIÈRE DE FAIRE
> Caractère Bois, c’est l’alliance subtile entre héritage artisanal et modernité. Un savoir-faire d’exception porté par des mains expertes, où chaque création raconte l’histoire d’une passion pour le bois.
> Ébéniste
moderne
> Le sur-mesure
> Un projet
en tête ?
> La boutique
> Contacter
Caractère Bois

## Page Intent

**Type:** `landing` (confidence 0.75)
**Description:** Caractère Bois, votre ébéniste moderne. De la conception à la réalisation, nous donnons vie à vos projets en bois avec créativité et précision. Visitez notre boutique et nos projets.

## Section Roles

Reading order (top→bottom): content → hero → content → nav → content → hero → content → hero → hero → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | content | — | 0.3 |
| 1 | nav | — | 0.9 |
| 2 | hero | MATIÈRE PREMIÈRE
& MANIÈRE DE FAIRE | 0.85 |
| 3 | content | Caractère Bois, c’est l’alliance subtile entre héritage artisanal et modernité.  | 0.3 |
| 4 | hero | Ébéniste
moderne | 0.4 |
| 5 | content | Le sur-mesure | 0.3 |
| 6 | hero | La boutique | 0.4 |
| 7 | hero | Contacter
Caractère Bois | 0.4 |
| 8 | footer | — | 0.95 |
| 9 | content | — | 0.3 |

## Material Language

**Label:** `flat` (confidence 0.55)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.41 |
| Shadow profile | none |
| Avg shadow blur | 0px |
| Max radius | 8px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `photography` (confidence 0.529)
**Counts:** total 17, svg 0, icon 0, screenshot-like 0, photo-like 16
**Dominant aspect:** portrait
**Radius profile on images:** square

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Arial` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
