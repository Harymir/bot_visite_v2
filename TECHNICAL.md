# Documentation Technique

## Architecture du Bot

### Composants Principaux
1. **SiteVisitBot** : Classe principale
   - Gestion des sessions Telegram
   - Simulation des visites HTTP
   - Métriques de performance
   - Gestion automatique des erreurs

### Flux de Données


## Configuration

### Variables d'Environnement (.env)
- TELEGRAM_API_ID : ID de l'API Telegram
- TELEGRAM_API_HASH : Hash de l'API Telegram
- TELEGRAM_PHONE : Numéro de téléphone

### Système de Logs
- Niveau : INFO
- Format : timestamp - level - message
- Sortie : fichier (bot_visite.log) et console

## Fonctionnalités Techniques

### Simulation HTTP
- Rotation des User-Agents
- Gestion des sessions SSL
- Délais randomisés
- Métriques de performance

### Gestion des Erreurs
- Reconnexion automatique
- Gestion des timeouts
- Backoff exponentiel
- Détection des faux positifs

### Métriques
- Temps de réponse bot
- Temps de réponse HTTP
- Statistiques de performance
- État des connexions

## Maintenance

### Mises à Jour
1. Mettre à jour requirements.txt
2. Vérifier les logs d'erreur
3. Ajuster les paramètres de performance

### Dépannage
- Vérifier les logs
- Contrôler l'état de la session
- Monitorer les métriques
- Valider les credentials

## Sécurité
- Tokens stockés dans .env
- Session Telegram sécurisée
- HTTPS pour les requêtes
- Rotation des User-Agents
