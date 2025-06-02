# auth.py

import os
import requests
from dotenv import load_dotenv

# Chargement du fichier .env
load_dotenv()

EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

def get_token():
    """
    Authentifie l’utilisateur auprès de l’API FarmBot
    et renvoie le token JWT complet (dictionnaire).
    """
    response = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {
            "email": EMAIL,
            "password": PASSWORD
        }
    })
    response.raise_for_status()
    return response.json()["token"]

def get_headers():
    """
    Renvoie les en-têtes d’authentification à utiliser dans les requêtes API.
    """
    token = get_token()
    return {"Authorization": f"Bearer {token}"}