#CHALLENGE 52: Prime numbers
#GOAL: Write code that prints out if the integer the user provided was a prime number
#SKILL: Learning about for loops

n= int(input('Type in any integer: '))

for i in range(2, n, 1):
    if(n%i==0):
        print(f'The number {n} is not a prime number!')
        exit()

print(f'The number {n} is a prime number!')
