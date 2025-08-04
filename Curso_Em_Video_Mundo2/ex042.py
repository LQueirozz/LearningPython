#CHALLENGE 42: Triangle formations 2
#GOAL: Write code that receives the length of 3 lines and shows what kind of triangle it is (isoceles, scaleno, equilateral)
#SKILL: Learning about nested conditionals

print('Type in the lenght of 3 lines!')
a = int( input('Type in the first length (integer): ') )
b = int( input('Type in the second length (integer): ') )
c = int( input('Type in the third length (integer): ') )

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

if(a==b and b==c):
    info='Equilatery'

elif(a!=b and a!=c and c!=b):
    info='Scalene'

else:
    info='Isoceles'

if( a>=(b+c) ):
    print('It is not possible to create a triangle with these side lengths!')
    exit()

else:
    print(f'You can create a {info} triangle with these lines!')


