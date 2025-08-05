#CHALLENGE 100: Sorting and adding
#GOAL:Write code that sorts 5 numbers, then sums only the even ones
#SKILL: Learning about functions pt 1

from random import randint
from time import sleep

def sorting():
    lst=list()
    print('Sorting 5 numbers: ')
    for i in range(0,5):
        num= randint(1,10)
        print(f'{num}', end=' ', flush=True)
        lst.append(num)
        sleep(0.5)
    return lst


def sumEven(lstt):
    sum =0
    for item in lstt:
        if item%2==0:
            sum+=item

    print(f'\nThe sum of the even numbers is {sum}')

sumEven(sorting())