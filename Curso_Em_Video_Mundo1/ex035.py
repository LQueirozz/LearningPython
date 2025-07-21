#CHALLENGE 35: Possibility of triangles
#GOAL: Write code that receives the size of 3 lines and checks if it is possible to build a triangle with them
#SKILL: Learning about conditionals

print('Provide the length of 3 lines')
a = int( input('First line: ') )
b = int( input('Second line: ') )
c = int( input('Third line: ') )

if( (a>=(b+c)) or (b>=(a+c)) or (c>=(a+b)) ):
    print('It is not possible to build a triangle with these lines')

else:
    print('It is possible to build a triangle with these lines')