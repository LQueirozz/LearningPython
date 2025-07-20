#Exercício 27: Adivinhação simples
#Aprendendo sobre condicionais

from random import randint

n= randint(0,5)
chute = int(input('Pensei em um número inteiro secreto entre 0 e 5, tente adivinhá-lo: '))

if(chute==n):
    print('Você acertou! O número secreto era {} mesmo!' .format(n))

else:
    print('Poxa, você errou! O número secreto era {} e não {}!' .format(n, chute))
