#CHALLENGE 39: Military enlistment
#GOAL: Write code that calculates when a person should enlist in the military based on their birth year and the current year
#SKILL: Learning about nested conditionals

currentYear = int(input('Enter the current year: '))
birthYear = int(input('Enter your birth year: '))

if( (birthYear+18) < currentYear):
    print('Your enlistment year was {} years ago' .format( currentYear - ( birthYear+18 ) ))

elif( (birthYear+18) > currentYear):
    print('Your enlistment year will be in {} years ' .format( ( birthYear+18 ) - currentYear ))

else:
    print('This is your year to enlist!')