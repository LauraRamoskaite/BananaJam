#hi
# Top Trumps project
import requests

import random

# Input variable to ask the player how many rounds they want to play
number_of_rounds = int(input('How many rounds do you want to play? Please enter a whole number. '))


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
def two_random_cards(cards):
    for card in range(2):
        cards.append(random_pokemon())
    return cards

# Function that starts the game
def start_the_game():
    competing_cards = two_random_cards(competing_cards)
    print(competing_cards)

# Calling the function to generate two random cards
for round in range(number_of_rounds):
    print(f"Round {round + 1} of {number_of_rounds}")
    start_the_game()


#hello world
