import math

def distance(x1, y1, x2, y2):
    """Calcule la distance euclidienne entre 2 points (mm)"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 🔧 Exemple de test
x_weed = 100
y_weed = 150
x_plant = 120
y_plant = 160

d = distance(x_weed, y_weed, x_plant, y_plant)
print(f"Distance entre weed et plante : {d:.2f} mm")