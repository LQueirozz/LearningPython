#CHALLENGE 98: Counting
#GOAL:Write code that receives a start, an end and a pace to count numbers
#SKILL: Learning about functions pt1

from time import sleep

def count(s, e, p):
    if p==0:
        p=1
    if p<0:
        p=p*(-1)
    print(f'I shall count from {s} to {e} in intervals of {p}')
    if (e>s):
        while e>s:
            print(f'{s}', end=' ', flush=True)
            s+=p
            sleep(0.5)

    elif (s>e):
        while s>e:
            print(f'{s}', end=' ', flush=True)
            s-=p
            sleep(0.5)

    else:
        print (f'{s}')

count(int(input('Start: ')), int(input('End: ')), int(input('Pace: ')))