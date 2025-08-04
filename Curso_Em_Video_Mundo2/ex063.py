#CHALLENGE 63: Fibonacci sequence
#GOAL: Write code that prints out as many terms of the fibonacci sequence as the user wants
#SKILL: Learning about while loops

a=int(input('Type in a positive integer: '))
print(f'The first {a} terms of the fibonacci sequence are:')
i=0
fib=[0, 1]


while(i<a):
    if(i>1):
        fib.append(fib[i-1] + fib[i-2])

    print('{}' .format(fib[i]), end='')
    i+=1

    if(i<a):
        print(' -> ', end='')

        
