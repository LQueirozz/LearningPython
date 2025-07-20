#Exercício 25: Procurando uma substring
#Aprendendo sobre manipulação de strings pt4

nome = ( ( input("Qual o seu nome?: ") ).strip() ).lower() 

print('Você possui Silva no seu nome: {}' .format( bool(nome.find('silva')+1 ) ) )