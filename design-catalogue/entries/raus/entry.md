---
title: "Raus"
url: https://www.raus.life/
source_url: https://www.raus.life/
captured: 2026-09-04
origin: refero
extract: ok
category: hospitality
category2: editorial
family: whispered-cabin-journal
dna: "Weight-300 whisper-tight sans headlines x a single marigold booking bar"
register: warm photographic
grammar: chaptered editorial
lane: "A cream-paper canvas holds asymmetric photo pairs and weight-300 headlines with almost no visible chrome, punctuated once by a marigold search bar floating across the hero's bottom edge as the page's only loud gesture"
mode: persuade
traits: ["weight 300 everywhere, negative tracking at scale", "cream canvas, zero shadow", "one marigold accent, one use per screen", "20-40px radius, no sharp corners", "asymmetric 2-column photo pairs", "pine green reserved for wordmark and links only"]
palette: ["#f7f0e1", "#23212c", "#006434", "#fcbd1c", "#a6dfff", "#dd5000"]
type: ["neue-haas-unica"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Raus.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. A single typeface carries the entire page at weight 300 for nearly
everything, with weight 400 reserved only for meta labels and body copy where
300 "would feel too fragile" — the source's own language for why the whisper
weight needs an escape hatch at small, information-dense sizes. Negative
tracking tightens consistently from -0.02em at display down to -0.005em at
caption, which is what keeps the airy weight from reading as merely thin.

Colour discipline is exact: Pine green `#006434` is confined to the wordmark,
hero headings and inline links — never a button fill, badge or decorative
shape — while marigold `#fcbd1c` is confined to the search bar, accent blocks
and tag fills, never text. Those two rules, stated as absolutes in the source,
are what let a single bright marigold search bar function as the entire page's
loud moment: everything else, including the CTA button, stays charcoal-on-
cream.

Geometry reinforces the same restraint through generosity rather than
sharpness: every radius is generous (20px default, 40px for hero cards, 99px
for pills) and shadows are banned outright — depth comes only from layering
cream tones and radius, never elevation. Combined with an asymmetric,
never-centred hero image pair (one image roughly 60% width, one 40%), the page
reads as a hand-printed travel journal that happens to have a booking widget
rather than a travel-tech product.

## What to borrow (principle)

- **Give a whisper-weight system an escape hatch at small sizes.** Reserving a
  slightly heavier weight for meta labels and dense body text keeps 300-weight
  from becoming illegible where it matters most.
- **Split brand colour into "identity" and "action" roles that never overlap.**
  One colour for wordmark/links, a completely different one for the single
  interactive surface — never mixed — makes each colour instantly legible for
  its job.
- **Ban sharp corners entirely, not just on buttons.** A minimum-20px radius
  policy across cards, buttons and pills creates a uniform softness that a
  mixed radius scale can't achieve.
- **Let one saturated surface carry the entire page's energy.** A single
  marigold search bar against an otherwise charcoal-on-cream page does more
  visual work than a full accent palette would.
- **Compose the hero as an uneven photo pair, never a symmetric split.** A
  60/40 image ratio reads as considered editorial composition rather than a
  generic two-up template.

## What to leave

- Zero shadow anywhere means every card boundary depends entirely on subtle
  cream-tone layering; on a low-contrast display this system risks reading as
  flat and undifferentiated.
- Weight 300 as the default text weight across headlines through captions is a
  narrow font requirement — a substitute typeface without a genuine light cut
  will make the whole system feel broken rather than airy.
- The hard "green never fills, marigold never speaks" rule is easy to violate
  under marketing pressure (a green promotional badge, a marigold headline) and
  needs active enforcement to hold.

## Signature move

The marigold search bar: a 40px-radius pill spanning nearly the full hero
width, floating across the bottom edge of the asymmetric photo pair — the
booking widget doubles as the hero's single chromatic event rather than being
a separate utility bolted beneath it.

## Motion

(from designlang extract) Feel reads as springy, and the page is scroll-linked —
a real surprise against the "restraint as a design value" reading: alongside a
plain `ease` and a standard `cubic-bezier(0.4, 0, 0.2, 1)`, the extract confirms
a genuine spring/overshoot curve, `cubic-bezier(0.665, 0.425, 0.44, 1.105)`, in
use across five duration steps from 100ms to 1s. So the restraint is visual,
not kinetic — interactive elements likely settle with a small bounce rather
than a flat linear stop. Worth noting: the extract's own #fcbd1c usage count is
exactly 1 across the whole page, a literal confirmation of the "marigold, one
use per screen" rule stated in the frontmatter traits. (observed in capture)
the live capture confirms a static composition matching the layout closely (same
marigold search bar, same asymmetric photo pair, same announcement bar); given
the zero-shadow register, hover states most plausibly still shift the pill link
button's fill from transparent to charcoal, now most likely with that spring
settle rather than a flat cut.

| Token | Value | Easing |
|---|---|---|
| xs | 100ms | `ease` |
| sm | 200ms | `ease` |
| md | 300ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| lg | 500ms | spring |
| xl | 1s | spring |
| spring/overshoot | — | `cubic-bezier(0.665, 0.425, 0.44, 1.105)` |

## Brief

Build a warm, editorial cabin-booking landing page. Canvas is cream paper
`#f7f0e1`; charcoal `#23212c` carries all body text and hairline borders —
never pure black. Pine green `#006434` is reserved strictly for the wordmark,
hero headings and inline links; marigold `#fcbd1c` is reserved strictly for the
search bar and accent-block surfaces — neither colour crosses into the other's
role. Set every heading and most body copy in one typeface at weight 300, with
weight 400 only for meta labels and captions; tighten tracking from -0.02em at
40px display down to -0.005em at 12px caption. Round every interactive element
generously: 20px for cards/buttons, 40px for hero cards, 99px for pills — never
below 12px anywhere. Compose the hero as an asymmetric 2-column image pair
(roughly 60/40 width split) with a marigold 40px-radius search pill floating
across the bottom. Ban shadows entirely; depth comes only from cream-on-cream
layering and radius. Caption every photo section with a small uppercase meta
tag before any descriptive copy, and keep the footer on the same cream canvas
with no dark inversion.

## Image recipe

Editorial lifestyle photograph of [SUBJECT] — a cabin or nature retreat in soft
natural daylight, warm greens and muted earth tones, generously sized and
un-cropped within its rounded frame, shot as a documentary travel-journal
image rather than a styled real-estate listing, no heavy retouching or
saturation boost.

## Photo search

Unsplash first, Pexels second.
- "cabin in forest natural light exterior"
- "cozy cabin interior warm light"
- "nature retreat meadow morning light"
- "person reading terrace outdoor cabin"

## Reference lock

Primary reference/direction: Raus — whisper-weight editorial cabin-booking
journal, one marigold booking bar as the page's sole loud gesture.
Preserve (3-5 traits): cream paper `#f7f0e1` canvas with charcoal `#23212c`
ink, never pure black or white; weight 300 default across nearly every text
role, weight 400 reserved for meta/caption only; Pine green confined to
wordmark/headings/links, marigold confined to the search bar and accent
surfaces, never crossing roles; minimum 20px radius on every element, zero
shadow anywhere; asymmetric (never symmetric) hero photo composition.
Borrow only (1-2): the marigold search-bar-as-hero-CTA device; the small
uppercase "IDEA ##" category label preceding editorial captions.
Role rules: marigold never sets text; pine green never fills a button or
badge; body copy never centres; no radius below 12px on any clickable element.
Media strategy: photo:unsplash — warm, documentary nature/cabin lifestyle
photography only; no staged real-estate photography, no 3D renders.
Reject: drop shadows or elevation; sharp corners (0-8px); a second bright
accent colour; a centred hero stack; Pine green as a CTA fill.
Token commitments: bg `#f7f0e1`, ink `#23212c`, ink-white `#ffffff`, brand-green
`#006434`, accent `#fcbd1c`, sky `#a6dfff`, ember `#dd5000`; type weight 300
default/400 at meta sizes; display 40px/leading 0.95/-0.02em tracking down to
caption 12px/leading 1.18/-0.005em; radius 20px default, 40px hero cards, 99px
pills; page max-width 1280px, section gap 80-120px.
