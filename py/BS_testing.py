import requests

EMAIL = "trolions71@gmail.com"
PASSWORD = "farmbot21"

res = requests.post("https://my.farm.bot/api/tokens", json={
    "user": {
        "email": EMAIL,
        "password": PASSWORD
    }
})

print(res.status_code)
print(res.json())
