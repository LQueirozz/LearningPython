#CHALLENGE 94: Logging personal data
#GOAL:Write code that takes in many peoples data (name, sex, age) and prints out how many people were logged, the average age of the group,
#a list with all the women, and a list with the people whose age is bigger than the average
#SKILL: Learning about dictionaries

lst=[]
person={}
lstW=[]
sumAge=0

while True:
    flag= ( (input('Would you like to add another person to your list? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='Y'):
        print('That is not a valid option!') 
        continue

    person['name'] = str(input('Name: '))

    while True:
        person['sex'] = ((str(input('Sex (M, F, I): '))).strip()).upper()
        if (person['sex'] not in 'MFI'): 
            print('That is not a valid option!', end=' ') 
            continue
        else:
            break
    
    if person['sex']=='F':
        lstW.append(person['name'])
    
    while True:
        person['age'] = int(input('Age: '))
        if (person['age'] <0 ): 
            print('That is not a valid option!', end=' ') 
            continue
        else:
            sumAge+=  person['age']
            break

    lst.append(person.copy())

avg= sumAge/len(lst)
lstOld=[]
for p in lst:
    if p['age']>avg:
        lstOld.append(p.copy())

print('='*50)
print(f'The list we buit based on your data was: [')
for p in lst:
    print(p)
print(']')
print('='*50)
print(f'The number of people on the list was {len(lst)}')
print(f'The average age of a person in this list is {avg:.2f}')
print(f'The women in this list are {lstW}')
print(f'The people older than the average age were: {lstOld}')