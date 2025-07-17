#Exercício 6: Dobro, Triplo, Raiz Quadrada
#Aprendendo sobre operadores pt2

n= float( input("Digite um número por favor: ") )

if (n%1==0):
    n= int(n)

print('O dobro de {} é {}' .format(n, n*2))
print('O triplo de {} é {}' .format(n, n*3))
print('A raiz quadrada de {} é {:.2f}' .format(n, n**(0.5)))
