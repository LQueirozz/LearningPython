#Exercício 52: Números primos
#Aprendendo sobre for loops pt7

n= int(input('Digite um número inteiro qualquer: '))

for i in range(2, n, 1):
    if(n%i==0):
        print('O número {} não é primo!' .format(n))
        exit()

print('O número {} é primo!' .format(n))
