---
titre: "Le WACC : le prix de l'argent qui finance une entreprise"
rubrique: "Valorisation"
chapo: "Comment on assemble le coût des fonds propres et celui de la dette en un seul taux, pourquoi la dette semble moins chère qu'elle ne l'est, et ce que ce taux fait à une valorisation."
date: 2026-10-21
brouillon: false
---

Une entreprise se finance de deux manières : par ses actionnaires (fonds propres) et par ses prêteurs (dette). Chacun exige une rémunération. Le **coût moyen pondéré du capital** (*weighted average cost of capital*, WACC) est la moyenne de ces deux exigences, pondérée par le poids de chaque source. C'est le taux auquel on actualise les flux d'exploitation d'une société.

## La formule

```
WACC = E/V × coût des fonds propres + D/V × coût de la dette × (1 − taux d'impôt)
```

où *E* est la valeur de marché des fonds propres, *D* celle de la dette et *V* = E + D.

## Un exemple chiffré

Une société vaut 700 en fonds propres et doit 300. Ses actionnaires exigent 10 % (voir la fiche sur le MEDAF), ses prêteurs 5 %, et le taux d'impôt est de 25 % :

```
WACC = 0,70 × 10 % + 0,30 × 5 % × (1 − 0,25) = 7 % + 1,125 % = 8,125 %
```

## Trois points qui font souvent douter

**Pourquoi multiplier la dette par (1 − impôt) ?** Parce que les intérêts sont déductibles du bénéfice imposable : une dette à 5 % ne coûte réellement que 3,75 % après l'économie d'impôt. C'est l'avantage fiscal de la dette, et la raison pour laquelle le WACC baisse d'abord quand on s'endette.

**Pourquoi ne pas en profiter à fond ?** Parce que le coût des fonds propres monte avec l'endettement : l'actionnaire, passant après les prêteurs, supporte plus de risque et exige plus. Le coût de la dette monte aussi à mesure que le risque de défaut grandit. Au-delà d'un certain niveau, le WACC remonte.

**Valeur de marché ou valeur comptable ?** De marché. Le poids des fonds propres est la capitalisation boursière, non les capitaux propres du bilan, qui retracent l'histoire et non le prix actuel. C'est une source d'erreur fréquente.

## À quoi il sert, et ce qu'il compare

Le WACC est le taux plancher de rentabilité d'une entreprise : si ce qu'elle gagne sur le capital qu'elle emploie est inférieur, elle détruit de la valeur, même si elle affiche un bénéfice comptable. C'est exactement la comparaison faite dans la fiche sur le capital employé et le ROIC : un ROIC de 4,6 % face à un coût du capital de 10 % (le chiffre retenu dans l'étude Vicor) signifie un écart de 5,4 points en défaveur de l'entreprise.

C'est aussi le taux qui sert à actualiser les flux dans un modèle de flux de trésorerie. Un point de WACC de plus ou de moins déplace fortement la valeur finale, surtout quand l'essentiel de cette valeur est situé dans la valeur terminale.

## Les limites

- Le WACC mélange deux estimations incertaines (le coût des fonds propres et le coût de la dette), et hérite de l'incertitude de l'un et de l'autre.
- Il suppose une structure financière stable. Une société qui change de politique d'endettement change de WACC.
- Il est propre à un **risque** : on n'actualise pas avec le même taux les flux d'une activité stable et ceux d'une activité cyclique. Un taux unique pour toute une société peut être faux pour une de ses divisions.

La bonne pratique est de publier le WACC retenu avec les hypothèses qui le composent, et de montrer ce que devient la valeur autour de lui, plutôt que de la présenter comme un résultat unique.
