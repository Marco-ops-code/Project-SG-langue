# Stratégie de gestion des tokens

Date d’analyse : 2026-10-20.
Dépôt : `Project-SG-langue` (1 fichier à l’audit, commit initial).
Automation : cron quotidien `Project M` (06:00 UTC).

Objectif : **moins de demandes, moins de corrections, moins de tokens**, sans perdre de qualité.

## 1. Diagnostic

Trois fuites se cumulent à chaque tour d’agent :

| Fuite | Mécanisme | Coût |
| --- | --- | --- |
| Demandes | Brief incomplet → questions → nouveaux tours | Préfixe (système + outils + historique) renvoyé à chaque tour |
| Corrections | Première passe hors critère → retravail | Relire, réécrire, re-vérifier le même périmètre |
| Contexte mort | Règles always-on longues, `AGENTS.md` imbriqués, lectures entières | Payé sur **tous** les tours, même inutiles |

Sur ce dépôt, le risque n°1 n’était pas le code applicatif : il n’y en avait pas. Le risque était qu’un cron quotidien **ré-explore et réécrive** la même stratégie chaque matin.

## 2. Leviers, par ordre d’impact

1. **Brief unique et fermé** — une demande = un objectif, un hors-périmètre, un critère d’acceptation. Supprime la majorité des tours de clarification.
2. **Contexte always-on minimal** — un seul `AGENTS.md` court, **zéro** règle `alwaysApply: true`. Les `.mdc` se chargent par description ou par glob.
3. **Découverte ciblée** — `grep` / `glob` avant `Read`. Pas de relecture du même fichier dans le même tour.
4. **Première passe juste** — checklist de livraison, puis re-contrôle des écarts seulement. Une correction doit coûter moins de 20 % de la tâche d’origine.
5. **Mémoire inter-runs** — `revue/AAAA-MM-JJ.md` + validateur. Le cron lit la dernière revue, ne relance pas l’analyse complète.

## 3. Budgets

| Surface | Plafond | Pourquoi |
| --- | --- | --- |
| `AGENTS.md` | 40 lignes / 500 mots | Chargé à chaque message |
| Règles `alwaysApply: true` | 0 fichier | Évite le double always-on |
| Contexte always-on estimé | 800 tokens (`chars/4`) | Garde de dérive |
| Tours d’une tâche simple | 1 à 3 | Au-delà = brief trop flou |
| Tours d’une tâche moyenne | 5 à 10 | Au-delà = découper |
| Correction | ≤ 20 % des tokens de la tâche | Sinon le critère d’acceptation manquait |

Source chiffrée : `scripts/validate-kit.py`.

## 4. Anti-patterns

- Plusieurs `.mdc` en `alwaysApply: true` (3 000+ tokens de préfixe par tour).
- `AGENTS.md` imbriqués : Cursor les charge tous.
- Recopier un document dans une règle au lieu de le pointer (`@fichier`).
- Relire tout le dépôt « pour être sûr ».
- Demander confirmation alors qu’une convention du kit tranche.
- Réécrire `docs/strategie.md` à chaque cron sans nouveau constat.
- Toucher un fichier déjà validé par l’humain.

## 5. Mesure

Chaque run quotidien :

1. Exécute le validateur (vert / rouge, tokens always-on).
2. Compte les fichiers de revue et note s’il y a eu correction.
3. N’ajoute **qu’une** amélioration si un plafond est dépassé ou si un gaspillage réel est observé.

Pas de tableau fantôme : tant qu’il n’y a pas d’usage produit, la métrique utile est le **budget always-on** et le **nombre de réécritures évitées**.
