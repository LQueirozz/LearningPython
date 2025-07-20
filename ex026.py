#Exercício 26: Contando ocorrências
#Aprendendo sobre manipulação de strings pt5

frase = ( ( input("Digite um texto qualquer: ") ).strip() ).lower()

num = frase.count('a')
pos1 = frase.find('a') + 1
pos2 = frase.rfind('a') + 1

print('A letra "a" aparece {} vezes no seu texto' .format(num))
print('A primeira vez que a letra "a" aparece no seu texto foi na posição {}' .format(pos1))
print('A última vez que a letra "a" aparece no seu texto foi na posição {}' .format(pos2))