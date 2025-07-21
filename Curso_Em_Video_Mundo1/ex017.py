#CHALLENGE 17: Finding the hypothenuse
#GOAL: Write code that receives both legs of a rectangle triangle and prints out the hypothenuse 
#SKILL: Learning about importations

from math import hypot

ol = float (input('Type in the size of the opposite leg of your triangle: '))
al = float (input('Type in the size of the adjacent leg of your triangle: '))
h = hypot(ol, al)

print(f'The triangle with legs {ol} and {al} has a hypothenuse of size {h}')
