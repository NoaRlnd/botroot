from blob_scan import detect_weeds
from farmbot_status import get_current_position
from plant_filter import filter_weeds_against_plants
from dotenv import load_dotenv
import os
import requests

load_dotenv()

EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

def send_to_farmbot(weeds):
    print("Connexion à l'API FarmBot...")

    token_req = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {
            "email": EMAIL,
            "password": PASSWORD
        }
    })

    token = token_req.json()["token"]["encoded"]
    headers = {"Authorization": f"Bearer {token}"}

    # Obtenir la position actuelle du bras
    x_bot, y_bot, z_bot = get_current_position(headers)

    # Ajouter l'offset du bras à chaque mauvaise herbe
    for weed in weeds:
        weed["x"] += x_bot
        weed["y"] += y_bot
        weed["z"] = z_bot

    # Filtrer les mauvaises herbes trop proches des plantes utiles
    weeds = filter_weeds_against_plants(weeds, headers, margin=5)

    # Envoi des mauvaises herbes à FarmBot
    for i, weed in enumerate(weeds):
        payload = {
            "pointer_type": "Weed",
            "name": f"weed-{i+1}",
            "x": weed["x"],
            "y": weed["y"],
            "z": weed["z"],
            "radius": weed["radius"],
            "meta": {"created_by": "BotRoot"}
        }
        response = requests.post("https://my.farm.bot/api/points", headers=headers, json=payload)
        if response.status_code == 200:
            print(f"Weed #{i+1} envoyée avec succès ✅")
        else:
            print(f"Erreur envoi weed #{i+1} ❌", response.status_code, response.text)

def main():
    print("🔍 Lancement de la détection...")
    image, weeds = detect_weeds()

    if not weeds:
        print("✅ Aucune mauvaise herbe détectée.")
    else:
        print(f"📦 Envoi de {len(weeds)} weed(s) au FarmBot...")
        send_to_farmbot(weeds)

if __name__ == "__main__":
    main()