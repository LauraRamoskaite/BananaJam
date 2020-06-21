import random

import requests

# Input variable to ask the player how many rounds they want to play
number_of_rounds = int(input('How many rounds do you want to play? Please enter a whole number. '))

def random_pokemon ():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'moves': len(pokemon['moves']),
        'exp': pokemon['base_experience'],
        'abilities': len(pokemon['abilities']),
    }

outcome_list = []
number_of_wins = 0
number_of_losses = 0

def game_round ():

    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight, moves, exp, abilities) ')

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
        return "win"
    elif my_stat < opponent_stat:
        print('You Lose!')
        return "loss"
    else :
        print('Draw!')
        return "draw"

for round in range(number_of_rounds):
    print(f"Round {round + 1} of {number_of_rounds}")
    outcome = game_round()

    if outcome == 'win':
        number_of_wins = number_of_wins + 1
    if outcome == 'loss':
        number_of_losses = number_of_losses + 1

    outcome_list.append(outcome)

print(outcome_list)

print(f"You have {number_of_wins} wins and {number_of_losses} losses.")

if number_of_losses == number_of_wins:
    print("It's a tie!")
elif number_of_wins > number_of_losses:
    print("Congratulations, you won the game!")
else:
    print("Unfortuntely, you didn't win. Better luck next time!")


with open('game_outcomes.txt', 'w+') as text_file:
    results = str(outcome_list)
    message = f"Your game outcomes were as follows:\n{results}\nYou {number_of_wins} : {number_of_losses} Your Opponent"
    text_file.write(message)
    text_file.close()

print("You can view your results in game_outcomes.txt file.")