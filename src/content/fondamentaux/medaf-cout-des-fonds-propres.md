---
titre: "Le MEDAF : combien rapporte le risque"
rubrique: "Risque et taux"
chapo: "Le modèle de base de la finance de marché : ce que l'on peut raisonnablement exiger d'une action, comment le calculer, et pourquoi chacune de ses trois pièces est discutable."
date: 2026-10-21
brouillon: false
---

Le modèle d'équilibre des actifs financiers (MEDAF, ou *capital asset pricing model*, CAPM en anglais) répond à une question simple : **quel rendement un investisseur est-il en droit d'attendre pour détenir une action plutôt qu'un placement sans risque ?** C'est la brique qui fournit le coût des fonds propres dans presque toutes les valorisations par actualisation.

## La formule

```
Rendement attendu = taux sans risque + bêta × prime de risque du marché
```

Chaque pièce a un sens précis :

| Pièce | Ce que c'est | Où la trouver |
|---|---|---|
| **Taux sans risque** | Ce que rapporte un placement sans défaut, en pratique un emprunt d'État de la même durée | Rendement de l'OAT ou du Treasury à dix ans |
| **Prime de risque du marché** | Le supplément de rendement qu'exigent les actions en moyenne par rapport au sans-risque | Études historiques, enquêtes, ordre de grandeur de 4 à 6 % |
| **Bêta** | La sensibilité du titre au marché : un bêta de 1,3 signifie que le titre bouge en moyenne 30 % plus que l'indice | Régression des rendements du titre sur ceux de l'indice |

Le bêta se calcule ainsi : covariance entre les rendements du titre et ceux du marché, divisée par la variance des rendements du marché. Le titre moyen a un bêta de 1.

## Un exemple chiffré

Taux sans risque de 3 %, prime de risque de 5,5 %, bêta de 1,3 :

```
3 % + 1,3 × 5,5 % = 10,15 %
```

Une société plus défensive, avec un bêta de 0,6, donnerait 3 % + 0,6 × 5,5 % = 6,3 %. L'écart de 3,85 points ne vient pas de la qualité de la société, mais de la manière dont son cours accompagne ou amortit les mouvements du marché.

## L'idée qui rend le modèle utile

Le MEDAF repose sur une distinction : le **risque propre** à une société (un litige, un produit raté) peut être éliminé en détenant beaucoup de titres, donc le marché ne le rémunère pas. Seul le **risque de marché**, celui qu'on ne peut pas diversifier, est payé. Le bêta ne mesure que celui-là.

C'est pourquoi une société très volatile mais dont les fluctuations ne dépendent pas du marché peut avoir un bêta faible, et inversement.

## Ce qui rend le modèle fragile

Il faut le dire avec la même netteté que la formule : le MEDAF est un modèle, pas une mesure.

- **Le bêta est instable.** Il change selon la période et l'indice retenus. Calculé sur deux ans ou sur cinq ans, sur un indice local ou mondial, le même titre peut donner 0,9 ou 1,4.
- **La prime de risque n'est pas observable.** Ce que l'on observe, ce sont des rendements passés, qui dépendent de la période choisie. Deux analystes sérieux retiennent 4,5 % et 6 %.
- **Le taux sans risque varie.** Avec un dix ans américain au-dessus de 5 % en octobre 2026, le même bêta et la même prime donnent un coût des fonds propres nettement plus élevé qu'avec un taux à 3 %.
- **Un seul facteur ne suffit pas.** Les modèles à plusieurs facteurs (taille, valeur, momentum) ont été créés parce que le bêta seul explique mal les écarts de rendement observés.

## Comment l'utiliser sans se tromper

Le bon usage est de ne pas lire le résultat comme une vérité, mais comme un **ordre de grandeur à tester**. Avec une société à 10,15 %, on regarde ce que donne la valorisation à 9 % et à 11 %. Si la conclusion change entre les deux, c'est que le coût des fonds propres compte plus que l'on ne le pensait, et c'est ce qu'il faut dire au lecteur.

Le coût des fonds propres n'est d'ailleurs qu'une moitié du coût du capital : l'autre moitié est la dette, et l'assemblage des deux est décrit dans la fiche sur le coût moyen pondéré du capital.
