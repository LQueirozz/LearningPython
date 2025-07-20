#Exercício 62: Progressão aritmética com while e mais interações
#Aprendendo sobre while loops pt6

print('Informe a razão e o primeiro termo de uma progressão aritmética')
r=int(input('Razão: '))
a0= float(input('Primeiro termo:'))
a=a0
i=0

lim=10

while(lim):

    lim+=i
    
    while(a!= (a0 + (lim -1)*r)):
        a= a0 + i*r
        print('Termo a{}: {:.2f}' .format(i,a))
        i+=1

    lim= int(input('Quantos mais termos você quer ver?: ')) 
