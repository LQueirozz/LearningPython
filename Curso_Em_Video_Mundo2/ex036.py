#Exercício 36: Empréstimo bancário
#Aprendendo sobre condicionais aninhadas pt1

print('Vamos calcular as suas parcelas mensais para quitar uma casa')
valorCasa = int( input('Digite qual o valor da casa: ') )
salario = int( input('Digite o seu salário mensal: ') )
tempo = (int( input('Digite em quantos anos você pretende financiar essa casa: ') ) )*12

#se a parcela mensal for maior que 30% do salário, o empréstimo é negado

if(valorCasa/tempo> 0.3*salario):
    print('\033[1;31mSeu empréstimo foi negado!\033[0;30m')

else:
    print('A sua parcela mensal será de: \033[1;31mR${:.2f} \033[0;30m' .format(valorCasa/tempo))