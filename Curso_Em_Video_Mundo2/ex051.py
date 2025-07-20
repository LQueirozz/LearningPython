#Exercício 51: Progressão aritmética
#Aprendendo sobre for loops pt6

print('Informe a razão e o primeiro termo de uma progressão aritmética')
r=int(input('Razão: '))
a0= float(input('Primeiro termo:'))

for i in range(0, 10, r):
    print('Termo a{}: {:.2f}' .format(i, a0+i*r))