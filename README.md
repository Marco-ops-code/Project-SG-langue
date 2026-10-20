# Project-SG-langue

Kit de stratégie pour réduire les demandes, les corrections et les tokens.

## Démarrer

```bash
python3 scripts/validate-kit.py
```

## Carte

| Fichier | Rôle | Chargé quand |
| --- | --- | --- |
| `AGENTS.md` | Contrat agent (seul always-on) | Chaque message |
| `docs/strategie.md` | Analyse et leviers | À la demande |
| `docs/playbook.md` | Méthode point par point | À la demande |
| `templates/brief.md` | Brief fermé | Avant d’agir |
| `checklists/livraison.md` | Double revue | Avant commit |
| `revue/` | Journal des crons | Dernier fichier seulement |
| `.cursor/rules/*.mdc` | Brief, revue, kit | Description ou glob |

Règle : ne pas réécrire la stratégie chaque jour. Lire la dernière revue, mesurer, n’ajouter qu’un écart réel.
