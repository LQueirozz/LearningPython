#Exercício 47: Soma de impares multiplos de 3
#Aprendendo sobre for loops pt3

soma=0
for i in range(1, 501, 2):
    if(i%3==0):
        soma+= i


print('A soma dos números ímpares e multiplos de 3 no intervalo de [1, 500] é {}' .format(soma))