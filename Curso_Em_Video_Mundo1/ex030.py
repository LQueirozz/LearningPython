#CHALLENGE 30: Odd or even
#GOAL: Write code that checks if user input was an odd or an even number
#SKILL: Learning about conditionals

n=int(input('Type in an integer greater than 0: '))

if(n%2==0):
    print(f'The number {n} is even')

else:
    print(f'The number {n} is odd')