#Exercício 61: Progressão aritmética com while
#Aprendendo sobre while loops pt5

print('Informe a razão e o primeiro termo de uma progressão aritmética')
r=int(input('Razão: '))
a0= float(input('Primeiro termo:'))
a=a0
i=0

while(a!= (a0 + 9*r)):
    a= a0 + i*r
    print('Termo a{}: {:.2f}' .format(i,a))
    i+=1