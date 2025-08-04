#CHALLENGE 51: Arithmetic progression
#GOAL: Write code that receives the first term and the pace of a geometric progression, and prints out the first 10 numbers of the progression
#SKILL: Learning about for loops

print('Informe a razão e o primeiro termo de uma progressão aritmética')
r=int(input('Razão: '))
a0= float(input('Primeiro termo:'))

for i in range(0, 10, r):
    print('Termo a{}: {:.2f}' .format(i, a0+i*r))