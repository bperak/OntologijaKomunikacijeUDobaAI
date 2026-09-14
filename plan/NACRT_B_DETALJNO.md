# KNJIGA — VARIJANTA B: DETALJNI NACRT

**Radni dokument v0.3 · 14. rujna 2026. · temelj: predavanje „Elements of Cognition in Complex Language" (IUC Dubrovnik, 11. 9. 2026.)**

---

## 0. Zašto ova knjiga

### 0.1 Pozicioniranje — tri knjige, tri posla
| knjiga | fokus | status |
|---|---|---|
| *Komunikacija u doba umjetne inteligencije* (2025) | **povijest i praksa**: komunikacija + razvoj LLM-a i komunikacijskih agenata | objavljena |
| *Data Science u kulturi* (u izradi) | **kako** raditi s podacima (metode, praktikum) | u izradi |
| **ova knjiga (B)** | **ontološki smještaj**: gdje je jezik, gdje je komunikacija, gdje je model — i što se promijeni kad u sustav uđe novi entitet | nacrt |

**Razlika je u pitanju, ne u temi.** Prva knjiga odgovara *što se dogodilo*; DSK odgovara *kako to izmjeriti*; ova knjiga odgovara **gdje to ontološki stoji**. Zato nema ponavljanja: ista pojava, tri razine apstrakcije.

### 0.2 Tri tvrdnje koje knjiga brani
1. **Razine su operativan okvir, ne metafora.** Ontološke razine (OMLCC: tri domene, 16 razina) definiraju se *relacijskim shemama* i mogu se čitati iz podataka.
2. **Komunikacija je jedna od tih razina (14) — i ujedno metoda.** Ona je istovremeno objekt (društveni čin s namjerom, artefaktom i konvencijom) i instrument (sve ostale razine čitamo iz komunikacijskih podataka).
3. **AI nije 17. razina, nego novi entitet koji ulazi u postojeće razine** — i time mijenja uvjete komunikacije: novi tip sudionika, novi artefakti, nove konvencije, novi protokoli.

### 0.3 Čitatelji
- **primarni:** studenti kulturalnih studija, lingvistike i digitalne humanistike (2.–5. godina + diplomski)
- **sekundarni:** istraživači emergencije, kompleksnosti i AI koji traže ontološki okvir
- **tercijarni:** praktičari (jezične tehnologije, kulturna baština, komunikacija) koji trebaju pojmovni aparat bez matematike

### 0.4 Radni naslovi (odabrati jedan)
1. **Razine i entiteti: ontologija komunikacije u doba umjetne inteligencije**
2. **Od materije do kulturnih modela: šesnaest razina i jedan novi sudionik**
3. **Komunikacija kao razina: jezik, mreže i umjetna inteligencija**
   *(napomena: naslov odlučuje gdje je težište — 1. komunikacija + AI · 2. razine · 3. komunikacija)*

### 0.5 Obim
16 poglavlja × ~6.000–8.000 riječi ≈ **105.000 riječi** + dodaci ≈ **310–330 stranica**.

---

## 1. Arhitektura i konvencije

### 1.1 Makrostruktura
| dio | poglavlja | posao dijela |
|---|---|---|
| **I. RAZINE: OKVIR** | 1–4 | postaviti pojmove: sustav, emergencija, razina, OMLCC, metodologija |
| **II. KOMUNIKACIJA KAO RAZINA** | 5–8 | dokazati da je komunikacija razina, ne alat; razina 14 kao nosivo mjesto |
| **III. AI U SUSTAVU** | 9–12 | od vektorskog prostora do novog entiteta; što model jest, a što nije |
| **IV. KOMUNIKACIJA S NOVIM ENTITETOM** | 13–16 | što se mijenja na razini 14; kultura; posljedice i falsifikacija |

### 1.2 Anatomija svakog poglavlja (sedam blokova)
1. **Teza** — jedan odlomak u kurzivu, tvrdnja koja se u poglavlju dokazuje
2. **Teorijski okvir** — pojmovi, povijest, izričita atribucija tuđih doprinosa
3. **Metode i podaci** — što se mjeri, na kojim podacima, kojim postupkom
4. **Praktikum** — kod korak po korak + odjeljak **„Ako ne radi"** (tri najčešće greške). *Obavezan u poglavljima koja mjere (4, 6, 10, 11, 14); u teorijskim poglavljima (1, 2, 3, 5, 7, 8) na njegovu mjestu stoji **radni primjer** s istim zahtjevom: postupak koji čitatelj može ponoviti.*
5. **Vježbe** — 🟢 provjeri razumijevanje · 🟡 primijeni na vlastite podatke · 🏆 istraživački zadatak
6. **Sažetak i ključni pojmovi** — 10 natuknica koje ulaze u rječnik
7. **Kako bismo znali da griješimo** — falsifikacijski okvir: koji bi rezultat oborio tvrdnju poglavlja

### 1.3 Konvencije i pravila
- **oznake stanja materijala:** ✅ materijal postoji · 🟡 djelomično · ❌ treba napisati od nule
- **brojevi su sveti:** svaka brojka ima izvor, datum i vrstu (**mjereno** ili **procjena**); procjene se nikad ne prikazuju kao mjerenja
- **citat bez rupa:** tvrdnja + citat + izvor u istoj rečenici; nema „vidi literaturu"
- **skromnost tvrdnji:** knjiga ostaje na **slaboj emergenciji** (Bedau 1997), ne na jakoj (Chalmers 2006); model je **kandidat** za novi entitet, ne zaključak
- **terminološka stega:** *entitet* = **gdje** je (pozicija u sustavu) · *agent* = **što radi** (sistemska uloga). Riječ „razina" nikad se ne upotrebljava za model.

---

# DIO I — RAZINE: OKVIR

## 1. Sustavi, cjeline i organizacija — što je razina
**Teza:** razina nije veličina ni količina složenosti, nego **razlika u tipu svojstava** koja proizlazi iz organizacije.

**Stanje materijala:** ✅ (slajdovi 3–5; govor §1; definicije-pojmovi.md)

**Sekcije:**
1.1 Cjelina i dijelovi — sustav kao „kompleks elemenata u interakciji" (von Bertalanffy 1968: 55)
1.2 Slaba emergencija: makrostanje izvedivo iz mikrodinamike, „ali samo simulacijom" (Bedau 1997) — i zašto knjiga ostaje na njoj
1.3 Jaka emergencija: „nije deducibilan ni u načelu" (Chalmers 2006) — što bismo morali pokazati da bismo je tvrdili (i zašto to ne tvrdimo)
1.4 Relativnost svojstva prema razini organizacije (Emmeche, Køppe & Stjernfelt 1997)
1.5 „More Is Different" (Anderson 1972) — zašto zakoni niže razine ne objašnjavaju pojavu
1.6 Što razina **nije**: nije mjerilo veličine, nije vrijednosna ljestvica, nije stupanj složenosti po sebi

**Figure:** ljestvica razina + Andersonov „kolač" (hijerarhija znanosti)

**Vježbe:** 🟢 prepoznaj svojstvo i njegovu razinu u 8 primjera · 🟡 dokaži za jedno svojstvo da nije zbroj svojstava dijelova · 🏆 konstruiraj kandidata za jaku emergenciju i objasni što bi ga oborilo

**Kako bismo znali da griješimo:** ako se svako „više" svojstvo može izvesti iz nižega *bez* simulacije (deduktivno, u zatvorenoj formi), okvir razina gubi posao i knjiga pada na prvoj tvrdnji.

**Obim:** ~6.000 riječi

---

## 2. OMLCC: šesnaest razina ontološke složenosti
**Teza:** ontologiju možemo organizirati u **tri domene** i **šesnaest razina**, pri čemu je svaka razina definirana **relacijskom shemom** (tip entiteta + tip relacije + tip svojstva), a ne popisom primjera.

**Stanje materijala:** ✅ (slajdovi 6–8; fig_omlcc_stage 1–3; Perak 2018 OMLCC; Perak 2019)

**Sekcije:**
2.1 **Tri domene — izričito prema Searleu (1995; 2010):** materijalna (brute facts) · psihološka (mental facts) · društvena (institutional facts). *Podjela domena je Searleova; razrada na šesnaest razina je autorov doprinos — to je u tekstu rečeno na svakom mjestu gdje se pojavi.*
2.2 **Šesnaest razina s definicijama:**
- MATERIJALNO: 1 Existence · 2 Emergence · 3 MaterialStructure · 4 Spatial · 5 Force · 6 Motion · 7 SequenceActivity · 8 InformationSystem
- PSIHOLOŠKO: 9 Perception · 10 Affect · 11 Cognition
- DRUŠTVENO: 12 SocIdentity · 13 SocBehaviourInteraction · 14 SocCommunication · 15 SocCulturalInstitution · 16 CulturalModel
2.3 **Relacijske sheme** — kako se razina operacionalizira: koje relacije moraju postojati da bi nešto bilo *na* toj razini (npr. komunikacija zahtijeva adresiranje, namjeru, zajednički artefakt, konvenciju)
2.4 **Zašto 16, a ne 5 ili 100** — kriterij razlikovanja: promjena tipa svojstva i tipa relacije, ne promjena količine
2.5 **Granice modela** — što OMLCC tvrdi (organizacijska shema) i što ne tvrdi (da su razine „u prirodi" kao takve)
2.6 **Srodni modeli** — Searleove domene, Chalmersova ljestvica, Andersonova hijerarhija: gdje se OMLCC poklapa, a gdje razilazi

**Figure:** ljestvica 1–16 kroz tri domene (fig_omlcc_stage_1/2/3)

**Vježbe:** 🟢 smjesti 20 pojmova na razine i obrazloži · 🟡 nađi pet spornih slučajeva (npr. „emocija u tekstu", „algoritam") · 🏆 predloži reviziju jedne razine i obrani je protiv zamjene

**Kako bismo znali da griješimo:** ako se za predviđanja na novim podacima jednako dobro pokaže **ravni model bez razina**, razine su suvišne i OMLCC pada kao okvir.

**Obim:** ~7.000 riječi

---

## 3. Tri koraka emergencije: PARTS → NETWORK → NEW ENTITY
**Teza:** emergencija nije misterij, nego postupak u tri koraka — dijelovi se organiziraju u mrežu, mreža dobiva nova svojstva, a ta svojstva postaju nova cjelina na višoj razini: **materijal se ne mijenja, mijenja se organizacija.**

**Stanje materijala:** ✅ (slajd 9: PARTS / NETWORK / NEW ENTITY; poanta „The material never changes — only the organisation"; čip Social Communication)

**Sekcije:**
3.1 Korak 1 — dijelovi (što ulazi u sustav; identitet i svojstva dijelova)
3.2 Korak 2 — mreža (relacije; organizacija kao izvor novih svojstava)
3.3 Korak 3 — nova cjelina (kad skup relacija postaje **jedan** nositelj svojstva; i zašto to nije nova *razina*, nego novi *entitet*)
3.4 Radni primjer 1: od zvučnog vala do komunikacijskog čina (materijal → informacija → interakcija → komunikacija)
3.5 Radni primjer 2: od ko-okurencije do konceptualne mreže (priprema za dio II)
3.6 Dijagnostika: kako prepoznati u kojem je koraku neki sustav (i gdje se postupak zaustavlja)

**Vježbe:** 🟢 raščlani tri sustava na tri koraka · 🟡 uzmi vlastite podatke i prođi tri koraka · 🏆 pokaži sustav u kojem treći korak *ne* nastupa i objasni zašto

**Kako bismo znali da griješimo:** ako se pokaže da treći korak uvijek možemo opisati bez uvođenja nove cjeline (samo kao skup relacija), tada je „novi entitet" samo skraćeni zapis i knjiga to mora priznati.

**Obim:** ~6.000 riječi

---

## 4. Kako se razine čitaju iz podataka — metodologija
**Teza:** razine nisu metafizičke tvrdnje, nego **mjerljive hipoteze**: čitamo ih iz komunikacijskih podataka (korpus, ko-okurencija, mreže, konstrukcije, ugrađivanja).

**Stanje materijala:** 🟡 (slajdovi 12, 19–22; govor §3; metode iz DSK knjige — treba ih preformulirati za ovu svrhu)

**Sekcije:**
4.1 **Podaci:** korpusi (hrWac i srodni), leksikoni, anketni i eksperimentalni podaci; što je uzorak, a što populacija
4.2 **Od teksta do mreže:** ko-okurencija, PMI, konstrukcija grafa (čvor = leksem/konstrukcija, veza = mjera asocijacije)
4.3 **Od mreže do vektora:** ugrađivanje (na vlastitom postavu: **Qwen3-Embedding, 4096 dimenzija**, spark-embed.syntagent.com); što dimenzija znači i što ne znači
4.4 **Od vektora do razine:** klasifikacija, klasteriranje, usporedba s ručnom anotacijom; kako se tvrdnja „ovo je razina 14" testira
4.5 **Statistika i etika mjerenja:** veličina uzorka, višestruka usporedba, reproducibilnost, verzije modela i podataka; zašto „isti broj iz iste metode" nije formalnost
4.6 **Kako prijaviti rezultat:** tablica + graf + kod + verzije + zapis neuspjelih pokušaja (negativni rezultati se objavljuju)
4.7 **Repozitorij knjige:** struktura mapa (`/data`, `/code`, `/figures`, `/notebooks`), licence, kako čitatelj reproducira svaku figuru

**Figure:** cjevovod podataka (tekst → mreža → vektor → razina → tvrdnja)

**Vježbe:** 🟢 izračunaj PMI za pet parova · 🟡 izgradi mrežu iz vlastitog korpusa · 🏆 testiraj hipotezu o razini i prijavi i negativan rezultat

**Kako bismo znali da griješimo:** ako mjerenja pokažu da se razlike među razinama gube čim kontroliramo veličinu uzorka i vrstu teksta, tvrdnja o razinama nije empirijska.

**Obim:** ~7.000 riječi

---

# DIO II — KOMUNIKACIJA KAO RAZINA

## 5. Jezik kao emergentna pojava
**Teza:** jezik nije ni sustav znakova ni skup pravila, nego **organizacija uporabe** iz koje se svojstva (značenje, gramatika, konvencija) pojavljuju kao stabilne strukture.

**Stanje materijala:** ✅ (slajdovi 10–11; govor §2; šest definicija jezika)

**Sekcije:**
5.1 **Šest definicija i njihove posljedice** — Sapir 1921 (voljno proizvedeni simboli) · Bloch & Trager 1942 (kooperirajuća skupina) · Chomsky 1957 (konačan skup elemenata) · Saussure 1916 (znak čija je vrijednost razlika) · Halliday 1978 (resurs za stvaranje značenja) · Firth 1957 (riječ među susjedima). **Poanta je nesuglasje, ne konsenzus:** definicija odlučuje gdje značenje stanuje.
5.2 **Saussure:** *langue* kao „sustav čistih vrijednosti" — razlike i sinkronijske solidarnosti
5.3 **Firth i Harris:** uporaba i distribucija (Firth 1957; Harris 1954, *Distributional Structure*)
5.4 **Uporabna gramatika:** konstrukcije kao parovi oblika i značenja koje nasljeđujemo iz ponovljene uporabe (Croft 2001; Goldberg 2006; Perak & Ban Kirigin 2023)
5.5 **Zašto „emergentno" nije „proizvoljno":** stabilnost kroz uporabu, a ne propis
5.6 **Što ovo isključuje:** jezik kao popis pravila i jezik kao privatni mentalni objekt

**Vježbe:** 🟢 za svaku od šest definicija napiši primjer koji joj proturječi · 🟡 usporedi dvije definicije na istom korpusu · 🏆 pokaži konstrukciju koja se stabilizirala u uporabi i dokaži to podacima

**Kako bismo znali da griješimo:** ako se gramatička i leksička svojstva mogu objasniti bez uporabe (bez podataka o uporabi), emergencijski okvir nije potreban.

**Obim:** ~6.500 riječi

---

## 6. Mreže značenja: od ko-okurencije do konceptualne konstrukcije
**Teza:** značenje je relacijsko i mrežno — rekonstruira se iz zajedničke pojavnosti i pretvara u **konceptualnu mrežu**, a mreža je *prikaz* značenja, ne njegov spremnik.

**Stanje materijala:** ✅ (slajdovi 12, 19–20; govor §3; Perak & Ban Kirigin 2023 CGCN; Perak 2014; EmoCNet 2019–21; fig_emotion_network.png)

**Sekcije:**
6.1 Konceptualna mreža: čvorovi, veze, konstrukcije; što je jedinica analize
6.2 Postupak građenja mreže iz korpusa (korak po korak, s pragovima i njihovim posljedicama)
6.3 **Interpretacija mjera:** gustoća, modularnost, centralnost, tranzitivnost — što koja mjera znači i što **ne** znači (najčešća pogreška: mjera se čita kao uzrok)
6.4 **Studija slučaja: emocije** — mreža **125 hrvatskih emocionalnih leksema** sa *strah* u središtu (Perak 2014; EmoCNet 2019–21). Figura: `fig_emotion_network.png` (1618×1456)
6.5 Granice: semantička mreža ne „sadrži" značenje; ona pokazuje strukturu uporabe
6.6 Kako se mreža povezuje s razinama 10 (afekt) i 11 (kognicija) — most prema poglavlju 7

**⚠️ Otvoreno:** točna publikacija u kojoj je mreža *strah* objavljena nije utvrđena — **potvrditi prije pisanja** (inače ostaje citirano kao vlastita figura s metodom).

**Vježbe:** 🟢 interpretiraj tuđu mrežu i nađi tri pogrešna čitanja · 🟡 izgradi mrežu za jedan semantički domen iz hrWac-a · 🏆 usporedi mrežu iz korpusa s mrežom iz ankete i objasni razlike

**Kako bismo znali da griješimo:** ako mrežna struktura ne predviđa ništa izvan podataka iz kojih je izgrađena (nulta prediktivna vrijednost), mreža je samo lijepa slika.

**Obim:** ~7.000 riječi

---

## 7. ★ Komunikacija kao razina 14 — SocCommunication
**Teza:** komunikacijski čin nije prijenos informacije, nego **društveni čin**: zahtijeva prepoznavanje namjere, zajednički artefakt i konvenciju — i zato je komunikacija **razina**, a ne alat.

**Stanje materijala:** ✅ (slajd 9 — čip „Social Communication — OMLCC 14"; slajdovi 28–29; govor §2 i §5; Harris 1954/1957; Searle 1995/2010) · 🟡 **Grice treba dodati u korpus referenci** (Grice 1957, *Meaning*; Grice 1975, *Logic and Conversation*) — nije u sadašnjem popisu predavanja

**Sekcije:**
7.1 **Zašto komunikacija zaslužuje razinu** — primjena kriterija iz poglavlja 2.4 na komunikacijski čin
7.2 **Grice:** značenje kao **prepoznata namjera** (govornik želi da sugovornik prepozna njegovu namjeru *time što je prepozna*)
7.3 **Harris:** komunikacija kao prepoznavanje namjere — što model radi i što ne radi „iznutra"
7.4 **Searle:** statusne funkcije i kolektivna intencionalnost — mjesto gdje informacija postaje **obveza**
7.5 **Anatomija komunikacijskog čina u OMLCC-u:** izvor · primatelj · zajednički artefakt · konvencija · obveza — pet uvjeta koji čine razliku prema razini 8 (informacijski sustav)
7.6 **Mjerenje razine 14 u podacima:** adresiranje, dijaloške oznake, deikse, konvencionalizirani obrasci, obrasci izmjene (turn-taking) — operacionalizacija s pragovima
7.7 **Komunikacija kao metoda:** sve ostale razine čitamo iz komunikacijskih podataka — zato komunikacija nije „još jedna tema", nego *mjesto mjerenja*
7.8 **Granica:** gdje prestaje razina 14 i počinje 15 (institucija)

**Vježbe:** 🟢 označi komunikacijske činove u odlomku i obrazloži svaki · 🟡 izračunaj obrasce adresiranja u korpusu · 🏆 testiraj tvrdnju da konvencija zahtijeva zajedničku obvezu (dizajniraj promatranje ili eksperiment)

**Kako bismo znali da griješimo:** ako se komunikacijski čin može u cijelosti objasniti bez prepoznavanja namjere i bez obveze (čista inferencija iz distribucijskih podataka), razina 14 reducira se na 8 + 13 i nosiva tvrdnja knjige pada.

**Obim:** ~8.000 riječi (najveće poglavlje)

---

## 8. Institucije (15) i kulturni modeli (16)
**Teza:** kad komunikacija stabilizira obveze i imena, nastaju institucije; kad se institucije naslijede kao obrasci tumačenja, nastaje kulturni model — a to je ono što razina 16 znači, i za ljude i za modele.

**Stanje materijala:** ✅ (slajdovi 28–29; govor §6; Searle 1995/2010; Perak 2025)

**Sekcije:**
8.1 **Statusna funkcija:** X broji kao Y u kontekstu C (Searle) — primjeri od novca do „dokumenta"
8.2 **Jezik kao institucija:** imena, naslovi, formule, pravni jezik — gdje jezik djeluje, a ne samo opisuje
8.3 **Kulturni model i nasljeđivanje:** razlika između *učenja iz podataka* i *predaje unutar zajednice koja priznaje*
8.4 **Što se od toga nalazi u modelu** (obrasci, stilovi, žanrovi) **i što se ne nalazi** (zajednička intencionalnost, obveza, odgovornost)
8.5 **Most prema dijelu III:** institucije i kulturni modeli kao uvjeti u koje ulazi novi entitet

**Vježbe:** 🟢 klasificiraj deset statusnih funkcija po kontekstu C · 🟡 nađi u korpusu jezične formule koje djeluju institucionalno · 🏆 oblikuj test za razlikovanje konvencije od obveze

**Kako bismo znali da griješimo:** ako se institucionalni fakti mogu opisati kao puki obrasci uporabe bez obveze i priznanja, razina 15 nije potrebna.

**Obim:** ~7.000 riječi

---

# DIO III — AI U SUSTAVU

## 9. Od vektorskog prostora do modela
**Teza:** model je organizacija statističkih relacija iz komunikacijskih podataka; arhitektura (ugrađivanje + pažnja) pretvara ko-okurenciju u **geometriju**, a geometrija omogućuje operacije koje nalikuju pojmovnim.

**Stanje materijala:** ✅ (slajdovi 13–15; govor §3)

**Sekcije:**
9.1 **Distribucijska hipoteza:** kontekst je značenje (Harris 1954; Firth 1957) — i što ona točno tvrdi, a što joj se pripisuje
9.2 **Prvi vektori:** word2vec (Mikolov et al. 2013) i GloVe (Pennington et al. 2014) — od riječi do koordinata
9.3 **Kontekstualni obrat:** pažnja i transformer (Vaswani et al. 2017); BERT i GPT (Devlin et al. 2018; Radford et al. 2018–19); vektor riječi prestaje biti jedan
9.4 **Što je „parametar", a što „učenje"** — objašnjenje za netehničkog čitatelja, bez matematike, ali bez pojednostavljenja koje iskrivljuje
9.5 **Skala:** zakoni skaliranja (Kaplan et al. 2020) i Chinchilla (Hoffmann et al. 2022) — što je bilo otvoreno i što je zatvoreno
9.6 **Pouka poglavlja:** model nije kopija svijeta, nego **organizacija uporabe** — isti postupak kao u poglavlju 3, samo s drugim materijalom

**Figure:** dijagram: korpus → ko-okurencija → ugrađivanje → pažnja → kontekstualni vektor

**Vježbe:** 🟢 objasni vlastitim riječima razliku između statičkog i kontekstualnog vektora · 🟡 izračunaj srodnost deset pojmova na vlastitom postavu · 🏆 testiraj gdje distribucijski pristup pada (polisemija, ironija, deiksa) i prijavi rezultat

**Kako bismo znali da griješimo:** ako se pokaže da uspjeh modela ne zavisi od organizacije uporabe (npr. da je dovoljna memorija bez strukture), tvrdnja o organizaciji je suvišna.

**Obim:** ~7.000 riječi

---

## 10. Geometrija na djelu — i njezine granice
**Teza:** operacije u vektorskom prostoru daju mjerljive i ponovljive rezultate na stvarnim podacima, ali **geometrija nije pojam**: dobivamo strukturu uporabe, ne značenje samo.

**Stanje materijala:** ✅ (slajdovi 19–22: vlastiti podaci, kontekstni prozor, konceptualna geometrija; fig_scale, fig_scoreboard, fig_context, fig_trillion_club; govor §3)

**Sekcije:**
10.1 **Postupak na vlastitim podacima:** leksemi → vektori (Qwen3-Embedding, 4096 dim) → mjere srodnosti → klasteri; što je ulaz, što izlaz
10.2 **Vizualizacija i ono što vizualizacija skriva** (t-SNE/UMAP): udaljenost u prikazu ≠ udaljenost u prostoru
10.3 **Kontekstni prozor:** 512 → 10 M tokena (×5.000) i cijena konteksta („context rot", Chroma 2025)
10.4 **Veliki brojevi:** „klub 10¹² parametara" — Thompson 2026 (Models Table, LifeArchitect.ai), **procjene**, uz napomenu da ukupni broj uključuje sparse experte i da veličina nije mjera kvalitete
10.5 **Rezultati i stropovi:** GPQA i „Humanity's Last Exam" (GPQA arXiv:2311.12022; HLE arXiv:2602.13964) — rezultati na stropu testa i zašto test prestaje razlikovati
10.6 **Vremenski horizont (METR):** 9 sekundi (2020) → sati (2026); udvostručavanje ~7 mjeseci, 3–4 mjeseca od 2024; **granice mjerenja** (saturacija suite; pomak jednog zadatka mijenja procjenu)
10.7 **Što geometrija ne pokazuje:** referenciju, namjeru, odgovornost; prijelaz na dio IV

**⚠️ Pravilo za cijelo poglavlje:** svaka brojka u tekstu ima izvor, datum i vrstu (mjereno/procjena). Nijedna se procjena ne piše kao mjerenje.

**Vježbe:** 🟢 nađi tri pogrešna čitanja grafa skaliranja · 🟡 ponovi jedan vlastiti rezultat na novoj verziji modela · 🏆 provjeri jednu Thompsonovu procjenu na primarnom izvoru i prijavi razliku

**Kako bismo znali da griješimo:** ako se pokaže da rezultati na stropu testa odražavaju kontaminaciju podacima, dio tvrdnji o „sposobnostima" pada — i knjiga to mora prijaviti kao vlastito ograničenje.

**Obim:** ~8.000 riječi

---

## 11. Mišljenje kao procesiranje: kontekst koji se unaprjeđuje
**Teza:** „mišljenje" u modelu nije skriveni unutarnji prostor, nego **kontinuirano unaprjeđenje konteksta** — od niza tokena do lanca koraka; to je isti proces koji opisujemo kao rezoniranje, ali **bez tvrdnje o fenomenalnom iskustvu**.

**Stanje materijala:** ✅ (slajdovi 22–25; govor §4)

**Sekcije:**
11.1 Od predviđanja sljedećeg tokena do lanca koraka (i zašto je to jedna operacija, a ne dvije)
11.2 **Što mjerimo kad mjerimo „razmišljanje":** vrijeme, broj koraka, točnost, trošak; metrika je izbor, ne činjenica
11.3 **Devijacije:** kolaps modela (Shumailov et al. 2024, *Nature*), pasivna memorija i štetne strategije (Amodei et al. 2016; Krakovna et al. 2020)
11.4 **Tri kriterija razlike između procesiranja i mišljenja:** cilj (postavlja li ga sustav sam), provjera (može li ocijeniti vlastiti ishod), odgovornost (kome se ishod pripisuje)
11.5 Zašto ovo nije ni dualizam ni eliminativizam — treća pozicija: **organizirana kauzalna struktura**
11.6 Kako bi izgledalo da teza pada

**Vježbe:** 🟢 odijeli procesiranje od mišljenja u tri primjera · 🟡 izmjeri jedan zadatak kroz tri metrike · 🏆 dizajniraj test za kriterij „provjere"

**Kako bismo znali da griješimo:** ako se pokaže da lanac koraka ne poboljšava ishod na zadacima koji traže provjeru, „mišljenje kao procesiranje" opisuje samo duži izlaz.

**Obim:** ~6.500 riječi

---

## 12. Novi entitet u sustavu: od modela do agenta
**Teza:** model postaje **entitet** u sustavu kad mu se dodaju djelovanje, pamćenje, dohvat, orkestracija i interoperabilnost; pritom **entitet imenuje *gdje* je, a agent *što* radi** — i to je razlika između pozicije i uloge.

**Stanje materijala:** ✅ (slajdovi 26–27 — mehanika pa teza; fig_agent „candidate new agent"; govor §5)

**Sekcije:**
12.1 **Pet dodataka:** ACTION (izlaz postaje operacija u sustavu) · MEMORY (stanje koje nadživljava sesiju) · RETRIEVAL (svijet uključen u vrijeme rada) · ORCHESTRATION (petlje, delegiranje, podagenti) · INTEROPERABILITY (protokoli)
12.2 **Protokoli kao komunikacijska infrastruktura:** MCP za alate (Anthropic 2024), A2A za agente (Google 2025), AP2/x402 za plaćanja — „vodovod društvenog sloja"
12.3 **Zašto entitet, a ne razina:** model ne dodaje sedamnaestu razinu, nego zauzima postojeće u novom supstratu
12.4 **Kandidat, ne zaključak:** kako bi izgledalo da *nije* entitet i koji bi test to pokazao (kriteriji: trajni identitet, uloga u sustavu, posljedice njegovih akata)
12.5 **Kolaborator i kompetitor:** resursi, jurisdikcija, odgovornost, autorstvo — zašto je „suradnik" tvrdnja, a ne metafora, i gdje ta tvrdnja prestaje

**Figure:** fig_agent (pet slojeva oko modela)

**Vježbe:** 🟢 razluči model i agenta u tri scenarija · 🟡 opiši vlastiti agentni sustav kroz pet dodataka · 🏆 oblikuj test za tvrdnju „ovo je entitet u sustavu"

**Kako bismo znali da griješimo:** ako se pokaže da sve pet dodataka možemo opisati kao pozive funkcija bez ikakvog trajnog identiteta sudionika, „entitet" je suvišan pojam.

**Obim:** ~7.500 riječi

---

# DIO IV — KOMUNIKACIJA S NOVIM ENTITETOM

## 13. Human→agent i agent→agent: što se mijenja na razini 14
**Teza:** novi sudionik ne dodaje razinu, nego mijenja **uvjete** komunikacije: prepoznavanje namjere, zajednički artefakt, konvencije i obveze moraju se iznova urediti.

**Stanje materijala:** ✅ (slajdovi 27–28; govor §5–6; obrasci MCP/A2A)

**Sekcije:**
13.1 **Tri konfiguracije:** čovjek→agent, agent→čovjek, agent→agent — što se u svakoj mijenja
13.2 **Prepoznavanje namjere bez uma** (Harris) — je li namjera prepoznata ili samo simulirana iz obrasca
13.3 **Zajednički artefakt:** memorija, kontekst, radni dokument kao „mjesto susreta"
13.4 **Konvencije i obveze:** mogu li agenti imati zajedničke obveze? (Searle: obveza traži priznanje, ne samo ponašanje)
13.5 **Gdje se razina 14 vidi u praksi:** dijaloški protokol kao mjesto gdje se mjeri komunikacija (adresiranje, izmjena, ispravak, preuzimanje obveze)
13.6 **Neuspjesi komunikacije s novim sudionikom:** nerazumijevanje, lažna suradnja, gubitak konteksta — taksonomija i primjeri

**Vježbe:** 🟢 klasificiraj deset primjera komunikacije po konfiguraciji · 🟡 analiziraj transkript jednog dijaloga s agentom kroz pet uvjeta iz 7.5 · 🏆 dizajniraj mjerenje „prepoznate namjere" u human→agent dijalogu

**Kako bismo znali da griješimo:** ako se ispostavi da komunikacija s agentom ne traži nijednu novu konvenciju (sve se pokriva postojećim protokolima), poglavlje gubi tvrdnju o promjeni.

**Obim:** ~7.000 riječi

---

## 14. Razine 12–16 kod agenata: što vidimo, što ne vidimo
**Teza:** sustavi agenata već pokazuju **funkcionalne parnjake** identiteta, interakcije i komunikacije; institucije i kulturni modeli pokazuju se samo kao naslijeđeni obrasci, **bez zajedničke intencionalnosti**.

**Stanje materijala:** ✅ (slajd 28 — pregled razina 12–16; govor §6; Perak 2018)

**Sekcije:**
14.1 **Identitet (12):** imena, uloge, ključevi, konfiguracije — funkcionalni parnjak
14.2 **Interakcija (13):** protokoli, predaja zadatka (handoff), peer organizacija bez vođe (A2A, MCP)
14.3 **Komunikacija (14):** jezični činovi, artefakti, adresiranje
14.4 **Institucija (15):** pravila i sankcije — postoje li, ili samo pravila bez sankcije?
14.5 **Kulturni model (16):** naslijeđeni obrasci bez zajedništva
14.6 **Zbirna tablica:** razina · funkcionalno prisutno · intrinzično prisutno · nema — s kriterijem za svaki stupac
14.7 **Što to znači za OMLCC:** model kao test okvira (ako okvir ne razlikuje funkcionalno od intrinzičnog, ne vrijedi)

**Vježbe:** 🟢 popuni tablicu za tri agentna sustava · 🟡 nađi primjer „pravila bez sankcije" · 🏆 oblikuj kriterij koji razlikuje funkcionalni parnjak od pravog slučaja

**Kako bismo znali da griješimo:** ako se funkcionalni parnjaci ne mogu razlikovati od „pravih" slučajeva nijednim mjerljivim kriterijem, razlika je verbalna.

**Obim:** ~7.000 riječi

---

## 15. Hoće li imati kulturu?
**Teza:** kultura nije nusprodukt veličine, nego **prijenosa** — pitanje nije „mogu li modeli biti kulturni", nego *mogu li naslijediti i predati obrasce unutar zajednice koja ih priznaje*.

**Stanje materijala:** ✅ (slajd 28/29 „Will they have a culture?"; govor §6; Searle 1995/2010; Perak 2025)

**Sekcije:**
15.1 Što je kulturni model u OMLCC-u (razina 16): obrasci tumačenja koji se predaju
15.2 **Nasljeđivanje bez sudjelovanja:** model uči iz zapisa kulture, ali ne sudjeluje u zajednici koja je proizvodi
15.3 **Tri scenarija:** (a) alat — ostaje izvan razine 16 · (b) sudionik — sudjeluje u komunikaciji i konvencijama · (c) novi sloj — preuzima predaju obrazaca; što je za svaki potrebno
15.4 **Kriteriji:** kolektivna intencionalnost, obveza, prijenos kroz generacije sustava; kako bi se to *testiralo*
15.5 Što bi značilo „kultura modela" za ljude: jezične politike, autorstvo, baština
15.6 Skromnost tvrdnje: kandidat, ne proročanstvo

**Vježbe:** 🟢 razvrstaj tri primjera po scenarijima · 🟡 analiziraj prijenos stila kroz generacije modela · 🏆 dizajniraj eksperiment prijenosa konvencije između agenata

**Kako bismo znali da griješimo:** ako se pokaže da se „kultura" svodi na stilsku reprodukciju bez obveze i priznanja, pojam se mora vratiti na razinu 13–14.

**Obim:** ~6.500 riječi

---

## 16. Što to znači za lingvistiku — i kako bismo znali da griješimo
**Teza:** ako su razine stvarne, lingvistika nije samo opis jezika nego **mjerenje jednog sloja ontologije**; a teorija koja ne može pasti nije teorija, nego pripovijest.

**Stanje materijala:** ✅ (slajdovi 30–33; govor §7; referentna zbirka iz predavanja)

**Sekcije:**
16.1 **Četiri odgovora knjige** (sažetak: što je sustav · što je jezik · što je model · što je mišljenje) — u jednoj tablici
16.2 **Posljedice za lingvistiku:** od opisa prema mjerenju razina; korpus kao ontološki instrument
16.3 **Posljedice za razvoj AI-a:** što bi se promijenilo kad bismo razine uzeli kao projektni kriterij (procjena, ne recept)
16.4 **Zbirna tablica „Kako bismo znali da griješimo"** — po svim poglavljima: tvrdnja · test · što bi je oborilo · tko ju je već pokušao oboriti
16.5 **Istraživački program:** pet eksperimenata koji mogu oboriti ovu knjigu (i tri koja je mogu potvrditi)
16.6 **Zatvaranje:** teza u jednoj rečenici + poziv na provjeru

**Vježbe:** 🟢 napiši vlastiti falsifikacijski test za jedno poglavlje · 🟡 pokušaj oboriti vlastiti rezultat iz poglavlja 6 · 🏆 izvedi jedan od pet eksperimenata

**Obim:** ~6.500 riječi

---

# DODACI

| dodatak | sadržaj | stanje |
|---|---|---|
| **A. Okruženje i alati** | Python, Colab, hrvatski korpusi, Gephi, vlastiti embedding poslužitelj (Qwen3-Embedding 4096-dim); verzije i zamke | 🟡 |
| **B. Rječnik pojmova** | ~45 natuknica (sustav, razina, svojstvo, relacijska shema, emergencija, entitet, agent, konvencija, obveza, ugrađivanje, kontekstni prozor, strop testa…) | ✅ postoji 28 |
| **C. Rješenja vježbi** | sva tri nivoa po poglavlju, s kodom | ❌ |
| **D. Podaci i kod** | struktura repozitorija, licence, verzije skupova, kako reproducira svaku figuru | ❌ |
| **E. Izvori i provjera brojki** | tablica: brojka · izvor · datum · **mjereno/procjena** · veza | 🟡 djelomično (u decku) |
| **F. Prigovori i odgovori** | deset najčešćih: stohastički papagaj (Bender et al. 2021), kineska soba (Searle 1980), symbol grounding (Harnad 1990), Bender & Koller 2020, polisemija, kontaminacija testova, „samo statistika", autorstvo, privatnost, antropomorfizacija | ✅ dijelom (slajdovi 30–31) |
| **G. Kazalo pojmova i imena** | — | ❌ |

---

# MOST PREMA PREDAVANJU (IUC, 11. 9. 2026.)

Predavanje je **pilot cijelog dijela I–IV**: 35 slajdova + **8.594 riječi** govornih bilješki.

| dio knjige | poglavlja | slajdovi predavanja | riječi govora (procjena) | status |
|---|---|---|---|---|
| I. RAZINE: OKVIR | 1–4 | 3–9 | ~2.400 | ✅ kostur |
| II. KOMUNIKACIJA KAO RAZINA | 5–8 | 9–13, 19–22, 28–29 | ~2.300 | ✅ kostur |
| III. AI U SUSTAVU | 9–12 | 13–18, 22–27 | ~2.600 | ✅ kostur |
| IV. KOMUNIKACIJA S NOVIM ENTITETOM | 13–16 | 27–33 | ~1.300 | ✅ kostur |
| referentna zbirka | — | 34 (References) | — | ✅ ~40 referenci |

**Zaključak:** predavanje nije skica knjige — ono je **kondenzat knjige** (≈ 8.600 riječi za 16 poglavlja ≈ 5 % potrebnog teksta). Posao nije istraživanje od nule, nego **širenje u prozu, pedagogiju i vježbe**.

---

# VREMENSKI PLAN (4 mjeseca)

| faza | tjedni | posao | isporuka |
|---|---|---|---|
| **1. Pilot** | 1–3 | DIO I (pogl. 1–3) + **pogl. 7** (komunikacija kao razina 14) | ~28.000 riječi → potvrda tona i dubine |
| **2. Recenzija pilota** | 4 | čitanje, komentari, kalibracija obima i terminologije | odluka: ide li ovako dalje |
| **3. Dio II** | 5–7 | pogl. 5, 6, 8 | ~20.500 riječi |
| **4. Dio III** | 8–10 | pogl. 9–12 | ~29.000 riječi |
| **5. Dio IV + dodaci** | 11–13 | pogl. 13–16 + dodaci A–G | ~27.000 riječi |
| **6. Lektura i prijelom** | 14–16 | lektura, kazalo, provjera brojki, prijelom | rukopis ~310–330 str. |

**Izdanje:** **FFRI Biblioteka** (open access) — u prednosti jer knjiga ima repozitorij, kod i podatke; alternativa: komercijalni izdavač s udžbeničkom linijom.

---

# OTVORENA PITANJA (potrebna odluka)

1. **Naslov** — 1 (komunikacija + AI), 2 (razine) ili 3 (komunikacija kao razina)
2. **Ton** — priručnik / udžbenik / između *(default: između)*
3. **Jezik** — samo hrvatski, ili hrvatski + engleska izdanja/poglavlja
4. **Izdanje** — FFRI Biblioteka open access ili komercijalni izdavač
5. **Referenca figure emocija** — u kojoj je publikaciji mreža *strah* objavljena (potvrditi!)
6. **Grice u referencama** — dodati Grice 1957/1975 u korpus (nedostaje u decku)
7. **Brojevi projekata** — STUDIA, DEMOKRACIJA, FORMALS, AI4LANG (ne izmišljati)

# RIZICI I OGRANIČENJA

| rizik | zaštita |
|---|---|
| **širenje obima** (16 poglavlja × 8.000 = 128.000+ riječi) | pilot prvo; poglavlja s tvrdim proračunom riječi |
| **brojke bez izvora** | svaka brojka u dodatku E; procjena nikad kao mjerenje |
| **ponavljanje knjige 2025** | jasna podjela: povijest/praksa (2025) vs. ontološki smještaj (ova) |
| **pretencioznost** | slaba emergencija; model = **kandidat**; svako poglavlje ima odjeljak „kako bismo znali da griješimo" |
| **terminološka nedosljednost** | stega: entitet = gdje, agent = što radi; rječnik kao kontrolna lista |
| **neprovjerene tvrdnje o tuđim radovima** | atribucija na svakom mjestu; Searleove domene izričito njegove, razine autorove |

---

*v0.3 · izrađeno 14. 9. 2026. · temelj: `KNJIGA_PLAN.md` v0.2 (Varijanta B) + predavanje IUC Dubrovnik 2026.*
