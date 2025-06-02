import numpy as np
import cv2
from image_capture import save_image

# Créer une image factice 480x640 pixels, noire
dummy_image = np.zeros((480, 640, 3), dtype=np.uint8)

# Ajouter du texte dessus pour la différencier
cv2.putText(dummy_image, 'Test Image', (50, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Sauvegarde avec prefix "test" dans le dossier "images_archv/before"
try:
    saved_path = save_image(dummy_image, prefix="test", folder="images_archv/before")
    print(f"✅ Image enregistrée avec succès : {saved_path}")
except Exception as e:
    print(f"❌ Erreur lors de la sauvegarde : {e}")