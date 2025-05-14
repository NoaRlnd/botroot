
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
    return res.json()["token"]

# 🔑 Authentification
print("📦 Test de petits déplacements du bras FarmBot...")
print(f"🔐 Email récupéré : {EMAIL}")
token_data = get_token()
jwt_token = token_data["encoded"]
mqtt_ws_url = token_data["unencoded"]["mqtt_ws"]
device = token_data["unencoded"]["bot"]
print("✅ Authentification réussie.")

# 📤 Message de mouvement à envoyer
move_message = {
    "kind": "rpc_request",
    "args": {"label": "move_ws"},
    "body": [{
        "kind": "move_absolute",
        "args": {
            "location": {
                "kind": "coordinate",
                "args": {"x": 100, "y": 100, "z": -50}
            },
            "offset": {"x": 0, "y": 0, "z": 0},
            "speed": 100
        }
    }]
}

# 🧠 Fonction exécutée une fois la connexion WebSocket ouverte
def on_open(ws):
    print("✅ Connexion WebSocket établie")
    auth_msg = json.dumps({
        "kind": "authorization",
        "args": {"token": jwt_token}
    })
    ws.send(auth_msg)
    print("🔐 Auth envoyé")
    
    def delayed_move():
        time.sleep(1)
        ws.send(json.dumps(move_message))
        print("📤 Mouvement envoyé")
        time.sleep(2)
        ws.close()
    
    threading.Thread(target=delayed_move).start()

# 🛠 Fonctions de gestion des erreurs et de fermeture
def on_error(ws, error):
    print("❌ Erreur WebSocket :", error)

def on_close(ws, close_status_code, close_msg):
    print("🔌 Connexion WebSocket fermée")

# 🚀 Connexion au serveur WebSocket
print("🌐 Connexion à WebSocket MQTT...")
ws = websocket.WebSocketApp(
    mqtt_ws_url,
    subprotocols=["mqtt"],
    on_open=on_open,
    on_error=on_error,
    on_close=on_close
)

# 🔒 Sécurité SSL pour la connexionimport requests
import json
import ssl
import websocket
import os
import time
from dotenv import load_dotenv

# 📁 Chargement des variables d'environnement depuis le fichier .env
load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

# 🔐 Fonction pour obtenir un token JWT depuis l'API REST de FarmBot
def get_token():
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {
            "email": EMAIL,
            "password": PASSWORD
        }
    })
    res.raise_for_status()
    return res.json()["token"]

# 🟢 Authentification
print("📦 Test de petits déplacements du bras FarmBot...")
print(f"🔐 Email récupéré : {EMAIL}")
token_data = get_token()
jwt_token = token_data["encoded"]
device_name = token_data["unencoded"]["bot"]
ws_url = token_data["unencoded"]["mqtt_ws"]
print("✅ Authentification réussie.")

# 🤖 Commande de mouvement à envoyer
move_message = {
    "kind": "rpc_request",
    "args": {"label": "move_test"},
    "body": [{
        "kind": "move_absolute",
        "args": {
            "location": {
                "kind": "coordinate",
                "args": {"x": 100, "y": 100, "z": -50}
            },
            "offset": {"x": 0, "y": 0, "z": 0},
            "speed": 100
        }
    }]
}

# 📡 Fonction appelée dès que la connexion WebSocket est ouverte
def on_open(ws):
    print("✅ Connexion WebSocket établie")

    # 🔐 Envoi du message d'autorisation
    auth_msg = json.dumps({
        "kind": "authorization",
        "args": {"token": jwt_token}
    })
    ws.send(auth_msg)
    print("🔐 Auth envoyé")

    # ⏳ Délai pour que le serveur traite l'autorisation
    time.sleep(1)

    # 📤 Envoi de la commande de mouvement
    ws.send(json.dumps(move_message))
    print("📤 Mouvement envoyé")

    # ⏳ Délai pour laisser le serveur exécuter le mouvement avant fermeture
    time.sleep(2)
    ws.close()

# 🔁 Autres callbacks WebSocket
def on_message(ws, message):
    print("📩 Message reçu :", message)

def on_error(ws, error):
    print("❌ Erreur WebSocket :", error)

def on_close(ws, close_status_code, close_msg):
    print("🔌 Connexion WebSocket fermée")

# 🌐 Connexion WebSocket MQTT (protocole FarmBot)
print("🌐 Connexion à WebSocket MQTT...")
ws = websocket.WebSocketApp(
    ws_url,
    subprotocols=["mqtt"],  # important pour FarmBot
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    header={"Authorization": f"Bearer {jwt_token}"}
)

# 🔒 Lancement de la connexion sécurisée
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})