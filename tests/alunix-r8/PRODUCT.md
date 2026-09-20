# Product

<!-- impeccable:product-schema 1 -->

Källa: `tests/alunix-ab-r7/PROMPT.md`, avsnitten "Alunix, fakta", "Copy som ska användas
ordagrant" och "Förbjudet, bindande". Ingen annan källa har använts. Står det inte där står
det inte här.

## Platform

web

Belägg: de tre exempelsajterna är `.html`-filer under `/sites/` som serveras live och visas i
`<iframe>` från samma origin.

## Users

Vi vänder oss till verksamheter som behöver en webbplats. Sidan tilltalar dem i andra person,
"er" och "ni", aldrig "jag". De verksamhetstyper vi faktiskt kan visa upp är florist,
restaurang och konferens, eftersom det är vad de tre exempelsajterna är.

Vad de behöver av oss står i rubriken och ingen annanstans: `Er hemsida är nutidens
visitkort`. Vi vet alltså vad sidan lovar dem. Vi vet inte hur de köper, när de köper eller
vad de jämför med. Ingen intervju finns.

Ingen ytterligare målgrupp är bekräftad. Bransch, storlek och köpsituation är öppna frågor,
inte fakta.

## Product Purpose

Alunix är en webbyrå i Sverige. Sidan säljer en tjänst: webbdesign.

Vi skapar skräddarsydda webbplatser. Underraden löd ordagrant: `Vi skapar
skräddarsydda webbplatser som hjälper er att exponera verksamheten.`
**V3d, Antons beslut 2026-09-20: underraden är borttagen helt.** Heron bär på
rubriken och kortet. Låset gäller fortfarande V3c.

Erbjudandet är samlat: `Webbdesign, design och system. Allt på ett ställe.` Tjänsterna är tre
och numrerade 01 till 03: `Design`, `Utveckling`, `System`. Var och en får en kort underrad i
byråröst, utan påståenden om kunder eller resultat.

Tesrubriken är `VI BYGGER ERT VARUMÄRKE.`

Prisrubriken är `Alla har rätt till bra design.`

## Positioning

Vi visar vad vi kan i stället för att påstå det. Byrån visar sitt arbete genom tre riktiga
exempelsajter som ligger i samma repo och serveras live. De får visas live i `<iframe>`, samma
origin när sidan serveras från repo-roten, och de ska vara användbara när de är öppna. En
besökare kan alltså använda arbetet direkt på sidan, inte bara titta på en bild av det.

Tre saker till skiljer erbjudandet: design, utveckling och system kommer från samma ställe;
två av tre paket har ett pris utskrivet på sidan; och prislöftet är formulerat som en
principsats, `Alla har rätt till bra design.`

## Operating Context

- De tre exempelsajterna ligger i samma repo som sidan och serveras live därifrån.
- Ramarna är samma origin när sidan serveras från repo-roten.
- En ram som visats får aldrig transformeras eller tonas efteråt. Den ska gå att använda.
- Skärmbilder av de tre sajterna ligger i `assets/demo-calyx.webp`, `assets/demo-horai.webp`
  och `assets/demo-hyperborea.webp`.
- Logotypen ligger i `assets/logo-white.svg` och `assets/logo-black.svg` och får läggas inline.
- Allt material ligger i `assets/`. Inga egna Unsplash-anrop och ingen egen server.
- Servern är `python ~/.agents/skills/design/scripts/serve.py --port <port>` från repo-roten.
- Kontakt sker via e-post. Det finns inget formulär som skickar någonstans.
  **V3d, Antons beslut 2026-09-20:** låset hävt för V3d. Sidan får en egen
  kontaktsektion med formulär efter priserna. Ingen server tillkommer: knappen
  öppnar ett mejl till `kontakt@alunix.se` med fältens innehåll, så den gör det
  den säger. Gäller bara V3d.

## Capabilities and Constraints

**Tre paket.** Raderna och priserna är låsta och skrivs ordagrant:

| Paket | Pris |
|---|---|
| `Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering.` | `26 900 kr` |
| `Paket med bokningssystem, betalning och kunddatabas.` | `38 900 kr` |
| `Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera` | `Pris vid förfrågan` |

**Tre tjänster.** `Design`, `Utveckling`, `System`, numrerade 01 till 03, en kort underrad var.

**En kontaktväg.** `kontakt@alunix.se`, både som text och som mailto. Inget formulär.
  **V3d:** se hävningen ovan. Adressen står kvar som alternativ väg in bredvid formuläret.

**Tre exempelsajter, live.** Se Evidence on Hand.

**Bindande begränsningar i allt vi bygger:**

- Inga påhittade tal, kunder, omdömen, citat, logotypväggar, stjärnor eller "nöjda kunder".
- Inga tankstreck i synlig text.
- Inget "jag".
- Inga foton som läses som "vårt kontor" eller "vårt team".
- Inga hexfärger och inga typsnitt hämtade ur någon annan färdig mall.

**Öppet, inte bestämt:** vad de tre tjänsternas underrader säger ordagrant. De ska vara korta
och i byråröst, men texten är inte skriven.

## Brand Commitments

**Namn.** Alunix. Ett förbjudet namn finns, se Absences.

**Röst.** Byråröst i vi-form. Korta satser. Fakta före adjektiv. Svenska. Inget "jag". Inga
tankstreck i synlig text.

**Låst copy, copy-gate.** Följande rader bevaras ordagrant och skrivs aldrig om:

- `Er hemsida är nutidens visitkort`
- `Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten.` (gäller V3c. I V3d borttagen på Antons uttryckliga beslut 2026-09-20: "ta bort den lilla texten vid visitkortet helt". Låst copy räknar därmed 11 synliga rader i V3d.)
- `VI BYGGER ERT VARUMÄRKE.` (gäller V3c. I V3d borttagen på Antons uttryckliga beslut 2026-09-19: tesbandet slutar på "Vi hjälper er att synas på rätt sätt.")
- `Webbdesign, design och system. Allt på ett ställe.`
- `Design`, `Utveckling`, `System`
- `Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering.`
- `26 900 kr`
- `Paket med bokningssystem, betalning och kunddatabas.`
- `38 900 kr`
- `Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera`
- `Pris vid förfrågan`
- `Alla har rätt till bra design.`
- `kontakt@alunix.se`
- `Exempelsida: Calyx, florist i Stockholm`
- `Exempelsida: Hōrai, Asian fusion-koncept`
- `Exempelsida: Hyperborea, konferens i Lund`

(De tre bildtexterna gäller V3c. I V3d borttagna på Antons beslut 2026-09-19: liten beskrivande text är förbjuden, F-016. Ramens namn bärs av iframens `title`.)

**Logotyp.** `assets/logo-white.svg` och `assets/logo-black.svg`. Får läggas inline.

**Dagens register, som jämförelse och inte som lås.** Kall nästan svart `#17181B`. Blå
`#1E5E9C` bara för handling. Geist för rubrik, Inter för brödtext, JetBrains Mono för data.
Ett nytt koncept får avvika helt från det.

## Evidence on Hand

Detta är hela beviskassan. Inget annat får synas på sidan.

**Tre exempelsajter, live i `<iframe>`, med sina låsta bildtexter:**

| Sajt | Fil | Rad att använda |
|---|---|---|
| Calyx | `/sites/calyx.html` | `Exempelsida: Calyx, florist i Stockholm` |
| Hōrai | `/sites/horai.html` | `Exempelsida: Hōrai, Asian fusion-koncept` |
| Hyperborea | `/sites/hyperborea.html` | `Exempelsida: Hyperborea, konferens i Lund` |

De tre exempelsajterna är de enda kunder som får synas.

**Skärmbilder av dem:** `assets/demo-calyx.webp`, `assets/demo-horai.webp`,
`assets/demo-hyperborea.webp`.

**Tre paket med pris:** `26 900 kr`, `38 900 kr`, `Pris vid förfrågan`, med paketraderna
ordagrant som de står under Capabilities and Constraints.

**En adress:** `kontakt@alunix.se`, som text och som mailto.

**Logotypfiler:** `assets/logo-white.svg`, `assets/logo-black.svg`.

**Ordagrann copy:** hela listan under Brand Commitments.

## Absences Future Work Must Not Fabricate

Inget av det här finns i beviskassan. Det får därför aldrig uppstå i en design, en bildtext,
en platshållare eller en bildprompt:

- Kunder utöver de tre exempelsajterna.
- Omdömen, recensioner och "nöjda kunder".
- Citat från någon utanför sidan.
- Logotypväggar.
- Stjärnor och betyg.
- Ett team att visa upp. Personer, porträtt, namn, roller.
- Ett kontor att visa upp. Inga foton som läses som "vårt kontor" eller "vårt team".
- Antal år i branschen.
- Antal projekt, antal kunder, antal leveranser.
- Påhittade tal överhuvudtaget. De enda siffrorna vi har är `26 900 kr` och `38 900 kr`, och
  tjänsternas numrering 01 till 03.
- Namnet Klova. Det får aldrig förekomma.

## Product Principles

1. **Beviset ska gå att använda, inte bara ses.** De tre sajterna är riktiga och körs live på
   sidan. Ramar som visats förblir användbara.
2. **Varje siffra på sidan är en siffra vi kan stå för.** Vi har två priser och en numrering.
   Fler tal finns inte, så fler tal skrivs inte.
3. **Priset står framme.** Två paket har ett utskrivet pris. Det tredje säger `Pris vid
   förfrågan` och inget annat.
4. **En adress, inget formulär.** (**Hävt för V3d 2026-09-20**, se § ovan.) `kontakt@alunix.se` är hela kontaktvägen, som text och som
   mailto.
5. **Vi talar i vi-form och kort.** Fakta före adjektiv. Aldrig "jag".
