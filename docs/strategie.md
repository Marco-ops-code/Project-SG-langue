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

## 6. Addendum 2026-10-21

Constat nouveau (le kit 2026-10-20 n’était pas sur `main`) :

| Fuite observée | Preuve | Correction de ce run |
| --- | --- | --- |
| Kit seulement en PR brouillon | `main` = `README.md` seul ; cron du 21 redémarre à vide | Porter le kit, ne pas le régénérer |
| Deux stratégies parallèles | PR #1 (kit validé) et PR #2 (`alwaysApply: true`) | Une source : le kit #1. PR #2 = variante, pas un second contrat |
| Re-exploration du dépôt vide | Chaque cron sans `docs/etat.md` refait le glob | Snapshot `@docs/etat.md` |
| Invention produit | Aucune spec ; risque d’app « langue » | Lot unique `@docs/questions-ouvertes.md`, puis stop |

Levier propriétaire restant (hors dépôt) : fusionner **une** PR de kit, puis restreindre l’automation aux chemins `AGENTS.md` / `docs/` / `revue/` — sinon chaque merge `main` relance un agent.

## 7. Addendum 2026-10-22

Constat nouveau (récurrence, pas une nouvelle stratégie) :

| Fuite observée | Preuve | Correction de ce run |
| --- | --- | --- |
| Kit toujours hors de `main` au 3e cron | `main` = `README.md` ; PR #1, #2, #3 encore brouillon | Porter le kit #3, ne pas en inventer un quatrième |
| Le port quotidien est devenu la fuite | Chaque cron repart d’un dépôt vide et rouvre une PR | Revue « kit stable » ; aucune réécriture du contrat |

Levier propriétaire inchangé et plus urgent : fusionner **une** PR (#3 ou #1), fermer la #2, restreindre le cron. Sans ça, le 23 octobre reproduira le même port.

## 8. Addendum 2026-10-23

Constat nouveau (la prédiction du 22 s’est réalisée ; pas une nouvelle stratégie) :

| Fuite observée | Preuve | Correction de ce run |
| --- | --- | --- |
| Kit toujours hors de `main` au 4e cron | `main` = `README.md` ; PR #1 à #4 encore brouillon | Porter le kit #4, ne pas en inventer un cinquième |
| Le port quotidien reste la fuite | Quatre crons, quatre PR, même contrat 302 tokens | Revue « kit stable » ; contrat `AGENTS.md` inchangé |

Levier propriétaire unique désormais : fusionner **une** PR (#4, #3 ou #1), fermer la #2, restreindre le cron. Un 5e port n’ajoutera aucun levier.

## 9. Addendum 2026-10-24

Constat nouveau (la prédiction du 23 s’est réalisée ; pas une nouvelle stratégie) :

| Fuite observée | Preuve | Correction de ce run |
| --- | --- | --- |
| Kit toujours hors de `main` au 5e cron | `main` = `README.md` ; PR #1 à #5 encore brouillon | Porter le kit #5, ne pas en inventer un sixième |
| Le port quotidien reste la fuite | Cinq crons, cinq PR, même contrat 302 tokens | Revue « kit stable » ; contrat `AGENTS.md` inchangé |

Levier propriétaire unique désormais : fusionner **une** PR (#5, #4, #3 ou #1), fermer la #2, restreindre le cron. Un 6e port n’ajoutera aucun levier.

## 10. Addendum 2026-10-25

Constat nouveau (la prédiction du 24 s’est réalisée ; pas une nouvelle stratégie) :

| Fuite observée | Preuve | Correction de ce run |
| --- | --- | --- |
| Kit toujours hors de `main` au 6e cron | `main` = `README.md` ; PR #1 à #6 encore brouillon | Porter le kit #6, ne pas en inventer un septième |
| Le port quotidien reste la fuite | Six crons, six PR, même contrat 302 tokens | Revue « kit stable » ; contrat `AGENTS.md` inchangé |

Levier propriétaire unique désormais : fusionner **une** PR (#6, #5, #4, #3 ou #1), fermer la #2, restreindre le cron. Un 7e port n’ajoutera aucun levier.

## 11. Addendum 2026-10-26

Constat nouveau (la prédiction du 25 s’est réalisée ; pas une nouvelle stratégie) :

| Fuite observée | Preuve | Correction de ce run |
| --- | --- | --- |
| Kit toujours hors de `main` au 7e cron | `main` = `README.md` ; PR #1 à #7 encore brouillon | Porter le kit #7, ne pas en inventer un huitième |
| Le port quotidien reste la fuite | Sept crons, sept PR, même contrat 302 tokens | Revue « kit stable » ; contrat `AGENTS.md` inchangé |

Levier propriétaire unique désormais : fusionner **une** PR (#7, #6, #5, #4, #3 ou #1), fermer la #2, restreindre le cron. Un 8e port n’ajoutera aucun levier.
