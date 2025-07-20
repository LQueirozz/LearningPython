#Exercício 24: Verificando as primeiras letras de um texto
#Aprendendo sobre manipulação de strings pt3

nome = ( ( input("Qual o seu nome?: ") ).strip() ).lower() 

print('Você possui Silva no seu nome: {}' .format( bool(nome.find('silva')+1 ) ) )