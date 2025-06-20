#!/usr/bin/env python3

import os
import sys
import logging
import asyncio
import time
from datetime import datetime, timedelta
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from bot_visite import main

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='bot.log'
)
logger = logging.getLogger(__name__)

class BotWorker:
    def __init__(self):
        self.client = None
        self.last_restart = datetime.now()
        self.session_file = 'pa_session'
        self.run_time = 840  # 14 minutes (pour rester dans la limite de 15 min)
        self.cooldown_time = 60  # 1 minute de pause

    async def init_client(self):
        """Initialise le client Telegram."""
        try:
            if os.path.exists(self.session_file):
                self.client = TelegramClient(
                    self.session_file,
                    os.getenv('TELEGRAM_API_ID'),
                    os.getenv('TELEGRAM_API_HASH')
                )
                await self.client.connect()
                if await self.client.is_user_authorized():
                    logger.info("Session Telegram restaurée avec succès")
                    return True
            
            logger.error("Session Telegram non valide ou expirée")
            return False
        except Exception as e:
            logger.error(f"Erreur d'initialisation du client: {e}")
            return False

    async def run_bot_cycle(self):
        """Exécute un cycle du bot avec limite de temps."""
        try:
            start_time = time.time()
            logger.info(f"Démarrage d'un nouveau cycle de {self.run_time} secondes")
            
            # Créer une tâche pour le bot avec timeout
            try:
                bot_task = asyncio.create_task(main())
                await asyncio.wait_for(bot_task, timeout=self.run_time)
            except asyncio.TimeoutError:
                logger.info("Cycle terminé par timeout (normal)")
            
            elapsed = time.time() - start_time
            logger.info(f"Cycle terminé après {elapsed:.1f} secondes")
            
            # Pause avant le prochain cycle
            logger.info(f"Pause de {self.cooldown_time} secondes")
            await asyncio.sleep(self.cooldown_time)
            
            return True
        except Exception as e:
            logger.error(f"Erreur pendant le cycle: {e}")
            return False

    async def run(self):
        """Boucle principale du worker."""
        while True:
            try:
                # Vérifier/initialiser le client
                if not self.client or not self.client.is_connected():
                    if not await self.init_client():
                        logger.error("Impossible d'initialiser le client. Attente de 5 minutes.")
                        await asyncio.sleep(300)
                        continue

                # Exécuter un cycle
                await self.run_bot_cycle()
                
                # Mettre à jour le timestamp du dernier redémarrage
                self.last_restart = datetime.now()
                
            except Exception as e:
                logger.error(f"Erreur dans la boucle principale: {e}")
                await asyncio.sleep(60)

async def main_worker():
    """Point d'entrée principal."""
    worker = BotWorker()
    await worker.run()

if __name__ == "__main__":
    logger.info("Démarrage du worker...")
    asyncio.run(main_worker())
