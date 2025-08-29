# Archon + VS Code + GitHub Copilot — Starter Kit

Ce dépôt de départ applique le workflow **Architecture → Types → Tests → Implémentation → ADR** pour garder le contrôle quand on code avec l’IA.

## Contenu
- `PRD.md` — Cahier des charges (produit, utilisateurs, contraintes)
- `STRUCTURE.md` — Proposition d’arborescence et conventions
- `AGENTS.md` — Règles pour guider GitHub Copilot/Chat
- `TESTS_GUIDE.md` — Stratégie de tests (TDD/integ en priorité)
- `SECURITY_RULES.md` — Bonnes pratiques d’ENV et secrets
- `ADR/0001-record-template.md` — Modèle d’Architecture Decision Record
- `.vscode/` — Extensions recommandées et réglages basiques
- `.gitignore` — Python/Node/ENV

## Idée d’exercice (facultatif)
Construire une petite API **FastAPI** “Poèmes aléatoires” puis demander à **Archon** de proposer un agent d’amélioration (refactor + tests + lint + docs).

## Rappel des principes
1. **Architecturer** avant de coder
2. **Types d’abord**
3. **Tests d’abord** (intégration, puis unitaires)
4. **Implémenter** (agents en parallèle sur tâches indépendantes)
5. **Documenter en ADR** immédiatement
