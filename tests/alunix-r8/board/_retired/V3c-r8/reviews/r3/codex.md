fix

## persistence

Codex (`gpt-5.5`, headless, read-only) kördes en gång från repo-roten med
`codex exec --skip-git-repo-check -`, prompten bar invarianterna ordagrant (F-011, motorn
redigeras aldrig, `--sc-ps` mot `--sc-p`, `.sc-*` restylas aldrig, `will-change` bara medan
0 < ps < 1, lokala typsnitt, låst copy). Körningen tog cirka 9 minuter, exit 0, 213 399
tokens. Codex kunde inte köra en webbläsare i sin sandlåda och sa det uttryckligen i stället
för att gissa; all mätning nedan är därför min egen, med Playwright mot `127.0.0.1:3321` vid
1440x900 och 1512x945.

Tio fynd kom tillbaka. **Åtta överlevde verifikationen, ett skrevs om, ett ströks.**

Struket: `index.html:907`, påståendet att IntersectionObservern inte kan förvarna eftersom
dess mål ligger inuti ett `content-visibility:auto`-subträd. Jag mätte det: Calyx `src` sätts
vid `scrollY` 800 när ramens överkant står 1580 px ned, alltså cirka 1,75 skärmar i förväg,
och Hōrai vid 1200/1494. Förvarningen fungerar i Chromium och fyndet går inte att återskapa.

Omskrivet: `index.html:486`. Codex ville ha BRIEF:ens `1px 800px`. Mätt höjd på `.price` är
505 px, så 800 är också fel; målvärdet nedan är det mätta.

Två Codex-fynd (858 och 860) är samma rotorsak och är slagna ihop till en post. Fem poster
nedan är mina egna, mätta och inte från Codex: preview-lägenas inert-tillstånd, bildernas
sökvägar, ramarnas nätverkstrafik, dokumenthöjdens 359 px-svängning och de duplicerade
CSS-reglerna.

Ingen invändning om rörelsepreferens kom tillbaka (F-011 höll i prompten), inga tankstreck
och ingen `fonts.googleapis.com` finns i cellens eget dokument, ingen regel i sidan selekterar
en `.sc-*`-klass, och konsolen är ren från sidans egen kod.

## fidelity

Mekaniskt gör sidan i allt väsentligt det BRIEF.md beskriver. Aktsekvensen stämmer: en
`pin` (`data-sc-span="2.2" data-sc-dwell="0.35"`, index.html:624), sex `flow`, noll `scrub`,
stagen märkt med attributet `data-sc-stage` och inte med klassen. Device-tabellens rad om
datakällan håller: `--flip` (280-284), ljuspölen (310), `--scrub` (510) och `.giant`-skalan
(518) läser alla `--sc-ps`; ingen bespoke rörelse läser rått `--sc-p`. `--sc-ps` publiceras
per akt av shimen, så varje akt räknar på sin egen progress, vilket är förutsättningen för att
både `--flip` och `--scrub` ska kunna vara ren CSS.

Tre avvikelser mot brief-texten, alla mätta: preview-lägena `front|mid|back` sätter `--flip`
korrekt men blir överkörda av sidans egen rAF på nästa bildruta (se fix 3), `?preview=bleed`
(972) tvingar ingenting utan scrollar bara dit (bleeden är statisk CSS på rad 443 vid minst
900 px bredd, så läget är i praktiken en no-op), och `content-visibility`-raden (BRIEF.md:162)
är byggd med andra tal än de låsta och saknas helt på `.horai-wrap`. Bilderna är fortfarande
inte vendorade in i cellen trots R2-raden om att sökvägarna byts i R3.

## ceiling

Motorn, `scroll/scrollcraft.js` och `scrollcraft.css`: rapporteras, rättas aldrig.
`scrollcraft.js:1026` schemalägger `requestAnimationFrame(tick)` ovillkorligt i varje varv,
även på en sida utan `scrub`-klipp och utan sekvens, alltså en rAF-loop hela sidans livstid.
Sidans egen loop gör tvärtom det rätta: `schedule()` (868) körs bara på scroll och resize, och
`readState` gör noll layoutläsningar. Där är sidan bättre än motorn den ligger på.

`sc-smooth.js:80` läser `getComputedStyle` per akt och bildruta medan någon akt rör sig, och
`window.__scSmooth.acts` (131) binds till den array `collect()` sedan byter ut, så handtaget
är inaktuellt efter första resize. Bägge är shim-nivå och rapporteras, inte fixas.

V3b, den låsta primärreferensen: n/a på kodnivå för fynden nedan. Varje post är ny kod i V3c,
inte ärvd, och V3b gör inget av det bättre.

## material_fixes

1. `index.html:271` `.hero-plate{overflow:clip}` klipper signaturaktens egen mätpunkt. Mätt
vid 1512x945 med `?preview=mid`: `.plate-edge` projiceras till 749 px men målar bara 306-725,
alltså 420 px; 110 px försvinner i överkanten och 219 px i underkanten, alltså två tredjedelar
av bortfallet nedtill, vilket är det leaden läste som 405 mot 502. Med `overflow:visible` på
samma element målas hela 196-944. Stagens `overflow:clip` och `container-type` är oskyldiga,
verifierat genom att stänga av dem var för sig. Målvärde: vid `--flip` 0.5 målar hårlinjen
minst 95 procent av kortets höjd (minst 478 av 504 px vid 1440x900, minst 502 av 529 px vid
1512x945) och bortfallet är lika stort upptill som nedtill. Kortet behöver fortfarande sitt
skydd mot rubriken (kommentaren 260-265), så klippningen hör hemma på en förälder med
huvudhöjd, alternativt motskalas rimmen med perspektivfaktorn 1/1,42.

2. `index.html:858` sidans egen progress hoppar över motorns `dwell`-omräkning. Motorn räknar
`a.p = dwell(raw, 0.35)` i `scrollcraft.js:835`, sidan räknar `ps = (scrollY - actTop) /
travel` rått. Mätt: vid raw 0.42 står motorns `--sc-p` på 0.4475. Vändningen passerar 90
grader när `--sc-p` är 0.42, alltså vid raw 0.3806, men `setFace` växlar först vid raw 0.42,
41 px scroll för sent, och i det fönstret är den bortvända ytan den fokuserbara. Samma
rotorsak träffar `is-turning` på rad 860: gränsen 0.9995 nås av det råa värdet medan shimen
fortfarande lerpar de sista cirka 20 bildrutorna, så `will-change` tas bort mitt i rörelsen.
Målvärde: båda gränserna räknas ur samma tal som CSS ritar med, alltså `--sc-ps` på akten, så
ansiktsbytet sker vid `--sc-ps` 0.42 och `is-turning` ligger kvar tills `--sc-ps` står på 0
eller 1.

3. `index.html:954-964` preview-lägena körs över av `schedule()` på rad 871. Den rAF:en är
köad före preview-blocket och kör `readState` en bildruta senare, så det scrollhärledda
tillståndet vinner. Mätt på `?preview=back`: `--flip` är 1 och baksidan syns, men
`faceBack.inert` är true, `aria-hidden` är true och `.card-cta` går inte att fokusera
(`document.activeElement` blir inte länken). Målvärde: när `mode` finns i `MODES` rör
`readState` varken `setFace` eller `is-turning`, och `?preview=back` lämnar baksidan
fokuserbar med `aria-hidden` satt till false.

4. `index.html:486` och `:567`, plus `:467`, fel respektive saknad `contain-intrinsic-size`.
Mätt vid 1440x900: `.price` reserverar 760 px men är 505 px, `.horai-wrap` har
`content-visibility:auto` utan intrinsic size alls (beräknas till `auto none`) och är 1022 px
mot sin `min-height` 80dvh, alltså 720 px. Dokumenthöjden går från 4378 px vid load till
4019 px när blocken målats, alltså 359 px scrolltrack som försvinner under läsaren. Motorn
mäter `a.top` och `a.height` bara i `layout()`, som körs på resize och `fonts.ready`, så varje
`flow`-akt under priset räknar progress mot en geometri som inte längre gäller. Målvärde:
`.price` `contain-intrinsic-size: auto 505px`, `.horai-wrap` `auto 1020px`, `.calyx-wrap`
`auto 810px`, och dokumenthöjden skiljer mindre än 1 procent mellan load och genomscrollad
sida.

5. `index.html:639`, `:683` och `:806`: cellen är inte självständig. Alla tre bilderna pekar
på `/tests/alunix-concepts-r3/build/assets/`, medan `runs/V3c/assets/` bara innehåller
`fonts/`, `ASSETS.md` och `credits.json`. BRIEF.md:188 lovar uttryckligen att sökvägarna byts
till `assets/` i R3. Grundbilden sätts dessutom från JS på rad 806, så utan skript har sidan
ingen grund alls. Målvärde: de tre filerna ligger under `runs/V3c/assets/`, refereras
relativt, och `--ground-img` deklareras i CSS med JS-raden borttagen.

6. `index.html:8` och `:73`: påståendet att sidan inte hämtar något över nätet är falskt vid
körning. De två live-ramarna drar `cdn.tailwindcss.com`, `fonts.googleapis.com`,
`fonts.gstatic.com` och fyra Unsplash-bilder, se `sites/calyx.html:7-10` och `:48-51` samt
`sites/horai.html:7`. Mätt som två konsolvarningar från Tailwind-CDN vid full genomscroll.
Det slår rakt in i prestandaplanens tak på 2,5 MB. Målvärde: antingen vendoras ramarnas egna
beroenden, eller så begränsas påståendet i kommentaren till sidans eget dokument och
överföringen mäts om med ramarna inräknade.

7. `index.html:79`: `preload` på Geist 700 motsäger både BRIEF.md:490, som säger bara Public
Sans 300, och filens egen kommentar två rader ovanför, som avfärdar Geist Mono med argumentet
att kortbaksidan är bortvänd vid p = 0. Geist 700 har exakt samma bortvända baksida som enda
foldbruk. Målvärde: exakt en `preload`-rad, Public Sans 300; Geist 700 laddas av `@font-face`
med `font-display:swap` som i dag.

8. `index.html:411`, `:591` mot `:605`, och `:561` mot `:562`: död och dubblerad CSS.
`.kicker-sans` definieras men används av noll element; enda förekomsten av strängen i filen är
regeln själv. `.thesis-figure{margin-right:0;transform:none}` deklareras identiskt i
`max-width:900` och igen i `max-width:640`, där 900-regeln redan täcker hela intervallet.
`.ledger-row{grid-template-columns:1fr}` står både som `@container (max-width:360px)` och som
`@media (max-width:900px)`, och container-varianten kan aldrig träffa utanför media-varianten.
Målvärde: tre rader borta, noll ändring i renderad geometri, verifierat med en diff av
`getBoundingClientRect` på `.thesis-figure` och `.ledger-row` vid 320, 640 och 900.

## keep

`--flip` som ren CSS-smoothstep ur `--sc-ps` (280-284) och `--scrub` på samma sätt (510).
Noll JS-bildrutor i vändningen, och `--sc-ps` är registrerad som ett tal av shimen, så
uttrycket räknar och substituerar inte bara. Ordscrubben skriver `--i` och `--n` en gång vid
montering (929-947) och aldrig per bildruta.

`readState` (855-867) gör noll layoutläsningar; geometrin cachas i `measureAct` och uppdateras
på resize och load. Scroll- och resizelyssnarna är passiva och `schedule()` har en
pending-flagga, så en scroll ger som mest en rAF.

`.frame-fig{will-change:auto}` (463) neutraliserar motorns promovering av
`[data-sc-reveal]` på sidans två största block, och gör det på sidans egen klass, inte på en
`.sc-*`-klass. Mätt: `willChange` beräknas till `auto`. Ingen vilande promovering finns kvar
någonstans; `.hero.is-turning .plate-card` (287) är den enda `will-change` på sidan.

Iframe-monteringen (880-920): `data-src` plus `loading="lazy"` plus IntersectionObserver med
`rootMargin: 100% 0px`, `obs.unobserve` per ram, och `src`-skrivningen lagd i en
`requestIdleCallback` med timeout. Mätt: noll `src` vid load, Calyx monteras 1,75 skärmar i
förväg, Hōrai likaså, och ingen ram transformeras efteråt.

`.ground{contain:strict}` (199), `background-blend-mode` i stället för `mix-blend-mode`, och
att `background-attachment:fixed` är borttaget. Attributionstabellen i kommentaren är mätt och
stämmer med hur elementet faktiskt är byggt.

Alla `img` har `width` och `height`, båda iframes har `title` och `loading="lazy"`, `footer`
ligger utanför `main` så att `contentinfo` mappas, `.frame-wrap:focus-within` ritar
fokusringen på wrappern i stället för på ramen, och sidan har noll tankstreck och noll externa
typsnittsanrop i sitt eget dokument.
