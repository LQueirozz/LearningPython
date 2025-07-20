#Exercício 65: Estatística para muitos números
#Aprendendo sobre while loops pt9

flag='S'
cont=0
soma=0
lst=[]
maior=0
menor=0

while(flag!='N'):
    lst.append( int(input('Digite um número inteiro: ')) )
    soma+=lst[cont]

    if (cont>1):
        if(lst[cont]<lst[cont-1]):
            menor=lst[cont]

        if(lst[cont]>lst[cont-1]):
            maior=lst[cont]

    else:
        menor=lst[cont]
        maior=lst[cont]

    cont+=1
    flag= ( (input('Você quer digitar mais um número? (S/N): ')).strip()).upper()

print('Antes de parar, a média dos números inseridos por você foi {:.2f}' .format(soma/cont))
print('O maior número foi {}' .format(maior))
print('O menor número foi {}' .format(menor))
