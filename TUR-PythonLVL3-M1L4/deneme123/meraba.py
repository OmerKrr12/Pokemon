import requests
url = "https://pokeapi.co/api/v2/pokemon/1"
x = requests.get(url)
data = x.json()

print(data["stats"][0]["base_stat"])