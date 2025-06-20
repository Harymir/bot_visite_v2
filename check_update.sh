#!/bin/bash

# Couleurs pour le terminal
GREEN="[0;32m"
RED="[0;31m"
NC="[0m"

echo -e "${GREEN}=== Bot Visite v2 - Outil de maintenance ===${NC}
"

# Vérifier les mises à jour Git
echo "Vérification des mises à jour..."
git pull origin main

# Vérifier les dépendances Python
echo -e "
Vérification des dépendances Python..."
pip install -r requirements.txt

# Vérifier le fichier .env
echo -e "
Vérification de la configuration..."
if [ ! -f .env ]; then
    echo -e "${RED}ERREUR: Fichier .env manquant${NC}"
    echo "Création du template .env..."
    echo "TELEGRAM_API_ID=votre_api_id
TELEGRAM_API_HASH=votre_api_hash
TELEGRAM_PHONE=votre_numero" > .env
    echo -e "${RED}Veuillez éditer le fichier .env avec vos credentials${NC}"
else
    echo -e "${GREEN}Fichier .env trouvé${NC}"
fi

# Vérifier les logs
echo -e "
Vérification des logs..."
if [ ! -f bot_visite.log ]; then
    touch bot_visite.log
    echo "Fichier de log créé"
fi

# Afficher les dernières erreurs dans les logs
echo -e "
Dernières erreurs dans les logs:"
grep "ERROR" bot_visite.log | tail -n 5

echo -e "
${GREEN}Vérification terminée !${NC}"
echo "Pour lancer le bot: python bot_visite.py"
