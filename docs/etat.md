# État du projet

Dernière mise à jour : 2026-10-21
Source : `main` (`ad878df`) + kit porté (PR #1) + revue du jour.

## Snapshot

| Clé | Valeur |
| --- | --- |
| Dépôt | `Marco-ops-code/Project-SG-langue` |
| Produit | **Non défini** — ne pas inventer |
| Stack | **Non défini** |
| Code applicatif | Aucun |
| Always-on | `AGENTS.md` seul (zéro `alwaysApply: true`) |
| Kit | Présent sur cette branche ; absent de `main` tant que la PR n’est pas fusionnée |
| PR kit déjà ouvertes | #1 (canonique), #2 (variante, `alwaysApply: true` — ne pas suivre) |

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
- Réécrire la stratégie ou ouvrir une troisième variante du kit.
- Activer `alwaysApply: true` (la PR #2 le faisait : double always-on).
