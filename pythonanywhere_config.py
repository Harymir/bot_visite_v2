#!/usr/bin/env python3

import os
import sys
from bot_visite import main

# Ajouter le chemin du projet
path = os.path.expanduser('~/bot_visite_v2')
if path not in sys.path:
    sys.path.append(path)

# Configuration des variables d'environnement
os.environ['PYTHONUNBUFFERED'] = '1'

# Point d'entrée pour PythonAnywhere
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Bot is running"]

# Si exécuté directement (pour les tests)
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
