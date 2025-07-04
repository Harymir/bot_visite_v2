FROM python:3.9-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends     git     && rm -rf /var/lib/apt/lists/*

# Copier les fichiers du projet
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Rendre le script de démarrage exécutable
RUN chmod +x koyeb_start.py

# Commande pour lancer le bot
CMD ["python", "koyeb_start.py"]
