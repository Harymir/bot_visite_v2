# Déploiement sur Render

## Étapes de déploiement

1. Créez un compte sur [Render](https://render.com)

2. Connectez votre compte GitHub à Render

3. Cliquez sur 'New +' et sélectionnez 'Web Service'

4. Configurez le service :
   - Name: bot-visite-v2
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python koyeb_start.py`

5. Ajoutez les variables d'environnement :
   - TELEGRAM_API_ID=22214283
   - TELEGRAM_API_HASH=d3ebb9a92636d8b111564fa4db2ab8da
   - TELEGRAM_PHONE=+261333147872

6. Sélectionnez :
   - Instance Type: Free
   - Region: La plus proche de vous

7. Cliquez sur 'Create Web Service'

## Surveillance
- Les logs sont disponibles dans l'interface Render
- Le service redémarre automatiquement en cas d'erreur
- Les mises à jour sont automatiques depuis la branche main

## Notes
- Le service gratuit a une limite de 750 heures par mois
- Le bot s'arrête après 15 minutes d'inactivité sur le plan gratuit
- Utilisez une instance payante pour un fonctionnement 24/7
