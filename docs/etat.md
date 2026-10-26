# État du projet

Dernière mise à jour : 2026-10-25
Source : `main` (`ad878df`) + kit porté (PR #6) + revue du jour.

## Snapshot

| Clé | Valeur |
| --- | --- |
| Dépôt | `Marco-ops-code/Project-SG-langue` |
| Produit | **Non défini** — ne pas inventer |
| Stack | **Non défini** |
| Code applicatif | Aucun |
| Always-on | `AGENTS.md` seul (zéro `alwaysApply: true`) |
| Kit | Présent sur cette branche ; **absent de `main` depuis 6 crons** |
| PR kit déjà ouvertes | #1 (canonique), #2 (variante, `alwaysApply: true` — ne pas suivre), #3 (port 21), #4 (port 22), #5 (port 23), #6 (port 24 + revue) |

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
- Réécrire la stratégie ou ouvrir une septième variante du kit.
- Activer `alwaysApply: true` (la PR #2 le faisait : double always-on).
- Fusionner plusieurs PR kit en parallèle (une seule suffit).
