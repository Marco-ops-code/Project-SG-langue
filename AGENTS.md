# Contrat agent — Project-SG-langue

Lire **en premier** `docs/etat.md` puis `docs/confirmations.yml`.
Ne pas explorer tout le dépôt si `docs/etat.md` existe.

## Règles dures

1. **Français.** Messages, commits, PRs, docs.
2. **Ne pas inventer** le produit, le stack, l’UI ou le contenu pédagogique.
3. **Ne pas modifier** un chemin listé dans `docs/confirmations.yml` sans demande explicite.
4. **Une tâche = un objectif.** Point par point. Pas de refonte collatérale.
5. **Vérifier deux fois** avant de déclarer terminé (relire le diff, relancer tests/lint s’ils existent, confirmer que les fichiers gelés n’ont pas bougé).
6. **Push** sur la branche de travail, puis PR. Jamais de force-push sur `main`.

## Budget tokens

- 1 glob ciblé max ; appels outils en parallèle.
- Ne pas relire un fichier déjà dans le contexte.
- Spec courte **avant** le code. Si une question ouverte bloque : l’ajouter à `docs/questions-ouvertes.md` et **s’arrêter** — ne pas coder autour.
- Docs always-on = ce fichier + la règle `.cursor/rules/tokens.mdc`. Le détail est dans `docs/strategie-tokens.md` (lire seulement si on change le process).
- Pas de sous-agents sur un dépôt aussi petit.

## Automation `push` sur `main`

Si `AGENTS.md` **et** `docs/strategie-tokens.md` existent déjà :

1. Lire `docs/etat.md` uniquement.
2. Si le commit ne change ni la stratégie ni une confirmation : **exit**. Pas de nouvelle PR, pas de réécriture.
3. Sinon : patch delta, un commit, push, PR unique.

## Définition de terminé

- Objectif de la tâche couvert, rien d’autre.
- Diff relu, fichiers gelés intacts.
- `docs/etat.md` mis à jour si la structure du dépôt a changé.
- Commit + push + PR.
