#CHALLENGE 69: Data analysis
#GOAL: Write code that receives personal information about as many people as the user wants and then print how many people are of legal age
#as well as how many men there are in the group, and how many women had less than 20 years
#SKILL: Learning about for loops

yearC= int(input('Type in the current year: '))
i=1
numWomen=0
numMen=0
legalAge=0

while True:
    flag= ( (input('Would you like to add someone else? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='Y'):
        print('That\'s not a valid option!') 
        continue

    print('================{}=================' .format(i))
    age= yearC - (int( input(f'Type in the {i}º person\'s birthyear: ')))
    sex= ((input(f'Type in the {i}º person\'s sex (M, F or I): ')).strip())
    print(' ')

    if age>21:
        legalAge+=1

    if(sex in 'fF' and age<20):
        numWomen+=1

    if sex in 'mM':
        numMen+=1

print(f'There are {legalAge} people older than 21 in the group')
print(f'There are {numMen} men in the group')
print(f'There are {numWomen} women under the age of 20 in the group' )
