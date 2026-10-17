# -*- coding: utf-8 -*-
"""Méthode d'analyse Sous-jacent — document autonome, daté et versionné."""
import json, os
import charts as c
from style import CSS

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.environ.get('SORTIE_VICOR', ICI)
IMG = json.load(open(os.path.join(ICI, 'assets', 'images.json')))

VERSION = "1.0"
DATE = "17 octobre 2026"
PIED = f"Sous-jacent · Méthode d'analyse · version {VERSION} · {DATE}"

FIL = ('<div class="filigrane"><div class="bloc">'
       '<div class="mot">Sous-jacent</div><div class="url">sousjacent.com</div>'
       '</div></div>')

pages = []
def P(cls, inner, foot=True, filigrane=True):
    f = (f'<div class="foot"><span>{PIED}</span>'
         f'<span><b>sousjacent.com</b></span></div>') if foot else ''
    pages.append(f'<section class="page {cls}">{FIL if filigrane else ""}{inner}{f}</section>')

def head(eyebrow, titre):
    return f'<div class="eyebrow">{eyebrow}</div><div class="rule-v"></div><h2>{titre}</h2>'

# ---------------------------------------------------------------- couverture
P('navy', f"""
<div style="display:flex;flex-direction:column;height:100%;padding:30mm 24mm 18mm">
  <div style="flex:0 0 auto">{c.logo("clair", 42)}</div>
  <div style="flex:1 1 auto;display:flex;flex-direction:column;justify-content:center">
    <div class="eyebrow" style="margin-bottom:6mm">Document de référence</div>
    <h1 style="font-size:34pt;margin-bottom:5mm">Méthode d'analyse</h1>
    <p class="lead" style="font-size:12.6pt;max-width:118mm;color:#D6DEE6">
      Les règles selon lesquelles toute étude publiée sur sousjacent.com est construite :
      le choix des sociétés, la période retenue, les retraitements appliqués aux comptes,
      la définition du capital employé, le modèle de valorisation, la construction de la
      fourchette et les conditions de sa révision.
    </p>
    <hr class="hr-strong" style="margin:9mm 0 6mm;max-width:118mm">
    <div style="display:flex;gap:14mm;font-size:9.6pt;color:#B3C4D3">
      <div><div class="eyebrow" style="margin-bottom:2mm">Version</div>{VERSION}</div>
      <div><div class="eyebrow" style="margin-bottom:2mm">Arrêtée au</div>{DATE}</div>
      <div><div class="eyebrow" style="margin-bottom:2mm">Auteur</div>Guillaume Le Merour</div>
    </div>
  </div>
  <p class="small" style="flex:0 0 auto;color:#8FA2B2;max-width:118mm;font-size:8.4pt">
    Ce document est antérieur aux conclusions qu'il permet d'obtenir. Il est publié pour que
    chaque chiffre avancé dans une étude puisse être refait par son lecteur, et contesté sur
    sa règle plutôt que sur son résultat.
  </p>
</div>""", foot=False)

# ---------------------------------------------------------------- 1 principe
P('egg', head("Chapitre premier", "Le principe") + """
<p class="lead">Une étude de ce site n'est pas une opinion documentée. C'est une règle appliquée à des comptes publics, dont le résultat n'est connu qu'une fois le calcul fait.</p>
<p>L'ordre compte. La méthode est arrêtée avant le choix de la société ; le retraitement est appliqué avant que la valorisation ne soit construite ; la fourchette est le produit d'hypothèses déclarées, et non un chiffre vers lequel les hypothèses auraient été ajustées. Une analyse dont on connaît la conclusion avant d'avoir ouvert les comptes n'est pas une analyse.</p>
<h3>Trois engagements de fond</h3>
<p><b>Tout est reproductible.</b> Les sources sont exclusivement publiques — dépôts réglementaires, communiqués, transcriptions d'échanges avec les actionnaires. Aucune donnée propriétaire, aucune conversation avec la direction, aucun service payant. Les comptes retraités sont publiés en fichier téléchargeable à côté de chaque étude, de sorte que le lecteur puisse refaire le calcul et trouver autre chose.</p>
<p><b>L'incertitude est tranchée en faveur de la société.</b> Lorsqu'une hypothèse est indéterminée et qu'un intervalle de valeurs défendables existe, c'est la borne la plus favorable à l'entreprise étudiée qui est retenue, et ce choix est signalé. Une conclusion qui tient malgré les hypothèses les plus généreuses est plus solide qu'une conclusion obtenue en chargeant la barque.</p>
<p><b>Rien n'est corrigé en silence.</b> Toute révision d'une fourchette publiée est inscrite, datée et motivée sur la page de l'étude concernée. L'historique reste visible, y compris lorsqu'il donne tort à la version précédente.</p>
<div class="quote">Ce qu'une méthode interdit à son auteur vaut davantage que ce qu'elle lui permet.</div>
<h3>Ce que ce document n'est pas</h3>
<p>Il ne prétend ni à l'originalité ni à la supériorité technique. Les opérations décrites ici sont celles qu'enseigne n'importe quel cours sérieux d'analyse financière. Son intérêt est ailleurs : il fige des conventions, afin qu'une étude puisse être comparée à la suivante sans que l'on ait à se demander si la règle a bougé entre les deux.</p>
""")

# ---------------------------------------------------------------- 2 perimetre
P('cream', head("Chapitre deux", "Le choix des sociétés") + """
<p>Le périmètre est volontairement large : <b>sociétés cotées, France et États-Unis, toutes tailles</b>. Le choix de chaque étude est un choix personnel, assumé comme tel, et susceptible de changer. Aucun filtre sectoriel n'est posé a priori.</p>
<p>Quatre conditions pratiques doivent néanmoins être réunies pour qu'une société soit retenue.</p>
<table class="plain"><tbody>
<tr><td style="width:46mm"><b>Une série longue disponible</b></td><td>Vingt exercices au moins doivent être reconstituables à partir des dépôts réglementaires. Une société récemment introduite en bourse ne peut pas être traitée au gabarit de ce site.</td></tr>
<tr><td><b>Une couverture faible</b></td><td>Peu d'analystes, ou des avis très dispersés. Là où vingt analystes convergent, une étude de plus n'apporte rien ; là où cinq divergent du simple au double, le travail a une utilité.</td></tr>
<tr><td><b>Une question identifiable</b></td><td>Une anomalie précise dans les comptes ou dans le prix, formulable en une phrase avant de commencer. Sans elle, l'étude devient une description.</td></tr>
<tr><td><b>Aucun intérêt personnel</b></td><td>Aucune position n'est détenue sur les sociétés étudiées, ni avant, ni pendant, ni après la publication. Aucune rémunération n'est perçue d'un tiers à propos d'une société couverte.</td></tr>
</tbody></table>
<h3>La question centrale</h3>
<p>Chaque étude s'ouvre sur une question unique, écrite avant l'analyse et conservée telle quelle même lorsque la réponse déçoit. Elle porte sur un écart constaté : entre ce que montrent les comptes et ce que montre la présentation qu'en fait la société, ou entre ce que montrent les comptes et ce que paie le marché.</p>
<p>Cette question est publiée en tête de l'étude. Si le travail la contredit, c'est la contradiction qui est publiée.</p>
""")

# ---------------------------------------------------------------- 3 periode
P('egg', head("Chapitre trois", "La période et son homogénéité") + """
<p>La série longue est l'outil principal de ce site. Un exercice isolé se prête à toutes les lectures ; vingt exercices consécutifs, traités à l'identique, en autorisent beaucoup moins.</p>
<h3>Le point de départ</h3>
<p>La période retenue court sur <b>vingt et un exercices au moins</b>, et remonte aussi loin que les dépôts réglementaires permettent de reconstituer des comptes homogènes. Pour les sociétés européennes, 2005 constitue une borne naturelle : c'est l'exercice du passage obligatoire aux normes IFRS, en deçà duquel la série cesse d'être comparable à elle-même. Pour les sociétés américaines, qui publient en principes comptables américains, cette borne n'a pas la même portée ; la période est alors choisie sur la seule disponibilité des dépôts, et sa longueur est indiquée dans l'étude.</p>
<h3>Pourquoi vingt ans</h3>
<p>Un cycle d'investissement, une récession au moins, un changement de génération technologique. Une entreprise qui traverse cela sans jamais couvrir son coût du capital ne souffre pas d'un accident de parcours. Inversement, une rentabilité tenue sur vingt ans ne s'explique pas par la chance.</p>
<p>La longueur sert aussi à tester les hypothèses d'un modèle. Projeter une marge normative n'a de sens qu'en regard de ce que l'entreprise a réellement obtenu, et sur combien d'exercices. C'est l'objet du quatrième des repères décrits au chapitre huit.</p>
<h3>Ce qui est relevé, exercice par exercice</h3>
<p>Chiffre d'affaires, marge brute, résultat opérationnel publié, éléments non récurrents, capitaux propres, dettes financières, trésorerie, flux de trésorerie d'exploitation, investissements. Lorsqu'une donnée manque pour un exercice, elle est laissée vide plutôt qu'estimée, et le nombre d'exercices effectivement calculables est indiqué à côté de chaque moyenne.</p>
""")

# ---------------------------------------------------------------- 4 retraitements
P('cream', head("Chapitre quatre", "Les retraitements") + """
<p class="lead">Un compte de résultat publié mélange ce qui se reproduira et ce qui ne se reproduira pas. Le retraitement sépare les deux. Il ne corrige aucune erreur : il isole.</p>
<h3>Les éléments non récurrents</h3>
<p>Est traité comme non récurrent tout produit ou toute charge dont la nature exclut la répétition dans le cours normal de l'activité : règlements judiciaires, provisions pour litige, plus ou moins-values de cession d'actifs, charges de restructuration annoncées comme exceptionnelles, dépréciations d'écarts d'acquisition.</p>
<p>La règle appliquée est symétrique, et ce point est essentiel : <b>les produits non récurrents sont retirés au même titre que les charges</b>. Retirer les seules charges produirait une entreprise flatteuse qui n'existe pas. Le résultat obtenu est appelé <b>résultat opérationnel courant retraité</b> ; il est publié à côté du résultat publié, jamais à sa place.</p>
<p>Ces éléments sont relevés dans les annexes aux comptes, dans le rapport de gestion et, lorsque les données structurées déposées auprès du régulateur le permettent, dans le détail des balises elles-mêmes — c'est par ce moyen qu'a été établi, dans l'étude n° 1, qu'un règlement judiciaire avait été logé à l'intérieur du chiffre d'affaires.</p>
<h3>Le récurrent déguisé</h3>
<p>Une charge présentée comme exceptionnelle qui revient quatre exercices sur cinq n'est pas exceptionnelle. Lorsqu'un élément qualifié de non récurrent par la société apparaît de façon répétée dans la série, il est réintégré, et ce choix est motivé dans l'étude.</p>
<h3>Les loyers</h3>
<p>Lorsque la série traverse l'entrée en vigueur des normes qui ramènent les contrats de location au bilan, les exercices antérieurs sont retraités pour que la comparaison tienne : les loyers sont capitalisés et portés au capital employé. Sans ce retraitement, la rentabilité des exercices anciens est mécaniquement surévaluée par rapport aux récents.</p>
""")

# ---------------------------------------------------------------- 5 capital employe
P('egg', head("Chapitre cinq", "Le capital employé et sa rentabilité") + """
<p>C'est la définition la plus susceptible de varier d'un auteur à l'autre, donc celle qui doit être fixée le plus précisément. Celle-ci est la définition officielle du site. Tout classeur de calcul s'y aligne ; jamais l'inverse.</p>
<div class="quote">Capital employé = capitaux propres + dettes financières − trésorerie et équivalents.</div>
<p>Trois conventions l'accompagnent.</p>
<table class="plain"><tbody>
<tr><td style="width:46mm"><b>Moyenne de l'exercice</b></td><td>Le capital employé retenu est la moyenne du capital d'ouverture et du capital de clôture. Un résultat se construit sur l'année entière, et doit donc être rapporté au capital effectivement mobilisé pendant cette année. Cette convention a une conséquence pratique : le premier exercice de la série n'est pas calculable, faute de capital d'ouverture, et le nombre d'exercices effectivement calculables est toujours indiqué.</td></tr>
<tr><td><b>Impôt normatif</b></td><td>Le résultat opérationnel courant retraité est imposé à un taux normatif uniforme, indépendant des taux effectifs constatés, afin que la série ne soit pas déformée par des reports déficitaires ou des événements fiscaux ponctuels. Le taux retenu est indiqué dans chaque étude ; il s'est établi à 21 % pour l'étude n° 1, société américaine.</td></tr>
<tr><td><b>Décomposition</b></td><td>La rentabilité est systématiquement présentée comme le produit d'une marge et d'une rotation du capital. Deux entreprises de même rentabilité peuvent n'avoir rien en commun ; cette décomposition le montre.</td></tr>
</tbody></table>
<h3>La comparaison qui compte</h3>
<p>La rentabilité du capital employé n'a de sens que rapportée à son coût. Une entreprise qui obtient durablement moins que le coût de l'argent qu'elle mobilise détruit de la valeur, quelle que soit la progression de son chiffre d'affaires. Cet écart, en points, constitue le deuxième des quatre repères publiés dans chaque étude.</p>
""")

# ---------------------------------------------------------------- 6 modele
P('cream', head("Chapitre six", "Le modèle de valorisation") + """
<p>Le modèle est une actualisation des flux de trésorerie disponibles sur dix ans, prolongée par une valeur terminale. Il n'a rien d'original, et c'est voulu : un modèle connu se conteste sur ses hypothèses, pas sur sa mécanique.</p>
<h3>Le point de départ</h3>
<p>La projection part du <b>chiffre d'affaires de l'exercice en cours</b>, et non du dernier exercice clos, lorsque l'exercice en cours est largement connu. Les trimestres publiés sont repris tels quels ; les trimestres non publiés sont estimés, et la part estimée du total est <b>chiffrée explicitement</b> dans l'étude, avec son incidence sur la valeur par action.</p>
<p>Lorsque les indications données par la société sont mutuellement incompatibles — ce qui arrive — l'étude retient la lecture la plus favorable à l'entreprise, le dit, et publie la sensibilité de la valeur aux lectures alternatives.</p>
<h3>Les hypothèses déclarées</h3>
<p>Onze paramètres suffisent à définir le modèle : chiffre d'affaires de départ, trajectoire de croissance annuelle, chiffre d'affaires terminal, marge opérationnelle de départ, marge opérationnelle normative, taux d'imposition normatif, rotation du capital employé, coût moyen pondéré du capital, croissance à l'infini, trésorerie nette, nombre d'actions diluées. Ils sont publiés en tableau, sans exception.</p>
<p>La marge normative n'est jamais retenue sans être confrontée à l'histoire : l'étude indique combien de fois elle dépasse la moyenne effectivement réalisée sur la période, et si elle dépasse le meilleur exercice jamais obtenu.</p>
<h3>Le calculateur</h3>
<p>Chaque étude publie en ligne un calculateur reprenant le modèle, dans lequel les hypothèses principales se déplacent librement. Des repères y situent, sous chaque curseur, ce que l'entreprise a réellement fait. L'écart entre le curseur et le repère est l'analyse ; le reste n'est que de l'arithmétique.</p>
""")

# ---------------------------------------------------------------- 7 fourchette
P('egg', head("Chapitre sept", "La fourchette, et ce qu'elle n'est pas") + """
<p class="lead">Le site publie un chiffre. Il ne publie ni horizon, ni avis d'achat ou de vente, ni recommandation.</p>
<h3>Une fourchette de valeur n'est pas un objectif de cours</h3>
<p>Un objectif de cours est une prévision assortie d'un avis : il annonce où ira le prix, à quelle échéance, et ce qu'il convient d'en faire. Une fourchette de valeur intrinsèque est le résultat arithmétique d'hypothèses déclarées — on en change une, elle change. La première engage son auteur sur l'avenir du marché ; la seconde l'engage sur la cohérence de son calcul.</p>
<h3>Comment la fourchette est construite</h3>
<p>Une <b>valeur centrale</b> est affichée, issue des hypothèses retenues au chapitre six. Deux <b>bornes</b> l'encadrent, obtenues en faisant varier les deux hypothèses les plus déterminantes à l'intérieur d'un intervalle défendable. Chaque borne est rattachée au couple d'hypothèses qui la produit, et à la lecture du dossier que ce couple suppose, de sorte qu'un lecteur puisse savoir ce qu'il faudrait croire pour s'y tenir.</p>
<p>Une grille de sensibilité complète l'ensemble, montrant la valeur obtenue pour l'ensemble des combinaisons des deux mêmes hypothèses, bien au-delà des bornes publiées.</p>
<h3>Trois choses volontairement absentes</h3>
<p><b>Aucune probabilité n'est affectée aux bornes.</b> Les pondérer supposerait de savoir estimer la vraisemblance d'événements que personne ne sait estimer. Un chiffre indéfendable affaiblirait tous ceux qui l'entourent.</p>
<p><b>Aucun scénario haussier, central et baissier.</b> Une seule fourchette resserrée, avec sa grille. Le triptyque de scénarios sert trop souvent à n'avoir jamais tort.</p>
<p><b>Aucun horizon.</b> Le modèle dit ce que vaut une entreprise au regard d'hypothèses ; il ne dit pas quand le marché en conviendra, ni s'il en conviendra.</p>
""")

# ---------------------------------------------------------------- 8 reperes
P('cream', head("Chapitre huit", "Les quatre repères") + """
<p>Quatre mesures sont calculées de façon identique dans chaque étude et publiées au même endroit. Elles ne jugent pas la société : elles situent le dossier, et rendent une étude comparable à la suivante.</p>
<table class="plain"><thead><tr><th style="width:52mm">Repère</th><th>Définition exacte</th></tr></thead><tbody>
<tr><td><b>Part non reproductible du résultat opérationnel</b></td><td>Montant net des éléments non récurrents du dernier exercice, rapporté au résultat opérationnel publié de ce même exercice. Mesure ce que le dernier résultat doit à ce qui ne se reproduira pas.</td></tr>
<tr><td><b>Écart entre la rentabilité du capital employé et son coût</b></td><td>Moyenne de la rentabilité du capital employé retraitée sur les exercices calculables, moins le coût moyen pondéré du capital retenu dans l'étude. Exprimé en points.</td></tr>
<tr><td><b>Amplitude de la fourchette</b></td><td>Écart entre les deux bornes, rapporté à la valeur centrale, exprimé en pourcentage de part et d'autre. Une étude dont la fourchette est large doit dire quelle inconnue la cause.</td></tr>
<tr><td><b>Écart entre les hypothèses et l'histoire</b></td><td>Rapport entre chacune des trois hypothèses structurantes du modèle — marge normative, rotation du capital, trajectoire de croissance — et la valeur effectivement observée sur la période. Mesure de combien le modèle est lui-même une rupture.</td></tr>
</tbody></table>
<div class="quote">Un modèle qui suppose une entreprise différente de celle que montrent vingt ans de comptes peut avoir raison. Il doit au moins le dire.</div>
""")

# ---------------------------------------------------------------- 9 suivi
P('egg', head("Chapitre neuf", "Le suivi et les révisions") + """
<p class="lead">Une étude publiée n'est pas une étude close. Une analyse que son auteur ne revisite jamais est un exercice d'école.</p>
<h3>La revue trimestrielle</h3>
<p>Chaque société couverte est revue <b>après chacune de ses publications trimestrielles</b>. La revue donne lieu à une note courte qui ne refait pas l'étude : elle confronte le trimestre publié aux hypothèses qui tenaient la valorisation, et conclut sur l'une des trois issues suivantes — l'hypothèse tient, l'hypothèse est affaiblie, l'hypothèse est démentie.</p>
<h3>Le journal des révisions</h3>
<p>Toute modification d'une fourchette publiée est inscrite sur la page de l'étude, sous la forme d'une ligne datée portant la nouvelle fourchette et le fait qui l'a causée. Les lignes antérieures ne sont jamais retirées. Un lecteur arrivant deux ans après la publication initiale doit pouvoir lire la suite complète des positions successives, y compris celles qui se sont révélées fausses.</p>
<h3>La page des sociétés suivies</h3>
<p>Une page du site récapitule, pour chaque société couverte, la fourchette en vigueur, la date de sa dernière mise à jour et la date de la prochaine revue. Elle dit, à tout moment, ce que le site soutient et depuis quand.</p>
<h3>Correction des erreurs</h3>
<p>Une erreur de fait avérée est corrigée dès qu'elle est établie, et la correction est signalée au même endroit que la révision, avec sa date. Les erreurs trouvées par des lecteurs sont créditées lorsque ceux-ci y consentent.</p>
""")

# ---------------------------------------------------------------- 10 limites
P('cream', head("Chapitre dix", "Les limites, et le statut de ces publications") + """
<h3>Ce que la méthode ne peut pas faire</h3>
<p>Elle travaille sur des comptes, c'est-à-dire sur le passé mis en forme par l'entreprise elle-même. Elle ne voit ni la qualité réelle d'une équipe dirigeante, ni la valeur d'une technologie, ni l'état d'un carnet de commandes au-delà de ce qui en est publié. Elle ne rencontre pas les directions, ne consulte pas les analystes qui couvrent la valeur et n'utilise aucune donnée propriétaire — ce qui est à la fois sa limite et la condition de sa reproductibilité.</p>
<p>Elle n'est pas davantage un instrument de détection d'irrégularités comptables. Lorsqu'elle met en évidence un écart de présentation, elle décrit cet écart et sa conséquence chiffrée, sans lui prêter d'intention.</p>
<h3>Statut réglementaire</h3>
<p>Les contenus publiés sur sousjacent.com ont une vocation pédagogique. Ils ne constituent ni une recommandation d'investissement, ni une incitation à acheter ou vendre un instrument financier, et ne tiennent compte d'aucune situation patrimoniale particulière. Les fourchettes de valeur publiées sont le résultat d'hypothèses déclarées et modifiables : elles ne constituent ni un objectif de cours, ni une prévision, ni un avis d'achat ou de vente.</p>
<p>Aucune position n'est détenue sur les sociétés étudiées. Le site n'a aucune affiliation, ne perçoit aucune rémunération d'un tiers à propos d'une société couverte, et ne propose aucun contenu payant ni réservé.</p>
<h3>Versions de ce document</h3>
<table class="plain"><thead><tr><th style="width:26mm">Version</th><th style="width:34mm">Date</th><th>Modifications</th></tr></thead><tbody>
<tr><td><b>1.0</b></td><td>17 octobre 2026</td><td>Première version publiée. Consolide les règles appliquées à l'étude n° 1 et fixe la définition officielle du capital employé, la construction de la fourchette, les quatre repères et le dispositif de suivi.</td></tr>
</tbody></table>
<p class="small" style="margin-top:6mm">Toute étude indique la version de la méthode sous laquelle elle a été construite. Une modification de ce document ne rétroagit pas sur les études publiées : elle s'applique aux suivantes, et les écarts éventuels sont signalés.</p>
""")

html = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>Méthode d'analyse Sous-jacent — version {VERSION}</title>
<style>{CSS}</style></head><body>{''.join(pages)}</body></html>"""

out = os.path.join(SORTIE, 'methode-sous-jacent.html')
open(out, 'w', encoding='utf-8').write(html)
print(f"pages: {len(pages)} octets: {len(html)}")
