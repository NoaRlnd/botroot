
import json
import ssl
import threading
import time
import websocket
from dotenv import load_dotenv
import os
import requests

# 📁 Chargement des variables d'environnement depuis .env
load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

# 🔐 Fonction d'authentification pour obtenir un token JWT
def get_token():
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {
            "email": EMAIL,
            "password": PASSWORD
        }
    })
    res.raise_for_status()
    return res.json()
# 🔑 Authentification
print("📦 Test de petits déplacements du bras FarmBot...")
print(f"🔐 Email récupéré : {EMAIL}")
TOKEN = get_token()


from farmbot import Farmbot

fb = Farmbot()
fb.set_token(TOKEN)

points = fb.api_get('points')
fb.log('test laserification', message_type='info')
fb.move(x=123, y=123, z=0)

# url = f'https:{TOKEN}/api/ai'
# headers = {'Authorization': 'Bearer ' + TOKEN,
#            'content-type': 'application/json'}
# payload = {
#     'prompt': 'write code',
#     'context_key': 'lua',
#     'sequence_id': 247148,
# }
# response = requests.post(url, headers=headers, json=payload, stream=True)
# for line in response.iter_lines():
#     print(line.decode('utf-8'))