#Exercício 63: Fibonacci
#Aprendendo sobre while loops pt7

a=int(input('Digite um número inteiro positivo: '))
i=0
fib=[0, 1]


while(i<a):
    if(i>1):
        fib.append(fib[i-1] + fib[i-2])

    print('{}' .format(fib[i]), end='')
    i+=1

    if(i<a):
        print(' -> ', end='')

        
