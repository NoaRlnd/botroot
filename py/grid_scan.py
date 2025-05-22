from blob_scan import detect_weeds
from farmbot_status import get_current_position
from movement import move_to, run_laserification_sequence
from grid_coords import generate_grid_positions
from send_laser import send_laser_sequence

import time

# --- Paramètres de la grille (ajustés au bac FarmBot Express 1.1) ---
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
def scan_area():
    positions = generate_grid_positions() # Génère les coordonées de la grille à scanner depuis grid_coords.py

    print(f"🔁 Démarrage du scan sur {len(positions)} positions...\n")

    for i, (x, y, z) in enumerate(positions):
        print(f"📍 Position {i+1}/{len(positions)} : X={x} mm, Y={y} mm, Z={z} mm")

        if SIMULATION_MODE:
            print("🧪 Mode simulation : aucun déplacement réel")
        else:
            move_to(x, y, z)

        # Détection d'image simulée à la position (x, y)
        image, weeds = detect_weeds()
        print(f"  -> {len(weeds)} mauvaise(s) herbe(s) détectée(s) à cette position\n")

        if len(weeds) > 0 and not SIMULATION_MODE:
            print("📤 Envoi de la séquence de laserification...")
            send_laser_sequence()                                   # Envoie la séquence de laserification bien clean de send_laser.py
            print("✅ Séquence de laserification envoyée.")

        time.sleep(DELAI_MOUVEMENT)  # Pause entre les captures (pour simuler le temps de déplacement)

    print("✅ Scan terminé.")

if __name__ == "__main__":
    scan_area()