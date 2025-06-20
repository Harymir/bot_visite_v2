#!/usr/bin/env python3

import webbrowser
import time
import os

def guide_deployment():
    print("
=== Assistant de Déploiement Render ===
")
    
    print("Étape 1: Préparation")
    input("Appuyez sur Entrée pour ouvrir Render.com dans votre navigateur...")
    webbrowser.open("https://dashboard.render.com")
    
    print("
Étape 2: Sur Render.com")
    print("1. Connectez-vous ou créez un compte")
    print("2. Cliquez sur \"New +\"")
    print("3. Sélectionnez \"Web Service\"")
    input("
Une fois fait, appuyez sur Entrée...")
    
    print("
Étape 3: Configuration")
    print("Copiez ces informations pour la configuration :")
    print("
Nom : bot-visite-v2")
    print("Runtime : Python 3")
    print("Build Command : $ pip install -r requirements.txt")
    print("Start Command : $ python render_unified.py")
    
    print("
Étape 4: Variables d environnement")
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            env_vars = f.readlines()
        print("
Copiez ces variables dans Render :")
        for line in env_vars:
            if "=" in line:
                print(line.strip())
    
    print("
Étape 5: Options avancées")
    print("Health Check Path : /status")
    print("HTTP Port : 8080")
    
    input("
Configuration terminée ? Appuyez sur Entrée...")
    
    print("
Étape 6: Déploiement")
    print("1. Cliquez sur \"Create Web Service\"")
    print("2. Attendez que le déploiement soit terminé")
    print("3. Votre bot sera accessible à : https://bot-visite-v2.onrender.com")
    
    print("
Vérification du déploiement :")
    print("1. Surveillez les logs dans l interface Render")
    print("2. Vérifiez le statut à : https://bot-visite-v2.onrender.com/status")
    print("3. Testez le bot sur Telegram")
    
    input("
Appuyez sur Entrée pour terminer...")
    
    print("
=== Déploiement terminé ! ===")
    print("N oubliez pas de surveiller les logs et le statut du bot.")

if __name__ == "__main__":
    guide_deployment()
