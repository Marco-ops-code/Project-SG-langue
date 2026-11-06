# État du projet

Dernière mise à jour : 2026-11-06
Source : `main` (`ad878df`) + kit porté (PR #17) + revue du jour.

## Snapshot

| Clé | Valeur |
| --- | --- |
| Dépôt | `Marco-ops-code/Project-SG-langue` |
| Produit | **Non défini** — ne pas inventer |
| Stack | **Non défini** |
| Code applicatif | Aucun |
| Always-on | `AGENTS.md` seul (zéro `alwaysApply: true`) |
| Kit | Présent sur cette branche ; **absent de `main` depuis 18 jours calendaires** (cron du 30 sans PR) |
| PR kit déjà ouvertes | #1 (canonique), #2 (variante, `alwaysApply: true` — ne pas suivre), #3 (port 21), #4 (port 22), #5 (port 23), #6 (port 24), #7 (port 25), #8 (port 26), #9 (port 27 + revue), #10 (port 28 + revue), #11 (port 29 + revue), #12 (port 31 + revue), #13 (port 1er nov. + revue), #14 (port 2 nov. + revue), #15 (port 3 nov. + revue), #16 (port 4 nov. + revue), #17 (port 5 nov. + revue) |

## Arborescence utile

- `README.md` — titre d’origine conservé (`# Project-SG-langue`)
- `AGENTS.md` — seul contexte always-on
- `docs/strategie.md` — leviers (lire seulement pour le process)
- `docs/playbook.md` — méthode point par point
- `docs/questions-ouvertes.md` — à trancher **en un lot**
- `revue/` — dernier fichier seulement
- `scripts/validate-kit.py` — plafonds chiffrés

## Ce qu’il ne faut pas refaire

- Re-globber tout le dépôt alors que ce fichier existe.
- Générer une app langue / un stack par défaut.
- Réécrire la stratégie ou ouvrir une dix-huitième variante du kit.
- Activer `alwaysApply: true` (la PR #2 le faisait : double always-on).
- Fusionner plusieurs PR kit en parallèle (une seule suffit).
