import random

import requests

# Input variable to ask the player how many rounds they want to play
number_of_rounds = int(input('How many rounds do you want to play? Please enter a whole number. '))

# Function that generates X random pokemons and stores their respective stats
def random_pokemon( number_of_pokemon ):

    # Lists that store the information about 4 random pokemons
    pokemon_number = []
    urls = []
    responses = []
    pokemon = []
    dictList = []


    # Generating X random numbers
    # Matching the X numbers to the corresponding URL in the Pokemon API
    # Pulling the correct URL for each random Pokemon
    # Retrieving all the available stats for those X random Pokemons
    # Putting all the stats that you're interested in about those X random Pokemons in a dictionary

    for i in range(0, number_of_pokemon):
        abc = random.randint(1, 151)
        pokemon_number.append(abc)
        urls.append('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number[i]))
        responses.append(requests.get(urls[i]))
        pokemon.append(responses[i].json())
        entry = {'name': pokemon[i]['name'],                    # name
                 'id': pokemon[i]['id'],                        # id
                 'height': pokemon[i]['height'],                # height
                 'weight': pokemon[i]['weight'],                # weight
                 'moves': len(pokemon[i]['moves']),             # moves
                 'experience': pokemon[i]['base_experience'],   # experience
                 'abilities': len(pokemon[i]['abilities']),     # abilities
                 }
        dictList.append(entry)
    return dictList


# Variables that store the outcomes of each game round
outcome_list = []
number_of_wins = 0
number_of_losses = 0


# Function that runs the game for 1 round
def game_round ():

    # Selecting one of the 4 random pokemons
    my_pokemons = random_pokemon(4)
    poke_names = []
    for j in range(0, 4):
        entry = my_pokemons[j]['name']
        poke_names.append(entry)

    print('You were given the following Pokemons - {}'.format(poke_names))
    poke_choice = input('Which one do you want to use? ')
    print('You have chosen {}'.format(poke_choice))


    input_translator = {
        '1': 'id',
        '2': 'height',
        '3': 'weight',
        '4': 'moves',
        '5': 'experience',
        '6': 'abilities',
    }


    # Lets you choose a stat to face the opponent and matches it to the corresponding Pokemon in the dictionary
    for k in my_pokemons:
        if k['name'] == poke_choice:
            k_index = my_pokemons.index(k)
            break
    stat_choice = input('Which stat do you want to use? (1: id, 2: height, 3: weight, 4: moves, 5: experience, 6: abilities)? Type 1-6 to choose your stat. ')
    my_stat = my_pokemons[k_index][ input_translator[stat_choice] ]


    opponent_pokemon = random_pokemon(1)[0]
    opponent_stat = opponent_pokemon[ input_translator[stat_choice] ] # same stat used for both players

    print(f"{poke_choice}'s {input_translator[stat_choice]} value is {my_stat}.")
    print(f"The opponent chose {opponent_pokemon['name']}. {opponent_pokemon['name']}'s {input_translator[stat_choice]} value is {opponent_stat}.")


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