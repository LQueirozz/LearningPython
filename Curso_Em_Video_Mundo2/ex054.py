#Exercício 54: Maioridade
#Aprendendo sobre for loops pt9

print("Vamos verificar quantas das próximas 7 pessoas são maiores de idade!")
anoA = int(input('Digite o ano atual: '))
maior=0

lista = []

for i in range(1, 8, 1):
    lista.append( int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i) ) ) )

for ano in lista:
    if (ano+21<=anoA):
        maior+=1

print('Entre as sete pessoas classificadas, há {} pessoas com 21 anos ou mais' .format(maior))