---
titre: "Actualiser : pourquoi un euro demain vaut moins qu'un euro aujourd'hui"
rubrique: "Valorisation"
chapo: "La valeur actuelle, la valeur actuelle nette et le taux de rendement interne : l'outil qui sous-tend toute valorisation, expliqué avec un seul projet chiffré."
date: 2026-10-21
brouillon: false
---

Toute valorisation, de l'entreprise cotée au projet industriel, repose sur la même opération : ramener à aujourd'hui des flux qui arriveront plus tard. Cette opération s'appelle l'**actualisation**.

## Pourquoi un euro demain vaut moins

Trois raisons se cumulent. On peut placer l'argent d'aujourd'hui et le faire fructifier (coût d'opportunité), l'inflation en réduit le pouvoir d'achat, et le flux futur n'est jamais certain (risque). Le taux d'actualisation résume les trois : c'est le rendement que l'on exige pour renoncer à l'argent aujourd'hui.

## La formule

```
Valeur actuelle = flux ÷ (1 + r)^t
```

où *r* est le taux d'actualisation et *t* le nombre d'années avant le flux. Avec r = 8 %, 100 € reçus dans cinq ans valent 100 ÷ 1,08⁵ = 68,06 € aujourd'hui. Inversement, 68,06 € placés à 8 % pendant cinq ans donnent 100 €.

## La valeur actuelle nette (VAN)

Pour décider d'un projet, on actualise tous ses flux et on en retranche l'investissement initial :

```
VAN = − investissement + somme des flux actualisés
```

**Exemple.** Un projet coûte 1 000 et rapporte 300 par an pendant cinq ans. À 8 %, la somme des cinq flux actualisés vaut 1 197,8. La VAN est donc de **+197,8** : le projet crée de la valeur au-delà de ce que le taux exigé réclamait. À 12 %, la somme tombe à 1 081,4 et la VAN à **+81,4** : le projet reste acceptable, mais avec une marge bien plus faible.

La règle est simple : une VAN positive crée de la valeur, une VAN négative en détruit, et la VAN d'une entreprise entière est exactement ce qu'on appelle sa valeur par la méthode des flux actualisés.

## Le taux de rendement interne (TRI)

Le TRI est le taux d'actualisation qui annule la VAN. Pour le même projet, il vaut environ **15,2 %** : à ce taux, les flux actualisés valent exactement 1 000. On peut alors comparer le TRI au taux exigé : 15,2 % contre 8 %, le projet passe largement.

Le TRI est intuitif, mais il a deux défauts connus :

- Il suppose que les flux intermédiaires sont réinvestis au TRI lui-même, ce qui est rarement réaliste pour un taux élevé.
- Si les flux changent plusieurs fois de signe (investissement, gain, puis coût de démantèlement), il peut y avoir plusieurs TRI, ou aucun.

Quand les deux critères divergent, la VAN fait autorité : elle se mesure en euros de valeur créée, pas en pourcentage.

## Ce que cela change pour lire une valorisation

Le taux fait varier le résultat de manière non linéaire : plus un flux est lointain, plus il est sensible au taux. Passer de 8 % à 12 % retire environ 30 % de la valeur actuelle d'un flux reçu dans dix ans, mais seulement 3,6 % de celle d'un flux reçu dans un an. C'est le mécanisme que mesure la duration, et la raison pour laquelle, dans une valorisation, la discussion sur le taux compte autant que celle sur les flux.

Une valorisation n'est donc jamais « un prix », mais un prix **conditionnel** : étant donné ces flux, et ce taux. C'est ce qui permet de la tester, et de la remettre en cause sur un point précis.
