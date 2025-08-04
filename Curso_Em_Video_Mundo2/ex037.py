#CHALLENGE 37: Number base converter
#GOAL: Write code that converts an integer chosen by the user to another numeric base (binary, octal, or hexadecimal)
#SKILL: Learning about nested conditionals

print('Let\'s convert an integer chosen by you to another numeric base!')
origNum = int(input('Enter the number you want to convert: '))

print('To convert the number {} to binary, type 1'.format(origNum))
print('To convert the number {} to octal, type 2'.format(origNum))
print('To convert the number {} to hexadecimal, type 3'.format(origNum))

base = int(input('Which base do you want?: '))

if(base==1):
    conversion='binary'
    num=bin(origNum)

elif(base==2):
    conversion= 'octal'
    num=oct(origNum)

elif(base==3):
    conversion= 'hexadecimal'
    num=hex(origNum)

else:
    print('That is not a valid option! Please choose a number between 1 and 3 next time')
    exit()
    
print('The number {}, when converted to {} base, becomes {}' .format(origNum, conversion, num[2::]))