import requests
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

# Authentification FarmBot API
def get_token():
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {"email": EMAIL, "password": PASSWORD}
    })
    token = res.json()["token"]["encoded"]
    return {"Authorization": f"Bearer {token}"}

# Récupération des dimensions du bac
def get_bac_dimensions(headers):
    res = requests.get("https://my.farm.bot/api/device", headers=headers)
    if res.status_code != 200:
        print("❌ Erreur lors de la récupération des dimensions du bac")
        return

    device = res.json()
    settings = device.get("firmware_settings", {})

    max_x = settings.get("movement_axis_length_x", "inconnu")
    max_y = settings.get("movement_axis_length_y", "inconnu")

    print(f"📐 Dimensions du bac : X = {max_x} mm, Y = {max_y} mm")

if __name__ == "__main__":
    headers = get_token()
    get_bac_dimensions(headers)
