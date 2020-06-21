#hi
# Top Trumps project

#Function to ask the player how many rounds they want to play
number_of_rounds = input ('How many rounds do you want to play? ')
print('Lets start round no. 1 of ' + number_of_rounds)

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

stat_choice = input('Which stat do you want to use? (id, height, weight) ')

opponent_pokemon = random_pokemon()
print('The opponent chose {}'.format(opponent_pokemon[id, height, weight])#here the opponent needs to choose a random stat

my_stat = my_pokemon[stat_choice]
opponent_stat = opponent_pokemon[stat_choice]

if my_stat > opponent_stat:
    print('You Win!')
elif my_stat < opponent_stat:
    print('You Lose!')
else:
    print('Draw!')

#End of the game:
play_again = input('Do you want to try again? yes/no ').title()
    if play_again == 'yes'
    elif play_again == 'no'
    print ('Thanks for playing!')
    else:
    print('Invalid input, please try again!')
#hello world
