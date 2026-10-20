# État du projet

Dernière mise à jour : 2026-10-20
Source : commit initial `ad878df` + analyse stratégie tokens (branche `cursor/strat-gie-gestion-tokens-454b`)

## Snapshot

| Clé | Valeur |
| --- | --- |
| Dépôt | `Marco-ops-code/Project-SG-langue` (public) |
| Produit | **Non défini** — ne pas inventer |
| Stack | **Non défini** |
| Code applicatif | Aucun |
| Fichiers gelés | Aucun (voir `docs/confirmations.yml`) |
| Questions ouvertes | `docs/questions-ouvertes.md` |

## Arborescence utile

- `README.md` — titre du dépôt uniquement (non gelé, non traité comme spec produit)
- `AGENTS.md` — contrat agent (toujours chargé, rester court)
- `.cursor/rules/tokens.mdc` — règles dures always-on
- `docs/strategie-tokens.md` — analyse et playbook (lire seulement pour le process)
- `docs/confirmations.yml` — décisions et fichiers confirmés
- `docs/questions-ouvertes.md` — à trancher **une seule fois**

## Ce qu’il ne faut pas refaire

- Re-globber tout le dépôt « pour voir ».
- Générer une app langue / un stack « par défaut ».
- Relancer une PR de stratégie si ces fichiers existent déjà et n’ont pas de delta.
