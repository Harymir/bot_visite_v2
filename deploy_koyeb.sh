#!/bin/bash

echo "=== Vérification pré-déploiement Koyeb ==="

# Vérifier les fichiers requis
required_files=("Dockerfile" "koyeb_start.py" "requirements.txt" "bot_visite.py" ".env" "Procfile")

echo "1. Vérification des fichiers..."
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ $file trouvé"
    else
        echo "✗ $file manquant!"
        exit 1
    fi
done

# Vérifier les variables d environnement
echo -e "
2. Vérification des variables d environnement..."
if grep -q "TELEGRAM_API_ID" .env && grep -q "TELEGRAM_API_HASH" .env && grep -q "TELEGRAM_PHONE" .env; then
    echo "✓ Variables d environnement configurées"
else
    echo "✗ Variables d environnement manquantes dans .env"
    exit 1
fi

# Vérifier les dépendances Python
echo -e "
3. Vérification des dépendances Python..."
if pip install -r requirements.txt --dry-run > /dev/null 2>&1; then
    echo "✓ Toutes les dépendances sont valides"
else
    echo "✗ Problème avec les dépendances"
    exit 1
fi

echo -e "
=== Prêt pour le déploiement ! ==="
echo "
Instructions de déploiement sur Koyeb :

1. Allez sur https://app.koyeb.com
2. Cliquez sur \"Create App\"
3. Choisissez \"GitHub\" comme source
4. Sélectionnez le repository \"bot_visite_v2\"
5. Configurez les variables d environnement :
   - TELEGRAM_API_ID
   - TELEGRAM_API_HASH
   - TELEGRAM_PHONE
6. Déployez !

Une fois déployé, vérifiez les logs sur Koyeb pour confirmer le bon fonctionnement."
