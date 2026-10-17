# -*- coding: utf-8 -*-
import json, data as d, charts as c
from style import CSS
IMG=json.load(open('/home/claude/vicor/assets/images.json'))

PIED="Sous-jacent · Étude n° 1 · Octobre 2026"
pages=[]

FILIGRANE=('<div class="filigrane"><div class="bloc">'
           '<div class="mot">Sous-jacent</div><div class="url">sousjacent.com</div>'
           '</div></div>')
def P(cls, inner, foot=True, filigrane=True):
    f=f'<div class="foot"><span>{PIED}</span><span><b>sousjacent.com</b></span></div>' if foot else ''
    w=FILIGRANE if filigrane else ''
    pages.append(f'<section class="page {cls}">{w}{inner}{f}</section>')

def head(eyebrow, titre):
    return f'<div class="eyebrow">{eyebrow}</div><div class="rule-v"></div><h2>{titre}</h2>'

def fig(svg, cap, src=None):
    s=f'<div class="srcline">{src}</div>' if src else ''
    return f'<div class="fig">{svg}<div class="figcap">{cap}</div>{s}</div>'

def boxed(t, body, f=None):
    ff=f'<div class="f">{f}</div>' if f else ''
    return f'<div class="boxed"><div class="t">{t}</div>{body}{ff}</div>'

def nb(x, dec=0):
    return f"{x:,.{dec}f}".replace(",", " ").replace(".", ",")

def chapitre(num, titre, items, phrase, img):
    lis="".join(f'<div><span>{n}</span>{t}</div>' for n,t in items)
    return (f'<div class="photo-bg" style="background-image:url({IMG[img]})"></div>'
            f'<div class="photo-veil"></div>'
            f'<div class="mark">{c.logo("clair",26)}</div>'
            f'<div class="photo-inner"><div class="eyebrow">Partie {num}</div>'
            f'<div class="rule-v"></div><h1>{titre}</h1>'
            f'<div class="quote" style="font-size:11.6pt;max-width:118mm">{phrase}</div>'
            f'<div class="chaplist">{lis}</div></div>')

# ======================================================== 1 · COUVERTURE
P('egg cover', f"""
<div class="cover-mark">{c.logo("sombre",46)}</div>
<div class="brand serif">Sous-jacent</div>
<div class="mg">Étude de société cotée<br>Guillaume Le Merour</div>
<div style="position:absolute;left:0;right:0;margin-top:0">
  <div style="height:52mm;background-image:url({IMG['bande']});background-size:cover;background-position:center"></div>
</div>
<div style="height:52mm;margin:22mm 0 20mm"></div>
<div class="ctr serif"><div class="t1">Vicor Corporation</div>
<div class="t2">Vingt et un exercices retraités, 2005-2025</div></div>
<div style="margin-top:26mm;text-align:center" class="small">NASDAQ : VICR &nbsp;·&nbsp; exercices clos au 31 décembre<br>Publié le 17 octobre 2026</div>
""", foot=False, filigrane=False)

# ======================================================== 2 · AVERTISSEMENT
P('cream', head("Avertissement","Ce document n'est pas un conseil en investissement")+"""
<p>Cette étude est un travail d'analyse financière à vocation pédagogique. Elle ne constitue ni une recommandation d'achat, ni une recommandation de vente, ni une invitation à souscrire à un quelconque instrument financier. Elle ne comporte aucun objectif de cours.</p>
<p>La fourchette de valeur intrinsèque présentée en troisième partie est le résultat arithmétique d'un jeu d'hypothèses explicitement énoncé. Elle n'exprime pas une opinion sur le cours de bourse. Son seul objet est de rendre visible le lien entre une hypothèse et une valeur, afin que le lecteur puisse y substituer les siennes. Le classeur de retraitement publié avec cette étude permet de le faire.</p>
<p>L'auteur ne détient aucune position, directe ou indirecte, sur les titres de Vicor Corporation ni sur ceux des sociétés citées en comparaison. Il n'entretient aucune relation d'affaires avec ces sociétés et n'a reçu aucune rémunération au titre de cette publication.</p>
<div class="hr-thin"></div>
<h3>Sources et périmètre</h3>
<p>L'intégralité des données comptables provient des rapports annuels déposés par la société auprès de la <em>Securities and Exchange Commission</em> des États-Unis, formulaires 10-K, identifiant déposant 0000751978, exercices 2005 à 2025. Chaque donnée a été recoupée entre les balises XBRL et le texte des états financiers consolidés. Les écarts relevés sont commentés au chapitre premier, où ils constituent le sujet même de l'étude.</p>
<p>Les cours de bourse historiques proviennent d'une source de marché non réglementaire, signalée dans la note de méthode. Le cours de référence retenu est de <b>202,40 dollars</b>, arrêté au 16 octobre 2026. Les montants sont en milliers de dollars des États-Unis, sauf mention contraire ; les exercices sont clos au 31 décembre.</p>
<div class="hr-thin"></div>
<div class="copyright"><div class="t">Propriété et conditions de reproduction</div>
<p>© 2026 <b>Sous-jacent</b>. L'ensemble de ce document — texte, retraitements, graphiques, modèle de valorisation et mise en page — constitue une œuvre originale protégée par le code de la propriété intellectuelle.</p>
<p>Sa consultation et son téléchargement sont libres. Sa reproduction, sa diffusion ou son adaptation, en tout ou partie, sont soumises à autorisation écrite préalable. La citation de courts extraits est permise à condition de mentionner <b>Sous-jacent · sousjacent.com</b>. Les données comptables brutes, elles, relèvent du domaine public : ce qui est protégé est le travail qui en a été fait.</p>
</div>
""")

# ======================================================== 3 · SOMMAIRE
toc=[(None,"Avant-propos",None),
 ("","Chiffres clés de l'étude","4"),("","La thèse en une page","5"),
 (None,"I · Le fait",None),
 ("1","Quarante-cinq millions logés dans le chiffre d'affaires","7"),
 ("2","Ce que la marge brute ne dit plus","8"),
 ("3","Vicor en vingt et un ans","9"),
 ("4","Un actionnaire, quatre-vingts pour cent des voix","10"),
 (None,"II · Les comptes",None),
 ("5","La méthode de retraitement","12"),
 ("6","Croissance : quatre pour cent l'an","13"),
 ("7","Marges : douze points gagnés, quatre repris","14"),
 ("8","La rentabilité du capital employé","15"),
 ("9","Ce que l'exploitation laisse en caisse","16"),
 ("10","Les licences, ou la bascule du modèle","17"),
 ("11","La cause : le socle produit perdu","18"),
 (None,"III · La valeur",None),
 ("12","Le point de départ : l'exercice 2026","20"),
 ("13","Le modèle et ses hypothèses","21"),
 ("14","La fourchette et sa sensibilité","22"),
 ("15","Le pont vers le cours","23"),
 ("16","Ce que disent les comparables","24"),
 (None,"IV · Les limites",None),
 ("17","Ce que les comptes ne disent pas","27"),
 (None,"Annexes",None),
 ("","Les vingt et un exercices retraités","28"),
 ("","Note de méthode et sources","29"),
 ("","Sources","30")]
rows=""
for n,lab,pg in toc:
    if pg is None: rows+=f'<div class="sec">{lab}</div>'
    else: rows+=f'<div><span class="n">{n}</span><span class="d">{lab}</span><span class="p">{pg}</span></div>'
P('egg', head("Sommaire","Table des matières")+f'<div class="toc">{rows}</div>')

# ======================================================== 4 · CHIFFRES CLÉS
kpi=[("407,7 M$","Chiffre d'affaires 2025, hors règlement de litige",0),
("45,0 M$","Règlement de litige encaissé en 2025, balisé à l'intérieur du chiffre d'affaires",0),
("9,0 %","Marge opérationnelle 2025 retraitée, contre 20,1 % en apparence",0),
("3,5 %","Marge opérationnelle courante moyenne sur vingt et un exercices",0),
("4,2 %","Croissance annuelle moyenne du chiffre d'affaires, 2005-2025",0),
("21,6x","Valeur d'entreprise rapportée au chiffre d'affaires, contre une médiane historique de 3,0x",1)]
cells=""
for i,(v,l,sm) in enumerate(kpi):
    cells+=f'<div class="kpi"><div class="kpi-v{" sm" if sm else ""}">{v}</div><div class="kpi-l">{l}</div></div>'
    if i%2==0: cells+='<div class="vsep"></div>'
P('egg', f"""
<div class="ctr"><div class="eyebrow">Chiffres clés</div><div class="rule-v"></div></div>
<hr class="hr-strong">
<p class="lead" style="text-align:center;margin:0 0 6mm">Six chiffres résument vingt et un exercices,<br>et l'écart entre ce qui est publié et ce qui se répète.</p>
<hr class="hr-strong">
<div class="kpis">{cells}</div>
<div class="note" style="position:absolute;left:22mm;right:22mm;bottom:20mm;text-align:center">
Source : formulaires 10-K, exercices 2005 à 2025, <em>Securities and Exchange Commission</em>, identifiant déposant 0000751978.<br>
Multiple de valorisation calculé au cours du 16 octobre 2026, 202,40 dollars, sur 46,0 millions d'actions diluées.</div>
""")

# ======================================================== 5 · THÈSE
P('cream', f'''<div class="panel" style="background-image:url({IMG['panneau']})">
<div class="pm">{c.logo("clair",24)}</div>
<div><div class="eyebrow" style="color:#B3C4D3;margin-bottom:3mm">Avant-propos</div>
<div class="pt">La thèse en une page</div></div></div>'''+"""
<p class="lead">Le marché paie Vicor pour une entreprise qu'elle n'a jamais été. Cette étude ne dit pas qu'il a tort. Elle dit exactement de combien l'histoire devrait changer.</p>
<div class="hr-thin"></div>
<p>Vicor fabrique des modules d'alimentation électrique depuis 1981. La société est cotée depuis 1990, dirigée depuis l'origine par son fondateur, et suivie par cinq analystes seulement, dont les objectifs de cours publics s'étalent de deux cents à quatre cent cinquante dollars. Cet écart, de plus du simple au double sur une société de douze milliards de dollars de capitalisation, est à lui seul le motif de cette étude.</p>
<p>Vingt et un exercices retraités donnent le portrait suivant : une croissance annuelle moyenne de <b>4,2 %</b>, une marge opérationnelle courante moyenne de <b>3,5 %</b>, une rentabilité du capital employé inférieure en moyenne au coût de ce capital, et six exercices déficitaires sur la période. Ce n'est pas le profil d'une entreprise de rupture. C'est celui d'un équipementier industriel honorable, soumis au cycle, qui n'a jamais transformé durablement son avance technique en rentabilité.</p>
<p>L'exercice 2025 semble rompre avec cela : marge brute de 57,3 %, résultat opérationnel de 81,8 M$, bénéfice net multiplié par dix-neuf. La première partie de cette étude montre que <b>cinquante-cinq pour cent de ce résultat opérationnel provient d'un règlement judiciaire de quarante-cinq millions de dollars</b>, et que ce règlement est balisé par la société à l'intérieur même de son chiffre d'affaires, dans les données que lisent les agrégateurs et les modèles automatiques. Retraité, l'exercice 2025 affiche <b>9,0 %</b> de marge opérationnelle, non 20,1 %.</p>
<p>La deuxième partie reconstruit les comptes sur la longue période et cherche la bascule réelle du modèle. Elle la trouve, mais ailleurs : les revenus de licence passent de 3,9 % du chiffre d'affaires en 2023 à 14,1 % en 2025, tandis que le chiffre d'affaires hors licences reste, en 2025, <b>dix pour cent en dessous de son niveau de 2023</b>. Le socle produit recule, le péage sur les brevets avance. La troisième partie met un prix sur ce basculement, hypothèse par hypothèse.</p>
<div class="hr-thin"></div>
<p class="small">La conclusion de ce travail tient en une phrase : avec les hypothèses les plus favorables que l'historique de la société autorise encore à formuler, le modèle ne rejoint pas le cours. Ce n'est pas un jugement, c'est le résultat d'une arithmétique dont toutes les entrées sont données au chapitre treize, et que le lecteur est invité à refaire.</p>
""")

# ======================================================== 6 · PARTIE I
P('photo', chapitre("I","Le fait",
 [("1","Quarante-cinq millions logés dans le chiffre d'affaires"),
  ("2","Ce que la marge brute ne dit plus"),
  ("3","Vicor en vingt et un ans"),
  ("4","Un actionnaire, quatre-vingts pour cent des voix")],
 "Avant toute valorisation, une vérification. Un chiffre déposé par la société ne dit pas la même chose selon l'endroit où elle le dépose.", "part4"))

# ======================================================== 7 · CH1
tbl="".join(f'<tr{" class=hi" if y==2025 else ""}><td>{y}</td><td class="num">{nb(x)}</td><td class="num">{nb(k)}</td>'
            f'<td class="num{" hi" if y==2025 else ""}">{"+"+nb(x-k) if x!=k else "0"}</td></tr>'
            for y,x,k in [(2019,262977,262977),(2020,296576,296576),(2021,359364,359364),
                          (2024,359058,359058),(2025,452701,407701)])
P('cream', head("Chapitre premier","Quarante-cinq millions logés dans le chiffre d'affaires")+f"""
<p>Le point de départ de cette étude est une vérification élémentaire, que tout lecteur peut refaire en vingt minutes. Les sociétés cotées aux États-Unis déposent leurs comptes deux fois : une fois en texte, dans les états financiers du formulaire 10-K, et une fois en données structurées, au format XBRL, qui est la version lue par les agrégateurs, les écrans de marché et les modèles automatiques. Les deux versions doivent concorder.</p>
<p>Le tableau ci-dessous confronte, pour cinq exercices, la balise XBRL <em>Revenues</em> et la ligne « <em>total net revenues</em> » du texte des 10-K.</p>
<table><caption>Balise XBRL <em>Revenues</em> et texte du 10-K, en milliers de dollars</caption>
<thead><tr><th>Exercice</th><th>Balise XBRL</th><th>Texte du 10-K</th><th>Écart</th></tr></thead>
<tbody>{tbl}</tbody></table>
<p>Quatre exercices concordent au dollar près. Le cinquième s'écarte de quarante-cinq millions exactement — le montant du règlement de litige de brevets encaissé en 2025.</p>
<p>Autrement dit, ce produit non récurrent n'est pas seulement présenté à l'avantage de la société dans le calcul de ses ratios : <b>il est balisé à l'intérieur du chiffre d'affaires lui-même</b>. Un investisseur qui lit les états financiers voit 407,7 M$ de ventes. Un modèle qui lit la donnée structurée voit 452,7 M$. L'écart, 11 % du chiffre d'affaires, est intégralement composé d'un encaissement qui ne se reproduira pas sous cette forme.</p>
{boxed("Définition · élément non récurrent",
 "<p>Un élément non récurrent est un produit ou une charge qui affecte le résultat d'un exercice sans appartenir au cycle normal d'exploitation : une indemnité judiciaire, une dépréciation d'écart d'acquisition, une charge de restructuration. Le retraiter ne consiste pas à le nier — il a bien été encaissé ou décaissé — mais à le sortir de la base servant à projeter les exercices futurs.</p><p>La règle appliquée dans toute cette étude est la suivante : un élément logé en produits affecte la marge brute et la marge opérationnelle ; un élément logé en charges d'exploitation n'affecte que la marge opérationnelle. Cette distinction, apparemment technique, est la source d'erreur la plus courante du retraitement.</p>")}
<p class="srcline">Source : Vicor Corporation, formulaires 10-K des exercices 2019 à 2025, états consolidés de résultat et données XBRL déposées, identifiant 0000751978.</p>
""")

# ======================================================== 8 · CH2
P('cream', head("Chapitre deux","Ce que la marge brute ne dit plus")+f"""
<p>La conséquence du chapitre précédent se lit dans la marge brute. Vicor calcule la sienne en rapportant la marge au total du chiffre d'affaires <em>et</em> du règlement de litige. La société affiche ainsi <b>57,3 %</b> pour 2025. Le même rapport, calculé sur le seul chiffre d'affaires, donne <b>52,6 %</b>.</p>
<p>L'écart de <b>4,7 points</b> est un effet de présentation, non une évolution d'activité. Il faut le distinguer soigneusement de la progression de 51,2 % en 2024 à 57,3 % en 2025, qui est un écart d'une année sur l'autre. Le premier est une convention de calcul, le second un fait économique partiellement expliqué par le premier.</p>
{fig(c.marge_brute(), "La ligne pleine rapporte la marge brute au seul chiffre d'affaires produit ; la ligne pointillée reproduit la présentation retenue par la société, qui ajoute à son dénominateur les produits non récurrents de l'exercice. Les deux lignes se confondent sur toute la période à l'exception de 2025.","Calculs de l'auteur d'après les formulaires 10-K, exercices 2005 à 2025.")}
<p>Le même mécanisme joue sur les autres ratios d'exploitation de l'exercice 2025 : les frais généraux ressortent à 21,9 % du total au lieu de 24,3 % du seul chiffre d'affaires, et la recherche et développement à 17,4 % au lieu de 19,3 %. Chaque ratio gagne entre deux et trois points, dans le même sens, pour la même raison.</p>
<p>Un contrôle de validation a été conduit sur le classeur accompagnant cette étude : la formule reproduisant la présentation de la société redonne exactement le 57,3 % publié pour 2025. C'est la preuve que la chaîne de retraitement est correcte, et non le signe d'une divergence d'interprétation.</p>
""")

# ======================================================== 9 · CH3
P('cream', head("Chapitre trois","Vicor en vingt et un ans")+f"""
<p>Vicor Corporation a été fondée en 1981 à Andover, dans le Massachusetts, par Patrizio Vinciarelli, qui la dirige toujours. La société conçoit et fabrique des modules de conversion de puissance : les composants qui, dans un serveur, un équipement médical ou un satellite, transforment une tension d'entrée en tensions utilisables par les circuits. Son activité se répartit entre deux lignes, les <em>Brick Products</em>, héritage historique de modules standardisés, et les <em>Advanced Products</em>, qui portent les architectures récentes ainsi que les revenus de licence.</p>
{fig(c.ca_barres(), "Le chiffre d'affaires publié passe de 179 M$ en 2005 à 408 M$ en 2025, soit 4,2 % de croissance annuelle moyenne sur vingt ans. La part dorée isole les revenus de licence, dont la société ne publie le détail que depuis l'exercice 2023.","Formulaires 10-K, exercices 2005 à 2025. Les revenus de licence de 2025 excluent le règlement de litige de 45 M$.")}
<p>La série raconte une entreprise cyclique plus qu'une entreprise de croissance. Trois phases se distinguent : une stagnation de 2005 à 2009 autour de deux cents millions de dollars ; un cycle 2010-2017 qui culmine à 253 M$ en 2011 avant de retomber à 200 M$ en 2016 ; puis une phase d'accélération à partir de 2018, portée par l'alimentation des centres de données, qui mène le chiffre d'affaires à 405 M$ en 2023 avant un recul de 11 % en 2024.</p>
<p>Six exercices sur vingt et un se soldent par une perte opérationnelle publiée. Quatre affichent un chiffre d'affaires en recul. Une entreprise dont le produit serait structurellement indispensable à une technologie en expansion ne présenterait pas ce profil : elle présenterait une pente. Vicor présente un cycle.</p>
""")

# ======================================================== 10 · CH4 (page vedette)
P('feature', f"""
<div class="feat-img" style="background-image:url({IMG['feature']})"></div>
<div class="feat-body">
<div class="mark">{c.logo("sombre",24)}</div>
{head("Chapitre quatre","Un actionnaire,<br>quatre-vingts pour cent des voix")}
<p>Le capital de Vicor est divisé en deux classes. Les actions ordinaires, cotées, donnent une voix chacune ; il en existe 33 646 426. Les actions de catégorie B, non cotées, donnent dix voix chacune ; il en existe 11 726 718.</p>
<p>Patrizio Vinciarelli détient <b>94,0 % de la catégorie B</b>. Il contrôle en conséquence <b>79,6 % des droits de vote pour 46,9 % du capital</b>. Fondateur, président-directeur général depuis 1981, il dispose seul de la majorité à toute assemblée générale, ordinaire comme extraordinaire.</p>
<p>Cette structure a trois conséquences qu'un investisseur minoritaire doit tenir pour acquises. Aucune opération hostile n'est possible : la prime de contrôle que le marché prête parfois aux sociétés de cette taille est ici inexistante. Aucune pression actionnariale ne peut s'exercer sur la stratégie, notamment sur la décision d'orienter l'entreprise vers l'exploitation de ses brevets plutôt que vers la reconquête de ses parts de marché. Enfin, la société reconnaît elle-même, dans ses facteurs de risque, la dépendance à une personne clé.</p>
<p>S'y ajoute une contrainte de marché : le flottant et les volumes quotidiens sont réduits au regard de la capitalisation. Une position significative ne se construit ni ne se défait sans affecter le cours, ce que la société signale également au titre de ses facteurs de risque.</p>
<div class="hr-thin"></div>
<p class="small">Ces éléments ne figurent pas ici au titre d'un jugement sur la gouvernance. Ils y figurent parce qu'ils conditionnent la lecture de la troisième partie : la stratégie de licence décrite au chapitre dix est la décision d'un actionnaire qui n'a de comptes à rendre à personne, et que rien ne contraindra à en changer.</p>
<p class="srcline">Source : Vicor Corporation, formulaire 10-K de l'exercice 2025, parties I et III.</p>
</div>""")

# ======================================================== 11 · PARTIE II
P('photo', chapitre("II","Les comptes",
 [("5","La méthode de retraitement"),("6","Croissance : quatre pour cent l'an"),
  ("7","Marges : douze points gagnés, quatre repris"),("8","La rentabilité du capital employé"),
  ("9","Ce que l'exploitation laisse en caisse"),("10","Les licences, ou la bascule du modèle"),
  ("11","La cause : le socle produit perdu")],
 "Vingt et un exercices ramenés à une base homogène. Ce qui se répète, mis à part de ce qui n'a eu lieu qu'une fois.", "part2"))

# ======================================================== 12 · CH5 méthode
nr_rows=""
for y in sorted(d.NR):
    for lab,cp,m,k in d.NR[y]:
        nr_rows+=(f'<tr><td class="num">{y}</td><td>{lab}</td><td>{cp or "—"}</td>'
                  f'<td style="text-align:center">{"produits" if k=="produits" else "charges"}</td>'
                  f'<td class="num{" hi" if abs(m)>=19000 else ""}">{"+" if m>0 else "−"}{nb(abs(m))}</td></tr>')
P('cream', head("Chapitre cinq","La méthode de retraitement")+f"""
<p>Retraiter des comptes consiste à ramener vingt et un exercices à une base comparable. L'opération est mécanique, mais elle décide de tout ce qui suit : une moyenne calculée sur des chiffres publiés tels quels mélange le cycle d'exploitation et des événements uniques, et ne mesure plus rien.</p>
<p>Le relevé ci-dessous recense les éléments non récurrents identifiés, exercice par exercice, par lecture du texte des états financiers. La colonne « rubrique » indique s'ils sont logés en produits ou en charges d'exploitation : c'est elle qui détermine s'ils affectent la marge brute ou seulement la marge opérationnelle.</p>
<table class="plain"><caption>Éléments non récurrents relevés, 2005-2025, en milliers de dollars</caption>
<thead><tr><th>Exercice</th><th>Libellé</th><th>Contrepartie</th><th style="text-align:center">Rubrique</th><th>Montant</th></tr></thead>
<tbody>{nr_rows}</tbody></table>
<p>Deux dossiers judiciaires distincts apparaissent dans ce relevé et ne doivent pas être confondus. La charge de 19 500 k$ de 2024 est une provision sur le litige <b>SynQor</b>, qui a assigné Vicor en janvier 2011 : la société y est payeur potentiel. Le produit de 45 000 k$ de 2025 provient d'accords conclus le 1<sup>er</sup> mai 2025 avec des parties non nommées dans le dépôt ; <b>rien ne permet de l'identifier au dossier SynQor</b>. Les frais juridiques associés à l'exercice 2025 s'élèvent à 5,1 M$, logés en frais généraux.</p>
<p>Deux retraitements changent le signe d'un exercice. L'exercice 2006, qui affiche une perte opérationnelle publiée de 33,2 M$, redevient <b>bénéficiaire à 2,1 %</b> une fois neutralisés les 37,2 M$ de perte nette sur le litige Ericsson — cinquante millions versés, douze huit cents repris par les assureurs. L'exercice 2024, publié à −0,4 %, ressort à <b>+5,1 %</b> une fois la provision SynQor écartée.</p>
<p class="small">Le gain de 1 975 k$ de 2012 est la queue de comète du dossier Ericsson : il provient de la procédure engagée contre les assureurs, soldée le 3 octobre 2012.</p>
""")

# ======================================================== 13 · CH6 croissance
cr5=[(2005,2010,"+6,9 %"),(2010,2015,"−2,6 %"),(2015,2020,"+6,1 %"),(2020,2025,"+6,6 %")]
P('cream', head("Chapitre six","Croissance : quatre pour cent l'an")+f"""
<p>Sur vingt ans pleins, de 2005 à 2025, le chiffre d'affaires progresse de 4,2 % par an en moyenne géométrique. Ce chiffre unique masque deux régimes distincts : <b>3,8 % par an de 2005 à 2018</b>, puis <b>4,9 % par an de 2018 à 2025</b>. L'accélération existe, elle est réelle, mais elle est d'un point et demi — pas d'un ordre de grandeur.</p>
<table><caption>Croissance annuelle moyenne par sous-période</caption>
<thead><tr><th>Période</th><th>Chiffre d'affaires de départ</th><th>Chiffre d'affaires d'arrivée</th><th>Croissance annuelle</th></tr></thead>
<tbody>{"".join(f'<tr><td>{a}–{b}</td><td class="num">{nb(d.CA[a])}</td><td class="num">{nb(d.CA[b])}</td><td class="num">{g}</td></tr>' for a,b,g in cr5)}</tbody></table>
<p>La volatilité importe autant que la moyenne. L'écart type des croissances annuelles atteint treize points sur la période. Le meilleur exercice, 2010, affiche +26,7 % ; le plus mauvais, 2012, −13,6 %. Une entreprise dont le produit serait un passage obligé verrait sa demande amortie par la nécessité ; celle-ci subit le cycle de ses clients sans atténuation.</p>
{fig(c.marge_op(), "Marge opérationnelle publiée, en gris, et marge opérationnelle retraitée des éléments non récurrents, en bleu. Deux exercices changent de signe au retraitement : 2006 et 2024. L'exercice 2025 perd onze points.","Calculs de l'auteur d'après les formulaires 10-K, exercices 2005 à 2025.")}
<p>Le graphique ci-dessus anticipe le chapitre suivant, mais il résume la série : sur vingt et un exercices, la marge opérationnelle courante franchit dix pour cent trois fois — en 2010, en 2018 et en 2021 — et le reste du temps oscille entre −10 % et +7 %.</p>
""")

# ======================================================== 14 · CH7 marges
P('cream', head("Chapitre sept","Marges : douze points gagnés, quatre repris")+f"""
<p>Le progrès industriel de Vicor sur la période est réel et mesurable : la marge brute, calculée sur le seul chiffre d'affaires, passe de <b>39,8 % en 2005 à 52,6 % en 2025</b>, soit douze virgule huit points gagnés en vingt ans. C'est le résultat d'une montée en gamme : les <em>Advanced Products</em>, plus denses en valeur, remplacent progressivement les modules historiques.</p>
<p>Ce gain ne parvient pourtant pas jusqu'au résultat. Sur la même période, la somme de la recherche et développement et des frais généraux passe de <b>39,2 % à 43,6 % du chiffre d'affaires</b>. Quatre points et demi des douze gagnés en haut du compte de résultat sont repris plus bas.</p>
{fig(c.frais(), "La marge brute monte de treize points ; la charge de structure en absorbe quatre et demi. L'écart entre les deux courbes est, à peu de chose près, la marge opérationnelle courante.","Calculs de l'auteur d'après les formulaires 10-K, exercices 2005 à 2025.")}
<p>Deux lectures de ce phénomène sont possibles, et cette étude ne tranche pas entre elles. La première y voit un investissement : la recherche et développement passe de 29 M$ en 2005 à 79 M$ en 2025, et c'est elle qui produit les brevets aujourd'hui monétisés. La seconde y voit une perte de levier d'exploitation : une société qui gagne treize points de marge brute en vingt ans sans en convertir un seul en marge opérationnelle n'a pas trouvé son échelle.</p>
<p>La moyenne de la marge opérationnelle courante sur les vingt et un exercices s'établit à <b>3,5 %</b>. Le meilleur exercice de la série reste 2021, à 15,5 %. L'exercice 2025 retraité, à 9,0 %, se situe au deuxième rang de la série — c'est un bon exercice, mais pas un exercice de rupture.</p>
""")

# ======================================================== 15 · CH8 ROIC
P('cream', head("Chapitre huit","La rentabilité du capital employé")+f"""
<p>La marge dit ce que l'entreprise gagne sur ce qu'elle vend ; elle ne dit pas ce qu'il a fallu immobiliser pour le vendre. C'est l'objet de la rentabilité du capital employé, qui rapporte le résultat opérationnel après impôt normatif au capital réellement mobilisé par l'exploitation.</p>
{boxed("Définition · rentabilité du capital employé",
 "<p>Le numérateur est le résultat opérationnel courant diminué d'un impôt normatif de 21 % : c'est ce que l'exploitation laisse, indépendamment du financement. Le dénominateur est le capital employé moyen de l'exercice, soit les capitaux propres augmentés des dettes et diminués de la trésorerie excédentaire.</p><p>La comparaison qui compte n'est pas avec zéro, mais avec le coût du capital — le rendement qu'exigent ceux qui ont apporté cet argent. Une entreprise dont la rentabilité du capital reste durablement sous son coût du capital détruit de la valeur même en affichant un bénéfice.</p>",
 "Rentabilité = Résultat opérationnel courant × (1 − 21 %) ÷ Capital employé moyen")}
{fig(c.roic_ch(), "Rentabilité du capital employé retraitée, exercices 2011 à 2025. La ligne dorée marque le coût du capital retenu dans la troisième partie de cette étude, soit 10 %.","Calculs de l'auteur d'après les formulaires 10-K. Série débutant en 2011, le calcul exigeant un capital employé d'ouverture.")}
<p>La moyenne s'établit à <b>4,6 %</b> sur les exercices calculables, pour un coût du capital retenu à 10 %. Trois exercices seulement franchissent ce seuil : 2018, 2021 et 2023. L'exercice 2021, meilleur de la série, atteint 20,4 %.</p>
<p>La rotation du capital employé, à <b>2,0 fois</b> en moyenne, n'est pas en cause : l'entreprise fait tourner son capital correctement. C'est la marge qui manque. Ce constat a une conséquence directe sur la troisième partie : toute projection qui retient une rentabilité durablement supérieure à 10 % postule une rupture par rapport à l'intégralité de l'historique disponible, et doit l'assumer comme telle.</p>
""")

# ======================================================== 16 · CH9 cash
P('cream', head("Chapitre neuf","Ce que l'exploitation laisse en caisse")+f"""
<p>Un résultat comptable se décide ; un flux de trésorerie se constate. L'épreuve de vérité d'une série longue est la conversion du résultat en liquidités disponibles.</p>
{boxed("Définition · flux de trésorerie disponible",
 "<p>Le flux de trésorerie disponible est ce que l'exploitation laisse une fois les investissements payés. On part de la trésorerie générée par l'activité, qui intègre les variations du besoin en fonds de roulement, et on en retranche les acquisitions d'immobilisations corporelles.</p><p>C'est le seul montant dont un actionnaire puisse espérer, à terme, qu'il lui revienne : le reste est soit immobilisé, soit déjà consommé.</p>",
 "Flux disponible = Trésorerie d'exploitation − Investissements corporels")}
{fig(c.fcf_ch(), "Flux de trésorerie disponible annuel, en millions de dollars. Le creux de 2021-2022 correspond au pic d'investissement industriel, jusqu'à 16 % du chiffre d'affaires.","Formulaires 10-K, tableaux consolidés de flux de trésorerie, exercices 2009 à 2025.")}
<p>Le profil est net : huit exercices sur dix-sept dégagent moins de vingt millions de dollars, deux sont négatifs, et l'exercice 2025 affiche à lui seul 119 M$ — dont une part substantielle provient de l'encaissement du règlement de litige déjà commenté.</p>
<p>Le bilan de clôture 2025 porte une trésorerie nette de <b>395 M$</b>, sans dette financière. C'est une situation confortable, et elle est intégrée telle quelle à la valorisation de la troisième partie : la trésorerie nette s'ajoute à la valeur d'entreprise pour obtenir la valeur des capitaux propres. Elle représente environ huit dollars et demi par action, soit un peu plus de quatre pour cent du cours.</p>
""")

# ======================================================== 17 · CH10 licences
lic_rows="".join(
 f'<tr><td class="num">{y}</td><td class="num">{nb(d.LICENCES[y])}</td>'
 f'<td class="num">{nb(d.LICENCES[y]/d.CA[y]*100,1)} %</td>'
 f'<td class="num">{nb(d.CA[y]-d.LICENCES[y])}</td>'
 f'<td class="num{" hi" if y!=2023 else ""}">{("+" if (d.CA[y]-d.LICENCES[y])/(d.CA[y-1]-d.LICENCES.get(y-1,0))-1>0 else "−") + nb(abs(((d.CA[y]-d.LICENCES[y])/(d.CA[y-1]-d.LICENCES.get(y-1,0))-1)*100),1)+" %" if y>2023 else "—"}</td></tr>'
 for y in (2023,2024,2025))
P('cream', head("Chapitre dix","Les licences, ou la bascule du modèle")+f"""
<p>La rupture que cherche cette étude existe bel et bien. Elle n'est pas où le compte de résultat 2025 la place, et elle a une conséquence que le chiffre d'affaires consolidé dissimule.</p>
<table><caption>Revenus de licence et chiffre d'affaires hors licences, en milliers de dollars</caption>
<thead><tr><th>Exercice</th><th>Licences</th><th>Part du CA</th><th>CA hors licences</th><th>Évolution</th></tr></thead>
<tbody>{lic_rows}</tbody></table>
<p>Les revenus de licence sont multipliés par trois et demi en deux ans et passent de 3,9 % à 14,1 % du chiffre d'affaires. Dans le même temps, le chiffre d'affaires hors licences recule de 19,7 % en 2024, se redresse de 12,1 % en 2025, et demeure <b>10,0 % en dessous de son niveau de 2023</b>.</p>
<p>Le fait brut est donc celui-ci : <b>sur deux exercices, la croissance apparente de Vicor est entièrement imputable aux licences, tandis que l'activité de vente de produits s'est contractée.</b> La société ne le dissimule pas — le détail figure dans ses dépôts — mais le chiffre d'affaires consolidé, seul retenu par la plupart des écrans, présente une entreprise qui a retrouvé la croissance.</p>
<p>Un revenu de licence n'a pas la même nature économique qu'une vente de produit. Il ne consomme presque pas de capital, ce qui est favorable à la rentabilité ; mais il dépend d'accords dont l'échéance, la portée et l'exclusivité ne sont pas publiées, et dont la pérennité repose sur la validité de brevets contestables en justice. La troisième partie de cette étude pose cette question en termes chiffrés : quelle part du revenu de licence faut-il tenir pour récurrente pour justifier le cours ?</p>
<p class="small">La société indique viser, à terme, un ordre de grandeur proche de trois cents millions de dollars de revenus annuels de licence. Ce chiffre est une ambition déclarée, non un carnet de commandes contractualisé : il est traité comme tel au chapitre treize.</p>
""")

# ======================================================== 18 · CH11 la cause
P('cream', head("Chapitre onze","La cause : le socle produit perdu")+"""
<p>Le chapitre précédent décrit un basculement ; celui-ci en propose la cause. Elle ne se lit pas dans les comptes : elle se lit dans l'histoire technique du marché de l'alimentation des accélérateurs d'intelligence artificielle.</p>
<p>Vicor a équipé les générations V100 puis A100 de Nvidia, ainsi que les processeurs spécialisés de Google. La société disposait alors d'une avance reconnue sur la conversion de puissance au plus près du calculateur — ce que le secteur appelle le dernier pouce. Lors de la génération suivante, la H100, <b>Monolithic Power Systems a remplacé Vicor</b>, qui n'y a jamais livré en volume.</p>
<p class="quote">Le virage vers les licences n'est pas l'exploitation d'une position dominante. C'est la réponse d'une entreprise qui a perdu son socle produit et transforme ses brevets en péage.</p>
"""+f'<div class="band" style="background-image:url({IMG["bande"]})"></div>'+"""
<div class="bandcap">Le marché final : l'alimentation des accélérateurs de calcul, où Vicor a équipé les générations V100 et A100 avant d'en être écartée.</div>
<p>Cette lecture réconcilie l'ensemble des observations précédentes. Elle explique pourquoi le chiffre d'affaires hors licences recule de 2023 à 2025 alors que le marché final connaît l'expansion la plus rapide de son histoire. Elle explique pourquoi la société engage simultanément des procédures devant l'<em>International Trade Commission</em> des États-Unis et obtient des ordonnances d'exclusion. Elle explique enfin pourquoi la stratégie de licence est présentée comme un axe de développement et non comme un complément de revenu.</p>
<p>Elle a une conséquence directe sur la valorisation. Si les licences constituent un revenu de rente sur une propriété intellectuelle incontournable, la marge normative élevée retenue au chapitre treize est justifiée, et la valeur suit. Si elles constituent la monétisation d'une position en recul, ce revenu est par nature décroissant, et la marge normative doit être revue vers le bas. Les deux lectures sont défendables sur les informations publiques disponibles. Cette étude retient la première — l'hypothèse la plus favorable à la société — et montre que même ainsi, le compte n'y est pas.</p>
<p class="srcline">Source : SemiAnalysis, « Energizing AI Power Delivery Competition ». Les éléments relatifs aux procédures devant l'International Trade Commission proviennent du formulaire 10-K de l'exercice 2025.</p>
""")

# ======================================================== 19 · PARTIE III
P('photo', chapitre("III","La valeur",
 [("12","Le point de départ : l'exercice 2026"),("13","Le modèle et ses hypothèses"),
  ("14","La fourchette et sa sensibilité"),("15","Le pont vers le cours"),
  ("16","Ce que disent les comparables")],
 "On ne demande pas au modèle si le cours est juste. On lui demande quelles hypothèses il faudrait retenir pour que le cours le devienne.", "part3"))

# ======================================================== 20 · CH12 2026
P('cream', head("Chapitre douze","Le point de départ : l'exercice 2026")+f"""
<p>Un modèle de valorisation ne vaut que par son point de départ. Projeter à partir du chiffre d'affaires 2025 de 407,7 M$ serait une faute : l'exercice en cours est très supérieur, et il est largement connu.</p>
{fig(c.trimestres(), "Les deux premiers trimestres sont publiés ; le troisième reprend la prévision donnée par la société ; le quatrième est une estimation de l'auteur, prolongeant la tendance des redevances et du carnet.","Résultats trimestriels publiés par Vicor Corporation, exercices 2026. L'estimation du quatrième trimestre engage l'auteur seul.")}
<p>Le total ainsi reconstitué s'établit à <b>639,8 M$</b> pour l'exercice 2026, dont 452,5 M$ de produits et 187,2 M$ de redevances. Rapporté aux 407,7 M$ de 2025, c'est une croissance de <b>57 %</b>, dont l'essentiel provient des redevances.</p>
<p>Deux éléments étayent ce point de départ. Le carnet de commandes à fin juin 2026 s'établit à <b>380 M$</b>, en progression de 145 % sur un an. Le saut du troisième trimestre provient de la première licence non exclusive accordée sur l'architecture d'alimentation verticale.</p>
<p>Il faut cependant mesurer la part de l'estimation dans ce chiffre : les deux premiers trimestres, publiés, représentent 256,4 M$ ; le troisième, prévu par la société, 186,4 M$ ; le quatrième, estimé par l'auteur, 197,0 M$. <b>Trente pour cent du point de départ du modèle relève donc d'une estimation personnelle</b>, et quarante pour cent supplémentaires d'une prévision de la société. Le lecteur qui retiendrait un quatrième trimestre stable plutôt qu'en progression abaisserait la valeur centrale d'environ trois dollars par action.</p>
""")

# ======================================================== 21 · CH13 hypothèses
r=d.dcf()
hyp=[("Chiffre d'affaires 2026","639,8 M$","reconstitué, chapitre douze"),
("Croissance 2027 à 2035","30, 22, 16, 12, 10, 8, 6, 5, 4 %","décroissance régulière"),
("Chiffre d'affaires 2035",f"{nb(r['ca_terminal'],0)} M$","soit 4,5 fois celui de 2025"),
("Marge opérationnelle de départ","26 %","niveau implicite de l'exercice 2026"),
("Marge opérationnelle normative","33 %","atteinte en 2035, puis maintenue"),
("Taux d'imposition normatif","21 %","taux fédéral des États-Unis"),
("Rotation du capital employé","2,6 fois","contre 2,0 fois en historique"),
("Coût moyen pondéré du capital","10 %","retenu uniforme sur la période"),
("Croissance à l'infini","3 %","au-delà de 2035"),
("Trésorerie nette","395,4 M$","au 31 décembre 2025"),
("Nombre d'actions diluées","46,0 millions","exercice 2025")]
P('cream', head("Chapitre treize","Le modèle et ses hypothèses")+f"""
<p>Le modèle retenu est une actualisation des flux de trésorerie disponibles sur dix ans, prolongée par une valeur terminale. Onze hypothèses suffisent à le définir ; elles sont toutes données ci-dessous, afin que le lecteur puisse les remplacer.</p>
<table class="plain"><caption>Les onze hypothèses du modèle</caption>
<thead><tr><th>Hypothèse</th><th>Valeur retenue</th><th>Observation</th></tr></thead>
<tbody>{"".join(f'<tr><td>{a}</td><td class="num">{b}</td><td style="text-align:left;color:#6F7F86;font-size:7.8pt">{cc}</td></tr>' for a,b,cc in hyp)}</tbody></table>
{boxed("Définition · réinvestissement et actualisation",
 "<p>Une entreprise qui croît doit financer cette croissance : stocks, créances, machines. Le modèle en tient compte par la rotation du capital, qui indique combien de chiffre d'affaires supplémentaire un dollar de capital permet de produire. Avec une rotation de 2,6 fois, cent dollars de chiffre d'affaires nouveau exigent trente-huit dollars de capital nouveau, retranchés du flux de l'année.</p><p>Actualiser consiste ensuite à ramener chaque flux futur à sa valeur d'aujourd'hui : un dollar attendu dans cinq ans, au coût du capital de 10 %, vaut soixante-deux centimes aujourd'hui.</p>",
 "Flux de l'année = Résultat opérationnel × (1 − impôt) − Croissance du chiffre d'affaires ÷ Rotation")}
<p>Trois de ces hypothèses sont nettement favorables à la société et méritent d'être signalées. La marge normative de 33 % est <b>neuf fois la moyenne historique</b> de 3,5 % et double le meilleur exercice jamais réalisé. La rotation du capital de 2,6 fois dépasse l'historique, au motif que les revenus de licence ne consomment pas de capital. La trajectoire de croissance multiplie le chiffre d'affaires par 4,5 en dix ans, contre 2,3 fois sur les vingt années précédentes.</p>
<p class="small">La valeur terminale représente <b>{nb(r['part_vt'],0)} %</b> de la valeur d'entreprise obtenue. C'est élevé, et c'est inhérent à l'exercice : l'essentiel de ce que l'on valorise ici se situe au-delà de 2035, c'est-à-dire au-delà de ce que l'on peut raisonnablement prévoir.</p>
""")

# ======================================================== 22 · CH14 fourchette
grid=""
for m in (0.26,0.30,0.33,0.36,0.40):
    tds="".join(f'<td class="num{" hi" if (m==0.33 and w==0.10) else ""}">{nb(d.dcf(m,w)["par_action"],0)}</td>' for w in (0.09,0.10,0.11,0.12))
    lab=f'<b>{int(m*100)} %</b>' if m==0.33 else f'{int(m*100)} %'
    grid+=f'<tr><td>{lab}</td>{tds}</tr>'
bas=d.dcf(0.31,0.105)['par_action']; haut=d.dcf(0.35,0.095)['par_action']; cen=d.dcf()['par_action']
P('egg', head("Chapitre quatorze","La fourchette et sa sensibilité")+f"""
<p>Avec les hypothèses du chapitre précédent, le modèle produit une valeur intrinsèque de <b>{nb(cen,0)} dollars par action</b>. En faisant varier la marge normative de 31 à 35 % et le coût du capital de 9,5 à 10,5 %, la fourchette s'établit entre <b>{nb(bas,0)}</b> et <b>{nb(haut,0)} dollars</b>.</p>
<div class="kpis" style="grid-template-columns:1fr 1px 1fr 1px 1fr;margin:8mm 0 9mm">
<div class="kpi"><div class="kpi-v sm">{nb(bas,0)} $</div><div class="kpi-l">Borne basse<br><span style="color:#6F7F86">marge 31 %, capital 10,5 %</span></div></div>
<div class="vsep"></div>
<div class="kpi"><div class="kpi-v">{nb(cen,0)} $</div><div class="kpi-l">Valeur centrale<br><span style="color:#6F7F86">marge 33 %, capital 10,0 %</span></div></div>
<div class="vsep"></div>
<div class="kpi"><div class="kpi-v sm">{nb(haut,0)} $</div><div class="kpi-l">Borne haute<br><span style="color:#6F7F86">marge 35 %, capital 9,5 %</span></div></div>
</div>
<hr class="hr-strong">
<table class="plain"><caption>Valeur par action, en dollars, selon la marge normative et le coût du capital</caption>
<thead><tr><th>Marge normative</th><th>Capital 9 %</th><th>Capital 10 %</th><th>Capital 11 %</th><th>Capital 12 %</th></tr></thead>
<tbody>{grid}</tbody></table>
<p style="margin-top:5mm">Vingt combinaisons d'hypothèses sont présentées ci-dessus. La plus favorable d'entre elles — une marge normative de 40 %, supérieure à celle d'Analog Devices, associée à un coût du capital de 9 % — produit {nb(d.dcf(0.40,0.09)['par_action'],0)} dollars par action. <b>Aucune case de cette grille ne rejoint le cours de 202,40 dollars.</b></p>
<p>Ce constat n'est pas une conclusion sur le cours ; c'est une délimitation du débat. Il indique que l'écart entre ce modèle et le marché ne se résout ni par la marge, ni par le coût du capital, ni par aucune combinaison des deux dans des bornes défendables. Il se résout ailleurs — par la trajectoire de croissance elle-même, ce qu'examine le chapitre suivant.</p>
""")

# ======================================================== 23 · CH15 pont
P('cream', head("Chapitre quinze","Le pont vers le cours")+f"""
<p>La question centrale de cette étude peut maintenant être posée dans sa forme la plus utile : <em>que faut-il ajouter au modèle pour qu'il produise le cours observé ?</em> La réponse se construit par étapes, chacune isolant une hypothèse.</p>
{fig(c.pont(), "Chaque barre dorée mesure, en dollars par action, l'apport d'une hypothèse supplémentaire à la valeur du modèle central. Le cours observé se situe entre la troisième et la quatrième étape.","Calculs de l'auteur. Détail des hypothèses de chaque étape ci-dessous.")}
<p>Les quatre étapes se lisent ainsi. <b>Premièrement</b>, porter la trajectoire de croissance de 4,5 à environ 7 fois le chiffre d'affaires de 2025 sur dix ans ajoute cinquante-deux dollars. <b>Deuxièmement</b>, porter la marge normative de 33 à 40 % — au-dessus de celle d'Analog Devices, le meilleur opérateur comparable — en ajoute trente-deux. <b>Troisièmement</b>, abaisser le coût du capital de 10 à 9 % en ajoute trente-six. <b>Quatrièmement</b>, alléger encore le capital employé en ajoute six.</p>
<p>Le cours de 202,40 dollars est atteint une fois les trois premières étapes franchies simultanément. Formulé autrement, et c'est la phrase que cette étude propose de retenir :</p>
<p class="quote">Le cours actuel suppose que Vicor croisse sept fois plus vite qu'en vingt ans, atteigne une marge supérieure à celle du meilleur opérateur du secteur, et le fasse avec un risque inférieur à celui du marché.</p>
<p>Chacune de ces trois conditions est concevable isolément. Leur conjonction définit précisément le pari que le cours incorpore. Cette étude ne dit pas qu'il est perdu : elle dit qu'il est celui-là, et non un autre.</p>
""")

# ======================================================== 24 · CH16 comparables
comp=[("Vicor, exercice 2025","408 M$","52,6 %","9,0 %"),
("Monolithic Power Systems","3 273 M$","55,2 %","28,7 %"),
("Analog Devices","13 882 M$","65,8 %","35,7 %"),
("Infineon Technologies","15 591 M€","41,1 %","16,3 %")]
P('cream', head("Chapitre seize","Ce que disent les comparables")+f"""
<p>Un modèle de valorisation se contrôle de l'extérieur. Les trois sociétés retenues ci-dessous opèrent sur le même marché de la conversion de puissance et de l'analogique ; la première est précisément celle qui a remplacé Vicor sur la génération H100.</p>
<table><caption>Comparaison d'exploitation, douze mois glissants sauf Vicor</caption>
<thead><tr><th>Société</th><th>Chiffre d'affaires</th><th>Marge brute</th><th>Marge opérationnelle</th></tr></thead>
<tbody>{"".join(f'<tr><td>{a}</td><td class="num">{b}</td><td class="num">{cc}</td><td class="num">{e}</td></tr>' for a,b,cc,e in comp)}</tbody></table>
<p>La lecture est instructive. La marge brute de Vicor, à 52,6 %, soutient la comparaison avec Monolithic Power Systems, à 55,2 %. Le produit n'est donc pas en cause.</p>
<p>La marge opérationnelle, en revanche, est trois fois inférieure. L'écart ne vient pas de la qualité du produit mais de l'échelle : Monolithic Power Systems réalise huit fois le chiffre d'affaires de Vicor et amortit sa structure de recherche sur une base huit fois plus large. C'est exactement le phénomène décrit au chapitre sept — treize points de marge brute gagnés, dont aucun n'atteint le résultat.</p>
<p>Cette observation a une conséquence pour le modèle. La marge normative de 33 % retenue au chapitre treize n'est pas absurde sur le plan industriel : elle correspond à ce que réalise aujourd'hui Monolithic Power Systems. Elle suppose simplement que Vicor atteigne une échelle qu'elle n'a jamais eue, ce que la trajectoire de croissance du modèle intègre déjà par ailleurs.</p>
<p>Elle éclaire aussi la limite de l'exercice comparatif. Aucune des trois sociétés du tableau ne tire une part significative de ses revenus de l'exploitation de brevets. La comparaison vaut donc pour l'activité industrielle de Vicor, qui représente aujourd'hui 86 % de son chiffre d'affaires, et non pour les licences, qui en portent l'essentiel de la croissance et pour lesquelles aucun comparable coté direct n'existe.</p>
""")

# ======================================================== 25 · CH16 bis
P('cream', head("Chapitre seize (suite)","Le multiple, et ce qu'il résume")+f"""
{fig(c.ve_ca(), "Valeur d'entreprise rapportée au chiffre d'affaires, à quelques dates de référence. La barre de droite est calculée au cours du 16 octobre 2026.","Calculs de l'auteur. Cours de clôture de fin d'exercice issus d'une source de marché non réglementaire, signalée en note de méthode.")}
<p>Le multiple actuel de <b>21,6 fois</b> le chiffre d'affaires se compare à une médiane historique de 3,0 fois et à un sommet de 15,3 fois atteint fin 2021, au point haut du cycle précédent. Le marché valorise aujourd'hui chaque dollar de vente de Vicor sept fois plus cher que la médiane de ses vingt et un derniers exercices, et quarante pour cent plus cher qu'au sommet du cycle précédent.</p>
<p>Un multiple n'est pas un argument : il résume des hypothèses implicites plutôt qu'il ne les démontre, et il est d'autant plus trompeur ici que son dénominateur mélange des ventes de produits et des redevances qui n'ont ni la même marge ni la même durabilité. Il a néanmoins une vertu de cadrage. Ramené au chiffre d'affaires reconstitué de l'exercice 2026, 639,8 M$, le multiple retombe à <b>13,7 fois</b> ; ramené au chiffre d'affaires de 2035 retenu par le modèle, à 3,1 fois — soit, à cet horizon, la médiane historique.</p>
<p class="quote" style="font-size:11.4pt">Le cours n'exige donc pas que Vicor devienne une autre entreprise : il exige qu'elle le devienne vite, et qu'elle le reste.</p>
<p>C'est, en une phrase, la conclusion des trois chapitres précédents. Le modèle du chapitre treize accorde déjà à la société une croissance de quatre fois et demie en dix ans et une marge neuf fois supérieure à sa moyenne historique. L'écart qui subsiste avec le cours ne porte pas sur la nature de l'entreprise, mais sur le rythme auquel le marché suppose qu'elle se transforme.</p>
""")

# ======================================================== 25 · PARTIE IV
P('photo', chapitre("IV","Les limites",
 [("17","Ce que les comptes ne disent pas")],
 "Toute étude se juge à ce qu'elle reconnaît ignorer. Quatre inconnues conditionnent les conclusions qui précèdent.", "part1"))

# ======================================================== 26 · CH17
P('cream', head("Chapitre dix-sept","Ce que les comptes ne disent pas")+"""
<h3>L'échéance et la portée des accords de licence</h3>
<p>C'est l'inconnue majeure de ce dossier. Les dépôts ne publient ni la durée des accords, ni leur caractère exclusif ou non, ni le mode de calcul des redevances. Or la marge normative retenue au chapitre treize dépend entièrement de la réponse. Un accord de dix ans sur une architecture incontournable et un accord de trois ans sur une technologie contournable ne produisent pas la même entreprise. Le lecteur est invité à surveiller les dépôts trimestriels à venir : c'est là que l'information apparaîtra, si elle apparaît.</p>
<h3>La dépendance aux décisions de l'International Trade Commission</h3>
<p>Une part de la capacité de Vicor à négocier des licences repose sur les ordonnances d'exclusion obtenues devant l'<em>International Trade Commission</em> des États-Unis, qui interdisent l'importation de produits jugés contrefaisants. Ces décisions sont susceptibles de recours, de contournement technique et de révision. Leur remise en cause affaiblirait le levier de négociation sans qu'aucune ligne du compte de résultat ne l'annonce à l'avance.</p>
<h3>La concentration de la clientèle</h3>
<p>Le marché final de l'alimentation des accélérateurs est concentré sur un petit nombre d'acheteurs. Ce sont aussi les contreparties potentielles des accords de licence. La même entreprise peut donc être simultanément client, concurrent et adversaire judiciaire, configuration dont les comptes ne rendent pas compte et qui peut se dénouer brutalement.</p>
<h3>L'estimation du quatrième trimestre 2026</h3>
<p>Elle engage l'auteur seul et pèse trente pour cent du point de départ du modèle. Son incidence a été chiffrée au chapitre douze : environ trois dollars par action.</p>
<div class="hr-thin"></div>
<h3>Ce que cette étude n'a pas fait</h3>
<p>Elle n'a pas rencontré la direction de la société. Elle n'a pas consulté d'analyste couvrant la valeur. Elle ne s'appuie sur aucune donnée propriétaire. Elle repose exclusivement sur des documents publics, ce qui constitue à la fois sa limite et la condition de sa reproductibilité : chacun de ses chiffres peut être refait à partir des sources listées en page suivante.</p>
""")

# ======================================================== 27 · ANNEXE
rows=""
for y in d.YEARS:
    rp=d.ROP[y]/d.CA[y]*100
    rc=d.marge_courante(y)
    ro=d.roic(y)
    rows+=(f'<tr><td class="num">{y}</td><td class="num">{nb(d.CA[y])}</td>'
           f'<td class="num">{nb(d.marge_brute(y),1)}</td>'
           f'<td class="num">{nb(d.ROP[y])}</td>'
           f'<td class="num">{nb(d.rop_courant(y))}</td>'
           f'<td class="num">{nb(rc,1)}</td>'
           f'<td class="num">{nb(ro,1) if ro is not None else "—"}</td></tr>')
P('egg', head("Annexe","Les vingt et un exercices retraités")+f"""
<table class="plain" style="font-size:7.1pt;line-height:1.2">
<thead><tr><th>Exercice</th><th>Chiffre<br>d'affaires</th><th>Marge<br>brute, %</th>
<th>Résultat op.<br>publié</th><th>Résultat op.<br>courant</th><th>Marge op.<br>courante, %</th><th>Rentabilité du<br>capital, %</th></tr></thead>
<tbody>{rows}</tbody></table>
<p class="note" style="margin-top:3mm;font-size:7.2pt">Montants en milliers de dollars des États-Unis. La marge brute est rapportée au seul chiffre d'affaires, à l'exclusion des produits non récurrents. Le résultat opérationnel courant neutralise les éléments relevés au chapitre cinq. La rentabilité du capital employé rapporte le résultat opérationnel courant après impôt normatif de 21 % au capital employé moyen de l'exercice ; elle n'est pas calculable avant 2011, faute de capital employé d'ouverture.</p>
<div class="hr-thin"></div>
<div class="two">
<div><h3 style="margin-top:0;font-size:10pt">Moyennes de la période</h3>
<table class="plain" style="font-size:7.6pt"><tbody>
<tr><td>Croissance annuelle du chiffre d'affaires</td><td class="num"><b>4,2 %</b></td></tr>
<tr><td>Marge opérationnelle publiée</td><td class="num">2,8 %</td></tr>
<tr><td>Marge opérationnelle courante</td><td class="num"><b>3,5 %</b></td></tr>
<tr><td>Rentabilité du capital employé</td><td class="num"><b>4,6 %</b></td></tr>
<tr><td>Rotation du capital employé</td><td class="num">2,0x</td></tr>
</tbody></table></div>
<div><h3 style="margin-top:0;font-size:10pt">Repères de la série</h3>
<table class="plain" style="font-size:7.6pt"><tbody>
<tr><td>Meilleur exercice</td><td class="num">2021</td></tr>
<tr><td>Marge opérationnelle courante 2021</td><td class="num">15,5 %</td></tr>
<tr><td>Exercices déficitaires, résultat publié</td><td class="num">6 sur 21</td></tr>
<tr><td>Trésorerie nette au 31 décembre 2025</td><td class="num">395,4 M$</td></tr>
<tr><td>Dette financière</td><td class="num">néant</td></tr>
</tbody></table></div></div>
""")

# ======================================================== 28 · MÉTHODE ET SOURCES
srcs=[("Formulaire 10-K, exercice 2025","sec.gov · vicr-20251231.htm"),
("Formulaire 10-K, exercice 2024","sec.gov · vicr-20241231.htm"),
("Formulaire 10-K, exercice 2009 — données 2005 à 2008","sec.gov · b78711e10vk.htm"),
("Formulaire 10-K, exercice 2007 — litige Ericsson","sec.gov · b68148vce10vk.htm"),
("Formulaire 10-K, exercice 2012 — procédure contre les assureurs","sec.gov · d445003d10k.htm"),
("Données XBRL consolidées, identifiant 0000751978","data.sec.gov · companyfacts/CIK0000751978.json"),
("Résultats du deuxième trimestre 2026","vicorcorporation.gcs-web.com"),
("Concurrence sur l'alimentation des accélérateurs","semianalysis.com · energizing-ai-power-delivery-competition"),
("Comparables d'exploitation","stockanalysis.com")]
P('cream', head("Annexe","Note de méthode et sources")+f"""
<h3 style="margin-top:0">Construction des séries</h3>
<p>Les exercices 2009 à 2025 proviennent des balises XBRL déposées par la société. Les exercices 2005 à 2008 ont été saisis depuis les états consolidés de résultat des formulaires 10-K des exercices 2007 et 2009, la couverture XBRL ne remontant pas au-delà de 2009.</p>
<p>Chaque chiffre issu d'un tableau a été recoupé avec le texte qui le commente. Ce contrôle est la raison d'être du chapitre premier : c'est lui qui a mis au jour l'écart de quarante-cinq millions de dollars entre la donnée structurée et le texte des états financiers de l'exercice 2025.</p>
<h3>Retraitements</h3>
<p>Les éléments non récurrents ont été relevés par lecture du texte des états financiers, exercice par exercice, et non par un filtre automatique. Le relevé figure au chapitre cinq. Un élément logé en produits affecte la marge brute et la marge opérationnelle ; un élément logé en charges n'affecte que la seconde.</p>
<p>Le capital employé est défini comme les capitaux propres augmentés des dettes et diminués de la trésorerie. La rentabilité est calculée sur le capital employé moyen de l'exercice, ce qui interdit le calcul du premier exercice de la série.</p>
<h3>Réserve sur les cours de bourse</h3>
<p>Les cours de clôture de fin d'exercice utilisés pour les multiples historiques proviennent d'une source de marché non réglementaire. Ils n'engagent pas la même fiabilité que les données déposées et sont signalés comme tels partout où ils interviennent. Le cours de référence de 202,40 dollars relève de la même réserve.</p>
<h3>Reproductibilité</h3>
<p>Le classeur de retraitement accompagnant cette étude comporte six onglets et permet de refaire l'intégralité des calculs présentés, y compris la grille de sensibilité du chapitre quatorze.</p>
""")

# ======================================================== 30 · SOURCES
P('egg', head("Annexe","Sources")+f"""
<table class="plain" style="font-size:8pt"><tbody>
{"".join(f'<tr><td style="width:48%">{a}</td><td style="text-align:left;color:#6F7F86">{b}</td></tr>' for a,b in srcs)}
</tbody></table>
<p class="note" style="margin-top:6mm">Les formulaires 10-K de l'ensemble des exercices 2005 à 2025 sont accessibles depuis l'index des dépôts de la société, identifiant 0000751978, sur le site de la <em>Securities and Exchange Commission</em>. Les adresses complètes figurent dans le classeur de retraitement publié avec cette étude, ligne par ligne et exercice par exercice.</p>
<div class="hr-thin"></div>
<p class="note">Cette étude a été rédigée, calculée et composée par Guillaume Le Merour. Les graphiques ont été produits spécifiquement pour ce document à partir des séries retraitées ; aucun n'a été repris d'une source tierce.</p>
<p class="note" style="margin-top:3mm">Photographies : Unsplash, licence libre — Taylor Vick, İsmail Enes Ayhan, Matthieu Beaumont et autres auteurs. Toutes ont été retraitées en bichromie pour ce document. Emblème et identité visuelle : sousjacent.com.</p>
<div style="position:absolute;left:0;right:0;bottom:34mm;text-align:center"><div style="display:inline-block">{c.logo("sombre",40)}</div>
<div class="note" style="text-align:center;margin-top:6mm">Sous-jacent · Étude n° 1 · Vicor Corporation<br>Guillaume Le Merour · contact@sousjacent.com<br>sousjacent.com</div></div>
""")

# ======================================================== ASSEMBLAGE
html=f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vicor Corporation — Étude</title>
<style>{CSS}</style></head><body>{''.join(pages)}</body></html>"""
open('/home/claude/vicor/etude-vicor.html','w',encoding='utf-8').write(html)
print("pages:", len(pages), "octets:", len(html))
