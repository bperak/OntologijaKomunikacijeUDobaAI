# Dodatak D — Predlošci

Ovi predlošci nisu ukras ni administracija: oni su **oblik u kojemu se nalaz drži provjerljivim**. Knjiga ih navodi u praktikumima i u vježbama 🟡; ovdje su na jednome mjestu, u obliku koji se može kopirati i ispuniti. Svaki predložak ima dva dijela: **što se upisuje** i **što se ne smije preskočiti** — jer se gotovo svaka pogreška u mjerenju na kraju svodi na jedno preskočeno polje.

Redoslijed je isti kao slijed knjige: prvo podaci (D.1), potom mjere (D.2, D.4), pa test (D.3), pa zapisi o brojkama (D.5) i o razlučivanju razina (D.6).

---

## D.1 Predložak: korpusni upit

```
izvor (korpus):            <naziv, inačica, licenca>
datum pristupa:            <gggg-mm-dd>
upit (upitnik):            <točan izraz, uključujući filtre>
jedinica analize:          <lema | oblik | konstrukcija | replika>
broj pojavnica:            <broj>  ← uz njega obavezno kontrolni zbroj popisa
način provjere:            <skripta/datoteka | ručni pregled N primjera>
```

**Što se ne smije preskočiti:** inačica korpusa (bez nje se ne zna što je bilo na ulazu) i **kontrolni zbroj** popisa jedinica. Ako se popis promijenio između dvaju mjerenja, usporedba mjeri popis, a ne pojavu (→ pogl. 10.7).

## D.2 Predložak: evaluacija ugrađivanja

```
model:                     <naziv i verzija, npr. Qwen3-Embedding>
dimenzija:                 <broj>            ← mjerena činjenica o modelu, ne o jeziku
ulaz (linija):             <gola lema | prosjek pojavnica | rečenica>
normalizacija:             <L2 | nema>
mjera srodnosti:           <kosinus | skalarni produkt | euklidska>
raspon srodnosti:          <najniža … najviša>   ← dijagnostika sabijanja u visokoj dimenziji
broj skupina (k), prag, sjeme:  <vrijednost>     ← zapisuje se PRIJE gledanja rezultata
stabilnost:                <promjena pripadnosti pri drugom sjemenu / poduzorku / verziji modela>
```

**Što se ne smije preskočiti:** verzija modela i raspon srodnosti. Bez raspona se ne vidi je li mjera uopće razlučila jedinice; bez verzije se nalaz ne može ponoviti ni provjeriti je li o jeziku ili o jednome modelu (→ pogl. 10.6, 10.7).

## D.3 Predložak: protokol kauzalnog testa

```
tvrdnja koja se testira:   <jedna rečenica>
zahvat (intervencija):     <što se mijenja>
očekivani učinak:          <što bi trebalo porasti/pasti>
kontrole:                  <koje su i čime se mjere>
prag padanja:              <broj ili uvjet ispod kojega tvrdnja PADA>   ← upisuje se unaprijed
vrsta dokaza:              mjereno | procjena | izvedeno
negativan nalaz:           <kako će se prijaviti ako učinka nema>
```

**Što se ne smije preskočiti:** **prag padanja upisan prije podataka**. Ako se prag upiše nakon što su podaci viđeni, nalaz prestaje biti oboriv i postupak se pretvara u traženje potvrde (→ pogl. 16.5).

## D.4 Predložak: obrazac za mrežnu analizu

```
jedinica:                  <lema | oblik | konstrukcija>
mjera asocijacije:         <frekvencija | PMI | log-omjer>
prag i pravilo filtra:     <vrijednost + pravilo (npr. izbacivanje funkcijskih riječi)>
veličina mreže:            <broj čvorova, broj bridova>
gustoća / modularnost:     <broj>
broj skupina i metoda:     <algoritam + odluka o broju skupina>
robusnost:                 <kako se mijenja nalaz pri promjeni praga i mjere>
raspored na slici:         <siloviti | kružni>   ← položaj na slici NIJE udaljenost u značenju
```

**Što se ne smije preskočiti:** usporedba gustoće među mrežama različitoga broja čvorova (traži korekciju) i **oznaka da raspored na slici proizlazi iz algoritma crtanja**; slika je kazalo, a ne mjera (→ pogl. 6.5, 10.6).

## D.5 Predložak: zapis o brojci

Upisuje se u `data/fakti.csv` (jedan redak po brojci, koji se dijeli među svim trima knjigama):

```
id, brojka, jedinica, izvor, datum_izvora, vrsta, pojavljuje_se_u, napomena
```

- **vrsta:** `mjereno` | `procjena` | `izvedeno` — nikad prazno;
- **izvor:** autor, godina i mjesto objave (ili naziv podatkovnog skupa i inačica);
- **datum_izvora:** datum na koji se vrijednost odnosi (ne datum kada je knjiga pisana);
- **pojavljuje_se_u:** poglavlja u kojima se brojka rabi.

**Što se ne smije preskočiti:** vrsta i datum. Brojka bez vrste je dojam, a brojka bez datuma se ne može ni provjeriti ni ispraviti — a predmet knjige mijenja se brže od knjige (→ dodatak E).

## D.6 Predložak: zapisnik razlučivanja razina

Za razlučivanje funkcionalnoga parnjaka od intrinzičnoga (→ pogl. 14.6, 14.7):

```
sustav i verzija:          <naziv i verzija konfiguracije>
datum provjere:            <gggg-mm-dd>
dostupni zapisi:           <konfiguracija | dnevnik | transkript | stanje koje nadživljuje sesiju>
razina 12: funkcionalno <da|ne> · intrinzično <da|ne|nije provjereno> · dokaz: <mjesto>
razina 13: …
razina 14: …
razina 15: funkcionalno <da|ne|djelomično> · intrinzično <da|ne|nije provjereno> · dokaz: <mjesto>
razina 16: …
izvedena provjera za svaki „ne":  <što je promijenjeno i što je promatrano>
zapis koji nije bio dostupan:     <što>
```

**Što se ne smije preskočiti:** uz svaki odgovor „ne" mora stajati **izvedena provjera** (što je promijenjeno — polje u konfiguraciji, orkestracija, sadržaj poruke) i zaseban ishod **„nije provjereno"**. Bez toga se dokaz odsutnosti zamjenjuje odsutnošću dokaza (→ pogl. 14.6).

## D.7 Kako se predlošci koriste u nastavi

Predlošci su namijenjeni tome da student prvo ispuni predložak, a tek onda piše tekst. Iskustvo s ovakvim obrascem je jednoznačno: najveći dio pogrešaka nastaje na mjestima koja predložak izričito traži, a izostavlja ih svaki slobodni tekst — inačica podataka, mjera, prag, upisan prije podataka, i način na koji je negativan nalaz prijavljen. Zato se u ocjenjivanju vježbi 🟡 i 🏆 predložak smatra dijelom rješenja, a ne obrascem koji se ispunjava uz njega.
