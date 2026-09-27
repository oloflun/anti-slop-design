Alunix {{KONCEPT}}, runda 4 (kort). Arbetsmapp `{{UT_MAPP}}`, server-port {{PORT}}. Samma regler
som runda 3: bara headless, en webbläsare i taget, EFFECTS.md är skyddad, ingen commit.

Leaden har mätt din runda 3. Loopen är borta, varje iframe laddas 1 gång, alla sektioner ligger på
p95 17–19 ms, och ett hjulsteg ger 60 px. Det är utmärkt och får inte bli sämre. Två saker kvar:

## 1. Klicket är fortfarande hårt i starten
`python tests/alunix-r8/click_scroll_probe.py http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html`
mäter scrollY per bildruta efter klick på Hōrai. Den största enskilda bildrutan flyttar **629 px**
(V3f: 266 px).

Orsaker och rättning:
- `easing: 1 - 2^(-10t)` lägger nästan hela rörelsen i de första bildrutorna. Byt till en
  mjuk in-ut-kurva, till exempel `t < .5 ? 4t³ : 1 - (-2t + 2)³ / 2`, med `duration: 1.8`.
- Allt tungt arbete i klicket, som panelbyte, `measureCase` och tidslinjer, flyttas ut ur
  klickets bildruta med `requestAnimationFrame` eller en kort `gsap.delayedCall`, så att scrollen
  startar i en tom bildruta. Mät vilken del som tar tid innan du flyttar något.
- **Krav:** största enskilda steg ≤ 60 px i två körningar av proben, och sidan ska vara framme
  vid showcasen inom 2 s.

## 2. Stegskalan syns inte
Den lodräta linjen och strecken är nästan osynliga, och Hōrai-rutan läses som tom svart yta.
- Linjen blir 2 px i 35 % bläck, eller på Hōrai `--paper` 35 %.
- Strecken blir 14 px breda.
- Mintmarkören blir 4 × 28 px.
- Aktuellt streck står i full färg och 20 px brett.
- Skalan får en tunn mono-etikett överst: steget som räknare (`03`). Den är `aria-hidden` och
  identisk med räknaren, så ingen ny copy tillkommer. Hellre än så: låt räknaren flytta ned
  och stå vid skalans topp om det blir renare. Välj en av de två och motivera.
- Kontroll: skärmbild steg 3 för båda casen, 1440×900. Läs dem.

## Verifiering
- `click_scroll_probe.py` två gånger.
- `section_probe.py` två gånger, med samma krav som runda 3 och med
  `--baseline {{UT_MAPP}}/shots/lead-section-r3-1.json`.
- En `showcase_probe.py --headed` med bilder på 1440. Läs `sheet.png`.
- En R4-sektion i `RAPPORT.md`.
