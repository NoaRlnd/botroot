# --- Mesures physiques du champ de vision (en mm)
real_width_mm = 205       # largeur physique vue par la caméra éstimée
real_height_mm = 151     # hauteur physique vue par la caméra estimée

# --- Résolution de l'image (en pixels)
img_width = 640
img_height = 480


def pixels_to_mm(x_pixel, y_pixel, img_width, img_height, real_width_mm, real_height_mm): # 
    scale_x = real_width_mm / img_width
    scale_y = real_height_mm / img_height
    x_mm = x_pixel * scale_x
    y_mm = y_pixel * scale_y
    return x_mm, y_mm
