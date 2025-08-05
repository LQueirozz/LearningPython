#CHALLENGE 99: Finding the biggest
#GOAL:Write code that has a function to find the greateest among many integers
#SKILL: Learning about functions pt1

from time import sleep
def greatest(*num):
    print('='*30)
    print(f'Between the {len(num)} numbers: ')
    for n in num:
        print(n, end=' ', flush=True) 
        sleep(0.5)
    print(f'\nThe greatest is { max(num)}')   
    print('='*30)
    sleep(2.5)

greatest(1, 5, -3, 9, 6)
greatest(1, 2, 3)
greatest(8, 7, 3, 456)
