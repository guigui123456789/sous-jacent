---
titre: "VaR et expected shortfall : mesurer la perte que l'on ne veut pas dépasser"
rubrique: "Portefeuille et risque"
chapo: "La valeur à risque dit la perte qu'on ne devrait dépasser qu'une fois sur cent. L'expected shortfall dit ce que l'on perd quand on la dépasse. Un calcul chiffré, et les raisons pour lesquelles la première a été largement critiquée."
date: 2026-10-21
brouillon: false
---

La volatilité résume le risque en un seul chiffre, mais elle ne répond pas à la question que se pose un gestionnaire ou un régulateur : **combien puis-je perdre, au pire, sur un horizon donné ?** La valeur à risque (*value at risk*, VaR) y répond avec une convention : une perte maximale à un niveau de confiance fixé.

## La définition

Une VaR à 99 % sur un jour de 28 000 € se lit ainsi : *il y a 99 chances sur 100 que la perte de demain ne dépasse pas 28 000 €.* Autrement dit, la perte devrait dépasser ce montant un jour de bourse sur cent, soit environ deux à trois fois par an.

Trois paramètres la définissent toujours : le **niveau de confiance** (95 %, 99 %), l'**horizon** (un jour, dix jours) et la **méthode de calcul**.

## La VaR paramétrique

On suppose que les rendements suivent une loi normale. La VaR est alors la volatilité multipliée par un coefficient lié au niveau de confiance :

```
VaR = valeur du portefeuille × volatilité × z
```

avec z = 1,645 à 95 % et z = 2,326 à 99 %.

**Exemple.** Un portefeuille de 1 000 000 €, avec une volatilité quotidienne de 1,2 % :

```
VaR 99 % sur 1 jour  = 1 000 000 × 1,2 % × 2,326 = 27 916 €
VaR 95 % sur 1 jour  = 1 000 000 × 1,2 % × 1,645 = 19 738 €
VaR 99 % sur 10 jours = 27 916 × √10 = 88 279 €
```

Le passage à dix jours se fait par la **racine du temps** : si les rendements quotidiens sont indépendants, la variance s'additionne, donc la volatilité croît avec √T et non avec T.

## Les deux autres méthodes

- **La simulation historique** : on rejoue les variations passées (par exemple les 500 derniers jours) sur le portefeuille actuel, et l'on prend la perte au 1er centile. Elle ne suppose aucune loi, mais ne connaît que ce qui s'est déjà produit.
- **La simulation de Monte-Carlo** : on tire des milliers de scénarios selon un modèle, en général plus riche que la loi normale, puis on lit le centile. Elle est flexible, mais dépend du modèle choisi.

## Le défaut fondamental de la VaR

La VaR dit **où commence la queue de la distribution, pas ce qu'il y a dedans.** Une VaR à 99 % de 28 000 € est compatible avec une perte de 29 000 € comme avec une perte de 900 000 € les jours où elle est dépassée. Elle ne distingue pas les deux cas.

Elle a aussi un défaut théorique : elle n'est pas **sous-additive**. La VaR de deux portefeuilles réunis peut dépasser la somme de leurs VaR, ce qui contredit l'idée que la diversification réduit le risque. Une mesure raisonnable ne devrait pas avoir cette propriété.

## L'expected shortfall

L'*expected shortfall* (ES, ou CVaR) corrige le premier défaut : c'est **la perte moyenne les jours où la VaR est dépassée.** Sous la loi normale :

```
ES = valeur × volatilité × φ(z) ÷ (1 − confiance)
```

où φ est la densité de la loi normale.

Pour le même portefeuille, à 99 % : ES = 1 000 000 × 1,2 % × 2,665 = **31 983 €**, soit environ 15 % de plus que la VaR. À 95 %, ES = 24 753 € contre une VaR de 19 738 €. L'ES est toujours plus grande que la VaR, et elle est sous-additive : c'est pour cette raison que la réglementation bancaire (le *Fundamental Review of the Trading Book*) l'a retenue à 97,5 % à la place de la VaR à 99 % pour le calcul des fonds propres de marché.

## Les limites communes

- **La loi normale sous-estime les queues.** Les krachs sont bien plus fréquents qu'elle ne le prédit. Une VaR paramétrique à 99 % est donc trop optimiste justement quand elle importe.
- **L'historique est une fenêtre.** Une VaR historique calculée après une période calme est basse, et elle double au moment où la crise commence, c'est-à-dire trop tard : elle est *procyclique*.
- **Elle suppose que les positions peuvent être liquidées.** Un horizon de dix jours ne vaut que si l'on peut vendre sans déplacer le prix.
- **Elle ne remplace pas les scénarios de crise.** Les régulateurs exigent des *stress tests* en complément : on y simule des chocs précis (une hausse de taux de 200 points de base, un krach de 30 %), sans leur attribuer de probabilité.

## Ce qu'il faut en retenir

Une VaR est un **seuil**, pas un plafond. Elle sert à comparer et à fixer des limites au quotidien, mais elle ne doit jamais être lue comme « le pire qui puisse arriver ». La question utile est toujours double : quel est le seuil, et que se passe-t-il au-delà ?
