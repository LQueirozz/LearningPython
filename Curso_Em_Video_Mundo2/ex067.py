#CHALLENGE 67: Complete multiplication table
#GOAL: Write code that takes in as many integers as the user wants and then print out the highest, the lowest and the average
#SKILL: Learning about break

while(True):
    n= int( input('Type in any number to see it\'s multiplication table of 0 through 10 (-1 to exit): ') )
    numDec=0
    if(n<0):
        break

    while (n>1):
        n/=10
        numDec+=1

    n =int( n*(10**numDec) )
    siz= 1+numDec+8+(numDec+1)+1
    i=0

    print('-'*siz)
    while(i<11):
        print(f' {n} X {i} = {n*i} ')
        i+=1

    print('-'*siz)