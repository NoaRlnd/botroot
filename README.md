# 🤖 BotRoot – Détection automatique de mauvaises herbes

**BotRoot** est un projet de vision par ordinateur et d’automatisation agricole basé sur l’ESP32-CAM et un FarmBot Express v1.1.

> 📸 Détection | 📐 Conversion pixels → mm | 📍 Position réelle du bras | 📡 Envoi API FarmBot | 🔥 Traitement laser

---

## 🌱 Objectif
Créer un système capable de :

-Détecter automatiquement les mauvaises herbes dans un bac de culture

-Convertir leurs coordonnées pour les placer précisément dans le jardin virtuel FarmBot

-Envoyer ces positions à l’API FarmBot comme des points "Weed"

-Activer un laser pour brûler les mauvaises herbes détectées de manière ciblée

-Sauvegarder les images avant/après tir + métadonnées


---

## 🗂️ Structure du projet 

```
BotRoot/
├── py/
│   ├── grid_scan.py              # Scan automatique du bac en grille
│   ├── grid_coords.py            # Génération des coordonnées (X,Y,Z) de la grille
│   ├── movement.py               # Contrôle du bras FarmBot (lib officielle FarmBot)
│   ├── send_laser.py             # Exécution de la séquence 'laserification'
│   ├── send_to_farmbot.py        # Envoi des mauvaises herbes détectées via WebSocket
│   ├── image_capture.py          # Sauvegarde et nommage des images avec horodatage
│   ├── db_logger.py              # Insertion des métadonnées d’image dans MariaDB
│   ├── logger.py                 # Initialisation du système de logs du projet
│   ├── blob_scan.py              # Détection des mauvaises herbes sur une image
│   ├── conversion_px_to_mm.py    # Conversion coordonnées pixels → mm (calibration)
│   ├── farmbot_status.py         # Position réelle du bras FarmBot (via API)
│   ├── plant_filter.py           # Filtrage des herbes proches des plantes (spread)
│   ├── test_distance.py          # Test unitaire de la distance euclidienne
│   ├── call_sequence.py          # Lancement manuel d'une séquence FarmBot
│   ├── auth.py                   # Authentification API FarmBot
│   └── get_bac_dimensions.py     # Estimation (obsolète) de la taille du bac
├── logs/                         # Dossier des fichiers logs
├── images_archv/
│   ├── before/                   # Images avant laserification
│   └── after/                    # Images après laserification
├── .env                          # Identifiants FarmBot + accès DB (non versionné)
├── requirements.txt              # Liste des dépendances Python
├── README.md                     # Présentation du projet (ce fichier)
└── git_guide.md                  # Aide-mémoire Git
```

---

## 🧪 Technologies utilisées
- ESP32-CAM avec capteur OV2640
- Python 3 avec :
  - `opencv-python`
  - `numpy`
  - `requests`
  - `python-dotenv`
  - `mysql-connector-python`
- API FarmBot (+ WebSocket MQTT)
- Base MariaDB pour les métadonnées
- VS Code, Git, GitHub

---

## Procédure de démo sans FarmBot (simulation)
Branche la caméra et/ou prépare une feuille avec des “plantes” et “mauvaises herbes” dessinées

Configure le .env (voir exemple plus bas)

(Optionnel) Lance un environnement virtuel + installe les dépendances :

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
Lancer le scan automatique :

python grid_scan.py
Le script va :

-Parcourir la grille (ou une seule position en test)

-Détecter les herbes sur l’image

-Filtrer les herbes trop proches des plantes (via l’API)

-Sauvegarder les images avant/après (images_archv/)

-Logger tout le déroulé dans logs/

-(Si la BDD est connectée, écrire les métadonnées)

Montre les résultats dans le terminal, le dossier images_archv/, et la BDD si accessible

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

# installer les dépendances
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

# Lancer un scan complet en grille (avec détection, envoi, laser, image + logs)
python grid_scan.py

# Appeler manuellement la séquence "laserification"
python call_sequence.py
```

## 🔍 Fonction de filtrage “spread”
Le script plant_filter.py exclut les mauvaises herbes trop proches des plantes utiles, selon leur rayon de spread défini via l’API FarmBot.

---

## 💾 Stockage et traçabilité

-Images avant / après laser sauvegardées automatiquement dans images_archv/

-Métadonnées (nom fichier, coordonnées, timestamp) envoyées à la base MariaDB

-Logs centralisés dans logs/ avec toutes les infos de scan

---

## ✅ Avancement du projet
- [x] Détection d’herbes (très approximative)
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
FARMBOT_EMAIL=ton.email@example.com
FARMBOT_PASSWORD=ton_mot_de_passe
DB_HOST=adresse_ip_rpi
DB_PORT=3306
DB_USER=ton_utilisateur
DB_PASSWORD=mot_de_passe_db
DB_NAME=botroot_db

---

## 📘 Documentation Git
Consulte `git_guide.md` pour toutes les commandes utiles au projet.

---

## 🧪 Fiche de tests physiques

Consulte `test_checklist.md` pour la procédure complète de test avec FarmBot physique : (obsolète)
- Déplacement manuel
- Scan automatique en simulation ou réel
- Déclenchement de la séquence laser
- Vérification sur l’interface FarmBot

---
## ✨ Licence
Libre pour tout usage éducatif, expérimental ou pédagogique (license MIT) 💡