# Critic pass -- Alunix r7, Arm B, K2 Affischen v2

Reviewed: `tests/alunix-ab-r7/runs/B/K2/index.html`, served at
`http://127.0.0.1:3202/tests/alunix-ab-r7/runs/B/K2/index.html`. Read: `concepts.md` par K2
Affischen v2, `runs/B/K2/BRIEF.md`, `runs/B/K2/NOTES.md` (all five rounds), `design-catalogue/
TASTE.md`, `design-catalogue/FEEDBACK.md` (F-001 through F-005 binding on this page),
`~/.agents/skills/design/references/house-physics.md`, `production-tells.md`, `gates.md`, and
the r6 `runs/B/K2/index.html` plus its `NOTES.md` for the fingerprint comparison. Reference
locks inspected directly: `design-catalogue/entries/springsummer/fold.webp` and
`entries/indoek/fold.webp`.

Own captures: Playwright, 1440x900 and 390x844, both `no-preference` and `reduce` motion, 14
scroll fractions each (0-100%) plus all four `?preview=` hooks -- 72 screenshots total, all
read. Also read the orchestrator's `review/B-K2/grid-dense.png` and `grid-motion.png`, plus
targeted crops of the mask/collision regions and direct DOM/CSS-variable reads
(`getBoundingClientRect`, computed `--open`/`--l1`/`--l2`, canvas-rasterized contrast) to
confirm three of the findings below mechanically rather than by eye alone. Console was clean in
all four capture runs (only the expected `cdn.tailwindcss.com` dev warning, no page errors). No
horizontal overflow at 320/375/390/414/768/899/900/1440px.

## Summary

The core idea -- a photo genuinely masked into the ink of A, U and X, cycling Calyx to Hoerai
to Hyperborea while the wordmark itself never moves or fades, then the crushed block splitting
open in place to seed the next headline -- is real, well-built, and a decisive improvement over
r6's crude overlapping photo panel. But the build ships with two confirmed, reproducible bugs
in exactly the states this review was asked to check (`?preview=open` under reduced motion, and
`?preview=open` at mobile width), a letterform (X) whose mask genuinely breaks the "authority is
the type" claim, and the page's entire signature interaction is absent below 900px in both
motion modes, not only under reduced motion. It clearly beats r6. It does not clearly beat
Spring/Summer and Indoek as delivered -- it is close on desktop rest-states and ahead of Indoek
on masking precision, but the X-glyph failure and the mobile gap are exactly the kind of thing
neither reference ships with.

## Findings, severity-ranked

### 1 -- Blocking. `?preview=open` (and by construction `horai`/`hyperborea`) is broken under reduced motion
**Screenshots:** `1440-rm-preview-open.png`, `390-rm-preview-open.png` (reviewer's scratch
capture set, reproducible from the URL above with `reduced_motion: reduce`).
**What's wrong:** `apply(1)` correctly separates the rows (`--open:1.0000`, confirmed via
`getBoundingClientRect`: row1 bottom 351px, row2 top 539px -- a real 187px gap opens) and
correctly computes `--l1:1.0000`/`--l2:1.0000` on `#block`. But the CSS that is supposed to
reveal the heading lines is gated `.js:not(.rm) #block .headingWrap .hline:nth-child(n){
opacity:var(--l1|--l2,0) }` -- under `.rm` this selector never matches, so the unconditional
fallback `#block .headingWrap .hline{ opacity:0 }` (index.html line 170) wins and the heading
never appears. The result is a large, unexplained blank gap between ALU and NIX with no content
in it -- confirmed via computed style: `hline0`/`hline1` opacity both read `0` while
`--l1`/`--l2` read `1.0000` in the same DOM snapshot.
**Rule broken:** BRIEF.md par 10, the `?preview=`-plan itself: `?preview=open` must force "Hero
vid p=1: blocket fullt oeppnat... 'VI BYGGER ERT VARUMARKE.' som rubrik." It doesn't, under
reduced motion. This is also exactly the debug hook this task was asked to verify in both
motion modes -- it fails the check it exists to support.
**Fix:** drop the `:not(.rm)` qualifier from the two `.hline:nth-child` rules (or add an
equivalent `.rm` rule reading the same custom properties) so `--l1`/`--l2` drive opacity
regardless of the `.rm` class.

### 2 -- Blocking. `?preview=open` collides the wordmark into the desk photo at mobile width
**Screenshots:** `390-motion-preview-open.png`, `open-390-top.png` (crop), `390-rm-preview-open.png`
(same collision plus finding #1 stacked on top).
**What's wrong:** below 899px the composition switches to a single stacked column with the
plate reordered above the block (`.composition .plate{order:-1}`), but `.row-a{transform:
translateY(calc(var(--open,0)*-14vh))}` still fires unconditionally. Forcing `--open:1` pushes
ALU up by 14vh (roughly 118px at 844 tall) directly into the desk photo sitting above it,
partially covering the photo's own credit caption. This is a genuine occlusion, not a
transitional frame a real scrolling user would ever pass through cleanly -- it is the formed,
supposedly-final state.
**Rule broken:** concepts.md K2 v2 Foerbjudet ("foto under ordmarket" is banned specifically to
keep photo and type from fighting); TASTE.md par 1 (when type is the authority the photo must
stay "tyst: liten, bredvid, eller bakom typen," never overlapping it messily).
**Fix:** gate the `--open`-driven row transforms behind the same 900px boundary that already
disables the pin device, so a forced/preview `--open` value has no effect on the stacked mobile
layout.

### 3 -- High. The X-glyph's mask swallows almost the whole letterform
**Screenshots:** `x-rest-zoom.png` (crop of the rest-state hero, Calyx content), `x-zoom.png`
(crop of `?preview=hyperborea`) -- both derived from the reviewer's own captures at
`1440-motion-scroll-00-0pct.png` and `1440-motion-preview-hyperborea.png`.
**What's wrong:** `buildWindows()` doubles the mask polygons specifically for X (`ch === 'X' ?
r.polyRows.concat(r.polyCols) : r.polyRows`), opening all four triangular counters of the glyph
at once. Because X has no true closed counter -- only thin diagonal strokes -- this leaves just
a faint black cross floating over what is effectively a full photo panel. Compare A and U in the
same row: both keep solid, unambiguous ink around a modest window and read cleanly as letters at
every distance tested. X does not; at a glance it reads as a photo with a hairline X drawn over
it, not a bold letterform with a window cut into it.
**Rule broken:** the lane sentence itself ("authority = the type... an enda tung grotesk i
affischskala") and TASTE.md par 1 (one authority per screen -- inside the X, the photo is at
least as loud as the ink, which is the exact "two authorities" failure F-003 already named once
on this page for a different reason).
**Fix:** scope X's mask to one axis (e.g. `polyRows` only, matching A/U's treatment) or
hand-tune the counter selection so enough solid ink remains for the glyph to hold its weight.

### 4 -- High. The signature interaction is absent below 900px in both motion modes, not only reduced motion
**Screenshots:** `390-motion-scroll-00-0pct.png` through `390-motion-scroll-03-23pct.png`
(closed wordmark, immediately followed by an already-open second wordmark, with zero
interactive transition between them).
**What's wrong:** `narrowMQ.matches` (`max-width:899px`) strips `data-sc-act`/`data-sc-span`
before `ScrollCraft.mount()` runs, regardless of `prefers-reduced-motion`. This is a
reasonable, disclosed fix for a real layout collision (NOTES.md "Bugg 2"), but its effect is
that every phone visitor -- motion enabled or not, which is most real traffic to a page like
this -- gets the exact same collapsed, two-static-wordmarks-in-a-row fallback that reduced-motion
users are supposed to get. The page's stated peak (BRIEF.md par 5: "Peaken: akt 2-3... far mest
scrollutrymme") never happens on a phone.
**Rule broken:** BRIEF.md par 5/7 (the engineered peak), and by extension the lane sentence's
own claim that the mask-glide is the page's authority-carrying move -- it is not present for the
device class most visitors will use.
**Fix:** if the composition genuinely cannot fit a pinned 100vh act on a phone, that is a fair
constraint, but it should be solved by redesigning the mobile act (e.g. a shorter pin, or a
scroll-linked but non-pinned crossfade) rather than by silently reusing the RM fallback for
every narrow viewport -- at minimum this should be a named decision in concepts.md, not a side
effect of a layout bug fix.

### 5 -- Medium. Nav clock is not centered as the concept specifies
**Screenshot:** any 1440 frame, e.g. `1440-motion-scroll-00-0pct.png` (clock at x roughly 1173,
mail at x roughly 1338, both hugging the right edge of a 1440-wide bar whose center is x=720).
**What's wrong:** concepts.md's "Foersta skarmen" is explicit: "en liten SVG-logga + ordmarke...
vanster, riktig klocka HH:MM:SS Stockholm som text i mitten, kontakt@alunix.se hoeger." The
actual `.bar .wrap` is a single flex row with only `.mark{margin-right:auto}` pushing the logo
left; clock and mail simply sit adjacent at the right end, no true three-part split.
**Rule broken:** concepts.md's own explicit nav layout instruction for this build.
**Fix:** give `.bar .wrap` a real three-zone layout (e.g. clock at `position:absolute;
left:50%; transform:translateX(-50%)`, or a three-column grid) so the clock actually sits at
the bar's center.

### 6 -- Medium. Mobile authority order is inverted
**Screenshot:** `390-motion-scroll-00-0pct.png`.
**What's wrong:** below 899px, `.composition .plate{order:-1}` puts the desk photo before the
block, so the first thing a phone visitor sees after the description line is the photograph,
not ALU. This technically avoids the letter of "foto under ordmarket" (forbidden) but inverts
the stated authority order just as thoroughly.
**Rule broken:** BRIEF.md par 2 ("ordmarket ALU/NIX... bar hela sidans foersta skarm") and
TASTE.md par 1 (the photo must stay quiet/secondary when type is the authority, not appear
first).
**Fix:** keep the block first in mobile document order too; let the plate follow rather than
lead.

### 7 -- Medium. Zero-tolerance em-dash in the page `<title>`
**Location:** `index.html` line 6 -- `<title>Alunix -- Er hemsida ar nutidens visitkort</title>`
(rendered with a real em dash character, not the double-hyphen shown here).
**What's wrong:** this is the only em dash in delivered, visitor-facing content on the page
(everything else with an em dash is inside `/* CSS */` or `<!-- HTML -->` comments, which don't
count). The `<title>` shows in the browser tab, bookmarks, search results and share cards, so it
is copy.
**Rule broken:** production-tells.md gate 75, zero tolerance, no exceptions for titles.
**Fix:** `Alunix: Er hemsida ar nutidens visitkort`, or split into two sentences.

### 8 -- Low. Small, measured clip on the wordmark's own top edge at the formed state
**Screenshot:** `open-top-crop.png` (crop of `1440-motion-preview-open.png`).
**What's wrong:** at `?preview=open`, `#row1` (ALU)'s top measures 33.7px while `.stage`'s own
box (which clips via `overflow:clip`) starts at 52px -- about 18px of the "A"/"L"/"U" apexes
are cropped away. Confirmed via `getBoundingClientRect` on both elements at the same paint.
**Rule broken:** none of the numbered gates directly, but it is happening to the one element
that is this page's stated authority, at its own formed/final state -- the state most likely to
be screenshotted for a portfolio or a pitch.
**Fix:** clamp `ROW_A_VH`'s travel (or add a small top padding buffer to `.composition`) so the
row's translated top never crosses the stage's own top edge.

### 9 -- Moderate, disclosed. The reveal heading lands below the house's own scale-contrast floor
**Screenshot:** `1440-motion-preview-open.png`.
**What's wrong:** "VI BYGGER ERT VARUMARKE." resolves to 62.5px (NOTES.md runda 5's own
geometry formula, `finalGapPx / 3`), roughly 3.5x the 17-18px body/reading size. TASTE.md par
2.4 sets the house floor at 5-15x contrast, explicitly banning a 2-3x middle. It is reused
consistently as the site's second display tier (matching `.poster` in Akt D, "Alla har ratt
till bra design.", 30-58px), so it isn't an ad hoc invented size -- but it's still short of the
stated floor, and the builder's own NOTES.md documents the shortfall honestly (target was
"at least 5x", extensive iteration in runda 5 could not reach it without breaking
collision-freedom).
**Fix:** none forced here -- flagging for the orchestrator's judgment call, since going wider
requires either a wider `.block` column or a smaller ALU/NIX, both outside a "no other changes"
scope per the builder's own notes.

### 10 -- Low. Unconfirmed "Stockholm" presented as fact in the nav
**Location:** `.bar .clock` -- `<time id="clock">...</time><span>Stockholm</span>`.
**What's wrong:** BRIEF.md par 12 (open question 3) flags, unresolved at delivery, that no
Alunix fact actually names a city; "Stockholm" is inherited from prior rounds' assumption, not
a confirmed detail.
**Rule broken:** production-tells.md gate 85 licenses a locale label only for "a real physical
venue" -- here it's an unconfirmed guess presented as a running, real-time fact.
**Fix:** get Anton's confirmation before shipping, or use a locale-neutral label if Alunix has
no fixed office.

## What's genuinely good, unprompted by the fix list

The Bevis act (three ledgered spreads, real `<iframe>`s not screenshots-as-content, wipe
reveal, grayscale to color once) is clean, matches the "handel och redaktionellt i samma
rutnat" borrow from Indoek honestly, and has none of gates 79/82's fake-UI or overlay-pill
tells. Tjanster and Paket correctly demote numbers to small kickers next to real headings -- a
direct, confirmed fix of r6's F-003 violation (r6 ran `01`/`02`/`03` in full display grade,
competing with the poster headline on the same screen; r7 does not). Exactly five tokens, no
accent, no cards, no shadows, radius capped at 2px everywhere it appears. Contrast on
`.caps`/`--line-2` against `--paper` measures 4.70:1 (canvas-rasterized, independently
reproduced), clearing AA. Console is clean in all four capture runs. The A/U windows themselves
-- the actual "photo through the ink" idea -- are the strongest thing on the page and a real
technical step up from Indoek's simpler rectangle-behind-outline-type approach.

## Against the reference-lock

**Spring/Summer** (primary reference: crushed affischtyp, femfargstak, typeset clock in nav).
The crushed leading is honestly borrowed (rows genuinely close to touching at rest,
`row-b{margin-top:-2.6vw}`) and the five-token, no-accent discipline holds throughout. It does
not beat Spring/Summer's own execution: the reference's type is rock solid ink edge-to-edge
with no legibility compromise anywhere in the wordmark, and its nav clock actually reads as a
deliberate, centered typographic beat rather than a cluster at the right edge (finding 5).

**Indoek** (borrowed detail: photo masked through the letters' openings). K2 v2's `inkScan()`
technique -- a real canvas alpha-scan of the rendered glyph, not a guessed rectangle -- is more
technically rigorous than Indoek's own simpler photo-rectangle-behind-outline-strokes approach,
and A/U prove it can look better too. But X (finding 3) is a genuine regression against the
standard Indoek itself sets: Indoek's outline letters are consistently thin everywhere, so the
photo-through-void reads as one deliberate voice; here A/U are heavy and legible while X
collapses to almost nothing, which is an internal inconsistency Indoek doesn't have.

**Verdict on "beats the references":** not yet, plainly. On desktop, in the states that work,
it is close and in one respect (mask precision) ahead of Indoek. The X-glyph failure and the
two confirmed `?preview=open` bugs are exactly the category of flaw that would be caught in the
same kind of pixel-by-pixel scrutiny this project already applied to its own locked references,
and the total absence of the signature move on mobile is a gap neither locked reference has to
answer for, since both were captured and judged as desktop-first marketing sites without this
project's own explicit mobile testing requirement.

## Against r6 B-K2

Decisively better. r6's rectangular photo panel sat beside the letters unmasked and crashed
directly into the demo screenshot's own legible copy ("Botanical architecture" overlapped
illegibly by the giant U and X, per r6's `shots/fold-1440.png`); r7's masked windows never do
that. r6 ran service numbers in full poster display grade, a direct F-003 violation the
orchestrator already flagged; r7 fixed it. r7's single continuous pinned composition
(mask-glide, then block opens in place) is also structurally more ambitious than r6's separate
curtain-reveal into a pre-set block. r7 wins on every axis the fingerprint table names.

## Verdict

**Revise.** Findings 1-3 are confirmed, reproducible defects (two of them in the exact
preview/motion-mode combinations this review was asked to check) that should block sign-off on
their own; finding 4 is a scope decision that needs to be named and approved explicitly rather
than inherited from a layout bug fix. Findings 5-7 are small, concrete, and cheap to fix. The
underlying idea and its desktop execution (outside the X glyph) are strong enough that this is
a revise, not a rethink -- the lane sentence and reference-lock are the right call for K2; the
execution needs another pass, not a new direction.
