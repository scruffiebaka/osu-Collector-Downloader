import requests

response = requests.get("https://catboy.best/d/148393")
print(response.status_code)