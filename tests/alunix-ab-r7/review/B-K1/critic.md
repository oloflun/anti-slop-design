# Critic pass -- Alunix r7, Arm B, K1 Skymning v2

Reviewed: `tests/alunix-ab-r7/runs/B/K1/index.html`, served at
`http://127.0.0.1:3201/tests/alunix-ab-r7/runs/B/K1/index.html`. Read: `concepts.md` par K1,
`runs/B/K1/BRIEF.md`, `runs/B/K1/NOTES.md`, `design-catalogue/TASTE.md`,
`design-catalogue/FEEDBACK.md` (F-001, F-002, F-010 binding), `house-physics.md`,
`production-tells.md`, `gates.md`. Own captures: Playwright, 1440x900 and 390x844, both
`no-preference` and `reduce`, 18 scroll fractions each (0-100%, dense around the 40-60%
transition zone) plus all four `?preview=` hooks -- 76 screenshots total, all read. Also read
`tests/alunix-ab-r7/review/B-K1/grid-dense3.png` and `grid-dense4.png` (orchestrator's
captures), the raw `assets/push/f0*.webp` frames, `style.css`, `script.js`, and the r6 B-K1
comparison shots.

## Summary

The signature act genuinely fixes F-010 -- Hoerai is masked into the real arched window
opening and tracked frame-by-frame, not pasted over the facade as r6 did. That structural
win is real and verifiable. But the build ships with two confirmed, reproducible defects
that a critic can't wave through: the generated push-in sequence carries visible AI-video
artifacts (garbled signage, a melted lamppost) for a real stretch of the scrub, and the
final act's reveal never completes on any tested viewport -- the page runs out of scroll at
exactly half-open. There is also a self-inflicted token-role violation (a filled accent
badge) that the build's own reference-lock forbids in writing. It does not yet honestly beat
Rogo and Montoni; it partially beats r6, and only on the one axis F-010 asked for.

## Findings, severity-ranked

### 1 -- Blocking. The generated push sequence has visible AI-video artifacts inside the scrub window
**Screenshots:** `push/f040.webp`, `push/f050.webp`, `push/f060.webp` (raw source frames);
visible on-screen in `d-np-008.png` through `d-np-024.png` (frac 8-24%, local `--sc-p`
approx 0.15-0.45, confirmed via direct CSS-var read).
**What's wrong:** frames ~40-60 of the 100-frame Higgsfield/Kling sequence show a purple
banner with illegible gibberish lettering ("MAOKI"/"KAOKIMA" depending on frame), a warped,
unreadable red street sign, and a bizarre glowing melted-lamppost shape in `f040.webp`. These
are not subtle -- they sit in the mid-ground of the shot for roughly a third of total page
scroll, during exactly the "Drag" act the feeling curve calls the setup for the page's one
"toppen" moment (BRIEF par 5).
**Rule broken:** TASTE.md par 1 -- the photo/generated sequence *is* the auktoritet for acts
1-3; an authority that visibly glitches into uncanny-valley signage is not silent, it's the
loudest thing on screen. Rogo and Montoni, the two locked references, never show a warped or
fabricated object; this generated sequence does, for real screen-time.
**Fix:** re-generate or trim the sequence so the frame range with fabricated signage/pedestrians
is replaced or the push distance is redirected before that range becomes readable at full
resolution; QA a generated sequence pixel-by-pixel exactly as a stock photo would be vetted
(TASTE par 4.3's "art direction by render" standard, applied to generated media).

### 2 -- Blocking. The final act's reveal never reaches its finished state -- confirmed on every viewport
**Screenshots:** `m-np-100.png` (390x844, shows roughly 45% of the viewport as flat black
above the night photo); same defect present but less visually loud at `d-np-100.png` (1440x900).
**What's wrong:** direct CSS-variable read at the maximum scrollable position
(`document.documentElement.scrollHeight - window.innerHeight`, i.e. the very bottom of the
page, no more scroll available) shows `#landing`'s own `--sc-p` capped at exactly **0.50** on
*all three* tested viewport geometries (1440x900, 390x844, 1440x700). The iris/inset clip-path
(`inset(calc(50% - min(p,1)*50%) ...)`) is designed to fully open at p=1; at p=0.50 it is
locked at a permanent 25%-top/25%-bottom crop, forever, because the page has no more scroll
distance to give it. This is not a mid-scroll transitional state a user passes through -- it
is the terminal state of the page, unreachable-fixed at half-open.
**Rule broken:** concepts.md par K1 Landning: "nattfotot... oeppnar sig fraan horisonten...
Stilla; inget tonar bort" -- the ending is specified to fully resolve and hold, not stop
halfway. BRIEF par 7's cue contract for act 6 requires the cue to reach and hold at 1 ("Maaste
haalla... saa kontaktraden aldrig tonar bort innan sidan tar slut") -- the underlying
drift/reveal driving the same act's photo never gets there either. This also directly
contradicts NOTES.md round 5's closing claim ("Inga nya avvikelser hittade") -- the round 5
verification checked the `.proof-section` gap and a short-viewport variant of it, but never
scrolled to the literal end of the page to confirm the last act's own animation completes.
**Fix:** the `drift`/reveal math for the last section needs to reach p=1 at the actual
scroll-max, not assume a scroll runway the page (being the final element, per its own device
table) can't supply -- recompute the progress denominator against real available scroll
distance, or drive it off the document reaching scroll-bottom rather than a fixed
section-height assumption.

### 3 -- Major. The 01/02/03 proof-row numeral is a filled accent badge, exactly what the reference-lock forbids in writing
**Screenshots:** `d-np-052.png`, `d-np-084.png`, `d-reduce-048.png`, `d-reduce-064.png` -- the
badge is present and identical in both motion modes, so it's a design decision, not a
scrub artifact.
**What's wrong:** `.proof-row__num` (style.css line 243) sets
`background: color-mix(in oklab, var(--sc-accent) 70%, transparent)` with padding -- a filled
amber rectangle behind the numeral, next to every "Design / Utveckling / System" heading.
**Rule broken:** the build's own BRIEF.md par 3 Role rules state, verbatim: the accent
(fonsterbaernsten) does exactly two things -- the underline under "visitkort", the streak
under the contact address on hover -- never a button fill, never a section background. A
filled background swatch behind a numeral is a third role, not one of the two licensed ones --
this is gate 91 (token-role drift) against a role the build wrote for itself, not even a
borrowed one. It's also concepts.md's own maalbildsgrind, TASTE par 5 troplist: "ingen
badge-rad" is explicitly banned in K1's own gate-check (concepts.md line 100), and this is a
badge row of three. Secondarily, 01/02/03 next to three sequential rows the visitor can
already count is gate 69 territory ("if the user can count, the label is noise").
**Fix:** drop the fill; set the numeral in the accent or accent-ink color as plain text
(matches the kicker microformat the rest of the register-role type already uses), no
background.

### 4 -- Moderate. The window-glass overlay reads as visual noise at the reveal's payoff moment
**Screenshot:** `preview-window.png`.
**What's wrong:** the `.window-glass` canvas (mix-blend multiply grid pattern simulating
reflection/glazing bars) overlays the Hoerai wordmark and food photo with a busy, high-contrast
plaid pattern that competes with, rather than sells, the "that's a real, live site" reveal.
The feeling curve names this exact moment "Overraskning, foertjusning" (BRIEF par 5, the
page's one designated peak); the payoff should read cleanly. Right now the wordmark is
legible only in fragments between grid lines.
**Rule broken:** not a named gate directly, but it undercuts the concept's own stated purpose
for the moment (BRIEF par 6: what looks from a distance like a beautiful photo turns out to
be something real and working -- the reveal needs to read instantly, and this doesn't).
**Fix:** reduce the glass canvas's contrast/opacity or simplify its pattern so it reads as a
faint reflection rather than a competing grid.

### 5 -- Minor / observation. Mid-scrub collision frames are rougher than the bridged crossfades elsewhere
**Screenshot:** `grid-dense4.png` at 44% (orchestrator's capture).
**What's wrong:** at one scrub position, "VARUMAERKE." renders directly on top of the still-
legible Hoerai food photo/wordmark, a jumbled double-exposure moment that's messier than the
carefully-bridged blur crossfades documented elsewhere in `style.css` (the `--xfade1`/
`--xfade2` blur-bridge comments show real craft attention on the window-to-frame and frame-to-
exit transitions; this particular overlap doesn't get the same treatment).
**Rule broken:** house-physics motion bar generally (smooth, coordinated layering); not a hard
gate, since it is a genuinely transitional frame a user scrubs through quickly.
**Fix:** low priority; worth a look if the other two blocking items are being re-touched anyway.

## Things that hold up

- F-010 is genuinely fixed: `?preview=window` and the mid-scrub screenshots show Hoerai masked
  into the real arched window opening, tracked to the window's own arch and size per frame,
  glass layer on top -- categorically different from r6's flat rectangle
  (`tests/alunix-ab-r6/runs/B/K1/shots/desk-zoom-0.7.png`, the exact frame Anton called out).
- Reduced motion (F-001/F-002) is correct: `d-reduce-*.png` show the formed states as their
  own sections in order, no thumbnail of the end state shown early, no jump. This is the one
  area where the build clearly executed the target picture as specified.
- The ledger act, proof-row anatomy, and the one hard cut to white all match TASTE par 1/3
  and the reference lock's Rogo-derived structure -- hairlines, no cards, no shadow,
  alternating image side.
- The accent's other two roles (underline under "visitkort," hover-streak under the mailto)
  are correctly implemented and are the only other accent usage on the page.

## Does it honestly beat the references?

**No, not yet, on the two blocking items.** Rogo and Montoni are real, unglitched photography
with a hard, deliberate register change; K1's own signature material introduces visible
generation artifacts neither reference has, and its own final act fails to resolve on every
viewport tested -- a defect neither reference has either (their pages don't leave the visitor
staring at a permanently half-cropped photo at scroll-max). The structural moves borrowed from
each reference (hard register cut, image-paired proof rows, darkening only at the text edge)
are sound and correctly executed.

**Against r6 B-K1: better on exactly the one dimension it was built to fix (F-010), worse on
robustness.** r6's simpler CSS-transform-on-one-still-image approach couldn't glitch mid-scrub
the way a 100-frame generated sequence can, and nothing in r6's NOTES.md suggests its ending
act failed to complete. r7 v2 traded a simpler, safer implementation for a more ambitious one
and introduced two new failure modes in the process. The trade is worth making only if
findings 1 and 2 get fixed -- as shipped, it is not a clean win over r6, it's a different set
of problems.

## Verdict: revise

Findings 1 and 2 are both concrete, reproducible, and disqualifying for ship: an authority
(the generated photo) that visibly glitches, and a final act that mathematically cannot
finish on the device sizes the brief itself names. Finding 3 is a clean, cheap fix against
the build's own written rule. None of these are direction problems -- the lane sentence,
reference lock, and act structure are right; the execution needs another pass on the
generated asset, the last act's scroll math, and the one badge.
