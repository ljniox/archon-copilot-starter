# AGENTS.md — Règles pour l’IA (Copilot/Chat)

> **Objectif** : garder le contrôle tout en accélérant.

## Directives générales
- Respecter le flux **Architecture → Types → Tests → Implémentation → ADR**.
- Préférer des **petits changements** fréquents, accompagnés de **tests**.
- Ne jamais écrire de secrets dans le code. Utiliser `os.environ` et `.env.example`.

## Prompts utiles (copier-coller dans Copilot Chat)
1. **Plan d’architecture**  
   « Lis `PRD.md` et propose un plan d’architecture minimal en listant les modules/fichiers à créer. Donne-moi `STRUCTURE.md` à jour. »

2. **Types d’abord**  
   « À partir du PRD, crée `src/domain/types.py` avec les dataclasses / Pydantic models nécessaires. N’ajoute pas de logique. »

3. **Tests d’intégration**  
   « Écris les tests d’intégration dans `src/tests/test_api.py` pour vérifier les endpoints principaux. Utilise `pytest` + `httpx`. »

4. **Implémentation guidée par tests**  
   « Implémente le minimum pour faire passer les tests existants, sans logique superflue. Complète ensuite par petits incréments. »

5. **ADR**  
   « Documente les décisions clés prises dans `ADR/` en créant un nouveau fichier basé sur `ADR/0001-record-template.md`. »
