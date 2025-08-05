#CHALLENGE 93: Soccer player stats
#GOAL:Write code that receives a soccer player's name, how many matches they played and how many goals they made on each game. Then print out stats
#SKILL: Learning about dictionaries

player={}

player['name']= str(input('What is the name of the player?: '))
num= int(input(f'How many soccer matches did {player["name"]} partipate in?: '))
while num<0:
    print('That is not a valid number!')
    num= int(input(f'How many soccer matches did {player["name"]} partipate in?: '))

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

print('='*50)
print(f'The dictionary we buit based on your data was: {player}')
print('='*50)
for key, value in player.items():
    print(f'The key {key} has a value of: {value}')
print('='*50)
print(f'The player {player["name"]} played in {num} matches: ')
for i in range(1, num+1):
    print(f'    => In the {i}º match they scored {numGoals[i-1]}')
print(f'That is a total of {player["total"]} goals')
print('='*50)