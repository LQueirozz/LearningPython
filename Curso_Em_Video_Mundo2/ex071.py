#Exercício 71: Caixa eletrônico
#Aprendendo sobre break pt6

valor=float(input('Olá, eu sou um caixa eletrônico. Digite o quanto você quer sacar: R$'))
print(f'Para sacar R${valor:.2f}, vão ser necessárias...')

num50= valor//50
valor= valor- 50*num50

num20= valor//20
valor= valor- 20*num20

num10= valor//10
valor= valor - 10*num10

num1=valor

print(f'{num50:.0f} cédulas de R$50,00')
print(f'{num20:.0f} cédulas de R$20,00')
print(f'{num10:.0f} cédulas de R$10,00')
print(f'{num1:.0f} cédulas de R$1,00')