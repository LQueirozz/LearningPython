#Exercício 42: Formação de triangulos 2
#Aprendendo sobre condicionais aninhadas pt7

print('Informe o comprimento de 3 retas!')
a = int( input('Digite o primeiro número inteiro: ') )
b = int( input('Digite o segundo número inteiro: ') )
c = int( input('Digite o terceiro número inteiro: ') )

if(c>a):
    temp = a
    a = c
    c = temp

if(b>a):
    temp = b
    b = a
    a = temp

if(c>b):
    temp = b
    b = c
    c = temp

if(a==b and b==c):
    info='equilátero'

elif(a!=b and a!=c and c!=b):
    info='escaleno'

else:
    info='isóceles'

if( a>=(b+c) ):
    print('Não é possível formar um triângulo com estas retas!')
    exit()

else:
    print('É possível formar um triângulo {} com estas retas!' .format(info))


