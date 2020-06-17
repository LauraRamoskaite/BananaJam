#hi
# Top Trumps project

import requests

import random

# Function to generate random pokemon ID
def random_pokemon_ID():
    random_integer = random.randint(1, 151)
    return random_integer

# Function to retrieve a pokemon based on random ID
def random_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_pokemon_ID())
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        }

# Variable that stores the dictionary of pokemon attributes for 1 random card
pokemon_card = random_pokemon()

# A list of cards used in game each saved as dictionary within a list
competing_cards = []

# Function that selects 2 random cards; one for the player, one for the opponent
def two_random_cards():
    for card in range(2):
        competing_cards.append(random_pokemon())

# Function that starts the game
def start_the_game():
    two_random_cards()
    print(competing_cards)

# Calling the function to generate two random cards
start_the_game()


#hello world
