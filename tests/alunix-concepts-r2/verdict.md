# Verdict r2 — sex byråkoncept nära källornas balans (2026-09-04)

Runda 1 underkändes av Anton: copyn lät som en enmansfirma, sidorna saknade källornas visuella
balans. Runda 2: byråregister i vi-form på Insigns nivå (Antons rader som källa), varje koncept
följer EN dominerande källas layoutbalans med det närmaste Google-typsnittet, två koncept följer
Squarespace-layouten nära. Board: http://127.0.0.1:4621/board.html.

## Kedjan fyrade (ledgern efter omstarten, sessions-id 93a4e52c)

| Skill | laddningar |
|---|---|
| `design` | 6 (R1–R6) |
| `copywriting` med byråröst som CONTENT FUNDAMENTALS | 6 |
| `humanizer-svenska` | 6 |
| `copy-gate.md` Pass 1b (Antons rader = källa 4) | 6, läst som fil |
| bildläsningar (källor + egna skärmbilder) | 143 |

Route gap enligt stop-hooken: `animated-navigation, emil-design-eng, imagegen-frontend-web,
impeccable layout` pekades ut på kodsignal men laddades inte; inget av dem var motiverat i
fold+fyra-sektioner utan animerad nav, bildgenerering eller komponentbibliotek.

## Källa → typsnitt → vad som lånades

| R | källa | typsnitt | balans som lånades | eget |
|---|---|---|---|---|
| R1 | Squarespace | Inter 300 (Clarkson) | fullbleed mörk hero, centrerad 72 px 300-rubrik, ghost-knapp + underrad, kundens sajter som svävande ramar, svart/vit-band, vit sal med mejl i 72 px | palett (akromatisk men Alunix' demor som färg), copy, sektionsordning |
| R2 | Squarespace, andra läsningen | Figtree 300 | vit hero med pill-flikar, mörka kort med pil, svart enradsband, tre textkolumner utan ikoner, 0 px/100 px-radier | inget foto, egen ordning |
| R3 | insign.se | Hanken Grotesk 400 + Instrument Serif-logotyp | vit grotesk-hero utan foto, mosaikremsa, tre mättade tjänsteband med enhetsbild, projektarkiv, mörkt avslut | tre egna nyanser (blå/plommon/bärnsten ur Alunix + demona), inga omdömen/statistik |
| R4 | Sanity | Archivo 700 + IBM Plex Mono | mörk texturhero, komprimerad rubrik, en pill-CTA, vita sektioner 01–05 med riktiga skärmbilder, mono-spår | Alunix-blå i stället för orange, process som innehåll |
| R5 | Mattis Studio | Geist | konsolram med tagg/klocka/hörnmarkeringar, ordmärke + tjänstelista, mättat tesblock bredvid svartvitt foto, vitt jätterubriksblock | blå i stället för orange, inga slot-/projekträknare |
| R6 | Creative Giants | Public Sans 300 | ordmärke i viewport-bredd vikt 300, fullbleed dokumentärt foto med ortsrad, luftiga redaktionella sektioner, färg bara som små ytor | off-white, egen kolofon |

## Fingerprint (grammatik · nav · hero · aktform · avslut · signature)

| R | grammatik | nav | hero | aktform | avslut | signature | max delat |
|---|---|---|---|---|---|---|---|
| R1 | rhythmic cutlist | svart topprad, ghost | mörkt foto + centrerad rubrik + ramar | svart/vit-band | vit sal, mejl 72 px | ramarna glider in | 1/6 (R2: källa) |
| R2 | chaptered editorial | vit + pill-flikar | vit yta, vänsterställd rubrik | vit/svart/vit, kortrad | svart band | flikarna byter sajt | 1/6 |
| R3 | chaptered editorial | vit, serif-logotyp | vit, grotesk, ingen bild | mosaik → band → arkiv | mörkt band | färgbanden = tjänsterna | 2/6 (R2: grammatik, vit hero) |
| R4 | chaptered editorial | mörk, mono | fullbleed textur + komprimerad rubrik | 01–05 | mörkt band + pill | mono-numren | 2/6 (R3: grammatik, mörkt avslut) |
| R5 | split stage | konsolram | ordmärke i ram över foto | svart → mättat → vitt | vitt jätteblock | hörnmarkeringar | 0/6 |
| R6 | typographic poster | pill-meny | rubrik i affischskala | luft → foto → sektioner | off-white kolofon | små färgytor | 0/6 |

## Rättelser efter min pixelläsning

| R | fel | åtgärd |
|---|---|---|
| R1 | svävande ramar ~20 % breda, staplade | figure-marginal + max-width-lås hittade; ramar 31/35/31 % i 16:10, mitten höjd |
| R2 | kortbilder kapade demonas rubriker; Calyx hade Hōrais text | 16:10; egen faktarad per kort |
| R3 | mosaiken upprepade samma Hōrai-beskärning och visade avhuggna bokstäver | sex distinkta beskärningar (tre rubriker, tre detaljer) |
| R5 | bilden i tesblocket kapade Hyperboreas rubrik | 16:10, gråskala kvar |
| R6 | ordmärket ~45 % av bredden | vw-clamp, kant till kant; tre projektbeskrivningar med påhittat innehåll ("e-handel", "bordsbokning", "anmälan") ersatta av briefens fakta |
| R2, R6 | påhittade projektomfattningar | struket; endast florist/restaurang/konferens + designraden |

Kvar som uppföljning (flaggade, inte gjorda): R5:s och R6:s projektminiatyrer har samma
beskärningsmönster i mindre skala.

## Copy: en byråröst

Alla sex använder Antons rader som ryggrad: "Din digitala byrå, allt på ett ställe" (R1, R2, R3,
R5), "Er digitala byrå. Allt på ett ställe." (R4), "Nutidens visitkort" (R1, R2, R4, R6), "Vårt enda
mått: perfektion" (alla, som band, rubrik eller kolofonrad), filosofin ordagrant (alla). Inga
"jag", inga enmans-formuleringar, inga påhittade tal, inga kunder utöver demona, inga tankstreck.
Variationen sitter i betoningen: R4 processen (fem steg), R5 "Det första intrycket är digitalt /
Vi bygger webbplatser", R6 filosofin, R3 tjänsterna.

## Slår de referenserna? (ärligt)

R1 och R2 ligger nu på Squarespace-balansen; skillnaden mot förlagan är att Squarespace har video
och riktiga hovertillstånd, och att R1:s ramar är stillbilder. R3 har Insigns rytm och en tydligare
tjänstelogik (färgerna hör till Alunix) men saknar Insigns bevisband, för att inga siffror får
hittas på. R4 matchar Sanitys hero rakt av. R5 är den som står närmast sin förlaga i känsla och den
jag skulle visa först. R6 har Creative Giants proportioner men fotot är svagare än deras video.
Rangordning på pixlar: R5, R1, R3, R4, R2, R6.
