#CHALLENGE 55: Data analysis
#GOAL: Write code that receives personal information about 4 people and then print out the average age of the people submitted
#as well as the oldest man in the group, and how many women had less than 20 years
#SKILL: Learning about for loops


print("I need some data about a group of 4 people")
yearC= int(input('Type in the current year: '))

lstName = []
lstAge = []
lstSex = []

for i in range(1, 5, 1):
    print('================{}=================' .format(i))
    lstName.append((input(f'Type in the {i}º person\'s name: ' .format(i))).strip())
    lstAge.append( yearC - (int( input(f'Type in the {i}º person\'s birthyear: '))))
    lstSex.append((input(f'Type in the {i}º person\'s sex (M, F or I): ')).strip())
    print(' ')

avg= oldestManInd=0
numWomen=0

for j in range(0, 4, 1):
    avg+=(lstAge[j]/4)
    if (lstAge[j]>lstAge[oldestManInd] and lstSex[j] in 'mM'):
        oldestManInd=j

    if(lstSex[j] in 'fF' and lstAge[j]<20):
        numWomen+=1

print(f'The average age of the group is {avg}')
print(f'The oldest man in the group is {lstName[oldestManInd]}, who is {lstAge[oldestManInd]} years old' )
print(f'There are {numWomen} women in the group under the age of 20')

 


