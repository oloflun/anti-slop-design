# V3g · Opus a11y-granskning (design-a11y-reviewer, Opus, ingen delegering) · 2026-09-28

Sparad av leaden: granskarens roll är skrivskyddad. Innehållet är granskarens rapport ordagrant i
sak, förkortad i form.

**Dom: Block.**

## Kontroll först
`a11y_scan`, `tab_walk`, `reflow` och `contrast.py` fångade sina planterade fel i `tests/a11y/broken.html`.
`contrast_over_media` gick inte att avgöra (fixturen har ingen text över media). `contrast.py` har
fortfarande hårdkodad URL (localhost:3055) och kördes via sed-substitution. `tab_walk` stannar på sin
fällkontroll i Calyx-iframen och ersattes av en egen Tab-promenad. Allt headless via `browser_lock.py`.

## HIGH
1. **Tes (1.3.1/4.1.2):** SplitText `aria:'auto'` sätter `aria-label` på tre `<p>` plus
   footer-märkets `<span>` och `aria-hidden` inuti. Axe rapporterar `aria-prohibited-attr` (serious),
   och ingen av de tre meningarna finns som text i tillgänglighetsträdet.
2. **Showcase-steg dolda för hjälpmedel (1.3.1):** inaktiva steg har `aria-hidden` och
   `visibility:hidden`, så trädet har 1 av 5 (Calyx) och 1 av 6 (Hōrai). Räknaren är också `aria-hidden`.
3. **Dold iframe i tabbordningen (2.4.7/2.4.3):** Hōrai vid opacity 0 har 3 osynliga tabbstopp,
   och efter byte har Calyx 5.
4. **Fokus inne i Calyx (1.4.4/2.4.7):** skrollar ramen 524 px i sidled, och den står kvar förskjuten
   resten av besöket. Ramtexten är 9,9 px vid 100 % zoom och 4,5 CSS-px vid 200 %.
5. **Kontrast i casehuvudet (1.4.3):** bläck på rost 2,95:1, bläck på lack 2,57:1 (golvet för stor
   text är 3:1, bildtexten kräver 4,5:1). Vid inflygningen 1,34:1 mot svart i cirka 90 px scroll.
6. **768 × 432, alltså 200 % zoom (1.4.4/1.4.10):** stegtextens nederkant ligger på 444 och panelens
   nederkant på 432, så texten klipps. Hjulet skrollar inte panelen (ingen `data-lenis-prevent`).
7. **Kontaktkortet (2.4.7):** fokusringen på baksidans knapp klipps av `overflow:hidden`, så 0 px syns.

## MEDIUM / LOW (till skuldboken, kräver Antons kvittens)
- MED 2.5.3: casknapparna heter "Startsidan för Calyx…", medan den synliga etiketten är `aria-hidden`.
- MED 1.4.11: mintringen har 1,48:1 mot vitt, och kortets framsidesring 1,05:1 mot mint.
- MED 2.4.4: "Boka ett möte" på kortet går till `#kontakt`, alltså sektionen den redan står i.
- MED 1.4.10 vid 640 × 360: topplist och ram täcker 250 av 360 px. På mobil är ramen tom vid laddning
  (`scaleShowcaseFrame` körs aldrig på mobil).
- MED 2.4.3: Enter på vändningen skickar fokus till `<body>`.
- LOW: 13,3 % av pinnen ligger under 4,5:1 under övertoningen; mål på 17 px vid 320 px; sidtiteln är
  bara "ALUNIX"; fokus stannar på en knapp utanför skärmen efter casebyte; `<nav>` saknas fortfarande.

## Personas
| Persona | Förstå erbjudandet | Läsa stegen | Byta case | Hitta kontakt |
|---|---|---|---|---|
| Maja, NVDA | friktion | **fallerar** | friktion | fungerar |
| Johan, bara tangentbord | fungerar | friktion | omväg | omväg |
| Eva, 200 % zoom | fungerar | **fallerar** | fungerar | fungerar |
| Ali, en hand, styrplatta | fungerar | friktion (660 vh pin) | fungerar | fungerar |
| Sara, ADHD, mobil | fungerar | friktion | fungerar | friktion |
| Per, 390 px i sol | fungerar | friktion (2,57:1) | fungerar | fungerar |

## Rättningar (mål)
1. `inert` och `aria-hidden` på den iframe som ligger vid opacity 0. Mål: 0 tabbstopp i dold ram.
2. Båda ramarna blir `inert`, med en länk "Öppna Calyx/Hōrai i full storlek" (≥ 24 px). Mål: `scrollLeft` 0.
3. Inaktiva steg döljs bara med opacity 0, inte med `aria-hidden` eller `visibility`. Mål: 5/5 och 6/6
   steg i trädet vid varje progress.
4. `.showcase-head{color:#fff}` ger 5,33:1 och 6,13:1. Grunden ska vara målad innan bildtexten syns.
5. Kortets fokusringar ritas inuti ytan (`outline-offset:-4px` eller `:focus-within`), ≥ 3:1.
6. Efter vändning flyttas fokus till den nya sidans kontroll.
7. SplitText `aria:'hidden'` plus en sr-only-kopia. Mål: 0 noder med `aria-prohibited-attr`.
8. `data-lenis-prevent` på `.showcase-side`, eller ingen pin under 560 px höjd.

## Behåll
Övertoningen som visar exakt ett steg utan överlappande text, sr-only-kopian bakom hero-kortet, och
texten på svart grund (21:1 och 11:1).
