from blob_scan import detect_weeds
from farmbot_status import get_current_position
# from grid_coords import generate_grid_positions                   à remettre très vite, c'est juste pour un test rapide 
from grid_coords_test import generate_grid_positions
from send_laser import send_laser_sequence
from send_to_farmbot import send_weed_to_farmbot
from logger import init_logger  
from db_logger import log_image_metadata                               
from image_capture import save_image 
from plant_filter import filter_weeds_against_plants
from auth import get_headers
from movement import init_farmbot

import time
import os

# --- Paramètres de la grille (ajustés au bac FarmBot Express 1.1) --- probablement inutiles car déjà dans grid_coords.py mais à vérifier plus tard
GRID_WIDTH = 6       # 1200 mm / 205 mm ≈ 6
GRID_HEIGHT = 20     # 3000 mm / 151 mm ≈ 20
STEP_X = 205         # Largeur réelle couverte par l'image
STEP_Y = 151         # Hauteur réelle couverte par l'image

ORIGIN_X = 0
ORIGIN_Y = 0
Z_HEIGHT = 0         # Hauteur fixe (à ajuster si besoin)

DELAI_MOUVEMENT = 6.0 # Délai entre chaque mouvement (en secondes)
SIMULATION_MODE = True  # True = pas de mouvement réel, False = déplacement réel

# --- Fonction principale ---
logger = init_logger()
headers = get_headers()
fb = init_farmbot()  

def scan_area():
    positions = generate_grid_positions()  # Coordonnées X, Y, Z à scanner
    total = len(positions)
    logger.info(f"🔁 Démarrage du scan sur {total} positions...\n")

    # Initialisation de l'instance FarmBot
    fb = init_farmbot()

    for i, (x, y, z) in enumerate(positions):
        logger.info(f"📍 Position {i+1}/{total} : X={x} mm, Y={y} mm, Z={z} mm")

        if SIMULATION_MODE:
            logger.info("🧪 Mode simulation : aucun déplacement réel")
        else:
            logger.debug("🚫 Déplacement désactivé (move_to commenté volontairement)")
            # move_to(x, y, z)  # désactivé pour sécurité/test hors FarmBot

        # Capture simulée d'image + détection
        image, weeds = detect_weeds()
        logger.info(f"🔍 {len(weeds)} mauvaise(s) herbe(s) détectée(s)")

        # Filtrage des mauvaises herbes proches des plantes
        filtered_weeds = filter_weeds_against_plants(weeds, headers)
        logger.info(f"🧹 {len(filtered_weeds)} gardée(s) après filtrage par spread")

        # Sauvegarde image et log TOUJOURS, simulation ou réel
        prefix = "before_simu" if SIMULATION_MODE else "before"
        image_path = save_image(image, prefix=prefix, folder="images_archv/before")
        log_image_metadata(os.path.basename(image_path), prefix, x, y)
        logger.info(f"💾 Image sauvegardée (avant) : {image_path}")

        # Simulation d'une image "après"
        image_after, _ = detect_weeds()
        prefix_after = "after_simu" if SIMULATION_MODE else "after"
        after_path = save_image(image_after, prefix=prefix_after, folder="images_archv/after")
        logger.info(f"💾 Image sauvegardée (après) : {after_path}")
        log_image_metadata(os.path.basename(after_path), prefix_after, x, y)

        if not SIMULATION_MODE and filtered_weeds:
            for weed in filtered_weeds:
                try:
                    send_weed_to_farmbot(fb, weed["x"], weed["y"])
                    logger.info(f"📤 Envoyée à FarmBot à ({weed['x']}, {weed['y']})")
                except Exception as e:
                    logger.error(f"❌ Erreur d’envoi : {e}")

            # Séquence laser
            send_laser_sequence()
            logger.info("✅ Séquence de laserification exécutée")

            # Pause et recapture image après tir
            time.sleep(2)
            image_after, _ = detect_weeds()
            after_path = save_image(image_after, prefix="after", folder="images_archv/after")
            logger.info(f"💾 Image sauvegardée (après) : {after_path}")

        #  Délai entre deux positions
        time.sleep(DELAI_MOUVEMENT)

    logger.info("🏁 Scan terminé.")


if __name__ == "__main__":
    scan_area()