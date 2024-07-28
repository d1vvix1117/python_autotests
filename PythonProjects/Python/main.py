import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '40ddf6d18474d832dee0f4c2d9a62c48'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}


body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change_pokemon = {
    "pokemon_id": "45236",
    "name": "d1vvi",
    "photo_id": 2
}

body_catch_pokeball = {
    "pokemon_id": "9"
}

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.json())


response_changepokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_pokemon)
print(response_changepokemon.json())

response_catch_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pokeball)
print(response_catch_pokeball.json())

