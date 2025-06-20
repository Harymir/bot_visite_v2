# Guide de Contribution

## Commandes Git courantes

1. Pour obtenir les dernières mises à jour :
   ```bash
   git pull origin main
   ```

2. Pour ajouter des modifications :
   ```bash
   git add .
   git commit -m "Description de vos changements"
   git push origin main
   ```

3. Pour créer une nouvelle branche :
   ```bash
   git checkout -b nom-de-la-branche
   ```

4. Pour voir l'historique des commits :
   ```bash
   git log --oneline
   ```

## Workflow de développement

1. Toujours tirer (pull) les derniers changements avant de commencer à travailler
2. Créer une branche pour chaque nouvelle fonctionnalité
3. Tester les changements localement
4. Commiter avec des messages descriptifs
5. Pousser les changements sur GitHub

## Utilisation du Token GitHub

Le token GitHub est configuré. Pour le mettre à jour :
1. Générer un nouveau token sur GitHub
2. Mettre à jour la remote URL :
   ```bash
   git remote set-url origin https://NOUVEAU_TOKEN@github.com/Harymir/bot_visite_v2.git
   ```

## Structure du Projet

- `bot_visite.py` : Script principal
- `.env` : Configuration (ne pas commiter)
- `requirements.txt` : Dépendances
- `install.sh` : Script d'installation
- `bot_visite.log` : Logs (ignoré par git)

## Notes importantes

- Ne jamais commiter de credentials ou de tokens
- Toujours mettre à jour requirements.txt si vous ajoutez des dépendances
- Vérifier les logs avant de commiter
