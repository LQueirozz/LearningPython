#CHALLENGE 83: Checking for parentheses
#GOAL:Write code that receives a mathematic expression using parentheses. Then, print out if the use of the parentheses was correct or incorrect
#SKILL: Learning about lists


while True:
    exp= input('Type in a mathematical expression using parentheses: \n')
    if('(' in exp or ')' in exp):
        break

    else:
        print('You did not use the parentheses as requested!') 

opened=0

for letter in exp:
    if letter=='(':
        opened+=1

    elif letter==')':
        opened-=1

    if opened<0: #this would mean a parentheses was closed before it was opened
        print('You used the parentheses wrong!')
        break

if opened>0: #more opened then closed
    print('You used the parentheses wrong!')

elif opened==0:
    print('You used the parentheses correctly!')