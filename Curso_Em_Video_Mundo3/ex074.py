#CHALLENGE 74: Random tuple
#GOAL: Write code that generates 5 random integers and puts them in a tuple. Then, print out the tuple, its smallest and greatest number
#SKILL: Learning about tuples

from random import randint


t=(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'The generated tuple was: {t}')
print(f'The greatest number was {max(t)}')
print(f'The smallest number was {min(t)}')