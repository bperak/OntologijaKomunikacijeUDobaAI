#!/usr/bin/env python3
"""check_figure_overflow.py — mjeri izlazi li tekst iz okvira (bez ljudskog oka).

Zašto: vizualni pregled (`vision_analyze`) je za ovo nepouzdan — u praksi je dvaput
prijavio kvar koji je bila obična glava strelice, a može i prešutjeti stvarno
prelijevanje. Ova provjera je **mjerna**.

Kako mjeri (i zašto baš tako)
-----------------------------
Slova su u renderu **zasebne povezane komponente**, pa se stvarno prelijevanje ne vidi
kao „jedan dugi natpis", nego kao **slova koja nastavljaju red izvan ruba kućice**.
Zato se za svaku kućicu:

  1. nađu komponente teksta čije je središte **unutar** kućice (njezin red teksta),
  2. pogledaju komponente izvan kućice u njezinu susjedstvu (halo) i provjeri je li koja
     **nastavak istoga reda**: preklapa se po visini s unutrašnjim redom i od ruba je
     udaljena manje od ~0,6 visine slova (oznake bridova „da"/„ne" udaljene su više,
     pa se ne broje kao prelijevanje),
  3. isto okomito (red koji pada ispod/iznad kućice).

Alat je **provjeren na kontrolnim slikama** (namjerno prelijevanje lijevo/desno i
okomito, te tekst koji pravilno stoji unutra) — bez toga mjerenje ne vrijedi.

Uporaba: python3 kod/check_figure_overflow.py [figure/*.png ...]
Izlaz: 0 = nema nalaza, 1 = ima nalaza ili se neka slika ne može izmjeriti.
"""
import glob
import os
import sys

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISPUNE = [(236, 236, 255), (255, 255, 222), (236, 253, 255), (255, 240, 245)]
TOL_ISPUNE = 12
TEKST = (51, 51, 51)
TOL_TEKSTA = 60
DOPUSTENO = 4          # px tolerancije (zaobljeni rubovi, antialiasing)
HALO = 45              # px susjedstva u kojemu se traži nastavak reda


def _mape(putanja):
    im = Image.open(putanja).convert("RGBA")
    podloga = Image.new("RGBA", im.size, (255, 255, 255, 255))
    im = np.array(Image.alpha_composite(podloga, im).convert("RGB")).astype(int)
    ispuna = np.zeros(im.shape[:2], bool)
    for boja in ISPUNE:
        # tolerancija PO KANALU, i boja mora biti jasno razlučiva od bijele pozadine —
        # inače bijela pozadina prođe kao ispuna i cijela slika postane „jedna kućica"
        if np.abs(np.array(boja) - 255).max() < 10:
            continue
        ispuna |= (np.abs(im - np.array(boja)).max(axis=2) <= TOL_ISPUNE)
    tekst = (np.abs(im - np.array(TEKST)).sum(axis=2) <= TOL_TEKSTA)
    return im, ispuna, tekst


def _kutije(ispuna, min_povrsina=1500, r=8):
    """Pravokutnici ispune, otporni na rupe koje u ispuni ostavljaju slova."""
    from scipy import ndimage
    lab, n = ndimage.label(ndimage.binary_dilation(ispuna, structure=np.ones((2 * r + 1,) * 2, bool)))
    out = []
    for i in range(1, n + 1):
        pripadaju = ispuna & (lab == i)
        if pripadaju.sum() < min_povrsina:
            continue
        ys, xs = np.nonzero(pripadaju)
        out.append((int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())))
    return out


def _komponente(maska, min_povrsina=10):
    from scipy import ndimage
    lab, n = ndimage.label(maska)
    out = []
    for i in range(1, n + 1):
        ys, xs = np.nonzero(lab == i)
        if len(xs) < min_povrsina:
            continue
        x0, x1, y0, y1 = int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())
        povrsina_kutije = max((x1 - x0) * (y1 - y0), 1)
        # SLovo je puno (ispuna ≥ 0,18 svojega pravokutnika); crta strelice je prazna
        # (dijagonalna linija daje ~0,02) — bez ovoga se strelice broje kao tekst
        if len(xs) / povrsina_kutije < 0.18:
            continue
        out.append((x0, y0, x1, y1, len(xs)))
    return out


def _slova_u_redu(znakovi):
    """Zadrži samo komponente koje su dio REDA SLOVA (imaju susjeda u istoj visini).

    Zašto: u mermaidovoj zadanoj temi **strelice su iste boje kao tekst** (#333333), pa
    se glave strelica i crte inače broje kao slova i daju lažne nalaze („tekst izlazi
    iznad okvira" gdje je zapravo strelica koja ulazi u okvir). Slovo ima susjeda na
    udaljenosti slova; strelica je sama.
    """
    zadrzani = []
    for z in znakovi:
        x0, y0, x1, y1, _ = z
        for w in znakovi:
            if w is z:
                continue
            wx0, wy0, wx1, wy1, _ = w
            prekl = min(y1, wy1) - max(y0, wy0)
            if prekl <= 0.6 * (y1 - y0):
                continue
            razmak = max(wx0 - x1, x0 - wx1)
            if 0 <= razmak <= 1.6 * max(x1 - x0, 1):
                zadrzani.append(z)
                break
    return zadrzani


def provjeri(putanja):
    """Vrati (popis nalaza, je li slika uopće mjerljiva)."""
    _, ispuna, tekst = _mape(putanja)
    kutije = _kutije(ispuna)
    znakovi = _slova_u_redu(_komponente(tekst))
    if not kutije or not znakovi:
        return [], False
    nalazi = []
    for kx0, ky0, kx1, ky1 in kutije:
        unutra = [z for z in znakovi
                  if kx0 <= (z[0] + z[2]) / 2 <= kx1 and ky0 <= (z[1] + z[3]) / 2 <= ky1]
        if not unutra:
            continue
        visina = float(np.median([z[3] - z[1] for z in unutra]))
        # prag = dopušteni razmak od ruba. Stvarno prelijevanje ZNAČI da slova dodiruju
        # rub (razmak ≈ 0); oznaka brida („da"/„ne") stoji na strelici, dalje od ruba.
        prag = max(6.0, 0.35 * visina)
        # --- vodoravno: slova koja nastavljaju red izvan lijevoga/desnoga ruba
        lijevi_red = [z for z in unutra if z[0] - kx0 < 0.5 * (kx1 - kx0)]
        desni_red = [z for z in unutra if z[2] - kx0 >= 0.5 * (kx1 - kx0)]
        donji_red = [z for z in unutra if z[3] - ky0 >= 0.5 * (ky1 - ky0)]
        for z in znakovi:
            x0, y0, x1, y1, _ = z
            if (kx0 <= (x0 + x1) / 2 <= kx1 and ky0 <= (y0 + y1) / 2 <= ky1):
                continue                                  # unutrašnji znak
            isti_red_d = any(min(y1, u[3]) - max(y0, u[1]) > 0.5 * (y1 - y0) for u in desni_red)
            isti_red_l = any(min(y1, u[3]) - max(y0, u[1]) > 0.5 * (y1 - y0) for u in lijevi_red)
            isti_red_o = any(min(x1, u[2]) - max(x0, u[0]) > 0.5 * (x1 - x0) for u in donji_red)
            if 0 < x0 - kx1 < prag and isti_red_d and y0 >= ky0 - prag and y1 <= ky1 + prag:
                nalazi.append((f"tekst izlazi desno izvan okvira za {x1 - kx1} px "
                               f"(znak x{x0}–{x1}, kućica x{kx0}–{kx1}, y{ky0}–{ky1})", x1 - kx1))
            elif 0 < kx0 - x1 < prag and isti_red_l and y0 >= ky0 - prag and y1 <= ky1 + prag:
                nalazi.append((f"tekst izlazi lijevo izvan okvira za {kx0 - x0} px "
                               f"(znak x{x0}–{x1}, kućica x{kx0}–{kx1})", kx0 - x0))
            elif 0 < y0 - ky1 < prag and isti_red_o and x0 >= kx0 - prag and x1 <= kx1 + prag:
                nalazi.append((f"tekst izlazi ispod okvira za {y1 - ky1} px "
                               f"(znak y{y0}–{y1}, kućica y{ky0}–{ky1})", y1 - ky1))
            elif 0 < ky0 - y1 < prag and isti_red_o and x0 >= kx0 - prag and x1 <= kx1 + prag:
                nalazi.append((f"tekst izlazi iznad okvira za {ky0 - y0} px "
                               f"(znak y{y0}–{y1}, kućica y{ky0}–{ky1})", ky0 - y0))
    # ukloni dvostruke nalaze za istu kućicu
    jedinstveni, videno = [], set()
    for tekst_nalaza, iznos in nalazi:
        kljuc = tekst_nalaza.split("(")[0] + str(iznos)
        if kljuc not in videno:
            videno.add(kljuc)
            jedinstveni.append((tekst_nalaza, iznos))
    return jedinstveni, True


def main() -> int:
    putevi = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "figure", "*.png")))
    nalaza = 0
    nemjerljivo = []
    for p in putevi:
        n, mjerljivo = provjeri(p)
        ime = os.path.relpath(p, ROOT)
        if not mjerljivo:
            nemjerljivo.append(ime)
            print(f"— {ime}: nije mjerljivo (nisu prepoznate kućice/tekst)")
            continue
        if n:
            nalaza += len(n)
            print(f"⚠ {ime}: {len(n)} nalaza")
            for t, _ in n[:6]:
                print("     -", t)
        else:
            print(f"✔ {ime}: tekst je unutar okvira")
    if nemjerljivo:
        print(f"\n⚠ neizmjerene slike ({len(nemjerljivo)}): paleta boja nije prepoznata — "
              f"pregledati okom")
    print(f"\n{'⚠ nalaza ukupno: ' + str(nalaza) if nalaza else '✔ nema prelijevanja teksta'}")
    return 1 if nalaza else 0


if __name__ == "__main__":
    sys.exit(main())
