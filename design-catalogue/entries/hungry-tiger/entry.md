---
title: "Hungry Tiger"
url: https://www.eathungrytiger.com/
source_url: https://www.eathungrytiger.com/
captured: 2026-09-04
origin: refero
extract: ok
category: consumer-brand
category2: playful
family: tandoor-wall-poster
dna: "Spice-market signage type x raw unframed jar on a monochrome-warm canvas"
register: illustrated dark
grammar: typographic poster
lane: "A dark rust canvas carries dotted-gold section rules and display type up to 213px in a single wide-tracked face, with a raw product jar sitting straight on the canvas as the only image content on an otherwise 90%-type page"
mode: persuade
traits: ["up to 213px display, single typeface everywhere", "gold-on-rust, one heat-red badge exception", "pill radius on every control, 6px only on cards", "dotted gold rule as section divider", "raw unframed product, no card", "low-opacity botanical watermark texture"]
palette: ["#faae33", "#823513", "#9f531b", "#402011", "#281006", "#d1255c"]
type: ["Salmond", "Graphikx"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Hungry Tiger.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Every surface in the system stays inside one warm-brown family — page
canvas, card, and deepest recess step from `#823513` to `#402011` to `#281006` with
no box-shadow anywhere — so the single chromatic accent, Tiger Gold `#faae33`, is
the only thing capable of reading as "lit." A second saturated colour, chili red
`#d1255c`, exists but is fenced off entirely to heat-level badges, which keeps the
gold-on-rust relationship from ever being diluted.

A single typeface, Salmond, runs the entire page from an 11px caption to a 213px
display headline, with letter-spacing that scales inversely to size — tight
(-0.02em) at monument scale, open (0.02em) at the smallest UI text. That inverse
relationship is what keeps a headline this large from reading as merely stretched:
the tightening at scale makes the huge type feel pressed together rather than
blown up.

Imagery discipline mirrors the type discipline: the page is stated to run "90%
type, 10% product," and the product itself is never framed — no card, no
background plate — it simply sits raw on the Ember Rust canvas with a warm
backlight rim. Low-opacity botanical watermarks provide all the atmospheric
texture the page needs without ever competing with the display type sitting on
top of them.

## What to borrow (principle)

- **Fence a second saturated colour to one narrow use.** Reserving chili red
  strictly for heat-badges keeps the primary gold-on-brown relationship from ever
  being diluted by a second "loud" hue.
- **Scale letter-spacing inversely to size.** Tightening tracking as type grows
  (and opening it as type shrinks) is what makes both extremes of a huge type
  range feel intentional rather than merely resized.
- **State an explicit image-to-type ratio.** Declaring the page "90% type, 10%
  product" is a concrete brief that keeps photography from creeping into a
  typography-led system.
- **Let the product sit raw, with no card.** Skipping the frame/background-plate
  convention makes the object read as physically present on the canvas rather
  than as a photographed asset.
- **Replace whitespace dividers with a printed rule.** A dotted line in the
  accent colour gives "label-printed" section rhythm that plain whitespace
  wouldn't provide on a single-colour dark canvas.

## What to leave

- Display type up to 213px with a single-typeface-only rule leaves no room for a
  secondary display face if a future sub-brand or campaign needs a different
  voice — everything must be Salmond, at every scale.
- The all-brown, no-cool-neutral constraint ("do not dilute the gold-on-brown
  palette with white, blue, green, or cool neutrals") makes accessibility
  contrast checking harder than a system with a neutral-white fallback surface.
- Raw, unframed product photography with a backlight rim depends on genuinely
  excellent studio lighting on every shot; a flat or poorly lit product photo
  would read as a mistake rather than a deliberate "no frame" choice.

## Signature move

The raw product showcase: the jar sits directly on the Ember Rust canvas with no
card, no background plate, and a subtle warm backlight rim — positioned as a
small, precise anchor beneath 200px+ of display type, rather than as a
conventional hero product shot.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked.
Durations run 400ms, 450ms and a long 1.5s tier, with no named easing family
confidently parsed (interactions likely use inline, per-element bezier values
rather than a shared token). The one keyframe the extract confirms firing is
`spin` (a rotate transform) — direct confirmation of the live capture's read: the
product jar animates in with a genuine rotation, not just a fall or fade.
(observed in capture) the product jar sits mid-tumble/rotation over the "TIKKA
MASALA" headline on load, so the spin most plausibly plays on entrance before the
jar settles into its resting position beneath the display type — consistent with
the poster-first, type-crowns-everything layout the source describes.

| Token | Value | Easing |
|---|---|---|
| md | 400ms | — |
| lg | 450ms | — |
| xxl (entrance) | 1.5s | — |
| spin keyframe | rotate transform | 1 use, drives product-jar entrance |

## Brief

Build a maximalist condiment-brand landing page. Canvas is Ember Rust `#823513`
everywhere, no max-width container; card surfaces step to Dark Spice `#402011`
and the deepest recess to Charred Clove `#281006` — never a box-shadow. Tiger Gold
`#faae33` is the only chromatic accent permitted to interrupt the brown family;
reserve chili red `#d1255c` strictly for heat-level badges. Set a single typeface
everywhere: 130-213px weight 700 at 0.80-0.90 line-height for hero/section
display, dropping to 11-18px for nav, badges and body, with letter-spacing that
tightens at display size and opens at small sizes. Every button, badge, input and
icon container is a full pill (9999px radius); reserve 6px radius for cards only.
Crown each viewport with massive type first, then anchor a small raw product jar
below with no frame or card. Use a 1px dotted gold rule as the divider between
major sections, and a faint low-opacity botanical watermark layer behind content
for texture. Keep the page roughly 90% type, 10% product imagery.

## Image recipe

Studio product photograph of [SUBJECT] — a single jar or bottle centred on a flat
warm-rust background, tight crop, subtle warm backlight rim suggesting practical
light rather than a studio softbox, sharp focus, no props, no surface reflection,
no card or background plate — the object floats directly on the canvas colour.

## Photo search

Unsplash first, Pexels second.
- "sauce jar product shot dark background rim light"
- "spice jar warm background studio"
- "condiment bottle product photography dark"
- "botanical fern leaf illustration texture dark"

## Reference lock

Primary reference/direction: Hungry Tiger — tandoor-wall poster condiment page,
single typeface at 213px, raw unframed product on warm-brown monochrome.
Preserve (3-5 traits): warm-brown monochrome stepping `#823513` → `#402011` →
`#281006`, zero box-shadow; Tiger Gold `#faae33` as the sole chromatic accent,
chili red `#d1255c` fenced to heat badges only; single typeface (Salmond) at every
size, letter-spacing tightening at display scale and opening at UI scale; every
bordered/filled control a full pill, 6px radius reserved for cards only; product
photography raw and unframed, page kept roughly 90% type / 10% image.
Borrow only (1-2): the 1px dotted gold rule as section divider; the low-opacity
botanical watermark texture layer.
Role rules: chili red never leaves badge context; no cool or white neutrals enter
the palette; display type never drops below 130px or exceeds 0.90 leading; a
secondary display typeface is never introduced.
Media strategy: photo:unsplash — tightly cropped, warm-backlit single-object
product photography only; no lifestyle context, no hands, no kitchen setting.
Reject: box-shadow or glow on any component; a second bright accent outside heat
badges; framed/carded product imagery; solid alternating section-colour bands
(every section stays Ember Rust); a secondary display face.
Token commitments: bg `#823513`, card `#402011`, deepest `#281006`, accent
`#faae33`, accent-2 `#9f531b`, heat `#d1255c`; display 130-213px weight 700/leading
0.80-0.90/-0.02em to -0.005em tracking; body 11-18px/leading 1.2-1.43; radius 6px
cards, 9999px everything interactive; page max-width 1440px, section gap 80-120px.
