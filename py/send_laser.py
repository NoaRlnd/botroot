from farmbot import Farmbot
from dotenv import load_dotenv
import os
import requests

# 🔐 Authentification avec FarmBot API
load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

def send_laser_sequence():
    res = requests.post("https://my.farm.bot/api/tokens", json={
        "user": {"email": EMAIL, "password": PASSWORD}
    })
    res.raise_for_status()
    token = res.json()

    fb = Farmbot()
    fb.set_token(token)
    fb.sequence("laserification")