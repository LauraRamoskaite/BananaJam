# Top Trumps project

import random

import requests

# Function to generate random pokemon ID
def random_pokemon_ID():
    random_integer = random.randint(1, 151)

    return random_integer

# Function to retrieve a pokemon
def random_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_pokemon_ID())
    response = requests.get(url)
    pokemon = response.json()

    return {
         'name': pokemon['name'],}
#         'id': pokemon['id'],
#         'height': pokemon['height'],
#         'weight': pokemon['weight'],
#         }

print(random_pokemon())