# -*- coding: utf-8 -*-
"""Rend les PDF robustes à tous les visualiseurs.

Chromium enrobe chaque image dans un espace colorimétrique ICCBased. Les
visualiseurs intégrés aux navigateurs (PDF.js notamment) appliquent ce profil
de façon inconstante, ce qui fait virer les aplats bleu marine au rose. On
remplace l'espace par DeviceRGB, universellement interprété de la même façon.
"""
import sys, pikepdf
from pikepdf import Name

def normaliser(chemin):
    corriges = 0
    with pikepdf.open(chemin, allow_overwriting_input=True) as pdf:
        for page in pdf.pages:
            res = page.get('/Resources')
            if res is None or '/XObject' not in res:
                continue
            for _, xo in res['/XObject'].items():
                if xo.get('/Subtype') != Name('/Image'):
                    continue
                cs = xo.get('/ColorSpace')
                if cs is None:
                    continue
                # ICCBased à trois composantes -> DeviceRGB
                try:
                    est_icc = (isinstance(cs, pikepdf.Array) and len(cs) == 2
                               and str(cs[0]) == '/ICCBased')
                except Exception:
                    est_icc = False
                if est_icc:
                    flux = cs[1]
                    n = int(flux.get('/N', 3))
                    xo['/ColorSpace'] = Name('/DeviceRGB') if n == 3 else (
                        Name('/DeviceGray') if n == 1 else Name('/DeviceCMYK'))
                    corriges += 1
        # métadonnées du document
        with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
            meta['dc:title'] = "Vicor Corporation — le prix d’une entreprise qu’elle n’a jamais été"
            meta['dc:creator'] = ['Guillaume Le Merour']
            meta['dc:publisher'] = ['Sous-jacent']
            meta['dc:rights'] = ("© 2026 Sous-jacent. Reproduction soumise à autorisation écrite ; "
                                 "citation de courts extraits permise avec mention de la source.")
            meta['dc:language'] = ['fr-FR']
            meta['pdf:Keywords'] = ("Vicor Corporation, VICR, analyse financière, comptes retraités, "
                                    "valorisation, DCF inversé, equity research, sousjacent.com")
        pdf.save(chemin, linearize=True)
    return corriges

for f in sys.argv[1:]:
    print(f, '→', normaliser(f), 'images converties en DeviceRGB')
