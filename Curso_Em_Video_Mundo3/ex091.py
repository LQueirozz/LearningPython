#CHALLENGE 91: Dice game
#GOAL: Write code that generates a dice roll for 4 players and store it in a dictionary, then rank the players according to their number
#SKILL: Learning about dictionaries

from random import randint
from time import sleep

dice={'Player 1': randint(1,6), 'Player 2':randint(1,6), 'Player 3':randint(1,6), 'Player 4':randint(1,6)}
for key, value in dice.items():
    print(f'{key} rolled {value}')
    sleep(0.5)

diceV=dict(sorted(dice.items(), key=lambda item:item[1] ,reverse=True) )

i=1
for key, value in diceV.items():
    print(f'{i}º place: {key} who rolled {value}')
    i+=1
    sleep(0.5)