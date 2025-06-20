#!/usr/bin/env python3

import os
import sys
import logging
import asyncio
from threading import Thread
from flask import Flask
from bot_visite import SiteVisitBot, main

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

# Création de l application Flask
app = Flask(__name__)
bot_status = {"running": False, "last_error": None}

@app.route("/")
def home():
    return {"message": "Bot Visite v2", "status": "active"}

@app.route("/status")
def status():
    return {
        "status": "running" if bot_status["running"] else "stopped",
        "last_error": bot_status["last_error"]
    }

def run_flask():
    """Démarre le serveur Flask dans un thread séparé."""
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

async def start_bot():
    """Démarre le bot Telegram."""
    try:
        bot_status["running"] = True
        bot_status["last_error"] = None
        await main()
    except Exception as e:
        bot_status["running"] = False
        bot_status["last_error"] = str(e)
        logger.error(f"Erreur du bot: {e}")
        # Redémarrer le bot après 30 secondes
        await asyncio.sleep(30)
        await start_bot()

if __name__ == "__main__":
    # Vérifier les variables d environnement
    required_vars = ["TELEGRAM_API_ID", "TELEGRAM_API_HASH", "TELEGRAM_PHONE"]
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Variable d environnement manquante : {var}")

    # Démarrer Flask dans un thread séparé
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Démarrer le bot
    logger.info("Démarrage du bot...")
    asyncio.run(start_bot())
