# PRD — API Poèmes Aléatoires (Exercice guidé)

## 1. Contexte & objectif
Offrir une petite API de démonstration pour valider le workflow Archon + VS Code + Copilot.
Objectif: un endpoint public qui renvoie un poème aléatoire depuis un fichier JSON statique (~30 entrées).

## 2. Utilisateurs & parcours
- Dev interne ODS qui teste l’outillage IA.
- Parcours: appelle GET /poemes/random → reçoit { id, titre, auteur, contenu, tags }.

## 3. Portée (v1)
DOIT:
- Endpoint `GET /poemes/random` (100–300 ms local).
- Fichier `data/poemes.json` (≈30 poèmes).
- Tests d’intégration: statut 200 + schéma de réponse correct.
NE FAIT PAS:
- Authentification, base de données, écriture.

## 4. Contraintes
- Python 3.11, FastAPI, Pydantic.
- Pas de secrets en clair. `.env.example` uniquement.
- Qualité: tests d’intégration passent, code lisible et typé.

## 5. Risques & hypothèses
- Risque: “vibe coding” sans tests → on l’évite par TDD léger.
- Hypothèse: Copilot et/ou Archon aident à générer types/tests/implémentation.

## 6. Acceptation (DONE)
- Tests d’intégration verts.
- Endpoint stable et documenté (README bref).
- 1 ADR créé pour la décision “JSON statique vs DB”.
