# Project-SG-langue — contrat agent

Kit pour réduire les demandes, les corrections et la consommation de tokens.

## Invariants

- Répondre en français.
- Ne pas modifier le code déjà validé par l’humain.
- Un seul `AGENTS.md` à la racine. Aucun `AGENTS.md` imbriqué.
- Aucune règle `.mdc` en `alwaysApply: true` (ce fichier suffit).
- Chercher (`grep` / `glob`) avant de lire un fichier entier.
- Ne pas relire un fichier déjà lu dans le même tour.
- Décider avec le brief et ce contrat. Ne pas poser de question si une convention du kit tranche.
- Livrer en une passe : appliquer `@checklists/livraison.md` avant le commit.
- Commit incrémental, push sur la branche de travail, ouvrir une PR si le livrable le demande.

## Lire seulement si besoin

- Stratégie : `@docs/strategie.md`
- Méthode : `@docs/playbook.md`
- Brief : `@templates/brief.md`
- Revue : dernier fichier de `revue/`
- Budget : `python3 scripts/validate-kit.py`

## Interdit

- Réécrire la stratégie depuis zéro. Itérer et mesurer.
- Dupliquer ces consignes dans un autre fichier toujours chargé.
