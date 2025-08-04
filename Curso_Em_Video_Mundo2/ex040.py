#CHALLENGE 40: Grade average
#GOAL: Write code that calculates the average of two grades and determines if the student passed, needs recovery, or failed
#SKILL: Learning about nested conditionals

n1 = float( input('The student\'s first grade was: ') )
n2 = float( input('The student\'s second grade was: ') )

avg = (n1+n2)/2

if(avg>7):
    print('PASSED')

elif(avg>5):
    print('SUMMER SCHOOL')

else:
    print('FAILED')