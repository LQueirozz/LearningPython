#Exercício 22: Analisador de textos
#Aprendendo sobre manipulação de strings pt1

nome= (input("Escreva o seu nome: ")).strip()

nomeMais= nome.upper()
nomeMinu= nome.lower()
nomeSeparado=nome.split()
tam = len(nome)-nome.count(' ')
tamPri= len(nomeSeparado[0])

print("O seu nome todo em maiusculo é {}" .format(nomeMais))
print("O seu nome todo em minúsculo é {}" .format(nomeMinu))
print("O seu nome possui {} letras" .format(tam))
print("O seu primeiro nome possui {} letras" .format(tamPri))
