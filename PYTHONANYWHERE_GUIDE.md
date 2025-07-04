# Déploiement sur PythonAnywhere

## Avantages
- Limite de requête de 15 minutes (meilleur que Render)
- Console accessible en permanence
- Session Telegram persistante
- Redémarrage automatique configurable
- Logs faciles à consulter

## Installation

1. Créez un compte sur PythonAnywhere
2. Ouvrez une console Bash
3. Clonez le repository:
```bash
git clone https://github.com/Harymir/bot_visite_v2.git
cd bot_visite_v2
```

4. Configurez l'environnement:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. Créez le fichier .env:
```bash
echo "TELEGRAM_API_ID=votre_api_id" > .env
echo "TELEGRAM_API_HASH=votre_api_hash" >> .env
echo "TELEGRAM_PHONE=votre_phone" >> .env
```

6. Lancez la configuration:
```bash
python pa_setup.py
```

7. Suivez les instructions pour:
   - Authentification Telegram
   - Configuration de la tâche programmée
   - Démarrage du bot

## Maintenance

- Logs: `tail -f bot.log`
- Redémarrage: `bash start_bot.sh`
- Mise à jour: `git pull && pip install -r requirements.txt`

## Dépannage

1. Si le bot se déconnecte:
   ```bash
   python pa_setup.py  # Reconfigurer la session
   ```

2. Pour les logs d'erreur:
   ```bash
   cat bot.log | grep ERROR
   ```

3. Pour redémarrer complètement:
   ```bash
   pkill -f worker_config.py
   bash start_bot.sh
   ```

## Gestion des cycles du bot

Le worker est configuré pour:
- Exécuter des cycles de 14 minutes
- Faire une pause de 1 minute entre les cycles
- Gérer automatiquement la reconnexion
- Maintenir la session Telegram active
- Logger toutes les activités

Pour voir les cycles en action:
```bash
tail -f bot.log
```


## Surveillance du Bot

Pour surveiller le bot, utilisez le script monitor.py:

1. Vérification ponctuelle:
   ```bash
   python monitor.py
   ```

2. Surveillance continue:
   ```bash
   python monitor.py --continuous
   ```

Le moniteur vérifie:
- État actuel du bot
- Nombre d'erreurs récentes
- Derniers logs
- Inactivité prolongée

En cas d'inactivité, le moniteur suggère des commandes de dépannage.

