#!/usr/bin/env python3

import os
import sys
import logging
import time
import requests
from threading import Thread
from bot_visite import main

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout  # Log to stdout for Render
)

def keep_alive():
    """Maintient le service Render actif en faisant des requêtes périodiques."""
    while True:
        try:
            app_url = os.getenv("RENDER_EXTERNAL_URL")
            if app_url:
                requests.get(app_url)
                logging.info("Service ping successful")
            time.sleep(300)  # Ping toutes les 5 minutes
        except Exception as e:
            logging.warning(f"Keep-alive ping failed: {e}")
            time.sleep(60)

if __name__ == "__main__":
    # Vérification des variables d environnement
    required_vars = ["TELEGRAM_API_ID", "TELEGRAM_API_HASH", "TELEGRAM_PHONE"]
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Variable d environnement manquante : {var}")

    # Démarrer le thread keep-alive
    keep_alive_thread = Thread(target=keep_alive, daemon=True)
    keep_alive_thread.start()

    # Démarrer le bot
    main()
