# STIL — standard proze za knjigu „Razine i entiteti"

**Zašto ovaj dokument postoji.** U prethodnoj je knjizi velik skok u kvaliteti došao kada je autor
zatražio da se stil pisanja veže uz prozu **Radoslava Katičića** — hrvatsku znanstvenu prozu u kojoj
**jasnoća nosi težinu**, a naglasak se postiže **sintaksom i redom riječi**, ne tipografijom. Taj je
zahvat tada izveden jednokratno i nigdje nije zapisan, pa se ovdje **zapisuje kao standard** s mjerama,
da bude ponovljiv — u ovoj knjizi, u sljedećima i kod vanjskoga lektora.

Mjerni alat: `kod/check_stil.py`. Mjeri se **prije i poslije** svakoga zahvata.

---

## 1. Temeljna pravila

1. **Dvije su vrste masnoga, i samo je jedna dopuštena.**
   - **Podebljan POJAM — dopušteno i poželjno.** Masno slovo označuje **nazivlje**: pojam se podeblja
     kad se uvodi i definira te na mjestima gdje je nositelj tvrdnje (*holon*, *gotovo-razloživost*,
     *slaba emergencija*, *kauzalno isključivanje*, *artefakt mjere*). Tako čitatelj vidí gdje se
     uvodi termin, a tisak dobiva sidrišta za listanje.
   - **Podebljana TVRDNJA — zabranjeno.** Masno se **ne** stavlja na cijelu rečenicu, na tvrdnju ni na
     zaključak („**postoje cjeline čije se ponašanje ne može pročitati iz popisa dijelova**"). Naglasak
     tvrdnje nosi sintaksa, red riječi i čestica; podebljana tvrdnja je žvakana misao.
   - **Pragovi:** ukupno podebljano **≤ 15 %** riječi (cilj 5–10 %, jer pojmovi su česti), a podebljanih
     odlomaka **dužih od šest riječi ≤ 10 % svih podebljanih odlomaka** (`check_stil.py` to mjeri
     odvojeno). Stanje prije zahvata: 44,5 % riječi, s brojnim podebljanim rečenicama.
2. **Rečenica je jedinica argumenta, a ritam je dio tvrdnje.** Srednja dužina **20–30 riječi**, uz:
   - najmanje **25 %** rečenica kraćih od 12 riječi i najmanje **15 %** kraćih od 8 riječi — kratka
     rečenica nosi tvrdnju, nije ukras;
   - najviše **12 %** rečenica dužih od 40 riječi;
   - **nijedan niz dulji od dvije** uzastopne rečenice s više od 30 riječi — ritam se mora mijenjati;
   - raznolikost dužina (standardna devijacija ≥ 14) i **raznolika otvaranja odlomaka** (odlomak se ne
     otvara tri puta istim veznikom).

   **Praksa koja daje osobujnost.** Nakon duge objašnjavajuće rečenice dolazi kratka koja izvodi; tvrdnja
   se izriče, pa se kratko zaključi. Primjeri iz poglavlja 1: *To je pretpostavka, ne zakon.* ·
   *Integracija nije zbroj.* · *Ta je poruka nosiva.* · *Riječ je o namjerno oskudnoj definiciji.* ·
   *Izbor je ovdje konstitutivan.* Duga rečenica smije biti duga zbog **zavisnih surečenica**, a ne zbog
   nizanja umetaka među crtama.

   **Kratka rečenica mora nositi informaciju.** *Test brisanja:* ako se kratka rečenica izbriše i pri
   tome se **ništa ne izgubi**, ona je ukras i briše se. Kratka rečenica smije raditi jedno od četiriju:
   (a) izreći **razliku** — *To je pretpostavka, ne zakon.* · *Integracija nije zbroj.*; (b) izreći
   **posljedicu ili uvjet** — *Prigovor time nije riješen.* · *Opis bi mogao biti i pogrešan; uvjet ne.*;
   (c) **imenovati** pojam ili mjeru; (d) izreći **vrijeme, broj ili mjesto**. Zabranjeno je da samo
   **ocjenjuje** (*Ta je poruka nosiva.* · *To je važno.*) ili **najavljuje** (*To treba reći otvoreno.* ·
   *Vrijedi istaknuti…*). Takve se broje kao „šuplje kratke" i moraju biti **0**.
3. **Umetak se ne piše crtama, nego zavisnom surečenicom.** Par crta (— … —) u sredini rečenice je
   iznimka (do nekoliko puta u poglavlju), a ne ritam. Gdje umetak objašnjava, ide **naime**; gdje
   suprotstavlja, ide **pak**; gdje dopunjuje, **usto** ili **pritom**.
4. **Popis je aparat, ne proza.** Popisi i tablice dopušteni su za: kriterije i mjerila, postupke
   (koraci), falsifikatore („Kako bismo znali da griješimo"), vježbe i rješenja, sažetak i ključne
   pojmove. **Argument se piše tekućom rečenicom**; popis ne smije zamijeniti izlaganje.
5. **Čestice rade posao.** Repertoar: *naime, dakle, pak, usto, pritom, otud, naprotiv, štoviše,
   dakako, napose, zacijelo, tek*. Svaka se rabi **s mjerom** (orijentir: 1–3 pojavnice na 10.000
   riječi). „**Upravo**" nije pojačalo — cilj **ispod 3 na 10.000** (stanje prije zahvata: 9,9).
6. **Bez menadžerskoga i novinarskoga registra.** Zabranjeno: *implementirati, fokusirati se, adresirati*
   (u engleskome smislu „rješavati pitanje"), *procesuirati, validirati, optimizirati, bazirano na,
   feedback, trend, platforma* (kad nije naziv), *u okviru, u kontekstu, s ciljem, kroz prizmu, na kraju
   krajeva, igra ključnu ulogu, neizostavan*. (Mjeri `check_stil.py`; iznimka: **adresiranje** kao
   naziv razine 14 — to je termin, ne kliše.)
7. **Stega citata i brojki ostaje netaknuta.** Tvrdnja + citat + izvor **u istoj rečenici**; brojka s
   vrstom (mjereno · procjena · izvedeno). Stilski zahvat **ne dira** ni jedan citat, brojku, uputu
   („→ pogl. X.Y"), naslov, potpis slike ni tablicu.
8. **Stilski zahvat ne mijenja sadržaj.** Ne dodaje i ne oduzima tvrdnje. Ako se pri prepisivanju
   izgubi ijedna tvrdnja, to je pogreška zahvata — i provjerava se **usporedbom citata i brojki**
   prije i poslije (vidi §5).

## 1a. Pravilo 3 — izričaj (ZAPIS-022, autorova korekcija 3. 10. 2026.)

Autor: **„To nije jasno na što se odnosi i banalizira izričaj"** (o tezi uvoda).

1. **Pokazna zamjenica mora imati imenicu.** Ako rečenica tvrdi nešto s „to", „ovo", „ono" ili „time",
   imenica na koju se veže mora stajati u istoj ili prethodnoj rečenici. Ako je nema, zamjenica se
   zamjenjuje imenicom. ⛔ Zabranjeno: „uzima *to* pitanje ozbiljno" kad pitanje u tekstu nije izrečeno
   imenicom.
2. **Nijedna rečenica ne smije biti fraza.** Izrazi koji zvuče odlučno, a ne tvrde ništa (uzeti ozbiljno,
   igra ključnu ulogu, na pragu, nije slučajno, mijenja pravila igre, u suštini) zamjenjuju se tvrdnjom.
   Mjera: `kod/check_izricaj.py` — prag **0** floskula, uz iznimke koje se navode u `docs/ISPRAVKE.md`.
3. **Teza uvoda mora reći dvije stvari imenom:** što nedostaje i što knjiga daje. Bez toga je teza
   najava, a ne tvrdnja.

## 1b. Pravilo 4 — lepršavost i učvršćivanje (v2, nakon vanjske recenzije 3. 10. 2026.)

Autor: **„Još uvijek mi nedostaje lepršavosti i učvršćivanja teme i posljedica, nekako je još uvijek rigidno."**
Recenzenti: GPT-5.6 Sol Pro i Gemini 3.1 Pro (prvi krug) te GPT-6.1 Sol Pro, Gemini Pro i Claude Opus 5.5 (drugi krug).

**Uzrok krutosti nije duljina rečenice, nego polemički stav:** tvrdnja se iznosi kao odgovor na prigovor koji
čitatelj još nije postavio, pa tekst zvuči kao niz prigovora i odgovora. Dopunski uzroci (drugi krug):
tekst komentira vlastito izlaganje („tablica je najpoštenija forma"); apstraktne imenice nose radnju i
zaklanjaju aktere; previše je slikovnih izraza za različite logičke odnose; neke tvrdnje imaju nejasan
doseg; autor katkad prerano zatvara pitanje.

**Sedam pravila (v2 — prva četiri ispravljena prema recenziji):**

1. **Nosiva tvrdnja prije ograde.** Najprije iznesi tvrdnju, pa je ogradi. Negaciju zadrži kad određuje
   doseg ili razdvaja pojmove koje čitatelj lako zamjenjuje (razlika prijenos poruke / prijenos odgovornosti
   takvo je mjesto). ⛔ Nije cilj ukloniti sve antiteze: cilj je spriječiti njihovo **nizanje**.
2. **Ne izgovaraj svaku logičku vezu — ali ne uklanjaj sve.** Izostavi konektor kad je odnos jednoznačan iz
   poretka; zadrži ga kad razlikuje uzrok, uvjet, suprotnost ili zaključak. ⛔ Uklanjanje svih „jer" i „zato"
   daje odsječan niz — to je nova krutost, samo kraćih rečenica.
3. **Jedna tematska putanja po odlomku** (ne „jedan subjekt"): odlomak smije prijeći sa sustava na čovjeka i
   na ustanovu, ali prijelaz mora biti razumljiv iz odnosa koji se opisuje.
4. **Završetak odlomka obavlja posao:** zaključi, pokaže posljedicu, odredi granicu ili otvori sljedeće
   pitanje. ⛔ Sažetak nije obvezan — obvezna završna rečenica u svakom odlomku daje jednoličnost.
5. **Opis prije procjene.** Najprije pokaži što sustav radi, zatim procijeni ontološki status toga.
6. **Kratka rečenica mora imati posao:** razjasniti odnos, promijeniti tempo ili istaknuti posljedicu.
7. **Terminološka stega i u prozi:** razlikuj *falsifikaciju*, *opovrgavanje pojedine tvrdnje* i *obaranje
   knjige*; razluči što znači *potvrditi* (potpora u određenom testu ili potvrda teorije).

**Učvršćivanje teme i posljedica nije formula — to je raspored funkcija:**

| mjesto | posao |
|---|---|
| početak odjeljka | odrediti predmet: koje se pitanje sada rješava i što ostaje isto |
| unutar odlomka | držati nit: radnja → uvjet njezina tumačenja → raspodjela posljedice |
| gdje nalaz mijenja zaključak | imenovati posljedicu (klasifikacija · kriterij pripisivanja · raspodjela odgovornosti · način provjere) — smije otvoriti sljedeći odlomak |
| kraj odjeljka | zatvoriti lokalno pitanje (rezultat usporedbe, a ne prepričavanje) |
| kraj poglavlja | što je ustanovljeno · koliki je doseg · što sada treba provjeriti |

**Praktičan postupak (interni, ne u tekstu):** uz svaki odjeljak napiši rečenicu „Nakon ovoga čitatelj može
zaključiti…". Ako se ne može napisati, problem je strukturni; ako može, ne mora se doslovno pojaviti u rukopisu.

**Mjere:** `kod/check_leprsavost.py` (antiteza ≤ 6/1.000, konektor na početku ≤ 6 %) — oba su čuvari, a ne
ciljevi: ⛔ brojenje nalazi **mjesta za pregled**, ne daje presudu („dok" može značiti vrijeme, antiteza može
nositi nužnu razliku).

## 2. Što se dira, a što ne

| dira se | ne dira se |
|---|---|
| sloj rečenice i odlomka | terminologija (*razina, entitet, adresiranje, holon*) |
| gustoća podebljanoga | aparat (kriteriji, falsifikatori, vježbe, sažetak) |
| umetci među crtama | citati, brojke, upute, naslovi, potpisi slika |
| klišej i nominalne fraze | struktura poglavlja i redoslijed odjeljaka |
| izbor čestica i veznika | popisi koji su doista aparat (koraci, mjerila) |

## 3. Mjere (`kod/check_stil.py`)

| mjera | prag |
|---|---|
| podebljano ukupno (udio riječi) | ≤ 15 % (cilj 5–10 %: pojmovi) |
| podebljani odlomci duži od 6 riječi (udio svih podebljanih odlomaka) | ≤ 10 % (podebljane tvrdnje = 0) |
| srednja dužina rečenice | 20–30 riječi |
| rečenice kraće od 12 riječi | ≥ 25 % |
| rečenice kraće od 8 riječi | ≥ 15 % |
| niz uzastopnih rečenica dužih od 30 riječi | ≤ 2 |
| raznolikost dužina (SD) | ≥ 14 |
| „šuplje kratke" rečenice (kratkoća bez informacije) | 0 |
| rečenice duže od 40 riječi | ≤ 14 % |
| „upravo" | ≤ 3 / 10.000 |
| čestični repertoar (različitih čestica ≥ 0,5 / 10.000) | ≥ 5 |
| klišeji i menadžerski registar (ukupno u knjizi) | ≤ 5 |
| popisni redci (ukupno u knjizi) | ≤ 280 (stanje prije: 491) |

## 4. Primjeri (iz poglavlja 1)

| prije | poslije |
|---|---|
| „…počinje jednim gotovo banalnim uvidom: **postoje cjeline čije se ponašanje ne može pročitati iz popisa njihovih dijelova.**" | „…počinje jednim gotovo banalnim uvidom: postoje cjeline čije se ponašanje ne može pročitati iz popisa njihovih dijelova." *(podebljana tvrdnja → obično)* |
| „Koestler je za istu činjenicu predložio riječ *holon*." | „Koestler je za istu činjenicu predložio riječ **holon**." *(podebljan pojam → dopušteno)* |
| „Ta arhitektura nije estetski ukras — ona je razlog zašto složeni sustavi uopće mogu nastati i opstati." | „Ta arhitektura nije estetski ukras, nego razlog zašto složeni sustavi uopće mogu nastati i opstati." |
| „**Prvo**, razina nije klasa stvari, nego **klasa svojstava i relacija**." | „Najprije, razina nije klasa stvari, nego klasa svojstava i relacija." |
| „Upravo zato Simonova „gotovo-razloživost" nije samo tehnički pojam…" | „Zato Simonova „gotovo-razloživost" nije samo tehnički pojam…" |
| „…pa ostaje u okviru slabe emergencije…" | „…pa ostaje u domeni slabe emergencije…" |

## 5. Kako se zahvat izvodi (i kako se provjerava)

1. **Mjerenje prije:** `python3 kod/check_stil.py` — zapiši brojke za poglavlje.
2. **Prepisivanje poglavlja** po pravilima §1; aparat (§4) ostaje, argument se piše u tekućoj prozi.
3. **Provjera istovjetnosti sadržaja:** usporedba **skupova citata, brojki, naslova i uputa** prije i
   poslije (skripta `kod/check_stil.py --usporedi stara.md nova.md`); ijedan izgubljen citat = zahvat se
   vraća.
4. **Mjerenje poslije:** `check_stil.py` + `check_lit.py` + `check_fakti.py --strict` + `check_cisto.py`
   + `check_refs.py`.
5. **Zapis:** brojke prije/poslije u `docs/ISPRAVKE.md` (ZAPIS).
6. **Lektura dolazi poslije stilskoga zahvata** — inače se posao plaća dvaput, a potvrda o lekturi pada
   na tekstu koji se poslije mijenja.

## 6. Uzori za glas (radi provjere, ne za citiranje)

Katičićev glas u ovome standardu znači: **tvrdnja se izriče pa dokazuje**; pojmovi se uvode prije
uporabe; suprotstavljanje je izrečeno (*pak, naprotiv, štoviše*); objašnjenje je uvedeno (*naime*);
posljedica je izvedena (*otud, dakle*); pojmovna razlika se ne izriče pridjevom, nego surečenicom.
Ne oponaša se Katičićev predmet ni njegov rječnik — **preuzima se disciplina rečenice.**
