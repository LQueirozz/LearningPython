#Exercício 58: Adivinhação completa
#Aprendendo sobre while loops pt2

from random import randint

n= randint(0,11)
chute = int(input('Pensei em um número inteiro secreto entre 0 e 10, tente adivinhá-lo: '))
cont=1

while(chute!=n):
    chute = int(input('Não é esse! Tente novamente: '))
    cont+=1

print('Você acertou! O número secreto era {} mesmo! Você descobriu em {} chutes!' .format(n, cont))
