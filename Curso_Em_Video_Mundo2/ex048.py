#CHALLENGE 48: Summing up
#GOAL: Write code that prints out the sum of all odd numbers that are also divisible by 3 between 1 and 500
#SKILL: Learning about for loops

sum=0
for i in range(3, 501, 6):
    sum+= i


print(f'The sum of all odd numbers that are also divisible by 3 in the interval [1, 500] is {sum}')