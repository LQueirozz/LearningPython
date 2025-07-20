#Exercício 57: Validação de dados
#Aprendendo sobre while loops pt1


a=((input('Digite qual o seu sexo (M, F ou I): ')).strip()).upper()

while( (a!='F') and (a!='M') and (a!='I') ):
    a=((input('Opção inválida! Favor escolher uma das três opções fornecidas (M, F ou I): ')).strip()).upper()

print('Opção escolhida: {}' .format(a))
