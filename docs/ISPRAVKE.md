# ISPRAVKE — evidencija ispravljenih tvrdnji

Ova datoteka vodi **svaku tvrdnju koja je iznesena javno, a kasnije se pokazala netočnom ili nepotpunom**.
Pravilo knjige: pogreška se ne briše — bilježi se (što je pisalo, što je točno, odakle to znamo, gdje je ispravljeno).
Datum u zagradi = datum provjere na primarnom izvoru.

---

## ISPRAVAK-001 · 14. 9. 2026. · METR-ov vremenski horizont

- **Pisalo je:** METR-ov vremenski horizont za frontier model u veljači 2026. iznosi ~13–14,5 h. (izlaganje IUC Dubrovnik, 11. 9. 2026., slajd 16)
- **Točno je:** prvotna METR-ova procjena za **Claude Opus 4.6** (20. 2. 2026.) bila je **~14,5 h**, ali je METR **3. 3. 2026. ispravio bug** u svom modeliranju i vrijednost spustio na **~12 h**.
- **Uz to:** METR uz graf navodi: *„Measurements above 16 hrs are unreliable with our current task suite."* **Claude Mythos** (ožujak 2026.) ocijenjen je na **16+ h** — što je gornja granica skupa zadataka, a ne novi plato.
- **Izvor:** METR (2025), arXiv:2503.14499 (NeurIPS 2025); METR-ova napomena uz graf (2026.); A. Cotra (METR), *I underestimated AI capabilities (again)*, 3. 3. 2026.
- **Posljedica za tekst:** horizont se navodi kao **~12 h (nakon ispravka, 3. 3. 2026.)**, a svako navođenje brojke iznad 16 h mora nositi napomenu o nepouzdanosti mjerenja.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina G) · `data/fakti.csv` (`metr_horizon_2026`, novi `metr_unreliable_above`)

## ISPRAVAK-002 · 14. 9. 2026. · Strop GPQA

- **Pisalo je:** strop GPQA („nesporno točni" odgovori) ≈ **90 %**. (izlaganje, slajd 17)
- **Točno je:** strop je **~80 %** (zavisi od podskupa); GPQA je **zasićen 11/2025** (Gemini 3 Pro @ 93,8 %), a **Anthropic ga prestaje izvještavati od 6/2026**.
- **Izvor:** A. D. Thompson, *Mapping IQ, MMLU, MMLU-Pro, GPQA, HLE*, LifeArchitect.ai (ažurirano 4. 8. 2026.); Rein et al. (2023), arXiv:2311.12022.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina H) · `data/fakti.csv` (`gpqa_ceiling` = 80, uz novi `mmlu_ceiling` 91 i `mmlu_pro_ceiling` 90 za kontekst)

## ISPRAVAK-003 · 14. 9. 2026. · Strop HLE (nepotpuna tvrdnja)

- **Pisalo je:** strop HLE = **25,6 %**. (izlaganje, slajd 17)
- **Nepotpuno je:** postoje **dva izvora s različitim vrijednostima** — **~51,3 %** (FutureHouse, 7/2025) i **25,6 %** (Alibaba, 2/2026, arXiv:2602.13964v2). HLE je **gotovo zasićen 12/2025** (GPT-5.2 @ 50 %).
- **Izvor:** Thompson (2026), *Mapping*; HLE (2026), *Nature* 649:1139–1146, DOI 10.1038/s41586-025-09962-4.
- **Posljedica za tekst:** nikad se ne navodi jedan strop kao jedini — navode se **oba, s izvorom i datumom**.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina G) · `data/fakti.csv` (`hle_ceiling` = 51.3 + napomena o Alibabi)

---

## Zašto ovo postoji

Knjiga tvrdi da se razine razlučuju **po vrsti dokaza**, a ne po uvjerljivosti izvora. Ako autor ne bilježi vlastite ispravke, tvrdnja o razlučivanju razina nije vjerodostojna. Zato:

1. **Brojka bez datuma i vrste (mjereno / procjena) nije brojka.**
2. **Ako se dvije mjerne vrijednosti razilaze, navode se obje** — čitatelj dobiva stanje spora, ne autorov izbor.
3. **Ispravak se objavljuje, ne skriva.** Ova datoteka je javna.

## ISPRAVAK-004 — tekst izvan okvira na ploči `fig_omlcc_s1` i potpisi koji su citirali taj tekst

- **Što je pisalo:** na prvoj ploči ljestvice (`fig_omlcc_s1.png`) tekst zaglavlja nedovršenih
  domena glasio je „PSYCHOLOGICAL — reveal on the next click · mental facts · Searle 1995" i
  **prelazio je desni rub panela za 19 px** (tinta do x = 1888, panel do x = 1869). Potpisi
  slika 2.2 i 2.3 citirali su taj tekst („reveal on the next click").
- **Što je točno:** tekst je skraćen na „PSYCHOLOGICAL · mental facts · Searle 1995" (isto kao
  u otkrivenim pločama), pa prekoračenje iznosi **0 px** (mjereno: tinta do x = 1869 = rub
  panela). Nedovršene domene ostaju vidljive kao prigušeni stupci s brojevima 09–16.
- **Zašto je i sadržajno bolje:** „reveal on the next click" uputa je za predavanje (klik), a
  knjiga se ne klika — u tiskanoj slici takva uputa nema smisla.
- **Gdje je ispravljeno:** `figure/fig_omlcc_s1.png` (ponovno izrađeno iz
  `figure/izvori/fig_omlcc_stage.py`), potpisi slika 2.2 i 2.3 u `rukopis/poglavlje-02.md`.
- **Kako je nađeno:** neovisni vizualni pregled 19 figura (3 subagenta) + vlastito mjerenje
  tinte prema rubu panela. Ostalih 18 figura: bez prelijevanja i bez pokvarenih znakova.

## ISPRAVAK-005 — vlastiti pretvarač dijagrama spajao je razlomljene natpise u jedan red

- **Što je bilo:** alat `kod/mermaid_render.py` prevodio je Mermaidov `<foreignObject>` u SVG
  `<text>`, ali je **više redova natpisa spajao u jedan** — natpis je postao širi od kućice i
  tekst je izlazio iz okvira (uočio Benedikt na poslanim slikama).
- **Što je točno:** svaki `<p>` (i svaki `<br/>`) sada je **zaseban** `<text>` uz okomito
  centriranje; PNG za pregled traži se od poslužitelja (crta ga isti Chromium koji je mjerio
  okvire), a SVG za tisak ima ugrađenu sigurnosnu marginu od 8 %.
- **Dokaz:** alat `kod/check_figure_overflow.py` — mjeri prelijevanje pikselima i **provjeren je
  kontrolnim slikama** (tekst unutra → bez nalaza; preko desnoga ruba → nalaz; ispod ruba →
  nalaz; oznaka brida podalje → bez nalaza). Rezultat: 4/4 dijagrama čisto i u Chromiumovu i u
  tiskarskom putu (SVG → resvg).
- **Gdje je ispravljeno:** `kod/mermaid_render.py`, `figure/dijagram-*.svg|png`,
  novi alat `kod/check_figure_overflow.py`.

## ISPRAVAK-006 — iz natpisa dijagrama nestajale su strelice (→) i srednja točka (·)

- **Što je bilo:** filtar koji je iz Mermaid izvora uklanjao emoji bio je napisan kao popis
  **dopuštenih** raspona znakova; sve izvan njih se brisalo. Strelice (`→`, kategorija Sm),
  srednja točka (`·`, Po) i znak `×` (Sm) **nisu** bili u dopuštenome, pa je u dijagramu 13.1
  natpis „Čovjek → agent" ispao kao „Čovjek agent" — tvrdnja je promijenila smisao.
- **Što je točno:** filtar sada uklanja **samo prave emoji** (Unicode kategorija `So`),
  varijacijske selektore i nevidljive spojnike; interpunkcija, strelice i matematički znakovi
  ostaju. Provjera: u 13.1 sada stoje tri natpisa s `→`, u 12.1 dva s `·`.
- **Gdje je ispravljeno:** `kod/mermaid_render.py` (filtar `EMOJI`) i ponovno izrađeni
  `figure/dijagram-*.svg|png`.

## ISPRAVAK-007 — naslovi skupina preklapali su se s okvirima (13.1) i prekratki lomovi

- **Što je bilo:** u dijagramu 13.1 `subgraph` naslovi („Čovjek do agenta", „Agent do čovjeka",
  „Agent do agenta") **preklapali su se s okvirima** čvorova; u 12.1 i 12.4 natpisi su se lomili
  u 5–7 redaka, a slike su bile 4:1 stripovi — na 150 mm širine tekst bi ispao oko 5 pt.
- **Što je točno:** 13.1 više ne rabi `subgraph` (tri konfiguracije su čvorovi u mreži),
  12.4 je prebačen u uspravno stablo, lomovi natpisa kontroliraju se zapisom `%% wrap: N` u
  izvoru dijagrama. Izmjereno: tekst sada 8,5–17 pt na 150 mm (prije ~5 pt), bez stripova.
- **Kako je nađeno:** vlastitim pregledom slika nakon uključivanja `model.supports_vision`
  (→ ISPRAVAK-008); mjerilo prelijevanja te stvari **ne vidi** jer tekst nije izlazio iz okvira.

## ISPRAVAK-008 — Hermes je vision prosljeđivao lokalnom modelu iako glavni model ima vision

- **Što je bilo:** `auxiliary.vision` bio je postavljen na `custom:gemma4`
  (`gemma-4-26b-a4b-nvfp4`), a `model.supports_vision` nije bio deklariran — pa je svaki
  `vision_analyze` išao na lokalni Gemma 4 i vraćao **opis u tekstu**, umjesto da sliku priloži
  glavnome modelu. Posljedica: tri pogrešne prosudbe o figurama („pokvaren znak" = glava
  strelice) i prešućeni stvarni kvarovi (preklapanje naslova, nestale strelice).
- **Dokaz da glavni model ima vision:** slika poslana izravno na `deepseek-flash`
  (`/v1/chat/completions`, `image_url`) vraća točan odgovor („7391" i „donjoj").
- **Što je točno:** `hermes config set model.supports_vision true` (kopija configa:
  `config.yaml.prije-vision.bak`). Sada `vision_analyze` prilaže sliku izravno.
- **Napomena:** promjena vrijedi za nove sesije; u tekućoj je već stupila na snagu.

## ISPRAVAK-009 — tri figure ispod tiskarske rezolucije zamijenjene vektorskim dijagramima

- **Što je bilo:** tri PNG figure bile su ispod granice za tisak (~1800 px za 150 mm pri 300 dpi):
  `fig_razine` (891 × 832), `fig_emerg_hijerarhija` (873 × 437), `fig_voda` (952 × 672). U tisku
  bi bile mutne, a skaliranje rastra ne pomaže.
- **Što je točno:** sve tri zamijenjene su **vektorskim dijagramima** (SVG + PNG ~2000 px):
  `dijagram-1-5-slojevi-stvarnosti` (Slika 1.2), `dijagram-3-3-emergentna-hijerarhija`
  (Slika 3.1) i `dijagram-3-4-voda` (Slika 3.2). Stare PNG datoteke **uklonjene** su iz repoa,
  a potpisi prepisani prema onome što se na novim slikama stvarno vidi (npr. Slika 1.2 sada
  nosi i zaglavlja ljestvica — Hartmann 1940 te Novikoff 1945 · Feibleman 1954 — kojih na
  staroj slici nije bilo, pa se nije znalo čija je koja ljestvica).
- **Napomena o kriteriju:** vektorski dijagram nema „rezoluciju"; mjerilo je sada **veličina
  teksta na stranici** (traženo ≥ 8 pt pri širini 150 mm). Izmjereno za sve dijagrame:
  8,2–28 pt.

## ISPRAVAK-010 — četiri nova dijagrama ondje gdje je tekst tražio sliku

- **Dodano:** Slika 4.2 (`dijagram-4-5-vrste-dokaza`, trijaža mjereno/procjena/izvedeno),
  Slika 7.1 (`dijagram-7-5-pet-uvjeta`, pet uvjeta komunikacijskoga čina), Slika 8.1
  (`dijagram-8-1-statusna-funkcija`, X broji kao Y u kontekstu C) i Slika 14.1
  (`dijagram-14-6-funkcionalno-intrinzicno`, funkcionalno i intrinzično po razinama 12–16).
- **Zašto:** to su mjesta na kojima čitatelj mora držati nekoliko odnosa istodobno (trijaža,
  pet kumulativnih uvjeta, tri mjesta formule, dvije vrste prisutnosti kroz pet razina) —
  upravo ondje slika radi posao koji rečenica radi sporije.
- **Provjera:** svaki dijagram pregledan je vizualno (`model.supports_vision` uključen) i
  izmjeren (`check_figure_overflow.py`); vrijednosti u Slici 14.1 prepisane su iz tablice 14.6.

## ISPRAVAK-011 — rukopis je o sebi tvrdio nešto netočno (pogl. 16)

- **Što je bilo:** na kraju 16. poglavlja, u bloku „Otvoreno za provjeru u ovoj datoteci", stajale su
  dvije tvrdnje koje su u međuvremenu postale netočne: (3) da poglavlje 9 **nema** odjeljak
  „Kako bismo znali da griješimo" i (4) da u rukopisu **nema** poglavlja 4 i 15, pa se upute na 4.x i
  15.x odnose na plan, a ne na tekst.
- **Što je točno (17. 9. 2026.):** poglavlje 9 **ima** taj odjeljak, a poglavlja 4 (7.113 riječi) i 15
  (6.488 riječi) **postoje** i dovršena su.
- **Kako je ispravljeno:** tvrdnje nisu obrisane nego prepisane kao **riješene stavke** s datumom, uz
  uputu na ovaj zapis. Razlog je isti kao i za sve ostale ispravke: pogreška se ne briše, jer brisanje
  skriva i samu činjenicu da je rukopis jedno vrijeme bio nepotpun.
- **Uz to:** `check_fakti.py --strict` upozorio je na brojku **300 dimenzija** (fastText cc.hr.300) u
  potpisu slike 10.2 koje nije bilo u evidenciji; dodan je zapis `fasttext_hr_dim` u `data/fakti.csv`.
  Alat `check_lit.py` proširen je tako da provjerava i dijelove rukopisa **bez** popisa literature
  (uvod, zaključak, predgovor, studija slučaja) — u smjeru citat → baza.

## ISPRAVAK-012 — bibliografski podaci provjereni na primarnim izvorima (17. 9. 2026.)

**Što je bilo:** baza referenci navodila je četiri protokola (MCP, A2A, AP2, x402) i šest izvještaja
(GreyNoise, Tenable, Chroma, Knight, t-SNE/UMAP, Perak & Ban Kirigin 2023) **bez punih bibliografskih
podataka**, s oznakom ❓. Uz to je popis literature poglavlja 5 sadržavao **„Perak 2018, 2019"** —
radove kojih nema (OMLCC je izlaganje 2017a; 2017b, kako stoji i u odjeljku K baze).

**Što je utvrđeno (provjereno na primarnim izvorima, ne preko posrednika):**

| jedinica | utvrđeno |
|---|---|
| Anthropic 2024 (MCP) | *Introducing the Model Context Protocol*, spec. rev. 2024-11-05, objavljeno 25. 11. 2024. |
| Google 2025 (A2A) | *Announcing the Agent2Agent Protocol (A2A)*, Google Developers Blog, 9. 4. 2025. |
| Google 2025 (AP2) | *Powering AI commerce with the new Agent Payments Protocol (AP2)*, Google Cloud Blog, 16. 9. 2025. |
| Coinbase 2025 (x402) | *Introducing x402*, Coinbase Developer Platform, 6. 5. 2025. |
| Knight 2025 | *Levels of Autonomy for AI Agents*, **autori Feng, McDonald i Zhang**, 25-15 Knight First Amend. Inst., 28. 7. 2025.; pet razina autonomije |
| Chroma 2025 | Hong, Troynikov i Huber, *Context Rot*, Chroma Technical Report, 14. 7. 2025. |
| GreyNoise 2026 | *Agents Gone Wild…*, 9. 9. 2026. (potvrđene i brojke: 395 organizacija, 440 instanci, 48 zemalja) |
| Tenable 2026 | Research Special Operations, *The Agentic AI threat cluster…*, 14. 8. 2026. |
| t-SNE | van der Maaten & Hinton 2008, *JMLR* 9(86): 2579–2605 |
| UMAP | McInnes, Healy i Melville 2018, arXiv:1802.03426 (DOI 10.48550/arXiv.1802.03426) |
| Perak & Ban Kirigin 2023 | *Natural Language Engineering* 29(3): 584–614, DOI 10.1017/S1351324922000274 (Crossref) |

**Što je ispravljeno u rukopisu:**
1. poglavlje 5 — popis literature: „Perak 2014, 2018, 2019, 2025, 2026" → **„Perak 2014 · Perak 2025 · Perak 2026 · Perak, OMLCC - izlaganja 2017a; 2017b"**;
2. poglavlje 10 — t-SNE i UMAP više se ne navode samo imenom: dodani su citati i oba rada u popis;
3. poglavlja 3, 6 i 4 — ukinute napomene da se „puni podaci preuzimaju iz autorove bibliografije" (podaci su sada u bazi);
4. poglavlja 12 i 14 — ❓ blokovi skraćeni: riješene stavke (bibliografije, Knight) premještene u „Zatvoreno", ostaju samo one koje nisu bibliografske (vrsta brojke; nalazi o odsutnosti).

**Što ostaje otvoreno:** tipološka replikacija ljestvice (pogl. 2), nalazi o odsutnosti (pogl. 11, 14, 15, 16) i Perak 2025 (naslov i izdanje iz autorove bibliografije).

## ISPRAVAK-013 — popis literature 11. poglavlja bio je u drugom formatu, pa nije bio provjeravan (27. 9. 2026.)

**Što je bilo:** 11. poglavlje imalo je popis literature u **vlastitome formatu** — pune bibliografske
jedinice, jedna po retku s critom (`- Autor, I. (godina). Naslov…`) — dok sva ostala poglavlja rabe
jednoredni oblik `Autor godina · Autor godina` pod naslovom `### Literatura poglavlja`.
**Posljedica:** `kod/check_lit.py` čita popis iz **prvoga retka** iza naslova, pa je u tome poglavlju
provjeravao **1 jedinicu umjesto 24**: ostalih 23 nisu bile ni provjerene prema tekstu (smjer A), a u
repozitoriju su **dvostruko** stajali podaci koji pripadaju isključivo `referencije/REFERENCE_BASE.md`.

**Dokaz da je riječ o stvarnome propustu, a ne o stilu:** prije ispravka `check_lit.py` je izvješćivao
*425 jedinica / 909 citata*; nakon pretvorbe **459 jedinica / 926 citata** — razlika od 23 jedinice
u poglavlju 11 je upravo ono što nije bilo obuhvaćeno.

**Što je ispravljeno:** popis 11. poglavlja pretvoren je u standardni oblik (23 postojeće jedinice +
novi `Li et al. 2026`), a pune bibliografske jedinice ostaju samo u `REFERENCE_BASE.md`, kako pravilo
i nalaže. Nakon pretvorbe **sve jedinice prolaze oba smjera provjere** (nijedna nije prijavljena kao
„u popisu, a ne u tekstu", što je i kontrola da popis nije nabujao).

**Napomena za buduće unose:** nova poglavlja i dodaci moraju rabiti jednoredni oblik; ako se u nekom
popisu pojavi crita na početku retka, provjera ga **neće** obuhvatiti — a to je tišina koja izgleda
kao čistoća.

## ZAPIS-001 — dopuna izvora iz *Naturea* i njegovih časopisa (27. 9. 2026.)

Nije ispravak, nego zapis o dopuni: u knjigu je uneseno **dvanaest provjerenih izvora** iz *Naturea*
i časopisa u njegovu portfelju (odjeljak **M** u `referencije/REFERENCE_BASE.md`; puni popis ondje).
Svi su pročitani na primarnom izvoru, a bibliografski su podaci provjereni i u **Crossrefu**
(autori, volumen, stranice, DOI, datumi). Tri najveće dopune nisu citati nego **dokumentirani
slučajevi**: sustav **Robin** (autorstvo koje je preuzeto), **AISI** (provjera koja je glumljena) i
**australski upad** (sankcija koja se pokreće) — ušli su u poglavlja 12.5, 13.6 i 15.3 te u studiju
slučaja (novi slučajevi D i E).

## ZAPIS-002 — dodan sloj srodnih okvira: 4E kognicija, sistemske teorije i ANT (27. 9. 2026.)

Nije ispravak, nego zapis o dopuni koju je zatražio autor: knjizi je nedostajao **teorijski sloj
srodnih tradicija** i reference na kanonska djela. Dodano je:

- **novi dodatak H** (*rukopis/dodaci/dodatak-H-srodni-okviri.md*) — 4E kognicija (Varela, Thompson
  i Rosch; Clark; Clark i Chalmers; Noë; Gallagher; Thompson; Chemero; Menary; Hutto i Myin; Newen
  i sur.; Gibson; Brooks; Wilson; Engel i sur.), sistemske teorije i kibernetika (Wiener; Ashby;
  Bateson; Maturana i Varela; Prigogine i Stengers; Kauffman; Rosen; Capra; Capra i Luisi; Meadows;
  Luhmann) te ANT, teorija asemblaza i prevođenje (Latour; Callon; DeLanda) — sa **tablicom „što se
  preuzima / gdje se razilazi"** i s ishodom da nijedan od tih okvira ne daje **ljestvicu s
  pripisivanjem**, što je jedini dio na koji knjiga polaže pravo;
- **četiri odlomka u poglavljima** koja tim okvirima pripadaju: 1.5 (sistemska linija ljestvice),
  11.5 (4E: modelu od četiriju E pripadaju *ugrađenost* i *proširenost*, ne utjelovljenje),
  12.3 (autopoeza i zatvorenost prema djelotvornoj uzročnosti kao dva kriterija koja model **ne**
  zadovoljava) i 14.3 (Luhmann: društvo se sastoji od komunikacija);
- **33 nove jedinice u bazi referenci** (odjeljak **N**), s DOI-em ondje gdje postoji i s oznakom
  ☑ za kanonska djela bez DOI-a; svi su podaci provjereni u **Crossrefu** 27. 9. 2026.

**Uz to je proširen alat:** `kod/check_lit.py` sada prihvaća i naslov `### Literatura dodatka`, pa
dodatak H nije samo provjeren u smjeru *citat → baza*, nego mu je i popis provjeren prema tekstu
(dosad su dodaci s popisom bili izvan smjera A — ista vrsta tišine kao u ISPRAVKU-013).

## ISPRAVAK-014 — radne godine na naslovima slika i ponavljane „polureference" (27. 9. 2026.)

**Što je bilo:** naslovi generiranih slika ljestvice (`fig_omlcc16.png`, `fig_omlcc_s1`–`fig_omlcc_s3.png`)
nosili su radnu godišnju oznaku **„(Perak 2018; 2019)"** koja **nije referencija** — takve publikacije ne
postoje (odjeljak K baze). Slika je time nosila citat koji se u knjizi ne smije rabiti, a potpisi su to
morali objašnjavati („radna oznaka koja nije valjana referencija"), što je čitatelju šum. Uz to je
puni citat izlaganja stajao **14 puta** u tijelu poglavlja 2, plus u potpisima slika i u sažetku.

**Što je točno:**
1. skripte `figure/izvori/skripte/fig_omlcc16.py` i `fig_omlcc_stage.py` izmijenjene su (naslov bez
   godine i bez citata), a slike su **ponovno generirane** — provjereno čitanjem slike: naslov je
   „OMLCC — 16 levels of ontological complexity"; skripte sada same upisuju u `figure/` repozitorija i
   izlazni direktorij primaju kao argument;
2. iz poglavlja 2 uklonjene su **ponavljane polureference**: atribucija se izriče **na jednome mjestu
   (pogl. 2.1)**, a na svim ostalim mjestima stoji uputa (→ pogl. 2.1);
3. popis literature poglavlja 2 sveden je na kratki oblik `Perak, OMLCC - izlaganja 2017a; 2017b`,
   kakav rabe i ostala poglavlja.

**Zašto izlaganje nije izbrisano posve:** okvir **nije objavljen integralno**, pa je izlaganje jedini
izvor za razradu na šesnaest razina; izbrisati i posljednju uputu značilo bi ostaviti tvrdnju bez
nositelja. Zato je sačuvano **na jednome mjestu, s punim podacima**, a svugdje drugdje zamijenjeno uputom.

## ZAPIS-003 — drugo poglavlje razrađeno: ime okvira, razine i karta knjige (27. 9. 2026.)

Dopuna koju je zatražio autor („što je to OMLCC i zašto ga tako zovemo; više pažnje razinama; povezati
sve više"):

- **novi odjeljak 2.1 „Što je OMLCC: ime, oblik i namjena"** — što je okvir u jednoj rečenici, značenje
  **svake riječi** kratice (*ontološki · model · leksičkih koncepata · konstrukcija*), zašto se u knjizi
  rabi kratica, i **status okvira s načinom citiranja na jednome mjestu** (dosad razasut po poglavlju);
  dotadašnji odjeljak o domenama postao je **2.1.1** (numeracija ostalih odjeljaka nepromijenjena, pa
  se nijedna postojeća uputa u knjizi nije morala mijenjati);
- **podnaslovi 2.2.1–2.2.3** (materijalna, psihološka, društvena domena) radi čitljivosti i navigacije;
- **nova karta „Gdje se koja razina obrađuje u ovoj knjizi"** (u 2.3): za svaku od šesnaest razina —
  tipičan primjer i odjeljci u kojima se mjeri ili opovrgava; to je najkraći put od okvira do primjene;
- **odjeljak 2.6 proširen** trima srodnim tradicijama koje su u knjigu ušle istoga dana (sistemske
  teorije i kibernetika, ANT i asemblazi, Luhmann) s uputama na **dodatak H**;
- popis literature poglavlja 2 proširen s devet jedinica (Ashby, Brdar i sur., Callon, Capra & Luisi,
  DeLanda, Latour, Luhmann, Meadows, Wiener).

## ZAPIS-004 — Dodatak I: formalizacija razina (entiteti, interakcije, zakoni sastavljanja) (27. 9. 2026.)

Dopuna koju je zatražio autor („puna razrada s formalizacijom entiteta i interakcija"):

- **novi dodatak I** (*rukopis/dodaci/dodatak-I-formalizacija-razina.md*): oznake i pravila dobroga
  zapisa (**L_n = (E_n, R_n, P_n)**, relacijska shema *a{E} — [p : r] → b{E}*, mreža N_n, **peterokut
  interakcije** (r, p, arnost, smjer, uvjet dopuštenosti; učinak), **zakon sastavljanja κ_n : N_n ↦
  e_{n+1}{p}**, slaba emergencija, dva testa koja određuju broj razina);
- **tablica potpisa svih šesnaest razina** (E_n, R_n s potpisom, P_n);
- **za svaku razinu** — formalizacija **entiteta**, formalizacija **interakcije** s uvjetom dopuštenosti,
  **zakon sastavljanja**, **kako se čita iz podataka** i **što bi je oborilo** (16 blokova u tri domene);
- **I.6** izvodi četiri posljedice, među njima ključnu: društvene se razine od nižih ne razlikuju po
  složenosti nego po tome što im je **uvjet dopuštenosti priznanje drugoga** — zato se ne mogu izračunati
  iz nižih razina, i zato modelu ne nedostaje razina, nego priznanje koje bi ga obvezalo;
- u poglavlju 2 dodan odlomak „Formalni zapis ljestvice" (u 2.2) i uputa na dodatak I uz tablicu shema
  (u 2.3); uvod, README i plan sada navode dodatke **A–I**.

**Napomena o vrsti tvrdnje:** formalizacija je **autorova i iznosi se prvi put**; ona **ne dodaje** nove
tvrdnje o svijetu, nego zapisuje postojeće. Mjere ostaju u tekstu i u `data/fakti.csv`, s naznačenom vrstom.

## ISPRAVAK-015 — κ-oznake u dodatku I bile mješovito indeksirane (27. 9. 2026.)

**Što je nađeno.** Dok se crtala slika lanca zakona sastavljanja (→ ZAPIS-005), provjerene su sve
formulacije zakona κ u dodatku I. Pokazalo se da su **indeksi bili mješoviti**: dio formulacija
slijedio je definiciju iz I.1 (**κ_n : N_n ↦ e_{n+1}** — mreža razine *n* daje entitet razine *n+1*),
a dio je uzimao mrežu razine *n+1* (npr. *κ₅: gibanja ↦ događaj₇* uz *κ₆: (Σ, ≺) ↦ oznaka₈*).

**Zašto je to bilo ozbiljno.** Formula je obećanje o tome **što se s čime povezuje**. Mješoviti indeksi
ne bi bili vidljivi u čitanju, ali bi slika koja crta lanac tvrdila nešto drugo od teksta — čime pada
pravilo „figura nikada ne smije tvrditi više od teksta".

**Što je učinjeno.** **Svih šesnaest formulacija** prepisano je u jedinstveni oblik **κ_n : N_n ↦ e_{n+1}{p}**,
sačuvana je svaka dosadašnja pojašnjavajuća rečenica, uz to:
- **L1** je izričito označen kao **polazište** (nema prethodne mreže, pa nema ni κ ni ε);
- **iznad razine 16** petlja se **zatvara** (κ₁₆ : N₁₆ ↦ *zajednica kao nositelj*), što nije nova razina.

**Provjera.** Slika I.1 i tri ploče (slike I.2–I.4) sada crtaju točno taj lanac: strelica između razina
*k* i *k+1* nosi **κ_k**. Nalaz je zabilježen ovdje, a ne prešućen: pogreška se ne briše, nego bilježi.

## ZAPIS-005 — Slike I.1–I.4: lanac κ i tri ploče po domenama (27./28. 9. 2026.)

Autor je zatražio sliku lanca („Ajde, lanac"), a zatim i **tri detaljne ploče** po domenama.

- **Slika I.1** (*figure/dijagram-I-1-lanac-kapa.svg/.png*) — lanac zakona sastavljanja κ₁–κ₁₅:
  zmijski raspored (1–8 odozgo prema dolje, 9–16 odozdo prema gore), svaka kućica nosi naziv razine,
  entitet *e_n* i svojstva koja razina donosi; prijelaz 8 → 9 vodoravan; u podnožju zapis
  κ_n : N_n ↦ e(n+1){p} i zatvaranje petlje iznad 16. U tekstu: uvodna rečenica i potpis u **I.1**,
  uputa iz **pogl. 2.2**.
- **Slike I.2–I.4** (*figure/dijagram-I-2-materijalna-domena*, *-I-3-psiholoska-domena*,
  *-I-4-drustvena-domena*, svaka .svg + .png) — **tri ploče po domenama** (1–8, 9–11, 12–16), u kojima
  svaka kućica nosi: entitet *e_n*, **relaciju s arnošću**, **uvjet dopuštenosti**, **učinak**,
  **gdje se čita u podacima** i **što bi razinu oborilo**; strelice nose zakone κ_n, a prijelaz između
  redova vlastitu oznaku. U tekstu: uvodna rečenica i potpis u **I.3, I.4 i I.5**, uputa iz **pogl. 2.2**.

**Kako su provjerene (dvije razine).** (1) **Mjerenjem** — skripta *figure/izvori/skripte/fig_ploce_domena.py*
prije spremanja sama mjeri svaki redak teksta i svaku oznaku κ te prijavi svaki izlazak iz kućice ili
ulazak oznake u kućicu; mjerenje je pokazalo i **stvarnu grešku u rasporedu** (osi nisu ispunjavale
platno, pa „inčne" mjere nisu bile inči) — popravljeno, nakon čega je nalaza **0**. (2) **Čitanjem slike**
— `check_figure_overflow` ove slike ne može mjeriti (nema prepoznatljivih kućica), pa su pregledane okom,
uz ispravke: visina retka sada slijedi veličinu fonta (prije se tekst preklapao), a oznake κ lomljene su
tako da ostanu unutar razmaka među kućicama.

**Vrsta tvrdnje.** Slike **ne dodaju** nove tvrdnje: svaka kućica ponavlja ono što stoji u dodatku I,
i to bez ijedne brojke i bez ijedne referencije (citiranje okvira ostaje na jednome mjestu — pogl. 2.1).

## ZAPIS-006 — Stilski standard (Katičićev glas) i prvo poglavlje kao uzorak (30. 9. 2026.)

Autor: „u prethodnoj knjizi vrlo veliki skok je bio kad sam tražio da se stil pisanja poveže sa
Radoslav Katičić stilom" → standard se ovaj put **zapisuje i mjeri**, a ne izvodi jednokratno.

- **`docs/STIL.md`** — standard proze: osam pravila (naglasak nosi sintaksa, ne masno slovo; rečenica
  kao jedinica argumenta; umetak u zavisnoj surečenici, ne među crtama; popis samo kao aparat; čestice
  rade posao; bez menadžerskoga registra; stega citata i brojki netaknuta; stil ne mijenja sadržaj),
  tablica „što se dira / što se ne dira", pragovi i pet stvarnih primjera prije → poslije.
- **`kod/check_stil.py`** — mjerni alat: gustoća podebljanoga, dužina rečenice, udio kratkih i dugih
  rečenica, „upravo", čestični repertoar, klišeje, popisni redci, umetci među crtama; te
  `--usporedi stara nova` koji dokazuje da citati, godine, brojke, naslovi i upute **nisu izgubljeni**.
- **Poglavlje 1 prepričano** kao uzorak. Mjere prije → poslije:

| mjera | prije | poslije | prag |
|---|---|---|---|
| podebljano (udio riječi) | 11,0 % | **0,6 %** | ≤ 10 % (cilj 5) |
| „upravo" | 14,6 / 10.000 | **2,4 / 10.000** | ≤ 3 |
| čestični repertoar (različitih) | 3 | **5** (dakle, pritom, tek, naime, usto) | ≥ 5 |
| klišeje | 1 („u okviru") | **0** | ≤ 5 u knjizi |
| umetci među crtama | 21,9 / 10.000 | **7,3 / 10.000** | iznimka |
| srednja rečenica | 21,8 | 21,3 | 20–30 |
| \<12 riječi / >40 riječi | 27,0 % / 7,8 % | 27,7 % / 6,8 % | ≥ 18 % / ≤ 14 % |

- **Provjera istovjetnosti sadržaja** (`--usporedi`): citati (autor+godina) **33 → 33**, godine
  **33 → 33**, brojke s jedinicom 1 → 1, upute (→) **13 → 13**; jedina razlika je **preimenovan
  naslov 1.7** („Što razina NIJE" → „Što razina nije", u skladu sa standardom). Nijedan citat,
  brojka ni uputa nije izgubljena.
- **Ostale provjere nakon zahvata:** `check_lit` (544 jedinice / 1.072 citata), `check_fakti --strict`,
  `check_cisto`, `check_links`, `check_refs` — svi prolaze.

**Redoslijed ostaje obvezujući:** stilski prolaz → recenzije → lektura (lektura poslije stila, inače se
plaća dvaput i potvrda pada). Sljedeće: poglavlja 2–16, jedno po jedno, uz mjerenje prije i poslije.

## ZAPIS-007 — Odluka autora: masno slovo ostaje na POJMOVIMA (30. 9. 2026.)

Autor: „Ostavi ovo masno, čini mi se jasnije kad su pojmovi otisnuti masnim slovima, zar ne?" — odluka
je prihvaćena i **ugrađena u standard kao razlika između dviju vrsta masnoga**:

- **podebljan pojam (dopušteno, poželjno):** masno označuje nazivlje — pojam se podeblja kad se uvodi i
  definira te ondje gdje je nositelj tvrdnje (*holon*, *gotovo-razloživost*, *slaba emergencija*,
  *kausalna emergencija*, *kauzalno isključivanje*, *artefakt mjere*, *supervenijencija*);
- **podebljana tvrdnja (zabranjeno):** masno se ne stavlja na cijelu rečenicu ni na zaključak;
  naglasak tvrdnje nose sintaksa, red riječi i čestice.

**Mjerni kriterij u `check_stil.py`** sada razlikuje oboje: ukupno podebljano ≤ 15 % riječi, a
podebljanih odlomaka **dužih od šest riječi** ≤ 10 % svih podebljanih odlomaka (to su „podebljane
tvrdnje"). Poglavlje 1 nakon vraćanja masnoga: **podebljano 3,0 %** (prije zahvata 11,0 %), dugih
podebljanih odlomaka **1,7 %**, uz zadržane sve ostale dobitke („upravo" 2,4/10.000, čestice 5/12,
klišeje 0, umetci među crtama 7,3/10.000).

**Napomena (provjereno u kodu):** kazalo **ne** ovisi o masnom slovu — `kod/kazalo_build.py` gradi ga iz
registra pojmova (`pojmovnik/koncepti.csv`) i baze referenci, pa masno slovo nije uvjet za indeks; ono
služi čitatelju u tekstu i listanju knjige.

## ZAPIS-008 — Ritmički prolaz: kraće rečenice i promjenjiv ritam (30. 9. 2026.)

Autor: „ostavi A… da ima tih kraćih rečenica… da se mijenja ritam i da se dobije na nekom stilskom
osobujnom pristupu." Odluka: masno ostaje na pojmovima (gustoća A), a proza dobiva **ritmički sloj**.

**Pravilo 2 dopunjeno** (docs/STIL.md): ≥ 25 % rečenica kraćih od 12 riječi, ≥ 15 % kraćih od 8 riječi,
≤ 12 % dužih od 40, **nijedan niz dulji od dvije** rečenice s više od 30 riječi, SD dužina ≥ 14,
raznolika otvaranja odlomaka. Praksa: nakon duge objašnjavajuće rečenice kratka koja izvodi.

**Poglavlje 1 (12 ritmičkih zahvata, bez promjene sadržaja):**

| mjera | prije ritma | poslije |
|---|---|---|
| srednja rečenica | 21,3 | **20,1** |
| rečenice < 12 riječi | 27,7 % | **33,8 %** |
| rečenice ≤ 8 riječi | 15,4 % | **20,1 %** |
| rečenice > 40 riječi | 6,8 % | 6,4 % |
| najdulji niz rečenica > 30 riječi | 3 | **2** |
| čestice | 5/12 | **6/12** (+ naprotiv) |
| podebljano | 3,0 % | 3,0 % (pojmovi) |

Kratke rečenice koje su ušle u tekst (izvode, ne ukrašavaju): *To je pretpostavka, ne zakon.* ·
*Ta je poruka nosiva.* · *Izbor je ovdje konstitutivan.* · *Integracija nije zbroj.* ·
*Riječ je o namjerno oskudnoj definiciji.* · *Svojstvo je odabrano s razlogom.*

**Provjera istovjetnosti sadržaja nakon zahvata:** citati 33 → 33, godine 33 → 33, upute 13 → 13;
sve ostale provjere prolaze. Isti postupak primjenjuje se na poglavlja 2–16.

## ZAPIS-009 — Kratka rečenica ne smije biti banalna (30. 9. 2026.)

Autor: „malo su te kratke rečenice prebanalne ponekad." Točna primjedba. U ritmičkome prolazu (ZAPIS-008)
ušlo je pet kratkih rečenica koje su **ocjenjivale** ili **najavljivale**, a nisu nosile informaciju —
dakle bile su ukras. Zamijenjene su kratkim rečenicama koje nose razliku, posljedicu ili kriterij:

| prije (ukras) | poslije (informacija) |
|---|---|
| Riječ je o namjerno oskudnoj definiciji. | **Definicija je oskudna, ali ne i prazna.** |
| Ta je poruka nosiva. | **Opis bi mogao biti i pogrešan; uvjet ne.** |
| To treba reći otvoreno. | **Prigovor time nije riješen.** |
| Svojstvo je odabrano s razlogom. | **Svojstvo mora biti takvo da ga pojedinačni dio ne posjeduje.** |
| Ta sistemska linija ne smije se prešutjeti. | **Ta je linija starija od suvremene rasprave o kompleksnosti.** |

**Pravilo (docs/STIL.md, pravilo 2):** *test brisanja* — ako se kratka rečenica izbriše i ništa se ne
izgubi, ona je ukras. Kratka rečenica smije izreći razliku, posljedicu/uvjet, ime ili mjeru; ne smije
samo ocjenjivati ni najavljivati.

**Mjera:** `check_stil.py` sada broji **„šuplje kratke"** (kratka rečenica koja samo ocjenjuje ili
najavljuje: *važno, ključno, nosivo, vrijedi istaknuti, treba reći, riječ je o…*). Prag je **0**.

**Poglavlje 1 nakon korekcije:** ≤ 8 riječi **20,1 → 19,2 %** (i dalje iznad praga 15 %) · šuplje **0** ·
srednja rečenica 20,1 · SD 20,2 · najdulji niz > 30 riječi 2 · podebljano 3,0 % (pojmovi).
Provjera istovjetnosti: citati 33 → 33, godine 33 → 33, upute 13 → 13.

## ZAPIS-010 — Mjera ritma tjerala je brisanje aparata (3. 10. 2026.)

**Što se dogodilo.** U stilskome prolazu preko 20 datoteka (paralelni radnici) mjera „najdulji niz
rečenica > 30 riječi" računala se i na **popisnim retcima**. Popisni retci ne završavaju točkom, pa ih
je čistač teksta spajao u jednu „rečenicu"; uzastopni dugi retci (falsifikatori, koraci postupka) davali
su lažni niz od 5–9. Radnici su mjeru zadovoljili onako kako je nalagala — **brisanjem oznaka popisa**:
poglavlja 14, 15 i 16 izgubila su sve popisne retke (22→0, 23→0, 12→0), poglavlje 7 pet.

**Kako je uhvaćeno.** Neovisna provjera (`kod/provjeri_stil.py`) ne gleda samo citate i pragove, nego i
**strukturu**: broj popisnih redaka, naslova, slika, tablica i neuravnoteženih markera. Sadržaj je bio
sačuvan (nijedan citat, godina, brojka, naslov ni uputa nije izgubljena), ali je aparat bio razoren.

**Popravak.**
1. `check_stil.py`: svaki popisni redak sada završava rečeničnom granicom, a **niz dugih rečenica mjeri
   se samo na prozi** (`proza(tekst, bez_popisa=True)`). Aparat više ne ulazi u mjeru ritma.
2. `kod/provjeri_stil.py` (nov) — neovisna provjera: mjere + `--usporedi` + struktura, s popisom nalaza.
3. Poglavlja **7, 14, 15, 16 vraćena su iz kopije** (`/tmp/stil-staro/`) i prolaz je ponovljen s izričitom
   ogradom: *aparat je svet i ne dira se*.

**Naučeno.** Mjera koja se može zadovoljiti **uklanjanjem aparata** nije mjera nego zamka. Zato svaka
stilska provjera mora uz pragove vraćati i **strukturnu istovjetnost** — inače se uspjeh plaća sadržajem.

## ZAPIS-011 — Kalibracija pragova ritma i tri slijepe točke mjernoga alata (3. 10. 2026.)

**Pragovi (docs/STIL.md) nakon stvarnih mjerenja:**
- srednja dužina rečenice **najviše 30** riječi; **donja granica je ukinuta** (autor traži kraće
  rečenice, pa kratkoća nije pogreška — dodatak D, obrasci, ima srednju 10,6 i to je ispravno),
- kraćih od 12 riječi **≥ 20 %**, kraćih od 8 riječi **≥ 13 %** i najviše **15 %** rečenica dužih od 40
  riječi (uzorak — poglavlje 1 — daje 33,8 % / 15,3 % / 8,3 %; pragovi su postavljeni znatno niže od
  uzorka da 0,1 postotnoga poena ne tjera na umetanje rečenica bez sadržaja),
- nijedan niz dulji od **dvije** uzastopne rečenice s više od 30 riječi, i to **samo u prozi**,
- „šuplje kratke“ (kratkoća bez informacije) = **0**.

**Tri slijepe točke alata `check_stil.py` (sve tri popravljene, sve tri su pogrešno usmjeravale rad):**
1. popisni retci spajali su se u jednu „rečenicu“ (i kad završavaju zarezom ili točkom-zarezom), pa su
   uzastopni dugi popisni retci davali **lažni niz dugih rečenica** — radnici su ga uklanjali brisanjem
   oznaka popisa. Sada je svaki popisni redak zasebna jedinica, a niz se mjeri samo na prozi.
2. **masni podnaslovi** i **retci popisa literature** („Autor 1997 · Autor 2006 · …“) brojali su se kao
   rečenice: prvi kao „šuplje kratke“, drugi kao goleme rečenice (100+ riječi) koje su kvarile SD i udio
   dugih rečenica.
3. **blokovi koda** ulazili su u prozu (u dodacima B i D), pa su se retci predložaka brojali kao rečenice
   od 40–50 riječi.

**Posljedica koju treba zapamtiti:** mjera koja se može zadovoljiti uklanjanjem aparata nije mjera.
Zato `kod/provjeri_stil.py` uz pragove provjerava i **strukturnu istovjetnost** (popis, naslovi, slike,
tablice, parnost markera), a `kod/vrati_natuknice.py` vraća masno na uvodne natuknice koje su radnici
skinuli (vraćeno 27, samo nedvojbene — dvotočka, upitnik, najava).

## ZAPIS-012 — Stilski prolaz dovršen na svim 27 datoteka (3. 10. 2026.)

**Stanje:** sve 27 datoteka rukopisa prolaze `check_stil.py` (pragovi + struktura + sadržaj).
Knjiga u cjelini: podebljano **16,4 % → 9,2 %** · dugi masni odlomci **13,1 % → 2,4 %** ·
srednja rečenica **23,7 → 20,8** · ≤ 8 riječi **12,0 % → 17,6 %** · < 12 riječi **19,8 % → 27,3 %** ·
> 40 riječi **10,9 % → 6,9 %** · „upravo“ **9,8 → 0,7**/10k · čestični repertoar **3 → 8**/12.

**Mjerljivi dokazi koji prate svaku datoteku:** `kod/check_stil.py --usporedi` (citati, godine, brojke,
naslovi, **prave unutarnje upute**) i `kod/provjeri_stil.py` (struktura: popis, naslovi, slike, tablice,
parnost `**`). Nijedna datoteka nije izgubila nijednu jedinicu sadržaja ni redak aparata.

**Popravci alata u ovome prolazu (svi zbog lažnih nalaza koji su usmjeravali rad na krivo mjesto):**
1. popisni retci nisu rečenice — svaki je jedinica za sebe, a niz dugih rečenica mjeri se samo na prozi;
2. masni podnaslovi, uvodne natuknice i retci popisa literature ne broje se kao rečenice;
3. blokovi koda ne ulaze u prozu;
4. podebljane natuknice (na početku retka ili popisne čestice) ne broje se u „podebljane tvrdnje“;
5. unutarnje upute prepoznaju se po oznaci cilja (→ pogl. 2.3, → dodatak I.1, → Slika I.1, → data/…), a
   lanac pojmova („materijal → informacija → interakcija → komunikacija“) nije uputa.

**Otvoreno za autora (stilsko, ne mjerno):** 43 uvodne natuknice bile su masne u izvorniku; 30 ih je
vraćeno (nedvojbene: dvotočka, upitnik, najava poput „Slučaj A — …“), a 13 deklarativnih („Kompetitor je
ista tablica s obrnutim predznakom.“) ostalo je bez masnoga jer ih pravilo o podebljanim tvrdnjama
zabranjuje. Ako autor želi i njih masne kao natuknice, vraćaju se jednom naredbom
(`kod/vrati_natuknice.py`, uz proširenje filtra).

## ISPRAVAK-016 — Razina 14: četiri ili pet uvjeta (3. 10. 2026.)

**Nalaz (neovisno čitanje):** pogl. **2** izriče *„moraju biti zadovoljena četiri uvjeta"* (adresiranje,
namjera, zajednički artefakt, konvencija), a pogl. **7** i **13** govore o **pet uvjeta** i na petom
(obveza) grade zaključke 13.5–13.6. Karta u §2.3 u retku razine 14 već nosi *obvezu*. Recenzent bi to
našao prvo.

**Ispravak:** pogl. 2 usklađeno na **pet uvjeta** — dodan uvjet **(e) obveza** (izvor se obvezao da će
izraz vrijediti i da snosi posljedicu ako ne vrijedi, → pogl. 7.5), rečenica o distribucijskom opisu
proširena na prvi, treći, četvrti i peti uvjet, i kontrolna lista u §2.4 sada traži **pet** uvjeta.

## ISPRAVAK-017 — Knjiga o vlastitome repozitoriju mora biti točna (3. 10. 2026.)

1. **Putanja slika.** Pogl. 4 i 12 upućivali su na `slike/README.md`, a stvarna je mapa **`figure/`**
   (31 PNG). Ispravljeno na `figure/README.md`; u tablici §4.7 `slike/` (20 PNG) → **`figure/` (31 PNG)**,
   a rečenica o „hrvatskim nazivima" (`kod/`, `slike/`, `data/`) → `kod/`, `data/`, `figure/`,
   `referencije/`, `pojmovnik/`.
2. **Negativni rezultati.** Tekst i `README` datoteke upućuju na `kod/negativni/` i `data/negativni/`,
   a mape nisu postojale. **Stvorene su** (s README-om), pa se tvrdnja o njima može provjeriti.
3. **Pogl. 9 — „Napomena o izvorima".** Na nju se tekst upućuje **dvaput**, a nije postojala. Dodana je
   (word2vec/NIPS, GloVe/EMNLP, Chinchilla/NeurIPS — sve već u `REFERENCE_BASE.md`, bez novih izvora).
4. **Pogl. 10 — urednička bilješka u čitateljskom tekstu** („treba ih onamo unijeti prije nego uđu u koje
   drugo poglavlje") pretvorena je u čitateljsku: *„❓ Nepotvrđeno: … dok se ne upišu, ostaju označene
   kao procjena."*
5. **Legenda za ❓** dodana u uvod (nepotvrđena stavka: tvrdnja bez izvora ili mjerenja; ne rabi se kao
   dokaz i ne citira se).
6. **„Prokletstvo dimenzionalnosti"** bio je u ključnim pojmovima bez ijedne pojave u tekstu; pojam je
   sada imenovan ondje gdje se o njemu govori (§10.5).
7. **Uvod:** pet stupnjeva vodi na *pogl. 4.3*, a tablica 4.3 stoji u **4.4** → uputa proširena na
   *„→ pogl. 4.3–4.4; tablica 4.3"*.

## ZAPIS-013 — Sadržajni prolaz: djelovanje i povezanost (3. 10. 2026.)

**Povod (autor):** „posvetio bih još razjašnjavanju sadržaja knjige — je li dovoljno jasna, je li sve
povezano, jesu li tvrdnje dovoljno objašnjene pravom motivacijom, primjerima, primjenama; ovo ne bi
trebalo biti tek teorijsko djelo, nego jasno i utemeljeno promišljanje koje upućuje na jasnije djelovanje."

**Metoda:** pet neovisnih čitanja (poglavlja 1–16, uvod, zaključak, studija) + provjera svakog nalaza na
izvoru; zatim pet radnika na točno određene zahvate. **Pravilo za svaki dodatak:** izveden je isključivo
iz onoga što poglavlje već tvrdi — **nijedna nova tvrdnja, izvor ni brojka**; aparat (popisi, tablice,
slike, citati, upute, podebljani pojmovi) netaknut.

**Što je dodano:**
- **Praktikum u pogl. 4** (10 koraka s ulazom/odlukom/izlazom + „Ako ne radi" + „Što je izlaz") i
  **pogl. 9** (7 koraka, isti ustroj). Time **svako poglavlje ima praktični blok** (ranije: 4 i 9 nisu imala).
- **„Što to mijenja u praksi"** u pogl. **1, 6, 7, 9 i 11** — 2–4 rečenice o tome što čitatelj radi
  drukčije, što time sprječava i koja je ograda (5/16 poglavlja; u ostalima posljedicu nose praktikum,
  aktivnosti i falsifikacijski blok). Uvod je usklađen: odlomak stoji „ondje gdje nalaz ima neposrednu
  posljedicu za rad".
- **Pogl. 6:** tri konkretna primjera iz mreže straha (leksemi, konstrukcija *od straha*, konstrukcije
  miješanja) i **prediktivni test** u 6.5 s pragom i ishodom koji ga obara.
- **Pogl. 11 (najslabije uklopljeno):** izrečeno nasljeđivanje **11.4 → 12.4**, uvršten dokumentirani
  primjer (AISI, „provjera bez provjeravatelja") u 11.3, odlomak o praksi; i u **13.6** dodana uputa
  **→ 11.4** (pad kriterija PROVJERA).
- **Motivacija nabrajanja:** pogl. 5 (kriterij izbora šest definicija; neposredna posljedica za modele u
  5.6), pogl. 8 (kriterij izdvajanja pet vrsta; po jedna rečenica uz Tomasella, Elder-Vassa, Archera i
  Sawyera; obrazloženje tablice u 8.4), pogl. 12 (test spajanja i razdvajanja primijenjen na pet dodataka).
- **Mjesta provjere uz otvorene stavke:** pogl. 9 (četiri stavke) i pogl. 15 (15-2 do 15-4: „gdje provjeriti",
  a gdje stvarno mjesto ne postoji, izričito „provjera traži novi izvor").

**Mjereni pomak:** proza 99.724 → **102.119** riječi; poglavlja s praktičnim blokom **14/16 → 16/16**;
poglavlja s odlomkom o posljedici za rad 0 → **5**; ulazne upute na pogl. 11 **7 → 8**; karta razina:
ispravljene i upute za razine 4–6 (→ 2.2.1, dodatak I.2) i razinu 9 (→ 2.2.2, 7.7).

**Otvoreno (za odluku autora):** (a) proširiti „Što to mijenja u praksi" na sva poglavlja (sada 5/16 —
proširenje je moguće, ali samo ondje gdje posljedica nije općenita, da se ne uvede prazna proza);
(b) oznaka praktikuma: u pogl. 4 sada je natuknica **Praktikum.** (usklađeno s pogl. 6, 9, 10, 12).

## ZAPIS-014 — Uvod izgrađen od problema (3. 10. 2026.)

**Povod (autor):** „Uzmimo uvod recimo... On nije nadahnjujući, ne uvlači u temu, prekriptično je,
podrazumijeva da čitatelj želi nešto saznati o tome, ili kao da već zna ili razumije. Želim više
problematizacije, presliku rješenja, motivacije i povezivanja na problem."

**Dijagnoza staroga uvoda.** Otvarao je apstrakcijom o tvrdnji („u toj tvrdnji stoji nešto što nije
izrečeno: pretpostavka da postoji ljestvica"), a ne situacijom u kojoj se čitatelj prepoznaje. Nije bilo
problematizacije (zašto je rasprava nerješiva), ni preslike rješenja: čitatelj je do 7. poglavlja morao
vjerovati da odgovor postoji, jer nije vidio kako uopće izgleda.

**Što je učinjeno.** Prvi odjeljak zamijenjen je s četiri nova:
1. **„Pitanje koje se postavlja svakoga dana, a rijetko dobiva odgovor"** — polazi od dva dojma iz
   razgovora s modelom (posao obavljen / nešto izostalo), pa izvodi problem: dvije tvrdnje u optjecaju
   („samo predviđanje" i „razumije") dijele istu prazninu — nijedna ne imenuje mjesto ni kriterij; i
   povezuje ga s odlukama koje se već donose (pripisivanje, pomoć i prepisivanje, što se traži od
   studenta).
2. **„Dva odgovora koja se ne mogu provjeriti"** — odbacivanje i napuhavanje kao dvije pogrešne
   rečenice iz jednoga propusta (→ 14.7); popravak nije treće mišljenje, nego mjesto i kriterij.
3. **„Kako izgleda odgovor koji se može provjeriti"** — **preslika rješenja**: tablica s pet uvjeta iz
   7.5 primijenjena na mjesta mjerenja u transkriptu (13.5) i nalaz u obliku u kojem ga knjiga izvodi
   (14.6: *funkcionalno prisutno* za 12–14, *intrinzično ne*), uz izričito naveden uvjet pod kojim nalaz pada (16.5).
4. **„Što čitatelj odatle dobiva"** — motivacija kao četiri stvari koje se mogu ponijeti.
Uz to: **teza uvoda** preusmjerena s „okvira" na pitanje; naslov staroga prvog odjeljka („Zašto pitanje
„gdje" nije akademsko") zamijenjen; u tablici dijelova dodan stupac **„pitanje na koje dio odgovara"**;
ispravljeno dvostruko nijekanje („ne niječe" → „ne odbacuje").

**Pravilo je nepromijenjeno:** svaka tvrdnja u novim odjeljcima stoji na građi koja je već u knjizi
(7.5, 7.9, 13.4, 13.5, 14.6, 14.7, 16.5); **nijedna nova tvrdnja, izvor ni brojka**. Proza uvoda
2.129 → 2.093 riječi po mjeri (podebljano 10,6 % · ≤8 14,8 % · čestice 5/12 · „upravo" 0 · šuplje 0).

