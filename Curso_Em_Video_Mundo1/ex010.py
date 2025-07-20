#Exercício 10: Conversão de moedas
#Aprendendo sobre operadores pt6

n= float(input('Quanto de dinheiro que você tem na carteira?: R$') )

print('Com seus R${:.2f} reais, você consegue comprar US${:.2f} dólares' .format(n, (n/5.54)) )
