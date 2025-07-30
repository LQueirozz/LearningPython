#CHALLENGE 84: Data analysis in nested lists
#GOAL:Write code that receives many names and corresponding weights. Then, print out how many people were added to the list, the lightest and the heaviest
#SKILL: Learning about nested lists

people=[]
person=[]

while True:
    flag= ( (input('Would you like to add another person to your list? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='Y'):
        print('That is not a valid option!', end=' ') 
        continue
    
    person.append(input(f'Name: '))
    person.append( float(input(f'Weight (kg): ')))

    people.append(person[:])

    person.clear()

for pos, p in enumerate(people):
    if (pos==0):
        maxW=minW=p[1]

    else:
        if (p[1]>maxW):
            maxW=p[1]

        if (p[1]<minW):
            minW=p[1]

nMaxW=''
nMinW=''

for p in people:
    if p[1]==maxW:
        nMaxW+= p[0] + ' '

    if p[1]==minW:
        nMinW+= p[0] + ' '

print(f'The list we built based on your input was {people}')
print(f'The list we built based on your input had {len(people)} people')
print(f'The heaviest ({maxW}kg) people were: {nMaxW}')
print(f'The lightest ({minW}kg) people were: {nMinW}')


