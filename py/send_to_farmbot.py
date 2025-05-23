from farmbot import Farmbot

def send_weed_to_farmbot(fb: Farmbot, x_mm: float, y_mm: float, z_mm: float = 0.0, radius: float = 15.0):
    """
    Envoie une mauvaise herbe détectée au FarmBot via API.
    
    Args:
        fb (Farmbot): Instance de l'objet Farmbot déjà authentifiée.
        x_mm (float): Coordonnée X de la mauvaise herbe (en mm).
        y_mm (float): Coordonnée Y de la mauvaise herbe (en mm).
        z_mm (float): Coordonnée Z de la mauvaise herbe (par défaut 0).
        radius (float): Rayon de la mauvaise herbe détectée (en mm).
    """
    data = {
        "name": "weed",
        "plant_stage": "removed",  # ou "planned" si juste marqué sans intervention
        "x": x_mm,
        "y": y_mm,
        "z": z_mm,
        "radius": radius
    }

    fb.api_post("points", data)
    fb.log(f"🌱 Mauvaise herbe enregistrée à ({x_mm}, {y_mm})", message_type="info")
    fb.sequence("laserification")  # Déclenche la séquence de tir laser après enregistrement
    fb.log("🔫 Séquence laserification déclenchée", message_type="success")