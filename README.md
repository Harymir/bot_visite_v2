# Bot Visite v2

## Description
Un bot Telegram automatisé pour les visites de sites avec:
- Métriques de temps de réponse
- Monitoring des performances
- Gestion automatique des temps d'attente
- Simulation de visites HTTP sans navigateur

## Installation
1. Installer les dépendances:
   ```bash
   pip install -r requirements.txt
   ```

2. Configurer les variables d'environnement dans .env:
   - TELEGRAM_API_ID
   - TELEGRAM_API_HASH
   - TELEGRAM_PHONE

3. Lancer le bot:
   ```bash
   python bot_visite.py
   ```

## Fonctionnalités
- Simulation de visites HTTP
- Métriques de performance
- Gestion automatique des délais
- Reconnexion automatique
- Logs détaillés
