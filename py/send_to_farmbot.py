import os
import json
import time
import ssl
import threading
import websocket
import requests
from dotenv import load_dotenv

# 🔧 Chargement du fichier .env contenant les identifiants
load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

# 🔐 Fonction d'authentification qui renvoie les données du token
def get_token():
    response = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {"email": EMAIL, "password": PASSWORD}
    })
    response.raise_for_status()
    return response.json()["token"]

# 📤 Prépare le message de déplacement
def make_move_command(x, y, z):
    return {
        "kind": "rpc_request",
        "args": {"label": "move_command"},
        "body": [{
            "kind": "move_absolute",
            "args": {
                "location": {"kind": "coordinate", "args": {"x": x, "y": y, "z": z}},
                "offset": {"x": 0, "y": 0, "z": 0},
                "speed": 100
            }
        }]
    }

# 💬 Callback : déclenché à l'ouverture du WebSocket
def on_open(ws):
    print("✅ Connexion WebSocket établie")
    
    def delayed_auth():
        time.sleep(1)
        print("🔐 Auth envoyé")
        auth_msg = {
            "kind": "authorization",
            "args": {"token": jwt}
        }
        ws.send(json.dumps(auth_msg))

        time.sleep(1.5)
        move_cmd = make_move_command(100, 100, -50)
        ws.send(json.dumps(move_cmd))
        print("📤 Mouvement envoyé")

        time.sleep(2)
        ws.close()

    threading.Thread(target=delayed_auth).start()

# 💬 Callback : message reçu
def on_message(ws, message):
    print("📩 Message reçu :", message)

# 💬 Callback : erreur sur la connexion
def on_error(ws, error):
    print("❌ Erreur WebSocket :", error)

# 💬 Callback : fermeture de la connexion
def on_close(ws, code, msg):
    print("🔌 Connexion WebSocket fermée")

# ▶️ Point d’entrée du script
print("📦 Test de petits déplacements du bras FarmBot...")
print(f"🔐 Email récupéré : {EMAIL}")

# 🧾 Récupération du token
token_data = get_token()
jwt = token_data["encoded"]
ws_url = token_data["unencoded"]["mqtt_ws"]  # ex: wss://xxxxx.rmq.cloudamqp.com:443/ws/mqtt

print("🌐 Connexion à WebSocket MQTT...")
# 🌐 Connexion WebSocket sécurisée avec protocole MQTT
ws = websocket.WebSocketApp(
    ws_url,
    subprotocols=["mqtt"],  # important pour FarmBot
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

# 🔒 Connexion sécurisée TLS/SSL
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})