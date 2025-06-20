#!/usr/bin/env python3

import os
import sys
import logging
import asyncio
from bot_visite import main

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='bot.log'
)

async def run_bot():
    while True:
        try:
            await main()
        except Exception as e:
            logging.error(f"Erreur du bot: {e}")
            await asyncio.sleep(60)  # Attendre 1 minute avant de réessayer

if __name__ == "__main__":
    asyncio.run(run_bot())
