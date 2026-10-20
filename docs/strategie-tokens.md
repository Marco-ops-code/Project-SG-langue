# Stratégie de gestion des tokens

Analyse du 2026-10-20. Dépôt observé : 1 fichier (`README.md`), 0 spec produit, 0 issue, 0 PR, 2 agents cloud lancés en parallèle sur le même push `main`.

Objectif : **moins de demandes, moins de corrections**, donc moins de tokens — sans ralentir le vrai travail.

## Diagnostic

Les tokens se perdent surtout **entre deux tours** (re-découverte, inventions, rollbacks), pas dans une ligne de code.

| Rang | Foyer de gaspillage | Pourquoi ça coûte | Contre-mesure |
| --- | --- | --- | --- |
| 1 | Invention du produit | Une app « langue » générée sans spec → 3 à 10 cycles de correction | Stop si question ouverte bloquante |
| 2 | Re-exploration | Chaque agent glob `**` sur un dépôt déjà décrit | `docs/etat.md` lu en premier |
| 3 | Automation trop large | Chaque push `main` relance un agent ; 2 runs déjà en parallèle | Exit immédiat si stratégie déjà en place |
| 4 | Contexte always-on trop long | AGENTS.md / rules verbeux = tokens **à chaque** tour | Contrat court + détail on-demand |
| 5 | Toucher du code confirmé | Rollback + relitige | `docs/confirmations.yml` |
| 6 | Questions au compte-gouttes | 1 question × N tours | Lot unique dans `docs/questions-ouvertes.md` |

Ordre de grandeur (run type agent cloud, contexte ~100k) :

- Always-on utile : ~1–2 % du contexte (ce contrat).
- Always-on bavard : 10–20 % **à chaque** message.
- Une correction de refonte UI/produit : souvent **plus cher** que l’implémentation initiale.
- Deux agents sur le même push : **×2** pour le même livrable.

## Cible

```
avant : explorer → inventer → corriger → ré-explorer
après : état → spec/lot de questions → patch → double check → push
```

Le propriétaire tranche le produit **une fois**. Les agents n’arbitrent plus.

## Playbook (point par point)

1. Lire `docs/etat.md` + `docs/confirmations.yml`.
2. Si tâche produit et case ouverte bloquante → mettre à jour `docs/questions-ouvertes.md`, s’arrêter.
3. Spec en 5–10 lignes dans le message de PR (objectif, hors-scope, fichiers).
4. Un objectif, un diff. Pas de « tant qu’on y est ».
5. Vérification 1 : relire le diff. Vérification 2 : tests/lint + fichiers gelés intacts.
6. Commit descriptif, push branche, PR. Mettre à jour `docs/etat.md` si l’arbre a changé.

## Ce que cette PR installe (et seulement ça)

- Contrat agent court (`AGENTS.md`) + règle always-on minimale.
- Snapshot pour ne plus re-cartographier le vide.
- Registre des confirmations / interdits.
- Lot de questions produit, sans réponses inventées.
- Template PR pour forcer objectif + hors-scope.

`README.md` n’est **pas** modifié (fichier existant, pas une spec, mais on ne le réécrit pas « au cas où »).

## Recommandation propriétaire (hors dépôt)

L’automation déclenchée sur **tout** `push` de `main` est le plus gros levier restant. Après merge de cette stratégie : la restreindre (chemins `AGENTS.md`/`docs/**`) ou la passer en manuel. Sinon chaque feature merge relance une analyse déjà faite.
