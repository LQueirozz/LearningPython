#Exercício 17: calculando a hipotenusa
#Aprendendo sobre importações pt2

from math import hypot

co = float (input('Digite a medida do cateto oposto do seu triângulo: '))
ca = float (input('Digite a medida do cateto adjacente do seu triângulo: '))

h = hypot(co, ca)

print('Para o triângulo de catetos {} e {}, a hipotenusa deve ser: {}' .format(co, ca, h))