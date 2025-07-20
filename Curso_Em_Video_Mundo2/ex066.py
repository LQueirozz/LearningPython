#Exercício 66: Flags com interrupção de laços
#Aprendendo sobre break pt1

cont=0
soma=0

while(True):
    flag= int(input('Digite um número inteiro positivo: '))
    if(flag==999):
        break
    soma+=flag
    cont+=1

print('Antes de digitar o código de saida (999), você digitou {} números, que juntos somam {}' .format(cont, soma))