from db_logger import log_image_metadata
import os

# Simule une image test
filename = "test_image_20240604.jpg"
x, y = 123, 456
type = "before"

try:
    log_image_metadata(filename, type, x, y)
    print("✅ Insertion test réussie dans la BDD.")
except Exception as e:
    print(f"❌ Erreur lors de l’insertion dans la BDD : {e}") 