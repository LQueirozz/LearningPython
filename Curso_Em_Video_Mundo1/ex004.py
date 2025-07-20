#Exercício 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
#Aprendendo mais sobre tipos de dados básicos

n = input('Digite algo: ')

if (n):
    print('O tipo do seu input foi um: {}' .format( type(n)) )

    print('O seu input é um número?: {}' .format( n.isnumeric() ) )

    print('O seu input é alfabético?: {}' .format( n.isalpha() ) )
    print('O seu input é constituído apenas por letras minúsculas?: {}' .format( n.islower() ) )
    print('O seu input é constituído apenas por letras maiúsculas?: {}' .format( n.isupper() ) )
    print('O seu input está capitalizado?: {}' .format( n.istitle() ) )
    print('O seu input é constituído apenas por espaços?: {}' .format( n.isspace() ) )

    print('O seu input faz parte do conjunto união entre números e letras?: {}' .format( n.isalnum() ) ) 

else:
    print('Por favor, insira algo na próxima vez!')
