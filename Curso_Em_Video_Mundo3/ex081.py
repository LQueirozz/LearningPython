#CHALLENGE 81: Analysing a list of user input
#GOAL:Write code that receives many integers from the user and puts them in a list already in the correct postion based on order.
#Then, print out how many items are on the list, the list in reverse order, and if the number 5 was present in the list
#SKILL: Learning about lists

l=[]
isFive=False

while True:
    flag= ( (input('Would you like to add another number to your list? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='Y'):
        print('That is not a valid option!', end=' ') 
        continue

    num= int(input(f'Type in an integer: '))

    if(num==5):
        isFive=True

    l.append(num)
    print('Number added successfully!')    

print(f'The list we built based on your input was {l}')
print(f'The list we built based on your input had {len(l)} numbers')
l.sort(reverse=True)
print(f'The list we built based on your input, in reverse order, was {l}')
if isFive:
   print(f'The list we built based on your input had the number 5') 

else:
     print(f'The list we built based on your input did not have the number 5') 

