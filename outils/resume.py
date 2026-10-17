# -*- coding: utf-8 -*-
import json, data as d, charts as c
from style import CSS
IMG=json.load(open('/home/claude/vicor/assets/images.json'))

def nb(x,dec=0): return f"{x:,.{dec}f}".replace(","," ").replace(".",",")
cen=d.dcf()['par_action']; bas=d.dcf(0.31,0.105)['par_action']; haut=d.dcf(0.35,0.095)['par_action']
FIL=('<div class="filigrane"><div class="bloc">'
     '<div class="mot">Sous-jacent</div><div class="url">sousjacent.com</div>'
     '</div></div>')
PIED="Sous-jacent · Étude n° 1 · Résumé · Octobre 2026"
def foot(n): return f'<div class="foot"><span>{PIED}</span><span>{n} / 2 &nbsp;·&nbsp; <b>sousjacent.com</b></span></div>'

kpi=[("407,7 M$","Chiffre d'affaires 2025, hors règlement"),
("55 %","du résultat opérationnel 2025 vient d'un règlement judiciaire"),
("3,5 %","Marge opérationnelle moyenne sur 21 exercices"),
("21,6x","Valeur d'entreprise / chiffre d'affaires, médiane historique 3,0x")]
cells=""
for i,(v,l) in enumerate(kpi):
    cells+=f'<div class="kpi"><div class="kpi-v sm">{v}</div><div class="kpi-l">{l}</div></div>'
    if i%2==0: cells+='<div class="vsep"></div>'

grid=""
for m in (0.30,0.33,0.36,0.40):
    tds="".join(f'<td class="num{" hi" if (m==0.33 and w==0.10) else ""}">{nb(d.dcf(m,w)["par_action"],0)}</td>' for w in (0.09,0.10,0.11,0.12))
    lab=f'<b>{int(m*100)} %</b>' if m==0.33 else f'{int(m*100)} %'
    grid+=f'<tr><td>{lab}</td>{tds}</tr>'

P1=f"""<section class="page egg" style="padding:24mm 22mm 14mm">{FIL}
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:8mm">
  <div><div class="eyebrow" style="margin-bottom:4mm">Sous-jacent · Étude n° 1 · Résumé</div>
  <h2 style="font-size:24pt;margin-bottom:2mm">Vicor Corporation</h2>
  <div class="small" style="font-size:9.4pt">NASDAQ : VICR &nbsp;·&nbsp; vingt et un exercices retraités, 2005-2025 &nbsp;·&nbsp; 17 octobre 2026</div></div>
  <div style="flex:0 0 auto">{c.logo("sombre",34)}</div>
</div>
<hr class="hr-strong" style="margin:6mm 0">
<p class="lead" style="font-size:12.4pt;margin-bottom:5mm">Le marché paie Vicor pour une entreprise qu'elle n'a jamais été. Cette étude ne dit pas qu'il a tort. Elle dit exactement de combien l'histoire devrait changer.</p>
<div class="kpis" style="margin:0 0 6mm;row-gap:7mm">{cells}</div>
<hr class="hr-thin">
<h3 style="margin-top:4mm">Le fait : quarante-cinq millions logés dans le chiffre d'affaires</h3>
<p>En 2025, Vicor a encaissé un règlement de litige de brevets de 45 M$. Ce produit non récurrent est <b>balisé par la société à l'intérieur de son chiffre d'affaires</b> dans les données structurées déposées auprès du régulateur américain : la balise XBRL affiche 452,7 M$ là où les états financiers affichent 407,7 M$. Quatre exercices de contrôle concordent au dollar près ; seul 2025 s'écarte, exactement du montant du règlement.</p>
<p>La société calcule en outre tous ses ratios sur le total du chiffre d'affaires <em>et</em> du règlement. Sa marge brute ressort à 57,3 % au lieu de <b>52,6 %</b> — 4,7 points d'effet de présentation. Retraitée, la marge opérationnelle 2025 s'établit à <b>9,0 %</b> et non 20,1 %.</p>
{c.marge_brute()}
<div class="figcap">Marge brute rapportée au seul chiffre d'affaires (trait plein) et selon la présentation de la société (pointillé). Les deux se confondent sauf en 2025.</div>
{foot(1)}</section>"""

P2=f"""<section class="page cream" style="padding:22mm 22mm 11mm">{FIL}
<div class="eyebrow">Ce que le cours oblige à croire</div><div class="rule-v"></div>
<h2 style="font-size:17.5pt;margin-bottom:4mm">90 à 116 dollars, contre un cours de 202,40</h2>
<p>Vingt et un exercices retraités donnent <b>4,2 %</b> de croissance annuelle moyenne, <b>3,5 %</b> de marge opérationnelle courante, une rentabilité du capital durablement inférieure à son coût, et six exercices déficitaires.</p>
<p>Le modèle part du chiffre d'affaires 2026 reconstitué — <b>639,8 M$</b>, dont les deux tiers sont publiés ou guidés — puis retient une croissance qui multiplie les ventes par 4,5 en dix ans, une marge normative de <b>33 %</b> (neuf fois la moyenne historique) et un coût du capital de 10 %. Il produit <b>{nb(cen,0)} dollars par action</b>.</p>
<table class="plain" style="font-size:7.4pt;margin-top:3mm"><caption>Valeur par action selon la marge normative et le coût du capital</caption>
<thead><tr><th>Marge normative</th><th>Capital 9 %</th><th>Capital 10 %</th><th>Capital 11 %</th><th>Capital 12 %</th></tr></thead>
<tbody>{grid}</tbody></table>
<p style="margin-top:3mm"><b>Aucune de ces combinaisons ne rejoint le cours de 202,40 dollars.</b> L'écart ne se résout ni par la marge, ni par le coût du capital, mais par la trajectoire de croissance elle-même.</p>
<div style="max-width:126mm;margin:3mm auto 0">{c.pont()}</div>
<div class="figcap" style="margin-bottom:3mm;max-width:126mm;margin-left:auto;margin-right:auto">Apport de chaque hypothèse supplémentaire, en dollars par action. Le cours est atteint une fois les trois premières étapes franchies ensemble.</div>
<div class="two" style="gap:7mm;margin-top:2mm">
<div><h3 style="margin-top:0;font-size:9.4pt">La bascule réelle</h3>
<p class="small">Les licences passent de 3,9 % du chiffre d'affaires en 2023 à 14,1 % en 2025, tandis que le chiffre d'affaires hors licences reste <b>10 % sous son niveau de 2023</b>. Vicor a équipé les V100 et A100 de Nvidia avant d'être remplacée sur la H100 : le virage vers les brevets suit la perte du socle produit.</p></div>
<div><h3 style="margin-top:0;font-size:9.4pt">Ce que l'étude ne dit pas</h3>
<p class="small">L'échéance et la portée des accords de licence ne sont pas publiées : c'est l'inconnue qui décide de la marge normative. Ni recommandation d'achat ou de vente, ni objectif de cours — les onze hypothèses sont données dans l'étude complète.</p></div></div>
<div class="copyright" style="margin-top:3mm;padding-top:2.5mm"><div class="t">L'étude complète</div>
<p style="font-size:7.8pt">Trente pages, dix-sept chapitres et l'annexe des vingt et un exercices : <b>sousjacent.com/etudes/vicor-2005-2025</b> — © 2026 <b>Sous-jacent</b>, reproduction soumise à autorisation écrite.</p></div>
{foot(2)}</section>"""

html=f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>Vicor Corporation — Résumé de l'étude</title><style>{CSS}
.page .foot{{bottom:6mm}}
.copyright{{margin-top:2mm!important;padding-top:2mm!important}}
.copyright p{{margin-bottom:0}}</style></head>
<body>{P1}{P2}</body></html>"""
open('/home/claude/vicor/resume-vicor.html','w',encoding='utf-8').write(html)
print("ok", len(html))
