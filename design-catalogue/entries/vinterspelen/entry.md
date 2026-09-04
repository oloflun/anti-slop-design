---
title: "Vinterspelen"
url: file:///C:/Users/Anton%20L/anti-slop-design/sites/vinterspelen.html
captured: 2026-09-03
family: gustavian-salon
dna: "Opera playbill x museum wall label"
register: historical art
grammar: chaptered editorial
lane: "Deep teal salon lit by candle ochre, alternating with paper programme pages of numbered acts and dot-leader cast lists, interrupted by a scroll-driven stage machine that slides painted wing flats aside"
mode: persuade
traits: ["deep teal salon ground", "candle ochre accent", "Bodoni Moda display", "Newsreader body", "public-domain museum art only", "gilt-framed image plates", "dot-leader cast lists", "roman-numeral acts", "scroll-driven wing flats", "inventory-number captions"]
palette: ["#091C1F", "#13282B", "#213537", "#0B0603", "#EAE3D5", "#DAD1C0", "#ECE7DE", "#281E17", "#DAAE50", "#704100", "#A23432"]
type: ["Bodoni Moda", "Newsreader"]
kind: example
source: claude
origin: example-site
extract: none
category: editorial
category2: "institutional"
status: ready
---

## Why it works

Every image on the page is public-domain museum art — Pilo, Hilleström, Roslin,
Desprez, Piranesi — pulled from Nationalmuseum and The Met, and every one is
captioned with artist, title, year and inventory number (`Nationalmuseum, NM
18007`). A page about an eighteenth-century theatre is therefore illustrated with
eighteenth-century pictures rather than with a modern photograph pretending to be
old. It costs nothing, it cannot be mistaken for stock, and the credit line becomes
part of the design instead of a legal afterthought.

The colour scheme is a lit room. Deep teal `#091C1F` is the darkened salon, ochre
`#DAAE50` is candlelight, and the paper sections `#EAE3D5` are the programme in
your hands. Because there are only two states — room and paper — the alternation
reads as house lights down, house lights up, and the reader always knows which
they are in.

The programme is set as an actual playbill. Roman-numeral act, work title in Bodoni
italic, composer and librettist line in tracked micro-caps, a paragraph, then a
cast list with dot leaders running from role to singer — `Orfeo ......... Elin
Norlander`. Dot leaders are a typographic convention from printed programmes that
almost no website uses, and they do the job here perfectly: two columns, no table,
no borders.

The facts are specific enough to be checkable, and they are set as display type:
`2.20` playing time, 214 wax candles, 415 hertz, gut strings, 62 kilos in the
flying rig, 9 surviving back cloths of which four can still be hung. A page that
tells you the orchestra tunes low and the theatre has no amplification is selling
the constraint as the product.

Images are framed rather than bled. Each plate sits in a double gilt-line frame on
the teal ground with the caption in italic beneath — the exact treatment of a
picture hung on a wall or reproduced in a catalogue. Full-bleed would have been the
obvious move and would have destroyed the museum register.

## What to borrow (principle)

- **Illustrate from open museum collections.** Nationalmuseum, The Met, Rijksmuseum
  and Wikimedia Commons are free, period-accurate and unmistakably not stock. Caption
  with artist, title, year and inventory number and the provenance becomes design.
- **Two states, not five.** One dark "room" ground and one paper ground, alternating,
  will chapter a long page better than a palette of section colours.
- **Steal conventions from the printed artefact you are replacing.** Dot leaders,
  roman-numeral acts, a composer line in micro-caps — a playbill already solved this
  layout in 1777.
- **Frame the pictures.** A thin double rule and a caption in italic reads as
  collection; a full-bleed crop reads as marketing.
- **Sell the constraint.** No amplification, no recording, doors closed during act
  one, 214 candles — the limitations are the argument, set at display size.

## What to leave

- Every image is hotlinked from `upload.wikimedia.org` at 1280px. Public domain is a
  licence, not a CDN — rehost the files, or the page breaks when Commons rate-limits
  or a file gets renamed.
- The stage-machine setpiece animates `letter-spacing` and `filter: blur()` on every
  frame of a scroll scrub. Both force layout or a full-frame repaint; the same effect
  is available from `transform` and `opacity` on a pre-blurred layer.
- The scrub region is a tall sticky block: several viewport-heights of scrolling that
  advance the page by one image. Beautiful once, tedious on a second visit, and
  invisible to anyone who lands mid-page from a link.
- Ochre is used on the wordmark, the nav button, the kickers, the act numerals, the
  stat figures and the closing headline — it is doing so much work that nothing it
  touches reads as emphasised any more. Pick two roles for it.

## Signature move

The stage machine. A sticky section holds six painted wing flats — cut from a real
Desprez scene drawing — that slide outward in staggered order as you scroll, outer
pair first, inner pair travelling furthest, while the back cloth behind them
un-blurs and the caption line tightens from 0.42em tracking to almost none. It is
a working model of the 1777 machinery the page is describing: the same drawing, the
same seven-second wing change, driven by the reader's own scroll. Reduced motion
and `?preview=scen` both render the finished state outright.

## Brief

Build a page for a period theatre festival on a deep teal salon ground `#091C1F`
alternating with warm paper `#EAE3D5`, with a single candle-ochre accent `#DAAE50`.
Set all display type in Bodoni Moda (italic for work titles) and all body in
Newsreader at 1.05rem/1.7; use tracked micro-caps at 11px for kickers, composer
lines and stat labels. Illustrate exclusively with public-domain museum art,
hosted by you, each plate inside a thin double gilt frame with an italic caption
carrying artist, title, year and inventory number. Set the programme as a playbill:
roman-numeral act, italic work title, composer and librettist in micro-caps, one
paragraph, then a cast list with dot leaders from role to performer, and playing
time set as a large numeral at the right. Add a stat band of three checkable
numbers in ochre display type. Interrupt once with a scroll-driven stage sequence
in which painted flats slide aside to reveal a second scene. Close on a dark
candle-lit panel with ticket prices and travel directions.

## Image recipe

Public-domain collection artwork, not generated. Search museum open-access
archives for [SUBJECT] in eighteenth-century Swedish or French painting, theatre
scene design or architectural etching; prefer oil sketches, stage drawings and
Piranesi-style etchings with deep chiaroscuro and warm varnish tone. Download the
full-resolution file, rehost it, and caption it with artist, title, year,
institution and inventory number. If a photograph is genuinely required, shoot
candle-lit interiors at ISO 3200 with no fill.

## Photo search

Museum open access first, stock never.
- Nationalmuseum (Sweden) — "Desprez scenbild", "Pilo", "Hilleström", "Roslin"
- The Met Open Access — "Piranesi Carceri", "18th century candlestick", "viola da gamba"
- Wikimedia Commons — "Gustavian theatre", "Drottningholms slottsteater"
- Rijksmuseum — "theatre machinery engraving"

## Reference lock

Primary reference/direction: Vinterspelen — deep teal salon alternating with paper programme, Bodoni Moda + Newsreader, illustrated entirely with credited public-domain museum art.
Preserve (3-5 traits): two grounds only — teal salon `#091C1F` and paper `#EAE3D5` — alternating as house-lights-down/up; candle ochre `#DAAE50` as the single accent; all imagery public-domain museum works in thin double gilt frames with artist/title/inventory captions; the playbill programme with roman-numeral acts and dot-leader cast lists; checkable specifics (candle count, pitch, playing time) set as display numerals.
Borrow only (1-2): the scroll-driven wing-flat sequence; the stat band of three ochre numerals.
Role rules: Bodoni Moda never below 18px, Newsreader never in a headline; micro-caps capped at 11px/0.16em; ochre limited to two roles per page; images always framed, never bled; every image carries a full credit.
Media strategy: public-domain museum collections, rehosted locally — never stock photography, never generated imagery for a historical subject.
Reject: hotlinking Commons or museum URLs; animating letter-spacing or blur per scroll frame; multi-viewport sticky scrubs on a primary path; full-bleed crops of collection art; a second accent colour; sans-serif.
Token commitments: sal `#091C1F`, sal2 `#13282B`, sal3 `#213537`, natt `#0B0603`, papper `#EAE3D5`, papper2 `#DAD1C0`, kalk `#ECE7DE`, tryck `#281E17`, ockra `#DAAE50`, ockra-djup `#704100`, karmin `#A23432`; display `Bodoni Moda`, body `Newsreader`; max-width 1480px, micro-caps tracking 0.16em, body 1.05rem/1.7.
