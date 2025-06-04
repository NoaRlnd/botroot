import os
import requests
from dotenv import load_dotenv
from farmbot import Farmbot

# Chargement des variables d'environnement
load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

def get_token():
    """
    Récupère un token JWT à partir des identifiants dans .env
    """
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {
            "email": EMAIL,
            "password": PASSWORD
        }
    })
    res.raise_for_status()
    return res.json()

def init_farmbot():
    """
    Initialise et retourne une instance authentifiée de Farmbot
    """
    token = get_token()
    fb = Farmbot()
    fb.set_token(token)
    return fb