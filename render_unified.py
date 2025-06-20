#!/usr/bin/env python3

import os
import sys
import logging
import asyncio
from threading import Thread
from flask import Flask
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from bot_visite import SiteVisitBot, main

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

# Création de l'application Flask
app = Flask(__name__)
bot_status = {"running": False, "last_error": None}

@app.route("/")
def home():
    return {"message": "Bot Visite v2", "status": "active"}

@app.route("/status")
def status():
    return {
        "status": "running" if bot_status["running"] else "stopped",
        "last_error": bot_status["last_error"],
        "telegram_connected": hasattr(app, 'client') and app.client.is_connected()
    }

def run_flask():
    """Démarre le serveur Flask dans un thread séparé."""
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

async def initialize_telegram():
    """Initialise et connecte le client Telegram."""
    try:
        # Récupérer les credentials
        api_id = os.getenv("TELEGRAM_API_ID")
        api_hash = os.getenv("TELEGRAM_API_HASH")
        phone = os.getenv("TELEGRAM_PHONE")

        # Créer le client
        client = TelegramClient('session_name', api_id, api_hash)
        
        # Connexion et authentification
        await client.connect()
        
        if not await client.is_user_authorized():
            # Demander le code de vérification
            sent_code = await client.send_code_request(phone)
            
            # En production, on utiliserait un système de callback
            # Pour ce test, on utilisera une variable d'environnement
            verification_code = os.getenv("TELEGRAM_CODE")
            if not verification_code:
                logger.error("Code de vérification non fourni. Ajoutez TELEGRAM_CODE aux variables d'environnement.")
                return None
                
            try:
                await client.sign_in(phone, verification_code)
            except SessionPasswordNeededError:
                # Si l'authentification à deux facteurs est activée
                password = os.getenv("TELEGRAM_2FA_PASSWORD")
                if not password:
                    logger.error("Mot de passe 2FA requis. Ajoutez TELEGRAM_2FA_PASSWORD aux variables d'environnement.")
                    return None
                await client.sign_in(password=password)

        logger.info("Client Telegram connecté avec succès!")
        return client
    except Exception as e:
        logger.error(f"Erreur d'initialisation Telegram: {e}")
        return None

async def start_bot():
    """Démarre le bot Telegram."""
    try:
        # Initialiser le client Telegram
        client = await initialize_telegram()
        if not client:
            raise Exception("Échec de l'initialisation du client Telegram")

        bot_status["running"] = True
        bot_status["last_error"] = None
        
        # Stocker le client dans l'app Flask
        app.client = client
        
        # Démarrer le bot
        await main()
    except Exception as e:
        bot_status["running"] = False
        bot_status["last_error"] = str(e)
        logger.error(f"Erreur du bot: {e}")
        # Redémarrer après 30 secondes
        await asyncio.sleep(30)
        await start_bot()

if __name__ == "__main__":
    # Vérifier les variables d'environnement
    required_vars = ["TELEGRAM_API_ID", "TELEGRAM_API_HASH", "TELEGRAM_PHONE"]
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Variable d'environnement manquante : {var}")

    # Démarrer Flask dans un thread séparé
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Démarrer le bot
    logger.info("Démarrage du bot...")
    asyncio.run(start_bot())
