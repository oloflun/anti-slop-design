# Design Language: Office Lunches, Catering and Team Orders — 50+ restaurants for your team

> Extracted from `https://trypicnic.com` on September 4, 2026
> 1037 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f7f6f2` | rgb(247, 246, 242) | hsl(48, 24%, 96%) | 405 |
| Secondary | `#f74c25` | rgb(247, 76, 37) | hsl(11, 93%, 56%) | 603 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 992 |
| `#000000` | hsl(0, 0%, 0%) | 22 |
| `#12110c` | hsl(50, 20%, 6%) | 8 |
| `#525252` | hsl(0, 0%, 32%) | 7 |
| `#ffffff` | hsl(0, 0%, 100%) | 3 |
| `#cacac3` | hsl(60, 6%, 78%) | 2 |

### Background Colors

Used on large-area elements: `#f7f6f2`, `#f74c25`

### Text Colors

Text color palette: `#f74c25`, `#f7f6f2`, `#000000`, `#525252`, `#12110c`, `#141414`

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border | 992 |
| `#f74c25` | text, background, border | 603 |
| `#f7f6f2` | background, text, border | 405 |
| `#000000` | text, border | 22 |
| `#12110c` | text | 8 |
| `#525252` | text, border | 7 |
| `#ffffff` | background | 3 |
| `#cacac3` | border | 2 |

## Typography

### Font Families

- **__Inter_f367f3** — used for all (905 elements)
- **Arial** — used for all (60 elements)
- **__p22MackinacPro_6ce25e** — used for all (35 elements)
- **Inter** — used for all (33 elements)
- **__interDisplay_4fc95a** — used for all (4 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 82px | 5.125rem | 500 | 65.6px | -4.1px | div, p, em, img |
| 60px | 3.75rem | 500 | 63.6px | -1.74px | p, a, h1, span |
| 36px | 2.25rem | 500 | 39.6px | -0.36px | p |
| 30px | 1.875rem | 500 | 36px | -0.3px | h2, h3, span, a |
| 24px | 1.5rem | 500 | 28.8px | -0.24px | p, h3, br |
| 20px | 1.25rem | 500 | 22px | -0.08px | p, a, span, h3 |
| 18px | 1.125rem | 500 | 19.8px | -0.0324px | button, div, svg, path |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, link |
| 14px | 0.875rem | 400 | 18.2px | normal | p, div, label, input |
| 12px | 0.75rem | 500 | 12px | normal | a |

### Heading Scale

```css
h1 { font-size: 60px; font-weight: 500; line-height: 63.6px; }
h2 { font-size: 30px; font-weight: 500; line-height: 36px; }
h3 { font-size: 24px; font-weight: 500; line-height: 28.8px; }
h3 { font-size: 20px; font-weight: 500; line-height: 22px; }
```

### Body Text

```css
body { font-size: 16px; font-weight: 400; line-height: 24px; }
```

### Font Weights in Use

`400` (756x), `500` (279x), `530` (2x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-30 | 30px | 1.875rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-56 | 56px | 3.5rem |
| spacing-70 | 70px | 4.375rem |
| spacing-100 | 100px | 6.25rem |
| spacing-120 | 120px | 7.5rem |
| spacing-160 | 160px | 10rem |
| spacing-182 | 182px | 11.375rem |
| spacing-190 | 190px | 11.875rem |
| spacing-195 | 195px | 12.1875rem |
| spacing-240 | 240px | 15rem |
| spacing-282 | 282px | 17.625rem |
| spacing-320 | 320px | 20rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| md | 8px | 14 |
| lg | 16px | 1 |
| full | 9999px | 239 |

## Box Shadows

**lg** — blur: 25px
```css
box-shadow: rgba(0, 0, 0, 0.26) 0px 4px 25px 0px;
```

## CSS Custom Properties

### Colors

```css
--colors-data-standard-single: rgb(28,105,232);
--colors-data-standard-sentiment-negative: rgb(223,82,52);
--colors-data-standard-sentiment-notice: rgb(228,180,48);
--colors-data-standard-sentiment-positive: rgb(57,166,82);
--colors-data-categorical-10: rgb(242,123,97);
--colors-data-categorical-11: rgb(197,201,72);
--colors-data-categorical-12: rgb(46,175,188);
--colors-data-categorical-13: rgb(101,202,125);
--colors-data-categorical-14: rgb(72, 121, 26);
--colors-data-categorical-15: rgb(146, 72, 30);
--colors-data-categorical-01: rgb(130,52,218);
--colors-data-categorical-02: rgb(19,141,155);
--colors-data-categorical-03: rgb(209,44,115);
--colors-data-categorical-04: rgb(57,166,82);
--colors-data-categorical-05: rgb(223,82,52);
--colors-data-categorical-06: rgb(252,199,58);
--colors-data-categorical-07: rgb(21,136,213);
--colors-data-categorical-08: rgb(233,153,51);
--colors-data-categorical-09: rgb(54,61,209);
--colors-data-sequential-single-01: rgb(18,88,210);
--colors-data-sequential-single-02: rgb(28,105,232);
--colors-data-sequential-single-03: rgb(60,131,239);
--colors-data-sequential-single-04: rgb(106,162,244);
--colors-data-sequential-single-05: rgb(156,192,247);
--colors-data-sequential-single-06: rgb(191,216,250);
--colors-data-sequential-single-07: rgb(217,232,253);
--colors-data-sequential-gray-01: rgb(61, 61, 61);
--colors-data-sequential-gray-02: rgb(108, 108, 108);
--colors-data-sequential-gray-03: rgb(135, 134, 134);
--colors-data-sequential-gray-04: rgb(170, 170, 170);
--colors-data-sequential-gray-05: rgb(221, 221, 221);
--colors-data-sequential-gray-06: rgb(238, 238, 238);
--colors-data-sequential-purple-01: rgb(130,52,218);
--colors-data-sequential-purple-02: rgb(145,66,236);
--colors-data-sequential-purple-03: rgb(168,98,242);
--colors-data-sequential-purple-04: rgb(185,130,242);
--colors-data-sequential-purple-05: rgb(209,170,249);
--colors-data-sequential-purple-06: rgb(230,203,255);
--colors-data-sequential-purple-07: rgb(234,220,252);
--colors-data-sequential-teal-01: rgb(19,141,155);
--colors-data-sequential-teal-02: rgb(27,157,175);
--colors-data-sequential-teal-03: rgb(46,175,188);
--colors-data-sequential-teal-04: rgb(90,201,210);
--colors-data-sequential-teal-05: rgb(137,218,224);
--colors-data-sequential-teal-06: rgb(177,231,237);
--colors-data-sequential-teal-07: rgb(207,242,243);
--colors-data-sequential-pink-01: rgb(209,44,115);
--colors-data-sequential-pink-02: rgb(224,57,117);
--colors-data-sequential-pink-03: rgb(244,84,152);
--colors-data-sequential-pink-04: rgb(249,126,179);
--colors-data-sequential-pink-05: rgb(252,166,203);
--colors-data-sequential-pink-06: rgb(254,197,222);
--colors-data-sequential-pink-07: rgb(255,220,236);
--colors-data-sequential-green-01: rgb(57,166,82);
--colors-data-sequential-green-02: rgb(70,183,96);
--colors-data-sequential-green-03: rgb(101,202,125);
--colors-data-sequential-green-04: rgb(139,215,157);
--colors-data-sequential-green-05: rgb(177,229,191);
--colors-data-sequential-green-06: rgb(206,238,214);
--colors-data-sequential-green-07: rgb(226,246,230);
--colors-data-sequential-scarlet-01: rgb(223,82,52);
--colors-data-sequential-scarlet-02: rgb(239,95,62);
--colors-data-sequential-scarlet-03: rgb(242,123,97);
--colors-data-sequential-scarlet-04: rgb(246,154,134);
--colors-data-sequential-scarlet-05: rgb(249,190,178);
--colors-data-sequential-scarlet-06: rgb(251,213,204);
--colors-data-sequential-scarlet-07: rgb(253,230,226);
--colors-data-sequential-yellow-01: rgb(228,180,48);
--colors-data-sequential-yellow-02: rgb(252,199,58);
--colors-data-sequential-yellow-03: rgb(254,214,106);
--colors-data-sequential-yellow-04: rgb(255,228,156);
--colors-data-sequential-yellow-05: rgb(255,238,190);
--colors-data-sequential-yellow-06: rgb(255,244,214);
--colors-data-sequential-yellow-07: rgb(255,250,234);
--colors-data-sequential-cyan-01: rgb(13,118,189);
--colors-data-sequential-cyan-02: rgb(21,136,213);
--colors-data-sequential-cyan-03: rgb(87,182,233);
--colors-data-sequential-cyan-04: rgb(87,182,233);
--colors-data-sequential-cyan-05: rgb(138,207,241);
--colors-data-sequential-cyan-06: rgb(178,223,245);
--colors-data-sequential-cyan-07: rgb(207,237,250);
--colors-data-sequential-gold-01: rgb(233,153,51);
--colors-data-sequential-gold-02: rgb(255,173,72);
--colors-data-sequential-gold-03: rgb(255,191,98);
--colors-data-sequential-gold-04: rgb(255,207,138);
--colors-data-sequential-gold-05: rgb(255,222,170);
--colors-data-sequential-gold-06: rgb(255,233,202);
--colors-data-sequential-gold-07: rgb(255,242,220);
--colors-data-sequential-indigo-01: rgb(54,61,209);
--colors-data-sequential-indigo-02: rgb(70,78,231);
--colors-data-sequential-indigo-03: rgb(97,102,233);
--colors-data-sequential-indigo-04: rgb(135,140,243);
--colors-data-sequential-indigo-05: rgb(176,179,244);
--colors-data-sequential-indigo-06: rgb(205,207,248);
--colors-data-sequential-indigo-07: rgb(224,223,251);
--colors-data-sequential-olive-01: rgb(179,184,59);
--colors-data-sequential-olive-02: rgb(197,201,72);
--colors-data-sequential-olive-03: rgb(211,214,105);
--colors-data-sequential-olive-04: rgb(222,224,142);
--colors-data-sequential-olive-05: rgb(233,234,179);
--colors-data-sequential-olive-06: rgb(241,242,207);
--colors-data-sequential-olive-07: rgb(247,247,226);
--colors-dataviz-gray-10: rgb(44, 44, 48);
--colors-dataviz-gray-11: rgb(34, 34, 37);
--colors-dataviz-gray-12: rgb(25, 24, 27);
--colors-dataviz-gray-13: rgb(15, 15, 16);
--colors-dataviz-gray-00: rgb(239, 239, 240);
--colors-dataviz-gray-01: rgb(223, 223, 226);
--colors-dataviz-gray-02: rgb(202, 202, 206);
--colors-dataviz-gray-03: rgb(181, 181, 186);
--colors-dataviz-gray-04: rgb(160, 160, 167);
--colors-dataviz-gray-05: rgb(139, 138, 147);
--colors-dataviz-gray-06: rgb(118, 118, 127);
--colors-dataviz-gray-07: rgb(98, 98, 106);
--colors-dataviz-gray-08: rgb(79, 78, 85);
--colors-dataviz-gray-09: rgb(59, 59, 64);
--colors-dataviz-magenta-red-10: rgb(72, 20, 25);
--colors-dataviz-magenta-red-11: rgb(56, 16, 20);
--colors-dataviz-magenta-red-12: rgb(40, 11, 14);
--colors-dataviz-magenta-red-13: rgb(24, 7, 8);
--colors-dataviz-magenta-red-00: rgb(248, 231, 233);
--colors-dataviz-magenta-red-01: rgb(242, 207, 211);
--colors-dataviz-magenta-red-02: rgb(233, 175, 181);
--colors-dataviz-magenta-red-03: rgb(224, 144, 152);
--colors-dataviz-magenta-red-04: rgb(215, 112, 122);
--colors-dataviz-magenta-red-05: rgb(206, 80, 93);
--colors-dataviz-magenta-red-06: rgb(191, 54, 68);
--colors-dataviz-magenta-red-07: rgb(159, 45, 56);
--colors-dataviz-magenta-red-08: rgb(127, 36, 45);
--colors-dataviz-magenta-red-09: rgb(95, 27, 34);
--colors-dataviz-red-orange-10: rgb(72, 33, 20);
--colors-dataviz-red-orange-11: rgb(56, 26, 16);
--colors-dataviz-red-orange-12: rgb(40, 18, 11);
--colors-dataviz-red-orange-13: rgb(24, 11, 7);
--colors-dataviz-red-orange-00: rgb(248, 235, 231);
--colors-dataviz-red-orange-01: rgb(242, 216, 207);
--colors-dataviz-red-orange-02: rgb(233, 190, 175);
--colors-dataviz-red-orange-03: rgb(224, 164, 144);
--colors-dataviz-red-orange-04: rgb(215, 137, 112);
--colors-dataviz-red-orange-05: rgb(206, 111, 80);
--colors-dataviz-red-orange-06: rgb(191, 88, 54);
--colors-dataviz-red-orange-07: rgb(159, 73, 45);
--colors-dataviz-red-orange-08: rgb(127, 59, 36);
--colors-dataviz-red-orange-09: rgb(95, 44, 27);
--colors-dataviz-orange-10: rgb(72, 46, 20);
--colors-dataviz-orange-11: rgb(56, 36, 16);
--colors-dataviz-orange-12: rgb(40, 26, 11);
--colors-dataviz-orange-13: rgb(24, 15, 7);
--colors-dataviz-orange-00: rgb(248, 240, 231);
--colors-dataviz-orange-01: rgb(242, 224, 207);
--colors-dataviz-orange-02: rgb(233, 204, 175);
--colors-dataviz-orange-03: rgb(224, 184, 144);
--colors-dataviz-orange-04: rgb(215, 163, 112);
--colors-dataviz-orange-05: rgb(206, 143, 80);
--colors-dataviz-orange-06: rgb(191, 122, 54);
--colors-dataviz-orange-07: rgb(159, 102, 45);
--colors-dataviz-orange-08: rgb(127, 82, 36);
--colors-dataviz-orange-09: rgb(95, 61, 27);
--colors-dataviz-orange-yellow-10: rgb(83, 64, 9);
--colors-dataviz-orange-yellow-11: rgb(64, 50, 7);
--colors-dataviz-orange-yellow-12: rgb(46, 36, 5);
--colors-dataviz-orange-yellow-13: rgb(28, 21, 3);
--colors-dataviz-orange-yellow-00: rgb(252, 246, 227);
--colors-dataviz-orange-yellow-01: rgb(249, 237, 200);
--colors-dataviz-orange-yellow-02: rgb(245, 224, 163);
--colors-dataviz-orange-yellow-03: rgb(241, 212, 126);
--colors-dataviz-orange-yellow-04: rgb(237, 200, 90);
--colors-dataviz-orange-yellow-05: rgb(233, 188, 53);
--colors-dataviz-orange-yellow-06: rgb(220, 171, 24);
--colors-dataviz-orange-yellow-07: rgb(184, 143, 20);
--colors-dataviz-orange-yellow-08: rgb(147, 114, 16);
--colors-dataviz-orange-yellow-09: rgb(110, 86, 12);
--colors-dataviz-yellow-lime-10: rgb(59, 72, 20);
--colors-dataviz-yellow-lime-11: rgb(46, 56, 16);
--colors-dataviz-yellow-lime-12: rgb(33, 40, 11);
--colors-dataviz-yellow-lime-13: rgb(20, 24, 7);
--colors-dataviz-yellow-lime-00: rgb(244, 248, 231);
--colors-dataviz-yellow-lime-01: rgb(233, 242, 207);
--colors-dataviz-yellow-lime-02: rgb(218, 233, 175);
--colors-dataviz-yellow-lime-03: rgb(204, 224, 144);
--colors-dataviz-yellow-lime-04: rgb(189, 215, 112);
--colors-dataviz-yellow-lime-05: rgb(174, 206, 80);
--colors-dataviz-yellow-lime-06: rgb(157, 191, 54);
--colors-dataviz-yellow-lime-07: rgb(131, 159, 45);
--colors-dataviz-yellow-lime-08: rgb(104, 127, 36);
--colors-dataviz-yellow-lime-09: rgb(78, 95, 27);
--colors-dataviz-lime-green-10: rgb(35, 68, 24);
--colors-dataviz-lime-green-11: rgb(27, 53, 19);
--colors-dataviz-lime-green-12: rgb(19, 38, 13);
--colors-dataviz-lime-green-13: rgb(12, 23, 8);
--colors-dataviz-lime-green-00: rgb(236, 247, 232);
--colors-dataviz-lime-green-01: rgb(217, 239, 210);
--colors-dataviz-lime-green-02: rgb(192, 228, 180);
--colors-dataviz-lime-green-03: rgb(166, 218, 149);
--colors-dataviz-lime-green-04: rgb(141, 207, 119);
--colors-dataviz-lime-green-05: rgb(116, 197, 89);
--colors-dataviz-lime-green-06: rgb(93, 181, 64);
--colors-dataviz-lime-green-07: rgb(78, 151, 53);
--colors-dataviz-lime-green-08: rgb(62, 121, 42);
--colors-dataviz-lime-green-09: rgb(47, 91, 32);
--colors-dataviz-mint-aqua-10: rgb(24, 68, 57);
--colors-dataviz-mint-aqua-11: rgb(19, 53, 44);
--colors-dataviz-mint-aqua-12: rgb(13, 38, 32);
--colors-dataviz-mint-aqua-13: rgb(8, 23, 19);
--colors-dataviz-mint-aqua-00: rgb(232, 247, 243);
--colors-dataviz-mint-aqua-01: rgb(210, 239, 232);
--colors-dataviz-mint-aqua-02: rgb(180, 228, 216);
--colors-dataviz-mint-aqua-03: rgb(149, 218, 201);
--colors-dataviz-mint-aqua-04: rgb(119, 207, 185);
--colors-dataviz-mint-aqua-05: rgb(89, 197, 170);
--colors-dataviz-mint-aqua-06: rgb(64, 181, 152);
--colors-dataviz-mint-aqua-07: rgb(53, 151, 126);
--colors-dataviz-mint-aqua-08: rgb(42, 121, 101);
--colors-dataviz-mint-aqua-09: rgb(32, 91, 76);
--colors-dataviz-aqua-blue-10: rgb(20, 59, 72);
--colors-dataviz-aqua-blue-11: rgb(16, 46, 56);
--colors-dataviz-aqua-blue-12: rgb(11, 33, 40);
--colors-dataviz-aqua-blue-13: rgb(7, 20, 24);
--colors-dataviz-aqua-blue-00: rgb(231, 244, 248);
--colors-dataviz-aqua-blue-01: rgb(207, 233, 242);
--colors-dataviz-aqua-blue-02: rgb(175, 218, 233);
--colors-dataviz-aqua-blue-03: rgb(144, 204, 224);
--colors-dataviz-aqua-blue-04: rgb(112, 189, 215);
--colors-dataviz-aqua-blue-05: rgb(80, 174, 206);
--colors-dataviz-aqua-blue-06: rgb(54, 157, 191);
--colors-dataviz-aqua-blue-07: rgb(45, 131, 159);
--colors-dataviz-aqua-blue-08: rgb(36, 104, 127);
--colors-dataviz-aqua-blue-09: rgb(27, 78, 95);
--colors-dataviz-blue-violet-10: rgb(20, 33, 72);
--colors-dataviz-blue-violet-11: rgb(16, 26, 56);
--colors-dataviz-blue-violet-12: rgb(11, 18, 40);
--colors-dataviz-blue-violet-13: rgb(7, 11, 24);
--colors-dataviz-blue-violet-00: rgb(231, 235, 248);
--colors-dataviz-blue-violet-01: rgb(207, 216, 242);
--colors-dataviz-blue-violet-02: rgb(175, 190, 233);
--colors-dataviz-blue-violet-03: rgb(144, 164, 224);
--colors-dataviz-blue-violet-04: rgb(112, 137, 215);
--colors-dataviz-blue-violet-05: rgb(80, 111, 206);
--colors-dataviz-blue-violet-06: rgb(54, 88, 191);
--colors-dataviz-blue-violet-07: rgb(45, 73, 159);
--colors-dataviz-blue-violet-08: rgb(36, 59, 127);
--colors-dataviz-blue-violet-09: rgb(27, 44, 95);
--colors-dataviz-violet-purple-10: rgb(35, 24, 68);
--colors-dataviz-violet-purple-11: rgb(27, 19, 53);
--colors-dataviz-violet-purple-12: rgb(19, 13, 38);
--colors-dataviz-violet-purple-13: rgb(12, 8, 23);
--colors-dataviz-violet-purple-00: rgb(236, 232, 247);
--colors-dataviz-violet-purple-01: rgb(217, 210, 239);
--colors-dataviz-violet-purple-02: rgb(192, 180, 228);
--colors-dataviz-violet-purple-03: rgb(166, 149, 218);
--colors-dataviz-violet-purple-04: rgb(141, 119, 207);
--colors-dataviz-violet-purple-05: rgb(116, 89, 197);
--colors-dataviz-violet-purple-06: rgb(93, 64, 181);
--colors-dataviz-violet-purple-07: rgb(78, 53, 151);
--colors-dataviz-violet-purple-08: rgb(62, 42, 121);
--colors-dataviz-violet-purple-09: rgb(47, 32, 91);
--colors-dataviz-purple-pink-10: rgb(57, 24, 68);
--colors-dataviz-purple-pink-11: rgb(44, 19, 53);
--colors-dataviz-purple-pink-12: rgb(32, 13, 38);
--colors-dataviz-purple-pink-13: rgb(19, 8, 23);
--colors-dataviz-purple-pink-00: rgb(243, 232, 247);
--colors-dataviz-purple-pink-01: rgb(232, 210, 239);
--colors-dataviz-purple-pink-02: rgb(216, 180, 228);
--colors-dataviz-purple-pink-03: rgb(201, 149, 218);
--colors-dataviz-purple-pink-04: rgb(185, 119, 207);
--colors-dataviz-purple-pink-05: rgb(170, 89, 197);
--colors-dataviz-purple-pink-06: rgb(152, 64, 181);
--colors-dataviz-purple-pink-07: rgb(126, 53, 151);
--colors-dataviz-purple-pink-08: rgb(101, 42, 121);
--colors-dataviz-purple-pink-09: rgb(76, 32, 91);
--colors-dataviz-red-vivid-10: rgb(83, 9, 9);
--colors-dataviz-red-vivid-11: rgb(64, 7, 7);
--colors-dataviz-red-vivid-12: rgb(46, 5, 5);
--colors-dataviz-red-vivid-13: rgb(28, 3, 3);
--colors-dataviz-red-vivid-00: rgb(252, 227, 227);
--colors-dataviz-red-vivid-01: rgb(249, 200, 200);
--colors-dataviz-red-vivid-02: rgb(245, 163, 163);
--colors-dataviz-red-vivid-03: rgb(241, 126, 126);
--colors-dataviz-red-vivid-04: rgb(237, 90, 90);
--colors-dataviz-red-vivid-05: rgb(233, 53, 53);
--colors-dataviz-red-vivid-06: rgb(220, 24, 24);
--colors-dataviz-red-vivid-07: rgb(184, 20, 20);
--colors-dataviz-red-vivid-08: rgb(147, 16, 16);
--colors-dataviz-red-vivid-09: rgb(110, 12, 12);
--colors-dataviz-red-orange-vivid-10: rgb(89, 24, 3);
--colors-dataviz-red-orange-vivid-11: rgb(69, 19, 2);
--colors-dataviz-red-orange-vivid-12: rgb(49, 14, 2);
--colors-dataviz-red-orange-vivid-13: rgb(30, 8, 1);
--colors-dataviz-red-orange-vivid-00: rgb(254, 233, 225);
--colors-dataviz-red-orange-vivid-01: rgb(253, 210, 196);
--colors-dataviz-red-orange-vivid-02: rgb(252, 180, 156);
--colors-dataviz-red-orange-vivid-03: rgb(251, 150, 116);
--colors-dataviz-red-orange-vivid-04: rgb(249, 120, 77);
--colors-dataviz-red-orange-vivid-05: rgb(248, 90, 37);
--colors-dataviz-red-orange-vivid-06: rgb(237, 65, 7);
--colors-dataviz-red-orange-vivid-07: rgb(198, 54, 6);
--colors-dataviz-red-orange-vivid-08: rgb(158, 43, 5);
--colors-dataviz-red-orange-vivid-09: rgb(119, 32, 4);
--colors-dataviz-orange-vivid-10: rgb(89, 46, 3);
--colors-dataviz-orange-vivid-11: rgb(69, 36, 2);
--colors-dataviz-orange-vivid-12: rgb(49, 26, 2);
--colors-dataviz-orange-vivid-13: rgb(30, 15, 1);
--colors-dataviz-orange-vivid-00: rgb(254, 240, 225);
--colors-dataviz-orange-vivid-01: rgb(253, 224, 196);
--colors-dataviz-orange-vivid-02: rgb(252, 204, 156);
--colors-dataviz-orange-vivid-03: rgb(251, 184, 116);
--colors-dataviz-orange-vivid-04: rgb(249, 163, 77);
--colors-dataviz-orange-vivid-05: rgb(248, 143, 37);
--colors-dataviz-orange-vivid-06: rgb(237, 122, 7);
--colors-dataviz-orange-vivid-07: rgb(198, 102, 6);
--colors-dataviz-orange-vivid-08: rgb(158, 82, 5);
--colors-dataviz-orange-vivid-09: rgb(119, 61, 4);
--colors-dataviz-orange-yellow-vivid-10: rgb(89, 67, 3);
--colors-dataviz-orange-yellow-vivid-11: rgb(69, 52, 2);
--colors-dataviz-orange-yellow-vivid-12: rgb(49, 37, 2);
--colors-dataviz-orange-yellow-vivid-13: rgb(30, 22, 1);
--colors-dataviz-orange-yellow-vivid-00: rgb(254, 247, 225);
--colors-dataviz-orange-yellow-vivid-01: rgb(253, 239, 196);
--colors-dataviz-orange-yellow-vivid-02: rgb(252, 228, 156);
--colors-dataviz-orange-yellow-vivid-03: rgb(251, 217, 116);
--colors-dataviz-orange-yellow-vivid-04: rgb(249, 206, 77);
--colors-dataviz-orange-yellow-vivid-05: rgb(248, 196, 37);
--colors-dataviz-orange-yellow-vivid-06: rgb(237, 180, 7);
--colors-dataviz-orange-yellow-vivid-07: rgb(198, 150, 6);
--colors-dataviz-orange-yellow-vivid-08: rgb(158, 120, 5);
--colors-dataviz-orange-yellow-vivid-09: rgb(119, 90, 4);
--colors-dataviz-green-mint-vivid-10: rgb(17, 75, 31);
--colors-dataviz-green-mint-vivid-11: rgb(13, 59, 24);
--colors-dataviz-green-mint-vivid-12: rgb(9, 42, 17);
--colors-dataviz-green-mint-vivid-13: rgb(6, 25, 10);
--colors-dataviz-green-mint-vivid-00: rgb(230, 249, 235);
--colors-dataviz-green-mint-vivid-01: rgb(205, 244, 215);
--colors-dataviz-green-mint-vivid-02: rgb(171, 237, 188);
--colors-dataviz-green-mint-vivid-03: rgb(138, 229, 161);
--colors-dataviz-green-mint-vivid-04: rgb(104, 222, 134);
--colors-dataviz-green-mint-vivid-05: rgb(71, 215, 107);
--colors-dataviz-green-mint-vivid-06: rgb(44, 201, 83);
--colors-dataviz-green-mint-vivid-07: rgb(37, 167, 69);
--colors-dataviz-green-mint-vivid-08: rgb(29, 134, 55);
--colors-dataviz-green-mint-vivid-09: rgb(22, 100, 42);
--colors-dataviz-aqua-blue-vivid-10: rgb(6, 66, 86);
--colors-dataviz-aqua-blue-vivid-11: rgb(4, 51, 67);
--colors-dataviz-aqua-blue-vivid-12: rgb(3, 37, 48);
--colors-dataviz-aqua-blue-vivid-13: rgb(2, 22, 29);
--colors-dataviz-aqua-blue-vivid-00: rgb(226, 246, 253);
--colors-dataviz-aqua-blue-vivid-01: rgb(197, 238, 251);
--colors-dataviz-aqua-blue-vivid-02: rgb(159, 226, 249);
--colors-dataviz-aqua-blue-vivid-03: rgb(121, 215, 246);
--colors-dataviz-aqua-blue-vivid-04: rgb(82, 204, 244);
--colors-dataviz-aqua-blue-vivid-05: rgb(44, 192, 242);
--colors-dataviz-aqua-blue-vivid-06: rgb(15, 176, 230);
--colors-dataviz-aqua-blue-vivid-07: rgb(12, 147, 192);
--colors-dataviz-aqua-blue-vivid-08: rgb(10, 118, 153);
--colors-dataviz-aqua-blue-vivid-09: rgb(7, 88, 115);
--colors-dataviz-purple-vivid-10: rgb(46, 3, 89);
--colors-dataviz-purple-vivid-11: rgb(36, 2, 69);
--colors-dataviz-purple-vivid-12: rgb(26, 2, 49);
--colors-dataviz-purple-vivid-13: rgb(15, 1, 30);
--colors-dataviz-purple-vivid-00: rgb(240, 225, 254);
--colors-dataviz-purple-vivid-01: rgb(224, 196, 253);
--colors-dataviz-purple-vivid-02: rgb(204, 156, 252);
--colors-dataviz-purple-vivid-03: rgb(184, 116, 251);
--colors-dataviz-purple-vivid-04: rgb(163, 77, 249);
--colors-dataviz-purple-vivid-05: rgb(143, 37, 248);
--colors-dataviz-purple-vivid-06: rgb(122, 7, 237);
--colors-dataviz-purple-vivid-07: rgb(102, 6, 198);
--colors-dataviz-purple-vivid-08: rgb(82, 5, 158);
--colors-dataviz-purple-vivid-09: rgb(61, 4, 119);
--colors-static-background-standard: rgb(255,255,255);
--colors-static-background-strong: rgb(239,239,239);
--colors-static-background-weak: rgb(245,245,245);
--colors-static-background-inverse-standard: #F7F6F2;
--colors-static-background-inverse-strong: rgb(13,13,13);
--colors-static-background-inverse-weak: rgb(31,31,31);
--colors-static-background-sentiment-negative: rgba(218,37,47, 0.08);
--colors-static-background-sentiment-positive: rgba(70,183,96, 0.12);
--colors-static-background-sentiment-notice: rgba(228,180,48, 0.16);
--colors-static-background-sentiment-info: #FEEDE9;
--colors-static-background-sentiment-neutral: rgba(26,26,26, 0.08);
--colors-static-background-sentiment-inverse-negative: rgb(218,37,47);
--colors-static-background-sentiment-inverse-positive: rgb(70,183,96);
--colors-static-background-sentiment-inverse-notice: rgb(228,180,48);
--colors-static-background-sentiment-inverse-info: rgba(18,88,210, 0.9);
--colors-static-background-sentiment-inverse-neutral: rgb(26,26,26);
--colors-static-divider-standard: rgba(0,0,0, 0.12);
--colors-static-divider-strong: rgba(0,0,0, 0.16);
--colors-static-divider-weak: #12110C14;
--colors-static-divider-inverse-standard: rgba(255,255,255, 0.32);
--colors-static-divider-inverse-strong: rgba(255,255,255, 0.48);
--colors-static-divider-inverse-weak: rgba(255,255,255, 0.24);
--colors-static-text-standard: #525252;
--colors-static-text-strong: #12110C;
--colors-static-text-weak: #6C6C6C;
--colors-static-text-inverse-standard: #F7F6F2;
--colors-static-text-inverse-strong: #F7F6F2;
--colors-static-text-inverse-weak: rgb(204,204,204);
--colors-static-text-sentiment-negative: rgb(197,35,43);
--colors-static-text-sentiment-positive: rgb(42,126,61);
--colors-static-text-sentiment-notice: rgb(134,105,30);
--colors-static-text-sentiment-info: #F74C25;
--colors-static-text-sentiment-neutral: rgb(61,61,61);
--colors-static-text-sentiment-inverse-negative: rgb(246,195,199);
--colors-static-text-sentiment-inverse-positive: rgb(177,229,191);
--colors-static-text-sentiment-inverse-notice: rgb(255,228,156);
--colors-static-text-sentiment-inverse-info: rgb(156,192,247);
--colors-static-text-sentiment-inverse-neutral: rgb(204,204,204);
--colors-interactive-fill-primary-enabled: #F74C25;
--colors-interactive-fill-primary-hover: #F4603E;
--colors-interactive-fill-primary-pressed: #D73814;
--colors-interactive-fill-primary-disabled: #DDD8D5;
--colors-interactive-fill-primary-on-primary: #F7F6F2;
--colors-interactive-fill-primary-on-disabled: rgb(143,143,143);
--colors-interactive-fill-secondary-enabled: #141414;
--colors-interactive-fill-secondary-hover: #292929;
--colors-interactive-fill-secondary-pressed: #454749;
--colors-interactive-fill-secondary-disabled: #8F8F8F4D;
--colors-interactive-fill-secondary-on-secondary: #FFFFFF;
--colors-interactive-fill-secondary-on-disabled: #8F8F8F99;
--colors-interactive-fill-tertiary-enabled: rgba(0,0,0, 0.06);
--colors-interactive-fill-tertiary-hover: rgba(0,0,0, 0.12);
--colors-interactive-fill-tertiary-pressed: rgba(0,0,0, 0.2);
--colors-interactive-fill-tertiary-disabled: rgb(245,245,245);
--colors-interactive-fill-tertiary-on-tertiary: rgb(82,82,82);
--colors-interactive-fill-tertiary-on-disabled: rgb(143,143,143);
--colors-interactive-fill-inverse-enabled: #F7F6F2;
--colors-interactive-fill-inverse-hover: rgb(239,239,239);
--colors-interactive-fill-inverse-pressed: rgb(214,214,214);
--colors-interactive-fill-inverse-disabled: rgb(108,108,108);
--colors-interactive-fill-inverse-on-inverse: #F74C25;
--colors-interactive-fill-inverse-on-disabled: rgb(204,204,204);
--colors-interactive-fill-danger-enabled: rgb(218,37,47);
--colors-interactive-fill-danger-hover: rgb(197,35,43);
--colors-interactive-fill-danger-pressed: rgb(170,30,36);
--colors-interactive-fill-danger-disabled: rgb(214,214,214);
--colors-interactive-fill-danger-on-danger: rgb(255,255,255);
--colors-interactive-fill-danger-on-disabled: rgb(143,143,143);
--colors-interactive-overlay-primary-enabled: rgba(28,105,232, 0);
--colors-interactive-overlay-primary-hover: rgba(28,105,232, 0.06);
--colors-interactive-overlay-primary-pressed: #FEEDE9;
--colors-interactive-overlay-primary-selected-enabled: rgba(28,105,232, 0.08);
--colors-interactive-overlay-primary-selected-hover: rgba(28,105,232, 0.14);
--colors-interactive-overlay-primary-selected-pressed: rgba(28,105,232, 0.18);
--colors-interactive-overlay-secondary-enabled: rgba(0,0,0, 0);
--colors-interactive-overlay-secondary-hover: rgba(0,0,0, 0.05);
--colors-interactive-overlay-secondary-pressed: rgba(0,0,0, 0.09);
--colors-interactive-overlay-secondary-selected-enabled: rgba(0,0,0, 0.08);
--colors-interactive-overlay-secondary-selected-hover: rgba(0,0,0, 0.13);
--colors-interactive-overlay-secondary-selected-pressed: rgba(0,0,0, 0.16);
--colors-interactive-overlay-inverse-enabled: rgba(255,255,255, 0);
--colors-interactive-overlay-inverse-hover: rgba(255,255,255, 0.04);
--colors-interactive-overlay-inverse-pressed: rgba(255,255,255, 0.12);
--colors-interactive-overlay-inverse-selected-enabled: rgba(255,255,255, 0.1);
--colors-interactive-overlay-inverse-selected-hover: rgba(255,255,255, 0.16);
--colors-interactive-overlay-inverse-selected-pressed: rgba(255,255,255, 0.24);
--colors-interactive-outline-primary-enabled: rgb(191,216,250);
--colors-interactive-outline-primary-hover: rgb(156,192,247);
--colors-interactive-outline-primary-pressed: #BB2807;
--colors-interactive-outline-primary-disabled: rgb(217,232,253);
--colors-interactive-outline-primary-selected-enabled: rgb(28,105,232);
--colors-interactive-outline-primary-selected-hover: rgb(18,88,210);
--colors-interactive-outline-primary-selected-pressed: rgb(14,73,180);
--colors-interactive-outline-secondary-enabled: #CACAC3;
--colors-interactive-outline-secondary-hover: #A3A3A3;
--colors-interactive-outline-secondary-pressed: #8F8F8F;
--colors-interactive-outline-secondary-disabled: rgb(214,214,214);
--colors-interactive-outline-secondary-selected-enabled: rgb(0,0,0);
--colors-interactive-outline-secondary-selected-hover: rgb(69,71,73);
--colors-interactive-outline-secondary-selected-pressed: rgb(61,61,61);
--colors-interactive-outline-inverse-enabled: rgb(108,108,108);
--colors-interactive-outline-inverse-hover: rgb(143,143,143);
--colors-interactive-outline-inverse-pressed: rgb(153,153,153);
--colors-interactive-outline-inverse-disabled: rgb(82,82,82);
--colors-interactive-outline-inverse-selected-enabled: rgb(163,163,163);
--colors-interactive-outline-inverse-selected-hover: rgb(204,204,204);
--colors-interactive-outline-inverse-selected-pressed: rgb(214,214,214);
--colors-interactive-outline-danger-enabled: rgb(231,71,80);
--colors-interactive-outline-danger-hover: rgb(218,37,47);
--colors-interactive-outline-danger-pressed: rgb(197,35,43);
--colors-interactive-outline-danger-disabled: rgb(214,214,214);
--z-indices-secondary-navigation: 3000;
--z-indices-primary-navigation: 5000;
--static-primary: var(--colors-interactive-fill-primary-enabled);
--static-primary-on-primary: var( --colors-interactive-fill-primary-on-primary );
--static-primary-hover: var(--colors-interactive-fill-primary-hover);
--static-primary-pressed: var(--colors-interactive-fill-primary-pressed);
--secondary: var(--colors-interactive-fill-secondary-enabled);
--secondary-on-secondary: var( --colors-interactive-fill-secondary-on-secondary );
--secondary-hover: var(--colors-interactive-fill-secondary-hover);
--secondary-pressed: var(--colors-interactive-fill-secondary-pressed);
--static-secondary: var(--colors-interactive-fill-secondary-enabled);
--static-secondary-on-secondary: var( --colors-interactive-fill-secondary-on-secondary );
--static-secondary-hover: var(--colors-interactive-fill-secondary-hover);
--static-secondary-pressed: var( --colors-interactive-fill-secondary-pressed );
--primary: var(--colors-interactive-fill-primary-enabled);
--primary-on-primary: var(--colors-interactive-fill-primary-on-primary);
--primary-hover: var(--colors-interactive-fill-primary-hover);
--primary-pressed: var(--colors-interactive-fill-primary-pressed);
--tw-ring-color: rgba(59,130,246,.5);
--tw-ring-shadow: 0 0 #0000;
--tw-border-spacing-x: 0;
--tw-ring-offset-width: 0px;
--tw-shadow-colored: 0 0 #0000;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-border-spacing-y: 0;
--tw-ring-offset-color: #fff;
```

### Spacing

```css
--space-0: 0px;
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-5: 20px;
--space-6: 24px;
--space-7: 28px;
--space-8: 32px;
--space-9: 36px;
--space-10: 40px;
--space-12: 48px;
--space-14: 56px;
--space-16: 64px;
--space-18: 72px;
--space-20: 80px;
--space-24: 96px;
--space-28: 112px;
--space-32: 128px;
--space-36: 144px;
--space-40: 160px;
--space-48: 192px;
--space-56: 224px;
--space-64: 256px;
--space-72: 288px;
--space-80: 320px;
--sizes-0: 0px;
--sizes-1: 4px;
--sizes-2: 8px;
--sizes-3: 12px;
--sizes-4: 16px;
--sizes-5: 20px;
--sizes-6: 24px;
--sizes-7: 28px;
--sizes-8: 32px;
--sizes-9: 36px;
--sizes-10: 40px;
--sizes-12: 48px;
--sizes-14: 56px;
--sizes-16: 64px;
--sizes-18: 72px;
--sizes-20: 80px;
--sizes-24: 96px;
--sizes-28: 112px;
--sizes-32: 128px;
--sizes-36: 144px;
--sizes-40: 160px;
--sizes-48: 192px;
--sizes-56: 224px;
--sizes-64: 256px;
--sizes-72: 288px;
--sizes-80: 320px;
--tw-numeric-spacing: ;
```

### Typography

```css
--fonts-display: 'Inter Display', system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
--fonts-text: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
--fonts-mono: 'Inter', ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace;
--font-weights-regular: 500;
--font-weights-bold: 500;
--font-sans: '__Inter_f367f3', '__Inter_Fallback_f367f3',
  system-ui,
  -apple-system,
  sans-serif,
  ui-sans-serif,
  Arial,
  BlinkMacSystemFont,
  'Segoe UI',
  Roboto,
  'Helvetica Neue',
  'Noto Sans',
  'Apple Color Emoji',
  'Segoe UI Emoji',
  'Segoe UI Symbol',
  'Noto Color Emoji';
--font-serif: '__p22MackinacPro_6ce25e', '__p22MackinacPro_Fallback_6ce25e',
  '__interDisplay_4fc95a', '__interDisplay_Fallback_4fc95a',
  system-ui,
  -apple-system,
  sans-serif,
  ui-sans-serif,
  Arial,
  BlinkMacSystemFont,
  'Segoe UI',
  Roboto,
  'Helvetica Neue',
  'Noto Sans',
  'Apple Color Emoji',
  'Segoe UI Emoji',
  'Segoe UI Symbol',
  'Noto Color Emoji';
--font-display: '__interDisplay_4fc95a', '__interDisplay_Fallback_4fc95a',
  system-ui,
  -apple-system,
  sans-serif,
  ui-sans-serif,
  Arial,
  BlinkMacSystemFont,
  'Segoe UI',
  Roboto,
  'Helvetica Neue',
  'Noto Sans',
  'Apple Color Emoji',
  'Segoe UI Emoji',
  'Segoe UI Symbol',
  'Noto Color Emoji';
--font-mono: var(--fonts-mono);
```

### Shadows

```css
--shadows-focus-inside: inset 0px 0px 0px 1px rgb(0, 0, 0), inset 0px 0px 0px 2px rgb(255, 255, 255);
--shadows-focus-outside: 0px 0px 0px 2px rgb(255, 255, 255), 0px 0px 0px 4px rgb(0, 0, 0);
--shadows-interactive-elevation-high: 0px 2px 4px 0px rgba(0, 0, 0, 0.05), 0px 3px 5px 0px rgba(0, 0, 0, 0.05), 0px 4px 6px 0px rgba(0, 0, 0, 0.05), 0px 4px 20px 0px rgba(0, 0, 0, 0.05);
--shadows-interactive-elevation-low: 0px 1px 1px 0px rgba(0, 0, 0, 0.1), 0px 1px 2px 0px rgba(0, 0, 0, 0.1), 0px 0px 2px 0px rgba(0, 0, 0, 0.07);
--shadows-interactive-elevation-medium: 0px 1px 1px 0px rgba(0, 0, 0, 0.1), 0px 2px 2px 0px rgba(0, 0, 0, 0.05), 0px 2px 4px 0px rgba(0, 0, 0, 0.07), 0px 1px 4px 0px rgba(0, 0, 0, 0.08);
--shadows-static-elevation-high: 0px 2px 4px 0px rgba(0, 0, 0, 0.03), 0px 6px 6px 0px rgba(0, 0, 0, 0.03), 0px 15px 20px 0px rgba(0, 0, 0, 0.03), 0px 30px 40px 0px rgba(0, 0, 0, 0.03), 0px 40px 70px 0px rgba(0, 0, 0, 0.03), 0px 4px 30px 0px rgba(0, 0, 0, 0.03), 0px 0px 8px 0px rgba(0, 0, 0, 0.03);
--shadows-static-elevation-low: 0px 1px 1px 0px rgba(0, 0, 0, 0.07), 0px 1px 2px 0px rgba(0, 0, 0, 0.08), 0px 2px 2px 0px rgba(0, 0, 0, 0.1), 0px 0px 8px 0px rgba(0, 0, 0, 0.05);
--shadows-static-elevation-medium: 0px 1px 1px 0px rgba(0, 0, 0, 0.05), 0px 2px 2px 0px rgba(0, 0, 0, 0.05), 0px 5px 5px 0px rgba(0, 0, 0, 0.05), 0px 10px 10px 0px rgba(0, 0, 0, 0.05), 0px 0px 8px 0px rgba(0, 0, 0, 0.05);
--tw-drop-shadow: ;
--tw-shadow: 0 0 #0000;
```

### Other

```css
--navHeight: 80px;
--mobileNavHeight: 64px;
--radii-container-large: 20px;
--radii-container-medium: 16px;
--radii-container-none: 0;
--radii-container-small: 12px;
--radii-control-large: 8px;
--radii-control-medium: 6px;
--radii-control-none: 0;
--radii-control-pill: 100vmax;
--radii-control-small: 4px;
--radii-deprecated-full: 9999px;
--radii-deprecated-large: 24px;
--radii-deprecated-medium: 16px;
--radii-deprecated-none: 0;
--radii-deprecated-round: 50%;
--radii-deprecated-small: 8px;
--radii-deprecated-x-small: 4px;
--radii-sheet-large: 28px;
--radii-sheet-medium: 24px;
--radii-sheet-none: 0;
--z-indices-elements-and-components: 1;
--z-indices-element-and-component-drop-downs: 2000;
--z-indices-header-footer: 4000;
--z-indices-full-screen-features: 6000;
--z-indices-special-cases: 7000;
--z-indices-pop-overs: 8000;
--z-indices-modals-dialog-windows: 8000;
--z-indices-notifications: 9000;
--breakpoints-0: 320px;
--breakpoints-1: 480px;
--breakpoints-2: 320px;
--breakpoints-3: 480px;
--breakpoints-4: 640px;
--breakpoints-5: 800px;
--breakpoints-6: 960px;
--breakpoints-7: 1120px;
--breakpoints-8: 1280px;
--breakpoints-9: 1440px;
--breakpoints-10: 1600px;
--breakpoints-11: 1760px;
--breakpoints-12: 1920px;
--responsive-thresholds-desktop: $5;
--static-inverse: var(--colors-interactive-fill-inverse-enabled);
--static-inverse-on-inverse: var( --colors-interactive-fill-inverse-on-inverse );
--static-inverse-hover: var(--colors-interactive-fill-inverse-hover);
--static-inverse-pressed: var(--colors-interactive-fill-inverse-pressed);
--inverse: var(--colors-interactive-fill-inverse-enabled);
--inverse-on-inverse: var(--colors-interactive-fill-inverse-on-inverse);
--inverse-hover: var(--colors-interactive-fill-inverse-hover);
--inverse-pressed: var(--colors-interactive-fill-inverse-pressed);
--tw-saturate: ;
--tw-gradient-to-position: ;
--nav-hide: 0;
--tw-scale-y: 1;
--tw-pan-x: ;
--tw-sepia: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-pan-y: ;
--tw-rotate: 0;
--tw-backdrop-hue-rotate: ;
--tw-skew-y: 0;
--tw-slashed-zero: ;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-brightness: ;
--tw-backdrop-brightness: ;
--tw-skew-x: 0;
--tw-gradient-via-position: ;
--tw-grayscale: ;
--tw-pinch-zoom: ;
--tw-backdrop-contrast: ;
--tw-translate-y: 0;
--tw-translate-x: 0;
--tw-blur: ;
--tw-invert: ;
--tw-backdrop-sepia: ;
--tw-ordinal: ;
--tw-backdrop-invert: ;
--tw-scroll-snap-strictness: proximity;
--tw-numeric-fraction: ;
--tw-backdrop-saturate: ;
--tw-contrast: ;
--tw-backdrop-blur: ;
--tw-scale-x: 1;
--tw-numeric-figure: ;
```

### Dependencies

```css
--static-primary: --colors-interactive-fill-primary-enabled;
--static-primary-hover: --colors-interactive-fill-primary-hover;
--static-primary-pressed: --colors-interactive-fill-primary-pressed;
--secondary: --colors-interactive-fill-secondary-enabled;
--secondary-hover: --colors-interactive-fill-secondary-hover;
--secondary-pressed: --colors-interactive-fill-secondary-pressed;
--static-secondary: --colors-interactive-fill-secondary-enabled;
--static-secondary-hover: --colors-interactive-fill-secondary-hover;
--static-inverse: --colors-interactive-fill-inverse-enabled;
--static-inverse-hover: --colors-interactive-fill-inverse-hover;
--static-inverse-pressed: --colors-interactive-fill-inverse-pressed;
--primary: --colors-interactive-fill-primary-enabled;
--primary-on-primary: --colors-interactive-fill-primary-on-primary;
--primary-hover: --colors-interactive-fill-primary-hover;
--primary-pressed: --colors-interactive-fill-primary-pressed;
--inverse: --colors-interactive-fill-inverse-enabled;
--inverse-on-inverse: --colors-interactive-fill-inverse-on-inverse;
--inverse-hover: --colors-interactive-fill-inverse-hover;
--inverse-pressed: --colors-interactive-fill-inverse-pressed;
--font-mono: --fonts-mono;
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
| sm | 599px | max-width |
| md | 743px | max-width |
| md | 744px | min-width |
| md | 800px | min-width |
| 959px | 959px | max-width |
| lg | 960px | min-width |
| lg | 1023px | max-width |
| lg | 1024px | min-width |
| 1439px | 1439px | max-width |
| 1440px | 1440px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.14s`, `0.5s`, `0.18s`, `0.15s`, `0.3s`, `0.2s`

### Common Transitions

```css
transition: all;
transition: background-color 0.14s ease-out, transform 0.5s;
transition: color 0.14s ease-out;
transition: transform 0.18s ease-out;
transition: background-color 0.14s ease-out, border-color 0.14s ease-out, color 0.14s ease-out, box-shadow 0.14s ease-out;
transition: opacity 0.14s ease-out;
transition: 0.15s linear;
transition: 0.14s ease-out;
transition: 0.5s;
transition: background-color 0.18s ease-out;
```

### Keyframe Animations

**pd-font-pulse-desktop**
```css
@keyframes pd-font-pulse-desktop {
  0%, 100% { font-size: 15px; line-height: 17px; transform: scale(1); }
  50% { font-size: 15px; line-height: 17px; transform: scale(1.133); }
}
```

**pd-font-pulse-mobile**
```css
@keyframes pd-font-pulse-mobile {
  0%, 100% { font-size: 7px; line-height: 9px; transform: scale(1); }
  50% { font-size: 7px; line-height: 9px; transform: scale(1.286); }
}
```

**pulse**
```css
@keyframes pulse {
  50% { opacity: 0.5; }
}
```

**splat-fade-out**
```css
@keyframes splat-fade-out {
  100% { opacity: 0; }
}
```

**nav-modal-enter**
```css
@keyframes nav-modal-enter {
  0% { clip-path: inset(0px 0px 0px 100%); }
  100% { clip-path: inset(0px); }
}
```

**nav-modal-enter**
```css
@keyframes nav-modal-enter {
  0% { clip-path: inset(0px 0px 0px 100%); }
  100% { clip-path: inset(0px); }
}
```

**nav-modal-exit**
```css
@keyframes nav-modal-exit {
  0% { clip-path: inset(0px); }
  100% { clip-path: inset(0px 0px 100%); }
}
```

**nav-modal-exit**
```css
@keyframes nav-modal-exit {
  0% { clip-path: inset(0px); }
  100% { clip-path: inset(0px 0px 100%); }
}
```

**nav-modal-enter**
```css
@keyframes nav-modal-enter {
  0% { clip-path: inset(0px 0px 100%); }
  100% { clip-path: inset(0px); }
}
```

**nav-modal-enter**
```css
@keyframes nav-modal-enter {
  0% { clip-path: inset(0px 0px 100%); }
  100% { clip-path: inset(0px); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (27 instances)

```css
.button {
  background-color: rgb(247, 246, 242);
  color: rgb(247, 246, 242);
  font-size: 16px;
  font-weight: 400;
  padding-top: 0px;
  padding-right: 0px;
  border-radius: 8px;
}
```

### Cards (4 instances)

```css
.card {
  background-color: rgb(247, 246, 242);
  border-radius: 9999px;
  padding-top: 60px;
  padding-right: 0px;
}
```

### Inputs (2 instances)

```css
.input {
  background-color: rgb(247, 246, 242);
  color: rgb(82, 82, 82);
  border-color: rgb(82, 82, 82);
  border-radius: 8px;
  font-size: 14px;
  padding-top: 11px;
  padding-right: 8px;
}
```

### Links (61 instances)

```css
.link {
  color: rgb(247, 246, 242);
  font-size: 16px;
  font-weight: 500;
}
```

### Navigation (10 instances)

```css
.navigatio {
  color: rgb(247, 246, 242);
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
  background-color: rgb(247, 76, 37);
  color: rgb(247, 246, 242);
  padding-top: 120px;
  padding-bottom: 20px;
  font-size: 16px;
}
```

### Modals (5 instances)

```css
.modal {
  background-color: rgb(255, 255, 255);
  border-radius: 0px;
  padding-top: 0px;
  padding-right: 0px;
  max-width: 100%;
}
```

### Dropdowns (2 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(229, 231, 235);
  padding-top: 0px;
}
```

### Avatars (112 instances)

```css
.avatar {
  border-radius: 9999px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 246, 242);
  padding: 1px 6px 1px 6px;
  border-radius: 0px;
  border: 0px none rgb(247, 246, 242);
  font-size: 16px;
  font-weight: 400;
```

### Button — 7 instances, 3 variants

**Variant 1** (3 instances)

```css
  background: rgb(247, 76, 37);
  color: rgb(247, 246, 242);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 16px;
  font-weight: 500;
```

**Variant 2** (2 instances)

```css
  background: rgb(247, 246, 242);
  color: rgb(247, 76, 37);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 16px;
  font-weight: 500;
```

**Variant 3** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 76, 37);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 1px solid rgb(247, 76, 37);
  font-size: 18px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(247, 246, 242);
  color: rgb(82, 82, 82);
  padding: 8px 8px 8px 8px;
  border-radius: 9999px;
  border: 0px none rgb(82, 82, 82);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(247, 246, 242);
  padding: 0px 0px 0px 0px;
  border-radius: 0px;
  border: 0px none rgb(247, 246, 242);
  font-size: 16px;
  font-weight: 400;
```

### Card — 4 instances, 1 variant

**Variant 1** (4 instances)

```css
  background: rgb(247, 246, 242);
  color: rgb(247, 76, 37);
  padding: 60px 0px 60px 0px;
  border-radius: 9999px;
  border: 1px solid rgb(247, 76, 37);
  font-size: 16px;
  font-weight: 400;
```

### Button — 3 instances, 2 variants

**Variant 1** (2 instances)

```css
  background: rgb(247, 246, 242);
  color: rgb(247, 76, 37);
  padding: 6px 16px 6px 16px;
  border-radius: 9999px;
  border: 1px solid rgb(247, 76, 37);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(0, 0, 0);
  padding: 1px 6px 1px 6px;
  border-radius: 0px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 16px;
  font-weight: 400;
```

### Input — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(247, 246, 242);
  color: rgb(82, 82, 82);
  padding: 11px 8px 11px 12px;
  border-radius: 8px;
  border: 0px none rgb(82, 82, 82);
  font-size: 14px;
  font-weight: 530;
```

## Layout System

**38 grid containers** and **236 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1960px | 0px |
| 100% | 0px |
| 600px | 0px |
| 1920px | 0px |
| min(100%, 600px) | 0px |
| 468px | 0px |
| 2048px | 0px |
| 460px | 0px |
| 392px | 20px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 1-column | 11x |
| 7-column | 10x |
| 6-column | 4x |
| 8-column | 2x |
| 9-column | 2x |
| 2-column | 2x |
| 3-column | 1x |

### Grid Templates

```css
grid-template-columns: [full-start] 20px [content-start] 1240px [content-end] 20px [full-end];
grid-template-columns: [text-start] 545px [text-end image-start] 545px [image-end];
gap: normal 150px;
grid-template-columns: [full-start] 20px [content-start] 1240px [content-end] 20px [full-end];
grid-template-columns: [full-start] 20px [content-start] 1240px [content-end] 20px [full-end];
grid-template-columns: 620px 620px;
gap: 64px normal;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 11x |
| row/nowrap | 220x |
| row/wrap | 5x |

**Gap values:** `12px`, `16px`, `20px`, `20px normal`, `24px`, `24px 150px`, `32px 20px`, `40px`, `64px`, `64px normal`, `8px`, `normal 10px`, `normal 150px`, `normal 16px`, `normal 20px`, `normal 8px`

## Accessibility (WCAG 2.1)

**Overall Score: 100%** — 0 passing, 0 failing color pairs

## Design System Score

**Overall: 86/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 100/100 |
| Typography Consistency | 50/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 100/100 |
| Border Radius Consistency | 100/100 |
| Accessibility | 100/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Clean elevation system, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 5 font families — consider limiting to 2 (heading + body)
- 23 !important rules — prefer specificity over overrides
- 72% of CSS is unused — consider purging
- 403 duplicate CSS declarations

## Z-Index Map

**6 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 50,50 | nav.s.c.-.c.d.d.f.0.d.8.2.-.1. .k.s.j.j.S.r |
| base | -1,5 | img.b.a.c.k.g.r.o.u.n.d.-.i.m.a.g.e, main.s.c.-.e.d.b.b.9.a.0.3.-.1. .f.T.R.g.c.B, div.s.c.-.7.2.4.0.0.a.1.-.9. .g.W.k.V.P.U |

## SVG Icons

**11 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| md | 4 |
| lg | 5 |
| xl | 1 |

**Icon colors:** `currentColor`, `var(--static-inverse)`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Material Symbols Rounded | self-hosted | 400, normal | normal |
| __Inter_f367f3 | self-hosted | 100 900 | normal |
| __p22MackinacPro_6ce25e | self-hosted | 500 | normal, italic |
| __interDisplay_4fc95a | self-hosted | 400, normal | normal |

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| avatar | 112 | objectFit: cover, borderRadius: 9999px, shape: circular |
| thumbnail | 49 | objectFit: fill, borderRadius: 0px, shape: square |
| general | 8 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 4 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (124x), 3:4 (7x), 3:2 (5x), 16:9 (4x), 1.97:1 (4x), 6.33:1 (4x), 2.17:1 (4x), 2.03:1 (4x)

## Motion Language

**Feel:** smooth · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `xs` | `140ms` | 140 |
| `sm` | `180ms` | 180 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |

### Easing Families

- **ease-in-out** (91 uses) — `ease`
- **linear** (27 uses) — `linear`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `enter` | fade | opacity | 4 |
| `enter` | fade | opacity | 4 |
| `enter` | fade | opacity | 4 |
| `enter` | fade | opacity | 4 |
| `enter` | fade | opacity | 4 |
| `enter` | fade | opacity | 4 |
| `scroll` | slide-x | transform | 8 |
| `scroll` | slide-x | transform | 8 |
| `scroll` | slide-x | transform | 8 |
| `scroll` | slide-x | transform | 8 |
| `scroll` | slide-x | transform | 8 |
| `scroll` | slide-x | transform | 8 |
| `scroll` | slide-x | transform | 8 |
| `scroll` | slide-x | transform | 8 |

## Component Anatomy

### button — 15 instances

**Slots:** label, icon

### card — 4 instances

**Slots:** media

## Brand Voice

**Tone:** friendly · **Pronoun:** we→you · **Headings:** Sentence case (tight)

### Top CTA Verbs

- **order** (3)
- **request** (3)
- **see** (2)
- **for** (1)
- **resources** (1)
- **already** (1)
- **sign** (1)

### Button Copy Patterns

- "request picnic" (3×)
- "see how it works" (2×)
- "order now" (2×)
- "for offices" (1×)
- "resources" (1×)
- "order" (1×)
- "already on picnic? order here" (1×)
- "sign up" (1×)

### Sample Headings

> 50+ restaurants delivered to your office
> Locations
> Our solutions
> Office meals
> Team orders
> 50+ restaurants delivered to your office
> Locations
> Locations
> Our solutions
> Office meals

## Page Intent

**Type:** `landing` (confidence 0.29)
**Description:** Discover zero fees zero tips office lunch delivery service, catering for large events, group ordering, and subsidized lunch programs with Trypicnic.com. Elevate your company's food experience with tai

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): nav → steps → content → nav → content → content → steps → testimonial → hero → content → hero → hero → hero → content → footer → nav

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.9 |
| 1 | steps | 50+ restaurants delivered to your office | 0.75 |
| 2 | content | 50+ restaurants delivered to your office | 0.3 |
| 3 | nav | Locations | 0.4 |
| 4 | content | — | 0.3 |
| 5 | content | — | 0.3 |
| 6 | steps | Our solutions | 0.75 |
| 7 | testimonial | Why Picnic? | 0.8 |
| 8 | hero | One delivery for many orders | 0.4 |
| 9 | content | — | 0.3 |
| 10 | hero | See how we changed office lunch delivery for MBK real estate | 0.4 |
| 11 | hero | All the options without the fees | 0.4 |
| 12 | hero | Trusted
by many | 0.4 |
| 13 | content | Follow us on Instagram @picnicatwork | 0.3 |
| 14 | footer | Get started | 0.95 |
| 15 | nav | Get started | 0.9 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.158 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 0 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.071)
**Counts:** total 174, svg 136, icon 9, screenshot-like 0, photo-like 3
**Dominant aspect:** square-ish
**Radius profile on images:** rounded

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `__Inter_f367f3` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
