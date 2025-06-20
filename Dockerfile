FROM python:3.9-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends     git     && rm -rf /var/lib/apt/lists/*

# Copier les fichiers du projet
COPY requirements.txt .
COPY bot_visite.py .
COPY .env .
COPY install.sh .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour lancer le bot
CMD ["python", "bot_visite.py"]
