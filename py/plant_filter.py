import requests
import math
from logger import init_logger

logger = init_logger()

def distance(x1, y1, x2, y2):
    """Calcule la distance euclidienne entre 2 points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def filter_weeds_against_plants(weeds, headers=None, margin=5):
    """
    Filtre les mauvaises herbes trop proches des plantes utiles en fonction du "spread" (rayon) des plantes.
    - weeds : liste de dicts avec clés 'x' et 'y'
    - headers : en-têtes d'authentification pour l'API FarmBot
    - margin : marge de sécurité en mm autour du spread
    """
    if headers is None:
        logger.warning("⚠️ Aucun header fourni : filtrage désactivé")
        return weeds

    try:
        response = requests.get("https://my.farm.bot/api/points?pointer_type=Plant", headers=headers)
        response.raise_for_status()
    except Exception as e:
        logger.error(f"❌ Erreur lors de la récupération des plantes : {e}")
        return weeds

    plants = response.json()
    filtered = []

    for weed in weeds:
        weed_x, weed_y = weed["x"], weed["y"]
        too_close = False

        for plant in plants:
            plant_x, plant_y = plant.get("x", 0), plant.get("y", 0)
            spread = plant.get("radius") or plant.get("spread") or 50  # fallback
            logger.debug(f"🌱 Plante à ({plant_x}, {plant_y}) avec zone d’influence = {spread} mm")
            if spread is None:
                logger.warning(f"⚠️ Plante à ({plant_x}, {plant_y}) sans zone d’influence définie, ignorée")
                continue

            d = distance(weed_x, weed_y, plant_x, plant_y)
            if d < (spread + margin):
                too_close = True
                break

        if not too_close:
            filtered.append(weed)

    logger.info(f"🌿 {len(filtered)} mauvaise(s) herbe(s) gardée(s) après filtrage par zone d'influence ('spread')")
    return filtered