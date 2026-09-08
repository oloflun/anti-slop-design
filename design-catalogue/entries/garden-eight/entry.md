---
title: "Garden Eight"
url: https://garden-eight.com/
source_url: https://garden-eight.com/
captured: 2026-09-04
origin: refero
extract: ok
category: portfolio
category2: editorial
family: monumental-parchment-gallery
dna: "Museum wall-text typography x floating biomorphic cream sculpture"
register: editorial print
grammar: typographic poster
lane: "A warm parchment canvas at near-museum gutter width holds a single 215px headline against floating cream-toned 3D sculptural forms, with nothing else above the fold — one typographic moment, one sculptural moment, separated by silence"
mode: persuade
traits: ["215px display at 0.77-1.30 leading", "binary two-tone palette, no accent", "1440px pill or 30px card, nothing between", "180px gallery-scale gutters", "biomorphic cream 3D forms as sole imagery", "zero UI shadow, only the sculpture casts one"]
palette: ["#dbd6d0", "#1e1f1f", "#000000"]
type: ["Lausanne", "Gunsan"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Garden Eight.md
---

## Why it works

Palette and type are read from Refero's extracted tokens. The system commits to a
genuinely binary palette — parchment `#dbd6d0` and carbon ink `#1e1f1f`, nothing
else, ever — and re-routes every signal a typical interface would encode in colour
(hover, active, emphasis) into weight, scale, or a border instead. That single
constraint is what keeps a studio homepage reading like a gallery wall rather than
a product.

Two display voices share the same monumental 215px size but oppose each other in
weight and leading: Gunsan at 600 with an extremely tight 0.77 line-height reads as
a magazine cover, while Lausanne at 200 with 1.30 leading reads as whisper-weight
exhibition text. Because both live at the identical size, the choice between them
is purely a register decision, not a scale decision — the page either shouts or
murmurs, never something in between, and there is no intermediate heading tier at
all (the type scale jumps straight from 12-15px reading size to 215px monument
size).

Radius carries the same binary discipline as colour and type: every bordered
interactive element is a 1440px true pill, and 30px is the only other permitted
radius, reserved for cards and image containers. The one place the system allows
itself a shadow is the floating biomorphic 3D sculptural forms — soft, cream-toned,
organic shapes that are the sole imagery mode and the only thing in the system with
literal depth, deliberately set apart from the flat, shadowless UI around them.

## What to borrow (principle)

- **Enforce a genuinely binary palette.** Two tones only, with every UI state
  re-encoded in weight/scale/border, produces a calmer, more confident register
  than even a "restrained" three- or four-colour system.
- **Give one size two opposing voices.** Running the identical display size at a
  heavy tight weight and a whisper light weight turns a single scale value into
  two distinct instruments.
- **Skip the intermediate heading tier entirely.** Jumping straight from reading
  size to monument size (no 24/32/48px steps) is what makes the "poster, not
  page" reading hold.
- **Reserve radius for exactly two jobs.** Pill for every interactive/bordered
  element, one mid-radius for cards/images, nothing between — an easy rule to
  audit visually.
- **Let only the "real" 3D object cast a shadow.** Confining elevation to a single
  imagery type keeps the rest of the UI legibly flat by contrast.

## What to leave

- A 215px minimum display size with "if it doesn't fit, the layout is wrong" is
  an extremely high floor — it demands short, poster-length headline copy and
  will not accommodate a typical multi-line marketing sentence.
- 180px horizontal gutters are a genuinely spacious, low-density choice that
  only reads as "gallery" rather than "empty" at large viewport widths; it will
  collapse awkwardly without a deliberate mobile rethink.
- Zero functional colour (no error red, no success green) is a real gap for
  anything beyond a static portfolio — a studio adding a contact form or booking
  flow will need to invent a convention this system doesn't provide.

## Signature move

The two-display-voice system at identical size: the same 215px scale rendered
either in Gunsan 600 at 0.77 leading (a magazine-cover shout) or Lausanne 200 at
1.30 leading (gallery wall-text whisper) — the choice between the two is the
page's entire register vocabulary.

## Motion

(from designlang extract) Feel reads as responsive, and the page is scroll-linked
— there is in fact a well-developed motion system, contrary to the earlier "no
tokens" read. A single ease-out curve, `cubic-bezier(0.32, 0.94, 0.6, 1)`, is
used with unusual consistency (37 uses) across six duration tiers spanning
instant (50ms) micro-feedback up through a 1.4s long-form reveal — that wide
range, on one disciplined curve, corroborates the "GARDEN ZERO" loading sequence
the live capture caught mid-animation: a system built for both snappy UI
feedback and a slow, deliberate entrance sequence. (observed in capture) given
the "binary palette, no shadow except on sculpture" rule, hover states most
likely invert border/fill (as described for the pill button) rather than adding
movement, and the floating 3D forms plausibly drift or rotate slowly on the same
long-duration tier.

| Token | Value | Easing |
|---|---|---|
| instant | 50ms | `cubic-bezier(0.32, 0.94, 0.6, 1)` |
| xs | 100ms | `cubic-bezier(0.32, 0.94, 0.6, 1)` |
| sm | 200ms | `cubic-bezier(0.32, 0.94, 0.6, 1)` |
| md | 300ms | `cubic-bezier(0.32, 0.94, 0.6, 1)` |
| lg | 600ms | `cubic-bezier(0.32, 0.94, 0.6, 1)` |
| xxl (entrance) | 1.4s | `cubic-bezier(0.32, 0.94, 0.6, 1)` |

## Brief

Build a design-studio homepage with museum-scale restraint. Canvas is parchment
`#dbd6d0` everywhere, text is carbon ink `#1e1f1f` — no third colour, ever. Use
180px horizontal gutters and no max-width container. Open on a single 215px
display headline (Gunsan 600 at 0.77 leading for a bold cover voice, or Lausanne
200 at 1.30 leading for a whisper voice) with no supporting copy above the fold,
composed against floating cream-toned biomorphic 3D sculptural forms that bleed to
the edges. A minimal transparent top bar carries the wordmark left and nav items
right, all at 12px Lausanne 400 with wide tracking — no background, no sticky
elevation. Every bordered interactive element (buttons, tags) is a 1440px pill
with a 1px border and no default fill; every card or image container uses a 30px
radius and a 1px border, never a background fill or shadow. Keep body/caption text
locked to 12-15px — there is no intermediate heading size. Let one editorial
spread occupy each screen, separated by 60px+ of silence rather than alternating
colour bands.

## Image recipe

Abstract biomorphic 3D render of [SUBJECT] — soft, organic, matte-cream sculptural
form (twisted ribbon, soft pod, melted geometry) in the same warm hue family as
the parchment canvas, subsurface-scattered lighting, no hard edges or mechanical
geometry, floating with a soft cast shadow, no environment or ground plane visible.

## Photo search

Unsplash first, Pexels second.
- "abstract sculptural form cream studio render"
- "organic 3D shape soft lighting minimal"
- "biomorphic sculpture neutral background"
- "matte clay abstract form studio photography"

## Reference lock

Primary reference/direction: Garden Eight — binary-palette museum-scale
typographic poster homepage, floating biomorphic cream sculpture.
Preserve (3-5 traits): strictly binary palette (parchment `#dbd6d0` / carbon ink
`#1e1f1f`), no third colour anywhere; 215px display type as the only heading size
above 15px, run either at Gunsan 600/0.77 leading or Lausanne 200/1.30 leading;
radius limited to 1440px (interactive) or 30px (cards/images), nothing between;
zero UI shadow — only the 3D sculptural forms carry elevation; 180px gutters with
no max-width container.
Borrow only (1-2): the AI/JA-style language toggle marked by underline only; the
floating circular scroll-indicator button.
Role rules: no chromatic accent is ever introduced; body/caption text never
exceeds 15px or drops below 12px; display headlines never scale down to fit —
the layout adjusts instead.
Media strategy: 3D render — abstract, cream-toned biomorphic sculptural forms
only; no photography, no human imagery, no lifestyle context, no flat illustration.
Reject: any third colour; box-shadow on UI components; corner radius outside
{0, 30px, 1440px}; an intermediate heading size between 15px and 215px; a filled
default state on bordered buttons.
Token commitments: bg `#dbd6d0`, ink `#1e1f1f`, ink-hard `#000000`; display 215px
at leading 0.77 (Gunsan 600) or 1.30 (Lausanne 200); body/caption 12-15px/leading
1.5; radius 30px cards, 1440px pills; horizontal gutter 180px, section gap 60px.
