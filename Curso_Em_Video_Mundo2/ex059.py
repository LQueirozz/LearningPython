#Exercício 59: Calculadora com menu de opções
#Aprendendo sobre while loops pt3

def pegaNumeros(a, b):
    a=int(input('Digite o primeiro número inteiro: ')) 
    b=int(input('Digite o segundo número inteiro: '))
    return [a,b]

def menu():
    print('OPÇÕES DA CALCULADORA:')
    print('1- SOMA')
    print('2- MULTIPLICAÇÃO')
    print('3- MAIOR')
    print('4- TROCAR NUMEROS')
    print('5- SAIR DA CALCULADORA')
    return(int (input('Digite qual opção você deseja: ')))

def maior(a, b):
    if(a>b):
        return ('{} > {}'.format(a,b) )
    
    elif(a<b):
        return ('{} > {}'.format(b,a) )
    
    else:
        return ('{} = {}'.format(a,b) )

lista = [0, 0]
opc=0

lista= pegaNumeros(lista[0], lista[1])
opc= menu()

while(opc!=5):
    if(opc==1):
        print('{} + {} = {}' .format(lista[0], lista[1], lista[0] + lista[1]))

    elif(opc==2):
        print('{} x {} = {}' .format(lista[0], lista[1], lista[0] * lista[1]))

    elif(opc==3):
        print(maior(lista[0], lista[1]))

    elif(opc==4):
        lista= pegaNumeros(lista[0], lista[1])

    else:
        print('Opção inválida!')

    opc= menu()

print('Execução finalizada!')
