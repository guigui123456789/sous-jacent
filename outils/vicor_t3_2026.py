# -*- coding: utf-8 -*-
"""Revue de l'étude Vicor après les résultats du troisième trimestre 2026
(publiés le 20 octobre 2026).

Ce script ne modifie pas data.py : les PDF de l'étude (publication du
17 octobre 2026) restent reproductibles à l'identique. Il surcharge, en
mémoire, les seules données que le trimestre a mesurées :

  - le chiffre d'affaires 2026 (trois trimestres publiés + plancher de la
    guidance du quatrième) ;
  - la trésorerie nette au 30 septembre 2026 ;
  - le nombre d'actions diluées du troisième trimestre.

Les hypothèses structurelles (croissance, marges, rotation, coût du capital,
croissance à l'infini) ne changent pas.

Usage : python3 outils/vicor_t3_2026.py
"""

import data

# --- Données publiées (communiqué du 20 octobre 2026) -----------------------
T1, T2, T3 = 113.0, 143.4, 197.1          # chiffre d'affaires total, M$
NEUF_MOIS = 453.4                          # publié par la société
PRODUITS_T3, REDEVANCES_T3 = 130.5, 66.6   # M$
PRODUITS_T2, REDEVANCES_T2 = 112.9, 30.4

# Guidance du quatrième trimestre (appel du 20 octobre 2026)
PRODUITS_T4 = round(PRODUITS_T3 * 1.10, 2)  # progression d'environ 10 % des produits
REDEVANCES_T4_PLANCHER = 43.0               # « au moins 43 M$ », sans nouvelle licence
T4_PLANCHER = PRODUITS_T4 + REDEVANCES_T4_PLANCHER
CA2026 = round(NEUF_MOIS + T4_PLANCHER, 1)

TRESO = 513.137          # trésorerie au 30/09/2026, M$
LOCATIONS = 1.733 + 5.427  # dettes locatives, seule dette (même traitement qu'en 2025)
TRESO_NETTE = round(TRESO - LOCATIONS, 3)
ACTIONS = 47.609         # actions diluées, troisième trimestre 2026, millions
COURS = 190.68           # clôture du 19 octobre 2026, veille de la publication
KE = 0.10                # coût des fonds propres = coût moyen pondéré (aucune dette financière)
DIVIDENDE = 0.0          # aucun dividende attendu à douze mois dans le modèle

data.CA2026, data.TRESO_NETTE, data.ACTIONS, data.COURS = CA2026, TRESO_NETTE, ACTIONS, COURS


def valeur(**kw):
    return data.dcf(**kw)["par_action"]


def objectif(v):
    return v * (1 + KE) - DIVIDENDE


def marge_pour_cours(cible, **kw):
    """DCF inversé : marge normative qui redonne `cible`, autres hypothèses inchangées."""
    lo, hi = 0.0, 1.5
    for _ in range(80):
        m = (lo + hi) / 2
        if valeur(marge_norm=m, **kw) < cible:
            lo = m
        else:
            hi = m
    return m


def avec_ca2026(ca):
    ancien = data.CA2026
    data.CA2026 = ca
    v = valeur()
    data.CA2026 = ancien
    return v


if __name__ == "__main__":
    print(f"T4 plancher : produits {PRODUITS_T4} + redevances {REDEVANCES_T4_PLANCHER} = {T4_PLANCHER:.2f}")
    print(f"CA 2026 = {NEUF_MOIS} + {T4_PLANCHER:.2f} = {CA2026}")
    print(f"Tresorerie nette = {TRESO} - {LOCATIONS:.3f} = {TRESO_NETTE}")
    print(f"Actions diluees = {ACTIONS}")

    c = data.dcf()
    v0 = c["par_action"]
    print(f"\nVALEUR CENTRALE = {v0:.2f}  (VE {c['ve']:.1f}, part VT {c['part_vt']:.1f} %, CA 2035 {c['ca_terminal']:.0f})")
    print(f"OBJECTIF 12 mois = {objectif(v0):.2f}   (ecart au cours {objectif(v0)/COURS*100-100:+.1f} %)")

    bas = valeur(marge_norm=0.31, wacc=0.105)
    haut = valeur(marge_norm=0.35, wacc=0.095)
    print(f"Borne basse (31 %, 10,5 %) = {bas:.2f} -> objectif {objectif(bas):.1f}")
    print(f"Borne haute (35 %, 9,5 %)  = {haut:.2f} -> objectif {objectif(haut):.1f}")
    print(f"Amplitude : -{(1-bas/v0)*100:.1f} % / +{(haut/v0-1)*100:.1f} %")

    print("\nGrille de sensibilite (valeur intrinseque)")
    print("marge   " + "  ".join(f"WACC {w}%" for w in (9, 10, 11, 12)))
    for m in (26, 30, 33, 36, 40):
        print(f"{m} %   " + "  ".join(f"{valeur(marge_norm=m/100, wacc=w/100):7.0f}" for w in (9, 10, 11, 12)))

    print("\nDCF inverse : marge normative requise pour atteindre le cours")
    for cible in (COURS, 203.43):
        print(f"  cours {cible:.2f} -> marge normative {marge_pour_cours(cible)*100:.1f} %")

    print("\nSensibilite au point de depart 2026 (valeur centrale)")
    for ca in (600.0, 640.0, 660.0, 700.0):
        print(f"  CA 2026 = {ca:.0f} M$ -> {avec_ca2026(ca):.1f} $")

    print("\nEffet de chaque correction mesuree (de 102,10 a la valeur actuelle)")
    data.CA2026, data.TRESO_NETTE, data.ACTIONS = 639.8, 395.384, 46.0
    base = valeur()
    data.CA2026 = CA2026
    a = valeur()
    data.TRESO_NETTE = TRESO_NETTE
    b = valeur()
    data.ACTIONS = ACTIONS
    d = valeur()
    print(f"  publication 17/10      {base:.2f}")
    print(f"  + CA 2026 = {CA2026}    {a:.2f}  ({a-base:+.2f})")
    print(f"  + tresorerie nette     {b:.2f}  ({b-a:+.2f})")
    print(f"  + 47,609 M d'actions   {d:.2f}  ({d-b:+.2f})")

    # Lecture du trimestre
    ro = 72.148
    redev_nettes = REDEVANCES_T3 - 16.1
    print("\nLecture du T3")
    print(f"  Produits +{(PRODUITS_T3/PRODUITS_T2-1)*100:.1f} % sur T2 (guidance : +10 %)")
    print(f"  Redevances {REDEVANCES_T3} contre ~5 guides")
    print(f"  Marge operationnelle T3 : {ro/T3*100:.1f} %")
    print(f"  Redevances nettes des frais juridiques : {redev_nettes:.1f} M$ = {redev_nettes/ro*100:.0f} % du resultat operationnel")
    print(f"  Resultat hors redevances nettes : {ro-redev_nettes:.1f} M$ = {(ro-redev_nettes)/PRODUITS_T3*100:.1f} % des produits")
    guide_t3 = PRODUITS_T2 * 1.10 + 5.0
    print(f"  T3 implique par la guidance de juillet : {guide_t3:.1f} M$ ; publie {T3} ({T3/guide_t3*100-100:+.0f} %)")
