#Exercício 23: Analisador de textos
#Aprendendo sobre manipulação de strings pt2

numero = int(input("Digite um número qualquer: "))

print("Analisando o numero {} ..." .format(numero))

milhar = numero//1000
numero -= milhar*1000

centena = numero//100
numero -= centena*100

dezena = numero//10
numero -= dezena*10

unidade = numero

print("Milhares: {}" .format(milhar))
print("Centenas: {}" .format(centena))
print("Dezenas: {}" .format(dezena))
print("Unidades: {}" .format(unidade))