# SECURITY_RULES.md — Bonnes pratiques

- **Secrets** : jamais dans le repo. Utiliser `.env` local (non commité) et fournir un `.env.example`.
- **Branches** : feature branches + PR obligatoire sur `main`.
- **CI** : lint + tests + sécurité (ex. `pip-audit`).
- **Prod** : ne jamais appeler des services de prod depuis les tests ou l’IA.
