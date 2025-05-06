from blob_scan import detect_weeds
from conversion_px_to_mm import pixels_to_mm
from movement import move_to
from dotenv import load_dotenv
import requests
import os
import time

load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

SEQUENCE_ID = 247082  # ID de la séquence "laserification"

def get_token():
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {"email": EMAIL, "password": PASSWORD}
    })
    return res.json()["token"]["encoded"]

def send_weed(x_mm, y_mm):
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "pointer_type": "Weed",
        "name": "auto-weed",
        "x": x_mm,
        "y": y_mm,
        "z": 0
    }

    res = requests.post("https://my.farm.bot/api/points", headers=headers, json=payload)
    return res.status_code == 200

def run_sequence(sequence_id):
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "kind": "execute",
        "args": {"sequence_id": sequence_id}
    }

    res = requests.post("https://my.farm.bot/api/celery_script", headers=headers, json=payload)
    return res.status_code == 200

if __name__ == "__main__":
    print("🔍 Lancement de la détection...")
    image, weeds = detect_weeds()

    if len(weeds) == 0:
        print("✅ Aucune mauvaise herbe détectée.")
    else:
        print(f"📦 Envoi de {len(weeds)} weed(s) au FarmBot...")

        for i, (x_mm, y_mm) in enumerate(weeds, start=1):
            success = send_weed(x_mm, y_mm)

            if success:
                print(f"🌿 Weed #{i} envoyée ✅")
                seq_ok = run_sequence(SEQUENCE_ID)
                if seq_ok:
                    print(f"🚨 Séquence laserification lancée pour Weed #{i} 🔥")
                else:
                    print(f"⚠️ Échec lancement séquence après Weed #{i}")
            else:
                print(f"❌ Erreur envoi weed #{i}")
            time.sleep(1)
