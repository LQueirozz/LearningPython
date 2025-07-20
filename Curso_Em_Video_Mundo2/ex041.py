#Exercício 41: Classificação etária
#Aprendendo sobre condicionais aninhadas pt6

anoA = int(input('Informe o ano atual: '))
anoN = int(input('Informe seu ano de nascimento: '))

idade=anoA-anoN

if(idade<=9):
    print('MIRIM')

elif(idade<=14):
    print('INFANTIL')

elif(idade<=19):
    print('JUNIOR')

elif(idade==20):
    print('SENIOR')

else:
    print('MASTER')

