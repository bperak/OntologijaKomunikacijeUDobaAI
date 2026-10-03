#!/usr/bin/env python3
"""Povezanost teksta: paradigmatske, referencijalne i sintagmatske veze (ZAPIS-018).

Mjeri koheziju na razini odlomka po trima vrstama veza:

1. **Referencijalna / sintagmatska natrag** — odlomak je vezan na prethodni ako (a) počinje konektorom
   ili pokaznom riječi, ili (b) mu prva rečenica ponavlja sadržajnu riječ iz posljednje rečenice
   prethodnoga odlomka (leksičko naslanjanje).
2. **Sintagmatska naprijed** — odlomak je vezan na sljedeći ako (a) završava rečenicom koja najavljuje
   posljedicu/uvjet (zato, otud, slijedi, time, posljedica, pa, te), ili (b) se sadržajna riječ iz njegove
   posljednje rečenice ponavlja u prvoj rečenici sljedećega odlomka.
3. **Kauzalni i paradigmatski repertoar** te **konkretnost** (primjer, brojka, ime) po odlomku.

**Izoliran odlomak** = nema ni veze natrag ni veze naprijed. To je mjesto gdje se kauzalni slijed prekida
i gdje čitatelj mora sam pogoditi zašto tekst tu stoji. Alat ispisuje takve odlomke za popravak.

Uporaba:  python3 kod/check_povezanost.py [--datoteka rukopis/poglavlje-07.md] [--strogo] [--isoli]
"""
import os
import re
import sys

KOR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUKOPIS = os.path.join(KOR, "rukopis")

KONEKTOR = re.compile(
    r"^(Ta|Taj|To|Ono|Ova|Ovaj|Ovo|Tim|Time|Toga|Odatle|Iz toga|Zato|Zbog toga|No\b|Ako|Sada|Pritom|"
    r"Ovdje|Tu\b|Uz to|Drugo|Prvo|Treće|Naposljetku|Posljedica|Otud|Stoga|Dakle|Ipak|Ali|Osim toga|"
    r"Sljedeće|Za razliku|Nasuprot|Umjesto|Naprotiv|Kad|Kada|Gdje|Što|Kako|Zašto|Pitanje|Odgovor|Problem|Teza|"
    r"Prvi|Drugi|Treći|Najprije|Zatim|Na kraju|Nakon|Prije|Vrijedi|Njegov|Njezin|Njihov|Isti|Ista|Isto|"
    r"Ponovno|Opet|Svaki|Nijedan|Nema|Postoji|Još|Već|Ako se|Sve|Svako|Svi|Nijedno|Nikad|Uvijek|"
    r"Ova knjiga|Ovaj okvir|Takav|Takva|Takvo|Takve|Takvi|Taj isti|U tome|U tom|Na tome|S tim|Od toga|Do toga|Po tome|"
    r"Iz svega|Iz toga slijedi|Ukratko|Jednom riječju)\b", re.UNICODE)
NAPRIJED = re.compile(r"\b(zato|otud|stoga|dakle|slijedi|posljedic|iz toga|time se|time je|time postaje|"
                      r"pa se|pa je|te se|te je|a time|uvjet je|tek tada|jedino tako|ostaje pitanje|"
                      r"otvara se|vodi k|prelazi u|pokazuje se)\b", re.I)
KAUZALNO = re.compile(r"\b(jer|zato|stoga|dakle|otud|zbog|uslijed|posljedic\w*|slijedi|iz toga|utoliko|"
                      r"proizlazi|uvjetuje|zahtijeva|traži da|omogućuje|omogućava)\b", re.I)
PARADIGM = re.compile(r"\b(nasuprot|naprotiv|umjesto|suprotno|za razliku|razlika prema|razlika je|a ne\b|"
                      r"nije isto|ne znači|tek\b|samo\b|ipak\b|dok\b)\b", re.I)
KONKRETNO = re.compile(r"\b\d[\d.,]*\b|[A-ZČĆŠĐŽ]{2,}|\(\d{4}\)|npr\.|\bprimjer|Slika|tablic")

STOP = set("koji koja koje koje koja kojim kojima koje nego nego tako tada sada ovdje ondje zato jer dakle stoga "
           "biti jesu jest nije nisu bio bila bilo biti može mogu treba valja također također vrlo više manje samo "
           "između prema protiv kroz nakon prije tijekom pomoću sve svi svaka svaki svako njegov njezin njihov"
           .split())


def odlomci(t):
    t = re.sub(r"^>.*$", "", t, flags=re.M)
    t = re.sub(r"^!\[.*$", "", t, flags=re.M)
    t = re.sub(r"^\|.*$", "", t, flags=re.M)
    t = re.sub(r"^```.*?^```", "", t, flags=re.M | re.S)
    t = re.sub(r"^\s*[-*]\s.*$", "", t, flags=re.M)
    t = re.sub(r"^\s*\d+\.\s.*$", "", t, flags=re.M)
    t = re.sub(r"^#.*$", "", t, flags=re.M)
    out = []
    for p in re.split(r"\n\s*\n", t):
        p = re.sub(r"\s+", " ", p).strip()
        if len(p.split()) >= 25:
            out.append(p)
    return out


def reci(p):
    return [r.strip() for r in re.split(r"(?<=[.!?])\s+", p) if r.strip()]


def sadrzajne(tekst):
    return {w.lower().strip(".,;:()»«„\"'") for w in re.findall(r"\b[\wčćšđžČĆŠĐŽ-]{5,}\b", tekst)
            if w.lower() not in STOP}


def analiza(tekst):
    od = odlomci(tekst)
    natrag, naprijed, izolirani = 0, 0, []
    kauz = par = konk = 0
    for i, p in enumerate(od):
        rr = reci(p)
        prva, zadnja = (rr[0] if rr else ""), (rr[-1] if rr else "")
        veza_natrag = bool(KONEKTOR.match(p))
        if not veza_natrag and i > 0:
            prethodni_zadnja = reci(od[i - 1])[-1] if reci(od[i - 1]) else ""
            veza_natrag = bool(sadrzajne(prva) & sadrzajne(prethodni_zadnja))
        veza_naprijed = bool(NAPRIJED.search(zadnja))
        if not veza_naprijed and i + 1 < len(od):
            sljedeci_prva = reci(od[i + 1])[0] if reci(od[i + 1]) else ""
            veza_naprijed = bool(sadrzajne(zadnja) & sadrzajne(sljedeci_prva))
        natrag += veza_natrag
        naprijed += veza_naprijed
        if not veza_natrag and not veza_naprijed:
            izolirani.append(" ".join(p.split()[:16]) + " …")
        kauz += len(KAUZALNO.findall(p))
        par += len(PARADIGM.findall(p))
        if KONKRETNO.search(p):
            konk += 1
    n = len(od) or 1
    return {"odlomaka": n, "natrag": 100.0 * natrag / n, "naprijed": 100.0 * naprijed / n,
            "izoliranih": len(izolirani), "posto_izoliranih": 100.0 * len(izolirani) / n,
            "kauz": kauz / n, "par": par / n, "konk": 100.0 * konk / n, "popis": izolirani}


def main():
    strogo = "--strogo" in sys.argv
    if "--datoteka" in sys.argv:
        dat = [sys.argv[sys.argv.index("--datoteka") + 1]]
    else:
        dat = [os.path.join(RUKOPIS, f) for f in ["uvod.md"] +
               [f"poglavlje-{i:02d}.md" for i in range(1, 17)] + ["zakljucak.md"]
               if os.path.exists(os.path.join(RUKOPIS, f))]
    print(f"{'datoteka':<24}{'odl.':>6}{'natrag%':>9}{'naprijed%':>11}{'izolir.':>9}{'%':>6}"
          f"{'kauz/odl':>10}{'parad/odl':>11}{'konkr%':>8}")
    tot_iz, nalazi = 0, []
    for p in dat:
        a = analiza(open(p, encoding="utf-8").read())
        print(f"{os.path.basename(p):<24}{a['odlomaka']:>6}{a['natrag']:>9.0f}{a['naprijed']:>11.0f}"
              f"{a['izoliranih']:>9}{a['posto_izoliranih']:>6.0f}{a['kauz']:>10.1f}{a['par']:>11.1f}{a['konk']:>8.0f}")
        tot_iz += a["izoliranih"]
        if a["posto_izoliranih"] > 20:
            nalazi.append(f"{os.path.basename(p)}: {a['posto_izoliranih']:.0f}% izoliranih odlomaka")
    print(f"\nukupno izoliranih odlomaka: {tot_iz}")
    print("\n=== NALAZI (prag: >20 % izoliranih) ===")
    print("\n".join("  ⚠ " + n for n in nalazi) if nalazi else "  nema nalaza")
    if "--isoli" in sys.argv or "--datoteka" in sys.argv:
        for p in dat:
            a = analiza(open(p, encoding="utf-8").read())
            if a["popis"]:
                print(f"\n--- izolirani odlomci: {os.path.basename(p)} ({len(a['popis'])}) ---")
                for o in a["popis"]:
                    print("  •", o)
    return 1 if (nalazi and strogo) else 0


if __name__ == "__main__":
    sys.exit(main())
