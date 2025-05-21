
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

# fb.move(x=123, y=123, z=0)

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

# Lancer séquence "laserification"
# def test_sequence(self):
#     '''Test sequence command'''
#     def exec_command():
#         self.fb.sequence('laserification')
#     self.send_command_test_helper(
#         exec_command,
#         expected_command={
#             'kind': 'execute',
#             'args': {'sequence_id': 247148},
#         },
#         extra_rpc_args={},
#         mock_api_response=[{'name': 'laserification', 'id': 247148}])

sequence_name = 'laserification'
kwargs = {
    'x': 123,
    'y': 123,
    'z': 0,
    'speed': 100,
    'tool_id': 1
}
def sequence(self, sequence_name, **kwargs):
    """Executes a predefined sequence."""
    return self.resources.sequence(sequence_name, **kwargs) # sauf que ce fdp ne marche pas
    print(f"Executing sequence: {sequence_name}")