#CHALLENGE 20: Shuffling lists
#GOAL: Write code that receives the names of four students and prints out thair names in a different random order
#SKILL: Learning about importations

import random

a1 = (input('First student: ')).strip()
a2 = (input('Second student: ')).strip()
a3 = (input('Third student: ')).strip()
a4 = (input('Fourth student: ')).strip()

lst=[a1, a2, a3, a4]

random.shuffle(lst)

print(f'{lst[0]} {lst[1]} {lst[2]} {lst[3]}')