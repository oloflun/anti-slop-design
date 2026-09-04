---
title: "Tidvatten"
url: file:///C:/Users/Anton%20L/anti-slop-design/sites/tidvatten.html
captured: 2026-09-03
family: slate-harbour
dna: "Grotesk poster x bathhouse ledger"
register: editorial print
grammar: chaptered editorial
lane: "A cold slate reading column punctuated twice by full-bleed dark panels — the sea hero and a scroll-scrubbed temperature diptych — closing on a dark practical footer"
mode: persuade
traits: ["cold slate ground", "Familjen Grotesk display over Literata body", "Fragment Mono kickers at 10.5px/0.22em", "sticky label column on a 12-col grid", "§-numbered bylaw rows", "scroll-scrubbed 2°/85° diptych", "ember orange as sole accent", "full-bleed dark interludes"]
palette: ["#E7ECF0", "#D9E1E6", "#ECF1F3", "#0D171F", "#151B22", "#1A252F", "#4B545B", "#AFB9BF", "#AB3E00", "#D87339", "#396250"]
type: ["Familjen Grotesk", "Literata", "Fragment Mono"]
kind: example
source: claude
origin: example-site
extract: none
category: hospitality
category2: "institutional"
status: ready
---

## Why it works

Three typefaces, three jobs, no overlap. Familjen Grotesk set tight at `-0.02em`
does every headline, price and address — it is the club shouting across a pier.
Literata at 18px does every sentence of actual prose. Fragment Mono, locked at
10.5px and 0.22em and never once larger, does every label, time, counter and
byline. Because each face is confined to one register, the page needs no chrome
to signal hierarchy: the reader can tell a fact from a voice from a label by
shape alone.

The ground is the argument. `#E7ECF0` is not white — it is the specific cold
slate of Öresund light in February, and everything warm on the page is
rationed against it. Ember `#AB3E00` appears on kickers, on prices, on the
mailto, and nowhere else; the only other heat is photographic, in two fires.
A cold-bath club that used a warm ground would be lying about the product.

The layout commits to an asymmetry and holds it: a mono kicker plus a grotesk
head sit in columns 1–3, sticky, while the reading column runs 4–12. The label
column staying pinned as the prose scrolls means the reader never loses which
chapter they are in, and it makes the empty left margin structural rather than
decorative.

The persuasion is done entirely in administrative register. The philosophy
section quotes its own bylaws — `§4 Tystnad på lavarna före klockan sju` —
ruled like a statute. The programme is four numbered fixtures with times and
seasons, not four benefit cards. The membership is three roman-numeraled tiers
against real kronor, closing on `Ingen platinanivå finns. Piren är lika kall
för alla.` Nothing is claimed that is not also scheduled or priced.

## What to borrow (principle)

- **Three faces, three sealed jobs.** Grotesk speaks, serif explains, mono
  records. Cap the mono at caption size and never let it carry a sentence.
- **Pick a ground with a latitude.** A specific cold grey commits the whole
  palette; ration exactly one warm accent against it and let photography carry
  the rest of the heat.
- **Sticky label column, scrolling content column.** Kicker plus head in cols
  1–3 pinned, prose in 4–12. Cheap, and it keeps orientation without a nav.
- **Sell by quoting your own paperwork.** Bylaw numbers, opening hours, a
  ledger of tiers with prices. Rules are more credible than adjectives because
  they cost the writer something.
- **Scrub a set-piece, don't trigger it.** Drive the animation off the section's
  distance from viewport centre so it runs backwards on the way up, and author
  the CSS base state as the *finished* state so a dead script leaves it legible.

## What to leave

- The fixed grain overlay: a full-screen `mix-blend-mode: multiply` SVG
  turbulence layer at 0.45 opacity, `z-index: 60`. It buys a texture almost no
  one consciously registers, costs a permanently composited layer over
  everything, and muddies an already low-chroma palette — visibly so on the
  ember accents.
- Tailwind via `cdn.tailwindcss.com`, with the nav toggling `bg-hav/90` and
  `backdrop-blur-md` by `classList.add` at runtime. It works only because the
  Play CDN watches the DOM; it is a production tell and a hard dependency on a
  script that is explicitly not for production.
- Vertical pacing in the middle third. The dark set-piece section and the gap
  below `.04 Gästeldare` both run close to a full viewport of near-empty
  ground. Restraint reads as confidence once; twice in a row reads as an
  unfinished layout.
- The blanket `.reveal` — a 1.25s opacity-and-translate transition applied to
  most blocks on the page. The four guard clauses around it (mount check, zero
  threshold, 3s failsafe, noscript fallback) are the right engineering, but
  they are engineering spent defending a decision worth reversing: if
  everything eases in, nothing is emphasised.

## Signature move

The temperature diptych. On a full-bleed dark panel lit by one fire photograph,
`2°` in cold grey and `85°` in ember sit either side of a single hairline, each
under a mono label — `HAVET`, `BASTUN` — with `DÄREMELLAN: FYRTIO STEG PÅ BLÖT
EK.` beneath. Both numerals are scrubbed continuously by the section's distance
from viewport centre, so the contrast builds as you arrive and unwinds as you
leave. The entire proposition of a cold-bath club stated as two numbers and the
walk between them.

## Brief

Build a cold-slate editorial page for a members' club whose product is physical
discomfort. Ground everything on `#E7ECF0`, a specific February grey, with deep
sea `#0D171F` for full-bleed interludes and a single ember `#AB3E00` as the only
warm colour on the page. Use three faces with sealed jobs: a grotesk (Familjen
Grotesk) tracked `-0.02em` for all display, prices and addresses; a serif
(Literata) at 18px for every sentence of prose; a mono (Fragment Mono) fixed at
10.5px and 0.22em uppercase for every label, time and counter. Open full-bleed
on the subject photographed at eye level, wordmark set huge along the bottom
edge under a three-stop scrim. Below, run a 12-column grid where a mono kicker
and grotesk head sit sticky in columns 1–3 and prose runs 4–12. Prove the club
by quoting its own paperwork — numbered bylaws, a `.01–.04` programme with real
times and seasons, and a roman-numeraled membership ledger with real prices.
Break the light column exactly twice with dark panels, one of them a
scroll-scrubbed pair of temperatures. Close on a dark contact panel with an
address, a ruled hours table and nothing else.

## Image recipe

Documentary photograph of [SUBJECT] in northern winter light, shot on 35mm at
dusk or first light, natural available light only — no strobe, no fill. Cool
desaturated slate blues throughout with heat confined to a single practical
source (fire, ember, low sun) occupying under a fifth of the frame. Water or
timber at eye level rather than shot from above. Human figures, if any, in
silhouette and mid-action, never posed or looking at camera. Grain retained,
highlights allowed to clip, no colour grading toward teal-and-orange.

## Photo search

Unsplash first, Pexels second.
- "cold sea surface eye level winter"
- "wood fired sauna interior dark"
- "beach bonfire silhouette dusk"
- "nordic harbour pier winter fog"

## Reference lock

Primary reference/direction: Tidvatten — cold slate bathhouse ledger, Familjen Grotesk + Literata + Fragment Mono, membership sold as paperwork.
Preserve (3-5 traits): cold slate ground `#E7ECF0` against deep sea `#0D171F`; three faces with sealed jobs (grotesk display / serif prose / mono metadata at 10.5px, 0.22em); 12-col grid with sticky kicker-and-head column at 1-3 and prose at 4-12; administrative persuasion — numbered bylaws, `.01–.04` fixtures with real times, roman-numeraled priced tiers; exactly two full-bleed dark interludes in an otherwise light column.
Borrow only (1-2): the scroll-scrubbed `2° / 85°` temperature diptych; ember `#AB3E00` on kickers and prices only.
Role rules: grotesk never sets prose, serif never sets a label, mono never sets a sentence; mono capped at 10.5px and 0.22em uppercase; ember reserved for kickers, prices and the mailto — never a filled button; every claim must carry a time, a rule number or a price.
Media strategy: photo:unsplash — available-light documentary frames at eye level, heat confined to one practical source; every figure captioned in mono with a date or a time.
Reject: fixed grain overlays; Tailwind Play CDN in anything shipped; blanket reveal transitions; warm or pure-white grounds; a second accent colour; icon-card "our values" rows; centred hero with two buttons; teal-and-orange grading.
