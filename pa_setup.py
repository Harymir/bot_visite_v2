#!/usr/bin/env python3

import os
import sys
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from dotenv import load_dotenv

async def setup_telegram():
    """Configure la session Telegram pour PythonAnywhere."""
    try:
        load_dotenv()
        api_id = os.getenv("TELEGRAM_API_ID")
        api_hash = os.getenv("TELEGRAM_API_HASH")
        phone = os.getenv("TELEGRAM_PHONE")

        print("\n=== Configuration Telegram sur PythonAnywhere ===")
        
        # Créer le client
        client = TelegramClient('pa_session', api_id, api_hash)
        await client.connect()

        if not await client.is_user_authorized():
            print("\nSession non autorisée. Démarrage de l'authentification...")
            sent_code = await client.send_code_request(phone)
            
            code = input("\nEntrez le code Telegram reçu: ")
            try:
                await client.sign_in(phone, code)
            except SessionPasswordNeededError:
                password = input("Entrez le mot de passe 2FA: ")
                await client.sign_in(password=password)

        print("\n✓ Session Telegram configurée!")
        await client.disconnect()
        
        # Créer le script de démarrage
        with open('start_bot.sh', 'w') as f:
            f.write('''#!/bin/bash
            source ~/bot_visite_v2/venv/bin/activate
            cd ~/bot_visite_v2
            python worker_config.py &
            ''')
        
        os.chmod('start_bot.sh', 0o755)
        
        # Créer la tâche programmée
        with open('schedule_task.txt', 'w') as f:
            f.write('''
            Pour configurer la tâche programmée sur PythonAnywhere:

            1. Allez dans l'onglet "Tasks"
            2. Ajoutez une nouvelle tâche:
               - Commande: bash ~/bot_visite_v2/start_bot.sh
               - Heure: Daily à 00:00
            
            Cela garantira que le bot redémarre chaque jour.
            ''')

        print("""
        \n=== Configuration terminée ! ===

        1. La session Telegram est configurée
        2. Le script de démarrage est créé (start_bot.sh)
        3. Instructions pour la tâche programmée dans schedule_task.txt

        Pour démarrer le bot:
        $ bash start_bot.sh

        Pour vérifier les logs:
        $ tail -f bot.log

        Le bot redémarrera automatiquement toutes les 15 minutes
        pour respecter les limites de PythonAnywhere.
        """)

    except Exception as e:
        print(f"Erreur lors de la configuration: {e}")

if __name__ == "__main__":
    asyncio.run(setup_telegram())
