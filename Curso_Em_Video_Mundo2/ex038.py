#Exercício 38: Maior entre dois números
#Aprendendo sobre condicionais aninhadas pt3

print('Vamos encontrar o maior de 2 números inteiros!')
a = int( input('Digite o primeiro número inteiro: ') )
b = int( input('Digite o segundo número inteiro: ') )

if(a>b):
    print('O maior número é {}' .format(a))

elif(b>a):
    print('O maior número é {}' .format(b))

else:
    print('Não há maior número, pois os dois são iguais a {}' .format(a))


