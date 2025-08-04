#CHALLENGE 41: Age classification
#GOAL: Write code that calculates a person's age and classifies them into age categories (MIRIM, INFANTIL, JUNIOR, SENIOR, MASTER)
#SKILL: Learning about nested conditionals

currentYear = int(input('Enter the current year: '))
birthYear = int(input('Enter your birth year: '))

age = currentYear - birthYear

if(age<=9):
    print('CHILD')

elif(age<=14):
    print('PRE-TEEN')

elif(age<=19):
    print('JUNIOR')

elif(age==20):
    print('SENIOR')

else:
    print('MASTER')