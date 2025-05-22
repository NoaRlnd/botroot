# Paramètres physiques et logiques de la grille (ajustés au bac FarmBot Express 1.1)
GRID_WIDTH = 6       # 1200 mm / 205 mm ≈ 6 colonnes
GRID_HEIGHT = 20     # 3000 mm / 151 mm ≈ 20 lignes
STEP_X = 205         # largeur réelle couverte par l'image (mm)
STEP_Y = 151         # hauteur réelle couverte par l'image (mm)
ORIGIN_X = 0         # point de départ en X
ORIGIN_Y = 0         # point de départ en Y
Z_HEIGHT = 0         # Hauteur Z par défaut (en mm, 0 = position home du Z)


def generate_grid_positions():
    """
    Génère une liste de tuples (x, y) correspondant aux positions 
    à scanner par le FarmBot selon une grille définie.
    """
    positions = []
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pos_x = ORIGIN_X + x * STEP_X
            pos_y = ORIGIN_Y + y * STEP_Y
            positions.append((pos_x, pos_y, Z_HEIGHT))
    return positions