import json, openpyxl, sys
sys.path.insert(0, '/root/amundi/da')
from charts import *

wb = openpyxl.load_workbook('/root/amundi/out/calc/amundi-comptes-2010-2025.xlsx', data_only=True)
def row(sheet, label):
    for r in wb[sheet].iter_rows(values_only=True):
        if r[0] and str(r[0]).startswith(label):
            return list(r[1:17])
    raise KeyError(label)
Y = list(range(2010, 2026))
REV = row('CR_comptable', 'Produit net'); RNPG = row('CR_comptable', 'Résultat net part du groupe')
FEE = row('CR_ajuste', 'Commissions nettes de gestion'); PERF = row('CR_ajuste', 'Commissions de surperformance')
RNA = row('CR_ajuste', 'Résultat net part du groupe ajusté'); REVA = row('CR_ajuste', 'Revenus nets ajustés')
CHA = row('CR_ajuste', 'Charges ajustées')
AUM = row('Encours_collecte', "Encours fin d'année"); FLOW = row('Encours_collecte', 'Collecte nette')
CP = row('Bilan', 'Capitaux propres'); GW = row('Bilan', "Écarts d'acquisition")
DPS = row('Action', 'Dividende par action'); MARG = row('Charges_marges', 'Marge sur commissions')
STAFF = row('Charges_marges', "Effectif fin")
MACRO = json.load(open('/root/amundi/macro/macro.json'))

PAGES = []
def page(cls, inner, run=None, folio=True, dark=False):
    n = len(PAGES) + 1
    r = f'<div class="run">{run}</div>' if run else ''
    f = (f'<div class="foot"><span>Sous jacent · Étude n° 2 · Amundi</span><span>{n}</span></div>' if folio else '')
    PAGES.append(f'<section class="page {cls}{" dark" if dark else ""}">{inner}{r}{f}</section>')
def panel(cls, inner, **k):
    page(cls, f'<div class="panel">{inner}', **k); PAGES[-1] = PAGES[-1].replace('</section>', '</div></section>', 1) if False else PAGES[-1]
    # close panel before footer: rebuild
    s = PAGES.pop(); n = len(PAGES)+1
    r = f'<div class="run">{k.get("run")}</div>' if k.get('run') else ''
    f = f'<div class="foot"><span>Sous jacent · Étude n° 2 · Amundi</span><span>{n}</span></div>' if k.get('folio', True) else ''
    dk = " dark" if k.get('dark') else ""
    PAGES.append(f'<section class="page {cls}{dk}"><div class="panel">{inner}{r}{f}</div></section>')

def chap(num, title, lead=None, center=False):
    c = ' center' if center else ''
    l = f'<div class="lead">{lead}</div>' if lead else ''
    return f'<div class="chap{c}"><div class="num">{num}</div><h2>{title}</h2>{l}</div>'
def op(text, tag="Opinion de l'auteur"):
    return f'<div class="op"><span class="tag">{tag}</span>{text}</div>'
def rb(lab, n, cap):
    return f'<div class="rb"><div class="lab">{lab}</div><div class="n">{n}</div><div class="cap">{cap}</div></div>'
def bh(t, unit=''):
    u = f' <i>({unit})</i>' if unit else ''
    return f'<div class="blockhead"><span class="tt">{t}{u}</span></div>'
def txtpage(run, head, body, src=''):
    page('bg-creme txt', f'<div class="body">{head}<div class="cols">{body}</div>'
         + (f'<div class="src" style="margin-top:3mm">{src}</div>' if src else '') + '</div>', run=run)
def onepage(run, head, body, src=''):
    page('bg-creme txt', f'<div class="body">{head}<div class="one">{body}</div>'
         + (f'<div class="src" style="margin-top:3mm;width:150mm">{src}</div>' if src else '') + '</div>', run=run)
def railpage(run, main, side, bg='bg-pale', dark=False):
    panel(f'{bg} rail', f'<div class="main">{main}</div><div class="vrule"></div><div class="side">{side}</div>', run=run, dark=dark)
def table(head, rows, cls='t', tot=None, hl=None):
    h = '<tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr>'
    b = ''
    for i, r in enumerate(rows):
        c = ' class="tot"' if (tot and i in tot) else (' class="hl"' if (hl and i in hl) else '')
        b += f'<tr{c}>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>'
    return f'<table class="{cls}">{h}{b}</table>'
def f1(v, d=1): return fr(v, d) if v is not None else '—'
def pct(v, d=1): return (fr(v*100, d) + ' %') if v is not None else '—'

# ====================================================================== 1. COUVERTURE
panel('cover', '''
 <img class="full" src="img/cover.jpg" style="width:100%;height:100%;object-fit:cover;object-position:62% 50%">
 <div style="position:absolute;left:0;right:0;top:14mm;text-align:center;color:var(--navy)">
  <div style="width:46mm;border-top:.25pt solid var(--navy);margin:0 auto"></div>
  <div style="font-family:Bod;font-weight:500;font-size:12pt;letter-spacing:.42em;text-transform:uppercase;margin:3.2mm 0 3mm">Sous jacent</div>
  <div style="width:46mm;border-top:.25pt solid var(--navy);margin:0 auto"></div>
  <div class="kicker" style="margin-top:3mm">Étude n° 2 · octobre 2026</div>
 </div>
 <div style="position:absolute;left:16mm;top:62mm;color:var(--navy)">
  <div style="font-family:Bod;font-size:76pt;line-height:.95">Amundi</div>
  <div style="font-family:Bod;font-style:italic;font-size:18pt;line-height:1.18;margin-top:6mm;max-width:92mm">L'épargne de l'Europe, et ce que coûte d'appartenir à une banque</div>
  <div style="margin-top:7mm;font-size:7pt;letter-spacing:.3em;text-transform:uppercase;font-weight:400">Euronext Paris · 2010 — 2026</div>
 </div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:50mm;background:var(--navy);color:#fff;display:grid;grid-template-columns:1fr .25pt 1fr .25pt 1fr;align-items:center;padding:0 12mm 9mm">
  <div style="text-align:center"><div style="font-family:Bod;font-size:30pt;color:var(--cu2)">94 €</div><div class="kicker" style="margin-top:2.4mm;color:var(--l2);letter-spacing:.2em">Objectif à 12 mois</div></div>
  <div style="height:22mm;background:rgba(255,255,255,.35)"></div>
  <div style="text-align:center"><div style="font-family:Bod;font-size:30pt">87,65 €</div><div class="kicker" style="margin-top:2.4mm;color:var(--l2);letter-spacing:.2em">Cours du 19/10/2026</div></div>
  <div style="height:22mm;background:rgba(255,255,255,.35)"></div>
  <div style="text-align:center"><div style="font-family:Bod;font-size:30pt">+12 %</div><div class="kicker" style="margin-top:2.4mm;color:var(--l2);letter-spacing:.2em">Rendement attendu, dividende compris</div></div>
 </div>
 <div style="position:absolute;left:0;right:0;bottom:5mm;text-align:center;font-size:5.8pt;color:#b3c1d4">Étude indépendante signée par son auteur, Guillaume Le Merour. Ceci n'est pas un conseil en investissement. L'auteur ne détient pas d'actions Amundi.</div>
 <div class="credit" style="bottom:53mm;color:#5a554c">Photographie : Lens by Benji, Unsplash</div>
''', folio=False)

# ====================================================================== 2. LE PRIX
bars_sotp = [("Gestion et technologie", 62.2), ("SBI Funds Management", 13.8), ("Victory Capital", 9.9), ("Capital excédentaire", 2.5), ("ICG et autres JV", 2.7)]
panel('bg-navy', f'''
 <div style="text-align:center;padding-top:9mm;color:var(--l1)"><div class="kicker">Amundi · l'avis de l'auteur</div>
 <div style="font-family:Bod;font-size:27pt;color:var(--cu2);margin-top:5mm">Le prix</div><div class="tick" style="color:var(--cu2);margin-top:3mm"></div></div>
 <div style="font-family:Bod;font-style:italic;font-size:15pt;line-height:1.28;margin:5mm 14mm 0 54mm">Le marché a déjà payé le départ d'UniCredit. Il ne paie pas encore les participations cotées, ni la régularité d'une machine qui n'a manqué aucun de ses plans depuis l'introduction en Bourse.</div>
 <div style="border-top:1pt solid rgba(255,255,255,.55);margin:6mm 10mm 0"></div>
 <div style="display:grid;grid-template-columns:86mm .25pt 1fr;margin:0 10mm;height:64mm;align-items:center">
  <div style="text-align:center"><div class="kicker" style="color:var(--l1)">Objectif de cours à douze mois</div>
   <div style="font-family:Bod;font-size:104pt;line-height:1.05">94<span style="font-size:.36em;vertical-align:1.15em;color:var(--cu2)">€</span></div>
   <div style="font-family:Bod;font-style:italic;font-size:12pt;color:var(--l1)">au 20 octobre 2027</div></div>
  <div style="height:52mm;background:rgba(255,255,255,.35)"></div>
  <div style="padding-left:9mm;font-size:7.6pt">
   {''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:.25pt solid rgba(255,255,255,.28);padding:1.7mm 0"><span style="color:var(--l2)">{k}</span><span style="font-family:Bod;font-size:14.5pt;color:{c}">{v}</span></div>' for k, v, c in [("Cours de référence, 19/10/2026","87,65 €","#fff"),("Valeur intrinsèque aujourd'hui","89,2 €","#fff"),("Potentiel de cours","+7 %","var(--cu2)"),("Avec le dividende attendu (≈ 4,40 €)","+12 %","var(--cu2)"),("Coût des fonds propres retenu","10,0 %","#fff")])}
  </div>
 </div>
 <div style="border-top:1pt solid rgba(255,255,255,.55);margin:0 10mm"></div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin:0 10mm">
  <div><div style="font-weight:500;font-size:7.4pt;margin:5mm 0 2.5mm">D'où vient la valeur <span style="font-weight:300;color:var(--l1)">(€ par action, somme des parties)</span></div>
   {hbars(bars_sotp, w=85, color="#C9D5E3", txt="#e8edf4", hi=[1,2], hi_color=CU2, labw=36)}
   <div style="display:flex;justify-content:space-between;border-top:.5pt solid rgba(255,255,255,.7);padding-top:1.4mm;font-size:7.4pt;margin-top:1mm"><b>Somme des parties</b><span style="font-family:Bod;font-size:12pt">91,2</span></div></div>
  <div><div style="font-weight:500;font-size:7.4pt;margin:5mm 0 2.5mm">Sensibilité de la valeur <span style="font-weight:300;color:var(--l1)">(€ par action)</span></div>
   {table(["Coût des fonds propres","g = 2,0 %","2,5 %","3,0 %"],[["9,5 %","89,8","92,8","96,3"],["10,0 %","85,8",'<b style="color:var(--cu2)">88,4</b>',"91,3"],["10,5 %","82,3","84,5","87,0"]])}
   <div style="font-size:7pt;color:var(--l1);margin-top:2.5mm;line-height:1.45">Revenus UniCredit perdus : 260 / <b style="color:#fff">300</b> / 340 / 450 M€ → valeur 90,6 / <b style="color:#fff">89,2</b> / 87,7 / 83,8 €</div></div>
 </div>
 <div style="border-top:1pt solid rgba(255,255,255,.55);margin:5mm 10mm 0"></div>
 <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8mm;margin:4mm 10mm 0">
  {''.join(f'<div><div style="font-family:Bod;font-size:20pt;color:var(--cu2)">{n}</div><div style="font-family:Bod;font-style:italic;font-size:13.5pt;line-height:1.2;margin:1.5mm 0 2mm">{t}</div><div style="font-size:7.4pt;line-height:1.45;color:var(--l2)">{b}</div></div>' for n,t,b in [("I","UniCredit est déjà dans le cours","À 87,65 €, le marché paie le cœur d'Amundi ≈ 980 M€ de bénéfice 2027, en dessous du scénario qui intègre la perte de ≈ 300 M€ de revenus."),("II","Près d'un tiers de la valeur est coté ailleurs","SBI FM et Victory Capital valent ≈ 5,3 Md€ au marché, soit près de 30 % de la capitalisation, mal lus par un multiple de bénéfices."),("III","Une régularité que la Bourse ne paie pas","Meilleur coefficient d'exploitation du panel, plans tenus depuis 2015, et pourtant le même multiple que DWS.")])}
 </div>
 <div class="note" style="position:absolute;left:10mm;right:10mm;bottom:12.5mm">Opinion de l'auteur, distincte des faits rapportés dans l'étude. Méthode : somme des parties (2/3) et multiples de pairs (1/3), valeur portée à douze mois au coût des fonds propres, diminuée du dividende attendu. Grille calculée sans l'effet d'entrée des marchés au second semestre 2026. Sources et calculs : chapitres 21 à 24 et classeur publié. Recommandation au sens du règlement (UE) 596/2014 ; historique des objectifs publiés sur sousjacent.com.</div>
''', dark=True)

# ====================================================================== 3. CHIFFRES CLES
cells = [("710<span class='ar'>→</span>2 581","milliards d'euros d'encours, de la fusion de 2010 au 30 juin 2026","Rapport 2011 ; communiqué S1 2026"),
 ("49,6<small>%</small>","des revenus absorbés par les charges au 1<sup>er</sup> semestre 2026, contre 58 % à 79 % chez les grands pairs européens","Communiqué S1 2026 ; DWS, Schroders, Aberdeen"),
 ("1","seule année de décollecte depuis la création : 2011, crise des dettes souveraines (−35 Md€)","Rapport 2011 ; communiqués annuels"),
 ("19,2<span class='ar'>→</span>15,8","points de base de marge sur les encours : le prix du passage à la gestion passive","Rapport 2011 ; communiqué S1 2026"),
 ("68,3<small>%</small>","du capital détenu par le groupe Crédit Agricole, qui préside le conseil","URD 2025"),
 ("<span style='font-family:Inter;font-weight:200;font-size:.6em;vertical-align:.25em'>≈</span> 300","millions d'euros de revenus annuels liés au réseau UniCredit, dont le contrat expire en juillet 2027","Calcul de l'auteur, prospectus italiens (ch. 14)")]
g = ''.join(f'<div class="cell{" last" if i>=4 else ""}"><div class="n">{n}</div><div class="l">{l}</div><div class="s">{s}</div></div>' for i,(n,l,s) in enumerate(cells))
panel('bg-stone', f'''
 <div style="text-align:center;padding-top:9mm;color:var(--navy2)"><div class="kicker">Amundi en six chiffres</div>
 <div style="font-family:Bod;font-size:27pt;color:var(--navy);margin-top:5mm">Ce que disent les comptes</div><div class="tick" style="color:var(--navy);margin-top:3mm"></div></div>
 <div class="thick" style="margin:6mm 10mm 0"></div>
 <div style="font-family:Bod;font-style:italic;font-size:15pt;line-height:1.28;text-align:center;margin:5mm 22mm;color:var(--navy)">Une entreprise qui a triplé de taille sans jamais perdre la main sur ses coûts, et dont la seule vraie faiblesse ne vient pas d'elle.</div>
 <div class="thin" style="margin:0 10mm"></div>
 <div class="kgrid">{g}</div>
 <div class="note" style="position:absolute;left:10mm;right:10mm;bottom:14mm;text-align:center">Mesures tirées des comptes publiés, sauf la dernière, estimée par l'auteur à partir de 40 prospectus de fonds italiens (75 Md€ × ≈ 40 pb). Encours y compris coentreprises ; marge = commissions nettes de gestion rapportées aux encours moyens hors coentreprises.</div>
''')

# ====================================================================== 4. SOMMAIRE
toc = [("I","Cadre",[("1","Ce que ce dossier est, et comment le lire"),("2","La thèse en une page")]),
 ("II","Le terrain de jeu",[("3","L'économie de la gestion d'actifs"),("4","L'économie, année par année"),("5","Le cadre réglementaire comme variable économique")]),
 ("III","L'entreprise",[("6","Le modèle, en une mécanique"),("7","Construction de l'entreprise, 2010-2026"),("8","Implantation, effectifs, organisation"),("9","Actionnariat, contrôle, gouvernance")]),
 ("IV","Les gens",[("10","Qui dirige, et d'où ils viennent")]),
 ("V","Ce qui est vendu, et à quel prix",[("11","La gamme, famille par famille"),("12","Les prix réels"),("13","Ce que l'étude ne mesure pas : la performance des fonds")]),
 ("VI","Les clients",[("14","Par où arrivent les encours, et le cas UniCredit")]),
 ("VII","Les chiffres",[("15","Les comptes, exercice par exercice"),("16","L'économie unitaire"),("17","Qualité du résultat")]),
 ("VIII","Autour",[("18","Les concurrents, sur les mêmes lignes"),("19","Ce que la presse et les analystes ont dit"),("20","Ce qui peut casser la thèse")]),
 ("IX","Le prix",[("21","Le titre en Bourse depuis 2015"),("22","Ce que le cours actuel suppose"),("23","Trois chemins vers la valeur"),("24","Le prix, et ce qui me donnerait tort"),("25","Les quatre repères maison")]),
 ("X","Après",[("26","Engagement de suivi"),("27","Annexes : sources, méthode, lexique")])]
cols = ''
for pn, pt, chs in toc:
    cols += f'<div style="break-inside:avoid;margin-bottom:5mm"><div class="kicker" style="color:var(--cu)">Partie {pn}</div><div style="font-family:Bod;font-size:14pt;color:var(--navy);margin:1mm 0 1.5mm">{pt}</div>' + ''.join(f'<div style="display:flex;gap:3mm;font-size:8.2pt;line-height:1.7;border-bottom:.25pt solid rgba(19,42,71,.18)"><span style="font-family:Bod;width:7mm;color:var(--navy2)">{n}</span><span>{t}</span></div>' for n,t in chs) + '</div>'
panel('bg-pale', f'''<div style="text-align:center;padding-top:9mm;color:var(--navy2)"><div class="kicker">Amundi</div>
 <div style="font-family:Bod;font-size:27pt;color:var(--navy);margin-top:5mm">Sommaire</div><div class="tick" style="color:var(--navy);margin-top:3mm"></div></div>
 <div class="thick" style="margin:6mm 10mm 6mm"></div>
 <div style="column-count:2;column-gap:12mm;margin:0 12mm">{cols}</div>''')

# ====================================================================== 5. CH1
onepage("Partie I · Cadre", chap("Chapitre 1", "Ce que ce dossier est, et comment le lire", "Une étude d'entreprise, signée, datée, qui publie un prix et dit sur quoi il repose."), '''
<h3>Objet et période</h3><p>Le dossier étudie Amundi, premier gestionnaire d'actifs européen, de sa création au 1<sup>er</sup> janvier 2010 au premier semestre 2026 , exercice par exercice. La période commence avec la société elle-même, née de la fusion de Crédit Agricole Asset Management et de Société Générale Asset Management. Les données sont arrêtées au 20 octobre 2026 ; le cours de référence est la clôture du 19 octobre 2026, 87,65 €.</p>
<h3>Ce qui est fait, et ce qui ne l'est pas</h3><p>Les comptes ont été reconstitués exercice par exercice à partir des documents publiés (rapport 2011, document de base de l'introduction en Bourse, documents de référence et d'enregistrement universel 2015-2025, communiqués trimestriels jusqu'au T2 2026). Les tarifs ont été relevés sur 636 ETF et 40 fonds italiens. La macroéconomie vient des séries de la BCE et de la Réserve fédérale de Saint-Louis. Trois choses n'ont pas pu être mesurées et sont dites comme telles : la performance des fonds pour leurs clients, les comptes de la filiale italienne (accès payant, non acheté) et le montant des pénalités versées par UniCredit (non publié).</p>
<h3>Comment distinguer les faits des opinions</h3><p>Tout chiffre porte sa source. Les calculs de l'auteur sont signalés <span class="calc">[calc]</span>. Les opinions sont composées en italique, dans un filet cuivre, sous la mention « Opinion de l'auteur ». Rien n'est estimé en silence : quand une donnée manque, le texte l'écrit.</p>
<h3>Statut réglementaire</h3><p>Ce dossier publie un objectif de cours : c'est une recommandation d'investissement au sens du règlement (UE) n° 596/2014 et de son règlement délégué (UE) 2016/958. L'auteur applique volontairement les obligations prévues pour les experts : identité, méthode accessible, horizon, sources, déclaration d'intérêts et historique des recommandations des douze derniers mois (chapitre 26). Ce dossier n'est pas un conseil en investissement personnalisé.</p>
<h3>Déclaration d'intérêts</h3><p>Auteur : Guillaume Le Merour, étudiant en finance, sans lien avec Amundi, le groupe Crédit Agricole ou ses concurrents. L'auteur <b>ne détient aucune action Amundi</b> ni instrument lié, et n'en détiendra pas pendant la période de validité de l'objectif. L'étude n'a été ni commandée ni rémunérée ; la société n'a pas été consultée avant publication.</p>
<h3>Horizon et révision</h3><p>L'objectif vaut à douze mois, jusqu'au 20 octobre 2027. Il sera revu à chaque publication trimestrielle, à commencer par celle du 29 octobre 2026 ; toute révision est datée et motivée dans le journal public, sans retrait des versions antérieures.</p>
<h3>Propriété et conditions de reproduction</h3><p>Consultation et téléchargement libres. Reproduction, même partielle, soumise à autorisation écrite ; citation de courts extraits permise avec la mention « Sous-jacent — sousjacent.com ». Les données comptables brutes relèvent du domaine public ; ce qui est protégé est le travail de retraitement, d'analyse et de mise en forme.</p>
<h3>Le classeur</h3><p>Tous les calculs sont reproductibles dans le classeur publié avec l'étude (« amundi-comptes-2010-2025.xlsx ») : comptes publiés et ajustés, encours, pont des encours, bilan, données par action, charges et marges, ruptures de série, macroéconomie.</p>
''')

# ====================================================================== 6. CH2 THESE
railpage("Partie I · Cadre", chap("Chapitre 2", "La thèse en une page", "Posée d'entrée, pas en conclusion.") + '''
<div class="txtb" style="margin-top:5mm">
<h3>Ce qu'est Amundi</h3><p>Une machine à transformer des encours en commissions, avec une efficacité qu'aucun concurrent européen n'égale : 2 581 Md€ gérés au 30 juin 2026, un coefficient d'exploitation ajusté de 49,6 % au premier semestre, un résultat net ajusté de 1 354 M€ en 2025, et chaque plan stratégique tenu depuis 2015.</p>
<h3>Ce qui inquiète le marché</h3><p>Le contrat de distribution de dix ans signé avec UniCredit lors du rachat de Pioneer expire en juillet 2027. UniCredit retire déjà ses encours (86 Md€ fin 2025, 75 Md€ de réseaux et 14 Md€ d'assureur mi-2026). La marge nette d'Amundi sur ces réseaux, mesurée dans les prospectus italiens, est d'environ 40 pb : ≈ 300 M€ de revenus annuels sont en jeu, soit ≈ 180 M€ de résultat après impôt.</p>
<h3>Pourquoi le cours l'intègre déjà</h3><p>À 87,65 €, une fois retirées les participations cotées et le capital excédentaire, le marché paie un bénéfice de base 2027 d'environ 980 M€, au multiple justifié de 12 fois. Mon scénario, qui inclut la perte d'UniCredit en année pleine et la fin des pénalités, donne 1 037 M€.</p>
<h3>Ce que le marché ne voit pas</h3><p>SBI Funds Management, cotée en Inde depuis juillet 2026, et Victory Capital, cotée au Nasdaq, valent à elles deux ≈ 5,3 Md€ au marché, près de 30 % de la capitalisation d'Amundi. Une lecture par le PER les valorise à 12 fois alors que le marché indien paie SBI 34 fois.</p>
<h3>Ce qui limite le potentiel</h3><p>Le capital excédentaire est presque épuisé : le ratio CET1 est passé de 21,8 % fin 2024 à 12,4 % mi-2026 (CRR3, ICG, rachat de 500 M€). Les retours à l'actionnaire dépendront désormais du résultat, pas des réserves. L'objectif 2028 (« BPA ajusté supérieur à 7 € ») est déjà dépassé en rythme : il faut un nouveau récit de croissance.</p>
</div>''' + op("Prix : 94 € à douze mois (valeur intrinsèque 89,2 €, fourchette 85-94 €). Potentiel de +7 %, +12 % avec le dividende. Une valeur de qualité, correctement mais pas généreusement payée, dont la principale option de hausse — un débouché italien par Banco BPM — n'est pas dans le prix."),
 rb("Objectif à 12 mois", "94 €", "au 20/10/2027, contre 87,65 € le 19/10/2026") + rb("En jeu avec UniCredit", "≈ 300 M€", "de revenus annuels, ≈ 40 pb sur 75 Md€ [calc]") + rb("Participations cotées", "≈ 5,3 Md€", "SBI FM et Victory, au cours de marché [calc]"))

# ====================================================================== 7. INTERCALAIRE II
panel('inter', '''<img src="img/i2.jpg" style="object-position:50% 70%">
<div class="ttl" style="left:14mm;top:26mm;color:var(--navy);width:150mm"><div class="pn">Partie II</div><h1>Le terrain de jeu</h1>
<div class="man">Un métier où l'on gagne un pourcentage de ce que l'on ne possède pas, dans une Europe qui épargne beaucoup et paie de moins en moins pour la gestion.</div>
<div class="toc"><div><span>3</span>L'économie de la gestion d'actifs</div><div><span>4</span>L'économie, année par année</div><div><span>5</span>Le cadre réglementaire comme variable économique</div></div></div>
<div class="credit" style="color:#fff">Photographie : Léo Crouzille, Unsplash</div>''', folio=False)

# ====================================================================== 8. CH3 economie gestion
txtpage("Partie II · Le terrain de jeu", chap("Chapitre 3", "L'économie de la gestion d'actifs", "Un revenu adossé à un actif que l'on ne possède pas."), '''
<h3>Comment un gérant gagne de l'argent</h3><p>Un gestionnaire d'actifs ne prête pas et n'investit pas son bilan : il gère l'épargne des autres contre une commission proportionnelle aux encours, prélevée chaque jour dans les fonds. Son chiffre d'affaires s'écrit donc encours moyens × marge en points de base. Chez Amundi, en 2025 : environ 1 892 Md€ d'encours moyens hors coentreprises × ≈ 16 pb = 3 052 M€ de commissions nettes de gestion (supplément financier T4 2025).</p>
<p>Les coûts, eux, sont surtout des salaires et de l'informatique, peu sensibles aux encours à court terme : 62 % à 68 % des charges d'Amundi sont des frais de personnel chaque année depuis 2014 <span class="calc">[calc]</span>. D'où un levier opérationnel : quand les marchés montent, les revenus suivent avec un an de retard et les charges restent ; quand ils baissent, l'inverse.</p>
<h3>Deux moteurs de croissance, qui n'ont pas la même valeur</h3><p>Les encours grossissent par la collecte nette — l'argent nouveau confié par les clients, qui se « fabrique » — et par l'effet de marché, qui s'« offre ». Sur 2015-2025, les encours d'Amundi sont passés de 878 à 2 380 Md€ : 43 % de la hausse vient de la collecte, 28 % des marchés et 27 % des acquisitions <span class="calc">[calc, ch. 6]</span>.</p>
<h3>La bascule de l'actif vers le passif</h3><p>Le fait majeur de l'industrie est le basculement de la gestion active, chère, vers la gestion indicielle et les ETF, presque gratuite. En Europe, la part de la gestion passive dans les actifs des OPCVM est passée de 13 % en 2015 à 30 % en 2025 ; les ETF OPCVM ont collecté 347 Md€ en 2025, sur une collecte record de 814 Md€, pendant que les fonds actions non indiciels subissaient leur troisième année de sorties. Le coût moyen des fonds actions a baissé de 18 pb en cinq ans (EFAMA, rapport du 15/06/2026).</p>
<p>Le marché européen des ETF pèse 3,01 tn$ à fin septembre 2025 : iShares (BlackRock) en détient 40,8 %, Amundi 12,2 % (368,5 Md$, deuxième), Xtrackers (DWS) 10,5 % (ETFGI). La croissance du marché est donc là où la marge est la plus faible : c'est la cause principale de la baisse de la marge d'Amundi.</p>
<h3>Qui capte la marge</h3><p>Entre l'épargnant et le gérant se tient le distributeur — banque, assureur, conseiller — qui conserve souvent plus de la moitié des frais. Dans les fonds italiens d'Amundi vendus par UniCredit, la part reversée au réseau est de l'ordre de 62 % de la commission de gestion ; chez les réseaux de conseillers (Fideuram, Fineco, Banca Generali), elle atteint 82 % (prospectus Amundi SGR ; ch. 12). Le gérant qui contrôle sa distribution garde la marge ; celui qui en dépend la partage.</p>
''' + op("Le modèle d'Amundi est d'abord un modèle de distribution. Sa force — les réseaux de ses actionnaires — est aussi sa dépendance, et le dossier UniCredit en montre le prix."), src="Sources : Amundi, supplément financier T4 2025, URD 2014-2025 ; EFAMA, Fact Book du 15/06/2026 ; ETFGI, septembre 2025 ; prospectus Amundi SGR.")


etfmkt=[("iShares (BlackRock)",40.8),("Amundi",12.2),("Xtrackers (DWS)",10.5),("Autres",36.5)]
railpage("Partie II · Le terrain de jeu", chap("Chapitre 3, suite", "L'industrie en chiffres", "Un marché qui collecte comme jamais, et paie de moins en moins la gestion.")
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm"><div>' + bh("Part de la gestion passive", "% des actifs des OPCVM européens") + columns(["2015","2025"],[13,30],w=64,h=46,d=0,hi=[1],fmt=lambda v: fr(v,0)+" %") + '</div><div>'
 + bh("ETF européens", "parts de marché, %, septembre 2025") + hbars(etfmkt,w=64,labw=28,d=1,unit=" %",hi=[1],hi_color=CU) + '</div></div>'
 + bh("OPCVM européens en 2025", "Md€") + table(["","Montant","Lecture"],[["Collecte nette des OPCVM","814","record (EFAMA)"],["dont ETF OPCVM","347","43 % de la collecte"],["Fonds actions non indiciels","sorties","troisième année consécutive"],["Coût moyen des fonds actions","−18 pb","sur cinq ans"],["ETF européens, encours","3,01 tn$","fin septembre 2025 (ETFGI)"],["dont Amundi","368,5 Md$","n° 2 européen"]])
 + '<div class="txtb" style="margin-top:4mm;column-count:2;column-gap:6mm"><p>Le paradoxe de la période est là : l\'épargne européenne n\'a jamais autant afflué vers les fonds, mais elle va surtout vers les produits qui rapportent le moins au gérant. Pour Amundi, deuxième acteur européen des ETF, c\'est une croissance de volume qui use la marge moyenne.</p><p>Le marché des ETF est un oligopole : trois acteurs détiennent 63,5 % des encours européens. Amundi y a gagné sa place par Lyxor (2021) et par ses propres lancements ; l\'écart avec iShares reste de un à trois.</p></div><div class="src">Sources : EFAMA, rapport du 15/06/2026 ; ETFGI, septembre 2025.</div>',
 rb("Gestion passive", "30<small>%</small>", "des actifs des OPCVM européens en 2025, contre 13 % en 2015") + rb("Collecte record", "814 Md€", "pour les OPCVM européens en 2025") + rb("Amundi", "n° 2", "des ETF européens, 12,2 % du marché"))

# ====================================================================== 9-10. CH4 MACRO (table + commentaire)
mh = ["Année","Dépôt BCE<br>fin, %","Inflation<br>déc., %","PIB zone<br>euro, %","OAT<br>10 ans","Bund<br>10 ans","BTP<br>10 ans","EUR/USD","Euro Stoxx 50","ES50<br>var. %","Nasdaq<br>var. %","Encours<br>Amundi","Collecte","Marge<br>pb"]
aum_d = dict(zip(Y, AUM)); aum_d[2026] = 2581
fl_d = dict(zip(Y, FLOW)); fl_d[2026] = 56
mg_d = dict(zip(Y, MARG)); mg_d[2012] = 19.6; mg_d[2013] = 18.6; mg_d[2026] = 15.8; mg_d[2025] = 16.1
mrows = []
for r in MACRO:
    y = int(r[0])
    mrows.append([r[0] + ('*' if y == 2026 else ''), f1(r[1],2), f1(r[2]), f1(r[3]), f1(r[4],2), f1(r[5],2), f1(r[6],2), f1(r[7],3), fr(r[8],0), f1(r[9]), f1(r[11]), fr(aum_d[y],0), fr(fl_d[y],1), f1(mg_d.get(y))])
es = [r[8] for r in MACRO]; dfr = [r[1] for r in MACRO]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 4", "L'économie, année par année", "Les revenus d'Amundi sont des pourcentages d'encours ; les encours dépendent des marchés, des taux et de la peur des épargnants.")
 + bh("L'économie et Amundi", "fin d'année sauf mention") + table(mh, mrows, cls='t small')
 + '<div class="note" style="margin-top:2mm">* 2026 : taux BCE au 20/10, EUR/USD au 19/10, taux à 10 ans et Euro Stoxx en moyenne de septembre, PIB = glissement annuel du T1, encours au 30/06, collecte et marge du S1. Inflation = IPCH zone euro, glissement de décembre. Variations d\'indices de décembre à décembre sur moyennes mensuelles <span class="calc">[calc]</span>. Marge 2010-2013 et 2025 : définitions publiées de l\'année (2025 : 15,9 pb à périmètre comparable).<br>Sources : BCE, Statistical Data Warehouse ; FRED (Nasdaq) ; Amundi, rapport 2011, document de base, URD 2015-2025, communiqué S1 2026.</div>'
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm">'
 + '<div>' + bh("Euro Stoxx 50", "points, décembre") + lines([str(y) for y in range(2010,2027)], [("", es, NAVY)], w=88, h=42, ymin=2000, ymax=6600, ticks=[2000,4000,6000], d=0, lab_every=4, legend=False, fmt=lambda v: fr(v,0)) + '</div>'
 + '<div>' + bh("Encours d'Amundi", "Md€") + columns([str(y)[2:] for y in range(2010,2027)], [aum_d[y] for y in range(2010,2027)], w=88, h=42, d=0, hi=[16], lab_every=2, fmt=lambda v: fr(v,0)) + '</div></div></div>', run="Partie II · Le terrain de jeu")

years = [
("2010","La naissance.","Fusion CAAM-SGAM au 1<sup>er</sup> janvier ; crise grecque (plan du 02/05/2010). Collecte quasi nulle (+1,2 Md€) : les sorties de fonds monétaires compensent l'entrée des réseaux."),
("2011","La crise des dettes souveraines.","BTP à 6,8 % en décembre, Euro Stoxx 50 −19 %. Seule année de décollecte (−35 Md€) : selon le rapport 2011, la collecte des banques françaises a été « détournée vers l'épargne de bilan » ; les fonds monétaires font 60 % des sorties."),
("2012","« Whatever it takes ».","Discours de M. Draghi (26/07), taux de dépôt à zéro, PIB −0,9 %, marchés +15 %. Collecte +17,6 Md€, encours +14 %."),
("2013","La récession sans panique.","PIB −0,1 %, Nasdaq +38 %. Collecte +11 Md€ ; accélération en Asie par les coentreprises."),
("2014","Les taux négatifs.","Dépôt à −0,1 % puis −0,2 %, inflation négative en décembre. Bascule de l'épargne vers l'assurance-vie et le diversifié ; collecte +32,5 Md€ ; marge 16,4 pb."),
("2015","L'introduction en Bourse.","Achats d'actifs de la BCE (mars), euro à 1,09 $, krach chinois d'août. Amundi est cotée le 11/11/2015 à 45 €. Collecte +79,9 Md€."),
("2016","Brexit et Trump.","Bund négatif en juin, Euro Stoxx 50 −2,5 %. Annonce du rachat de Pioneer (12/12/2016) : la croissance externe relaie la marge."),
("2017","La reprise synchronisée.","PIB +2,8 %, euro +14 %. Intégration de Pioneer, encours +32 % ; marge remontée à 19,1 pb par les réseaux italiens."),
("2018","La fin du QE.","Crise budgétaire italienne, Euro Stoxx 50 −14 %. Collecte +42 Md€, mais l'effet marché (−43 Md€) l'efface : encours stables."),
("2019","Tout monte.","Retour des baisses de taux et du QE, Bund à −0,3 %, marchés +20 %. Collecte record +107,7 Md€ ; aucun dividende versé au titre de 2019 (recommandation BCE)."),
("2020","Le Covid.","PIB −6,2 %, PEPP. Collecte +45 Md€ ; résultat net ajusté en baisse d'environ 5 % seulement (1 009 → 962 M€)."),
("2021","L'euphorie.","PIB +6,6 %, inflation 5 % en décembre. Rachat de Lyxor (825 M€, 148 Md€) ; encours record de 2 064 Md€ ; V. Baudson directrice générale."),
("2022","Le choc des taux.","Ukraine, inflation 9,2 %, BCE de −0,5 % à 2 % ; actions et obligations baissent ensemble (Nasdaq −33 %). Encours −8 %, collecte +7 Md€ seulement."),
("2023","Le retour du rendement.","Dépôt à 4 %, faillite de SVB et sauvetage de Credit Suisse. Fonds à échéance et monétaire redeviennent faciles à vendre : collecte +25,8 Md€."),
("2024","La baisse des taux.","BCE −100 pb, dissolution en France (écart OAT-Bund ≈ 80 pb). Collecte +55,4 Md€ ; Alpha Associates, aixigo ; accord Victory."),
("2025","L'Europe redevient investissable.","Droits de douane américains (02/04), plan allemand, euro +13 %. Collecte +87,6 Md€ ; sortie d'Amundi US ; marge 15,9 pb à périmètre comparable."),
("2026","Taux longs en hausse.","OAT à 4,44 % en septembre (écart avec le Bund ≈ 100 pb), taux de dépôt 2,5 %. Collecte +56 Md€ au S1 ; action +35 % depuis janvier au 08/09."),
]
yb = ''.join(f'<p><b style="font-family:Bod;font-size:10pt;font-weight:500;color:var(--navy)">{y}</b> <i style="font-family:Bod;color:var(--navy)">{t}</i> {d}</p>' for y,t,d in years)
txtpage("Partie II · Le terrain de jeu", chap("Chapitre 4, suite", "Ce que chaque année a fait à Amundi"), yb + '<h3>Les sensibilités qu\'on en tire</h3><p>Mesurées sur 2011-2024 hors années d\'acquisition <span class="calc">[calc]</span>, les commissions de gestion ne réagissent pas aux actions la même année (corrélation −0,07) mais à la moyenne des deux dernières années (pente 0,42, corrélation 0,52) : <b>+10 % sur les actions européennes → environ +4 % de commissions l\'année suivante</b>, soit ±5 à 8 % du résultat étalé sur deux ans. La collecte, elle, réagit d\'abord aux taux et à la liquidité des banques : ses trois plus mauvaises années (2011, 2010, 2022) sont des chocs de taux ou de liquidité, pas des krachs.</p>'
 + op("Un taux de dépôt entre 2 % et 2,5 % est le meilleur des mondes pour Amundi : produits à échéance et monétaire encore vendables, actions soutenues. La hausse des taux longs français de 2026 menace moins Amundi que son actionnaire assureur."), src="Sources : BCE ; FRED ; Amundi, rapport 2011 et communiqués annuels ; régression de l'auteur dans le classeur (feuille Macro).")

# ====================================================================== 11. CH5 REGLEMENTATION
txtpage("Partie II · Le terrain de jeu", chap("Chapitre 5", "Le cadre réglementaire comme variable économique", "La question n'est pas la conformité, mais qui garde la marge entre le producteur et le distributeur."), '''
<h3>Les rétrocessions survivent</h3><p>La stratégie européenne pour l'investissement de détail (RIS) a fait l'objet d'un accord politique provisoire le 18/12/2025. Elle n'interdit pas les rétrocessions au niveau européen — les États membres peuvent le faire — mais impose de démontrer le bénéfice pour le client et de publier leur coût à part. Surtout, elle crée une évaluation « value for money » : les coûts des OPCVM et des FIA vendus aux particuliers seront comparés à des références, et un produit trop cher pourra se voir interdire la commercialisation de détail. L'application est attendue vers la fin de 2028 (Loyens & Loeff).</p>
<p>Pour Amundi, le modèle de distribution par les réseaux bancaires, rémunéré par rétrocessions, est préservé. Mais la pression sur les fonds de réseau les plus chers — ceux qui portent la marge des particuliers, 30,7 pb en 2025 contre 51,2 pb en 2014 — devient structurelle.</p>
<h3>Un gestionnaire qui est aussi une banque</h3><p>Amundi est un établissement de crédit, soumis aux exigences de fonds propres bancaires. L'entrée en vigueur de CRR3 au 1<sup>er</sup> janvier 2025 a fortement augmenté les actifs pondérés au titre du risque opérationnel : avec l'opération ICG, le ratio CET1 est tombé de 21,8 % fin 2024 à 14,3 % fin 2025 (−746 pb), puis à 12,4 % au 30/06/2026 après le rachat de 500 M€. L'exigence SREP est de 7,75 % de CET1 et 11,25 % de fonds propres totaux (URD 2025). Le capital excédentaire, qui finançait les rachats et les acquisitions, est presque consommé (ch. 16).</p>
<h3>Le reste du cadre</h3><p>MIF II impose depuis 2018 la transparence des coûts et des rétrocessions ; SFDR 2.0 est en cours de révision, et l'indicateur de durabilité sort du document d'information clé. Les fonds d'Amundi sont pour l'essentiel des OPCVM de droit français, luxembourgeois, irlandais et italien, ce qui disperse les obligations de publication (ch. 12).</p>
<h3>La fiscalité française</h3><p>Amundi a payé 71,8 M€ de contribution exceptionnelle sur les bénéfices des grandes entreprises en 2025, et 56 M€ au seul premier semestre 2026. Le projet de loi de finances 2027 la proroge pour un troisième exercice, à un taux réduit d'environ un quart (31,4 % au lieu de 41,2 % de l'impôt sur les sociétés pour un chiffre d'affaires supérieur à 3 Md€ ; Legifiscal, 01/10/2026). S'il est voté, l'effet serait d'environ +28 M€ sur le résultat 2027 <span class="calc">[calc]</span>, non intégré au prix par prudence.</p>
<h3>Sanctions</h3><p>En août 2021, la Commission des sanctions de l'AMF a infligé 32 M€ d'amende à Amundi Asset Management et Amundi Intermédiation pour des opérations de 2014-2015 sur des contrats à terme Euro Stoxx 50 ; l'amende, provisionnée, a été payée en 2021 (URD 2021). L'URD 2025 ne mentionne aucune condamnation pour corruption.</p>
''' + op("La réglementation ne menace pas le modèle ; elle en rabote la partie la plus rentable, lentement. Le vrai changement réglementaire de la période est prudentiel : CRR3 a fait d'Amundi une société qui ne peut plus rendre à ses actionnaires que ce qu'elle gagne."), src="Sources : Loyens & Loeff (RIS) ; Amundi, URD 2021 et 2025, communiqué S1 2026 ; Legifiscal, 01/10/2026 ; AMF, décision du 04/08/2021.")

# ====================================================================== 12. INTERCALAIRE III (demi-page)
panel('half', '''<div class="ph"><img src="img/i3.jpg"></div>
<div class="right" style="color:var(--navy)"><div class="pn kicker" style="color:var(--cu)">Partie III</div>
<div style="font-family:Bod;font-style:italic;font-size:40pt;line-height:1.05;margin-top:3mm">L'entreprise</div>
<div class="tick" style="margin:6mm 0 6mm;color:var(--navy)"></div>
<div style="font-size:8pt;line-height:2">''' + ''.join(f'<div style="display:flex;gap:4mm;border-bottom:.25pt solid rgba(19,42,71,.2)"><span style="font-family:Bod;width:7mm">{n}</span>{t}</div>' for n,t in [("6","Le modèle, en une mécanique"),("7","Construction de l'entreprise, 2010-2026"),("8","Implantation, effectifs, organisation"),("9","Actionnariat, contrôle, gouvernance")]) + '''</div>
<div style="font-family:Bod;font-style:italic;font-size:17pt;line-height:1.3;position:absolute;bottom:0">Une entreprise qui a triplé en achetant ce que les banques européennes vendaient, sans jamais déprécier un euro de ce qu'elle a payé.</div></div>
<div class="credit" style="left:95mm;color:#fff">Photographie : Michael Yuan, Unsplash</div>''', folio=False)

# ====================================================================== 13. CH6 MODELE (pont)
cats = [str(y) for y in range(2015, 2026)]
col_ = [79.9,62.2,70.6,42.0,107.7,45.1,60.2,7.0,25.8,55.4,87.6]
mkt_ = [22.4,21.8,27.4,-43.1,120.6,9.5,121,-167.0,127.2,139.8,61.9]
per_ = [5.3,13.6,242.9,0,0,20.7,148,0,-20,7.9,-9.7]
railpage("Partie III · L'entreprise", chap("Chapitre 6", "Le modèle, en une mécanique", "Encours × marge − coûts. Le reste est commentaire.") + bh("D'où vient la variation des encours", "Md€ par an") + stacked(cats, [("Collecte", col_, NAVY), ("Marché et change", mkt_, "#8E9DB2"), ("Acquisitions", per_, CU)], w=136, h=62) + legend([("Collecte nette", NAVY), ("Marché et change", "#8E9DB2"), ("Périmètre", CU)]) + '''
<div class="txtb" style="margin-top:5mm;column-count:2;column-gap:6mm">
<p>La mécanique tient en une ligne : revenus = encours moyens × marge ; résultat = revenus − charges, à peu près fixes. Tout le reste de l'étude est la décomposition de ces trois termes.</p>
<p><b>Croissance fabriquée et croissance offerte.</b> Sur 2015-2025, la collecte nette apporte +644 Md€ (43 % de la hausse des encours), les marchés et le change ≈ +420 Md€ (28 %), les acquisitions ≈ +409 Md€ (27 %) <span class="calc">[calc]</span>. La croissance organique — collecte rapportée aux encours de début d'année — est de 4,3 % par an en moyenne, mais seulement 0,3 % à 2,7 % sur 2022-2024 avant de remonter à 3,9 % en 2025.</p>
<p><b>Deux années de vérité.</b> En 2018 (−43 Md€) et 2022 (−167 Md€), l'effet de marché a effacé la collecte. Le pont 2021 est approché : l'effet de marché est obtenu par différence (≈ 121 Md€) faute de décomposition publiée isolant Lyxor.</p>
<p><b>Ce que la mécanique implique.</b> Une baisse de 1 pb de marge coûte ≈ 189 M€ de revenus (1 892 Md€ d'encours moyens) ; une baisse de 10 % des actions, ≈ 4 % des commissions l'année suivante (ch. 4). La marge est le paramètre que le management ne contrôle pas, le coût celui qu'il contrôle.</p>
</div><div class="src">Sources : communiqués annuels 2015-2025 (encours, collecte, effets marché et périmètre) ; résidu de contrôle ≤ 2 Md€ par an ; classeur, feuille Pont_encours.</div>''',
 rb("Encours 2015 → 2025", "×2,7", "de 878 à 2 380 Md€") + rb("Part de la collecte", "43<small>%</small>", "de la hausse des encours, le reste vient des marchés et des acquisitions [calc]") + rb("Croissance organique", "4,3<small>%</small>", "par an en moyenne, 0,3 % seulement en 2022"))

# ====================================================================== 14. CH7 CONSTRUCTION — tableau
ops = [["2003","Gestion de CA Indosuez","intra-groupe","—","377,9"],["2004","Gestion du Crédit Lyonnais","intra-groupe","—","1 732,8"],["2009","Apport de SGAM (25 % du capital)","apport","—","707,8"],
 ["2011","BFT Gestion","non publié","20,8 Md€","—"],["2015","BAWAG PSK Invest","non publié","—","78,4"],["2016","KBI Global Investors","154,5 M€","8,6 Md€","159,9 (avec CA Immobilier Investors)"],
 ["2017","<b>Pioneer Investments</b>","<b>3 545 M€</b>","≈ 243 Md€","1 886,8"],["2020","Sabadell AM","430 M€ + 30 M€ d'earn-out","21,8 Md€","335,0"],["2021","<b>Lyxor</b>","<b>825 M€</b>","148 Md€","654,5"],
 ["2024","Alpha Associates","350 M€ (dont 190 d'earn-out)","8,5 Md€","288,2"],["2024","aixigo (technologie)","non publié","—","121,0"],["2025","Amundi US → Victory Capital","apport, 0 cash","—","plus-value 402,1"],["2025","ICG (4,64 % → 9,9 %)","317,5 M€ pour 4,64 %","—","—"],["2026","SBI FM : cession de 3,7 % à l'IPO","+≈ 300 M€ de plus-value nette","—","—"]]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 7", "Construction de l'entreprise, 2010-2026", "Ce que chaque opération a coûté, apporté, et laissé au bilan.")
 + bh("Les opérations", "M€ sauf mention ; écart d'acquisition au bilan fin 2025") + table(["Année","Opération","Prix payé","Encours acquis","Écart d'acquisition"], ops, hl=[6,8])
 + '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-top:5mm;font-size:8.4pt;line-height:1.42">
<div><h3>Le prix payé par euro d'encours</h3><p>Pioneer : 3 545 M€ pour ≈ 243 Md€ d'encours consolidés au T3 2017, soit ≈ 1,5 % des encours, ou ≈ 15,6 fois les 227 M€ de résultat net de Pioneer en 2015 <span class="calc">[calc]</span>. Lyxor : 825 M€ pour 148 Md€, soit ≈ 0,56 % des encours et ≈ 20 fois un résultat estimé à 40-42 M€. Sabadell : 430 M€ pour 21,8 Md€ (≈ 2 %), avec dix ans de distribution exclusive. Le prix suit la marge de ce qui est acheté : un réseau de détail italien vaut trois fois un encours d'ETF.</p>
<h3>Ce que les promesses sont devenues</h3><p>Pioneer : synergies de 180 M€ visées (150 de coûts, 30 de revenus), coûts d'intégration constatés de 191 M€ contre 190 annoncés, BPA ajusté +36 % entre 2016 et 2018 (3,46 € → 4,69 €) <span class="calc">[calc]</span>. Lyxor : 78 M€ de coûts d'intégration constatés contre 70 M€ annoncés ; la réalisation des 90 M€ de synergies n'est pas publiée isolément.</p></div>
<div><h3>Le bilan qu'elles laissent</h3><p>Les écarts d'acquisition atteignent 6 560,6 M€ fin 2025, pour 12 655 M€ de capitaux propres part du groupe. Le test de 2025 retient un taux d'actualisation de 8,1 % et une croissance perpétuelle de 2 % ; une variation de ±50 pb ne change pas la conclusion. Aucune dépréciation d'écart d'acquisition n'apparaît dans les comptes relus de 2015 à 2025.</p>
<h3>Le changement de doctrine de 2024-2025</h3><p>Après les rachats de taille (Pioneer, Lyxor), Amundi achète des capacités : actifs privés (Alpha Associates, ICG), technologie (aixigo), accès au marché américain sans le gérer (Victory Capital, échange d'Amundi US contre 26,1 % du capital dilué et quinze ans de distribution réciproque).</p></div></div>'''
 + op("Discipline d'allocation : bonne. Les deux grands rachats ont tenu leurs chiffres, aucun n'a été déprécié, et le groupe a su vendre (Amundi US) autant qu'acheter. Le point faible est humain : les équipes dirigeantes acquises ne restent pas (ch. 10).")
 + '<div class="src">Sources : URD 2025, note 5.13 (écarts d\'acquisition) ; communiqués Pioneer (12/12/2016), Sabadell (21/01/2020), Lyxor (31/12/2021), Alpha Associates (Swissinfo 23/02/2024), Victory Capital (SEC, 2025), ICG (18/11/2025), SBI FM (17/07/2026) ; URD 2016 (KBI).</div></div>', run="Partie III · L'entreprise")

# ====================================================================== 15-19. FICHES EVENEMENT
def fiche(img, pos, color, box_style, name, chapo, fields, why, nums, credit, veil=False, objpos="50% 50%"):
    flds = ''.join(f'<div><b>{k}</b><span>{v}</span></div>' for k, v in fields)
    nm = ''.join(f'<div><div class="n">{n}</div><div class="c">{c}</div></div>' for n, c in nums)
    vb = ' veilbox' if veil else ''
    panel(f'fiche {color}', f'''<img src="img/{img}" style="object-position:{objpos}">
<div class="box{vb}" style="{box_style}"><div class="band">Événement structurant</div><h2>{name}</h2><div class="ch">{chapo}</div>
<div class="id">{flds}</div><div class="why"><h4>Pourquoi cela compte</h4>{why}</div><div class="nums">{nm}</div></div>
<div class="credit" style="color:{'#fff' if color=='white' else '#222'}">Photographie : {credit}, Unsplash</div>''', folio=False)

fiche("f2010.jpg", "", "ink", "right:8mm;top:12mm", "La fusion", "Deux banques mettent leur gestion en commun, et l'une garde la main.",
 [("Exercice","2010"),("Nature","Fusion CAAM (Crédit Agricole) et SGAM (Société Générale)"),("Effet","Toujours visible : 707,8 M€ d'écart d'acquisition au bilan"),("Périmètre","France, Europe, coentreprises asiatiques"),("Date d'annonce","26/01/2009 ; accord définitif 09/07/2009")],
 "<p>Répartition 75 % / 25 % sans soulte ni valorisation publiée ; Yves Perrier, patron de CAAM, prend la direction. Les accords de distribution quasi exclusifs signés le 31/12/2009 avec les réseaux des deux banques fondent le modèle : en 2015 encore, 56 % des encours dépendaient des deux groupes <span class='calc'>[calc]</span>. Société Générale garde Lyxor, qu'Amundi rachètera onze ans plus tard.</p>",
 [("591 Md€","encours combinés annoncés, 4e européen"),("150 M€","synergies réalisées en 2011, contre 120 visées")], "Jess Morgan", veil=True)
fiche("f2015.jpg", "", "ink", "right:8mm;top:12mm", "L'introduction en Bourse", "Société Générale sort, Crédit Agricole reste à 75,7 %.",
 [("Exercice","2015"),("Nature","Cession par SG de ses 20 % ; offre réservée aux salariés"),("Effet","Toujours visible : un flottant de ≈ 28 %, un actionnaire de contrôle"),("Périmètre","Euronext Paris"),("Date","Prix fixé le 11/11/2015, 45,00 €")],
 "<p>Fourchette indicative 42,00-52,50 € : prix dans le bas, capitalisation ≈ 7,5 Md€, contre 6,75 Md€ implicites lors du rachat de 5 % par CA S.A. en mai 2014 <span class='calc'>[calc]</span>. Un investisseur lié à Agricultural Bank of China achète ≈ 2 % : le partenaire chinois devient actionnaire. Promesse : au moins 60 % de distribution ; tenue à 65 % dès 2015.</p>",
 [("45,00 €","prix d'introduction"),("+95 %","de cours au 19/10/2026, hors dividendes [calc]")], "Valentin Lacoste", veil=True, objpos="50% 60%")
fiche("f2017.jpg", "", "ink", "right:8mm;top:12mm", "Pioneer", "Le rachat qui a fait d'Amundi un groupe italien, et lié son destin à UniCredit.",
 [("Exercice","2017"),("Nature","Acquisition de Pioneer Investments auprès d'UniCredit"),("Effet","Toujours visible : 1 886,8 M€ d'écart d'acquisition ; contrat jusqu'en juillet 2027"),("Périmètre","Italie, Allemagne, Autriche, Europe centrale, États-Unis"),("Date d'annonce","12/12/2016 ; finalisée le 03/07/2017")],
 "<p>3 545 M€ en numéraire, financés par une augmentation de capital de ≈ 1,4 Md€ (une action nouvelle pour cinq à 42,50 €) et ≈ 1,5 Md€ de capital excédentaire. La marge remonte de 16,0 à 19,1 pb grâce aux réseaux de détail italiens. Le contrat de distribution de dix ans imposait que ≈ 75 % des actifs gérés par UniCredit pour ses clients italiens soient des produits Amundi : c'est lui qui expire en 2027.</p>",
 [("+36 %","de BPA ajusté entre 2016 et 2018 [calc]"),("191 M€","coûts d'intégration, pour 190 annoncés")], "Wassim Chouak", veil=True, )
fiche("f2021.jpg", "", "ink", "right:8mm;top:12mm", "Lyxor", "Société Générale vend enfin son ETF, et Amundi devient le numéro deux européen.",
 [("Exercice","2021"),("Nature","Acquisition de Lyxor auprès de Société Générale"),("Effet","Toujours visible : 654,5 M€ d'écart d'acquisition ; ETF > 400 Md€ en 2026"),("Périmètre","Europe, ETF et gestion indicielle"),("Date","Signature avril 2021 ; finalisée le 31/12/2021")],
 "<p>825 M€ en numéraire pour 148 Md€ d'encours, finalisé deux mois avant la date prévue. Le pari : la gestion passive, presque sans marge, mais avec la plus forte collecte du marché. En 2025, les ETF apportent +46,5 Md€ sur une collecte totale de +87,6 Md€. Les dirigeants de Lyxor ne restent pas : le responsable ETF issu de Lyxor part au bout de deux ans, remplacé par un ancien de BlackRock.</p>",
 [("0,56 %","prix payé par euro d'encours [calc]"),("412 Md€","ETF et ETC au 30/06/2026")], "Bastien Nvs", veil=True)
fiche("f2025.jpg", "", "ink", "right:8mm;top:12mm", "Victory, SBI, ICG", "Amundi cesse de gérer partout pour posséder des participations là où elle ne peut pas gérer.",
 [("Exercice","2025-2026"),("Nature","Apport d'Amundi US à Victory ; IPO de SBI FM ; entrée au capital d'ICG"),("Effet","En cours : ≈ 5,3 Md€ de participations cotées [calc]"),("Périmètre","États-Unis, Inde, actifs privés"),("Dates","01/04/2025 ; 18/11/2025 ; 21/07/2026")],
 "<p>Amundi US est échangée contre 26,1 % du capital dilué de Victory Capital (4,6 % des voix), avec quinze ans de distribution réciproque et une plus-value non monétaire de 402,1 M€. SBI FM, coentreprise indienne depuis 2011, est introduite en Bourse : Amundi cède 3,7 % (≈ 300 M€ de plus-value nette au T3 2026) et garde ≈ 32,4 %. ICG : 4,64 % pour 317,5 M€, cible 9,9 %.</p>",
 [("≈ 3,07 Md€","part de SBI FM au cours du 19/10/2026 [calc]"),("≈ 2,21 Md€","part de Victory au même cours [calc]")], "Harsh Kondekar", veil=True)

# ====================================================================== 20. CH8 IMPLANTATION
geo = [("France",1050.5),("Reste de l'Europe",517.1),("Asie",475.0),("Italie",199.2),("Reste du monde",138.2)]
staff = [("France",2909),("Autres pays de l'UE",1652),("Asie hors Japon",262),("Europe hors UE",251),("Japon",164),("Amérique du Nord",116)]
railpage("Partie III · L'entreprise", chap("Chapitre 8", "Implantation, effectifs, organisation", "Une holding française, une société de gestion principale, et des marques qui survivent aux fusions.")
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm">' + '<div>' + bh("Encours par géographie", "Md€, fin 2025") + hbars(geo, w=64, labw=26, d=1) + '</div><div>' + bh("Effectifs", "ETP, fin 2025") + hbars(staff, w=64, labw=26, d=0, color="#647793") + '</div></div>' + '''
<div class="txtb" style="margin-top:4mm;column-count:2;column-gap:6mm">
<p><b>La structure.</b> Amundi SA, holding cotée et établissement de crédit, contrôle Amundi Asset Management, la société de gestion principale. Autour d'elle, des sociétés de gestion françaises à 100 % : CPR Asset Management, BFT et Société Générale Gestion (S2G), Amundi Immobilier, Amundi Private Equity Funds, Amundi Transition Énergétique ; et des fonctions : Amundi Finance (garanties), Amundi ESR (épargne salariale), Amundi Intermédiation (table de négociation).</p>
<p><b>À l'étranger.</b> Amundi SGR (Italie), Amundi Deutschland et aixigo (Allemagne), KBI Global Investors (Irlande), Sabadell AM (Espagne), Amundi Alpha Associates (Suisse), Fund Channel (Luxembourg, 68,7 %), Amundi-BOC Wealth Management (Chine, 55 %), et une présence dans 35 pays.</p>
<p><b>Les coentreprises</b>, mises en équivalence : SBI Funds Management (Inde, ≈ 32,4 % après l'IPO), ABC-CA (Chine, 33,3 %), NH-Amundi (Corée, 30 %), Wafa Gestion (Maroc, 34 %). Leur quote-part de résultat 2025 : 135,2 M€, dont 112,9 M€ pour SBI FM (URD 2025).</p>
<p><b>Les effectifs.</b> 2 915 ETP fin 2010, 5 366 ETP consolidés fin 2025 (≈ 5 600 selon le communiqué) ; 42 % de femmes. Revenus ajustés par ETP ≈ 637 k€, frais de personnel par ETP ≈ 224 k€ <span class="calc">[calc]</span>. L'Amérique du Nord passe de 459 à 116 ETP avec l'apport d'Amundi US à Victory.</p>
</div><div class="src">Sources : URD 2025 (organisation juridique, note 9.3, données sociales ESRS S1) ; rapport 2011 ; communiqué T4 2025.</div>''',
 rb("Hors de France", "56<small>%</small>", "des encours fin 2025 (1 329 Md€)") + rb("Italie", "199 Md€", "−9,0 Md€ de collecte en 2025, −14,5 en 2024") + rb("Effectif", "5 366", "ETP consolidés, ×1,8 depuis 2010"))

# ====================================================================== 21. CH9 GOUVERNANCE
board = [["Olivier Gavalda","62","Président","2025","DG de Crédit Agricole S.A."],["Pierre Cambefort","61","Administrateur","2025","DGA de CA S.A."],["Patrice Gentié","62","Administrateur","2021","Président de Caisse régionale"],["Gérald Grégoire","51","Administrateur","2024","DGA de CA S.A."],["Michèle Guibert","58","Prés. comité des risques","2020","DG de Caisse régionale"],["Clotilde L'Angevin","47","Administratrice","2025","Comité exécutif de CA S.A."],["Nicolas Mauré","49","Administrateur","2025","Président de Caisse régionale"],["Virginie Cayatte","55","Indépendante, prés. audit","2015","—"],["Laurence Danon-Arnaud","69","Indépendante, prés. stratégie et rémunérations","2015","—"],["Jean-Christophe Mieszala","60","Indépendant","2025","ex-McKinsey"],["Hélène Molinari","62","Indépendante, prés. nominations","2015","—"],["Nathalie Wright","61","Indépendante","2022","—"],["Joseph Ouedraogo","50","Élu par les salariés","2022","—"]]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 9", "Actionnariat, contrôle, gouvernance", "Une société cotée dont le conseil est d'abord celui de son actionnaire.")
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm">'
 + '<div>' + bh("Actionnariat", "% du capital") + table(["Date","Groupe CA","SG","Salariés","Flottant","Autodét."],[["2010","75","25","—","—","—"],["mai 2014","80","20","—","—","—"],["fin 2015","75,7","0","≈ 0,2","≈ 24","—"],["fin 2017","70,0","—","0,2","29,8","0,0"],["fin 2019","69,8","—","0,5","29,1","0,7"],["fin 2025","68,3","—","2,4","28,4","0,8"],["30/06/2026","68,3","—","—","—","2,33"]]) + '''
<div style="font-size:8.2pt;line-height:1.42;margin-top:3mm"><p>Le groupe Crédit Agricole détient 141 057 399 actions, inchangées depuis 2017. Une action vaut une voix : avec 68,3 %, il conserve seul la majorité des deux tiers en assemblée extraordinaire, avec une marge de 1,6 point <span class="calc">[calc]</span>. Le rachat de 500 M€, destiné à l'annulation, l'augmentera mécaniquement.</p>
<p>La présidence revient au directeur général (ou délégué) de CA S.A. : J.-P. Chifflet jusqu'au 28/04/2016, X. Musca ensuite, Y. Perrier pendant la transition 2021-2023, P. Brassac, puis O. Gavalda depuis le 27/05/2025. Le président renonce à toute rémunération.</p></div></div>'''
 + '<div>' + bh("Le conseil au 31/12/2025", "13 membres") + table(["Nom","Âge","Rôle","Depuis","Fonction"], board, cls='t small') + '<div class="note" style="margin-top:1.5mm">7 membres issus du groupe CA, 5 indépendants (38 %), 1 salarié. Chaque administrateur détient environ 200 actions. Commissaires aux comptes : Forvis Mazars (depuis 2021) et Deloitte & Associés (depuis l\'exercice 2025, après PwC).</div></div></div>'
 + bh("Rémunération de la directrice générale", "k€, fixe + variable attribué") + table(["", "2022", "2023", "2024", "2025", "Repère"], [["V. Baudson, directrice générale","1 952","2 343","2 376","2 670","−56 % sous la médiane de 8 gérants européens cotés"],["N. Calcoen, directeur général délégué","—","—","—","1 335","ratio d'équité France 20,5, contre 54 au SBF 120"]])
 + op("Un actionnaire de contrôle discipliné, qui ne prélève pas de rémunération et laisse la direction tenir ses plans, mais qui arbitre au niveau du groupe : le dossier UniCredit montre qu'un intérêt de Crédit Agricole S.A. en Italie (Banco BPM) peut primer sur celui des minoritaires d'Amundi. C'était le risque n° 4.4.1 du document de base de 2015.")
 + '<div class="src">Sources : URD 2015-2025 (actionnariat, gouvernement d\'entreprise, rémunérations) ; communiqué S1 2026 ; document de base.</div></div>', run="Partie III · L'entreprise")

# ====================================================================== 22. INTERCALAIRE IV-V (pleine page)
panel('inter', '''<img src="img/i5.jpg" style="object-position:50% 50%">
<div class="ttl" style="left:14mm;top:22mm;color:var(--navy);width:120mm"><div class="pn">Parties IV à VI</div><h1>Le métier, de l'intérieur</h1>
<div class="man">Ceux qui dirigent Amundi, ce qu'elle vend et à quel prix, et d'où viennent ses clients.</div>
<div class="toc"><div><span>10</span>Qui dirige, et d'où ils viennent</div><div><span>11</span>La gamme, famille par famille</div><div><span>12</span>Les prix réels</div><div><span>13</span>La performance des fonds</div><div><span>14</span>Par où arrivent les encours</div></div></div>
<div class="credit" style="color:#333">Photographie : Martin Gleizes, Unsplash</div>''', folio=False)

# ====================================================================== 23. CH10 DIRIGEANTS
txtpage("Partie IV · Les gens", chap("Chapitre 10", "Qui dirige, et d'où ils viennent", "Une maison qui promeut ses dirigeants, et laisse partir ceux qu'elle achète."), '''
<h3>La direction depuis le 18 mai 2026</h3><p>Cinq pôles : Stratégie, Finance et Contrôle (Nicolas Calcoen, directeur général délégué) ; Clients (Fannie Wurtz, directrice générale déléguée) ; Investissements (Vincent Mortier, directeur général délégué) ; Opérations et Technologie (Claire Cornil) ; Transformation, RH et Communication (Sarah Finkelstein). Trois régions : Europe (Olivier Mariée), Asie (F. Wurtz), Amérique du Nord (N. Calcoen). Trois directeurs généraux délégués au lieu d'un : la succession de la directrice générale devient lisible.</p>
<h3>Valérie Baudson, directrice générale depuis le 10/05/2021</h3><p>HEC. Inspection générale de la Banque Indosuez (1995), Crédit Agricole Cheuvreux, Amundi en 2007, où elle fonde la ligne ETF, indiciel et smart beta (2008) ; directrice générale de CPR AM (2016), puis de la distribution tierce et de la banque privée (2020). Directrice générale adjointe et membre du comité exécutif de CA S.A.</p>
<h3>Les trois délégués</h3><p><b>Nicolas Calcoen</b> : ENA (1998), Direction du Budget, FMI (2002-2005), cabinets ministériels, Amundi en 2010, directeur financier en 2012 ; administrateur de Victory Capital depuis le 23/07/2026. <b>Vincent Mortier</b> : ESCP, filière Société Générale (audit, SG CIB, directeur financier de la division banque de financement), Amundi en 2015, directeur des investissements en 2022 ; administrateur d'ICG depuis le 31/03/2026. <b>Fannie Wurtz</b> : ESC Bordeaux ; State Street, KPMG, Fidelity, Schroders ; Amundi en 2011, responsable des ETF en 2016, de la distribution et de la gestion de fortune en 2021 ; vice-présidente de l'AFG.</p>
<h3>Les autres parcours publiés</h3><p><b>Claire Cornil</b>, directrice des opérations au 01/04/2026 : CACIB (1998), produits structurés chez Amundi, directrice générale de Société Générale Gestion (2023). <b>Olivier Mariée</b> : presque trente ans chez AXA (jusqu'à la direction de Direct Assurance), directeur général de CPR AM en 2021. <b>Cinzia Tagliabue</b>, Italie : plus de trente ans dans l'univers UniCredit, Pioneer de 2001 à 2018 ; elle porte la relation UniCredit. Aucune biographie publiée n'a été trouvée pour Sarah Finkelstein.</p>
<h3>Cartographie des filières</h3><p>Le sommet est d'abord issu du groupe Crédit Agricole (Baudson, Calcoen, Cornil) et de Société Générale par la fusion de 2010 (Mortier). Les recrues externes viennent de la distribution (Wurtz, Mariée). Les deux grandes acquisitions n'ont pas fourni de dirigeants durables : le directeur général de Pioneer, Giordano Lombardo, quitte le groupe dès la fusion (juin 2017) ; le responsable ETF venu de Lyxor, Arnaud Llinas, part au bout d'environ deux ans, remplacé par Benoit Sorel, recruté chez BlackRock.</p>
<h3>Les départs de 2026</h3><p>Jean-Jacques Barbéris (institutionnels, ESG) devient directeur général délégué de CACEIS (proposé le 19/05/2026). Dominique Carrel-Billiard quitte Amundi et le conseil de Victory au 23/07/2026. Guillaume Lesage n'apparaît plus au comité ; aucun communiqué n'a été trouvé sur son sort.</p>
''' + op("Amundi est une maison qui promeut : ses dirigeants ont fait carrière dans le groupe et en connaissent l'actionnaire. C'est une force pour l'exécution, et la raison pour laquelle l'intérêt du groupe Crédit Agricole est rarement contesté de l'intérieur."), src="Sources : communiqué « Nominations » du 18/05/2026 ; URD 2025 ; Crédit Agricole S.A. ; ICG ; Victory Capital (2026) ; Option Finance (19/05/2026) ; Bluerating (23/06/2017) ; ETF Stream. Informations professionnelles publiées uniquement.")


ppl=[["Valérie Baudson","Directrice générale (2021)","HEC","Indosuez, CA Cheuvreux, Amundi 2007","Crédit Agricole"],["Nicolas Calcoen","DG délégué, Stratégie et Finance","ENA, Sciences Po","Budget, FMI, cabinets ; Amundi 2010","Crédit Agricole"],["Vincent Mortier","DG délégué, Investissements","ESCP","Société Générale 1996-2015","ex-SG"],["Fannie Wurtz","DG déléguée, Clients ; Asie","ESC Bordeaux","State Street, KPMG, Fidelity, Schroders ; Amundi 2011","externe"],["Claire Cornil","Opérations et Technologie (2026)","Sciences Po, droit","CACIB, CASAM, SG Gestion","Crédit Agricole"],["Olivier Mariée","Europe ; JV et réseaux","ISG","AXA 1992-2021 ; CPR AM 2021","externe"],["Cinzia Tagliabue","Italie","n.p.","Pioneer 2001-2018","ex-Pioneer"],["Sarah Finkelstein","Transformation, RH, Communication","n.p.","n.p.","n.p."],["Céline Boyer-Chammard","Secrétaire générale","n.p.","administratrice de Victory 2025","n.p."],["Benoit Sorel","ETF et indiciel","n.p.","BlackRock","externe"]]
gone=[["Giordano Lombardo","DG et CIO de Pioneer","quitte le groupe dès la fusion","juin 2017"],["Arnaud Llinas","Responsable ETF, venu de Lyxor","part au bout d'environ deux ans","≈ 2023"],["Jean-Jacques Barbéris","Institutionnels, ESG","DG délégué de CACEIS","mai 2026"],["Dominique Carrel-Billiard","Actifs réels ; Victory","quitte Amundi","juillet 2026"],["Guillaume Lesage","Directeur des opérations","n'est plus au comité ; sort non publié","mai 2026"]]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 10, suite", "Cartographie des filières", "Qui vient d'où, et qui reste.")
 + bh("La direction en 2026", "parcours publiés") + table(["Nom","Fonction","Formation","Parcours","Filière"], ppl, cls='t small')
 + bh("Ceux qui sont partis", "acquisitions et réorganisation de 2026") + table(["Nom","Rôle","Ce qui s'est passé","Date"], gone, cls='t small')
 + '<div style="display:grid;grid-template-columns:repeat(4,1fr);margin-top:6mm;border-top:1.5pt solid #000">' + ''.join(f'<div style="text-align:center;padding:5mm 2mm"><div style="font-family:Bod;font-size:26pt;color:var(--navy)">{n}</div><div style="font-size:7pt;line-height:1.35;margin-top:1mm">{l}</div></div>' for n,l in [("3 / 8","dirigeants formés dans le groupe Crédit Agricole"),("1","issu de Société Générale (fusion de 2010)"),("1","issue de Pioneer, aucune de Lyxor"),("3","recrutés à l\'extérieur")]) + '</div>'
 + '<div class="note" style="margin-top:2mm">n.p. : non publié ou non trouvé. Comptage de l\'auteur sur les huit parcours publiés du tableau (hors S. Finkelstein et C. Boyer-Chammard). Informations professionnelles publiées uniquement : communiqué du 18/05/2026, URD 2025, Crédit Agricole S.A., Victory Capital, Option Finance, Bluerating, ETF Stream.</div></div>', run="Partie IV · Les gens")

# ====================================================================== 24. CH11 GAMME
cls = [("Obligations",761),("Actions",623),("Diversifiés",286),("Monétaire",180),("Privé, alternatif, structuré",106)]
act = [("Gestion active",1153),("ETF et ETC",342),("Indiciel",175),("Monétaire",180),("Privé et alternatif",65),("Produits structurés",40)]
railpage("Partie V · Ce qui est vendu", chap("Chapitre 11", "La gamme, famille par famille", "Moins d'un quart de l'encours est passif ; il fait l'essentiel de la collecte.")
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm"><div>' + bh("Par classe d'actifs", "Md€, fin 2025, hors JV") + hbars(cls, w=64, labw=30, d=0) + '</div><div>' + bh("Par type de gestion", "Md€, fin 2025, hors JV") + hbars(act, w=64, labw=28, d=0, hi=[1,2], hi_color=CU) + '</div></div>' + '''
<div class="txtb" style="margin-top:4mm;column-count:2;column-gap:6mm">
<p>Fin 2025, les 1 956 Md€ hors coentreprises se répartissent entre obligations (39 %), actions (32 %), diversifiés (15 %), monétaire (9 %) et actifs privés, alternatifs et structurés (5 %) <span class="calc">[calc]</span>. Par mode de gestion : 1 153 Md€ de gestion active, 518 Md€ d'ETF et d'indiciel, 180 Md€ de monétaire, 65 Md€ d'actifs privés et alternatifs, 40 Md€ de produits structurés.</p>
<p><b>La collecte de 2025 dit où va la gamme</b> : passif +75,6 Md€ (dont ETF +46,5), actif +13,2, alternatif −2,1, monétaire −11,7. Au 30/06/2026, les ETF et ETC atteignent 412 Md€.</p>
<p><b>Les autres familles.</b> L'épargne salariale et retraite (103,8 Md€ fin 2025, objectif +100 Md€ de retraite d'ici 2028), les actifs réels et privés (Amundi Immobilier, Alpha Associates, ICG), et Amundi Technology, qui vend la plateforme de gestion d'Amundi à d'autres sociétés : 116 M€ de revenus en 2025, objectif ×2 sur le plan.</p>
<p><b>Les objectifs du plan 2028</b> : +100 ETF, +150 Md€ en Asie, +50 % de distributeurs numériques, 800 M€ d'investissements organiques, 50 applications d'intelligence artificielle (communiqué du 18/11/2025).</p>
</div><div class="src">Sources : communiqué T4 2025 (encours par classe et par type, collecte) ; communiqué S1 2026 ; URD 2025 ; plan « Invest for the future » du 18/11/2025.</div>''',
 rb("ETF et indiciel", "518 Md€", "26 % de l'encours hors JV, +75,6 Md€ de collecte passive en 2025") + rb("Gestion active", "1 153 Md€", "59 % de l'encours, +13,2 Md€ seulement") + rb("Technologie", "116 M€", "de revenus en 2025, objectif ×2"))

# ====================================================================== 25. CH12 PRIX REELS
etf_bands = [("≤ 0,10 %",31),("0,11-0,20 %",42),("0,21-0,30 %",18),("0,31-0,45 %",6),("> 0,45 %",3)]
etfj = json.load(open('/root/amundi/etf.json'))
A = sum(x['size'] or 0 for x in etfj)
def band(lo, hi): return sum(x['size'] or 0 for x in etfj if x['ter'] is not None and lo < x['ter'] <= hi)/A*100
eb = [("≤ 0,10 %", band(-1,.10)), ("0,11-0,20 %", band(.10,.20)), ("0,21-0,30 %", band(.20,.30)), ("0,31-0,45 %", band(.30,.45)), ("> 0,45 %", band(.45,9))]
railpage("Partie V · Ce qui est vendu", chap("Chapitre 12", "Les prix réels", "Deux mondes : un monde de volume à quelques points de base, un monde de réseau où le banquier garde la moitié.")
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm"><div>' + bh("Les 636 ETF d'Amundi", "% des encours par tranche de frais") + hbars(eb, w=64, labw=22, d=0, unit=" %") + '</div><div>' + bh("Un fonds de réseau italien", "pb, gamme UniCredit 2016") + hbars([("Frais facturés",110.8),("Part du réseau",65.9),("Reste à Amundi",44.9)], w=64, labw=22, d=0, unit=" pb", hi=[2], hi_color=CU) + '</div></div>' + '''
<div class="txtb" style="margin-top:4mm;column-count:2;column-gap:6mm">
<p><b>Le relevé ETF.</b> Les 636 ETF et ETC d'Amundi référencés par justETF le 20/10/2026 totalisent 425,9 Md€ (cohérent avec les 412 Md€ publiés au 30/06). Frais moyens pondérés par les encours : <b>17,5 pb</b> ; médiane 20 pb ; 31 % des encours à 10 pb ou moins. Revenu brut théorique : ≈ 746 M€ par an, avant les coûts d'indices et de réplication <span class="calc">[calc]</span>. Les dix premiers ETF font 25 % des encours, les cinquante premiers 58 %.</p>
<p><b>Les réseaux italiens.</b> La réglementation italienne oblige chaque prospectus à publier la part moyenne des frais reversée aux distributeurs. Sur les quinze fonds de la gamme ex-Pioneer vendue par UniCredit (13,7 Md€ fin 2016), la commission de gestion pondérée est de 110,8 pb, la part du réseau de 59,4 % et le net pour la société de gestion de <b>44,9 pb</b> <span class="calc">[calc]</span>. Les produits à échéance plus récents (2025) ne laissent que 20 à 27 pb ; les réseaux de conseillers (Fideuram, Fineco, Banca Generali) prennent jusqu'à 83 %.</p>
<p><b>Un fonds de réseau français</b> à 1,65 % de frais courants (Amundi Patrimoine) face à une marge nette de ≈ 31 pb sur les particuliers : environ les deux tiers à trois quarts des frais payés par l'épargnant ne restent pas chez Amundi <span class="calc">[calc, ordre de grandeur]</span>.</p>
<p><b>Limites.</b> justETF donne des frais affichés, pas des revenus nets ; les SICAV luxembourgeoises, qui portent l'essentiel des encours UniCredit actuels, ne publient pas la part distributeur. Le relevé exhaustif des milliers de documents d'information clés n'a pas été fait.</p>
</div><div class="src">Sources : justETF, page fournisseur Amundi (20/10/2026) ; prospectus Amundi SGR (Sistema Amundi Fondi Italia 2016, Sistema Amundi Investi 2025, Fondi Amundi 2024) ; Mémo CA (17/01/2023) ; tableau des 40 fonds dans le classeur.</div>''',
 rb("Frais ETF pondérés", "17,5 pb", "sur 425,9 Md€, médiane 20 pb [calc]") + rb("Net UniCredit", "≈ 45 pb", "sur 111 pb facturés, gamme historique [calc]") + rb("Marge du groupe", "15,8 pb", "au S1 2026, tous clients confondus"))


top=sorted(etfj,key=lambda x:-(x['size'] or 0))[:22]
trows=[[x['name'].replace('UCITS ETF','').replace('  ',' ').strip()[:58], x['cat'].replace('  ',' · ')[:34], fr((x['size'] or 0)/1000,1), fr(x['ter']*100,0) if x['ter'] is not None else '—'] for x in top]
cats={}
for x in etfj:
    k=x['cat'].split('  ')[0] if x['cat'] else 'Autre'
    cats.setdefault(k,[0,0]); cats[k][0]+=x['size'] or 0; cats[k][1]+=(x['size'] or 0)*(x['ter'] or 0)
crow=sorted([(k,v[0]/1000,v[1]/v[0]*100 if v[0] else 0) for k,v in cats.items()],key=lambda t:-t[1])[:6]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 12, suite", "Les vingt-deux premiers ETF d'Amundi", "Un quart des encours dans dix produits, presque tous sous 20 pb.")
 + bh("Par encours", "Md€ et pb de frais courants, 20/10/2026") + table(["ETF","Catégorie justETF","Encours","Frais"], trows, cls='t small')
 + bh("Par grande catégorie", "Md€ et frais pondérés, pb") + table(["Catégorie","Encours","Frais pondérés"], [[k, fr(a,1), fr(f,1)] for k,a,f in crow])
 + '<div class="src" style="margin-top:2mm">Source : justETF, page fournisseur Amundi, relevé du 20/10/2026 (636 lignes) ; calculs de l\'auteur. Les encours sont ceux de chaque part, tels qu\'affichés ; les frais sont les frais courants (TER) affichés.</div></div>', run="Partie V · Ce qui est vendu")

# ====================================================================== 26. CH13 + CH14
txtpage("Parties V et VI", chap("Chapitres 13 et 14", "Ce que l'étude ne mesure pas, et par où arrivent les encours"), '''
<h3>13. La performance des fonds : non mesurée</h3><p>Le lien entre la performance des fonds et la collecte est réel — une sous-performance durable fait perdre des encours, donc de la marge — mais le mesurer exige les séries de performance de centaines de fonds face à leurs indices, réservées aux bases payantes (Morningstar, Lipper). L'étude ne les a pas : elle ne conclut donc rien sur la qualité de gestion d'Amundi, et le prix n'intègre aucune hypothèse à ce sujet.</p>
<h3>14. Par où arrivent les encours</h3><p>Fin 2025 (2 379,9 Md€) : particuliers 704,2 Md€ (réseaux France 146,2 ; réseaux internationaux, dont UniCredit, 161,4 ; distributeurs tiers 396,6) ; institutionnels 1 251,5 Md€ (institutionnels et souverains 572,1 ; entreprises 120,5 ; épargne salariale et retraite 103,8 ; <b>assureurs CA et SG 455,1</b>) ; coentreprises 364,4 ; distribution américaine via Victory 59,9 (supplément financier T4 2025).</p>
<h3>Captif et conquis</h3><p>À l'introduction en Bourse, 56 % des encours dépendaient des deux groupes fondateurs : 41,4 % de contrats en euros de leurs assureurs et 14,6 % de leurs réseaux (document de base). Fin 2025, ce n'est plus qu'environ 25 % <span class="calc">[calc]</span>. Mais la dépendance économique est ailleurs : les mandats d'assureurs (19 % des encours) rapportent ≈ 3,7 pb, soit ≈ 5 % des commissions, quand les particuliers (≈ 30 % des encours) en apportent ≈ 69 % à 30,7 pb <span class="calc">[calc]</span>. C'est par les réseaux de détail que passe la valeur.</p>
<h3>La valeur d'un accord de distribution que l'on ne contrôle pas</h3><p>Le contrat de 2017 imposait qu'environ les trois quarts des actifs gérés par UniCredit pour ses clients italiens soient des produits Amundi (Reuters, 14/01/2025). En janvier 2025, UniCredit propose de le prolonger dix ans si Crédit Agricole apporte ses titres Banco BPM à son offre ; Crédit Agricole monte au contraire à 19,8 %, puis 29,3 % de BPM. UniCredit développe sa gamme maison onemarkets, rachète Alkimis sgr, et retire ses encours en payant des pénalités, provisionnées pour l'essentiel de 2026 et la moitié de 2027 (A. Orcel, Reuters 09/02/2026). Aucune pénalité n'est à attendre après juillet 2027 (N. Calcoen, T2 2026).</p>
<table class="t" style="margin:2mm 0 3mm"><tr><th>Date</th><th>Encours liés à UniCredit</th><th>Collecte</th></tr><tr><td>fin 2025</td><td>86 Md€ (dont 66 en Italie)</td><td>−16 Md€ sur l'année</td></tr><tr><td>T1 2026</td><td>réseaux 75 Md€</td><td>−9 Md€</td></tr><tr><td>T2 2026</td><td>réseaux 75 Md€ ; assureur 14 Md€</td><td>réseaux −5 ; assureur −7</td></tr><tr><td>mi-2027</td><td>≈ 20 Md€ (projection presse)</td><td>—</td></tr></table>
<h3>Ce qui est en jeu</h3><p>75 Md€ × ≈ 40 pb = <b>≈ 300 M€ de revenus annuels</b>, fourchette 225-340 M€, soit 7 à 9 % des commissions de gestion ; ≈ 180 M€ après coûts variables et impôt <span class="calc">[calc]</span>. JPMorgan estimait fin 2024 que l'accord pèserait ≈ 20 % du bénéfice 2027 (Investing.com, 26/11/2024) : cela supposerait ≈ 60 pb de marge nette, au-dessus de tout ce que montrent les prospectus ; retenu en borne haute.</p>
''' + op("La sortie d'UniCredit est le prix d'un choix du groupe Crédit Agricole en Italie. Si Crédit Agricole prend tout ou partie de Banco BPM, Anima (212 Md€, ≈ 287 M€ de résultat net normalisé) et le réseau BPM (1 363 agences) deviennent la contrepartie possible. Rien de cela n'est dans le prix."), src="Sources : supplément financier T4 2025 ; document de base ; transcriptions T4 2025 et T2 2026 ; Reuters (14/01/2025, 09/02/2026, 24-25/09/2026) ; Milano Finanza (29/06/2026) ; Anima, résultats 2025 ; Zonebourse (29/09/2026) ; Investing.com.")


itf=[x for x in json.load(open('/root/amundi/it/funds.json')) if x['doc']=='fondiitalia']
mf=[1.85,1.85,2.0,2.0,2.0,1.15,0.85,1.0,1.2,1.1,1.3,0.9,0.8,1.3,1.2]
itrows=[[x['fondo'], fr(x['aum'],0), fr(m*100,0), fr(x['cc']*100,0), fr(x['distrib'],1), fr(m*(100-x['distrib']),1)] for x,m in zip(itf,mf)]
At=sum(x['aum'] for x in itf)
itrows.append(["Total, moyennes pondérées", fr(At,0), "110,8", fr(sum(x['aum']*x['cc'] for x in itf)/At*100,0), "59,4", "44,9"])
panel('bg-navy', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 14, suite", "Le dossier UniCredit, mesuré", "Quarante prospectus italiens disent ce que les comptes d'Amundi taisent.", center=True)
 + '<div class="tick" style="margin:4mm auto;color:var(--cu2)"></div>'
 + '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;border-top:1pt solid rgba(255,255,255,.6);border-bottom:1pt solid rgba(255,255,255,.6)">' + ''.join(f'<div style="text-align:center;padding:5mm 3mm;{"border-left:.25pt solid rgba(255,255,255,.4)" if i else ""}"><div style="font-family:Bod;font-size:30pt;color:{c}">{n}</div><div style="font-size:7pt;color:var(--l2);margin-top:1.5mm;line-height:1.4">{l}</div></div>' for i,(n,l,c) in enumerate([("111 pb","commission de gestion pondérée de la gamme vendue par UniCredit","#fff"),("59 %","de cette commission reversés au réseau","#fff"),("≈ 45 pb","restent à la société de gestion, avant ses coûts","var(--cu2)")])) + '</div>'
 + bh("La gamme ex-Pioneer vendue par UniCredit", "fin 2016 ; M€ et pb") + table(["Fonds","Encours","Gestion","Frais courants","Part du réseau, %","Net SGR"], itrows, cls='t small', tot=[15])
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-top:4mm;font-size:8pt;line-height:1.45;color:var(--l3)"><div><p><b>Ce que disent les gammes récentes.</b> Sistema Amundi Investi (UniCredit et CA Italia, 2025) : produits à échéance et garantis, commission de gestion de 0,45 % à 0,80 %, part du réseau de 55,6 % à 66,7 %, soit 20 à 27 pb nets. Fondi Amundi (multi-distributeurs, 2024) : jusqu\'à 82,9 % reversés aux réseaux de conseillers. Le mix se dégrade vers des produits moins chers.</p></div><div><p><b>La conclusion retenue.</b> Une marge nette de ≈ 40 pb sur les 75 Md€ de réseaux, fourchette 30-45 pb : ≈ 300 M€ de revenus annuels. Repère : avant son rachat, Pioneer faisait 875 M€ de revenus sur ≈ 222 Md€ (≈ 39 pb, 2015). Limite : les SICAV luxembourgeoises, majoritaires dans les encours UniCredit actuels, ne publient pas la part distributeur.</p></div></div>'
 + '<div class="note" style="margin-top:2mm">Sources : prospectus Sistema Amundi Fondi Italia (données au 30/12/2016), Sistema Amundi Investi (30/12/2025), Fondi Amundi (30/12/2024) ; calculs de l\'auteur. Part du réseau = « quota parte percepita in media dai collocatori », appliquée à la commission de gestion.</div></div>', run="Partie VI · Les clients", dark=True)

# ====================================================================== 27. INTERCALAIRE VII CHIFFRES
panel('inter', '''<img src="img/i6.jpg" style="object-position:50% 40%">
<div class="ttl" style="left:14mm;top:24mm;color:#fff;width:150mm"><div class="pn">Partie VII</div><h1>Les chiffres</h1>
<div class="man">Des comptes reconstitués depuis 2010, une marge qui recule de trois points de base, et un coût qui ne dérape jamais.</div>
<div class="toc"><div><span>15</span>Les comptes, exercice par exercice</div><div><span>16</span>L'économie unitaire</div><div><span>17</span>Qualité du résultat</div></div></div>
<div class="credit" style="color:#fff">Photographie : Mat, Unsplash</div>''', folio=False)

# ====================================================================== 28. CH15 COMPTES
yy = [str(y) for y in Y]
def rr(lbl, arr, d=0, f=None):
    return [lbl] + [(f(v) if f else f1(v, d)) for v in arr]
cr = [rr("Encours fin d'année, Md€", AUM), rr("Collecte nette, Md€", FLOW, 1), rr("Revenus nets IFRS", REV), rr("Commissions nettes de gestion", FEE), rr("Commissions de surperformance", PERF),
      rr("Revenus nets ajustés", REVA), rr("Charges ajustées", [(-v if v else None) for v in CHA]),
      ["Coefficient ajusté, %"] + [ (f1(-c/r*100,1) if (c and r) else '—') for c, r in zip(CHA, REVA)],
      rr("Résultat net part du groupe publié", RNPG), rr("Résultat net ajusté", RNA), rr("Capitaux propres part du groupe", CP), rr("Écarts d'acquisition", GW), rr("Dividende par action, €", DPS, 2), rr("Marge sur commissions, pb", MARG, 1), rr("Effectif fin d'année", STAFF)]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 15", "Les comptes, exercice par exercice", "M€ sauf mention. Publié et ajusté, côte à côte.")
 + bh("Exercice par exercice", "M€") + table(["Ligne"] + yy, cr, cls='t small', hl=[9])
 + '''<div class="note" style="margin-top:2mm">Ajusté = définitions d'Amundi (hors amortissement des contrats de distribution, coûts d'intégration et éléments exceptionnels ; 2025 hors plus-value Victory de 402 M€). Revenus et charges ajustés publiés depuis 2016. 2010-2011 : présentation de gestion du rapport 2011, pro forma BFT ; rupture de présentation entre 2011 et 2012. 2012 : JV comptées à 100 % dans les encours. 2017 : Pioneer consolidé au 3 juillet. 2019 : aucun dividende (recommandation BCE). Effectif : ETP ou ordre de grandeur publié. Collecte 2021-2022 corrigée (60,2 et 7,0 Md€ ; les chiffres de 65,6 et 15,0 étaient ceux du T4).</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm">''' + '<div>' + bh("Résultat net ajusté", "M€") + columns(yy, RNA, w=86, h=48, d=0, lab_every=3, hi=[15]) + '</div><div>' + bh("Coefficient d'exploitation ajusté", "%") + lines([str(y) for y in range(2016,2026)], [("", [-c/r*100 for c, r in zip(CHA[6:], REVA[6:])], NAVY)], w=86, h=48, ymin=44, ymax=58, ticks=[45,50,55], d=1, lab_every=3, legend=False) + '</div></div>'
 + '<div class="src" style="margin-top:2mm">Sources : rapport 2011 ; document de base ; URD 2015-2025 ; communiqués T4 ; classeur publié (feuilles CR_comptable, CR_ajuste, Encours_collecte, Bilan, Action).</div></div>', run="Partie VII · Les chiffres")


FPT = row('Bilan', 'Fonds propres tangibles'); TB = row('Bilan', 'Total bilan'); DIVT = row('Action','Dividende total'); PAY = row('Action','Taux de distribution')
br = [rr("Capitaux propres part du groupe", CP), rr("Écarts d'acquisition", GW), rr("Fonds propres tangibles (calcul brut)", FPT), rr("Total du bilan", TB), rr("Dividende total, M€", DIVT), ["Taux de distribution, %"]+[(f1(v*100,0) if v else ('0' if v==0 else '—')) for v in PAY]]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 15, suite", "Bilan, capital et distribution", "Un bilan fait d'écarts d'acquisition, un capital qui se distribue.")
 + bh("Postes clés du bilan et distribution", "M€ au 31/12") + table(["Ligne"]+yy, br, cls='t small')
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm">' + '<div>' + bh("Dividende par action", "€, au titre de l'exercice") + columns(yy[1:], DPS[1:], w=86, h=50, d=2, lab_every=2, hi=[14]) + '</div><div>'
 + bh("Ratio CET1", "%") + columns(["fin 2024","fin 2025","30/06/2026","exigence"],[21.8,14.3,12.4,7.75],w=86,h=50,d=1,hi=[3],hi_color="#8E9DB2") + '</div></div>'
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm;font-size:8.3pt;line-height:1.42;margin-top:3mm"><div><p>Les capitaux propres part du groupe passent de 5,2 Md€ (2010) à 12,7 Md€ (2025), dont 6,6 Md€ d\'écarts d\'acquisition. Les fonds propres tangibles bruts, qui avaient chuté à 1,9 Md€ après Pioneer (2017), sont remontés à 5,7 Md€ ; Amundi publie sa propre mesure, 4,9 Md€. Le total du bilan (38,7 Md€) est gonflé par les actifs et passifs des produits structurés et des garanties d\'Amundi Finance ; il ne mesure pas l\'activité.</p></div><div><p>Le taux de distribution n\'est jamais descendu sous 65 % depuis l\'introduction en Bourse (2019 excepté, sur recommandation de la BCE) ; il atteint 74 % au titre de 2025. Avec le rachat de 500 M€ lancé le 04/02/2026, Amundi aura rendu en 2026 ≈ 1,4 Md€ à ses actionnaires, soit ≈ 100 % de son résultat ajusté <span class="calc">[calc : 877 M€ de dividende + 500 M€ de rachat]</span>.</p></div></div>'
 + '<div class="src">Sources : URD 2015-2025 ; communiqué S1 2026 ; classeur (feuilles Bilan et Action).</div></div>', run="Partie VII · Les chiffres")

# ====================================================================== 29. CH16 ECONOMIE UNITAIRE
seg_y = ["2014","2015","2016","2017","2022","2023","2024","2025"]
railpage("Partie VII · Les chiffres", chap("Chapitre 16", "L'économie unitaire", "Où va la marge quand la taille monte, qui la capte, et ce qu'il reste à l'actionnaire.")
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm"><div>' + bh("Marge sur commissions", "pb des encours moyens") + lines([str(y) for y in [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]], [("", [19.2,18.8,19.6,18.6,16.4,16.1,16.0,19.1,18.8,18.4,17.4,17.5,17.8,17.7,17.7,16.1,15.8], NAVY)], w=64, h=44, ymin=14, ymax=21, ticks=[15,17,19,21], lab_every=4, legend=False) + '</div><div>'
 + bh("Marge par clientèle", "pb") + lines(seg_y, [("Particuliers", [51.2,49.4,49.0,46.0,36.6,35.7,34.4,30.7], NAVY), ("Institutionnels", [12.5,11.5,11.2,10.9,10.1,10.4,10.6,10.3], "#647793"), ("Assureurs", [3.8,3.6,3.5,3.4,3.6,3.7,3.7,3.7], CU)], w=64, h=44, ymin=0, ymax=56, ticks=[0,25,50], lab_every=3, legend=False) + legend([("Particuliers", NAVY), ("Institutionnels", "#647793"), ("Assureurs CA et SG", CU)]) + '</div></div>' + '''
<div class="txtb" style="margin-top:4mm;column-count:2;column-gap:6mm">
<p><b>La marge recule lentement.</b> 19,2 pb en 2010, 16,1 en 2015, remontée à 19,1 en 2017 avec les réseaux italiens de Pioneer, puis érosion jusqu'à 17,7 en 2024 et 15,9 à périmètre comparable en 2025 (15,8 au S1 2026). Trois causes : la gestion passive, le poids des institutionnels, la sortie d'Amundi US. Sur 2010-2026, la baisse moyenne est de ≈ 1,2 % par an <span class="calc">[calc]</span>.</p>
<p><b>La marge des particuliers fond.</b> 51,2 pb en 2014, 30,7 pb en 2025 : ce sont les réseaux de détail — et parmi eux UniCredit — qui portent la valeur, et c'est là que la compression est la plus forte. Les institutionnels restent à ≈ 10 pb, les mandats d'assureurs à ≈ 3,7 pb.</p>
<p><b>Le coût suit.</b> Les charges représentent ≈ 9,3 pb des encours moyens en 2025, contre 11,5 en 2010 : le coût unitaire a baissé presque aussi vite que la marge, et le coefficient d'exploitation ajusté reste entre 48 % et 53 % depuis 2016.</p>
<p><b>Ce qu'il reste à l'actionnaire.</b> Fonds propres tangibles publiés : 4,9 Md€ fin 2025 ; résultat net ajusté / fonds propres tangibles ≈ <b>28 %</b> <span class="calc">[calc]</span>, contre un coût des fonds propres de 10 %. Le capital excédentaire, lui, s'épuise : CET1 2 448 M€ et 12,4 % au 30/06/2026, actifs pondérés ≈ 19,7 Md€ ; ≈ 0,9 Md€ au-dessus de l'exigence, ≈ 0,5 Md€ au-dessus d'un coussin de gestion de 10 % <span class="calc">[calc]</span>.</p>
</div><div class="src">Sources : rapport 2011 ; document de base ; URD 2015-2025 (§ 4.3, marges par segment, lecture des graphiques) ; supplément T4 2025 ; communiqué S1 2026 ; Pilier 3.</div>''',
 rb("Rentabilité des fonds propres tangibles", "≈ 28<small>%</small>", "contre 10 % de coût des fonds propres [calc]") + rb("Particuliers", "30,7 pb", "en 2025, contre 51,2 en 2014") + rb("Capital excédentaire", "≈ 0,5 Md€", "au-dessus d'un coussin de 10 % de CET1 [calc]"))

# ====================================================================== 30. CH17 QUALITE
txtpage("Partie VII · Les chiffres", chap("Chapitre 17", "Qualité du résultat", "Ce qui se reproduira, ce qui ne se reproduira pas, et l'honnêteté de l'écart entre publié et ajusté."), '''
<h3>L'écart publié / ajusté</h3><p>Amundi publie un résultat « ajusté » qui exclut l'amortissement des contrats de distribution acquis (UniCredit, Bawag, Sabadell), les coûts d'intégration et les éléments exceptionnels. En 2025, le résultat publié (1 592 M€) dépasse l'ajusté (1 354 M€) à cause de la plus-value non monétaire de 402 M€ sur Victory, nette du coût du plan d'optimisation (88 M€). Sur 2016-2024, l'ajusté dépasse le publié de 11 à 119 M€ selon les années (le maximum en 2017, coûts d'intégration de Pioneer), sauf en 2021 où le publié est supérieur : l'écart est documenté, explicable ligne à ligne, et va dans les deux sens.</p>
<h3>La surperformance</h3><p>Les commissions de surperformance varient de 72 M€ (2011) à 427 M€ (2021) ; 173 M€ en 2025, 123 M€ au seul S1 2026 contre 57 M€ au S1 2025. Le scénario de l'étude les ramène à ≈ 150 M€ par an, ce qui retire ≈ 69 M€ après impôt au rythme du S1 2026 <span class="calc">[calc]</span>.</p>
<h3>Ce qui ne se reproduira pas</h3><p>Trois éléments du résultat 2025-2026 sont temporaires : les revenus UniCredit (≈ 180 M€ après impôt, perdus d'ici fin 2027), les pénalités payées par UniCredit (montant non publié, supposé ≈ 45 M€ après impôt, fourchette 0-90), et l'excès de surperformance. Ensemble, ≈ 18 % du résultat ajusté 2025 <span class="calc">[calc, repère maison n° 1]</span>.</p>
<h3>Ce qui vient d'ailleurs</h3><p>Les quotes-parts des coentreprises, de Victory et d'ICG atteignent 154 M€ au S1 2026 (+35 % sur un an), dont 71 M€ de coentreprises sur le semestre ; Victory 35 M€ et ICG 12 M€ au seul T2. Ce sont des bénéfices réels mais non distribués : ils ne financent ni le dividende ni le rachat.</p>
<h3>La fiscalité</h3><p>Le taux d'impôt ajusté 2025 (≈ 27 %) est gonflé par la contribution exceptionnelle française (71,8 M€). Le S1 2026 en supporte 56 M€. Le scénario de l'étude la reconduit au même niveau en 2027 ; le projet de loi de finances 2027 la réduirait d'environ un quart.</p>
<h3>Le résultat normalisé 2027</h3>
<table class="t" style="margin:1.5mm 0 3mm"><tr><th>M€</th><th>Montant</th></tr>
<tr><td>Résultat net ajusté S1 2026 × 2</td><td>1 562</td></tr><tr><td>− quotes-parts JV, Victory, ICG (valorisées à part)</td><td>−308</td></tr><tr><td>− surperformance au-dessus de la normale, après impôt</td><td>−69</td></tr><tr class="sub"><td>= cœur 2026 au rythme courant</td><td>1 185</td></tr><tr><td>+ effet d'entrée des marchés (S2 2026)</td><td>+47</td></tr><tr><td>+ croissance nette 2027 (organique 3,5 % − compression 1 %)</td><td>+30</td></tr><tr><td>− perte UniCredit en année pleine (300 M€ × 80 % × 75 %)</td><td>−180</td></tr><tr><td>− fin des pénalités UniCredit (hypothèse)</td><td>−45</td></tr><tr class="tot"><td>= cœur normalisé 2027</td><td>1 037</td></tr><tr><td>+ SBI, Victory, ICG, autres JV</td><td>+327</td></tr><tr class="tot"><td>= résultat net ajusté 2027e ; BPA 6,82 € sur 200 M d'actions</td><td>1 364</td></tr></table>
''' + op("Le résultat d'Amundi est de bonne qualité : récurrent, peu dépendant de la surperformance, avec un ajustement honnête. Mais 2027 sera son point bas, et c'est ce point bas qu'il faut valoriser."), src="Sources : URD 2016-2025 ; communiqués S1 2025 et S1 2026 ; calculs de l'auteur (classeur). 200 M d'actions = 206,4 M émises moins ≈ 6,5 M rachetées pour annulation.")

# ====================================================================== 31. INTERCALAIRE VIII
panel('half', '''<div class="ph"><img src="img/i4.jpg"></div>
<div class="right" style="color:var(--navy)"><div class="kicker" style="color:var(--cu)">Partie VIII</div>
<div style="font-family:Bod;font-style:italic;font-size:40pt;line-height:1.05;margin-top:3mm">Autour</div>
<div class="tick" style="margin:6mm 0 6mm;color:var(--navy)"></div>
<div style="font-size:8pt;line-height:2">''' + ''.join(f'<div style="display:flex;gap:4mm;border-bottom:.25pt solid rgba(19,42,71,.2)"><span style="font-family:Bod;width:7mm">{n}</span>{t}</div>' for n,t in [("18","Les concurrents, sur les mêmes lignes"),("19","Ce que la presse et les analystes ont dit"),("20","Ce qui peut casser la thèse")]) + '''</div>
<div style="font-family:Bod;font-style:italic;font-size:17pt;line-height:1.3;position:absolute;bottom:0">Le meilleur élève du secteur, dans une industrie qui se concentre partout, sauf là où Amundi est la plus exposée.</div></div>
<div class="credit" style="left:95mm;color:#fff">Photographie : Hans Reniers, Unsplash</div>''', folio=False)

# ====================================================================== 32. CH18 CONCURRENTS
peers = [["<b>Amundi</b>","2 581 Md€ (06/2026)","1 354 M€ ajusté","≈ 49,6 %","12,1 / 11,3","4,85 %"],["DWS","1 085 Md€","927 M€","58 %","12,9 / 12,0","4,6 %"],["Schroders","≈ 825 Md£","RO aj. ≥ 745 M£","≈ 71 %","13,5 / 14,7","3,8 %"],["Aberdeen","556 Md£","RO aj. 264 M£","≈ 79 % [calc]","11,9 / 15,8","6,0 %"],["Azimut","≈ 141 Md€","> 515 M€","n.d.","10,2 / 9,8","5,3 %"],["T. Rowe Price","—","—","—","10,1 / 9,9","5,2 %"],["BlackRock","> 13 tn$","—","—","25,6 / 18,0","2,0 %"],["Anima (non cotée)","212 Md€","287 M€ normalisé","—","OPA ≈ 8x","—"],["Eurizon (non cotée)","395 Md€ (2024)","573 M€ (2024)","—","—","—"]]
cir = [("Amundi",49.6),("DWS",58.0),("Schroders",71.0),("Aberdeen",79.3)]
railpage("Partie VIII · Autour", chap("Chapitre 18", "Les concurrents, sur les mêmes lignes", "Le meilleur coefficient du panel, au même multiple que les autres.")
 + bh("Le panel", "cours de septembre-octobre 2026") + table(["","Encours","Résultat 2025","Coefficient","PER passé / prévisionnel","Rendement"], peers, cls='t small', hl=[0])
 + bh("Coefficient d'exploitation", "%, dernier exercice ou semestre") + hbars(cir, w=100, labw=24, d=1, unit=" %", hi=[0], hi_color=CU) + '''
<div class="txtb" style="margin-top:3mm;column-count:2;column-gap:6mm">
<p><b>Leurs projets.</b> BlackRock vise en 2030 plus de 35 Md$ de revenus et 400 Md$ de levées en actifs privés, après GIP, HPS (12 Md$) et Preqin. BNP Paribas AM, fusionné avec AXA IM (> 1,6 tn€), veut doubler son résultat avant impôt de 820 M€ d'ici 2030, avec 400 M€ de synergies de coûts. DWS promet +10 à 15 % de BPA par an jusqu'en 2028, un coefficient sous 55 % en 2027 et un dividende exceptionnel d'≈ 1 Md€. Schroders coupe 150 M£ de coûts ; Eurizon lance ses ETF italiens avec BlackRock ; Vanguard baisse encore ses frais (ex. 0,07 → 0,05 %).</p>
<p><b>Ce que l'Italie a appris.</b> Le projet de coentreprise Natixis IM–Generali (≈ 1,9 tn€) a été abandonné le 11/12/2025 face aux pouvoirs spéciaux italiens et à l'opposition de Delfin et Caltagirone. La concentration a lieu en Europe, mais pas en Italie.</p>
</div><div class="src">Sources : StockAnalysis, ABC Bourse (cours et PER) ; DWS FY 2025 ; Schroders (AJ Bell, 15/01/2026) ; Aberdeen (03/03/2026) ; Azimut (FinanzaOnline, 12/01/2026) ; Anima FY 2025 ; Intesa 2024 ; BNP Paribas (17/03/2026) ; BlackRock ; communiqués BPCE-Generali.</div>''',
 rb("Écart de coefficient", "−8 à −30", "points d'Amundi sur DWS, Schroders et Aberdeen") + rb("Même PER que DWS", "≈ 12x", "le marché paie la croissance promise, pas l'efficacité") + op("La décote d'Amundi ne vient pas de sa qualité mais de son absence de promesse : son objectif 2028 est déjà atteint et le marché attend le suivant."))


plans=[["BlackRock","> 13 tn$","Plan 2030 : revenus > 35 Md$, résultat opérationnel 15 Md$, croissance organique des commissions > 5 %/an, 400 Md$ de levées privées","Le n° 1 mondial va vers le privé et les données ; il domine les ETF européens (40,8 %)"],["BNP Paribas AM + AXA IM","> 1,6 tn€","Résultat avant impôt de 820 M€ à doubler d'ici 2030 ; coefficient < 60 % ; 400 M€ de synergies de coûts, 150 M€ de revenus ; 350 Md€ de collecte","Un second champion français, même modèle de bancassurance"],["DWS","1 085 Md€","BPA +10-15 %/an jusqu'en 2028 ; coefficient < 55 % en 2027 ; > 160 Md€ de collecte longue ; dividende exceptionnel ≈ 1 Md€","Concurrent direct sur les ETF (Xtrackers) et le numérique"],["Natixis IM / Generali","≈ 1,9 tn€","Coentreprise abandonnée le 11/12/2025","Un rapprochement transfrontalier en Italie est politiquement bloqué"],["Eurizon (Intesa)","395 Md€","ETF italiens ; partenariat avec BlackRock","Premier gérant italien, capte ce qu'UniCredit laisse"],["Anima (Banco BPM)","212 Md€","Filiale de BPM (≈ 90 %) depuis 2025","Cible possible si Crédit Agricole prend BPM"],["onemarkets (UniCredit)","en montée","Gamme maison d'UniCredit avec des gérants tiers","Le remplaçant d'Amundi chez UniCredit"],["Schroders","≈ 825 Md£","150 M£ d'économies ; 20 Md£ visés pour Schroders Capital","Les gérants actifs coupent leurs coûts"],["Vanguard","> 10 tn$","Baisse continue des frais en Europe (01/07/2025)","Pression sur le cœur ETF"]]
panel('bg-stone', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 18, suite", "Ce que préparent les concurrents", "Tout le monde se concentre, sauf en Italie.")
 + bh("Les projets déclarés", "faits sourcés ; colonne de droite : lecture de l'auteur") + table(["Acteur","Taille","Projet déclaré","Ce que cela change pour Amundi"], plans, cls='t small')
 + op("En 2026, la consolidation a lieu (BNP Paribas–AXA IM, BlackRock–GIP–HPS) mais pas en Italie, où l'État la bloque. Amundi n'a plus besoin d'acheter de la taille ; ses rachats récents visent les actifs privés, les États-Unis et la technologie, exactement comme BlackRock.")
 + '<div class="src">Sources : BlackRock ; BNP Paribas (17/03/2026) ; DWS FY 2025 ; BPCE et Generali (19/09/2025, 11/12/2025) ; Intesa Sanpaolo ; Anima FY 2025 ; Reuters (09/02/2026) ; Schroders ; Vanguard.</div></div>', run="Partie VIII · Autour")

# ====================================================================== 33. CH19 PRESSE
press = [("14/01/2025","Reuters","UniCredit propose de prolonger de dix ans le contrat Amundi si CA apporte ses titres BPM."),("25/02/2025","Der Spiegel","V. Baudson plaide pour la souveraineté financière européenne et un label européen de fonds."),("02/04/2025","MarketScreener","L'action perd plus de 4 % sur des rumeurs de remise en cause du contrat UniCredit."),("30/04/2025","Reuters","V. Baudson : UniCredit représente « environ 100 milliards d'euros » d'encours."),("06/11/2025","MarketScreener","RBC dégrade la valeur à « performance de secteur », objectif 66 €."),("11/12/2025","Bloomberg","Fin du projet Natixis IM–Generali."),("09/02/2026","Reuters","UniCredit sort d'Amundi au profit d'onemarkets, avec pénalités."),("17/03/2026","BNP Paribas","Plan BNP Paribas AM 2030."),("18/05/2026","Amundi","Nouvelle organisation : trois directeurs généraux délégués."),("08/09/2026","RBC ; cours","Objectif RBC 85 € ; action à 95,80 € (+35,6 % depuis janvier)."),("24-25/09/2026","Reuters","CA et UniCredit évoquent un partage de Banco BPM ; offre de MPS. C. L'Angevin : « rien ne peut se faire sans nous, rien ne peut se faire contre nous »."),("29/09/2026","Bloomberg","CA étudierait un rachat de Banco BPM."),("19/10/2026","Clôture","87,65 €, −8,5 % depuis le 08/09 [calc].")]
prow = ''.join(f'<tr><td style="white-space:nowrap">{d}</td><td class="l" style="white-space:nowrap">{s}</td><td class="l">{t}</td></tr>' for d, s, t in press)
txtpage("Partie VIII · Autour", chap("Chapitre 19", "Ce que la presse et les analystes ont dit"), f'''<table class="t" style="column-span:all;margin-bottom:4mm"><tr><th>Date</th><th class="l">Source</th><th class="l">Ce qui a été dit ou fait</th></tr>{prow}</table>
<h3>Le consensus</h3><p>Les notes d'analystes lues dans la presse convergent : une machine régulière à rendement élevé, mais une décote de « filiale contrôlée » et l'incertitude UniCredit de 2027. JPMorgan (novembre 2024) : objectif 70 €, accord UniCredit ≈ 20 % du bénéfice 2027 ; RBC : 66 € (novembre 2025), puis 85 € (septembre 2026) ; BofA relève son objectif après le S1 2026 ; CIC passe à « neutre » ; AlphaValue à « accumuler ». Le PER prévisionnel affiché (12,2 au cours de 94,60 €) implique un BPA 2026 d'environ 7,75 €.</p>
<h3>Ce que peu de notes chiffrent</h3><p>La valeur des participations cotées (SBI, Victory, ICG ≈ 5,6 Md€ au marché, ≈ 30 % de la capitalisation) et la marge réelle des réseaux UniCredit, que cette étude mesure dans les prospectus italiens.</p>
<h3>La voix de la direction</h3><p>Amundi affirme que ses objectifs 2028 seront tenus « quoi qu'il arrive avec UniCredit » et que le plafond de coefficient de 56 % vaut « quel que soit le scénario UniCredit » (conférences T4 2025 et T1 2026). Hors pénalités et revenus du contrat, la croissance des commissions du T2 2026 aurait été « très similaire » (N. Calcoen).</p>''', src="Sources citées dans le tableau ; Investing.com (26/11/2024) ; StockAnalysis (10/09/2026) ; transcriptions des conférences T4 2025, T1 et T2 2026.")

# ====================================================================== 34. CH20 RISQUES
risks = [["Perte UniCredit plus forte (450 M€ de revenus au lieu de 300)","borne JPMorgan","−5,4"],["Pénalités UniCredit plus élevées (120 M€ au lieu de 60)","non publié","−2,7"],["Coût des fonds propres +0,5 point","bêta, taux","−3,9"],["Compression de marge 2 %/an au lieu de 1 %","RIS, passif","−0,7"],["Décote des participations 20 % au lieu de 10 %","fiscalité, liquidité","−2,8"],["Actions −10 % durablement","marchés","≈ −4 à −6 [calc]"],["SBI FM sous 400 ₹ ou Victory sous 80 $","cours","−2 à −3 chacun"],["CET1 sous 11 % ou acquisition en actions","capital","non chiffré"],["Influence de l'actionnaire majoritaire (Italie)","gouvernance","non chiffré"],["À la hausse : option Anima / Banco BPM avec synergies","Italie","+3,6"],["À la hausse : surtaxe 2027 réduite (PLF 2027)","fiscalité","+1,7"]]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 20", "Ce qui peut casser la thèse", "Chaque risque chiffré en euros par action, à partir de la valeur centrale de 89,2 €.")
 + bh("Les risques, en euros par action", "écart à la valeur intrinsèque, € ; calculs de l'auteur") + table(["Risque","Nature","€ par action"], risks, hl=[9,10])
 + '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-top:4mm;font-size:8.4pt;line-height:1.42"><div>
<h3>Le risque principal n'est pas UniCredit</h3><p>Le coût des fonds propres pèse quatre fois plus que UniCredit dans la valeur : un demi-point de plus retire ≈ 3,9 €, quand 40 M€ de revenus UniCredit supplémentaires perdus en retirent ≈ 1,5 € <span class="calc">[calc]</span>. La valeur d'Amundi est d'abord une valeur de rendement, sensible aux taux longs français.</p></div><div>
<h3>Le risque de gouvernance</h3><p>Il ne se chiffre pas. Le dossier UniCredit montre qu'un arbitrage du groupe Crédit Agricole en Italie peut coûter aux minoritaires d'Amundi ; il peut aussi leur rapporter (Banco BPM, Anima). L'étude le traite comme une asymétrie à surveiller, pas comme une décote.</p></div></div>'''
 + op("Aucun risque isolé ne fait passer la valeur sous 83 €. Leur cumul défavorable (UniCredit à 450 M€, pénalités hautes, coût des fonds propres +0,5 point) la ramènerait vers 77 €, soit ≈ −12 % sous le cours [calc].")
 + '<div class="src">Sources : grille de sensibilité de l\'auteur (classeur) ; BASE de l\'étude, chapitres 14, 16, 17 et 24.</div></div>', run="Partie VIII · Autour")

# ====================================================================== 35. INTERCALAIRE IX
panel('inter', '''<img src="img/i7.jpg" style="object-position:50% 70%">
<div class="ttl" style="left:14mm;top:24mm;color:#fff;width:150mm"><div class="pn">Partie IX</div><h1>Le prix</h1>
<div class="man">Ce que la Bourse a payé, ce que le cours suppose, et ce que je crois que la société vaut.</div>
<div class="toc"><div><span>21</span>Le titre en Bourse depuis 2015</div><div><span>22</span>Ce que le cours actuel suppose</div><div><span>23</span>Trois chemins vers la valeur</div><div><span>24</span>Le prix, et ce qui me donnerait tort</div><div><span>25</span>Les quatre repères maison</div></div></div>
<div class="credit" style="color:#fff">Photographie : Arlind Photography, Unsplash</div>''', folio=False)

# ====================================================================== 36. CH21 BOURSE
px = [43.18,49.73,70.65,46.16,69.90,66.80,72.55,53.00,61.60,64.20,70.60,87.65]
per = [13.7,14.4,17.0,9.8,14.0,14.0,11.2,9.2,10.3,9.5,10.7,12.1]
yld = [4.7,4.4,3.5,6.3,None,4.3,5.7,7.7,6.7,6.6,6.0,4.85]
pcats = [str(y) for y in range(2015,2026)] + ["10/26"]
railpage("Partie IX · Le prix", chap("Chapitre 21", "Le titre en Bourse depuis 2015", "La Bourse n'a jamais payé la régularité plus de dix-sept fois.")
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm"><div>' + bh("Cours de fin d'année", "€") + columns(pcats, px, w=64, h=46, d=2, lab_every=2, hi=[11], fmt=lambda v: fr(v,0)) + '</div><div>' + bh("PER sur BPA ajusté", "fois") + lines(pcats, [("", per, NAVY)], w=64, h=46, ymin=6, ymax=19, ticks=[8,12,16], lab_every=3, legend=False) + '</div></div>'
 + table(["", *pcats], [["Cours, €", *[fr(v,2) for v in px]], ["PER ajusté", *[f1(v) for v in per]], ["Rendement, %", *[f1(v) for v in yld]]], cls='t small') + '''
<div class="txtb" style="margin-top:3mm;column-count:2;column-gap:6mm">
<p>De 45 € à l'introduction (11/11/2015) à 87,65 € le 19/10/2026 : +95 % de cours, et ≈ 33,8 € de dividendes cumulés, soit un rendement total simple d'environ +170 %, ≈ 9,5 % par an <span class="calc">[calc]</span>.</p>
<p>Le PER de fin d'année a oscillé entre 9,2 (2022) et 17,0 (2017, euphorie Pioneer) ; il est autour de 10 depuis 2022 et à 12,1 aujourd'hui sur le BPA ajusté glissant de ≈ 7,25 € (S2 2025 ≈ 3,47 € + S1 2026 3,78 €). Le rendement a culminé à 7,7 % fin 2022. Le marché a successivement payé Amundi comme une croissance (2017), comme une obligation (2022-2024), puis à nouveau comme une valeur européenne de qualité (2025-2026).</p>
<p>Capitalisation au 19/10/2026 : 17,6 Md€ ; plus haut sur un an 97,70 €, plus bas 60,90 € (ABC Bourse).</p>
</div><div class="src">Sources : URD de chaque exercice (« Amundi on the stock markets ») ; ABC Bourse (19/10/2026) ; PER et rendement calculés par l'auteur sur BPA ajusté et dividende de l'exercice.</div>''',
 rb("Depuis l'IPO", "+170<small>%</small>", "de rendement total simple, ≈ 9,5 % par an [calc]") + rb("PER aujourd'hui", "12,1", "contre 9-17 sur la période, ≈ 10 depuis 2022") + rb("Rendement", "4,85<small>%</small>", "4,25 € de dividende au titre de 2025"))

# ====================================================================== 37. CH22 DCF INVERSE
railpage("Partie IX · Le prix", chap("Chapitre 22", "Ce que le cours actuel suppose", "Avant de dire ce que vaut Amundi, lire ce que le marché croit déjà.") + '''
<div class="txtb" style="margin-top:5mm">
<h3>La méthode</h3><p>On part de la capitalisation, on retire ce qui se valorise à part au prix de marché — les participations cotées, les autres coentreprises, le capital excédentaire — et on lit le bénéfice que le reste, le cœur de gestion et de technologie, doit produire pour justifier le cours au multiple que justifie la théorie.</p>
<h3>Le multiple justifié</h3><p>Pour une société qui distribue durablement 90 % de son résultat, avec un coût des fonds propres de 10 % et une croissance perpétuelle de 2,5 % : PER = 0,90 / (0,10 − 0,025) = <b>12,0</b>. Le coût des fonds propres combine l'OAT à 10 ans (4,43 %, 10/09/2026), un bêta de 1,1 (bêtas publiés 1,09 et 1,11) et la prime de risque France de Damodaran (5,01 %, 05/01/2026) : 9,94 %, arrondi à 10 %.</p>
<h3>Le calcul</h3>''' + table(["M€",""], [["Capitalisation (87,65 € × 200 M d'actions)","17 530"],["− SBI FM, au cours, −10 %","−2 763"],["− Victory Capital, au cours, −10 %","−1 980"],["− ICG au coût, −10 %","−286"],["− autres coentreprises (22 M€ × 12)","−264"],["− capital excédentaire","−500"],["= valeur implicite du cœur","11 737"],["÷ 12,0 = bénéfice de base implicite","≈ 978"],["Mon scénario 2027 (ch. 17)","1 037"]], tot=[6,7]) + '''
<h3 style="margin-top:4mm">Ce qu'il faut en retenir</h3><p>Le marché valorise le cœur d'Amundi sur un bénéfice d'environ 978 M€, ≈ 5,5 % sous mon scénario qui intègre pourtant la perte d'UniCredit en année pleine et la fin des pénalités (≈ 1 % en dessous sans l'effet d'entrée des marchés du second semestre 2026) <span class="calc">[calc]</span>.</p></div>'''
 + op("Le cours a déjà fait le travail d'intégrer UniCredit. Il ne suppose ni catastrophe, ni rebond : il paie un Amundi amputé de l'Italie, sans option sur la suite."),
 rb("Cœur implicite", "≈ 978 M€", "de bénéfice de base au multiple de 12 [calc]") + rb("Mon scénario 2027", "1 037 M€", "avec UniCredit perdu en année pleine") + rb("Multiple justifié", "12,0", "90 % / (10 % − 2,5 %)"))

# ====================================================================== 38. CH23 TROIS CHEMINS
sotp = [["Cœur (gestion et technologie)","bénéfice normalisé 2027 de 1 037 × 12,0","12 444","62,2"],["SBI FM (660,7 M d'actions)","496,35 ₹ / 106,74 ₹ par €, −10 %","2 763","13,8"],["Victory Capital (22,99 M d'actions)","107,71 $ / 1,1227 $ par €, −10 %","1 980","9,9"],["ICG (4,6 %)","coût, −10 %","286","1,4"],["Autres coentreprises","22 M€ × 12","264","1,3"],["Capital excédentaire","au-dessus d'un CET1 de 10 %","500","2,5"],["Somme des parties","","18 237","91,2"]]
panel('bg-pale', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 23", "Trois chemins vers la valeur", "Somme des parties, multiples de pairs, dividendes : là où ils convergent, et pourquoi ils divergent.")
 + bh("Chemin 1 — la somme des parties", "méthode principale ; M€ et € par action, 200 M d'actions") + table(["Composante","Méthode","M€","€ / action"], sotp, tot=[6])
 + '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-top:3mm;font-size:8.3pt;line-height:1.42"><div>
<h3>Chemin 2 — les multiples de pairs</h3><p>BPA ajusté 2027e de 6,82 € × 12,5 fois = <b>85,2 €</b>. Le multiple retenu se situe entre DWS (12,0 prévisionnel) et Schroders (14,7), au-dessus d'Aberdeen et d'Azimut (9,8) ; il intègre une prime pour le coefficient d'exploitation et la rentabilité des fonds propres tangibles, et une décote pour la croissance promise plus faible.</p>
<h3>Chemin 3 — les dividendes</h3><p>Dividende 2026e ≈ 4,40 € ; croissance 2,5 % ; coût des fonds propres 10 % : 4,40 × 1,025 / 0,075 ≈ <b>60 €</b> pour le seul dividende ordinaire. Le chemin n'est pas retenu dans la moyenne, car Amundi distribue moins que son résultat économique (participations non distribuées, rachats) ; il confirme que le rendement de 4,85 % rémunère à lui seul la moitié du coût des fonds propres.</p></div><div>
<h3>Pourquoi ils divergent</h3><p>Les multiples appliquent ≈ 12 fois à des participations que le marché valorise bien plus cher : SBI FM se paie ≈ 34 fois en Inde, pour un résultat de 30 674 M₹ (+21 %) et une rentabilité des fonds propres de 43 % (exercice clos le 31/03/2026). La somme des parties capte cette valeur ; elle est donc privilégiée, mais tempérée, parce que cette valeur n'est pas distribuée.</p>
<h3>La convergence</h3>''' + table(["Chemin","Valeur","Poids"], [["Somme des parties","91,2 €","2/3"],["Multiples de pairs","85,2 €","1/3"],["Valeur intrinsèque","89,2 €",""]], tot=[2]) + '</div></div>'
 + '<div class="src" style="margin-top:3mm">Sources : prospectus SBI FM (736,08 M d\'actions détenues avant l\'IPO, 75,37 M cédées) ; Victory Capital, 10-Q T1 2026 ; ValutaFX (₹, 16/10/2026) ; Pound Sterling Live ($, 19/10/2026) ; Business Today et StockAnalysis (cours du 19/10/2026) ; URD 2025 (coentreprises) ; communiqué S1 2026 (CET1).</div></div>', run="Partie IX · Le prix")

# ====================================================================== 39. CH24 LE PRIX (pilier navy)
grid = [["9,0 %","94,3","97,9","102,2"],["9,5 %","89,8","92,8","96,3"],["<b>10,0 %</b>","85,8","<b>88,4</b>","91,3"],["10,5 %","82,3","84,5","87,0"],["11,0 %","79,2","81,1","83,2"]]
hyp = [["Bénéfice de base 2026 au rythme du S1","1 185 M€","S1 2026 × 2, hors quotes-parts et surperformance excédentaire"],["Croissance organique 2027","3,5 %","moyenne 2015-2025 : 4,3 %"],["Compression de marge","−1 %/an","historique 2010-2026 : ≈ −1,2 %/an"],["Revenus UniCredit perdus","300 M€","40 pb × 75 Md€ ; fourchette 225-340"],["Pénalités UniCredit","60 M€/an","non publiées ; fourchette 0-120"],["Coût des fonds propres","10,0 %","OAT 4,43 % + 1,1 × 5,01 %"],["Croissance perpétuelle","2,5 %",""],["Distribution soutenable","90 %",""],["Décote des participations","10 %","fiscalité, non-distribution, absence de contrôle"],["Nombre d'actions","200 M","après annulation du rachat"]]
panel('bg-navy', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 24", "Le prix, et ce qui me donnerait tort", "Un chiffre, une date, un horizon, et les faits qui l'invalideraient.", center=True)
 + '<div class="tick" style="margin:4mm auto;color:var(--cu2)"></div>'
 + '<div style="display:grid;grid-template-columns:70mm 1fr;gap:8mm;align-items:center;border-top:1pt solid rgba(255,255,255,.6);border-bottom:1pt solid rgba(255,255,255,.6);padding:4mm 0">'
 + '<div style="text-align:center"><div class="kicker" style="color:var(--l1)">Objectif à douze mois</div><div style="font-family:Bod;font-size:66pt;line-height:1.05">94 €</div><div style="font-family:Bod;font-style:italic;color:var(--l1)">au 20/10/2027 · cours de référence 87,65 €</div></div>'
 + '<div style="font-size:8pt;line-height:1.45;color:var(--l3)"><p>Valeur intrinsèque aujourd\'hui : <b>89,2 €</b> (somme des parties 91,2 € aux deux tiers, multiples 85,2 € au tiers). Portée à douze mois au coût des fonds propres (× 1,10) et diminuée du dividende attendu (≈ 4,40 €) : 93,7 €, arrondi à <b>94 €</b>. Fourchette de valeur : 85-94 €.</p><p>Potentiel de cours : +7 % ; rendement attendu dividende compris : +12 %. Révisé le 20/10/2026 de 95 € à 94 € après la mesure de la marge UniCredit dans les prospectus italiens.</p></div></div>'
 + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm">'
 + '<div>' + bh("Les hypothèses, ligne à ligne") + table(["","Retenu","Repère"], hyp, cls='t small') + '</div>'
 + '<div>' + bh("Grille de sensibilité", "valeur, € par action ; somme des parties") + table(["Coût des fonds propres","g 2,0 %","2,5 %","3,0 %"], grid) + '<div class="note" style="margin-top:1.5mm">Grille calculée sans l\'effet d\'entrée des marchés du S2 2026, qui relève chaque case d\'environ +2,8 €. Revenus UniCredit perdus 260 / 300 / 340 / 450 M€ → 90,6 / 89,2 / 87,7 / 83,8 €.</div></div></div>'
 + bh("Ce qui me donnerait tort — faits observables et datés") + '''<div style="column-count:2;column-gap:8mm;font-size:7.6pt;line-height:1.45;color:var(--l3)">
<p><b>29/10/2026 et février 2027</b> : sorties UniCredit supérieures à ≈ 10 Md€ par trimestre et marge des particuliers sous 28,5 pb → perte plus forte que prévu, valeur sous 85 €.</p>
<p><b>S1 2027</b> : marge totale sous 15,0 pb → compression plus rapide que 1 % par an.</p>
<p><b>2027</b> : coefficient d'exploitation ajusté au-dessus de 54 % → le levier joue contre.</p>
<p><b>À tout moment</b> : CET1 sous 11 %, ou acquisition payée en actions diluant Crédit Agricole sous les deux tiers → changement de politique de capital.</p>
<p><b>Cours</b> : SBI FM durablement sous ≈ 400 ₹ ou Victory sous ≈ 80 $ → −2 à −3 € par action chacun.</p>
<p><b>À la hausse</b> : débouché italien (Banco BPM, Anima) ou BPA 2027 publié au-dessus de 7,3 €.</p></div>'''
 + '<div class="note" style="margin-top:3mm">Opinion de l\'auteur. Recommandation au sens du règlement (UE) 596/2014 ; l\'auteur ne détient pas de titres Amundi. Historique des objectifs : chapitre 26.</div></div>', run="Partie IX · Le prix", dark=True)

# ====================================================================== 40. CH25 REPERES
panel('bg-stone', '<div style="position:absolute;left:10mm;right:10mm;top:16mm">' + chap("Chapitre 25", "Les quatre repères maison", "Les mêmes quatre mesures, au même endroit, dans chaque étude Sous jacent.", center=True)
 + '<div class="tick" style="margin:4mm auto;color:var(--navy)"></div><div class="thick"></div>'
 + '<div class="kgrid" style="margin:0">' + ''.join(f'<div class="cell{" last" if i>=2 else ""}" style="padding:8mm 6mm"><div class="kicker" style="color:var(--cu)">Repère n° {i+1}</div><div style="font-family:Bod;font-size:13pt;color:var(--navy);margin:2mm 0 3mm">{t}</div><div class="n">{n}</div><div class="l">{l}</div><div class="s">{s}</div></div>' for i,(t,n,l,s) in enumerate([
  ("Part non reproductible du résultat","18<small>%</small>","du résultat net ajusté 2025 : revenus UniCredit (≈ 180 M€), pénalités supposées (≈ 45 M€) et surperformance excédentaire (≈ 17 M€) [calc]","Vicor : 55 %"),
  ("Rentabilité des fonds propres tangibles − coût des fonds propres","+18 pts","≈ 28 % contre 10 % : variante « sociétés financières » du repère, le ROIC n'ayant pas de sens pour un gestionnaire d'actifs","Vicor : −5,4 points (ROIC)"),
  ("Amplitude de la fourchette","±5<small>%</small>","85-94 € autour de 89,2 €, causée d'abord par le coût des fonds propres (±0,5 point), puis par la marge UniCredit","Vicor : ±13 %"),
  ("Écart hypothèses / histoire","×0,8","croissance organique 3,5 % contre 4,3 % ; compression 1 %/an contre 1,2 % ; coefficient ≈ 50 % contre 48-53 % : hypothèses plus prudentes que l'histoire","Vicor : marge ×9,4")])) + '</div>'
 + op("Amundi est l'inverse de Vicor : un résultat très reproductible, un capital qui rapporte presque trois fois son coût, une fourchette étroite, des hypothèses en dessous de l'histoire. Ce qui manque à la valeur n'est pas la qualité ; c'est la croissance.")
 + '<div class="src">Méthode d\'analyse Sous jacent, version 1.0 ; calculs de l\'auteur (classeur).</div></div>', run="Partie IX · Le prix")

# ====================================================================== 41. CH26 SUIVI
onepage("Partie X · Après", chap("Chapitre 26", "Engagement de suivi", "Rien ne sera corrigé en silence."), '''
<h3>Calendrier des revues</h3>''' + table(["Date","Publication","Ce qui sera testé"], [["29/10/2026","Résultats du T3 2026","plus-value SBI (≈ 300 M€), sorties UniCredit, avancement et annulation du rachat"],["début février 2027","Résultats annuels 2026","marge des particuliers, dividende 2026, BPA réel contre ≈ 7,75 € de consensus"],["fin avril 2027","T1 2027","rythme des sorties UniCredit, CET1"],["juillet 2027","Fin du contrat UniCredit ; S1 2027","encours résiduels, fin des pénalités, marge totale contre 15,0 pb"],["17/11/2026","Vote First Eagle chez Victory","dilution de la participation à ≈ 23 %, endettement de Victory"]]) + '''
<h3>Historique des objectifs de cours (douze derniers mois)</h3>''' + table(["Date de diffusion","Auteur","Objectif","Cours à la diffusion","Sens","Validité"], [["20/10/2026","Guillaume Le Merour","94 €","87,65 € (19/10/2026)","au-dessus du cours (+7 %)","12 mois, jusqu'au 20/10/2027"]]) + '''
<p style="margin-top:2mm">Une version de travail avait retenu 95 € le même jour ; elle a été révisée avant diffusion après la mesure de la marge UniCredit. Toute révision ultérieure sera datée, motivée et ajoutée sous cette ligne, sans retrait.</p>
<h3>Déclaration de positions et de conflits d'intérêts</h3><p>L'auteur ne détient aucune action Amundi ni aucun instrument financier lié, directement ou indirectement, à la date de diffusion. Il n'a aucun lien d'emploi, de conseil ou de rémunération avec Amundi, le groupe Crédit Agricole, UniCredit ou leurs concurrents. L'étude n'a été ni commandée ni rémunérée. Ce document n'est pas un conseil en investissement personnalisé ; il ne tient compte d'aucune situation individuelle.</p>
<h3>Conservation</h3><p>Le classeur de calcul, les documents sources et les versions successives de l'étude sont conservés pour pouvoir motiver la recommandation auprès de l'autorité compétente sur demande.</p>
''')

# ====================================================================== 42-43. ANNEXES
srcs = '''<h3>Documents d'Amundi</h3><p>Rapport d'activité 2011 (« 2011 Business Report ») ; document de base de l'introduction en Bourse (AMF I.15-073, 06/10/2015) ; note d'opération (visa n° 15-552, 30/10/2015) ; documents de référence 2015-2018 ; documents d'enregistrement universel 2019-2025 ; communiqués de résultats annuels T4 2015 à T4 2025 ; communiqués T1 et T2 2026 et rapport semestriel 2026 ; suppléments financiers (xls) T4 2025 et T2 2026 ; transcriptions des conférences T4 2025, T1 2026, T2 2026 ; rapports Pilier 3 (2023-2026) ; communiqués d'opérations : Pioneer (12/12/2016), Sabadell (21/01/2020), Lyxor (31/12/2021), Victory (09/07/2024, 01/04/2025), ICG (18/11/2025), SBI FM (06/11/2025, 08/07/2026, 17/07/2026, 21/07/2026), plan « Invest for the future » (18/11/2025), nominations (18/05/2026). Archive OPENDATA de l'AMF (echanges.dila.gouv.fr).</p>
<h3>Prospectus et rapports de fonds</h3><p>Amundi SGR : Sistema Amundi Fondi Italia (30/12/2016), Sistema Amundi Investi (30/12/2025), Fondi Amundi (30/12/2024), Fondi Amundi Selezione (30/12/2025), Amundi PIR — amundi.it, fundstore.it, finecobank.com. Amundi Fund Solutions, rapport annuel audité au 31/12/2025 (amundi.lu). justETF, page fournisseur Amundi (636 ETF, 20/10/2026). PEA.fr, ABC Bourse, Mémo CA (fiches de fonds).</p>
<h3>Tiers et participations</h3><p>SBI Funds Management, prospectus définitif (16/07/2026) ; Victory Capital : 10-Q T1 2026, DEFM14A, DEFA14A, communiqué sur le conseil (2026) ; ICG ; Anima, résultats 2025 ; Banco BPM.</p>
<h3>Macroéconomie et industrie</h3><p>BCE, Statistical Data Warehouse (taux de dépôt, IPCH, PIB réel zone euro, taux à 10 ans FR/DE/IT, EUR/USD, Euro Stoxx 50, Euro Stoxx) ; Federal Reserve Bank of St. Louis, FRED (Nasdaq Composite, S&P 500, DJIA) ; EFAMA, rapport du 15/06/2026 ; ETFGI (septembre 2025) ; Damodaran, primes de risque par pays (05/01/2026) ; AFT et Pretto (OAT).</p>
<h3>Concurrents</h3><p>DWS, résultats 2025 et objectifs 2028 ; Schroders (AJ Bell, 15/01/2026) ; Aberdeen, résultats du 03/03/2026 ; Azimut (FinanzaOnline, 12/01/2026) ; BNP Paribas AM (17/03/2026, 05/01/2026) ; BlackRock (résultats T4 2025, plan 2030) ; Intesa Sanpaolo (Eurizon 2024) ; BPCE et Generali ; Vanguard (01/07/2025) ; StockAnalysis (cours et PER, sept.-oct. 2026).</p>
<h3>Presse</h3><p>Reuters (14/01/2025, 30/04/2025, 09/02/2026, 24-25/09/2026) ; Bloomberg (11/12/2025, 29/09/2026) ; Milano Finanza (29/06/2026) ; MarketScreener (02/04/2025, 06/11/2025) ; Investing.com (26/11/2024) ; Der Spiegel (25/02/2025) ; France Épargne ; Zonebourse (29/09/2026) ; Option Finance (19/05/2026) ; Bluerating (23/06/2017) ; ETF Stream ; Legifiscal (01/10/2026) ; Loyens & Loeff (RIS).</p>
<h3>Réglementation</h3><p>Règlement (UE) n° 596/2014 ; règlement délégué (UE) 2016/958 ; décision de la Commission des sanctions de l'AMF (août 2021).</p>
<h3>Photographies</h3><p>Unsplash, licence libre : Lens by Benji (couverture), Léo Crouzille, Michael Yuan, Jess Morgan, Valentin Lacoste, Wassim Chouak, Bastien Nvs, Harsh Kondekar, Martin Gleizes, Mat, Hans Reniers, Arlind Photography.</p>'''
txtpage("Partie X · Après", chap("Chapitre 27", "Annexes", "Sources, méthode, lexique."), srcs)
lex = '''<h3>Méthode de retraitement</h3><p>Les séries sont reprises de la dernière version publiée de chaque exercice. Le résultat « ajusté » est celui d'Amundi (hors amortissement des contrats de distribution, coûts d'intégration, éléments exceptionnels). Les ruptures sont signalées dans le classeur (feuille Ruptures_retraitements) : présentation bancaire 2010-2011, JV à 100 % dans les encours à partir de 2012, Pioneer en 2017, Lyxor fin 2021, Amundi US en 2025. Les marges de 2010-2013 sont calculées sur les revenus nets de gestion, celles de 2015 et après sur les commissions nettes de gestion. Le pont des encours utilise les effets publiés ; son résidu de contrôle est inférieur à 2 Md€ par an, sauf 2021 (effet de marché obtenu par différence). Les changes sont ceux des 16 et 19/10/2026 (106,74 ₹/€ ; 1,1227 $/€).</p>
<h3>Lexique</h3>
<p><b>Encours</b> : actifs gérés pour le compte des clients. <b>Collecte nette</b> : souscriptions moins rachats. <b>Point de base (pb)</b> : 0,01 %. <b>Marge sur commissions</b> : commissions nettes de gestion / encours moyens. <b>Commission de surperformance</b> : commission prélevée quand un fonds bat sa référence. <b>Coefficient d'exploitation</b> : charges / revenus. <b>Rétrocession</b> : part des frais d'un fonds reversée au distributeur. <b>ETF</b> : fonds indiciel coté. <b>Gestion passive</b> : gestion qui réplique un indice. <b>Coentreprise (JV)</b> : société détenue avec un partenaire, mise en équivalence. <b>Mise en équivalence</b> : quote-part du résultat d'une participation non contrôlée. <b>Écart d'acquisition</b> : prix payé au-delà de la valeur comptable des actifs acquis. <b>CET1</b> : fonds propres de base de catégorie 1 rapportés aux actifs pondérés. <b>CRR3</b> : règlement européen sur les exigences de fonds propres, applicable depuis 2025. <b>SREP</b> : exigence de capital fixée par le superviseur. <b>RIS</b> : stratégie européenne pour l'investissement de détail. <b>DIC / KID</b> : document d'information clé. <b>BPA</b> : bénéfice par action. <b>PER</b> : cours / BPA. <b>Somme des parties</b> : valorisation de chaque composante séparément. <b>DCF inversé</b> : lecture du bénéfice implicite dans le cours. <b>Coût des fonds propres</b> : rendement exigé par l'actionnaire. <b>Fonds propres tangibles</b> : capitaux propres moins écarts d'acquisition et incorporels. <b>Effet d'entrée</b> : écart entre l'encours de fin de période et sa moyenne, qui gonfle les revenus de la période suivante.</p>
<h3>Ce que l'étude n'a pas pu établir</h3><p>Montant des pénalités UniCredit ; comptes d'Amundi SGR (registre payant) ; performance des fonds ; sort de la participation de 20 % dans TCW apportée en 2009 ; parcours publié de S. Finkelstein ; conventions détaillées avec le groupe CA après 2020 ; bêta propre (pas de série de cours gratuite accessible).</p>'''
txtpage("Partie X · Après", chap("Chapitre 27, suite", "Méthode et lexique"), lex)

# ====================================================================== DOS
panel('bg-navy', '''<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#fff">
<div style="width:46mm;border-top:.25pt solid rgba(255,255,255,.7)"></div><div style="font-family:Bod;font-weight:500;font-size:12pt;letter-spacing:.42em;text-transform:uppercase;margin:3.2mm 0 3mm">Sous jacent</div><div style="width:46mm;border-top:.25pt solid rgba(255,255,255,.7)"></div>
<div style="font-family:Bod;font-style:italic;font-size:15pt;margin-top:12mm;max-width:120mm;line-height:1.35;color:var(--l2)">Des études d'entreprise signées, datées, sourcées, qui publient un prix et disent ce qui leur donnerait tort.</div>
<div class="kicker" style="margin-top:12mm;color:var(--cu2)">sousjacent.com · Étude n° 2 · Amundi · 20 octobre 2026</div>
<div style="position:absolute;bottom:12mm;font-size:5.8pt;color:#b3c1d4;max-width:160mm">Étude indépendante rédigée par Guillaume Le Merour. Ceci n'est pas un conseil en investissement. L'auteur ne détient pas d'actions Amundi. Tous droits réservés sur le texte et les graphiques ; photographies sous licence Unsplash.</div></div>''', folio=False, dark=True)

css = open('/root/amundi/da/style.css').read()
import re as _re
WM='<div class="wm"><div class="a">Sous-jacent</div><div class="b">sousjacent.com</div></div>'
PAGES=[PAGES[0]]+[pg.replace('</section>', WM+'</section>') for pg in PAGES[1:]]
html = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Amundi — Étude n° 2</title><style>{css}</style></head><body>{"".join(PAGES)}</body></html>'
open('/root/amundi/da/amundi.html', 'w').write(html)
print(len(PAGES), 'pages')
