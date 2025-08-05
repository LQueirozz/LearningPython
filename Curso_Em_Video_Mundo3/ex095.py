#CHALLENGE 95: Soccer player stats pt2
#GOAL:Write code that receives many soccer players' names, how many matches they played and how many goals they made on each game. Then print out stats
#SKILL: Learning about dictionaries

lst=list()
player={}
big=-1
while True:
    flag= ( (input('Would you like to add another soccer player to your list? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='Y'):
        print('That is not a valid option!') 
        continue

    player['name']= str(input('What is the name of the player?: '))
    num= int(input(f'How many soccer matches did {player["name"]} partipate in?: '))
    while num<0:
        print('That is not a valid number!')
        num= int(input(f'How many soccer matches did {player["name"]} partipate in?: '))

    if num>big:
        big=num
    numGoals=[]
    total=0
    for i in range(1, num+1):
        n=int(input(f'How many goals did {player["name"]} score on the {i}º game?: '))
        while n<0:
            print('That is not a valid number!')
            n=int(input(f'How many goals did {player["name"]} score on the {i}º game?: '))
        numGoals.append(n)
        total+=n

    player['goals']=numGoals
    player['total']=total
    lst.append(player.copy())
big=big*3  
print('='*60)
print('Player scores'.center(60))
print('='*60)
print(' Num   Name', end='')
print(' '*16, end=' ') 
print('Goals', end=' ')
print(' '*big, end='') 
print('Total')

for pos,person in enumerate(lst):
    print(f' {pos+1}:    {person["name"]:.<20} {person["goals"]}', end='')
    space=(big-3*(len(person["goals"]))) +6
    print(' '*space, end='') 
    print(f'{person["total"]}')
print('='*60)

while True:
    src=int(input('Which player do you want to see the data in detail? (search by num, 999 interrupts): '))

    if src==999:
        break

    if (src>(len(lst)+1) or src<1):
        print('That is not a valid option!') 
        continue

    num=len(lst[src-1]["goals"])

    print('='*50)
    print(f'The player {lst[src-1]["name"]} played in {num} matches: ')
    for i in range(1, num+1):
        print(f'    => In the {i}º match they scored {lst[src-1]["goals"][i-1]}')
    print(f'That is a total of {lst[src-1]["total"]} goals')
    print('='*50)
