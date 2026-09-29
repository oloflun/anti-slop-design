fix

## persistence

- **Fail, in part.** V3g has no `BRIEF.md` with a § reference lock and no target image (`concepts.md` has no V3g cell). I read `BYGGSPEC.md` (V3f/V3g build spec: Rutverket, reference Inspo `aspensearch-com`, motion borrowed from `cyphr-studio`), `EFFECTS.md` and `design-catalogue/FEEDBACK.md` F-015–F-022 this run, and used them as the governing spec instead. The fidelity-to-target part of this review is therefore suspended. The usability verdict is not, because the caller named the key tasks and the build and URL were live. The orchestrator may treat the fidelity part as `recapture`.
- **Pass.** I read `index.html` in full (markup, CSS and script) this run. I ran four headless probes on the live URL, each under `browser_lock.py`, one browser at a time, with scrolling driven by Lenis-aware jumps or real mouse wheel. The session restarted mid-run, so the last probe was re-run after the restart. I read every screenshot I judge below.
  - Desktop 1440×900: fold, hero pin, tes, process, picker, a Calyx click, a 100-notch wheel pass through the showcase, a wheel pass back up to the picker, a Hōrai click, Hōrai at 30/62/97 % of the pin, pris, kontakt, a click on "Boka ett möte", the page bottom and a 24-step Tab sequence.
  - 390×844 touch: the same page, a Hōrai tap, a wheel pass through the rows, a tap that misses the links on the contact card, and trigger-position measurement.
- **URL discovery:** I only used the given URL. The iframe sources `/sites/calyx.html` and `/sites/horai.html` come from its own markup. I fetched no guessed sub-pages.
- Probe scripts and screenshots are in the session scratchpad (`d/`, `m/`, `m2/`, `m3/`, `probe_desk.py`, `probe2-4.py`).

## fidelity

No target image exists, so this is a read against BYGGSPEC and EFFECTS, screen by screen, followed by the usability table and the walkthroughs.

**Screen by screen (1440):** the order is hero → tes → process → Exempelcase picker → pinned showcase → pris → kontakt → footer, which matches BYGGSPEC. All protected effects are present and intact: the tes headline rise, the hero card flip, the single showcase pin with crossfade, counter, mint track and loupe, the fade on case switch, and the kontakt card flip at 0.7. I propose no change to any of them. The costs below are usability costs *of* those effects.

**Nielsen's 10**

| # | Heuristic | Verdict | Key finding |
|---|---|---|---|
| 1 | Visibility of system status | caution | The showcase counter and mint track report progress well. Clicking "Boka ett möte" gives no feedback at all, because nothing happens. On mobile, a tapped Hōrai that has not loaded shows a blank white frame. |
| 2 | Match with real world | caution | Prices do not say whether VAT is included, or whether they are one-off or monthly. "System" is vague until the pricing tiers explain it. |
| 3 | User control and freedom | **fail** | Switching case from inside the showcase means wheeling back 110 notches. A tap on the contact card that misses a link flips the card and hides the contact details. |
| 4 | Consistency and standards | **fail** | Two "Boka ett möte" are underlined like links and do nothing. One has no `href`; the other links to `#kontakt`, i.e. itself. |
| 5 | Error prevention | caution | The accidental card flip-back. Keyboard focus can enter the demo sites' links, including a real `mailto` to a fictional florist. |
| 6 | Recognition over recall | caution | There is no navigation, so the page structure has to be remembered. The selected case is marked only by a 4 px mint underline, though the showcase head repeats the case name. |
| 7 | Flexibility and efficiency | **fail** | No shortcuts. The prices start at 14,047 px, which is about 234 wheel notches at `wheelMultiplier 0.6`. |
| 8 | Aesthetic, minimalist | pass | Lean copy with no filler in the paths I walked. |
| 9 | Error recognition and recovery | caution | The blank Hōrai frame has no fallback. A poster image exists but stays `display:none`. |
| 10 | Help and documentation | pass (n/a) | For a marketing page, the process section answers "how does it work". |

**Cognitive walkthroughs**

*T1: a prospective client understands what Alunix does and the price level (1440).*
1. **Fold** (`01-fold`): the H1 "Er hemsida är nutidens visitkort" plus the photo card. The visitor will guess "websites" (Q1 yes). They cannot see who Alunix is or what it sells until the card flips. **Uncertain** for Q4.
2. **Scroll ~33 notches** through the hero pin (`03-hero-end`). The card back says "Digital byrå · Design Utveckling System · Boka ett möte". **Q2 fails**: the CTA looks like a link, but its hit-test lands on `.hero-stage`, it has `href=null` and the cursor stays `auto`. At the same moment the H1 lines are sheared ("visitkort" is clipped at the top).
3. **Process** (`05-process`): seven clear steps. Pass.
4. **Price:** there is no way to jump there. The visitor passes the whole 660 vh showcase first. Price arrives about 234 notches from the top. **Q2 is uncertain** for anyone who wants the price first.
5. **Pris** (`14-pris`, `15-pris-b`): at 900 px tall, 38 900 kr is fully visible while the standard tier's 26 900 kr sits at y ≈ 885, clipped at the fold. The lead tier's label and figure are about 350 px apart. VAT and period are not stated. **Q3 is uncertain**: is it 26 900 incl. VAT, one-off, and what does förvaltning cost?

*T2: choose a case, follow the showcase to the end, scroll back and switch (1440).*
1. **Picker** (`07-picker`): two large buttons with `aria-pressed`, a mint underline on the selected one, and a hover zoom. Q1–Q2 pass.
2. **Click Calyx.** Lenis scrolls 1.8 s to `#showcase` but lands at y 6891, 206 px short of the pin start at 7097 (`08-calyx-start`). The picker is still on screen. Minor, and Q4 passes.
3. **Through the showcase:** 100 wheel notches, about 20 per step. The counter goes 01→05, the track fills, the loupe matches the step (`09-calyx-w030/060/090`). Q4 passes. **Uncertain:** the caption crossfades at 0–30 % of a segment while the site glides over 0–70 %. At `w090` the counter says "05/05 Ett mejl räcker" while the frame still shows testimonials.
4. **Scroll back up:** 110 notches to reach the picker again (`11-back-at-picker`). The state rewinds correctly to 01/05.
5. **Switch to Hōrai:** it lands exactly at the pin start (`12-horai-start`, 01/06). **Q2 fails for switching mid-way**: no switch control exists inside the pin, so the only route is the 110-notch reverse scroll.
6. **Hōrai steps** (`13-horai-30/62/97`) read correctly. At 30 %, the 家 that step 2 describes sits half under Hōrai's own sticky nav inside the frame; the loupe compensates.

*T2 at 390 px mobile.*
1. **Tap Hōrai.** The frame stays blank white for rows 1–2 (`m3/h06`) because Hōrai had not loaded yet (`loaded:false` 3 s after the tap), and `activateCase` never shows `#showcasePosterHorai`.
2. **Rows vs. site: fails Q4.** The Hōrai row triggers are built in the same frame the Hōrai panel appears, while the Calyx rows are still in flow (they are hidden only at +0.3 s). There is no re-measure afterwards. Measured: every Hōrai trigger starts **1,155 px late** (start 6074 against the real position 4919, through 7105 against 5949). While the last Hōrai row is on screen (scrollY 6101), the iframe is still on row 0; it reaches row 5 only at scrollY 7361, after the rows have left (`m3/h20`, `h27`).
3. **Reading window:** the sticky frame is 56 svh (473 of 844 px). A row turns active at `top 70%` (591 px), 70 px below the frame, so the active row's h3 slides under the frame (`m2/w23`: "Varje bild har ett nummer" is hidden while its paragraph reads).
4. **Cropping:** the 1440 site is scaled 0.525 and cropped to its left 52 %. Details the captions point to are out of frame: "pris i högerkant", and the RESERVATIONS button top right that step 6 is about.

*T3: contact Alunix (card in #kontakt, mailto + booking).*
1. **Arrival:** the card auto-flips at 0.7 (`16-kontakt`). The mailto and "Boka ett möte" links are visible. Pass.
2. **Click "Boka ett möte": fails Q4.** `href="#kontakt"`; scrollY stays 15003 → 15003 and only the hash changes (`17-after-boka`). Dead end on the page's primary conversion.
3. **Tap slightly off a link (390): fails Q3.** The back face is one full-size "Vänd kortet" button. A tap at 80/80 % flipped the card back to the photo and made the links `inert` (`m2/k-after-misstap`). The link targets are 17 px tall.
4. **The mailto works,** and it is also in the topline and footer. Mailto-only contact fails silently where no mail client is configured; the address is at least visible as text.

*Keyboard only (1440).* The order is: topline mailto (a good first stop) → Calyx → Hōrai → **5 stops inside the Calyx iframe** (Calyx #, Index, Studio, Commission, `mailto:atelier@calyx.se`) → **2 stops inside the Hōrai iframe** (RESERVATIONS, `https://book.horai.se`) → card "Vänd kortet" → mailto → Boka → footer.
- With Hōrai active, the 5 Calyx stops sit in an `opacity:0` frame, so focus is invisible.
- Activating `#index` and similar links scrolls the embedded page off its scripted anchor.
- The card's first stop, "Vänd kortet", hides the links it sits in front of.
- The iframes have `pointer-events:none` for the mouse but are still reachable by keyboard.

**Drift classification.** The 110-notch switch path, the 234-notch route to price and the mobile desync are defects in how the showcase is *wired*. None of them requires changing a protected effect.

**Low-severity, not in the fixes:**
- Calyx click lands 206 px short of the pin start. Use `showcaseST.start` as the scroll target.
- The hero H1 shears during the card reveal.
- The topline logo does not link to the top.
- The embedded Hōrai nav covers 家 in step 2.

## ceiling

- `aspensearch-com` (BYGGSPEC reference, Inspo): **could not open.** No Inspo tool is available to this reviewer this run, and V3g has no BRIEF § reference lock that names it as locked.
- `cyphr-studio` (motion borrow only): **could not open**, same reason. No verdict.

## material_fixes

1. **HIGH · both "Boka ett möte"** (kontakt `href="#kontakt"`, hero `.card-cta` without `href` under `.card-anchor{pointer-events:none}`) → a real booking URL, or `mailto:kontakt@alunix.se?subject=Boka ett möte` (URL-encoded). Give the hero CTA `pointer-events:auto`. Target: 0 self-links or dead links; a click fires navigation or compose in ≤ 100 ms (H4, H1, T3 step 2).
2. **HIGH · in-pin case switch:** two buttons in `.showcase-head` calling `activateCase(key,{scroll:false})`. This path already keeps pin progress and never refreshes, so the protected mechanism is untouched. Target: switching costs 0 wheel notches at any pin progress 0–1 (today 110) (H3, T2 step 5).
3. **HIGH · mobile Hōrai sync:** build the new case's row triggers after `prevC` is hidden (in the `tl.add(…,0.3)` callback, no global `refresh()`, per F-021), and show `C.poster` until `C.loaded`. Targets: trigger start = real row position ± 4 px (today +1,155 px); iframe scrollY within ± 20 px of `C.y[active]` ≤ 700 ms after each row turns active; 0 blank-frame frames after a tap (H1, H9, T2-mobile).
4. **MEDIUM · topline anchors:** `#process · #exempelcase · #pris · #kontakt` in the empty middle cell (Lenis already has `anchors:true`). Target: price 1 click from any point (today about 234 notches or 14,047 px) (H7, H6, T1 step 4).
5. **MEDIUM · keep the embedded sites out of the Tab order:** `tabindex="-1"` on both iframes plus `inert` on `.showcase-frame-wrap`. Target: 0 Tab stops inside the embedded sites (today 7, 5 of them invisible) (H5, keyboard walkthrough).
6. **MEDIUM · contact card:** remove the full-face `.face-back-hit`, or shrink it to a ≤ 44×44 px corner control placed after the links in Tab order. Make the link rows ≥ 44 px tall at 390 (today 17 px). Target: 0 flip-backs from a tap outside the control (H3, T3 step 3).
7. **MEDIUM · pris:**
   - Put the lead figure within 120 px of its label, fully above the fold at 1440×900. Today the gap is about 350 px and the figure sits at y ≈ 885 of 900.
   - Add one identifying line: VAT included or excluded, one-off or not, and the förvaltning price. This passes F-016's test because it differentiates the offer and enables a decision; it is not filler.
   - Target: lead tier label and figure together within the first view of the section (H2, T1 step 5).
8. **MEDIUM · mobile reading window:** a row turns active when its top reaches the frame bottom + 16 px (≈ 537 px at 844, today 591 px). Target: the active step's h3 stays fully visible over ≥ 40 vh of scroll. Optionally show the existing `.showcase-detail` loupe on mobile so cropped details stay visible (T2-mobile steps 3–4).

## keep

Keep the showcase mechanism exactly as EFFECTS.md protects it: one pin, crossfade, counter plus mint track, the loupe per step, and a case switch that keeps pin progress without a refresh. Also keep the topline `mailto` as the first Tab stop, since it is the fastest contact path on the page.
