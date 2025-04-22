from blob_scan import detect_weeds
from farmbot_status import get_current_position
import time

# --- Paramètres de la grille (ajustés au bac FarmBot Express 1.1) ---
GRID_WIDTH = 6   # 1200 mm / 205 mm ≈ 6
GRID_HEIGHT = 20  # 3000 mm / 151 mm ≈ 20
STEP_X = 205     # largeur réelle couverte par l'image
STEP_Y = 151     # hauteur réelle couverte par l'image

# Position d'origine du scan (coin haut-gauche du bac par exemple)
ORIGIN_X = 0
ORIGIN_Y = 0

# --- Fonction principale ---
def scan_area():
    positions = []

    # Générer les coordonnées de la grille
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pos_x = ORIGIN_X + x * STEP_X
            pos_y = ORIGIN_Y + y * STEP_Y
            positions.append((pos_x, pos_y))

    print(f"🔁 Démarrage du scan sur {len(positions)} positions...")

    for i, (x, y) in enumerate(positions):
        print(f"\n📍 Position {i+1}/{len(positions)} : X={x} mm, Y={y} mm")

        # À ce stade : on ne déplace pas le bras, on simule la position
        # Tu pourrais ici appeler une fonction de déplacement FarmBot API plus tard

        # Détection d'image (comme si on était à la position (x, y))
        image, weeds = detect_weeds()

        print(f"  -> {len(weeds)} mauvaise(s) herbe(s) détectée(s) à cette position")
        time.sleep(1)  # Pause entre les captures (pour simuler le temps de déplacement)

    print("\n✅ Scan terminé.")

if __name__ == "__main__":
    scan_area()