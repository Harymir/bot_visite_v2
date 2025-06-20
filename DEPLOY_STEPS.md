#!/bin/bash

echo "=== Guide de déploiement Koyeb ===

1. Ouvrez https://app.koyeb.com dans votre navigateur

2. Connectez-vous ou créez un compte

3. Une fois connecté :
   - Cliquez sur \"Create App\"
   - Choisissez \"GitHub\" comme source de déploiement
   - Sélectionnez le repository \"bot_visite_v2\"

4. Configuration :
   - Name: bot-visite-v2
   - Region: Choisissez la plus proche
   - Instance Type: Free

5. Variables d environnement :
   TELEGRAM_API_ID=22214283
   TELEGRAM_API_HASH=d3ebb9a92636d8b111564fa4db2ab8da
   TELEGRAM_PHONE=+261333147872

6. Build Settings :
   - Builder: Docker
   - Dockerfile path: ./Dockerfile
   - Docker command: python koyeb_start.py

7. Cliquez sur \"Deploy\"

8. Une fois déployé :
   - Surveillez les logs dans l interface Koyeb
   - Vérifiez que le bot répond sur Telegram
   - Configurez les alertes si nécessaire

Pour plus d informations, consultez :
- KOYEB_DEPLOY.md
- TECHNICAL.md

=== Fin du guide ==="
