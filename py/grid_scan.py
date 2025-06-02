from blob_scan import detect_weeds
from farmbot_status import get_current_position
from movement import move_to, run_laserification_sequence
from grid_coords import generate_grid_positions
from send_laser import send_laser_sequence
from send_to_farmbot import send_weed_to_farmbot
from logger import init_logger  
from db_logger import log_image_metadata                               
from image_capture import save_image 
from plant_filter import filter_weeds_against_plants
from auth import get_headers                                        # la plupart des imports sont inutiles (peut être ?)


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
SIMULATION_MODE = False  # True = pas de mouvement réel, False = déplacement réel

# --- Fonction principale ---
logger = init_logger()
headers = get_headers()

def scan_area():
    positions = generate_grid_positions()  # Génère les coordonnées de la grille à scanner depuis grid_coords.py
    total = len(positions)
    logger.info(f"🔁 Démarrage du scan sur {total} positions...\n")

    for i, (x, y, z) in enumerate(positions):
        logger.info(f"📍 Position {i+1}/{total} : X={x} mm, Y={y} mm, Z={z} mm")

        if SIMULATION_MODE:
            logger.info("🧪 Mode simulation : aucun déplacement réel")
        else:
            try:
                move_to(x, y, z)  # Déplacement vers la position (x, y, z)
            except Exception as e:
                logger.error(f"❌ Erreur de déplacement : {e}")
                continue

        # Détection d'image simulée à la position (x, y)
        image, weeds = detect_weeds()

        # Filtrage des mauvaises herbes selon la position des plantes
        filtered_weeds = filter_weeds_against_plants(weeds, headers)

        logger.info(f"  -> {len(weeds)} mauvaise(s) herbe(s) détectée(s)")
        logger.info(f"  -> {len(filtered_weeds)} mauvaise(s) herbe(s) gardée(s) après filtrage par spread\n")

        # Envoi des données pour chaque mauvaise herbe gardée
        if not SIMULATION_MODE and filtered_weeds:
            for weed in filtered_weeds:
                try:
                    send_weed_to_farmbot(weed["x"], weed["y"])
                    logger.info(f"📤 Mauvaise herbe envoyée à ({weed['x']}, {weed['y']})")
                except Exception as e:
                    logger.error(f"❌ Erreur d'envoi de mauvaise herbe : {e}")

            # Sauvegarde de l'image avant
            image_path = save_image(image, prefix="before", folder="images_archv/before")
            log_image_metadata(os.path.basename(image_path), "before", x, y)
            logger.info(f"💾 Image avant tir sauvegardée : {image_path}")

            # Séquence de laserification
            send_laser_sequence()
            logger.info("✅ Séquence de laserification envoyée.")

            # Image après traitement
            time.sleep(2)
            image_after, _ = detect_weeds()
            after_path = save_image(image_after, prefix="after", folder="images_archv/after")
            logger.info(f"💾 Image après tir sauvegardée : {after_path}")

        time.sleep(DELAI_MOUVEMENT)

    logger.info("✅ Scan terminé.")


if __name__ == "__main__":
    scan_area()