# Playbook — travail point par point

Méthode obligatoire pour ce dépôt. Détail stratégique : `@docs/strategie.md`.

## Avant de coder

1. Lire `AGENTS.md` (déjà en contexte), `@docs/etat.md` s’il existe, et le **dernier** fichier de `revue/`.
2. Lancer `python3 scripts/validate-kit.py` si le kit ou les règles sont en jeu.
3. Cadrer la tâche sur `@templates/brief.md` (compléter en silence si l’humain a omis un champ non irréversible).
4. Lister 3 à 7 points d’exécution. Un point = un résultat vérifiable.

## Pendant

5. `grep` / `glob` d’abord ; `Read` seulement sur les extraits utiles.
6. Ne pas modifier le code déjà validé par l’humain.
7. Un changement = un objectif. Commit dès que le point est vrai.
8. Si un écart apparaît, le corriger tout de suite — ne pas empiler les dettes.

## Avant de livrer (deux passages)

9. Passage 1 : `@checklists/livraison.md` en entier.
10. Passage 2 : uniquement les items qui ont bougé ou qui étaient douteux.
11. Relancer le validateur. Les deux sorties doivent être identiques et vertes.
12. Push sur la branche de travail. Ouvrir la PR si le livrable le demande.

## Cron quotidien (Project M)

A. Lire la dernière revue, pas toute la stratégie.
B. Validateur. Si vert et aucun nouveau constat : écrire la revue du jour (« kit stable ») et s’arrêter.
C. Si rouge ou constat nouveau : une seule correction ciblée, commit, revue, push.
D. Si le kit existe déjà sur une PR ouverte mais pas sur `main` : le porter, écrire la revue, ne pas en inventer un troisième.
E. Interdit : régénérer le kit, dupliquer les docs, ouvrir une seconde stratégie parallèle.
