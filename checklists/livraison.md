# Checklist de livraison

Cocher dans l’ordre. Le second passage ne rejoue que les écarts.

## Périmètre

- [ ] L’objectif du brief est tenu, rien d’autre.
- [ ] Aucun fichier validé par l’humain n’a été modifié.
- [ ] Hors-périmètre respecté.

## Qualité de première passe

- [ ] Pas de question restée ouverte alors qu’une convention du kit tranchait.
- [ ] Pas de lecture entière là où un `grep` suffisait.
- [ ] Pas de duplication always-on (`AGENTS.md` recopié dans une règle).

## Preuves

- [ ] Validateur exécuté : `python3 scripts/validate-kit.py`
- [ ] Validateur relancé une deuxième fois, même résultat.
- [ ] Critères d’acceptation du brief cochés avec une preuve.

## Git

- [ ] Commits incrémentaux, messages factuels.
- [ ] Branche de travail uniquement.
- [ ] Push effectué. PR ouverte si le livrable le demande.
