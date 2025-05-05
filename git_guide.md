
# 📘 Guide Git pour le projet BotRoot

## ⚙️ Initialisation du projet (déjà fait)

```bash
git init                            # Initialise un dépôt Git
git remote add origin <URL_DU_REPO>  # Lien avec le dépôt GitHub
```

---

## 🔄 Cycle de travail classique

```bash
git add .                           # Prépare tous les fichiers modifiés pour le commit
git commit -m "Message clair"      # Enregistre une étape localement
git push                            # Envoie les modifications sur GitHub
```

➡️ À faire à chaque fois que tu avances dans ton projet

---

## 🔃 Récupérer les dernières modifs (depuis un autre PC ou un collaborateur)

```bash
git pull                            # Met à jour ton dossier avec les dernières modifs du dépôt GitHub
```

---

## 🔍 Vérifier l’état de ton projet

```bash
git status                          # Affiche les fichiers modifiés, ajoutés ou non suivis
```

---

## ❌ Annuler une modification (avant commit)

```bash
git checkout -- fichier.py          # Annule les changements sur un fichier donné
```

---

## 🌿 Créer une nouvelle branche (optionnel, pour faire des tests)

```bash
git checkout -b nom_de_branche     # Crée une nouvelle branche et bascule dessus
```

Pour revenir à la branche principale :
```bash
git checkout main
```

Pour fusionner une branche dans main :
```bash
git merge nom_de_branche
```

---

## 📦 Exemples concrets (BotRoot)

```bash
# Tu viens de modifier blob_scan.py et send_to_farmbot.py
git add .
git commit -m "Amélioration détection + envoi API"
git push
```

```bash
# Tu veux mettre à jour ton projet depuis GitHub (autre PC ou coéquipier)
git pull
```

---

## 🧠 Astuce : utiliser .gitignore
Ajoute un fichier `.gitignore` avec ceci :

```
__pycache__/
*.pyc
.env
.vscode/
*.log
```

➡️ Évite d’ajouter les fichiers temporaires ou secrets à ton dépôt GitHub.

---

## 🧳 Reprendre le projet sur un autre PC (setup multi-machine)

### 1. Depuis ton PC actuel (sauvegarde sur GitHub) :

```bash
git add .
git commit -m "Dernières modifs avant changement de machine"
git push
```

### 2. Sur le nouveau PC :

```bash
git clone https://github.com/NoaRlnd/botroot.git
cd botroot
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Crée un fichier `py/.env` ou plutôt `.env` tout court avec :

```
FARMBOT_EMAIL=ton@email.com 
FARMBOT_PASSWORD=tonmotdepasse
```

➡️ Tu es prêt à lancer le projet :

```bash
python blob_scan.py
python send_to_farmbot.py
python grid_scan.py
```