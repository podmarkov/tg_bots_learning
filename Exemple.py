import requests

res = requests.get("https://api.thecatapi.com/v1/images/search")
print(res.json()[0]["url" if res.status_code == 200 else "Error: " + str(res.status_code)])