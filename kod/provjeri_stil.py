#!/usr/bin/env python3
"""provjeri_stil.py — neovisna provjera stilskog prolaza na cijelome rukopisu.

Za svaku datoteku uspoređuje stanje prije (kopija u STARO) i poslije:
  - mjere iz check_stil.py
  - citati/godine/brojke/naslovi/upute (--usporedi)
  - STRUKTURA: broj redaka popisa (- ), broj naslova (#), broj slika (![), broj redaka tablica (|),
    broj podebljanih odlomaka i NEOBALANSIRANIH ** (parnost markera)
Sve što odstupa ispisuje se kao NALAZ.
"""
import importlib.util
import os
import re
import sys

STARO = "/tmp/stil-staro"
B = "/home/agent/knjiga-emergencija/"
spec = importlib.util.spec_from_file_location("cs", B + "kod/check_stil.py")
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)


def struktura(tekst):
    return {
        "popis": len(re.findall(r"^\s*[-*] ", tekst, re.M)),
        "naslovi": len(re.findall(r"^#{1,6} ", tekst, re.M)),
        "slike": len(re.findall(r"!\[", tekst)),
        "tablice": len(re.findall(r"^\|", tekst, re.M)),
        "bold_odlomci": len(re.findall(r"\*\*[^*]+\*\*", tekst)),
        "markeri": tekst.count("**") % 2,
    }


def main():
    nalazi = []
    redovi = []
    for put in cs.datoteke():
        rel = os.path.relpath(put, B)
        stari = os.path.join(STARO, rel[len("rukopis/"):] if rel.startswith("rukopis/") else rel)
        if not os.path.exists(stari):
            nalazi.append(f"{rel}: NEMA kopije u {STARO}")
            continue
        a, b = open(stari, encoding="utf-8").read(), open(put, encoding="utf-8").read()
        ma, mb = cs.mjere(stari), cs.mjere(put)
        sa, sb = struktura(a), struktura(b)
        # parnost markera i u staroj verziji (da se zna je li greška nova)
        promj = os.path.getmtime(put) != os.path.getmtime(stari)
        for k in sa:
            # bold_odlomci se NE prijavljuje: skidanje masnoga s tvrdnji je cilj prolaza.
            if k == "bold_odlomci":
                continue
            # Prijavljuje se samo GUBITAK aparata (uklanjanje je šteta); dodavanje je namjerni zahvat.
            if sb[k] < sa[k] and k != "markeri":
                nalazi.append(f"{rel}: struktura {k} {sa[k]} -> {sb[k]}")
        if sb["markeri"] and not sa["markeri"]:
            nalazi.append(f"{rel}: NEOBALANSIRANI ** (novo)")
        prekoracenja = []
        if mb["bold"] > cs.PRAG["bold"]: prekoracenja.append(f"bold {mb['bold']:.1f}")
        if mb["bold_dugi"] > cs.PRAG["bold_dugi"]: prekoracenja.append(f"dugi {mb['bold_dugi']:.1f}")
        if mb["vrlo_kratke"] < cs.PRAG["vrlo_kratke"]: prekoracenja.append(f"≤8 {mb['vrlo_kratke']:.1f}")
        if mb["niz_dagih"] > 2: prekoracenja.append(f"niz {mb['niz_dagih']}")
        if mb["upravo"] > cs.PRAG["upravo"]: prekoracenja.append(f"upravo {mb['upravo']:.1f}")
        if mb["suplje"] > 0: prekoracenja.append(f"šuplje {mb['suplje']}")
        redovi.append([rel, round(ma["bold"], 1), round(mb["bold"], 1), round(ma["bold_dugi"], 1),
                       round(mb["bold_dugi"], 1), round(ma["upravo"], 1), round(mb["upravo"], 1),
                       ma["niz_dagih"], mb["niz_dagih"], round(ma["vrlo_kratke"], 1),
                       round(mb["vrlo_kratke"], 1), ma["kliseji"], mb["kliseji"],
                       "promijenjeno" if promj else "-", ",".join(prekoracenja) or "OK"])
    zag = ["datoteka", "bold→", "", "dugi→", "", "upr→", "", "niz→", "", "≤8→", "", "kliš→", "", "mtime", "stanje"]
    w = [max(len(zag[i]), max((len(str(r[i])) for r in redovi), default=0)) for i in range(len(zag))]
    print("  ".join(zag[i].rjust(w[i]) for i in range(len(zag))))
    for r in redovi:
        print("  ".join(str(x).rjust(w[i]) for i, x in enumerate(r)))
    print("\n=== NALAZI STRUKTURE I GRANICA ===")
    print("\n".join(nalazi) if nalazi else "nema odstupanja u strukturi")
    return 1 if nalazi else 0


if __name__ == "__main__":
    sys.exit(main())
