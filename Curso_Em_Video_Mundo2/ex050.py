#Exercício 50: Soma dos pares
#Aprendendo sobre for loops pt5

print('Digite 6 números inteiros')
soma=0
for i in range(1, 7, 1):
    a= int(input('{}º número inteiro: ' .format(i)))
    if (a%2==0):
        soma+=a

print('a soma dos números pares digitados foi: {}' .format(soma))