# MICROTEXT-AUDIT.md — F-016/gate 99 run over existing pages

Read-only. Run 2026-09-19 with `skills/design/scripts/microtext_scan.py` (no
`--price-ledger` unless noted) against the live pages at `http://localhost:3090/…`,
both viewports (1440px, 390px — findings were identical between the two on every
page tested, so counts below are unique findings; the script's own total doubles
them). **No page was edited for this audit.**

`--price-ledger` was also run against every page below (Calyx, Hyperborea, and
both Alunix runs carry a priced ledger). It found zero matches everywhere — no
text cell shares a digit cell's font-size on any of these pages, so F-017 is a
forward-looking rule here, not a fix.

The script is a heuristic candidate-finder, not a verdict — every row below is
scanner output plus a short human judgement per Anton's test (F-016): does the
line do a job the reader needs, or does it talk about the page/example in a
smaller-than-body size?

---

## `sites/calyx.html` — 33 unique findings (66 raw, both viewports identical)

All are the kicker microformat (`.kicker`, `font-size: 10.5px`, uppercase,
tracked) that carries Calyx's magazine apparatus, plus its own nav links at the
same size.

| Group | Examples | Genre-apparat (undantag) eller utfyllnad |
|---|---|---|
| Commission ledger metadata | `Cmsn. 0211 — Hotel Pigalle, Drottninggatan`, `02 / 14`, `cut 14.iv · serves a long table for 12` | **Undantag.** Identifies a real commission and its plate index in the atelier's own catalogue — exactly the licensed apparatus F-016 names for Calyx. |
| Edition/colophon line | `Vol. ix · spring`, `No. 042 — Spring Edition`, `© Calyx Atelier MMXXVI`, `Set in Cardo & PT Mono` | **Undantag.** Edition marker and colophon on a business that plausibly publishes an edition. |
| Client-note attribution | `Anna L., Östermalm — twice-yearly client`, `Magnus K. — Aira, Djurgården` | **Undantag.** Names a real (in-fiction) client and locates the commission — differentiates one testimonial from the next. |
| Nav links (`Index`, `Studio`, `Commission`) | — | **Undantag** in the sense that it's a real link, not descriptive text — flagged only because the mono nav voice reads small+tracked; it enables navigation, gate 99 doesn't apply. |
| `SEK` currency kicker beside each price | — | **Undantag**, and exactly the F-017 pattern done right: currency stays in the kicker, the digits carry the display size. |

**Verdict:** clean. This is the reference case for the exception, not a violation.

---

## `sites/horai.html` — 2 unique findings (4 raw)

| Group | Examples | Genre-apparat (undantag) eller utfyllnad |
|---|---|---|
| Menu figcaptions | `SANSAI · SECOND COURSE · PICKLED MOUNTAIN VEGETABLES, SOFT TOFU`, `SEKAI · FIFTH COURSE · HAND-CUT YAKISOBA WITH WAGYU SCRAPS` | **Undantag.** Names a real course and its place in the tasting menu — Hōrai's own deliberate labels, the second example FEEDBACK.md F-016 names by name as licensed. |

**Verdict:** clean.

---

## `sites/hyperborea.html` — 41 unique findings (82 raw)

Same shape as Calyx: a conference/programme ledger in the kicker microformat.

| Group | Examples | Genre-apparat (undantag) eller utfyllnad |
|---|---|---|
| Edition/colophon | `Edition MMXXVI · Vol. 03`, `© Hyperborea Föreningen MMXXVI`, `Set in Italiana, Archivo & Noto Serif JP` | **Undantag.** Edition marker on a body that plausibly runs a numbered conference series. |
| Programme schedule | `12.ix · friday`, `Programme 003`, `a three-day gathering of technologists and humanists.` | **Undantag.** Roman/day-date apparatus locates a real session in a real three-day programme — functional ordering, not decoration. |
| Speaker meta | `Machine-learning artist · Tokyo`, `Neural-interface researcher · Lund` | **Undantag.** Differentiates one speaker from the next (role + city) — this is the content, not a label describing the content. |
| Ticket tiers | `96 seats · single attendee`, `18 seats · application open`, `6 seats · letter required`, `SEK` / `SEK · funded` | **Undantag.** Real availability and condition per tier; `SEK` is the currency kicker beside a display-size price, the F-017 pattern done correctly. |
| `120 seats. Three tiers. No platinum.` | — | **Undantag** by intent — this is TASTE.md's named "values move" (a proper value statement in kicker voice), not a restated-heading filler line. |

**Verdict:** clean — same reference-case shape as Calyx, in this business's own register.

---

## `sites/tidvatten.html` — 0 findings

No text on the page is both smaller than body copy and kicker/eyebrow/caption/rail-shaped.

**Verdict:** clean, nothing to judge.

---

## `sites/index.html` — roughly 86 unique findings (171 raw)

This is the repo's own dev-facing demo index, not a client marketing page. The
finds fall into two very different buckets.

| Group | Examples | Genre-apparat (undantag) eller utfyllnad |
|---|---|---|
| Real nav/footer links (top nav, footer sitemap, upstream credits, `Open ↗`, `Scroll inside`) | `Antagonist`, `Demos`, `README`, `/calyx`, `Impeccable 29.2k★` | **Undantag.** Every one is a real `<a>`/`<button>` — the mono-tracked voice is this page's nav register, but the text enables an action (navigate, open a live demo). Not descriptive microtext; flagged only because small+tracked+uppercase matches the mechanical heuristic. |
| Per-demo register summary blobs | `Register: editorial printBuilt with Impeccable and high-end-visual-des…`, `Register: illustrated darkFourteen inline SVGs, no photography at all…` | **Borderline utfyllnad.** This *is* a small line describing what a demo is, in a dev-catalogue register that has no equivalent to Calyx's "plausibly publishes an edition" license. It carries real information (what built it) for a page whose whole job is comparing builds, which argues for keeping it — but it should be sized and placed as real body copy, not as a `.stack` micro-blob at kicker scale. Worth revisiting if this page is ever treated as a marketing page rather than an internal index. |

**Verdict:** the nav/footer noise is a false-positive class the scanner can't tell from real filler by font-size alone — expected, and why gate 99's finding is "a candidate," not an automatic fail. The one soft finding (register summary blobs) is minor and page is explicitly out of scope for edits here.

---

## `tests/alunix-r8/runs/V3c/index.html` — 9 unique findings (18 raw)

| Selector / text | Genre-apparat (undantag) eller utfyllnad |
|---|---|
| `figcaption.frame-cap` — `Exempelsida: Calyx, florist i Stockholm` | **Utfyllnad.** Anton's own named example (F-016). Names what the framed screenshot is, in a register (generic digital-byrå demo) with no license to publish captions — the frame's `title`/`aria-label` should carry this instead. |
| `figcaption.frame-cap` — `Exempelsida: Hōrai, Asian fusion-koncept` | **Utfyllnad.** Same as above — Anton's second named example. |
| `span.cap-line` — `Exempelsida: Hyperborea, konferens i Lund` | **Utfyllnad.** Same pattern as the two figcaptions, just not a `<figcaption>` tag — the mechanical scan still catches it via the class heuristic. |
| `p.kicker-sans` — `Så går det till` | **Utfyllnad.** Restates a section's own heading topic in a smaller kicker instead of being the heading. |
| `p.kicker-sans` — `Hur vi tänker` | **Utfyllnad.** Same shape as above. |
| `p.card-kicker` — `Digital byrå` | **Borderline.** A one-word category kicker above the company name — arguably identifies what kind of business this is (a function), but it is also exactly the "small label above a heading" shape gate 99 targets. Cheap to cut; not one of Anton's named examples. |
| `span` — `Design` / `Utveckling` / `System` | **Borderline.** Short service-name tags — could be read as functional (labels a service list) or as decorative capability chips. Lower priority than the figcaptions/kickers above. |

**Verdict:** confirms Anton's complaint directly — the two named figcaptions and the "Så går det till" kicker are present verbatim in this build. No page edits made; this is the read-only baseline the next session fixes against.

---

## `tests/alunix-r8/runs/V3d/index.html` — 11 unique findings (22 raw)

Same page family as V3c, one step further into the pattern — `EXEMPELCASE` now
appears twice and `Från exempel till er sida` (also one of Anton's four named
examples) shows up as its own kicker line.

| Selector / text | Genre-apparat (undantag) eller utfyllnad |
|---|---|
| `figcaption.frame-cap` — `Exempelsida: Calyx, florist i Stockholm` | **Utfyllnad.** Same as V3c. |
| `figcaption.frame-cap` — `Exempelsida: Hōrai, Asian fusion-koncept` | **Utfyllnad.** Same as V3c. |
| `span.cap-line` — `Exempelsida: Hyperborea, konferens i Lund` | **Utfyllnad.** Same as V3c. |
| `p.kicker-sans` — `Så går det till` (flagged `short-grey-line-near-heading` here, not on V3c — smaller/greyer in this run) | **Utfyllnad.** Anton's third named example, present verbatim. |
| `p.kicker-sans` — `Från exempel till er sida` | **Utfyllnad.** Anton's fourth named example, present verbatim, plus flagged as a short grey line sitting right above a heading — the exact shape F-016 describes. |
| `p.kicker-sans` — `Exempelcase` ×2 | **Utfyllnad.** Repeats across the page — a section label that only names "this is an example," which the reader already knows from context. |
| `p.card-kicker` — `Digital byrå` | **Borderline**, same read as V3c. |
| `span` — `Design` / `Utveckling` / `System` | **Borderline**, same read as V3c. |

**Verdict:** the clearest hit of the whole audit — all four of Anton's literally-named examples appear verbatim on this one page. Confirms the ban targets a real, currently-shipping pattern, not a hypothetical.

---

## Summary

| Page | Unique findings | Verdict |
|---|---|---|
| `sites/calyx.html` | 33 | Clean — licensed genre apparatus throughout |
| `sites/horai.html` | 2 | Clean — licensed genre apparatus |
| `sites/hyperborea.html` | 41 | Clean — licensed genre apparatus throughout |
| `sites/tidvatten.html` | 0 | Clean |
| `sites/index.html` | ~86 | Mostly real nav/footer links (false positives by design of the heuristic); one minor borderline (register-summary blobs) |
| `tests/alunix-r8/runs/V3c/index.html` | 9 | Two named-example figcaptions + one named-example kicker present; several borderline |
| `tests/alunix-r8/runs/V3d/index.html` | 11 | All four of Anton's named examples present verbatim |

`--price-ledger`: zero findings on every page — F-017 has no existing violation to
fix, only future builds to hold to the rule.

No page was modified as part of this audit.
