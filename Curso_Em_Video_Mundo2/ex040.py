#Exercício 40: Média de notas
#Aprendendo sobre condicionais aninhadas pt5

n1 = float( input('A primeira nota do aluno foi: ') )
n2 = float( input('A segunda nota do aluno foi: ') )

med= (n1+n2)/2

if(med>7):
    print('APROVADO')

elif(med>5):
    print('RECUPERAÇÃO')

else:
    print('REPROVADO')