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
    ├── blob_scan.py               # Détection d’herbes sur image (OpenCV + ESP32)
    ├── conversion_px_to_mm.py     # Conversion coordonnées pixels → millimètres
    ├── send_to_farmbot.py         # Script principal : détection + envoi API
    ├── farmbot_status.py          # Récupération de la position du bras FarmBot
    ├── git_guide.md               # Fiche d’aide sur Git
    └── README.md                  # Présentation du projet
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

### Installation des dépendances
```bash
pip install opencv-python numpy requests
```

### Lancer la détection seule
```bash
python blob_scan.py
```

### Lancer la détection + envoi vers FarmBot
```bash
python send_to_farmbot.py
```

➡️ Les mauvaises herbes détectées s'afficheront automatiquement dans votre jardin virtuel FarmBot 🌿

---

## ✅ Avancement du projet
- [x] Détection d’herbes
- [x] Conversion px → mm calibrée
- [x] Récupération position bras
- [x] Envoi à l’API FarmBot
- [ ] Scan automatique du bac complet
- [ ] Filtrage par "spread" des plantes
- [ ] Intégration laser (simulation ou GPIO)


---

## 🙋‍♂️ Auteur
**Noa** – Étudiant en informatique 🧠🌿
**nathan r** - Étudiant en informatique
> Projet personnel d’apprentissage en vision par ordi, robotique et dev embarqué


---

## 🔐 Sécurité
Penser à ne **pas versionner** ses identifiants !
Ajoute-les dans un `.env` ou stocke-les ailleurs si besoin 💡

---

## 📘 Documentation Git
Consulte `git_guide.md` pour toutes les commandes utiles au projet.

---

## ✨ Licence
Libre pour tout usage éducatif, expérimental ou pédagogique 💡