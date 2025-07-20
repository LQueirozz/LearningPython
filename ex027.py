#Exercício 26: Primeiro e último nome
#Aprendendo sobre manipulação de strings pt6

nome = ( ( ( input("Qual o seu nome?: ") ).strip() ).lower() ).split()

print('Prazer em te conhecer!')
print('O seu primeiro nome é {}' .format(nome[0]))
print('O seu último nome é {}' .format(nome[len(nome) -1]))