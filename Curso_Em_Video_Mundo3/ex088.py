#CHALLENGE 88: Lottery numbers
#GOAL:Write code that receives how many times the user wishes to play the lottery. Then, show as many random lottery tickets for it as he wishes
#SKILL: Learning about nested lists

from random import randint

n= int(input('How many lottery tickets do you want?: '))

ltt=[]
tckt=[]
num=0

for i in range(0, n):
    for j in range(0,6):
        num=randint(1,60)
        while num in tckt:
            num=randint(1,60)
        tckt.append(num)


    tckt.sort()
    ltt.append(tckt[:])
    tckt.clear()

print('Your lottery tickets were: ')
for pos,item in enumerate(ltt):
    print (f'Ticket nº {pos+1}: {item}')

print('Good luck!')