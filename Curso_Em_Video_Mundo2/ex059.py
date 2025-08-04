#CHALLENGE 59: Calculator
#GOAL: Write code that receives two integers from the user, then an operation and calculate it for him
#SKILL: Learning about while loops

def getNums(l:list):
    l[0]=int(input('Type in the first integer: ')) 
    l[1]=int(input('Type in the second integer: '))
    return l[:]

def menu():
    print('CALCULATOR OPTIONS:')
    print('1- SUM')
    print('2- MULTIPLICATION')
    print('3- GREATEST')
    print('4- NEW NUMBERS')
    print('5- LEAVE CALCULATOR')
    return(int (input('What option do you want: ')))

def greatest(a, b):
    if(a>b):
        return (f'{a} > {b}')
    
    elif(a<b):
        return (f'{b} > {a}')
    
    else:
        return (f'{a} = {b}')

lst = [0, 0]
opc=0

lsl= getNums(lst[0], lst[1])
opc= menu()

while(opc!=5):
    if(opc==1):
        print(f'{lst[0]} + {lst[1]} = {lst[0] + lst[1]}')

    elif(opc==2):
        print(f'{lst[0]} x {lst[1]} = {lst[0]* lst[1]}')

    elif(opc==3):
        print(greatest(lst[0], lst[1]))

    elif(opc==4):
        lst= getNums(lst[0], lst[1])

    else:
        print('Invalid option!')

    opc= menu()

print('End of execution')
