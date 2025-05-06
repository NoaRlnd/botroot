
import requests
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

def get_token():
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {"email": EMAIL, "password": PASSWORD}
    })
    return res.json()["token"]["encoded"]

def run_sequence(sequence_id):
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "kind": "execute",
        "args": {
            "sequence_id": sequence_id
        }
    }

    res = requests.post("https://my.farm.bot/api/celery_script", headers=headers, json=payload)

    if res.status_code == 200:
        print(f"✅ Séquence {sequence_id} lancée avec succès")
    else:
        print(f"❌ Erreur lors du lancement : {res.status_code}", res.text)

if __name__ == "__main__":
    # ID de la séquence "burn_weed"
    run_sequence(sequence_id=247082)
