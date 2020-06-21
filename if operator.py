import math
import random
import time
toon_list = [] #Python Lang
player_deck = []
cpu_deck = []
class character:
       def __init__(self, name, health, stamina, morality, strength, height, will):
               self.name = name
               self.health = health
               self.stamina = stamina
               self.morality = morality
               self.strength = strength
               self.height = height
               self.will = will
               toon_list.append(self)
########################################################################Character definitions
vader = character('Darth Vader’, 85, 30, 40, 75, 80, 40)
finn = character('Finn’, 80, 80, 95, 90, 60, 80)
gandalf = character('Gandalf’, 75, 50, 100, 65, 90, 70)
tony_stark = character('Iron Man’, 85, 90, 90, 85, 60, 10)
batman = character('Batman’, 90, 90, 90, 80, 80, 10)
joker = character('The Joker’, 70, 90, 30, 40, 80, 50)
two_face = character('Two Face’, 70, 70, 50, 70, 80, 60)
superman = character('Superman’, 90, 90, 90, 90, 90, 90)
wonder_woman = character('Wonder Woman’, 80, 75, 90, 80, 70, 95)
spider_man = character('Spider Man’, 70, 90, 70, 70, 80, 90)
all_cards = {'Darth Vader’:vader, 'Vader':vader, 'vader’:vader, 'Finn’:finn, 'finn’:finn, 'White Wizard’:gandalf,
            'white wizard’:gandalf, 'Stark’:tony_stark, 'Tony Stark’:tony_stark, 'Tony’:tony_stark, 'Iron man’:tony_stark,
            'iron man’:tony_stark, 'gandalf’:gandalf, 'Gandalf’:gandalf, 'Batman’:batman, 'Bat man’:batman,
            'Bat Man’:batman, 'BatMan’:batman, 'Bruce Wayne’:batman, 'bruce wayne’:batman, 'The Joker’:joker,
            'the joker’:joker, 'joker’:joker, 'Joker’:joker, 'Two Face’:two_face, 'two face’:two_face,
            'Harvey Dent’:two_face, 'harvey dent’:two_face, 'Twoface’:two_face, 'TwoFace’:two_face, 'superman’:superman,
            'Superman’:superman, 'super man’:superman, 'Super Man’:superman, 'Super man’:superman, 'Wonder Woman’:wonder_woman,
            'wonder woman’:wonder_woman, 'Wonderwoman’:wonder_woman, 'WonderWoman’:wonder_woman, 'Spider Man’:spider_man, 'spider man’:spider_man,
            'Spiderman’:spider_man}
########################################################################Print character stats
cpu_index = ['health’, 'stamina’, 'morality’, 'strength’, 'height’, 'will’]
def print_all_toon_stats(deck):
       print (“*****************************************************************************************************************************************”)
       print (“* Name ********* Health ********* Stamina ********* Morality ********* Strength ********* Height ********* Will**”)
       print (“—————————————————————————————————————————————–”)
       for toon in deck:
               col_1 = “*************”
               col_1 = col_1.replace(“*”, toon.name + “ ”,1)
               col_1 = col_1[:14]
               col_2 = “**************”
               col_2 = col_2.replace(“*”, str(toon.health) + “ ”,1)
               col_2 = col_2[:16]
               col_3 = “*******************************************”
               col_3 = col_3.replace(“*”, str(toon.stamina) + “ ”,1)
               col_3 = col_3[:17]
               col_4 = “**************************”
               col_4 = col_4.replace(“*”, str(toon.morality) + “ ”,1)
               col_4 = col_4[:18]
               col_5 = “****************”
               col_5 = col_5.replace(“*”, str(toon.strength) + “ ”,1)
               col_5 = col_5[:18]
               col_6 = “****************************”
               col_6 = col_6.replace(“*”, str(toon.height) + “ ”,1)
               col_6 = col_6[:16]
               col_7 = “**************”
               col_7 = col_7.replace(“*”, str(toon.will) + “ ”,1)
               col_7 = col_7[:10]
               data_length = (len(toon.name) + len(str(toon.health)) + len(str(toon.stamina)) + len(str(toon.morality)) + len(str(toon.strength)) + len(str(toon.height)) + len(str(toon.will)))
               print (“*”, col_1 + “|” + col_2, col_3, col_4, col_5, col_6, col_7)
               print (“ ”)
########################################################################Player 1 character selections
def player_card_picker():
       def player_1_pick():
               player_1_pick = input(“Select a character to fight!”)
               return str(player_1_pick)
       card_picked = False
       while card_picked == False:
               player_1_pick = player_1_pick()
               if player_1_pick in all_cards:
                       player_1_pick = all_cards[player_1_pick]
                       if player_1_pick in player_deck:
                               card_picked = True
                       else:
                               pass
               else:
                       print (“Invalid card. Please re-enter”)
#######################################################################Random card selection
def cpu_card_picker():
       random_1_pick = random.choice(cpu_deck)
       return random_1_pick
#######################################################################Randomly assign cards to deck
def random_asign(deck):
       if len(toon_list) == 0:
               print (“Pack out of cards”)
       else:
               while len(deck) < 5:
                       temp = random.choice(toon_list)
                       if temp in deck:
                               pass
                       else:
                               deck.append(temp)
                               toon_list.remove(temp)
               if deck == player_deck:
                       print (“Your deck updated: ”)
                       print (deck[0].name, “|”, deck[1].name, “|”, deck[2].name, “|”, deck[3].name, “|”, deck[4].name, “|”)
#######################################################################Player terms
#######################################################################Game initialisation
game_started = False
turn_count = 0
while game_started == False:
       random_asign(cpu_deck)
       random_asign(player_deck)
       game_started = True
       print (“START”)
       player_turn = True
       while len(player_deck) > 0 and len(cpu_deck) > 0:
               turn_count += 1
               current_card = random.choice(player_deck)
               cpu_current_card = random.choice(cpu_deck)
               if player_turn == True:
                       print (“”)
                       print (“YOU’RE NOW PLAYING WITH”, (current_card.name).upper() + “!”)
                       print (“*********************************************************************************************************************”)
                       print (“* Name ********* Health ********* Stamina ********* Morality ********* Strength ********* Height ********* Will******”)
                       print (“———————————————————————————————————————”)
                       col_1 = “*************”
                       col_1 = col_1.replace(“*”, current_card.name + “ ”,1)
                       col_1 = col_1[:14]
                       col_2 = “**************”
                       col_2 = col_2.replace(“*”, str(current_card.health) + “ ”,1)
                       col_2 = col_2[:16]
                       col_3 = “*******************************************”
                       col_3 = col_3.replace(“*”, str(current_card.stamina) + “ ”,1)
                       col_3 = col_3[:17]
                       col_4 = “**************************”
                       col_4 = col_4.replace(“*”, str(current_card.morality) + “ ”,1)
                       col_4 = col_4[:18]
                       col_5 = “****************”
                       col_5 = col_5.replace(“*”, str(current_card.strength) + “ ”,1)
                       col_5 = col_5[:18]
                       col_6 = “****************************”
                       col_6 = col_6.replace(“*”, str(current_card.height) + “ ”,1)
                       col_6 = col_6[:16]
                       col_7 = “**************”
                       col_7 = col_7.replace(“*”, str(current_card.will) + “ ”,1)
                       col_7 = col_7[:10]
                       print (“*”, col_1 + “|” + col_2, col_3, col_4, col_5, col_6, col_7)
                       print (“ ”)
                       class_selected = False
                       while class_selected == False:
                               current_class = (input(“What will you battle with?”)).lower()
                               if current_class == 'health’ or current_class == 'Health’:
                                       current_battle_stat = current_card.health
                                       class_selected = True
                               elif current_class == 'stamina’ or current_class == 'Stamina’:
                                       current_battle_stat = current_card.stamina
                                       class_selected = True
                               elif current_class == 'morality’ or current_class == 'Morality’:
                                       current_battle_stat = current_card.morality
                                       class_selected = True
                               elif current_class == 'strength’ or current_class == 'Strength’:
                                       current_battle_stat = current_card.strength
                                       class_selected = True
                               elif current_class == 'stamina’ or current_class == 'Stamina’:
                                       current_battle_stat = current_card.stamina
                                       class_selected = True
                               elif current_class == 'height’ or current_class == 'Height’:
                                       current_battle_stat = current_card.height
                                       class_selected = True
                               elif current_class == 'will’ or current_class == 'Will’:
                                       current_battle_stat = current_card.will
                                       class_selected = True
                               else:
                                       pass
                       cpu_class_selected = False
                       while cpu_class_selected == False:
                               cpu_current_class = current_class
                               if cpu_current_class == 'health’ or cpu_current_class == 'Health’:
                                       cpu_current_battle_stat = cpu_current_card.health
                                       cpu_class_selected = True
                               elif cpu_current_class == 'stamina’ or cpu_current_class == 'Stamina’:
                                       cpu_current_battle_stat = cpu_current_card.stamina
                                       cpu_class_selected = True
                               elif cpu_current_class == 'morality’ or cpu_current_class == 'Morality’:
                                       cpu_current_battle_stat = cpu_current_card.morality
                                       cpu_class_selected = True
                               elif cpu_current_class == 'strength’ or cpu_current_class == 'Strength’:
                                       cpu_current_battle_stat = cpu_current_card.strength
                                       cpu_class_selected = True
                               elif cpu_current_class == 'stamina’ or cpu_current_class == 'Stamina’:
                                       cpu_current_battle_stat = cpu_current_card.stamina
                                       cpu_class_selected = True
                               elif cpu_current_class == 'height’ or cpu_current_class == 'Height’:
                                       cpu_current_battle_stat = cpu_current_card.height
                                       cpu_class_selected = True
                               elif cpu_current_class == 'will’ or cpu_current_class == 'Will’:
                                       cpu_current_battle_stat = cpu_current_card.will
                                       cpu_class_selected = True
                               else:
                                       pass
                       print (current_card.name, “has”, current_battle_stat, current_class.capitalize())
                       print (“”)
                       print (“”)
                       print (“************************”, (current_card.name).upper(), “(” + str(current_battle_stat) + “)”,“VS”, (cpu_current_card.name).upper(), “(” + str(cpu_current_battle_stat) + “)”, “************************”)
                       print (“”)
                       print (“”)
                       time.sleep(2)
               elif player_turn == False:
                       cpu_current_battle_stat = 0
                       cpu_current_class = 0
                       for x in cpu_index:
                               if x == 'health’:
                                       if cpu_current_card.health > cpu_current_battle_stat:
                                               cpu_current_battle_stat = cpu_current_card.health
                                               current_battle_stat = current_card.health
                                               current_class = x
                               if x == 'stamina’:
                                       if cpu_current_card.stamina > cpu_current_battle_stat:
                                               cpu_current_battle_stat = cpu_current_card.stamina
                                               current_battle_stat = current_card.stamina
                                               current_class = x
                               if x == 'morality’:
                                       if cpu_current_card.morality > cpu_current_battle_stat:
                                               cpu_current_battle_stat = cpu_current_card.morality
                                               current_battle_stat = current_card.morality
                                               current_class = x
                               if x == 'strength’:
                                       if cpu_current_card.strength > cpu_current_battle_stat:
                                               cpu_current_battle_stat = cpu_current_card.strength
                                               current_battle_stat = current_card.strength
                                               current_class = x
                               if x == 'height’:
                                       if cpu_current_card.height > cpu_current_battle_stat:
                                               cpu_current_battle_stat = cpu_current_card.height
                                               current_battle_stat = current_card.height
                                               current_class = x
                               if x == 'will’:
                                       if cpu_current_card.will > cpu_current_battle_stat:
                                               cpu_current_battle_stat = cpu_current_card.will
                                               current_battle_stat = current_card.will
                                               current_class = x
                       print (“”)
                       print (“YOU’RE NOW PLAYING WITH”, (current_card.name).upper() + “!”)
                       print (“*********************************************************************************************************************”)
                       print (“* Name ********* Health ********* Stamina ********* Morality ********* Strength ********* Height ********* Will******”)
                       print (“———————————————————————————————————————”)
                       col_1 = “*************”
                       col_1 = col_1.replace(“*”, current_card.name + “ ”,1)
                       col_1 = col_1[:14]
                       col_2 = “**************”
                       col_2 = col_2.replace(“*”, str(current_card.health) + “ ”,1)
                       col_2 = col_2[:16]
                       col_3 = “*******************************************”
                       col_3 = col_3.replace(“*”, str(current_card.stamina) + “ ”,1)
                       col_3 = col_3[:17]
                       col_4 = “**************************”
                       col_4 = col_4.replace(“*”, str(current_card.morality) + “ ”,1)
                       col_4 = col_4[:18]
                       col_5 = “****************”
                       col_5 = col_5.replace(“*”, str(current_card.strength) + “ ”,1)
                       col_5 = col_5[:18]
                       col_6 = “****************************”
                       col_6 = col_6.replace(“*”, str(current_card.height) + “ ”,1)
                       col_6 = col_6[:16]
                       col_7 = “**************”
                       col_7 = col_7.replace(“*”, str(current_card.will) + “ ”,1)
                       col_7 = col_7[:10]
                       print (“*”, col_1 + “|” + col_2, col_3, col_4, col_5, col_6, col_7)
                       print (“ ”)
                       print (current_card.name, “has”, current_battle_stat, current_class.capitalize())
                       print (“”)
                       print (“”)
                       print (“************************”, (current_card.name).upper(), “(” + str(current_battle_stat) + “)”,“VS”, (cpu_current_card.name).upper(), “(” + str(cpu_current_battle_stat) + “)”, “************************”)
                       print (“”)
                       print (“”)
                       time.sleep(2)
               if current_battle_stat > cpu_current_battle_stat:
                       print ((current_card.name).upper(), “WINS!”)
                       time.sleep(2)
                       player_turn = True
                       player_deck.append(cpu_current_card)
                       cpu_deck.remove(cpu_current_card)
               elif current_battle_stat < cpu_current_battle_stat:
                       print ((cpu_current_card.name).upper(), “WINS!”)
                       time.sleep(2)
                       player_turn = False
                       cpu_deck.append(current_card)
                       player_deck.remove(current_card)
               else:
                       print (“BOTH HERO’S LIVE TO FIGHT ANOTHER DAY!”)
                       time.sleep(2)
               print (“CPU has”, len(cpu_deck), “cards left!”)
               print (“You have”, len(player_deck), “cards left!”)
               if current_battle_stat > cpu_current_battle_stat:
                       print (“”)
                       print (“”)
                       print (“##############”)
                       print (“###HAND WON###”)
                       print (“##############”)
                       print (“”)
                       print (“”)
               elif current_battle_stat < cpu_current_battle_stat:
                       print (“”)
                       print (“”)
                       print (“###############”)
                       print (“###HAND LOST###”)
                       print (“###############”)
                       print (“”)
                       print (“”)
               else:
                       print (“”)
                       print (“”)
                       print (“###############”)
                       print (“###HAND DRAW###”)
                       print (“###############”)
                       print (“”)
                       print (“”)
               time.sleep(2.0)
       if len(cpu_deck) == 0:
               print (“*****************************************************************************************************************************************”)
               print (“**************************************************************         ******************************************************************”)
               print (“************************************************************** YOU WIN ******************************************************************”)
               print (“**************************************************************         ******************************************************************”)
               print (“*****************************************************************************************************************************************”)
       else:
               print (“*****************************************************************************************************************************************”)
               print (“**************************************************************          *****************************************************************”)
               print (“************************************************************** YOU LOSE *****************************************************************”)
               print (“**************************************************************          *****************************************************************”)
               print (“*****************************************************************************************************************************************”)
       print(“”)
       for x in player_deck:
               toon_list.append(x)
               player_deck.remove(x)
       for x in cpu_deck:
               toon_list.append(x)
               cpu_deck.remove(x)
       Valid = False
       while Valid == False:
               play_again = input(“Would you like to play again?”)
               if play_again == 'Yes’ or play_again == 'yes’ or play_again == 'y’ or play_again == 'Y’:
                       game_started = False
                       Valid = True
               elif play_again == 'No’ or play_again == 'no’ or play_again == 'n’ or play_again == 'N’:
                       print (“Thanks for playing!!”)
                       Valid = True
                       continue
               else:
                       print (“Invalid input, please try again!”)