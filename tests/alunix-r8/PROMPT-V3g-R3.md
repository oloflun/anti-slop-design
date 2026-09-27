Du är byggaren för Alunix {{KONCEPT}}, runda 3. Arbetsmapp `{{UT_MAPP}}`, server-port {{PORT}}.
Designkedjan är påslagen. Följ varje hooknekning genom att göra det den kräver.

## Läs först, i den här ordningen
1. `{{UT_MAPP}}/EFFECTS.md`: effekterna Anton godkänt. De får inte ändras och inte bli sämre.
2. `{{UT_MAPP}}/SHOWCASE-SPEC.md` och `{{UT_MAPP}}/RAPPORT.md`: vad runda 1–2 byggde och varför.
3. `design-catalogue/FEEDBACK.md` F-019, F-020, F-021: Antons domar över runda 2.
4. `Skill(design)` med referensgolvet, sedan `~/.agents/skills/design/references/scroll/devices.md`
   § The engine → Load-bearing rules (nya regler 2026-09-25) och `references/motion.md`
   § Approved effects are protected.
5. Skills: `lenis`, `gsap-scrolltrigger`, `gsap-performance`. UI-skill:
   `ibelick/fixing-motion-performance`.

## Uppdraget, fyra delar. Inget annat på sidan ändras.

### 1. Omladdningsloopen (grundorsaken till F-021). Gör först
Iframarna i `#showcase` laddas om vid varje `ScrollTrigger.refresh()`, eftersom pin-spacern
flyttar `.showcase-stage` i DOM:en. Varje `load` ber om en ny refresh. Uppmätt: 9 omladdningar
per iframe och 4 refreshar under en scroll, och tesrubriken tappar hälften av sina bildrutor.
- Lägg en egen wrapper runt `.showcase-stage` i HTML:en, till exempel
  `<div class="showcase-pin-spacer">`, och ge pinnen `pinSpacer: '.showcase-pin-spacer'`.
- Ta bort varje `safeRefresh()`/`refresh()` som körs från en iframes `load`. `measureCase`
  på `load` står kvar.
- Iframarna laddas inte vid `window.load`:
  - Calyx står kvar med `src` i HTML:en, som i V3f.
  - Hōrai monteras via sidans befintliga `mountDue`-princip när `#exempelcase` är inom 2
    viewports, alltså före första möjliga klick men inte under hero och tes.
- Kontroll: `python "C:/Users/Anton L/.agents/skills/design/scripts/section_probe.py" http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --out {{UT_MAPP}}/shots/section-probe-r3.json`.
  - Kravet är varje iframe laddad 1 gång och 0 refreshar under passet.
  - `#tes` ska ha p95 ≤ 33,4 ms, över två körningar.

### 2. Tempot över hela sidan (F-020)
- Lenis: `lerp: 0.075, wheelMultiplier: 0.6`.
- Alla scrubbade triggers på sidan får `scrub: true`, också hero (i dag `scrub: 0.6`) och alla
  andra med numerisk scrub.
- Hero-pinnen (kortvändningen) spänner `+=220%` i stället för `+=120%`, så att kortet syns
  vända sig.
  - Kontrollera kortvändningens tidslinje i pinnen så att vändningen fördelas över den
    längre sträckan och inte är klar efter första hjulsteget.
- Kontroll: `section_probe` rapporterar `px_per_notch` ≈ 60 och inga sektioner sämre än
  V3f-baslinjen.
- Mät också **jämnheten**: `showcase_probe.py --headed --no-shots`, två körningar, genom-p95
  jämfört med runda 2.

### 3. Showcasen: långsammare och mjukare mellan texterna (F-020)
- Segment per steg **110 vh** i stället för 75. Pinnens längd är `6 × 1,1 × innerHeight`,
  fast för båda casen.
- Sajten glider mellan ankarna under de första **70 %** av segmentet med `sine.inOut` och
  står stilla resten.
- Texten tonas över under de första 30 % av segmentet (ut 0–15 %, in 15–30 %) och står
  sedan still.

### 4. Textrutans layout (F-019). Ny layout, samma mekanism
Rubriken får aldrig ta över. Sajten är huvudsaken och texten är bildtexten.
- **Rad 1, överst:** räknaren `03 / 06` och mintspåret, som i dag.
- **Rad 2, flexibel höjd:** en lodrät stegskala, `aria-hidden`.
  - En tunn linje med 5–6 jämnt fördelade streck.
  - En mintmarkör glider längs linjen, kontinuerligt med pinnens progress och inte i steg.
  - Aktuellt streck står i bläck och de andra i 25 %.
  - Inga tal, ingen text. Den här raden bär rutans höjd, i stället för stor text.
- **Rad 3, nederst med luft under:** det aktiva steget. Samma `h3` och `p` som i dag, staplade
  i en gridcell och övertonade som nu.
  - `h3`: 30 px, rad 1,15, vikt 500.
  - `p`: 18 px, rad 1,5, `max-width: 40ch`.
- **Ta bort** den stora skuggsiffran (`03`/`05`) helt.
- Calyx och Hōrai behåller sina ytor (papper respektive svart).
- Kontroll: skärmbilder vid steg 1, 3 och sista för båda casen, 1440×900. Rubriken får inte
  vara högre än 2 rader, och ingen text i rutan får vara större än 32 px.
- Mobil: oförändrad från runda 2 utom tempot.

## Verifiering, i den här ordningen. Bara headless, en webbläsare i taget, stäng alltid
- `section_probe.py` två gånger (krav ovan).
- `showcase_probe.py --headed --no-shots` två gånger, och en gång med bilder på 1440 och 390.
  Läs `sheet.png`.
- Den isolerade `showcase_check` i `verify_motion.py`: alla ankare ±2 px, båda casen.
- `verify.py`: 0 px överflöd, copy-diffen oförändrad mot V3f.
- Skriv en R3-sektion i `RAPPORT.md` med före/efter per del och bildvägar. Skriv också vad
  i EFFECTS.md du kontrollerade inte blev sämre, och hur.

Ingen commit.
