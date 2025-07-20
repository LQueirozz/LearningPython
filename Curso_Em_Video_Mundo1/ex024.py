#Exercício 24: Verificando as primeiras letras de um texto
#Aprendendo sobre manipulação de strings pt3

cidade = ( ( ( input("Qual a cidade em que você nasceu?: ") ).strip() ).lower() ).split()

print("A primeira palavra da sua cidade natal é santo: {}" .format( cidade[0]=='santo' ) )

