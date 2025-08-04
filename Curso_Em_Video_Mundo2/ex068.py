#CHALLENGE 68: Odds or evens
#GOAL: Write code that plays odds or evens with the user
#SKILL: Learning about break

from random import randint
vic=0

while True:
    comp = randint(0,9)
    pi = ( (input('Would you like odd or even? (O/E): ')).strip()).upper()

    if(pi!='O' and pi!='E'):
        print('That\'s not a valid option, pick between O or E next time')

    num = int(input('Type the integer number you want to play: '))

    if((pi=='E') and ((comp+num)%2==0) ) or ((pi == 'O') and ((comp+num)%2==1)):
        vic+=1
        print(f'Congrats you WON! I played {comp} and you played {num}. Let\'s go another game!')

    else:
        print(f'Oh no, you LOST! I played {comp} and you played {num}.')
        break

print(f'You reached a streak of {vic} consecutive victories')


    


        
