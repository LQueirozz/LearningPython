#Exercício 9: Tabuada
#Aprendendo sobre operadores pt5

n= int( input('Digite um numero inteiro para ver sua tabuada de 0 a 10: ') )
numCasas=0

#A formatação desejada é:
# --------------
#  n X 0 = 0 
#  n X 1 = n 
#  n X 2 = 2n
#  n X 3 = 3n 
#  n X 4 = 4n
#  n X 5 = 5n
#  n X 6 = 6n 
#  n X 7 = 7n
#  n X 8 = 8n 
#  n X 9 = 9n
#  n X 10 = 10n
# --------------


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