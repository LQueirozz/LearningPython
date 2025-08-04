#CHALLENGE 50: Sum of evens
#GOAL: Write code that receives 6 integers and prints out the sum of only the even numbers inputed
#SKILL: Learning about for loops

print('Type in 6 integers')
sum=0
for i in range(1, 7, 1):
    a= int(input(f'{i}º integer '))
    if (a%2==0):
        sum+=a

print(f'The sum of only the even numbers you provided was {sum}')