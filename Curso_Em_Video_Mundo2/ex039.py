#Exercício 39: Alistamento militar
#Aprendendo sobre condicionais aninhadas pt4

anoA = int(input('Informe o ano atual: '))
anoN = int(input('Informe seu ano de nascimento: '))

if( (anoN+18) <anoA):
    print('Sua época de alistamento foi {} anos atrás' .format( anoA - ( anoN+18 ) ))

elif( (anoN+18) >anoA):
    print('Sua época de alistamento vai ser daqui a {} anos ' .format( ( anoN+18 ) - anoA ))

else:
    print('Esse é seu ano de se alistar!')



