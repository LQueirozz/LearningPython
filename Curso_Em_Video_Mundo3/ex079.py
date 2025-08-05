#CHALLENGE 79: Sorting a list of user input
#GOAL:Write code that receives many integers from the user and puts them in a list. Then, print out the list in order and without duplicates
#SKILL: Learning about lists

l=[]

while True:
    flag= ( (input('Would you like to add another number to your list? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='Y'):
        print('That is not a valid option!', end=' ') 
        continue

    num= int(input(f'Type in an integer: '))

    if num in l:
        print('That number was already in the list, disregarding...')
        continue

    else:
        l.append(num)
        print('Number added successfully!')
l.sort()
print(f'The list we built based on your input was {l}')

