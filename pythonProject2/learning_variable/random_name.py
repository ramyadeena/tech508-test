import random
import requests

def get_random_pokemon():
    random_id = random.randint(1, 151)  # First generation
    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None