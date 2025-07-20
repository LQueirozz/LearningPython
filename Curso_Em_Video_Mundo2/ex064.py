#Exercício 64: Flags
#Aprendendo sobre while loops pt8

flag= int(input('Digite um número inteiro positivo: '))
cont=0
soma=0

while(flag!=999):
    soma+=flag
    cont+=1
    flag= int(input('Digite um número inteiro positivo: '))

print('Antes de digitar o código de saida (999), você digitou {} números, que juntos somam {}' .format(cont, soma))
