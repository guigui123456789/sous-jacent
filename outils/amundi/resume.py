import sys, re
sys.path.insert(0, '/root/amundi/da')
from charts import *
css = open('/root/amundi/da/style.css').read() + '''
.r .panel{background:var(--pale)} .r2 .panel{background:var(--stone)}
.hd{background:var(--navy);color:#fff;padding:7mm 10mm 6mm;position:relative}
.hd .k{font-size:6.2pt;letter-spacing:.32em;text-transform:uppercase;color:var(--cu2)}
.hd h1{font-family:Bod;font-weight:400;font-size:30pt;line-height:1.02;margin-top:2mm}
.hd .s{font-family:Bod;font-style:italic;font-size:12.5pt;color:var(--l2);margin-top:1.5mm;max-width:105mm}
.hd .px{position:absolute;right:10mm;top:6mm;text-align:right}
.hd .px .n{font-family:Bod;font-size:44pt;line-height:1;color:#fff}
.hd .px .n span{font-size:.4em;vertical-align:1.1em;color:var(--cu2)}
.hd .px .c{font-size:6.6pt;color:var(--l1);letter-spacing:.08em;margin-top:1mm}
.bx{margin:0 10mm}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:7mm}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.k6{display:grid;grid-template-columns:repeat(3,1fr);border-top:1.5pt solid #000;border-bottom:.25pt solid var(--navy)}
.k6 div{text-align:center;padding:4.6mm 2mm;border-right:.25pt solid rgba(19,42,71,.3)} .k6 div:nth-child(3n){border-right:none}
.k6 div:nth-child(-n+3){border-bottom:.25pt solid rgba(19,42,71,.3)}
.k6 b{display:block;font-family:Bod;font-weight:400;font-size:21pt;color:var(--navy);line-height:1.05}
.k6 span{font-size:6.5pt;line-height:1.3;display:block;margin-top:1mm}
.tx{font-size:8.1pt;line-height:1.48} .tx p{margin-bottom:1.6mm}
.ttl{font-family:Bod;font-size:11.5pt;color:var(--navy);border-top:1.5pt solid #000;padding-top:1.6mm;margin:5.5mm 0 2.2mm}
.ttl i{font-size:8.5pt}
.mini{font-size:5.8pt;color:var(--slate);line-height:1.4}
.op2{border-left:.6pt solid var(--cu);padding-left:3mm;font-family:Bod;font-style:italic;font-size:9.6pt;line-height:1.33;color:var(--navy)}
.big3 div{text-align:center} .big3 b{font-family:Bod;font-weight:400;font-size:26pt;color:var(--navy);display:block}
.big3 span{font-size:6.4pt;line-height:1.3;display:block}
'''
WM = '<div class="wm"><div class="a">Sous-jacent</div><div class="b">sousjacent.com</div></div>'
def foot(n): return f'<div class="foot"><span>Sous jacent · Étude n° 2 · Amundi · résumé</span><span>{n} / 2</span></div>'
def tab(h, rows, tot=None, cls='t small'):
    return f'<table class="{cls}"><tr>' + ''.join(f'<th>{x}</th>' for x in h) + '</tr>' + ''.join(
        f'<tr{" class=tot" if tot and i in tot else ""}>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for i, r in enumerate(rows)) + '</table>'

aum = [710.3,658.6,748.5,792,877.6,985,1083,1426,1425,1653,1729,2064,1904,2037,2240,2380,2581]
marg = [19.2,18.8,19.6,18.6,16.4,16.1,16.0,19.1,18.8,18.4,17.4,17.5,17.8,17.7,17.7,16.1,15.8]
yrs = [str(y) for y in range(2010, 2027)]

p1 = f'''<section class="page r"><div class="panel">
<div class="hd"><div class="k">Sous jacent · Étude n° 2 · 20 octobre 2026 · résumé</div>
<h1>Amundi</h1><div class="s">L'épargne de l'Europe, et ce que coûte d'appartenir à une banque</div>
<div class="px"><div class="k" style="color:var(--l1)">Objectif à 12 mois</div><div class="n">94<span>€</span></div><div class="c">cours 87,65 € (19/10/2026)<br>+7 % · +12 % dividende compris</div></div></div>
<div class="bx" style="margin-top:5mm">
<div class="op2">Le marché a déjà payé le départ d'UniCredit. Il ne paie pas encore les participations cotées, ni la régularité d'une machine qui n'a manqué aucun de ses plans depuis l'introduction en Bourse.</div>
<div class="k6" style="margin-top:4.5mm">
<div><b>2 581 Md€</b><span>d'encours au 30/06/2026, contre 710 Md€ fin 2010</span></div>
<div><b>49,6 %</b><span>coefficient d'exploitation ajusté au S1 2026 ; 58 à 79 % chez les pairs</span></div>
<div><b>1 354 M€</b><span>résultat net ajusté 2025 ; ≈ 28 % sur fonds propres tangibles</span></div>
<div><b>15,8 pb</b><span>marge sur encours au S1 2026, contre 19,2 pb en 2010</span></div>
<div><b>68,3 %</b><span>du capital détenu par le groupe Crédit Agricole</span></div>
<div><b>≈ 300 M€</b><span>revenus annuels liés au réseau UniCredit, contrat échu en juillet 2027 [calc]</span></div></div>
<div class="g2" style="margin-top:1mm">
<div><div class="ttl">La thèse en quatre phrases</div><div class="tx">
<p><b>Une machine rare.</b> Amundi transforme des encours en commissions avec une efficacité qu'aucun concurrent européen n'égale, et a tenu chaque plan depuis 2015.</p>
<p><b>Un risque connu.</b> Le contrat UniCredit hérité de Pioneer expire en juillet 2027 : ≈ 40 pb de marge nette sur 75 Md€, soit ≈ 180 M€ de résultat après impôt.</p>
<p><b>Déjà dans le cours.</b> À 87,65 €, le marché paie un bénéfice de base 2027 de ≈ 978 M€, sous mon scénario (1 037 M€) qui intègre pourtant cette perte en année pleine.</p>
<p><b>Une valeur cachée, un frein.</b> SBI FM et Victory valent ≈ 5,3 Md€ au marché, près de 30 % de la capitalisation. Mais le CET1 est tombé de 21,8 % à 12,4 % : les retours à l'actionnaire dépendront du résultat.</p></div></div>
<div><div class="ttl">Les encours <i>(Md€)</i></div>{columns([y[2:] for y in yrs], aum, w=88, h=37, d=0, hi=[16], lab_every=2, fmt=lambda v: fr(v,0))}
<div class="ttl" style="margin-top:2mm">La marge <i>(pb des encours moyens)</i></div>{lines(yrs, [("", marg, NAVY)], w=88, h=31, ymin=14, ymax=21, ticks=[15,18,21], lab_every=4, legend=False)}</div></div>
<div class="g2">
<div><div class="ttl">D'où vient la croissance <i>(2015-2025)</i></div><div class="tx"><p>Les encours passent de 878 à 2 380 Md€ : collecte 43 %, marchés 28 %, acquisitions 27 % <span class="calc">[calc]</span>. Pioneer (3 545 M€, 2017) et Lyxor (825 M€, 2021) ont tenu leurs chiffres ; aucun des 6,6 Md€ d'écarts d'acquisition n'a été déprécié. Une seule année de décollecte : 2011 (−35 Md€).</p>
<p>Les commissions réagissent aux actions avec un an de retard : +10 % sur l'Euro Stoxx → ≈ +4 % de commissions l'année suivante <span class="calc">[calc]</span>.</p></div></div>
<div><div class="ttl">Qui capte la marge</div><div class="tx"><p>Particuliers : ≈ 30 % des encours, ≈ 69 % des commissions, 30,7 pb (51,2 en 2014). Assureurs du groupe : 19 % des encours à ≈ 3,7 pb. 636 ETF : 425,9 Md€ à 17,5 pb pondérés.</p>
<p>Dans la gamme vendue par UniCredit, sur 111 pb facturés, le réseau garde 59 % : il reste ≈ 45 pb à Amundi (40 prospectus italiens) <span class="calc">[calc]</span>.</p></div></div></div>
<div class="mini" style="margin-top:2mm">Sources : Amundi (rapport 2011, document de base, URD 2015-2025, communiqués jusqu'au S1 2026) ; prospectus Amundi SGR ; justETF ; DWS, Schroders, Aberdeen ; StockAnalysis ; BCE. [calc] = calcul de l'auteur.</div>
</div>{foot(1)}{WM}</div></section>'''

sotp = [("Gestion et technologie", 62.2), ("SBI Funds Management", 13.8), ("Victory Capital", 9.9), ("Capital excédentaire", 2.5), ("ICG et autres JV", 2.7)]
p2 = f'''<section class="page r2"><div class="panel">
<div class="bx" style="padding-top:9mm">
<div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-family:Bod;font-size:22pt;color:var(--navy)">Le prix, et ce qui me donnerait tort</div><div class="kicker" style="color:var(--cu)">Amundi · résumé</div></div>
<div class="g3 big3" style="border-top:1.5pt solid #000;border-bottom:.25pt solid var(--navy);padding:3mm 0;margin-top:3mm">
<div><b>89,2 €</b><span>valeur intrinsèque : 2/3 somme des parties (91,2 €), 1/3 multiples (85,2 €)</span></div>
<div><b style="color:var(--cu)">94 €</b><span>objectif à 12 mois : valeur × 1,10 − dividende de 4,40 €</span></div>
<div><b>85 – 94 €</b><span>fourchette de valeur, ±5 %, causée d'abord par le coût des fonds propres</span></div></div>
<div class="g2">
<div><div class="ttl">D'où vient la valeur <i>(€ par action)</i></div>{hbars(sotp, w=86, labw=34, d=1, hi=[1,2], hi_color=CU)}
<div class="tx" style="margin-top:1.5mm"><p>Cœur : bénéfice 2027 de 1 037 M€ × 12,0 (90 % / (10 % − 2,5 %)). SBI FM (660,7 M d'actions à 496,35 ₹) et Victory (22,99 M à 107,71 $) au cours, −10 %.</p></div></div>
<div><div class="ttl">Sensibilité de la valeur <i>(€ ; somme des parties)</i></div>{tab(["Coût des fonds propres","g 2,0 %","2,5 %","3,0 %"],[["9,5 %","89,8","92,8","96,3"],["<b>10,0 %</b>","85,8","<b>88,4</b>","91,3"],["10,5 %","82,3","84,5","87,0"]])}
<div class="mini" style="margin-top:1mm">Sans l'effet d'entrée des marchés du S2 2026 (+2,8 € par case).</div>
<div class="ttl" style="margin-top:3mm">Le bénéfice 2027, ligne à ligne <i>(M€)</i></div>{tab(["",""],[["Rythme du S1 2026, hors participations et surperformance","1 185"],["+ effet d'entrée et croissance nette (3,5 % − 1 %)","+77"],["− UniCredit (300 × 80 % × 75 %) et fin des pénalités","−225"],["= bénéfice de base 2027","1 037"],["+ SBI, Victory, ICG, JV → BPA 6,82 € (200 M d'actions)","1 364"]], tot=[3])}</div></div>
<div class="g2">
<div><div class="ttl">Les risques, en euros par action</div>{tab(["Risque","€"],[["Perte UniCredit 450 M€ au lieu de 300","−5,4"],["Coût des fonds propres +0,5 point","−3,9"],["Décote des participations 20 % au lieu de 10","−2,8"],["Pénalités 120 M€ au lieu de 60","−2,7"],["Compression de marge 2 %/an au lieu de 1","−0,7"],["Option Anima / Banco BPM (hors prix)","+3,6"],["Surtaxe 2027 réduite (projet de loi)","+1,7"]])}</div>
<div><div class="ttl">Ce qui me donnerait tort</div><div class="tx">
<p><b>T3 2026 et annuel 2026</b> : sorties UniCredit &gt; 10 Md€ par trimestre et marge des particuliers &lt; 28,5 pb.</p>
<p><b>S1 2027</b> : marge totale &lt; 15,0 pb ; <b>2027</b> : coefficient ajusté &gt; 54 %.</p>
<p><b>À tout moment</b> : CET1 &lt; 11 % ; SBI FM &lt; 400 ₹ ou Victory &lt; 80 $ durablement.</p>
<p><b>À la hausse</b> : débouché italien (Banco BPM, Anima) ou BPA 2027 &gt; 7,3 €.</p></div></div></div>
<div class="ttl">Les quatre repères maison</div>
<div class="g3" style="grid-template-columns:repeat(4,1fr)">{''.join(f'<div class="big3"><b style="font-size:17pt">{n}</b><span>{l}</span></div>' for n,l in [("18 %","du résultat ajusté 2025 non reproductible"),("+18 pts","rentabilité des fonds propres tangibles − coût des fonds propres"),("±5 %","amplitude de la fourchette de valeur"),("×0,8","hypothèses rapportées à l'histoire : plus prudentes")])}</div>
<div class="op2" style="margin-top:4mm">Une valeur de qualité, correctement mais pas généreusement payée. Ce qui manque à Amundi n'est pas la qualité, c'est un nouveau récit de croissance : son objectif 2028 est déjà atteint en rythme.</div>
<div class="mini" style="margin-top:3mm;line-height:1.5">Opinion de l'auteur, Guillaume Le Merour, diffusée le 20/10/2026, valable douze mois. Recommandation d'investissement au sens du règlement (UE) n° 596/2014, établie selon le règlement délégué (UE) 2016/958 ; ce n'est pas un conseil en investissement personnalisé. L'auteur ne détient aucun titre Amundi ; l'étude n'a été ni commandée ni rémunérée. Étude complète (50 pages), classeur et historique des objectifs : sousjacent.com/etudes/amundi-2010-2026. Prochaine revue après le T3 2026, le 29/10/2026. © 2026 Sous-jacent, reproduction soumise à autorisation écrite.</div>
</div>{foot(2)}{WM}</div></section>'''
open('/root/amundi/da/resume.html','w').write(f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Amundi — résumé</title><style>{css}</style></head><body>{p1}{p2}</body></html>')
print('ok')
