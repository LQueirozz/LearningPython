#Exercício 56: Maior e menor da lista
#Aprendendo sobre for loops pt11

print("Informe, em kg, o peso de 5 pessoas")

lista=[]

for i in range(1, 6, 1):
    lista.append( int( input('Informe o peso da {}ª pessoa: ' .format(i)) )) 

menor=lista[0]
maior=0

for peso in lista:
    if (peso < menor):
        menor=peso

    if (peso>maior):
        maior=peso

print('O maior peso lido foi {}kg' .format(maior))
print('O menor peso lido foi {}kg' .format(menor))