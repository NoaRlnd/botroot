import requests

EMAIL = "numerique@association-ore.fr"
PASSWORD = "Fablab@0r3"

res = requests.post("https://my.farm.bot/api/tokens", json={
    "user": {
        "email": EMAIL,
        "password": PASSWORD
    }
})

print(res.status_code)
print(res.json())
