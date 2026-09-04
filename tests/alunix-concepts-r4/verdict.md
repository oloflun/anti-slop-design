# Verdict r4 — tre remixer av r3-sidan (2026-09-04)

Anton om r3: "känns fortfarande lite off". Uppdraget: tre remixer med tydligt olika upplägg och struktur,
samma koncept och copy, egna scrollresor där text och bild går åt olika håll, inspiration ur katalogen.
Board: http://127.0.0.1:4622/board.html (tangent 1–3). Cellerna: `cells/M1..M3-chain/index.html`.

## Tre riktningar

| M | struktur | text ↔ bild | signature move | källor |
|---|---|---|---|---|
| M1 Kontinuerlig grund | Tidvatten fullbredd, två spalter förskjutna 50vh, en mörk grund under allt | text stiger, bild sjunker | fönster i panelerna som visar grunden | rre-ventures, veloura, creative-giants |
| M2 Kapitel · pinnad scen | en spalt i fem kapitel med folio, kapitel 02 = pinnad scen där Tidvatten, Hōrai och Calyx byter plats | text in från höger, bild wipas från vänster | roterad löptext längs kanten som scrollens spelhuvud | vinterspelen, sanity, not-real, shelby-kay |
| M3 Galleri · sidopanering | affischordmärke över konsolkortet, horisontell rail med tre ramar som objekt, ledgern scrubbad ord för ord | etiketter åt vänster, ramar åt höger | ordscrubb med tråd som ritar sig (vintergatan) | vintergatan, palais, garden-eight, mattis-studio |

Fingerprint mot r3: M1 1/6, M2 2/6, M3 0/6. Mellan remixerna: 0–1/6.

## Min pixelläsning, per remix

**M2.** Första bygget hade två fel: kapitelpanelen upprepade "Er hemsida är nutidens visitkort" ovanpå
Tidvatten-ramen där rubriken redan står, och tjänstetexterna låg i en smal högerställd remsa. Efter
fixen: kapitlets rubrikrad ligger i flödet ovanför scenen, tjänsterna som en panel i taget (36ch),
Tidvattens egen rubrik fri. Scenbytet Hōrai → Calyx visar ett kort svart fält till höger mitt i wipen;
det är övergången, inte ett fel, men det syns. Rangordning: den remix som tydligast bryter med r3:s
upplägg och ändå håller ihop.

**M3.** Första bygget: loggan skar "DIGITAL BYRÅ", objektetiketten upprepade Tidvattens rubrik, etikett
03 kapades med tre punkter, räknaren stod still på 01/03, och det blå blocket var en tom blå viewport
med en svart irisfläck innan innehållet. Efter fixen: allt rättat; tesblockets text hälsar direkt och
bara Hyperborea-bilden irisar in. Railen mäter 1775 px resa. Stark öppning (ordmärke över konsolkort).

**M1.** Första bygget: fönstren renderades som suddiga grå cirklar över innehåll, rubriken "VI BYGGER /
ERT VARUMÄRKE." revs isär av per-rad-rörelse, tomband ovanför Hōrai och Calyx, hål i konsolkortet.
Fixrunda med hårda gränser (en wrapper per block, ≤ 90 px text, ≤ 120 px bild inuti overflow-hidden,
fönster = skarpa rektanglar i innehållsfria band). Efter den: rörelsen håller ihop, men fönstren
lästes som trasiga bildplatser och ramarnas nedsjunkning dolde Calyx och Hōrais egna topprader. Tredje
rundan: fönstren borttagna (grunden syns ändå i förskjutningen och luckorna), ramarna statiska, bara
foton sjunker. Slutläge: rent; signature move är nu förskjutningen själv plus grundens tre färgstopp,
vilket är ärligt men svagare än M2:s och M3:s. Rangordning på pixlar: M2, M3, M1.

## Kedjan

`Skill(design)` laddad i alla tre bygg-agenter (ledger). Ingen copy-kedja: copyn är r3:s ordagrant.
Verifiering per cell: scroll_verify, a11y 0 fel, inget dokumentöverflöde, tre ramar med titel, konsol
ren, reduced motion statisk, fem rörelsebilder (`shots/motion-0..4.png`) som bevis för riktningarna.

## Ärligt

Rörelserna "text och bild åt olika håll" är svårast i M1 där båda ligger i samma flöde; M2 och M3 får
det gratis av sina grammatiker (pinnad scen, rail). Om Anton vill gå vidare med en remix bör nästa steg
vara en riktig scrollverifiering i webbläsaren, inte bara skärmbilder.
