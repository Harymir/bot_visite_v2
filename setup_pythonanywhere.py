#!/usr/bin/env python3

print("""
=== Guide de déploiement PythonAnywhere ===

1. Créez un compte sur www.pythonanywhere.com (gratuit)

2. Dans le tableau de bord PythonAnywhere:
   - Allez dans "Consoles" -> "Bash"
   - Exécutez les commandes suivantes:

   git clone https://github.com/Harymir/bot_visite_v2.git
   cd bot_visite_v2
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Configuration de l'application:
   - Allez dans l'onglet "Web"
   - Cliquez sur "Add a new web app"
   - Choisissez "Manual configuration"
   - Sélectionnez Python 3.9

4. Configuration du chemin WSGI:
   - Dans la section "Code" de votre web app
   - Cliquez sur le lien WSGI configuration file
   - Remplacez le contenu par:

   import os
   import sys
   path = '/home/VOTRE_USERNAME/bot_visite_v2'
   if path not in sys.path:
       sys.path.append(path)
   
   from pythonanywhere_config import application

5. Configuration des variables d'environnement:
   - Allez dans l'onglet "Web"
   - Cherchez la section "Environment variables"
   - Ajoutez:
     TELEGRAM_API_ID=votre_api_id
     TELEGRAM_API_HASH=votre_api_hash
     TELEGRAM_PHONE=votre_phone

6. Démarrer le Worker:
   - Allez dans "Consoles" -> "Bash"
   - Exécutez:
     cd bot_visite_v2
     source venv/bin/activate
     python bot_visite.py

Avantages de PythonAnywhere:
- Limite de requête de 15 minutes
- Sessions persistantes
- Console accessible en permanence
- Pas de redémarrage automatique
- Logs facilement accessibles
""")
