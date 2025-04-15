from conversion_px_to_mm import pixels_to_mm

import cv2
import numpy as np
import requests

# Dimensions de l'image en pixels
img_width = 640
img_height = 480

# Dimensions physiques vues par la caméra (à ajuster selon tes mesures réelles)
real_width_mm = 300   # à remplacer par la valeur réelle
real_height_mm = 225  # pareil

# Adresse IP de votre ESP32-CAM (modifiez-la si besoin)
ESP32_URL = "http://192.168.218.245/capture" # URL de l'ESP32-CAM

# --- Fonctions ---
def get_image_from_esp32(url):
    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    return cv2.imdecode(image_array, cv2.IMREAD_COLOR)

def remove_border_noise(mask, margin=30):
    height, width = mask.shape
    mask[0:margin, :] = 0
    mask[-margin:, :] = 0
    mask[:, 0:margin] = 0
    mask[:, -margin:] = 0
    return mask

def detect_green_areas(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([37, 42, 42])
    upper_green = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    return mask

def get_green_contours(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours):
    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > 300:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)

            x_mm, y_mm = pixels_to_mm(
                center[0], center[1],
                img_width, img_height,
                real_width_mm, real_height_mm
            )

            print(f"Weed #{i+1} détectée à x={x_mm:.1f} mm, y={y_mm:.1f} mm")

            cv2.circle(image, center, radius, (0, 255, 0), 2)
            cv2.putText(image, f"Weed #{i+1}", (center[0] - 30, center[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

def detect_weeds():
    image = get_image_from_esp32(ESP32_URL)
    mask = detect_green_areas(image)
    mask = remove_border_noise(mask)
    contours = get_green_contours(mask)

    weeds = []
    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > 300:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)

            x_mm, y_mm = pixels_to_mm(
                center[0], center[1],
                img_width, img_height,
                real_width_mm, real_height_mm
            )

            weeds.append({
                "x": x_mm,
                "y": y_mm,
                "z": 0,
                "radius": radius
            })

    return image, weeds