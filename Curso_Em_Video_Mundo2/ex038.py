#CHALLENGE 38: Larger of two numbers
#GOAL: Write code that receives two integers from the user and determines which one is larger or if they are equal
#SKILL: Learning about nested conditionals

print('Let\'s find the greatest among 2 integers!')
a = int( input('Enter the first integer: ') )
b = int( input('Enter the second integer: ') )

if(a>b):
    print('The larger number is {}' .format(a))

elif(b>a):
    print('The larger number is {}' .format(b))

else:
    print('There is no larger number, because both are equal to {}' .format(a))