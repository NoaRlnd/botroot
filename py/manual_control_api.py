from flask import Flask, request, jsonify
from flask_cors import CORS
from movement import init_farmbot  # Doit retourner l'instance fb, voir ton movement.py

app = Flask(__name__)
CORS(app)  # Autorise les appels depuis le frontend JS

# Instance unique de Farmbot (évite la reconnexion à chaque clic)
fb = init_farmbot()

# @app.route("/api/move", methods=["POST"])
# def move():
#     data = request.get_json()
#     if not data or "direction" not in data:
#         return jsonify({"status": "error", "message": "Direction non fournie"}), 400
#     direction = data.get("direction")
#     try:
#         # Ici tu adaptes la logique selon la commande envoyée (ex: 'Haut', 'Bas', etc.)
#         step = 20  # mm à chaque déplacement, adapte à ton usage
#         pos = {"Haut": (0, step), "Bas": (0, -step), "Droite": (step, 0), "Gauche": (-step, 0)}
#         if direction in pos:
#             x_delta, y_delta = pos[direction]
#             # Récupère la position actuelle, puis bouge (exemple basique)
#             current = fb.api_get('device')['body']['location_data']['position']
#             status = fb.api_get("status")
#             print("===== STATUS:", status)
#             pos = status.get("location_data", {}).get("position", {})
#             x = pos.get("x", 0)
#             y = pos.get("y", 0)
#             z = pos.get("z", 0)
#             print(f"Coords trouvées : x={x}, y={y}, z={z}")
#             fb.move(x=x + x_delta, y=y + y_delta, z=z)
#             return jsonify({"status": "ok", "message": f"Bras déplacé vers {direction}"})
#         else:
#             return jsonify({"status": "error", "message": "Direction inconnue"}), 400
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/move", methods=["POST"])
def move():
    data = request.get_json()
    if not data or "direction" not in data:
        return jsonify({"status": "error", "message": "Direction non fournie"}), 400
    direction = data.get("direction")
    try:
        step = 20  # mm à chaque déplacement, adapte à ton usage
        pos_delta = {"Haut": (0, step), "Bas": (0, -step), "Droite": (step, 0), "Gauche": (-step, 0)}
        if direction in pos_delta:
            x_delta, y_delta = pos_delta[direction]
            # ===== Correction ici !
            status = fb.api_get("status")
            print("===== STATUS:", status)
            pos = status.get("location_data", {}).get("position", {})
            x = pos.get("x", 0)
            y = pos.get("y", 0)
            z = pos.get("z", 0)
            print(f"Coords trouvées : x={x}, y={y}, z={z}")
            fb.move(x=x + x_delta, y=y + y_delta, z=z)
            return jsonify({"status": "ok", "message": f"Bras déplacé vers {direction}"})
        else:
            return jsonify({"status": "error", "message": "Direction inconnue"}), 400
    except Exception as e:
        print("Erreur attrapée :", e)
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)