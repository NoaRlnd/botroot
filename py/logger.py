import logging
import os
from datetime import datetime

def init_logger(name="botroot"):
    """Initialise un logger avec fichier dans logs/ + affichage console"""

    # Crée le dossier logs/ s'il n'existe pas
    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Nom du fichier de log avec horodatage
    log_filename = datetime.now().strftime("botroot_%Y-%m-%d.log")
    log_path = os.path.join(log_dir, log_filename)

    # Création du logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Empêche la duplication des handlers
    if logger.hasHandlers():
        return logger

    # Format du log
    formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')

    # Handler fichier
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger