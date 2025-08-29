# ADR 0002: Source de données — JSON statique vs Base de données

- **Date**: 2025-08-29
- **Statut**: accepté
- **Contexte**: Pour la version 1 (v1) de démonstration nous visons une livraison rapide, latence locale, et aucune écriture côté serveur (zéro persistance). Les exigences du PRD demandent un endpoint public GET /poemes/random qui renvoie des poèmes depuis une source locale. Nous devons choisir une solution simple et fiable pour les données.
- **Décision**: Utiliser un fichier JSON statique dans le dépôt (`data/poemes.json`) pour v1. Remigrer vers une base de données relationnelle ou NoSQL plus tard si la roadmap exige : persistance côté serveur, requêtes multi-critères, montée en charge horizontale, ou besoins transactionnels.
- **Conséquences**:
  - Positives:
    - Simplicité de mise en œuvre et de déploiement — pas d'infrastructure supplémentaire.
    - Temps de développement réduit — idéal pour une démo/POC.
    - Faible latence locale lorsqu'hébergé proche de l'exécution (lecture fichier en mémoire).
    - Facilité de versionnement des données (git) et reproductibilité.

  - Négatives / limitations:
    - Pas de support natif pour les écritures concurrentes ni pour la persistance côté serveur.
    - Requêtes multi-critères (recherche avancée, filtres complexes) seront inefficaces et nécessiteront chargement intégral en mémoire.
    - Pas de transactions, ni garanties ACID pour les opérations de mise à jour.
    - Scalabilité limitée si plusieurs instances doivent partager un état mutable.

  - Risques:
    - Si les données deviennent volumineuses, le chargement complet en mémoire peut impacter la mémoire et la latence.
    - Migration vers une DB demandera une étape de transformation et d'import des données.

- **Actions de suivi**:
  1. Documenter un schéma cible pour la base de données (tables/colonnes ou collections) afin de rendre la migration plus simple.
  2. Écrire un script de migration/ingestion qui transforme `data/poemes.json` en bulk-insert compatible avec la DB choisie.
  3. Ajouter des tests d'intégration pour vérifier l'équivalence des réponses entre la source JSON et la future source DB.
  4. Surveiller la taille du fichier JSON et les métriques d'utilisation : si latence ou mémoire pose problème -> prioriser migration.

- **Références**:
  - ADR 0001: template (structure de document)
  - PRD.md (exigences fonctionnelles pour l'API poèmes)
