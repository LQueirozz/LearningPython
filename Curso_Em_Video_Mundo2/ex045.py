#CHALLENGE 45: Rock, paper, scissors
#GOAL: Write code that plays rock, paper, scissors with the user
#SKILL: Learning about nested conditionals

from random import randint

print('Let\'s play rock, paper scissors!')
print('For rock, type 0')
print('For paper, type 1')
print('For scissors, type 2')

user = int(input('What do you want to play?: '))
comp = randint(0,2)

lis=['rock', 'paper', 'scissors']


if(comp==user):
    print(f'It\'s a TIE, we both played {lis[user]}')
    exit()

elif(user==0):
    if(comp==1):
        venceu=False
    else:
        venceu=True

elif(user==1):
    if(comp==2):
        venceu=False
    else:
        venceu=True
    
elif(user==2):
    if(comp==0):
        venceu=False
    else:
        venceu=True

else:
    print('That is not a valid option! Please pick an option between 0 and 2 next time!')
    exit()

if(venceu):
    print(f'Congrats, you WON! I played {lis[comp]} and you played {lis[user]}!')

else:
    print(f'Oh no, you LOST! I played {lis[comp]} and you played {lis[comp]}!')