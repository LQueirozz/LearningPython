#CHALLENGE 33: Greatest of 3 numbers
#GOAL: Write code that finds the biggest number between the 3 integers that the user provides
#SKILL: Learning about conditionals

print('We shall find the greatest number among the next 3!')
a = int( input('Type in the first integer: ') )
b = int( input('Type in the second integer: ') )
c = int( input('Type in the third integer: ') )

if(c>a):
    temp = a
    a = c
    c = temp

if(b>a):
    temp = b
    b = a
    a = temp

if(c>b):
    temp = b
    b = c
    c = temp

print(f'The greatest among the three was {a}' )
print(f'The smallest among the three was {c}' )