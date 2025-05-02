import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3898a83826d66f8ac0094d226c31aa54'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "304634",
    "name": "gogo",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "304634"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
