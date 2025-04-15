import requests

def get_current_position(headers):
    """
    Interroge l’API FarmBot pour récupérer la position actuelle du bras.

    Retourne : (x, y, z) en millimètres
    """
    response = requests.get("https://my.farm.bot/api/device", headers=headers)

    if response.status_code != 200:
        print("❌ Impossible d'obtenir la position du bras FarmBot.")
        return 0, 0, 0

    device = response.json()
    position = device.get("location_data", {}).get("position", {})

    x = position.get("x", 0)
    y = position.get("y", 0)
    z = position.get("z", 0)

    print(f"📍 Position actuelle du bras : x={x}, y={y}, z={z}")
    return x, y, z
