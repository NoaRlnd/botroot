def generate_grid_positions():
    """
    Génère une mini grille de test 2x3 avec STEP_X=205, STEP_Y=151, Z fixe à 0
    """
    step_x = 205
    step_y = 151
    origin_x = 0
    origin_y = 0
    z_height = 0

    width = 2
    height = 3

    positions = []
    for i in range(height):
        for j in range(width):
            x = origin_x + j * step_x
            y = origin_y + i * step_y
            positions.append((x, y, z_height))

    return positions
