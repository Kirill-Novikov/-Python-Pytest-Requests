import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3898a83826d66f8ac0094d226c31aa54'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '28160'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers/{TRAINER_ID}')
    assert response_get.json()["trainer_name"] == 'Кот Мурзик'
    


    