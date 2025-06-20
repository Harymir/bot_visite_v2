#!/usr/bin/env python3

import os
import logging
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="bot.log"
)
logger = logging.getLogger(__name__)

async def run_bot():
    """Exécute le bot avec la session préauthentifiée."""
    try:
        # Récupérer la session
        session_string = os.getenv("TELEGRAM_SESSION")
        api_id = os.getenv("TELEGRAM_API_ID")
        api_hash = os.getenv("TELEGRAM_API_HASH")
        
        if not all([session_string, api_id, api_hash]):
            raise ValueError("Variables d environnement manquantes")
        
        # Créer le client avec la session existante
        client = TelegramClient(
            StringSession(session_string),
            api_id,
            api_hash
        )
        
        await client.connect()
        if not await client.is_user_authorized():
            raise ValueError("Session non valide")
        
        logger.info("Bot démarré avec succès")
        
        # Boucle principale
        while True:
            try:
                from bot_visite import main
                await main()
            except Exception as e:
                logger.error(f"Erreur: {e}")
                await asyncio.sleep(60)
                
    except Exception as e:
        logger.error(f"Erreur fatale: {e}")

if __name__ == "__main__":
    asyncio.run(run_bot())

