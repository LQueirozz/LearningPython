#Exercício 33: Maior de 3 numeros
#Aprendendo sobre condicionais pt6

print('Vamos encontrar o maior de 3 números inteiros!')
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

print('O maior dos três numeros fornecidos é {}' .format(a))
print('O menor dos três numeros fornecidos é {}' .format(c))