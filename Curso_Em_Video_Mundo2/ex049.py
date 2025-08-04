#CHALLENGE 49: Multiplication table upgraded
#GOAL: Write code that prints out the multiplication table of whatever number the user puts in
#SKILL: Learning about for loops

n= int( input('Type in any number to see it\'s multiplication table of 0 through 10: ') )
numDec=0

while (n>1):
    n/=10
    numDec+=1

n =int( n*(10**numDec) )
len= 1+numDec+8+(numDec+1)+1
i=0

print('-'*len)
for i in range(0, 11, 1):
    print(f' {n} X {i} = {n*i} ')
print('-'*len)