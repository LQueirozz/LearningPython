#CHALLENGE 80: Sorting a list of user input without sort()
#GOAL:Write code that receives 5 integers from the user and puts them in a list already in the correct postion based on order. Then, print out the list in order and without duplicates
#SKILL: Learning about lists

l=[]

for i in range(0,5):
    num= int(input(f'Type in an integer: '))

    if (len(l)>0):
        for pos,number in enumerate(l):
            if (num<number):
                l.insert(pos, num)
                print(f'Adding to the {pos}º position...')
                break
    
    if(len(l)==i):
        l.append(num)
        print(f'Adding to the end of the list...')

print(f'The list we built based on your input was {l}')

