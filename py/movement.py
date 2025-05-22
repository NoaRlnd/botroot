
import json
import ssl
import threading
import time
import websocket
from dotenv import load_dotenv
import os
import requests

# Chargement des variables d'environnement depuis .env
load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

# Fonction d'authentification pour obtenir un token JWT
def get_token():
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {
            "email": EMAIL,
            "password": PASSWORD
        }
    })
    res.raise_for_status()
    return res.json()

# Authentification
print("📦 Test de petits déplacements du bras FarmBot...")
print(f"🔐 Email récupéré : {EMAIL}")
TOKEN = get_token()
jwt_token = TOKEN["token"]["encoded"]  # Token JWT (string)

# initialisation farmbot
import sys
import unittest
from farmbot import Farmbot
from unittest.mock import Mock, patch, call

fb = Farmbot()
fb.set_token(TOKEN)

# récup points et envoie log
points = fb.api_get('points') 
fb.log('rien qui marche', message_type='info')
# Envoi d'une requête GET à l'API pour récupérer les points

sequence_name = "laserification"
print(f"📤 Lancement de la séquence : {sequence_name}")
fb.sequence(sequence_name)
print(f"✅ Séquence {sequence_name} exécutée.")