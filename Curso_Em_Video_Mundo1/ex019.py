#Exercício 19: Sorteando item na lista
#Aprendendo sobre importações pt4

from random import randint

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista=[a1, a2, a3, a4]

print('O aluno sorteado foi: {}' .format(lista[randint(0,3)]))