#Exercício 70: Estatística em produtos
#Aprendendo sobre break pt5

m1000=0
i=1
soma=0
ncaros=0
listaN=[]
listaP=[]
ind=0

while True:
    flag= ( (input('Você quer passar mais um produto? (S/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='S'):
        print('Opção Inválida!') 
        continue

    print('\n================{}=================' .format(i))
    nome= ((input(f'Informe o nome do {i}º produto: ')).strip())
    preço=(float( input(f'Informe o preço do {i}º produto: R$') ))
    print(' ')

    soma+=preço

    if(preço>1000):
        ncaros+=1

    listaN.append(nome)
    listaP.append(preço)

    if( i>2 and listaP[i-1]<listaP[ind]):
        ind=i-1

    i+=1

print(f'O total gasto foi R${soma:.2f}')
print(f'Você comprou {ncaros} item mais caros do que R$1000.00')
print(f'O item mais barato que você comprou foi {listaN[ind]}, o qual custava R${listaP[ind]:.2f}')

    

