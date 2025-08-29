# STRUCTURE — Proposition de base

```
.
├── src/
│   ├── app/               # FastAPI app (endpoints)
│   ├── domain/            # Types / modèles / logique pure
│   ├── services/          # Couche services (DB, vendors, etc.)
│   └── tests/             # Tests d’intégration + unitaires
├── ADR/
├── .vscode/
└── .gitignore
```

## Conventions
- **types d’abord** dans `src/domain/`
- **tests d’intégration** dans `src/tests/` (utiliser `pytest` et `httpx`)
- **.env.example** à la racine, **jamais** de secrets en clair
