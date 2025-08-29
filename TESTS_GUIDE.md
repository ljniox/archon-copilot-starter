# TESTS_GUIDE.md — Stratégie

## Priorité : intégration
- Utiliser `pytest` + `httpx` pour appeler les vrais endpoints FastAPI (en local), avec des **données réalistes**.

## Unitaire ensuite
- Ajouter des tests unitaires sur les fonctions pures (`src/domain`).

## TDD léger
1. Écrire le test qui échoue
2. Implémenter le minimum pour le faire passer
3. Refactorer si nécessaire (sans casser les tests)

## Exemples de dépendances
```
pip install fastapi uvicorn pytest httpx pydantic
```
