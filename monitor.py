#!/usr/bin/env python3

import os
import sys
import time
import json
import logging
from datetime import datetime, timedelta

class BotMonitor:
    def __init__(self):
        self.log_file = 'bot.log'
        self.stats_file = 'bot_stats.json'
        self.alert_threshold = 300  # 5 minutes sans activité

    def read_last_logs(self, lines=50):
        """Lit les dernières lignes du fichier de log."""
        if not os.path.exists(self.log_file):
            return []
        try:
            with open(self.log_file, 'r') as f:
                return f.readlines()[-lines:]
        except Exception:
            return []

    def get_bot_status(self):
        """Vérifie le statut actuel du bot."""
        logs = self.read_last_logs()
        if not logs:
            return "INCONNU"

        last_log_time = None
        for log in reversed(logs):
            try:
                log_time = datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
                last_log_time = log_time
                break
            except:
                continue

        if not last_log_time:
            return "INCONNU"

        time_diff = datetime.now() - last_log_time
        if time_diff.seconds > self.alert_threshold:
            return "INACTIF"
        return "ACTIF"

    def get_error_count(self):
        """Compte les erreurs dans les logs récents."""
        logs = self.read_last_logs()
        error_count = sum(1 for log in logs if 'ERROR' in log)
        return error_count

    def save_stats(self):
        """Sauvegarde les statistiques actuelles."""
        stats = {
            'timestamp': datetime.now().isoformat(),
            'status': self.get_bot_status(),
            'recent_errors': self.get_error_count(),
            'last_logs': self.read_last_logs(10)
        }
        
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(stats, f, indent=2)
        except Exception as e:
            print(f"Erreur de sauvegarde des stats: {e}")

    def display_status(self):
        """Affiche un résumé du statut du bot."""
        status = self.get_bot_status()
        errors = self.get_error_count()
        
        print("\n=== Status du Bot ===")
        print(f"État     : {status}")
        print(f"Erreurs  : {errors} récentes")
        
        print("\nDerniers logs:")
        for log in self.read_last_logs(5):
            print(f"  {log.strip()}")
        
        if status == "INACTIF":
            print("\n⚠️  ALERTE: Bot inactif depuis plus de 5 minutes!")
            print("Commandes de dépannage:")
            print("1. pkill -f worker_config.py")
            print("2. bash start_bot.sh")

    def monitor_continuously(self):
        """Surveille le bot en continu."""
        print("Démarrage de la surveillance...")
        try:
            while True:
                self.display_status()
                self.save_stats()
                time.sleep(60)  # Vérification toutes les minutes
        except KeyboardInterrupt:
            print("\nSurveillance arrêtée.")

if __name__ == "__main__":
    monitor = BotMonitor()
    if len(sys.argv) > 1 and sys.argv[1] == '--continuous':
        monitor.monitor_continuously()
    else:
        monitor.display_status()
