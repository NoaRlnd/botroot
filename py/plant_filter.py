import requests
import math

def distance(x1, y1, x2, y2):
    """Calcule la distance euclidienne entre 2 points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def filter_weeds_against_plants(weeds, headers, margin=5):
    """Filtre les mauvaises herbes trop proches des plantes utiles"""
    # Étape 1 : Récupérer les plantes
    response = requests.get("https://my.farm.bot/api/points?pointer_type=Plant", headers=headers)

    if response.status_code != 200:
        print("❌ Erreur lors de la récupération des plantes")
        return weeds  # On retourne toutes les mauvaises herbes sans filtrage

    plants = response.json()

    filtered = []
    for weed in weeds:
        weed_x = weed["x"]
        weed_y = weed["y"]
        too_close = False

        # Pour chaque plante, on compare la distance
        for plant in plants:
            plant_x = plant["x"]
            plant_y = plant["y"]
            spread = plant.get("radius", 50)  # 50 mm par défaut

            d = distance(weed_x, weed_y, plant_x, plant_y)
            if d < (spread + margin):
                too_close = True
                break

        if not too_close:
            filtered.append(weed)

    print(f"🌿 {len(filtered)} mauvaise(s) herbe(s) gardée(s) après filtrage par \"spread\".")
    return filtered
