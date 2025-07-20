#Exercício 60: Fatorial
#Aprendendo sobre while loops pt4

a=int(input('Digite um número inteiro positivo: '))
b=''
fat=1

print('{}! = ' .format(a), end='')

while(a>1):
    fat *= a
    b+='{} x ' .format(a)
    a-= 1

b += '1'

print('{} = {}' .format(b, fat))


