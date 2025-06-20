#!/usr/bin/env python3

import os
import sys
import subprocess
import shutil
from datetime import datetime

class PythonAnywhereInstaller:
    def __init__(self):
        self.log_file = "installation.log"
        self.venv_path = os.path.expanduser("~/venv")
        self.project_path = os.path.expanduser("~/bot_visite_v2")

    def log(self, message):
        """Enregistre un message dans le log et l'affiche."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")

    def run_command(self, command):
        """Exécute une commande shell."""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                self.log(f"Erreur: {result.stderr}")
                return False
            return True
        except Exception as e:
            self.log(f"Erreur d'exécution: {e}")
            return False

    def setup_environment(self):
        """Configure l'environnement Python."""
        self.log("Configuration de l'environnement...")
        
        # Créer le virtualenv s'il n'existe pas
        if not os.path.exists(self.venv_path):
            self.log("Création du virtualenv...")
            if not self.run_command(f"python3 -m venv {self.venv_path}"):
                return False

        # Activer le virtualenv
        activate_script = f"source {self.venv_path}/bin/activate"
        self.run_command(activate_script)

        return True

    def clone_repository(self):
        """Clone le repository Git."""
        self.log("Clonage du repository...")
        if os.path.exists(self.project_path):
            shutil.rmtree(self.project_path)
        return self.run_command(
            f"git clone https://github.com/Harymir/bot_visite_v2.git {self.project_path}"
        )

    def install_dependencies(self):
        """Installe les dépendances Python."""
        self.log("Installation des dépendances...")
        return self.run_command(
            f"{self.venv_path}/bin/pip install -r {self.project_path}/requirements.txt"
        )

    def setup_systemd_service(self):
        """Crée un service systemd pour le bot."""
        service_content = f"""[Unit]
        Description=Telegram Bot Visite Service
        After=network.target

        [Service]
        Type=simple
        User={os.getenv('USER')}
        WorkingDirectory={self.project_path}
        Environment="PATH={self.venv_path}/bin"
        ExecStart={self.venv_path}/bin/python worker_config.py
        Restart=always
        RestartSec=60

        [Install]
        WantedBy=multi-user.target
        """
        
        service_file = "bot_visite.service"
        with open(service_file, "w") as f:
            f.write(service_content)
        
        self.log("Configuration du service systemd...")
        commands = [
            f"sudo mv {service_file} /etc/systemd/system/",
            "sudo systemctl daemon-reload",
            "sudo systemctl enable bot_visite",
            "sudo systemctl start bot_visite"
        ]
        
        for cmd in commands:
            if not self.run_command(cmd):
                return False
        return True

    def setup_monitoring(self):
        """Configure la surveillance du bot."""
        cron_job = "*/5 * * * * cd {} && {}/bin/python monitor.py >> monitoring.log 2>&1"
        cron_job = cron_job.format(self.project_path, self.venv_path)
        
        self.log("Configuration de la surveillance...")
        current_crontab = subprocess.getoutput("crontab -l")
        if cron_job not in current_crontab:
            with open("tempcron", "w") as f:
                f.write(current_crontab + "\n" + cron_job + "\n")
            self.run_command("crontab tempcron")
            os.remove("tempcron")

    def install(self):
        """Processus d'installation complet."""
        self.log("Démarrage de l'installation...")
        
        steps = [
            (self.setup_environment, "Configuration de l'environnement"),
            (self.clone_repository, "Clonage du repository"),
            (self.install_dependencies, "Installation des dépendances"),
            (self.setup_systemd_service, "Configuration du service"),
            (self.setup_monitoring, "Configuration de la surveillance")
        ]
        
        for step_func, step_name in steps:
            self.log(f"\nExécution: {step_name}")
            if not step_func():
                self.log(f"❌ Échec de: {step_name}")
                return False
            self.log(f"✓ {step_name} terminé")
        
        self.log("\n✓ Installation terminée avec succès!")
        self.log("\nPour démarrer le bot:")
        self.log("  sudo systemctl start bot_visite")
        self.log("\nPour voir les logs:")
        self.log("  journalctl -u bot_visite -f")
        return True

if __name__ == "__main__":
    installer = PythonAnywhereInstaller()
    installer.install()
