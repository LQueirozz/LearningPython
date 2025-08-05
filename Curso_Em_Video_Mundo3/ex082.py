#CHALLENGE 82: Evens and odds in a list
#GOAL:Write code that receives many positive integers from the user and puts them in a list. 
#Then, print out the list and two others: one containing only the even numbers and the othe only containg the odds
#SKILL: Learning about lists

l=[]
ev=[]
od=[]

while True:
    flag= ( (input('Would you like to add another number to your list? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='Y'):
        print('That is not a valid option!', end=' ') 
        continue

    num= int(input(f'Type in a non negative integer: '))

    while(num<0):
        print('That is not a valid option!', end=' ') 
        num= int(input(f'Type in a non negative integer: '))

    l.append(num)
    print('Number added successfully!')

    if(num%2==0):
        ev.append(num)
    else:
        od.append(num)

print(f'The list we built based on your input was\n{l}')
print(f'The list we built based on your input with only odd numbers was \n{od}')
print(f'The list we built based on your input with only even numbers was \n{ev}')