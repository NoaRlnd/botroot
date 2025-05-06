
# ✅ BotRoot – Check-list de tests FarmBot physique

## 🧳 Avant de partir (sur PC principal)

- [x] `git add . && git commit -m "Préparation tests FarmBot physique"`
- [x] `git push`
- [x] Vérifier `git status` = propre

---

## 💻 Setup sur le PC de test (sur place)

```bash
git clone https://github.com/NoaRlnd/botroot.git
cd botroot
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Créer le fichier `py/.env` :

```env
FARMBOT_EMAIL=ton@email.com
FARMBOT_PASSWORD=tonmotdepasse
```

---

## 🔹 Étape 1 – Tester les mouvements (movement.py)

```python
from movement import move_to
move_to(100, 100, 0)
move_to(200, 300, 5)
```

✅ Le bras doit se déplacer correctement

🕒 **Mesurer le temps réel de déplacement** pour ajuster le délai entre chaque scan dans `grid_scan.py`

---

## 🔹 Étape 2 – Scan en simulation

Dans `grid_scan.py` :
```python
SIMULATION_MODE = True
```

Lancer :
```bash
python grid_scan.py
```

✅ Vérifier les logs dans le terminal

---

## 🔹 Étape 3 – Scan réel (désactive le mode simulation)

Dans `grid_scan.py` :
```python
SIMULATION_MODE = False
```

Lancer :
```bash
python grid_scan.py
```

✅ Le bras doit scanner le bac et détecter les weeds

---

## 🔹 Étape 4 – Vérifier sur my.farm.bot

➡️ Ouvrir https://my.farm.bot  
- Onglet **Weeds** → points envoyés
- Onglet **Logs** → messages et positions
- Onglet **Sequences** → exécution de "laserification"

---

## 🔹 Étape 5 – Lancer manuellement la séquence (optionnel)

```bash
python call_sequence.py
```

✅ Le bras simule un tir laser

---

## 📌 Remarques utiles

- Chaque weed détectée lance automatiquement la séquence `"laserification"`
- Tu peux ajuster :
  - le pas de la grille (`grid_spacing`)
  - le délai entre deux points (`time.sleep`) selon la vitesse réelle mesurée
