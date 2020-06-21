import random

import requests

#Generating 4 random numbers
def random_pokemon():
    pokemon_number = []
    for i in range(0,4):
        abc = random.randint(1, 151)
        pokemon_number.append(abc)
#Matching the 4 numbers to the corresponding URL in the Pokemon API
    urls = []
    for i in range(0,4):
        urls.append('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number[i]))
#Pulls the correct URL for each random Pokemon
    responses = []
    for i in range(0,4):
        responses.append(requests.get(urls[i]))
#Gives you all the available stats for those 4 random Pokemons
    pokemon = []
    for i in range(0,4):
        pokemon.append(responses[i].json())
#Puts all the stats that you're interested in about those 4 random Pokemons in a dictionary
    dictList = []
    for i in range(0,4):
        entry = {'name': pokemon[i]['name'],
                 'id': pokemon[i]['id'],
                 'height': pokemon[i]['height'],
                 'weight': pokemon[i]['weight'],}
        dictList.append(entry)
    return dictList

#Tells you which 4 Pokemons you can choose from and lets you choose 1
def run():
    my_pokemons = random_pokemon()
    poke_names= []
    for j in range(0,4):
        entry = my_pokemons[j]['name']
        poke_names.append(entry)
    print('You were given the following Pokemons - {}'.format(poke_names))
    poke_choice = input('Which one do you want to use? ')
    print('You have chosen {}'.format(poke_choice))
#Lets you choose a stat you want to use to face the opponent and matches it to the corresponding Pokemon in the dictionary
    for k in my_pokemons:
        if k['name'] == poke_choice:
            k_index=my_pokemons.index(k)
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    my_stat = my_pokemons[k_index][stat_choice]

#Give the opponent (the computer) 4 random Pokemons and chooses the first one to play with
    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon[0]['name']))
    opponent_stat = opponent_pokemon[0][stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')

run()
