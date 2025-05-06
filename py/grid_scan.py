from blob_scan import detect_weeds
from farmbot_status import get_current_position
from movement import move_to
import time

DELAI_MOUVEMENT = 2.0

# --- Paramètres de la grille (ajustés au bac FarmBot Express 1.1) ---
GRID_WIDTH = 6       # 1200 mm / 205 mm ≈ 6
GRID_HEIGHT = 20     # 3000 mm / 151 mm ≈ 20
STEP_X = 205         # largeur réelle couverte par l'image
STEP_Y = 151         # hauteur réelle couverte par l'image

ORIGIN_X = 0
ORIGIN_Y = 0
Z_HEIGHT = 0         # Hauteur fixe (à ajuster si besoin)

SIMULATION_MODE = True  # ⬅️ True = pas de mouvement réel, False = déplacement réel

# --- Fonction principale ---
def scan_area():
    positions = []

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pos_x = ORIGIN_X + x * STEP_X
            pos_y = ORIGIN_Y + y * STEP_Y
            positions.append((pos_x, pos_y))

    print(f"🔁 Démarrage du scan sur {len(positions)} positions...\n")

    for i, (x, y) in enumerate(positions):
        print(f"📍 Position {i+1}/{len(positions)} : X={x} mm, Y={y} mm")

        if SIMULATION_MODE:
            print("🧪 Mode simulation : aucun déplacement réel")
        else:
            move_to(x, y, Z_HEIGHT)
        
        # À ce stade : on ne déplace pas le bras, on simule la position
        # Tu pourrais ici appeler une fonction de déplacement FarmBot API plus tard

        # Détection d'image (comme si on était à la position (x, y))
        image, weeds = detect_weeds()

        print(f"  -> {len(weeds)} mauvaise(s) herbe(s) détectée(s) à cette position\n")
        time.sleep(DELAI_MOUVEMENT) # Pause entre les captures (pour simuler le temps de déplacement)

    print("✅ Scan terminé.")

if __name__ == "__main__":
    scan_area()