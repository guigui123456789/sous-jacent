#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Graphiques SVG pour les pages du site (palette web, pas celle des PDF).

Tous les graphiques du site sont dessinés ici, à la main : aucune image n'est
reprise d'un autre site. La palette est celle de global.css.

Usage : python3 outils/graphiques_web.py
Sortie : public/graphiques/vicor-2005-2025/ et public/graphiques/notes/
"""

import os

BLEU = "#162b4b"
OR = "#a8803c"
GRENAT = "#8a1e41"
GRILLE = "#d8d5d0"
DOUX = "#706e6c"
SANS = "'Source Sans 3','Source Sans Pro','Segoe UI',system-ui,sans-serif"
SERIF = "Spectral,Georgia,serif"

RACINE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public", "graphiques")


def fr(x, dec=0):
    return f"{x:,.{dec}f}".replace(",", " ").replace(".", ",")


def cadre(w, h, corps, titre=None, legende=None, alt=""):
    t = ""
    if titre:
        t = (f'<text x="0" y="13" font-family="{SANS}" font-size="9.2" '
             f'letter-spacing="0.09em" fill="{DOUX}">{titre.upper()}</text>')
    lg = ""
    if legende:
        x = 0
        for lab, col in legende:
            lg += f'<rect x="{x}" y="27" width="14" height="7" fill="{col}"/>'
            lg += f'<text x="{x + 20}" y="34" font-family="{SANS}" font-size="8.6" fill="{BLEU}">{lab}</text>'
            x += 30 + len(lab) * 4.6
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg role="img" aria-label="{alt}" viewBox="0 0 {w} {h}" '
            f'xmlns="http://www.w3.org/2000/svg" '
            f'style="width:100%;height:auto;overflow:visible;font-synthesis:none">'
            f'{t}{lg}{corps}</svg>\n')


def grille(x0, x1, y0, y1, vmax, pas, suffixe=""):
    out = []
    v = 0
    while v <= vmax + 1e-9:
        y = y1 - v / vmax * (y1 - y0)
        out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" '
                   f'stroke="{GRILLE}" stroke-width="0.6"/>')
        out.append(f'<text x="{x0 - 7}" y="{y + 3:.1f}" text-anchor="end" '
                   f'font-family="{SANS}" font-size="8.4" fill="{DOUX}">{fr(v)}{suffixe}</text>')
        v += pas
    return "".join(out)


# ---------------------------------------------------------------- graphique 1
def produits_redevances():
    """Produits et redevances de licence, 2023-2026. Le graphique de la semaine."""
    W, H = 660, 300
    x0, x1, y0, y1 = 46, 648, 56, 232
    SERIES = [
        (2023, 389.2, 15.9, "publié"),
        (2024, 312.5, 46.6, "publié"),
        (2025, 350.3, 57.4, "publié"),
        (2026, 479.6, 160.4, "neuf mois publiés + plancher T4"),
    ]
    vmax, pas = 700, 100
    b = grille(x0, x1, y0, y1, vmax, pas)
    bw = (x1 - x0) / len(SERIES) * 0.42

    # repère : le niveau des produits de 2023, étiquette à gauche pour ne croiser aucune barre
    yr = y1 - 389.2 / vmax * (y1 - y0)
    b += (f'<line x1="{x0}" y1="{yr:.1f}" x2="{x1}" y2="{yr:.1f}" stroke="{GRENAT}" '
          f'stroke-width="0.9" stroke-dasharray="4 3"/>')
    b += (f'<text x="{x0 + 4}" y="{yr + 12:.1f}" font-family="{SANS}" '
          f'font-size="8.4" fill="{GRENAT}">niveau des ventes de produits de 2023 : 389 M$</text>')

    for i, (an, p, r, note) in enumerate(SERIES):
        cx = x0 + (x1 - x0) * (i + 0.5) / len(SERIES)
        hp = p / vmax * (y1 - y0)
        hr = r / vmax * (y1 - y0)
        b += (f'<rect x="{cx - bw / 2:.1f}" y="{y1 - hp:.1f}" width="{bw:.1f}" '
              f'height="{hp:.1f}" fill="{BLEU}" opacity="0.88"/>')
        b += (f'<rect x="{cx - bw / 2:.1f}" y="{y1 - hp - hr:.1f}" width="{bw:.1f}" '
              f'height="{hr:.1f}" fill="{OR}"/>')
        b += (f'<text x="{cx:.1f}" y="{y1 - hp - hr - 8:.1f}" text-anchor="middle" '
              f'font-family="{SERIF}" font-size="13.5" fill="{BLEU}">{fr(p + r)}</text>')
        b += (f'<text x="{cx:.1f}" y="{y1 + 16}" text-anchor="middle" font-family="{SANS}" '
              f'font-size="9.4" fill="{BLEU}">{an}</text>')
        b += (f'<text x="{cx:.1f}" y="{y1 + 27}" text-anchor="middle" font-family="{SANS}" '
              f'font-size="7.6" fill="{DOUX}">{note}</text>')
        # part des redevances : dans la barre si elle est assez haute, à côté sinon
        part = f'{fr(r / (p + r) * 100)} %'
        if hr >= 13:
            b += (f'<text x="{cx:.1f}" y="{y1 - hp - hr / 2 + 3:.1f}" text-anchor="middle" '
                  f'font-family="{SANS}" font-size="8" fill="#fff">{part}</text>')
        else:
            b += (f'<text x="{cx + bw / 2 + 5:.1f}" y="{y1 - hp - hr - 2:.1f}" '
                  f'font-family="{SANS}" font-size="8" fill="{OR}">{part}</text>')

    b += f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{BLEU}" stroke-width="0.8"/>'
    b += (f'<text x="{x0 - 7}" y="{y0 - 8}" text-anchor="end" font-family="{SANS}" '
          f'font-size="8" fill="{DOUX}">M$</text>')
    return cadre(W, H, b,
                 "Vicor, chiffre d'affaires par nature, 2023-2026",
                 [("Ventes de produits", BLEU), ("Redevances de licence", OR)],
                 "Chiffre d'affaires de Vicor de 2023 à 2026, réparti entre ventes de "
                 "produits et redevances de licence. Les redevances passent de 3,9 % à "
                 "25,1 % du total, et les produits dépassent en 2026 leur niveau de 2023.")


# ---------------------------------------------------------------- graphique 2
def trimestres_2026():
    """2026 trimestre par trimestre : publié, contre guidance et contre le modèle."""
    W, H = 660, 300
    x0, x1, y0, y1 = 46, 648, 56, 226
    T = [
        ("T1", 92.6, 20.4, None, "publié"),
        ("T2", 112.9, 30.4, None, "publié"),
        ("T3", 130.5, 66.6, 129.2, "publié"),
        ("T4", 143.6, 43.0, None, "plancher annoncé"),
    ]
    vmax, pas = 200, 50
    b = grille(x0, x1, y0, y1, vmax, pas)
    bw = (x1 - x0) / len(T) * 0.40

    for i, (lab, p, r, guide, note) in enumerate(T):
        cx = x0 + (x1 - x0) * (i + 0.5) / len(T)
        hp = p / vmax * (y1 - y0)
        hr = r / vmax * (y1 - y0)
        b += (f'<rect x="{cx - bw / 2:.1f}" y="{y1 - hp:.1f}" width="{bw:.1f}" '
              f'height="{hp:.1f}" fill="{BLEU}" opacity="0.88"/>')
        b += (f'<rect x="{cx - bw / 2:.1f}" y="{y1 - hp - hr:.1f}" width="{bw:.1f}" '
              f'height="{hr:.1f}" fill="{OR}"/>')
        b += (f'<text x="{cx:.1f}" y="{y1 - hp - hr - 8:.1f}" text-anchor="middle" '
              f'font-family="{SERIF}" font-size="13.5" fill="{BLEU}">{fr(p + r, 1)}</text>')
        b += (f'<text x="{cx:.1f}" y="{y1 + 16}" text-anchor="middle" font-family="{SANS}" '
              f'font-size="9.4" fill="{BLEU}">{lab} 2026</text>')
        b += (f'<text x="{cx:.1f}" y="{y1 + 27}" text-anchor="middle" font-family="{SANS}" '
              f'font-size="7.6" fill="{DOUX}">{note}</text>')
        if guide:
            hg = guide / vmax * (y1 - y0)
            b += (f'<line x1="{cx - bw * 0.8:.1f}" y1="{y1 - hg:.1f}" '
                  f'x2="{cx + bw * 0.8:.1f}" y2="{y1 - hg:.1f}" stroke="{GRENAT}" '
                  f'stroke-width="1.5" stroke-dasharray="3 2"/>')
            b += (f'<text x="{cx + bw * 0.9:.1f}" y="{y1 - hg + 3:.1f}" font-family="{SANS}" '
                  f'font-size="8" fill="{GRENAT}">{fr(guide, 1)} attendus</text>')

    b += f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{BLEU}" stroke-width="0.8"/>'
    b += (f'<text x="{x0 - 7}" y="{y0 - 8}" text-anchor="end" font-family="{SANS}" '
          f'font-size="8" fill="{DOUX}">M$</text>')
    b += (f'<text x="{x0}" y="{y1 + 44}" font-family="{SANS}" font-size="8" fill="{DOUX}">'
          f'Le trait grenat situe le troisième trimestre que les indications de juillet '
          f'laissaient attendre : 129,2 M$, contre 197,1 publiés.</text>')
    return cadre(W, H, b,
                 "Vicor, exercice 2026 trimestre par trimestre, en M$",
                 [("Produits", BLEU), ("Redevances de licence", OR)],
                 "Chiffre d'affaires trimestriel de Vicor en 2026, réparti entre produits et "
                 "redevances. Le troisième trimestre publié atteint 197,1 M$ contre 129,2 M$ "
                 "attendus d'après les indications de juillet.")


def ecrire(chemin, contenu):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)
    print(f"  {chemin}  ({len(contenu)} octets)")


if __name__ == "__main__":
    print("Graphiques web :")
    ecrire(os.path.join(RACINE, "vicor-2005-2025", "produits-redevances-2023-2026.svg"),
           produits_redevances())
    ecrire(os.path.join(RACINE, "notes", "vicor-t3-2026-trimestres.svg"),
           trimestres_2026())
