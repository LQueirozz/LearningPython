#CHALLENGE 75: Analysing data from tuples
#GOAL: Write code that receives 5 integers from the user and puts them in a tuple. Then, print out how many times the number 9 showed up, the position oh the first 3, and the even numbers that were typed
#SKILL: Learning about tuples

t=( int(input('Type in an integer: ')),  
   int(input('Type in an integer: ')),  
   int(input('Type in an integer: ')),  
   int(input('Type in an integer: '))
   )

strE=''

for pos,number in enumerate(t):   
    if(number%2==0):
        if(len(strE)!=0):
            strE+=', '
        strE+= str(number)

print(f'The numbers you typed were {t}')
print(f'The number 9 showed up {t.count(9)} times')
if(3 in t):
    print(f'The number 3 first showed up at the {t.index(3)}º position ')
else:
    print(f'The number 3 was not a part of the typed numbers')
print(f'The even numbers were {strE}')