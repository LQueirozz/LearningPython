#Exercício 67: Várias tabuadas 
#Aprendendo sobre break pt2

while(True):
    n= int( input('Digite um número positivo inteiro para ver sua tabuada de 0 a 10: ') )
    if(n<0):
        break
    numCasas=0

    while (n>1):
        n/=10
        numCasas+=1

    n =int( n*(10**numCasas) )
    len= 1+numCasas+8+(numCasas+1)+1
    i=0

    print('-'*len)
    while(i<11):
        print(' {} X {} = {} ' .format(n, i, n*i))
        i+=1

    print('-'*len)