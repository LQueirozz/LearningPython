#CHALLENGE 60: Factorial
#GOAL: Write code that shows the factorial of a number
#SKILL: Learning about while loops

a=int(input('Type in a positive integer: '))
b=''
fact=1

print(f'{a}! = ', end='')

while(a>1):
    fact *= a
    b+= (f'{a} x ')
    a-= 1

b += '1'

print(f'{b} = {fact}')


