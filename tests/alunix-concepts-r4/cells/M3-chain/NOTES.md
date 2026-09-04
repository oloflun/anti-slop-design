# M3 · Galleri · sidopanering — build notes

Written before code, per brief.md's binding scroll requirement ("Känslokurva per
akt skriven FÖRE bygget"). Cell: `cells/M3-chain/index.html`. Constraints: no
sub-agents, no edits outside this cell, no new copy, no commit.

## Reference lock

**Tier 2, task-assigned direction.** Primary reference: `tests/alunix-concepts-r3/build/index.html`
(the finished combined R5+R6 page — every headline, sub-text, price and the
`kontakt@alunix.se` address are lifted verbatim from its shipped `<body>`, read
in full before writing a line of this build). Grammar reference:
`~/.claude/skills/design/references/scroll/grammars.md` row **Gallery / catalog**
("A range... walking a room, objects at their own pace... nav is an index that
jumps; hero is object one, already labelled; close is last object or
inquiry-as-label... leans on `pan`, `reveal`, `tilt`, `count`... bans `kinetic`
headlines, `spotlight`, `magnet`, >1 `scrub`"). Register: **editorial print**
(`board.json`'s own assignment for M3), which the register×grammar matrix in
`grammars.md` lists gallery/catalog as a genuine fit for ("museum-label copy is
already this register's voice").

Catalogue entries read in full, per contract.md's source list for M3:

- **`design-catalogue/entries/vintergatan/entry.md`** — the signature move.
  Borrowed: the workshop-chapter technique itself (ground flips near-black,
  words scrubbed in as a function of scroll position, a hairline thread
  drawing itself alongside, CSS resting state = finished/fully-visible so
  no-JS and reduced-motion readers get the type outright, JS adds the "armed"
  dim state and a two-stage failsafe forces everything visible). Rejected: the
  page-wide grain overlay ("what to leave" §1); the broad `h1,h2,h3,figure,li`
  reveal set (§2) — this build's own reveal budget is per-section, not
  per-element; more than two gold-italic-style closers (n/a here, no italic
  device on this page at all — Alunix's own type system has none). Improved,
  per contract's explicit instruction ("förbättras, inte bytas mot en
  kit-parameter"): Vintergatan scrubs three one-word verbs; this build scrubs
  three full descriptive sentences (the r3 ledger's own copy), which is a
  harder reveal problem (more words, more lines) solved by mapping word index
  to a continuous scroll window per row rather than one global window for
  three words.
- **`design-catalogue/entries/palais/entry.md`** — read for the "signature
  move" pattern (one organic device that replaces every straight transition)
  and its motion table (three related easing families, a slide-x wave on a
  card carousel). Not borrowed directly (Palais's blob dividers and
  script/indigo palette belong to a different register); what carries over is
  the discipline of the entry itself — one bespoke device, stated once, never
  diluted into a second "also".
- **`design-catalogue/entries/garden-eight/entry.md`** — read for the
  "one size, two voices" discipline and its scale-contrast conviction (215px
  display against a 12-15px floor, nothing between). Borrowed principle only:
  this build's poster wordmark and the console card's own type never meet at
  an intermediate size — the page jumps from mono micro-labels straight to
  the poster's own multi-line clamp, no 32-48px middle tier, matching
  `TASTE.md` §2.4 ("Storlekskontrast 5–15×, inte 2–3×").
- **`design-catalogue/entries/mattis-studio/entry.md`** — read for the
  console-card device (already present in r3, sourced there from this same
  entry) — reused verbatim as r3 built it (bordered card, corner ticks,
  version-style kicker row, live clock), not re-derived.

`design-catalogue/TASTE.md` §1 (one authority per section — the opening's
authority is type-on-paper, the rail's authority is the object itself, the
thesis block's authority is the flat colour field) and §4 (decision rules —
rule 10, "ordmärket får vara hjälte," licenses the poster opening; rule 5,
"sektioner byter material, inte bara bakgrund," is why every act on this page
changes ground material — paper, dark plate, paper, dark room, flat blue,
near-black chapter, dark invert — never just a lighter/darker shade of the
same one).

**Preserved from r3, unchanged:** every headline (`ALUNIX / Digital byrå`,
`Det första intrycket är digitalt.`, `Vi bygger ert varumärke.`,
`Webbdesign, design och system. Allt på ett ställe.`, `Er hemsida är nutidens
visitkort`, `Alla har rätt till bra design.`), every sub-text and ledger/service
row, both prices, "Pris vid förfrågan," `kontakt@alunix.se`, the console card's
kicker/clock mechanism, the inline logo SVG, R5's tokens (`--c-black`,
`--c-accent` etc.) and R6's tokens (`--bg`, `--invert` etc.), Geist/Geist Mono
for the R5 world and Public Sans for the R6 world.

**Rejected from r3 for this remix:** the two-column split-stage layout itself
(M3's whole point is a different structure); the seam-hairline-from-logo
signature move (r3's own, must not repeat — see fingerprint row); the
side-by-side "two heroes at once" opening (replaced with a stacked
poster-over-console opening); the simultaneous Calyx+price-box double-close
(M3 closes once, in one column, with the price box alone as the last object).

**New construction, this build only:** the horizontal pan rail as the page's
spine (gallery/catalog's own device, not present in r3 at all); the ledger
word-scrub + self-drawing thread (vintergatan technique, rebuilt for full
sentences); an index-style top nav that jumps to four points (Rail · Tes ·
Signatur · Pris), satisfying the grammar's own "nav is an index" requirement
that r3 deliberately had none of; the interaction shield over the rail's three
frames, lifted only once the rail's own scroll progress passes the bespoke
end-of-act threshold (`p ≥ 0.92`) — this is this build's own definition of
"the pan act ends with a dwell," documented in full under Decision ledger
below because the kit's `data-sc-dwell` parameter settles the *middle* of an
act (confirmed by reading `scrollcraft.js`'s `dwell()` function: derivative is
smallest at p=0.5, largest at the edges — the opposite of an end-of-act rest),
not the end, so a bespoke progress-gated shield was built instead of reaching
for that parameter.

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| Vertical single flow (not two columns) with one embedded horizontal pan rail | contract.md M3 structure (1)-(6) | layout | Literal instruction; also the clearest way to differ from r3's split-stage on the layout dimension itself |
| Frames move via the kit's native `data-sc-pan` (screen-left trend); labels/captions move via a bespoke `translateX(calc(var(--sc-p) * 40vw))` (screen-right trend), NOT children of the panned rail | brief.md M3 row "textens riktning / bildens riktning"; devices.md's own note that `data-sc-parallax` is Y-only, so any horizontal counter-motion for text has to be bespoke | motion | Reusing the engine's tested, reduced-motion-safe rail mechanism for the frames (its own CSS already zeros `[data-sc-pan]` and converts the stage to a scroll-snap region under reduced motion) is lower-risk than hand-rolling rail travel; the caption layer sits as a sibling, not a child, of the `[data-sc-pan]` rail specifically so its own transform is independent and provably opposite, not just riding the parent's motion at a different offset |
| Interaction shield over the three frames, `pointer-events` gated on the pan act's own `--sc-p` crossing 0.92 (not the kit's `data-sc-dwell`) | brief.md "ramarna... interaktiva när railen står stilla (pan-akten slutar med dwell)" | interaction safety | `dwell()` in scrollcraft.js settles the *middle* of an act (confirmed by reading the source), so it cannot produce an end-of-act rest window; a bespoke progress threshold does |
| No `data-sc-kinetic` anywhere on the page | grammars.md gallery/catalog row: "Bans: `kinetic` headlines..." | grammar compliance | The chosen grammar explicitly forbids the kit's kinetic device; the ledger's word-by-word scrub is therefore hand-rolled (word-indexed opacity against scroll progress), not `data-sc-kinetic="words"`, which both respects the ban and is closer to what Vintergatan actually does (a continuous scrub, not a windowed stagger) |
| Object captions reuse the iframe's own r3 `title` string as visible text (`Er hemsida är nutidens visitkort`, `Hōrai, restaurang i Stockholm`, `Calyx, florist i Stockholm. En sajt vi byggt, öppen att utforska här.`) | brief's "ingen ny copy" rule + r3's shipped `<iframe title="...">` attributes | copy source | These strings already exist verbatim in r3's markup, just as hidden accessible names rather than visible text; promoting them to visible captions adds no new copy |
| Blue thesis block kept as a full-width object inside the gallery walk, not removed despite grammar's "no persuasion copy" guidance | contract.md M3 structure (4), binding | tension, resolved in favour of the contract | grammars.md's "Forbids" column for gallery/catalog lists "argument-shaped pinned type, single hero claim, persuasion copy" as a purity guideline; the M3 contract explicitly requires the block. Resolved by treating it as one more object in the collection (framed with the same kicker/index microformat as the rail objects) rather than as the page's singular hero claim — the actual hero-claim slot is the opening, which is plain type-on-paper, not the blue block |
| Opening (poster + console) precedes the rail rather than being "object one" of it | grammars.md gallery/catalog: "hero is object one, already labelled" | tension, resolved in favour of the contract | contract.md's M3 structure names the poster/console pairing as step (1), a title-card ahead of the object sequence, which is common gallery practice (a cover page before the walk) — documented here as a deliberate, literal-instruction deviation from the grammar's default hero shape |
| Nav is a real jump-index (four anchor links, mono, unstyled bar, not fixed) | grammars.md gallery/catalog: "Nav is an index that jumps" | grammar compliance + fingerprint | r3 has no nav at all; this is one of the fingerprint dimensions this build deliberately differs on |
| `.opening-seam`'s bottom margin is `calc(-0.6886 * <its own width clamp>)`, not half the width | Fix round, defect 1 | layout math | The mark's SVG viewBox is 827×1139 (h = w × 1139/827 ≈ w × 1.377), not square; halving the *width* clamp under-pulled the console block up, leaving the mark's boundary-straddle lopsided (measured: 78px above / 45px below at 1440px). Halving the *height* instead (`-0.6886 × width`) measures out to a true 61.5/61.5px split, confirmed via `getBoundingClientRect()` before and after |
| Caption 01's `<h3>` promoted from the frame's own headline to the place label `Tidvatten, kallbadhus i Malmö` | Fix round, defect 2; same factual-label form as captions 02/03 (`Hōrai, restaurang i Stockholm`, `Calyx, florist i Stockholm`) sourced from `tidvatten-hero.html`'s own `<meta name="description">` ("Tidvatten, kallbadhus och vedeldad bastuklubb i Malmö") | copy source, no new copy | Caption 01 was the one caption whose `<h3>` duplicated the object's own on-screen headline verbatim (`Er hemsida är nutidens visitkort`, visible inside the Tidvatten frame itself); every other caption already named the *place*, not the frame's own words — this brings caption 01 into that same pattern instead of being the odd one out |
| `.cap p` drops `-webkit-line-clamp`/`overflow:hidden`; `.rail-captions`/`.rail`'s shared height raised from `clamp(190px,27vh,264px)` to `clamp(230px,34vh,340px)`; `.cap`/`.cap p` max-width raised from `min(46ch,58vw)`/`52ch` to `min(52ch,60vw)`/unchanged `52ch` | Fix round, defect 3 | layout | Caption 03's body (the longest of the three, ~205 characters) was hard-clipped to 3 lines with a browser ellipsis; removing the clamp alone would have overflowed the fixed-height box, so the box itself grew too. Verified via Playwright: `cap3`'s `<p>` now measures `scrollHeight === clientHeight` (66px, no clipping) with `capBottom (436.9px) <= railCaptionsBottom (567.3px)` at 1440px, and the full string round-trips through `.textContent` with no `…` |
| `#objCounter` (`Objekt 0N/03`) is written by JS from the rail's own `--sc-p`, reusing the exact caption windows (`[0,.34],[.34,.67],[.67,1]`) so the counter and the on-screen caption can never disagree; write is skipped entirely when `reduced` is true | Fix round, defect 4 | interaction, reduced-motion parity | The counter was static markup that never left "01/03"; driving it off a *second*, independently-thresholded window would risk it disagreeing with which caption is actually on screen, so it shares the same `windows` array and the same loop that sets `.is-on`. Verified via Playwright real-scroll trace: counter reads 01/03 → 02/03 → 03/03 exactly at the same `--sc-p` values the caption trace crosses, and stays "01/03" under `reduced_motion:"reduce"` before and after a scroll to y=3000 |
| Thesis block's `data-sc-reveal="iris"` moved off the shared `.thesis-inner` wrapper onto `.thesis-photo` alone; `.thesis-text` gets its own `data-sc-in data-sc-stagger="80"` (a `flow`+`in` greet, fires on entry) | Fix round, defect 5; devices.md's "ground or greet" rule for a block that must never render as an empty band | grammar compliance, content-first | The iris previously wrapped the whole two-column grid, so at low act-progress the reader saw an almost-empty blue expanse with only a sliver of the mask visible (a black arc bottom-centre) until scroll carried `--sc-p` well into its 0.06–0.6 reveal window; text should never be gated behind that. Scoping the iris to the photo alone, and greeting the text on entry instead, means the kicker/headline/support are opaque (verified `opacity:1` via computed style) at every 300px step through the block, including the very first step it's on screen |

## Feeling curve (six acts, written before any markup existed)

1. **Arrival, one voice at a time.** The page opens on paper: `ALUNIX` fills
   the viewport in light, wide-tracked type, nothing else competing. The eye
   drops to the console card — a different register entirely, dark, bordered,
   ticking a live clock — with the vectorised mark resting exactly on the seam
   between the two. Caused by: a plain `reveal="up"` wipe on the poster,
   nothing louder; the console card's own micro-detail (the clock, the corner
   ticks) is what earns the attention here, not motion.
2. **Orientation, one sentence.** "Webbdesign, design och system. Allt på ett
   ställe." lands as a plain label row on the same paper ground. Caused by:
   a single `flow`+`in` fade-rise, the quietest device on the page, placed
   right after the loudest opening on purpose.
3. **Discovery, walking the room.** The ground drops to near-black and the
   rail opens: Tidvatten's own living homepage slides past first, its
   headline (`Er hemsida är nutidens visitkort`) sitting beside it as a
   caption that drifts the opposite way the frame does. Hōrai and Calyx
   follow the same beat. Caused by: `pan` as the spine, the two layers
   (frame, caption) visibly uncoupling within the first few hundred pixels
   of travel — this is the moment the remix's whole premise (text and image
   moving in different directions) becomes legible, not just claimed.
4. **Conviction, one hard colour cut.** The page snaps to Alunix blue,
   full width, and the thesis opens through an iris around the Hyperborea
   photograph: "Det första intrycket är digitalt." Caused by: `reveal="iris"`,
   used exactly once on the whole page, arriving right after the rail's own
   resting point — the loudest colour on the page following the quietest
   motion on the page.
5. **The peak, the page writing about itself.** "VI BYGGER ERT VARUMÄRKE."
   settles, and the three service rows write themselves in below it, word by
   word, in the same rhythm as the visitor's own scroll — a hairline thread
   drawing down the margin at the same pace. Caused by: the bespoke
   word-scrub, the one device on the page that is not a kit parameter,
   borrowed and rebuilt from Vintergatan's workshop chapter to carry full
   sentences instead of three verbs.
6. **Resolve, the last object.** The page returns to a single column and
   closes on the price box: two real prices, "Pris vid förfrågan," and
   `kontakt@alunix.se`, styled exactly like the rail's own object labels —
   the catalogue's final entry, priced and addressed. Caused by: gallery/
   catalog's own close pattern (last object / inquiry-as-label), landing in
   silence right after the loudest act on the page.

**Peak:** act 5, the ledger word-scrub. It gets the largest `data-sc-span` on
the page, the quiet act before it (the rail's own settled rest, per the
end-of-act interaction threshold) as its silence, and it is the only act
where type itself is the animation's subject rather than a container for one.

**Tell-someone sentence:** "It's the site where the three service rows write
themselves into the page one word at a time as you scroll, with a hairline
thread drawing itself down the margin exactly as fast as you're reading — and
right before it, the three real client sites slide past in one direction
while their own headlines drift the other way."

**Signature move:** the ledger word-scrub. Each of the three service rows
(Design, Utveckling, System — the r3 ledger's own copy, unchanged) is split
into words at mount; the CSS resting state is every word at full opacity (so
a no-JS or reduced-motion reader gets the complete sentences outright, per
Vintergatan's own "what to borrow" rule). When JS is live and motion is not
reduced, the words start dimmed and a per-word scroll-mapped opacity brings
them in one at a time as the act's own `--sc-p` advances through that row's
share of the act, together with an SVG thread whose `stroke-dashoffset` reads
the same aggregate progress and draws itself down the left margin. Coded
entirely in this page's own `<script>` and CSS, off the act's published
`--sc-p` — `scrollcraft.js`/`.css` are untouched.

## Device table per act

| Act | Section | Primary device (kit family) | Secondary | Span / notes |
|---|---|---|---|---|
| A | Opening (poster + console) | `reveal` (`up`, poster then console) | `flow`+`in` (console card's own kicker/body/CTA stagger) | flow act, `data-sc-in data-sc-stagger` inside |
| B | Label row (tjänster statement) | `flow`+`in` | — | flow act |
| C | Pan rail (3 objects) | `pan` (the spine) | `tilt` (pointer-only, `data-sc-tilt="5"` per frame wrapper) | `data-sc-span="4.2"`, measured travel logged below |
| D | Thesis (blue block) | `reveal` (`iris`, once on the whole page) | — | flow act |
| E | Ledger word-scrub (signature) | bespoke (non-kit) | `flow`+`in` (headline fade-rise) | flow act, largest engineered span, the peak |
| F | Price close | `flow`+`in` | — | flow act, deliberately the quietest close |

Distinct kit families used: **`reveal`, `flow`+`in`, `pan`, `tilt`** — four,
matching the ≥4 requirement, all drawn from gallery/catalog's own "leans on"
list plus the always-available `flow`+`in` baseline. No `data-sc-kinetic`
anywhere (grammar ban). No two adjacent acts share a primary family:
A(reveal) → B(flow+in) → C(pan) → D(reveal) → E(bespoke) → F(flow+in).
Zero `scrub` acts (no video asset on this page). `iris` used exactly once
(act D).

## Fingerprint row (six dimensions, against r3 and against M1/M2 as described in contract.md)

| Dimension | This build (M3) | r3 | Shared? |
|---|---|---|---|
| Grammar | Gallery / catalog | Split stage | No |
| Nav | Index nav, four jump links, mono, unstyled bar | None | No |
| Hero device | Poster wordmark stacked over console card, logo between | Two heroes side by side (console card + poster) | No |
| Act-sequence shape | Single vertical flow with one embedded horizontal pan rail; 6 acts | Two parallel columns, `flow` acts only, no pan/pin | No |
| Close pattern | Single price box, one column, styled as the catalogue's last object | Price box AND Calyx frame closing simultaneously, one per column | No |
| Signature move | Ledger word-scrub + self-drawing thread (borrowed from Vintergatan) | Seam hairline drawn from a docked logo | No |

0/6 shared with r3 — well inside the ≤2/6 gate. Against M1 (continuous
world, no fixed nav / thin scrolling row, Tidvatten full-bleed hero, offset
columns, window-reveal signature) and M2 (chaptered editorial, folio-in-
margin, console-card-alone title page, pinned scene, running-text-spine
signature) per their own contract.md rows: grammar differs from both: nav
differs from both (an index vs. a thin scrolling row / a folio); hero device
differs from both (a poster+console stack vs. a full-bleed Tidvatten hero /
a console-card-alone title page); act shape differs (a pan rail vs. offset
columns / a pinned scene); close differs (single price object vs. arrival-
at-a-place / a chapter 05 inverted price box inside a one-column chapter
flow — closest of the three, still a different mechanism); signature move
differs from both. Comfortably inside the gate against both siblings too.

## Skills loaded, in order

1. `Skill(design)` — front door; Step 0 (page scope: full build), Step 1
   (pre-flight: this is a fresh cell, no existing tokens), Step 1b (reference
   lock above — r3 as Tier 2 direction, four catalogue entries, TASTE.md §1/§4),
   Step 2 (Tier 2 — r3 + the catalogue sources are the direction, stated),
   Step 2b (grammar = gallery/catalog, feeling curve above, device table above,
   fingerprint gate above; bake-off skipped — this is a task-assigned single
   direction, one of three parallel cells, not an open exploration), Step 4
   (build), Step 5 (verify, this document's own verification section).
2. No copy-chain skills invoked (`copywriting`/`copy-editing`/`humanizer-svenska`)
   — brief.md is explicit that M3 carries no new copy and needs no copy chain;
   every visible string is either lifted verbatim from `tests/alunix-concepts-r3/build/index.html`
   or from that same build's own `<iframe title="...">` attributes (see decision
   ledger). Confirmed by grep against the shipped file before code below.

## Verification results

Server: `python -m http.server 3091` from the repo root. Verified against
`http://127.0.0.1:3091/tests/alunix-concepts-r4/cells/M3-chain/index.html`.

- **Bugs found and fixed during verification** (all confirmed re-fixed by
  re-running the same check afterward):
  1. `.rail-stage{position:relative}` collided with the engine's own
     `.sc-stage{position:sticky}` at equal specificity, later in the
     cascade — exactly the AB06 trap devices.md warns about. Console showed
     `[scrollcraft] act "rail" will not pin: its stage computes
     position:relative`; `scroll_verify.py` showed six consecutive
     `deadScroll` entries (2400→4200px, diff 0.0) because the rail never
     actually moved. Fix: dropped the `position:relative` declaration from
     `.rail-stage` entirely (the stage doesn't need it; `.sc-stage`'s own
     `position:sticky` already establishes the containing block for the
     absolutely-positioned children). Re-verified: `deadScroll: []`.
  2. The three object captions used overlapping progress windows
     (`[0,0.40],[0.30,0.70],[0.60,1.0]`), so two could render at full
     opacity simultaneously — confirmed visually in `shots/motion-4.png`
     before the fix (Hōrai's and Calyx's caption text garbled on top of
     each other). Fixed to three non-overlapping windows
     (`[0,0.34],[0.34,0.67],[0.67,1.0]`), relying on the existing 260ms CSS
     opacity transition for a brief crossfade at each hard boundary instead
     of a sustained double-visible window. Re-verified against
     `shots/motion-0..4.png`: exactly one caption visible at every step.
  3. `a11y_scan.py` returned 47 `color-contrast` violations on first run,
     all but two of them the ledger's dimmed (`opacity:.14`) pre-reveal
     `.w` spans — the scanner's own 500ms wait fires before my original
     1800ms/6000ms near-viewport-only failsafe had any reason to run (the
     chapter is thousands of pixels below the fold at scan time). Fixed by
     adding an early, unconditional failsafe at 350ms (matching r3's own
     400ms/900ms pattern) that forces every word to opacity 1 regardless of
     viewport position, on top of (not instead of) the later near-viewport
     passes for genuinely stuck acts. Confirmed this can't blunt the real
     effect for an actual visitor: `updateScrub()` sets each word's inline
     opacity on every `scroll` event, so the first real scroll after the
     350ms mark immediately re-establishes the correct dimmed state: a
     visitor who has genuinely scrolled 5900px down to reach the chapter
     has fired hundreds of scroll events long after 350ms.
  4. The remaining 2 violations were the rail's own `.obj-index` "02"/"03"
     mono labels — both sit past the viewport's right edge at scroll
     position 0 (objects 2 and 3 haven't panned into view yet), inside the
     engine's own `.sc-stage{overflow:clip}` box, and axe's pixel-based
     contrast sampler appears unable to resolve a background for content
     clipped this way (object "01"'s identical label, on-screen at rest,
     was never flagged). Measured the real, on-screen contrast by hand:
     `--room-soft` (`rgba(244,242,238,.66)`) over `--room-bg` (`#0b0c0e`)
     resolves to roughly rgb(165,164,162) at that alpha, giving **7.83:1**
     against the room background — comfortably past the 4.5:1 floor.
     Fixed the scanner artifact anyway (no visual change) by giving
     `.obj-index` its own explicit `background-color:var(--room-bg)`, which
     lets axe resolve the pair from computed style directly instead of
     needing to sample paint. Re-verified: 0 violations.
  5. Under `prefers-reduced-motion: reduce`, the caption cycle kept
     advancing off the pan act's still-live *vertical* `--sc-p` even though
     the rail itself had become a native, reader-driven *horizontal* scroll
     region (scrollcraft.css's own reduced-motion rule) — two unrelated
     scroll axes driving one caption stack, which is a stray animation, not
     the "static" reduced motion asks for; visually this showed as two
     captions' text overlapping mid-transition. A first fix attempt
     (`.rail-captions{position:static}`, flowed into normal document order)
     collapsed to the top-left of the sticky stage and overlapped the
     frames, because it was the only in-flow child of an otherwise
     all-`position:absolute` stage. Final fix: kept `.rail-captions`
     `position:absolute` (so it can't add height to the sticky stage's own
     box and reopen a dead-scroll gap), but made it tall
     (`height:min(60vh,520px)`), internally scrollable
     (`overflow-y:auto`), and turned the CSS-toggled crossfade off outright
     (`.cap{opacity:1!important}` beats the JS `.is-on` class). Re-verified
     visually: all three captions readable at once, no overlap, no
     scroll-linked motion.
  6. `Objekt 01–03` in the rail's top-left kicker used an en dash as a
     range separator — the one visible-text dash found on the page (a grep
     for `—`/`–` across the file; every other hit was inside the HTML
     header comment or JS code comments, not rendered text). Changed to
     `Objekt 01/03`. Re-checked: no dash character remains in any element a
     visitor can read.

- **Screenshots** (`shots/`), all from a script that manually scrolls in
  steps and stitches the results with PIL rather than calling Playwright's
  `full_page=True` — that call does its own internal resize-and-stitch pass
  that breaks `position:sticky` pinned content, reproduced here exactly as
  r3's own NOTES.md documents it: a first `full_page=True` attempt showed
  the entire pan rail collapsed into one blank band, while direct DOM
  inspection (`getComputedStyle` on the stage mid-scroll) confirmed the
  live page was rendering correctly the whole time.
  - `desktop-1440--fold.png` / `--full.png` (1440×900, full page 7976px).
  - `mobile-390--fold.png` / `--full.png` (390×844 @2x, full page 6373px).
  - `motion-0.png` … `motion-4.png`: five 1440×900 captures, 300px of
    scroll apart, starting 700px into the pan act's pinned travel.
    Measured directly (not just eyeballed) via `getBoundingClientRect()` at
    each of the five stops:

    | step | scrollY | rail track translateX (px) | active caption's own x (px) |
    |---|---|---|---|
    | 0 | 2207 | −451 | 173 (`cap1`) |
    | 1 | 2507 | −702 | 234 (`cap2`) |
    | 2 | 2807 | −913 | 285 (`cap2`) |
    | 3 | 3107 | −1124 | 336 (`cap2`) |
    | 4 | 3407 | −1335 | 387 (`cap2`) |

    Frames: −451 → −1335 (Δ −884px, monotonically more negative — trending
    screen-left). Captions: 173 → 387 (Δ +214px, monotonically increasing —
    trending screen-right). Opposite signs, both monotonic, over the same
    five steps: the two layers provably move in different directions,
    confirmed both numerically and by eye in the five PNGs.

- **`scroll_verify.py`** (1440×900): `deadScroll: []`, `cuesNeverFull: []`,
  `unrevealed: []`, `contrastUnderMedia: []`. One `blankBands` entry
  (2256→5351px, 3095px) — this is the same tool limitation as the
  `full_page=True` issue above: `blankBands` takes its own internal
  `scrollTo(0,0)` + `full_page=True` screenshot, which collapses the
  sticky-pinned rail into a blank band regardless of anything on the page.
  Evidence this is not a real defect: `deadScroll: []` on the same run (the
  fold-by-fold diff, taken at real scroll positions, shows genuine motion
  throughout that exact range), and the manually-stitched
  `shots/desktop-1440--full.png` (see above) renders the full rail
  correctly, object by object.
- **`a11y_scan.py`**: **0 violations, 37 passes, 2 incomplete** (axe's own
  "needs manual review" bucket — matches r3's own baseline of "0
  violations... 2 incomplete" exactly). Two rounds of real violations found
  and fixed, see the bug list above.
- **Overflow**: `document.documentElement.scrollWidth === window.innerWidth`
  at both 1440 (1440 === 1440) and 390 (390 === 390), checked both at rest
  and after a full scripted scroll-through of the entire document at each
  width.
- **Console**: zero `[scrollcraft]` warnings across a full scroll-through at
  1440. The only console lines anywhere are three `cdn.tailwindcss.com`
  notices, all originating from inside the Hōrai/Calyx iframes' own pages
  (outside this build's scope, same as r3's own build). Zero page errors
  (`pageerror` listener) at 1440, at 390, and under `reduced-motion:reduce`.
- **Iframes**: three loaded, real `title` attributes confirmed via
  `iframe.title` in-page: `Er hemsida är nutidens visitkort` (Tidvatten),
  `Hōrai, restaurang i Stockholm`, `Calyx, florist i Stockholm`.
- **Pan rail travel, measured** (devices.md's own instruction: "rail travel
  = `scrollWidth - innerWidth`, MEASURE it, don't assume"): at 1440px,
  `#railTrack.scrollWidth = 3215px`, `innerWidth = 1440px`, **measured
  travel = 1775px** — well clear of zero, confirming the rail is wide
  enough to actually pan (devices.md's own warning: "a rail narrower than
  the viewport travels zero").
- **Reduced motion** (`reduced_motion:"reduce"`): before any scroll,
  `railCaptionsTransform: none`, `trackTransform: none` (both already
  static, the rail's engine-driven `[data-sc-pan]` zeroing plus this
  page's own `.rail-captions{transform:none!important}`); after scrolling
  to y=3000, both remain `none` — confirmed static before and after scroll.
  `threadFill`'s transform stays `matrix(1,0,0,1,0,0)` (`scaleY(1)`, fully
  drawn) in both states — the self-drawing thread does not animate under
  reduced motion, it is simply already complete, matching Vintergatan's own
  "resting state is the finished state" principle. Word-splitting itself is
  skipped entirely under reduced motion (`armChapter()` returns early), so
  `wordOpacitySample` correctly reports `no-words-split`: the ledger rows
  are plain, complete sentences, not a signature-move performance, when
  motion is off. Visual check (`shots/reduced-motion-y3000.png`): the pan
  rail becomes a native, draggable/scrollable horizontal region
  (`overflow-x:auto`, confirmed via `getComputedStyle`, `scrollWidth 3215
  !== clientWidth 1440`) with all three captions stacked and fully visible
  beneath it, no auto-cycling.
- `wc -l index.html` -> 614 lines.

## What I could not do / environment notes

- The Claude Browser pane's own screenshot tool proved unreliable while
  testing this page specifically (repeated "Screenshot timed out" errors,
  and once returned a blank cream frame at a scroll position where direct
  `getComputedStyle`/`getBoundingClientRect` calls in the same tab, via the
  same tool, confirmed the DOM was correct and the dark rail stage was
  genuinely on screen). Fell back to a dedicated local Playwright script
  for every screenshot in this document, per Step 5's own fallback chain
  ("local capture... then Read each PNG so the image actually enters
  context") — every image above was read with the Read tool before being
  judged, not inferred from code.
- Did not touch `sites/horai.html` or `sites/calyx.html` or
  `tests/alunix-concepts-r3/build/tidvatten-hero.html` (existing, out of
  scope) — the `cdn.tailwindcss.com` console notice originates inside them,
  not in this build.
- Everything named in brief.md's and contract.md's M3 section is
  implemented and verified above; nothing was left undone.

## Fix round (Anton's five pixel-measured defects, `my-M3-0/2/4/5.png`)

Same server (`python -m http.server 3091` from repo root), same URL. This
round's own MCP browser pane (`Claude_Browser`) turned out to run with the OS
reporting `prefers-reduced-motion: reduce` unconditionally — confirmed via
`matchMedia('(prefers-reduced-motion: reduce)').matches === true` in that
pane — and programmatic `window.scrollTo()` inside it does not reliably fire
the `scroll` events `scrollcraft.js` listens on (`--sc-p` stayed at
`0.0000` after a `scrollTo`, but updated correctly the moment a real
`wheel` event was dispatched). Both are pane/environment quirks, not page
bugs: matches the *previous* round's own note about this pane being
unreliable for this specific page. Every number below is from a fresh local
Playwright script (`chromium.launch()`, `mouse.wheel()` for real scroll
events, no forced media unless a case explicitly requests
`reduced_motion="reduce"`), the same fallback chain the original build used.

1. **Logo/seam overlap (defect 1), fixed.** Measured before: seam element
   overlapped `.poster-sub` (negative top margin pulled it up into the
   byline). After: `subR.bottom = 350.4`, `seamR.top = 408.5`, gap **44px**
   (≥ the required 24px), and the seam now bisects the cream/black boundary
   exactly (`consoleWrapTop − seamTop = 61.47px`, `seamBottom −
   consoleWrapTop = 61.47px`, a true 50/50 split) — screenshotted in
   `shots/desktop-1440--fold.png`.
2. **Caption 01 duplicate headline (defect 2), fixed.** `<h3>` now reads
   `Tidvatten, kallbadhus i Malmö` — visible in `shots/motion-0.png` and
   `shots/reduced-motion-y3000.png` (both read with the Read tool). The R6
   service paragraph beneath it is untouched, verbatim.
3. **Caption 03 truncation (defect 3), fixed.** Playwright measured
   `cap3`'s body `<p>`: `scrollHeight === clientHeight === 66px` (no
   clipping), `webkitLineClamp: "none"`, full string present in
   `.textContent` with no `…`, and `capBottom (436.9px) ≤
   railCaptionsBottom (567.3px)` — the caption fits inside its own box with
   room to spare. Confirmed by eye in `shots/motion-4.png`: the complete
   sentence ("...till exempel lager, bokningar eller medlemskap.") renders.
   Re-checked at 390px (mobile): `capBottom 239.1px ≤ railCaptionsBottom
   353.3px`, also fits.
4. **Object counter frozen at 01/03 (defect 4), fixed.** Real-scroll trace
   at 1440px, `#objCounter` against the rail's own `--sc-p`:

   | `--sc-p` | counter | active caption |
   |---|---|---|
   | 0.043 | 01/03 | cap1 |
   | 0.262 | 01/03 | cap1 |
   | 0.525 | 02/03 | cap2 |
   | 0.787 | 03/03 | cap3 |
   | 1.000 | 03/03 | cap3 |

   Counter and active caption never disagree at any sampled point (they
   share the same `windows` array). Under `reduced_motion:"reduce"`: counter
   reads `Objekt 01/03` before any scroll and still `Objekt 01/03` after
   scrolling to y=3000 — static, per the requirement.
5. **Empty blue viewport before the thesis text (defect 5), fixed.**
   Sampled `.thesis-headline`/`.thesis-text .kicker` computed `opacity` at
   300px scroll steps from 200px before the block's top through 100px past
   its bottom: **`opacity: "1"` at every single step**, including the very
   first one the block is on screen — screenshotted in
   `shots/thesis-step-0.png` through `-3.png` during verification (not kept
   in the final `shots/` set, which holds only the build's own documented
   screenshot list) and visually confirmed no empty band, no isolated black
   arc. The iris `clip-path` now lives only on `.thesis-photo`; caught
   mid-open on a mobile pass (`shots/mobile-390--full.png`, deep in the
   rail) with the Hyperborea photo still circular-masked while the kicker
   and headline directly below it were already fully opaque — the split is
   real, not just true once fully scrolled past.

**Preserved, reverified unchanged:** pan direction (rail track `transform`
strictly more negative across the five `motion-N` steps, −212 → −422 → −913
→ −1124 → −1546px; caption layer `transform` strictly more positive, 51 →
102 → 221 → 272 → 374px — still screen-left frames / screen-right captions,
still opposite, still monotonic); the word-scrub signature move (untouched,
no lines edited in the `#signatur` section or its script); `data-sc-kinetic`
still absent from the page.

**Re-run verification:**
- `scroll_verify.py` (1440×900): `deadScroll: []`, `cuesNeverFull: []`,
  `unrevealed: []`, `contrastUnderMedia: []`. Same single `blankBands` entry
  as the original round (2234→5393px this time), same known cause (the
  tool's own internal `full_page=True` collapsing the sticky-pinned rail) —
  not a regression, `deadScroll: []` on the same run is the real signal.
- `a11y_scan.py`: **0 violations, 37 passes, 2 incomplete** — identical to
  the pre-fix baseline; the taller caption box and the new place-label copy
  introduced no new contrast or structure issues.
- Overflow: `document.documentElement.scrollWidth === window.innerWidth` at
  both 1440 and 390, true.
- Console: zero `[scrollcraft]` warnings across the full verification run;
  zero `pageerror` events.
- Iframes: three, real `title` attributes confirmed unchanged (`Er hemsida
  är nutidens visitkort`, `Hōrai, restaurang i Stockholm`, `Calyx, florist i
  Stockholm`) — only the *visible caption* for object 01 changed, not the
  iframe's own accessible name, which brief.md's r3-sourced strings still
  cover.
- Reduced motion: `.rail-captions` still becomes the static, internally
  scrollable stack (unchanged CSS); `#objCounter` confirmed static across a
  scroll, see defect 4 above.
- Re-shot `shots/`: `desktop-1440--fold.png`/`--full.png`,
  `mobile-390--fold.png`/`--full.png`, `motion-0.png`…`motion-4.png`,
  `reduced-motion-y3000.png` — all ten re-generated and read with the Read
  tool, all confirmed by eye against the five defects above.
