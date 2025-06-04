from flask import Flask, request, jsonify
from flask_cors import CORS
from movement import init_farmbot  # Utilise ton movement.py !
import os

app = Flask(__name__)
CORS(app)

# Variables pour la position simulée (mode manuel)
CURRENT_X = 0
CURRENT_Y = 0
CURRENT_Z = 0

@app.route('/api/move', methods=['POST'])
def api_move():
    global CURRENT_X, CURRENT_Y, CURRENT_Z
    data = request.json
    direction = data.get('direction', '')

    # On part de la position simulée
    x, y, z = CURRENT_X, CURRENT_Y, CURRENT_Z

    step = 10  # mm

    if direction == "Haut":
        y += step
    elif direction == "Bas":
        y -= step
    elif direction == "Gauche":
        x -= step
    elif direction == "Droite":
        x += step

    try:
        fb = init_farmbot()
        fb.move(x=x, y=y, z=z)
        CURRENT_X, CURRENT_Y, CURRENT_Z = x, y, z
        msg = f"Déplacement FarmBot vers : {direction} (x={x}, y={y}, z={z})"
        print(msg)
    except Exception as e:
        msg = f"Erreur déplacement FarmBot : {e}"
        print(msg)

    return jsonify({"message": msg})

@app.route('/api/reset', methods=['POST'])
def api_reset():
    global CURRENT_X, CURRENT_Y, CURRENT_Z
    try:
        fb = init_farmbot()
        fb.find_home()  # Home tous les axes
        CURRENT_X, CURRENT_Y, CURRENT_Z = 0, 0, 0
        msg = "Retour à la position home du FarmBot !"
        print(msg)
    except Exception as e:
        msg = f"Erreur reset FarmBot : {e}"
        print(msg)
    return jsonify({"message": msg})

@app.route('/api/laser', methods=['POST'])
def api_laser():
    data = request.json
    state = bool(data.get('state', False))
    try:
        fb = init_farmbot()
        if state:
            fb.sequence("laserification")  # On suppose que la séquence active le laser
            msg = "Séquence laser lancée sur le FarmBot !"
        else:
            # (optionnel : séquence d’arrêt, si existante)
            msg = "Laser désactivé (pas de séquence d’arrêt dédiée)"
        print(msg)
    except Exception as e:
        msg = f"Erreur contrôle laser FarmBot : {e}"
        print(msg)
    return jsonify({"message": msg})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)