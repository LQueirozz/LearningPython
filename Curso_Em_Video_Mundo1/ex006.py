#CHALLENGE 6: Double, triple and square root
#GOAL: Write code that receives a non negative number and prints out it's double, triple and sqrt
#SKILL: Learning about operators and basic data types

n= float( input("Type in a number equal or greater than zero: ") )

print(f'{n} doubled is {n*2}')
print(f'{n} tripled is {n*3}')
print(f'The sqrt of {n} is {(n**(0.5)):.2f}')
