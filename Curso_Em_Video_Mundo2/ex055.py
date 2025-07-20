#Exercício 55: Analise de dados pessoais
#Aprendendo sobre for loops pt10

print("Informe alguns dados sobre 4 pessoas")
anoA = int(input('Digite o ano atual: '))

listaN = []
listaI = []
listaS = []

for i in range(1, 5, 1):
    print('================{}=================' .format(i))
    listaN.append((input('Informe o nome completo da {}ª pessoa: ' .format(i))).strip())
    listaI.append( anoA - (int( input('Informe o ano de nascimento da {}ª pessoa: ' .format(i)) )) )
    listaS.append((input('Informe o sexo da {}ª pessoa (M, F ou I): ' .format(i))).strip())
    print(' ')

m=0
med=0
ind=0
inds=0

for j in range(0, 4, 1):
    med+=(listaI[j]/4)
    if (listaI[j]>m and listaS[j]=='M'):
        m=listaI[j]
        ind=j

    if(listaS[j]=='F' and listaI[j]<20):
        inds+=1

print('A média de idade do grupo é {} anos' .format(med))
print('O homem mais velho do grupo é o {}' .format(listaN[ind]))
print('Há {} mulheres no grupo com menos de 20 anos' .format(inds))

 


