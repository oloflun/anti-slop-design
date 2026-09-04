---
title: "Limón"
url: https://www.limon.no/
source_url: https://www.limon.no/
captured: 2026-09-04
origin: refero
extract: ok
category: hospitality
category2: consumer-brand
family: candlelit-signage-poke
dna: "Neon-signage tracking on an olive-black canvas x edge-to-edge editorial food photography"
register: warm photographic
grammar: chaptered editorial
lane: "A dark olive canvas floats a wide-tracked wordmark and a filled lemon CTA over a cream-and-olive rhythm of unframed, edge-to-edge food photography, with the display wordmark overlaid directly onto the dish itself"
mode: persuade
traits: ["wide positive tracking scaling with size", "one lemon accent, dark-canvas only", "near-zero 1px radius everywhere but the FAB", "unframed edge-to-edge food photography", "dark hero into cream content sections", "flat, zero-shadow surfaces"]
palette: ["#1d0b0d", "#103b15", "#f7ea48", "#fcf9f0", "#dbe2dc"]
type: ["VenusCom"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Limon.md
---

## Why it works

Palette and type are read from Refero's extracted tokens. The captured fold shows
a lighter, food-forward moment (a sage-green tabletop of poke and ceviche bowls
under a cream nav bar) rather than the deep olive-black hero the tokens describe as
dominant — evidence that the page alternates a dark, signage-lit hero with brighter
photographic sections rather than staying dark throughout. Either way, Lemon Zest
`#f7ea48` is treated as a rule, not a decoration: it is reserved for filled CTAs and
display text on dark surfaces only, and the source is explicit that placing it on
the cream background destroys its contrast — so the accent's placement is
load-bearing, not optional.

Typography carries an unusually wide, positive letter-spacing that scales with
size (0.06em at 75px display down to 0.02–0.04em at body), which the source
describes as "almost hand-stenciled" — wide-set enough that display lines read as
pressed onto glass or neon rather than typeset normally. Because tracking loosens
rather than tightens at scale (the opposite of the convention several sibling
entries in this set use), the brand voice reads as illuminated signage specifically,
not merely "bold."

Geometry stays almost entirely unsoftened: buttons, cards, inputs and badges sit
at 1px radius, and the sole exception — a 40px fully-round back-to-top control — is
reserved for exactly one utility element. Food photography runs edge-to-edge with
no frame, border or shadow, so the "cards" in any grid are effectively bare
photographs; the confident, near-square geometry keeps the system from reading as
either app-soft or brutalist-hard.

## What to borrow (principle)

- **Fence a bright accent to one surface only.** Lemon Zest working exclusively
  on the dark canvas — and explicitly failing on the light one — is a rule that's
  easy to state and easy to violate by accident; stating it prevents the mistake.
- **Open tracking with size instead of closing it.** Positive, size-scaling
  letter-spacing is a legible way to make display type feel like lit signage
  rather than merely large.
- **Reserve the one soft radius for one utility control.** A near-zero-radius
  system with a single fully-round exception (here, back-to-top) makes that one
  element instantly recognisable as "different," i.e. floating and persistent.
- **Let photography be the card.** Food or product tiles with zero chrome — no
  border, no shadow, no frame — read as more appetizing than the same image
  boxed in a container.
- **Pair a filled accent CTA with a same-colour ghost link nearby.** A filled
  lemon button next to a ghost "ORDER NOW" link in forest ink establishes
  hierarchy through fill-vs-outline rather than through a second colour.

## What to leave

- A near-zero (1px) radius system paired with a single 40px circular exception is
  a narrow rule set — any additional rounded element (a badge, a modal) would
  need to justify itself against that one exception or the system reads as
  inconsistent.
- Wide positive tracking at display size depends on a typeface with enough
  internal counter space to survive being spaced out; a tightly-fit or condensed
  substitute will look broken rather than "neon."
- Lemon-on-dark-only is a real constraint for a brand extending into print or a
  light-mode context — the system as documented offers no accent treatment for a
  cream-canvas CTA.

## Signature move

The overlaid display wordmark: the brand name and short phrases (LIMÓN, FRESH
CATCH) set at up to 75px in Lemon Zest, laid directly onto the food photograph
itself rather than on a plain background plate — the dish and the type share one
surface.

## Motion

(from designlang extract) Feel reads as smooth, and the page is scroll-linked.
Two durations are in use — a quick 250ms on a plain `ease` curve (7 uses) for
short state changes, and a slower 1s step for larger transitions. No keyframe
animations are confirmed firing. The 1s duration is consistent with a hero
crossfade: long enough to be a deliberate dissolve between dish photographs
rather than a UI micro-interaction. (observed in capture) the wordmark set
directly onto shifting food photography suggests the hero may cycle between
multiple dish photographs (a slideshow or crossfade) rather than holding a
single static image, and the ghost "ORDER NOW" links likely reveal an underline
only on hover, per the source's stated hover convention.

| Token | Value | Easing |
|---|---|---|
| sm | 250ms | `ease` |
| xl (crossfade) | 1s | `ease` |

## Brief

Build a fast-casual restaurant landing page. Alternate a Black Olive `#1d0b0d`
hero/dark section with Warm Cream `#fcf9f0` content sections — never a shade
between. Set the wordmark and display lines in a single grotesque at up to 75px,
line-height ~1.0, with letter-spacing that opens from 0.02em at body to 0.06em at
display. Overlay display text directly onto full-bleed food photography rather
than a plain background. Reserve Lemon Zest `#f7ea48` for filled CTA buttons and
display text on the dark canvas only — never on cream, never as a text colour on
its own fill. Use Forest Ink `#103b15` for headings, links and dividers on the
light sections. Cap every button, card, input and badge at 1px radius; the one
exception is a 40px fully-round back-to-top control, fixed bottom-right. Lay food
photography edge-to-edge with zero frame, border or shadow — the grid's "cards"
are simply the photographs, captioned below with a heading, body copy, and a
ghost "ORDER NOW →" link. Keep section gaps around 60px.

## Image recipe

Editorial food photograph of [SUBJECT] — a plated dish shot overhead or at a
three-quarter angle, tight crop, warm-toned surface (terracotta, peach, mauve)
beneath it, natural directional light with rich saturation, no props beyond the
food itself, no people, no styled table setting — the dish fills the frame
edge-to-edge.

## Photo search

Unsplash first, Pexels second.
- "poke bowl overhead food photography colourful"
- "ceviche plated dish overhead warm tone"
- "burrito wrap food photography close up"
- "tortilla chips guacamole overhead bright"

## Reference lock

Primary reference/direction: Limón — olive-black signage hero alternating with
cream editorial food sections, one lemon accent reserved for dark surfaces.
Preserve (3-5 traits): Black Olive `#1d0b0d` dark sections and Warm Cream
`#fcf9f0` light sections with no intermediate tone; Lemon Zest `#f7ea48` used only
as a filled CTA or display text on dark, never on cream; positive letter-spacing
that opens with size (0.02em body to 0.06em display); near-zero 1px radius
everywhere except a single 40px circular back-to-top control; food photography
always edge-to-edge, zero frame or shadow.
Borrow only (1-2): the display wordmark overlaid directly onto food photography;
the ghost "ORDER NOW →" inline link pattern beneath each dish caption.
Role rules: Lemon Zest never appears on the cream canvas; Forest Ink never
becomes a button background; display headlines never drop below 46px or use
negative tracking.
Media strategy: photo:unsplash — tightly cropped, edge-to-edge editorial food
photography, warm-toned surfaces, no people, no lifestyle staging.
Reject: rounding cards or buttons above 1px (outside the one FAB exception);
lemon accent on a light background; drop shadows or gradients; framed/bordered
food photography; a second chromatic accent beyond lemon and forest green.
Token commitments: dark `#1d0b0d`, green `#103b15`, accent `#f7ea48`, cream
`#fcf9f0`, hairline `#dbe2dc`; display up to 75px/leading 1.0/0.06em tracking;
body 19-20px/leading 1.25-1.3/0.4-0.57px tracking; radius 1px default, 40px
circular FAB only; page max-width 1200px, section gap 60px.
