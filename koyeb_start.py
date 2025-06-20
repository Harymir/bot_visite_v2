#!/usr/bin/env python3

import os
import logging
from bot_visite import SiteVisitBot, main

# Configuration du logging pour Koyeb
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

if __name__ == "__main__":
    # Vérification des variables d environnement
    required_env_vars = ["TELEGRAM_API_ID", "TELEGRAM_API_HASH", "TELEGRAM_PHONE"]
    for var in required_env_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Variable d environnement manquante : {var}")
    
    # Démarrage du bot
    main()
