#CHALLENGE 58: Complete guessing game
#GOAL: Write code that has a user guess what number the computer came up with
#SKILL: Learning about while loops

from random import randint

n= randint(0,10)
guess = int(input('I\'ve thought of a secret integer number between 0 and 10, try to guess it: '))
count=1

while(guess!=n):
    guess = int(input('Nope! Try again: '))
    count+=1

print(f'You got it! The secret integer was {n}! You got that right in {count} guesses!')
