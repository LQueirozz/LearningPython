#Exercício 53: Palindromos
#Aprendendo sobre for loops pt8

frase1 = (input('Digite uma frase qualquer: ') ).lower()
frase2 = ''
k = 0
total=0

for i in range (0, len(frase1), 1):
    if(frase1[i] != ' '):
        frase2 += frase1[i]

pali = ''

for j in range (len(frase2)-1, 0, -1):
    pali += frase2[j]

for l in range (0, len(frase2)-1, 1):
    if (pali[l] == frase2[l]):
        total+=1

if(total == len(frase2)-1):
    print('A frase "{}" é um palíndromo!' .format(frase1))

else:
    print('A frase "{}" não é um palíndromo!' .format(frase1))