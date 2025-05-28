import cv2
import uuid
import os
from datetime import datetime

def save_image(image, prefix="before", folder="images_archv/before"):
    """
    Sauvegarde une image avec un nom unique dans le dossier spécifié.
    :param image: L’image OpenCV (numpy array)
    :param prefix: Préfixe du nom de fichier (ex: "before", "after", "scan")
    :param folder: Dossier de destination (par défaut : images_archv/before)
    :return: Chemin d’accès complet de l’image enregistrée
    """
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    filename = f"{prefix}_{timestamp}_{unique_id}.jpg"
    filepath = os.path.join(folder, filename)

    success = cv2.imwrite(filepath, image)
    if not success:
        raise IOError(f"❌ Échec de la sauvegarde de l'image à {filepath}")

    return filepath