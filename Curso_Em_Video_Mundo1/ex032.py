#CHALLENGE 32: Leap year
#GOAL: Write code that checks if the year the user provided is a leap year
#SKILL: Learning about conditionals

y=int(input('Type in any year of your choice: '))

if(y%4==0 and y%100!=0):
    print(f'The year {y} is a leap year!')

else:
    print(f'The year {y} is not a leap year!')