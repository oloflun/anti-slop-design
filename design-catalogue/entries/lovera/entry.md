---
title: "Lovera"
url: https://td-lovera.framer.website
source_url: https://td-lovera.framer.website
captured: 2026-09-04
origin: raw-url
raw: raw/49f72a731343535e-td-lovera-framer-website.webp
extract: ok
category: portfolio
category2: product-focused
family: ghost-wordmark-bento-studio
dna: "Irreverent statue-hero agency branding x SaaS-dashboard bento proof"
register: modern clean
grammar: split stage
lane: "A near-black hero pairs a giant ghosted wordmark watermark with a classical statue wearing sunglasses and a chain, then the page drops to a white bento grid of client logos, stat cards and a mini process timeline"
mode: persuade
traits: ["near-black hero ground", "oversized ghosted wordmark watermark", "irreverent statue photography", "single orange pill CTA", "white bento-card proof grid", "large numeral stat cards", "mini process timeline chart", "circular avatar stack"]
palette: ["#FFFFFF", "#171717", "#434645", "#FF531F", "#FF825C", "#DDDFDE"]
type: ["Apfel Grotezk", "Oswald", "Antonio"]
measured: designlang
kind: reference-style
source: claude
status: ready
---

## Why it works

The hero earns attention through incongruity rather than polish: a classical marble bust
wearing mirrored sunglasses and a chunky chain sits against a near-black ground, with the
studio's own wordmark ghosted at giant scale directly behind it as a watermark. The joke
(old-world statuary styled as a modern founder) does the branding work a tagline usually
has to do — "creative studio for founders" reads as confirmed by the image before the
headline is even parsed.

Type carries three distinct jobs on one screen: a bold grotesque for the headline, a
smaller sans for the service list and supporting paragraph, and an orange pill CTA that is
the only saturated colour in the entire hero. Because everything else is black, white or
grey, the orange button and the statue photograph are the only two places the eye can
land, which keeps the "See pricing" CTA from getting lost against the busy background
texture.

The copy voice makes the same founder-to-founder move the imagery does: the extract
classifies it as friendly and moving we→you — the studio introduces itself in the
collective "we help brands grow," then addresses the visitor directly in service and CTA
copy, mirroring the hero's shift from brand statement to direct pitch.

Below the fold, the page changes vocabulary entirely, into a white bento grid that
borrows directly from SaaS product-dashboard convention: large numeral stat cards ("40%",
"$12M"), a client-logo strip, an avatar stack, and a small process timeline rendered as a
literal mini Gantt chart. For a design studio, presenting its own case-study proof in the
same visual language as a software dashboard is a considered choice — it signals "we can
build you this exact kind of interface," making the proof section itself a portfolio
piece.

## What to borrow (principle)

- **Use an oversized ghosted wordmark as hero texture**, not a literal logo lockup — it
  reinforces brand presence without competing with the photograph in front of it.
- **Let incongruous photography state your position before your headline does.** One
  striking, unexpected image can carry positioning that would otherwise need a paragraph.
- **Reserve your one accent colour for exactly the CTA**, when the surrounding hero is
  otherwise pure black/white/grey — the eye has nowhere else to land.
- **Present your own proof in the visual language of what you sell.** A studio that builds
  dashboards should show its own results as a dashboard, not a testimonial slider.

## What to leave

- The "Made in Framer" and "Get the template" badges are marketplace/tool artifacts, not
  part of the studio's own design system — exclude from any derived build.
- The ghosted wordmark watermark sits close enough in value to the dark background that
  it's barely legible in this capture — effective as texture, but if it's meant to be read
  at all it needs more contrast.
- Three different type families in one hero screen (Apfel Grotezk, Oswald, Antonio, per
  computed styles) is more type-system complexity than the visual result telegraphs;
  consolidating to two would likely be indistinguishable to a viewer while easier to
  maintain.

## Signature move

The photographic non-sequitur: a classical marble statue styled with sunglasses and a
chain as the entire hero image, doing the positioning work of "irreverent, confident,
culturally fluent" that this kind of agency site usually spends a full paragraph trying to
establish.

## Motion

The designlang extract (separate from the static `capture.py` scroll-through) reads the
overall feel as mixed and confirms scroll-linked behaviour, but the motion it can actually
verify is limited to quick hover/state transitions, not the bento grid's chart or counter
animations. Two durations are in use, 200ms and 300ms, carried by two distinct custom
easing curves: `cubic-bezier(0.81, 0.12, 0.25, 0.87)` on 200ms colour transitions, and the
same steep, symmetric `cubic-bezier(0.44, 0, 0.56, 1)` seen on Rogo, here driving 300ms
background-plus-box-shadow pairs (card/button hover). The first curve's control points
are unusually ordered (its x-values run high-to-low rather than low-to-high), which
typically reads as a slight anticipation or bounce on the way in rather than a plain
ease — the only near-spring quality found in this set of four. Only one keyframe is
defined in the CSS (`__framer-loading-spin`, a 360deg rotation) and it isn't in the "in
use" set, so the bento-card counter-up/chart-draw animation implied by the still frames
remains unconfirmed rather than disproven (from designlang extract).

| Duration | Easing | Applies to |
|---|---|---|
| 200ms (`sm`) | `cubic-bezier(0.81, 0.12, 0.25, 0.87)` | colour (slight bounce/anticipation quality) |
| 300ms (`md`) | `cubic-bezier(0.44, 0, 0.56, 1)` | background, box-shadow |

## Brief

Build a creative-studio landing page opening on a near-black hero with an oversized
ghosted wordmark watermark behind one striking, unexpected photograph that states the
studio's position without need for a long headline. Set the headline in a bold grotesque,
service list and supporting copy in a plain sans, and use exactly one saturated accent
colour for the primary CTA — nothing else in the hero should carry colour. Below the
fold, present client proof and results in a white bento grid styled like a product
dashboard: large numeral stat cards, a client-logo strip, a small avatar stack, and a
literal mini process-timeline chart. Let the proof section itself demonstrate the kind of
interface work the studio sells.

## Image recipe

High-contrast black-and-white photograph of [SUBJECT] — a classical statue or bust styled
with an incongruous modern accessory (sunglasses, jewellery, streetwear) — shot with
dramatic, slightly cool studio lighting, sharp detail on stone texture, composed with a
plain dark background so a ghosted wordmark watermark can sit behind it without
distraction.

## Photo search

Unsplash first, Pexels second.
- "classical marble statue sunglasses"
- "greek bust modern styling black white"
- "statue portrait dramatic lighting"
- "marble sculpture close up studio"

## Reference lock

Primary reference/direction: Lovera — ghosted-wordmark statue hero, white bento-dashboard
proof section for a creative studio.
Preserve (3-5 traits): a near-black hero with an oversized ghosted wordmark watermark
behind one striking, non-literal photograph; exactly one saturated accent colour reserved
for the primary CTA in an otherwise black/white/grey hero; a white bento-grid proof
section styled as a product dashboard (numeral stat cards, logo strip, avatar stack, mini
timeline chart); client and results proof presented as dashboard UI rather than
testimonial text.
Borrow only (1-2): the small circular avatar stack as a trust signal; the mini Gantt-style
process timeline card.
Role rules: hero accent colour appears only on the primary CTA, never a second element;
the ghosted watermark stays behind photography, never overlapping legible copy; bento
cards below the fold stay ungapped-white with consistent corner radius, no card exceeds
two content types (a stat, a chart, a quote — never combined).
Media strategy: photo:unsplash — high-contrast black-and-white statue/sculpture
photography styled with an incongruous modern element; never a straight, unstyled classical
photograph.
Reject: multiple accent colours in the hero; a literal (non-ghosted) giant wordmark
competing with the hero photo; testimonial sliders or quote carousels in place of the
dashboard-style proof grid; template-marketplace UI chrome left in the design.
Token commitments: hero-bg `#121212`, hero-ink-soft `#302F2E`, warm-tint `#816960`,
warm-pale `#C6B0AB`, paper `#DDDAD9`, proof-bg `#FFFFFF`; display `Apfel Grotezk` /
`Oswald` for headlines, `Antonio` for supporting copy; single accent colour reserved for
CTA only.
