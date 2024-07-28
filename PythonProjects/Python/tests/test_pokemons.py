import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '40ddf6d18474d832dee0f4c2d9a62c48'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '6655'


def test_status_code():
   response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
   assert response.status_code == 200

def test_part_of_response():
      response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
      assert response_get.json()["data"][0]['id'] == '6655'  


def test_status_code_trainers():
   response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
   assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '45505')])
def test_parametrize(key, value):
     response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
     assert response_parametrize.json()["data"][0][key] == value      


