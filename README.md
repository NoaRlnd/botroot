# 🤖 BotRoot – Détection automatique de mauvaises herbes

**BotRoot** est un projet de vision par ordinateur et d’automatisation agricole basé sur l’ESP32-CAM et un FarmBot Express v1.1.

> 📸 Détection | 📐 Conversion pixels → mm | 📍 Position réelle du bras | 📡 Envoi API FarmBot | 🔥 Traitement laser

---

## 🌱 Objectif
Créer un système capable de :
- Détecter automatiquement les mauvaises herbes dans un bac de culture
- Convertir leurs coordonnées pour les placer précisément dans le jardin virtuel FarmBot
- Envoyer ces positions à l’API FarmBot comme des points "Weed"
- Activer un **laser** pour brûler les mauvaises herbes détectées de manière ciblée (prochaine étape)


---

## 🗂️ Structure du projet 

```
BotRoot/
└── py/
    ├── grid_scan.py               # Scan automatique du bac (en grille)
    ├── movement.py                # Fonctions de mouvement du bras FarmBot
    ├── call_sequence.py           # Appel manuel d'une séquence FarmBot
    ├── plant_filter.py            # Filtrage des mauvaises herbes proches des plantes
    ├── test_distance.py           # Test unitaire de la distance euclidienne
    ├── get_bac_dimensions.py      # Tentative d'estimation automatique de la taille du bac, un peu useless
    ├── BS_testing.py              # Script de test de connexion/authentification à l'API FarmBot
    ├── blob_scan.py               # Détection d’herbes sur image (OpenCV + ESP32)
    ├── conversion_px_to_mm.py     # Conversion coordonnées pixels → millimètres
    ├── send_to_farmbot.py         # Script principal : détection + envoi API
    ├── farmbot_status.py          # Récupération de la position du bras FarmBot
    ├── git_guide.md               # Fiche d’aide sur Git (pas dans le dossier py)
    └── README.md                  # Présentation du projet (pareil)
```

---

## 🧪 Technologies utilisées
- ESP32-CAM avec capteur OV2640
- Python 3 avec :
  - `opencv-python`
  - `numpy`
  - `requests`
- API FarmBot
- VS Code, Git, GitHub


---

## 💻 Lancer le projet

### Prérequis
- Avoir une ESP32-CAM connectée au réseau Wi-Fi
- Créer un compte sur https://my.farm.bot
- Avoir Python 3 installé

### (Optionnel) Utiliser un environnement virtuel Python
```bash
# Créer l’environnement
python -m venv .venv

# Activer l’environnement sous PowerShell
.venv\Scripts\Activate.ps1

# Installer les dépendances manuellement
pip install opencv-python numpy requests python-dotenv

# OU (recommandé si requirements.txt est fourni)
pip install -r requirements.txt

# Sauvegarder les dépendances, ca prend toutes les extensions et dépendances et ca les mets dans requirments.txt. comme ca tu peux faire la commande du dessus avec tout ce qui faut
pip freeze > requirements.txt
```

### Lancer la détection seule
```bash
python blob_scan.py
```

### Lancer la détection + envoi vers FarmBot
```bash
python send_to_farmbot.py

# Lancer un scan complet en grille (en mode simulation)
python grid_scan.py

# Appeler manuellement la séquence "laserification"
python call_sequence.py
```

### Fonction de filtrage par \"spread\"
Le script exclut automatiquement les mauvaises herbes trop proches d'une plante utile (en se basant sur le rayon de \"spread\" des plantes défini par FarmBot).

➡️ Cela permet d'éviter de marquer comme weed une pousse utile.


➡️ Les mauvaises herbes détectées s'afficheront automatiquement dans votre jardin virtuel FarmBot 🌿

---

## ✅ Avancement du projet
- [x] Détection d’herbes
- [x] Conversion px → mm calibrée
- [x] Récupération position bras
- [x] Envoi à l’API FarmBot
- [x] Scan automatique du bac complet
- [x] Filtrage par "spread" des plantes
- [ ] Intégration laser (simulation ou GPIO)
- [x] Intégration laser (via séquence FarmBot)


---

## 🙋‍♂️ Auteur
**Noa** – Étudiant en informatique 🧠
**nathan r** - Étudiant en informatique 🌿
> Projet personnel d’apprentissage en vision par ordi, robotique et dev embarqué


---

## 🔐 Sécurité
Penser à ne **pas versionner** ses identifiants !
Ajoute-les dans un `.env` ou stocke-les ailleurs si besoin 💡

# Exemple de .env à la racine du projet (botroot/.env)
FARMBOT_EMAIL=xxxxxxxxxxxxxx@xxxxxxxx.fr
FARMBOT_PASSWORD=xxxxxxxxxx

---

## 📘 Documentation Git
Consulte `git_guide.md` pour toutes les commandes utiles au projet.

---

## 🧪 Fiche de tests physiques

Consulte `test_checklist.md` pour la procédure complète de test avec FarmBot physique :
- Déplacement manuel
- Scan automatique en simulation ou réel
- Déclenchement de la séquence laser
- Vérification sur l’interface FarmBot

---
## ✨ Licence
Libre pour tout usage éducatif, expérimental ou pédagogique (license MIT) 💡