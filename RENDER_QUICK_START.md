=== Guide de déploiement sur Render ===

1. Allez sur https://render.com
   - Créez un compte ou connectez-vous
   - Liez votre compte GitHub

2. Dans le dashboard Render:
   - Cliquez sur 'New +'
   - Sélectionnez 'Web Service'
   - Choisissez le repository 'bot_visite_v2'

3. Configurez le service:
   Nom: bot-visite-v2
   Environnement: Python 3
   Branch: main
   Build Command: pip install -r requirements.txt
   Start Command: python render_start.py

4. Variables d'environnement à configurer:
   TELEGRAM_API_ID=22214283
   TELEGRAM_API_HASH=d3ebb9a92636d8b111564fa4db2ab8da
   TELEGRAM_PHONE=+261333147872

5. Options avancées:
   - Instance Type: Free
   - Auto-Deploy: Yes
   - Health Check Path: /status

Le bot démarrera automatiquement après le déploiement.
Surveillez les logs dans l'interface Render pour vous assurer que tout fonctionne.

Pour vérifier le statut: https://bot-visite-v2.onrender.com/status
