#Exercício 20: Sorteando ordem na lista
#Aprendendo sobre importações pt5

import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista=[a1, a2, a3, a4]

random.shuffle(lista)

print('{} {} {} {}' .format(lista[0], lista[1], lista[2], lista[3]))