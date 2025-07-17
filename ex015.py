#Exercício 15: Aluguel de carros
#Aprendendo sobre operadores pt11

#Preço por dia do carro: R$60
#Preço por km rodado: R$0,15

dias= int( input('Digite quantos dias você alugou o carro: '))
km= float (input('Digite quantos kilômetros você andou com o carro: '))

print('Total a pagar R${:.2f}' .format( (dias*60) + (km*0.15) ) )