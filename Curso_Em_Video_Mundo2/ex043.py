#Exercício 43: Classificação IMC
#Aprendendo sobre condicionais aninhadas pt8

h = float(input('Informe a sua altura em metros: '))
m = float(input('Informe sua massa em kg: '))

imc= m/(h**2)

if(imc<18.5):
    print('ABAIXO DO PESO')

elif(imc<=25):
    print('PESO IDEAL')

elif(imc<=30):
    print('SOBREPESO')

elif(imc<=40):
    print('OBESIDADE')

else:
    print('OBESIDADE MÓRBIDA')

