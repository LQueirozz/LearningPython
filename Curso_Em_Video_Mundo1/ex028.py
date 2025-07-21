#CHALLENGE 28: Simple guessing game
#GOAL: Write code that comes up with a random number between 0 and 5 and has the user guess it
#SKILL: Learning about conditionals

from random import randint

n= randint(0,5)
g= int(input('I have thought of a secret interger between 0 and 5, try to guess it: '))

if(g==n):
    print(f'You got it! The secret number really was {n}')

else:
    print(f'Oh well, you got it wrong! The secret number was {n}, not {g}!')
