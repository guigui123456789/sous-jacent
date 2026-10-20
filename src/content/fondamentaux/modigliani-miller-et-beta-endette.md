---
titre: "Modigliani-Miller et le bêta endetté : pourquoi s'endetter ne rend pas une entreprise moins chère"
rubrique: "Structure financière"
chapo: "Le théorème qui dit que la structure de financement ne crée pas de valeur dans un monde parfait, ce qui change dès qu'on introduit l'impôt, et la formule de Hamada pour passer d'un bêta endetté à un bêta d'activité."
date: 2026-10-21
brouillon: false
---

Une question revient sans cesse en finance d'entreprise : peut-on faire baisser le coût du capital en s'endettant davantage, puisque la dette coûte moins cher que les fonds propres ? Franco Modigliani et Merton Miller ont donné en 1958 une réponse qui structure encore tout le champ : **dans un monde sans frictions, non.**

## Proposition I : la valeur ne dépend pas du financement

Dans un marché parfait (sans impôt, sans coût de faillite, information identique pour tous), la valeur d'une entreprise ne dépend que de ses flux d'exploitation, pas de la manière dont ils sont répartis entre actionnaires et prêteurs. Le raisonnement est celui du découpage : une pizza ne change pas de taille parce qu'on la coupe en huit ou en douze parts. Un actionnaire peut d'ailleurs reproduire lui-même l'endettement de la société en empruntant à titre personnel, donc il ne paie pas pour que l'entreprise le fasse à sa place.

## Proposition II : le coût des fonds propres monte avec l'endettement

Si la valeur est inchangée, le coût moyen du capital l'est aussi. Or la dette est moins chère que les fonds propres. Pour que la moyenne reste la même, il faut que **le coût des fonds propres augmente avec l'endettement** :

```
coût des fonds propres = Ku + (Ku − Kd) × D/E
```

où Ku est le coût du capital d'une société sans dette, Kd le coût de la dette et D/E le ratio dette sur fonds propres.

**Exemple.** Ku = 8,5 %, Kd = 5 %, D/E = 0,5 :

```
Ke = 8,5 % + (8,5 % − 5 %) × 0,5 = 10,25 %
WACC = (1/1,5) × 10,25 % + (0,5/1,5) × 5 % = 6,83 % + 1,67 % = 8,5 %
```

Le coût moyen du capital reste à 8,5 % : la dette bon marché est exactement compensée par des actionnaires qui exigent plus, parce que leur risque a augmenté (ils passent après les prêteurs).

## Ce qui change avec l'impôt

Les intérêts de la dette sont déductibles du bénéfice imposable, ce qui crée une économie d'impôt, le **bouclier fiscal** (*tax shield*). Avec un taux d'impôt de 25 %, une dette à 5 % coûte 3,75 % après impôt. La valeur de l'entreprise endettée devient alors celle de l'entreprise sans dette, plus la valeur de ce bouclier. Dans notre exemple, le WACC tombe à environ 8,29 % au lieu de 8,5 %. L'endettement a un avantage fiscal réel.

## Ce qui l'empêche d'aller à l'extrême

Si l'impôt incite à s'endetter, rien n'indique qu'il faille s'endetter à 100 %. Deux coûts en sens contraire entrent en jeu :

- **Les coûts de faillite** : plus la dette est élevée, plus la probabilité de détresse augmente, avec des coûts directs (frais de procédure) et indirects (clients, fournisseurs et salariés qui fuient).
- **Les conflits d'agence** : un actionnaire d'une société très endettée a intérêt à prendre des risques excessifs, puisque le prêteur supporte une partie des pertes.

C'est la **théorie de l'arbitrage** (*trade-off*) : il existe un niveau d'endettement qui équilibre le bouclier fiscal et le risque de détresse. Il dépend du secteur : une société de logiciels, aux actifs immatériels, supporte mal la dette, une société foncière, aux actifs tangibles, s'en accommode.

## Le bêta d'une société endettée : la formule de Hamada

Dans la fiche sur le MEDAF, le bêta mesure le risque de marché supporté par l'actionnaire. Or ce risque a deux sources : le **risque de l'activité** et le **risque financier** apporté par la dette. On les sépare avec la formule de Hamada :

```
bêta endetté = bêta d'activité × [ 1 + (1 − taux d'impôt) × D/E ]
```

**Exemple.** Bêta d'activité de 1,0, impôt de 25 %, D/E = 0,5 :

```
bêta endetté = 1,0 × [ 1 + 0,75 × 0,5 ] = 1,375
Ke = 3 % + 1,375 × 5,5 % = 10,56 %
```

## À quoi sert cette séparation

L'usage principal est la **comparaison de sociétés de structures différentes**. Pour estimer le bêta d'une société non cotée, on prend ceux de sociétés cotées comparables, on les *désendette* (on retire l'effet de leur propre dette pour retrouver le bêta d'activité), on en fait la moyenne, puis on le *réendette* avec la structure cible de la société étudiée.

C'est la procédure standard d'un évaluateur, et elle illustre l'idée de Modigliani-Miller : **le risque de l'activité est une propriété de l'actif, le risque financier un choix de structure**.

## Les limites

La formule de Hamada suppose une dette sans risque et un bouclier fiscal certain, deux hypothèses fausses quand l'endettement est élevé. Les chiffres de coût de la dette, d'impôt marginal et de ratio cible sont des estimations. Une valorisation sérieuse indique la structure retenue et montre la sensibilité de la valeur à ce choix.
