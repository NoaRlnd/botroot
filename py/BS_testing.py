# import requests

# EMAIL = "numerique@association-ore.fr"
# PASSWORD = "Fablab@0r3"

# res = requests.post("https://my.farm.bot/api/tokens", json={
#     "user": {
#         "email": EMAIL,
#         "password": PASSWORD
#     }
# })

# print(res.status_code)
# print(res.json())

# La version du dessus fonctionne aussi mais est moins élaborée

import requests
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("FARMBOT_EMAIL")
PASSWORD = os.getenv("FARMBOT_PASSWORD")

print("EMAIL:", EMAIL)
print("PASSWORD:", PASSWORD)

res = requests.post("https://my.farm.bot/api/tokens", json={
    "user": {"email": EMAIL, "password": PASSWORD}
})
print(res.status_code)
print(res.text)