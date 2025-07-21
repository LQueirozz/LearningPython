#CHALLENGE 19: Sorting a student
#GOAL: Write code that receives the names of four students and prints out one of their names at random
#SKILL: Learning about importations

from random import randint

a1 = (input('First student: ')).strip()
a2 = (input('Second student: ')).strip()
a3 = (input('Third student: ')).strip()
a4 = (input('Fourth student: ')).strip()

lst=[a1, a2, a3, a4]

print('The lucky student was: {}' .format(lst[randint(0,3)]))