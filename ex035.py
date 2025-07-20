#Exercício 35: Formação de triângulos
#Aprendendo sobre condicionais pt8

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

if( a>=(b+c) ):
    print('Não é possível formar um triângulo com estas retas!')

else:
    print('É possível formar um triângulo com estas retas!')