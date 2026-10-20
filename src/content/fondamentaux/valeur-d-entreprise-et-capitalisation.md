---
titre: "Capitalisation et valeur d'entreprise : combien coûte vraiment une société"
rubrique: "Valorisation"
chapo: "La capitalisation dit ce que valent les actions. La valeur d'entreprise dit ce que vaudrait l'activité, dette comprise. Le passage de l'une à l'autre, et la règle de cohérence qui évite de comparer ce qui n'est pas comparable."
date: 2026-10-21
brouillon: false
---

Deux notions se confondent souvent, et leur confusion produit des erreurs de multiples. La **capitalisation boursière** est le cours de l'action multiplié par le nombre d'actions : c'est la valeur de ce qui revient aux actionnaires. La **valeur d'entreprise** (VE, *enterprise value* en anglais) est la valeur de l'activité elle-même, quel que soit le mode de financement : c'est ce qu'il faudrait payer pour acheter l'ensemble, actionnaires et prêteurs compris.

## Le passage de l'une à l'autre

```
Valeur d'entreprise = capitalisation
                    + dette financière brute
                    − trésorerie et placements liquides
                    + intérêts minoritaires
                    (+ engagements assimilés à de la dette, selon la méthode)
                    − participations et actifs non opérationnels
```

La logique est celle d'un achat de maison : si l'on rachète une société, on devient propriétaire de ses actions, mais aussi débiteur de sa dette, et l'on récupère sa trésorerie. La VE est le prix net de l'opération.

## Un exemple chiffré

Capitalisation de 800, dette brute de 350, trésorerie de 150, intérêts minoritaires de 50 :

```
VE = 800 + 350 − 150 + 50 = 1 050
```

Avec un EBITDA de 150, la société se traite à **7,0 fois l'EBITDA** (1 050 ÷ 150). Si l'on avait rapporté la capitalisation seule à l'EBITDA, on aurait obtenu 5,3 fois, un chiffre qui flatte une société endettée sans tenir compte de ce qu'elle doit.

## Pourquoi il faut comparer VE avec VE

La règle de cohérence est simple : **le numérateur et le dénominateur d'un multiple doivent concerner les mêmes bailleurs de fonds.**

| Multiple | Numérateur | Dénominateur | Cohérent ? |
|---|---|---|---|
| VE / EBITDA, VE / résultat opérationnel | VE (actionnaires et prêteurs) | Résultat avant intérêts (revient aux deux) | Oui |
| Cours / bénéfice (PER) | Capitalisation (actionnaires) | Bénéfice net (revient aux actionnaires) | Oui |
| Capitalisation / EBITDA | Actionnaires | Résultat avant intérêts (les deux) | **Non** |

Comparer la capitalisation à un EBITDA, c'est rapprocher un prix qui ne revient qu'aux actionnaires d'un flux qui sert aussi les prêteurs. L'erreur pénalise injustement les sociétés peu endettées.

## Les pièges qui reviennent

- **La dette locative.** Depuis IFRS 16, les loyers de bail figurent au bilan comme une dette. Si la VE inclut la dette locative, l'EBITDA doit être l'EBITDA avant loyers ; si on les exclut des deux côtés, il faut un EBITDA après loyers. Mélanger les deux fausse le multiple, d'autant plus que la société loue beaucoup (voir la fiche sur la remise des loyers au bilan).
- **Les minoritaires.** Si l'on consolide à 100 % une filiale détenue à 70 %, la VE doit ajouter la part des autres actionnaires, sinon elle est sous-évaluée.
- **La trésorerie non disponible.** Une trésorerie immobilisée dans une filiale étrangère, ou nécessaire au fonctionnement, ne se retranche pas sans précaution.
- **Les titres dilutifs.** Les options et obligations convertibles augmentent le nombre d'actions à retenir.

## Ce qu'il faut en retenir

La VE est la bonne base pour comparer des sociétés qui n'ont pas la même structure financière, et c'est elle que l'on retrouve dans un modèle de flux actualisés : on actualise les flux d'exploitation pour obtenir la VE, puis on en retranche la dette nette pour retrouver la valeur des fonds propres, et on la divise par le nombre d'actions pour obtenir la valeur par action.
