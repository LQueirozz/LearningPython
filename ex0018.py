#Exercício 18: Seno, Cosseno e Tangente
#Aprendendo sobre importações pt3

import math
ang= float( input('Digite um ângulo em GRAUS: ') )

seno= math.sin(math.radians(ang))
cosseno= math.sqrt( 1 - (seno**2) )
tangente= seno/cosseno

print('O ângulo {:.2f}º possui...' .format(ang))
print('SENO = {:.2f} ' .format(seno))
print('COSSENO = {:.2f} ' .format(cosseno))
print('TANGENTE = {:.2f} ' .format(tangente))