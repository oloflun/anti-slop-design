Alunix {{KONCEPT}}, runda 2. Arbetsmapp `{{UT_MAPP}}`, server-port {{PORT}}.

Leaden har läst dina bilder och kört egna mätningar. Övertoningen vid klick, rutans stegbyte,
mintspåret och sajtens rörelse genom ankarna på desktop fungerar. Rätta nu fyra fel, i den här
ordningen. Inget annat på sidan ändras.

## 1. Casehuvudets rubrik klipps under pinnen (desktop). Blockerande, bryter läsregeln
Medan pinnen är aktiv ligger `.showcase-head`s rubrik (`Hōrai`/`Calyx`, `headline-40`) under
den sticky topplisten (48 px), så att övre halvan av glyferna skärs av.
- Leadens bilder: `{{UT_MAPP}}/shots/lead-headed-1440/through-05.png` till `through-12.png`.
- Felet finns också i V3f och är ärvt.
- Rätta så att hela rubriken och underraden syns under hela pinnen, till exempel med
  `start:'top top+=48'` och scenhöjden `calc(100svh - 48px)`, eller med en topputfyllnad lika
  topplistens höjd. Välj det som inte återskapar V3f:s svarta band under scenen (se kommentaren
  om R6 §3 i CSS:en).
- Kontroll: `getBoundingClientRect().top` för rubriken ≥ topplistens underkant vid pinnens
  början, mitt och slut.

## 2. Mobil: sajten i den sticky ramen följer inte raderna (390). Blockerande
I `{{UT_MAPP}}/shots/probe-r1-390/sheet.png` står Hōrais hero kvar medan alla sex rader
passerar under ramen. Ramens inre scroll ska tweenas till radens ankare (0,6 s) vid radens
`onEnter`/`onEnterBack`, som SHOWCASE-SPEC C säger.
- Trolig orsak: casets `C.y` mäts aldrig på mobil efter ändringen där båda iframes förladdas
  (samma klass av fel som du hittade på desktop).
- Mät om vid aktivering och vid iframe-`load` även på mobil.
- På mobil täcker ramen dessutom casehuvudet (`Hōrai` klipps mot ramens underkant i
  through-02). Huvudet ska stå helt synligt innan raderna börjar passera.
- Kontroll: iframens `scrollY` vid varje rads aktivering ±2 px mot ankaret, båda casen.

## 3. Rutan är mest död svart yta (desktop)
Stegtexten är liten och står långt ned i en hög, tom cell. På Hōrai är nästan hela rutan svart.
Anton har tidigare underkänt "död svart yta" (kontakten, R4).
- Ge texten rutans skala: stegrubriken i rutan cirka 40 px med `.showcase-box .h3`, alltså
  samma steg som `headline-40` men klassen står kvar; brödtexten 18 px med `max-width:44ch`.
- Placera stegen högt i rutan, direkt under räknaren och spåret, med luft ovanför. Inte
  vertikalt centrerat.
- Om det fortfarande blir tomt i rutans nedre del: låt räknarens siffra för aktuellt steg stå
  som ett stort mono-tal i rutans nederkant, `aria-hidden`, samma siffra som räknaren, ingen
  ny copy. Det bär ytan typografiskt, och det ska tonas i takt med stegen.
- Kontroll: skärmbild vid tre steg och båda casen. Rutans tomma vertikala yta ska vara under
  cirka 45 %.

## 4. Calyx sista ankare (`#commission`) ligger 11 px fel
Ta reda på varför, mätt och inte gissat, och rätta till ±2 px. Om orsaken är att Calyx egen
layout ändras efter mätningen: mät om efter `document.fonts.ready` i iframen.

## Verifiering
- `showcase_probe.py`: timing-only-pass med `--no-shots`, sedan ett pass med bilder, på både
  1440 och 390. Timing-siffror från headless räknas inte. Kör headed, en process i taget.
  Kraschar headed, säg det.
- `verify_motion.py` isolerad showcase-kontroll: alla ankare ±2 px, båda casen, båda
  bredderna.
- `verify.py`: 0 px överflöd på alla bredder, copy-diffen oförändrad mot V3f.
- Läs dina bilder. Skriv en R2-sektion i `RAPPORT.md` med före/efter per punkt och bildvägar.

Ingen commit.
