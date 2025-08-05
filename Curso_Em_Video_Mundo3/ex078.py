#CHALLENGE 78: Greatest and smallest in a list
#GOAL:Write code that receives 5 integers from the user and puts them in a list. Then, print out yhe list, the greatest and smallest number, and their respective positions
#SKILL: Learning about lists

l=[]
for i in range (0,5):
    l.append(int(input(f'Type in an integer for the {i}º position: ')))

gts= max(l)
sml= min(l)
gtsS=''
smlS=''

for pos, num in enumerate(l):
    if num==gts:
        if len(gtsS):
            gtsS+=', '
        gtsS += str(pos) + 'º'

    if num==sml:
        if len(smlS):
            smlS+=', '
        smlS += str(pos) + 'º'


print(f'The list you typed was: {l}')
print(f'The greatest number was {gts}, at the {gtsS} positions of the list')
print(f'The smallest number was {sml}, at the {smlS} positions of the list')