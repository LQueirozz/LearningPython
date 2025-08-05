#CHALLENGE 85: Evens and odds in nested lists
#GOAL:Write code that receives 7 positive integers and separate them in two lists (one of even numbers, and another of odds) that are both
#nested inside of a main list. Then, print out those two sub lists in order
#SKILL: Learning about nested lists

l=[[],[]]
for i in range (0,7):
    num= int(input(f'Type in a non negative integer for the {i}º position: '))

    while(num<0):
        print('That is not a valid option!', end=' ') 
        num= int(input(f'Type in a non negative integer for the {i}º position: '))

    if(num%2==0):
        l[0].append(num)
    else:
        l[1].append(num)

    print('Number added successfully!')


print(f'The even numbers were: {sorted(l[0])}')
print(f'The odd numbers were: {sorted(l[1])}')
