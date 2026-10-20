# Questions ouvertes

À trancher **en un seul lot**. Tant qu’une question bloquante n’est pas dans `docs/confirmations.yml`, aucun code produit.

## Produit

- [ ] Que signifie « SG-langue » (apprentissage, traduction, interne SG, autre) ?
- [ ] Qui sont les utilisateurs (élèves, formateurs, grand public, équipe interne) ?
- [ ] Quelle langue source / langue cible en v1 ?
- [ ] Quel canal (web, mobile, les deux) ?

## Technique

- [ ] Stack confirmé (framework, hébergement, auth, base) ?
- [ ] Contraintes (budget, RGPD, délai, hors-ligne) ?

## Process

- [ ] L’automation Cursor sur chaque `push` de `main` doit-elle rester active après merge de la stratégie ?
  - Recommandation : la désactiver ou la limiter aux changements de `AGENTS.md` / `docs/` — sinon chaque push relance un agent (gaspillage).

Réponses du propriétaire → copier dans `docs/confirmations.yml`, cocher ici, mettre à jour `docs/etat.md`.
