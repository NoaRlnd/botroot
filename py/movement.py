import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

# Authentification FarmBot API
def get_token():
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {"email": EMAIL, "password": PASSWORD}
    })
    return res.json()["token"]["encoded"]

# Fonction pour envoyer une commande de déplacement
def move_to(x, y, z=0):
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "kind": "move",
        "args": {
            "x": x,
            "y": y,
            "z": z
        }
    }

    print(f"🚜 Déplacement vers X={x}, Y={y}, Z={z}...")
    res = requests.post("https://my.farm.bot/api/celery_script", headers=headers, json=payload)

    if res.status_code == 200:
        print("✅ Mouvement envoyé avec succès")
    else:
        print(f"❌ Erreur lors du mouvement : {res.status_code}", res.text)

    time.sleep(5)  # Attente approximative du déplacement