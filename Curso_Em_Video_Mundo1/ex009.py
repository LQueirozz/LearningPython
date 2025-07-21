#CHALLENGE 9: Multiplication tables
#GOAL: Write code that receives an integer and prints out it's multiplication table, from 0 to 10
#SKILL: Learning about operators and basic data types

n= int( input('Type in an integer to see their multiplication table from 0 to 10: ') )
numDec=0
i=0

print('='*20)
while(i<11):
    print(f' {n} X {i} = {n*i} ')
    i+=1
print('='*20)