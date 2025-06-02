import cv2
import uuid
import os
from datetime import datetime

# Détection de la racine du projet (dossier contenant 'images_archv')
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # revient à botroot/

def save_image(image, prefix="before", folder="images_archv/before"):
    """
    Sauvegarde une image avec un nom unique dans le dossier spécifié.
    Le chemin est toujours relatif à la racine du projet.
    """
    # 🔁 Recalcul du chemin complet à partir de la racine
    full_folder = os.path.join(PROJECT_ROOT, folder)
    os.makedirs(full_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    filename = f"{prefix}_{timestamp}_{unique_id}.jpg"
    filepath = os.path.join(full_folder, filename)

    success = cv2.imwrite(filepath, image)
    if not success:
        raise IOError(f"❌ Échec de la sauvegarde de l'image à {filepath}")

    return filepath