#CHALLENGE 104: Validating integers
#GOAL:Write code that takes in an object and checks if it really is an integer
#SKILL: Learning about functions pt2

def isNumeric(n: str):
    """
    The function isNumeric() is meant to be an upgrade of the method .isnumeric, because it can catch negative numbers.
    It's also meant to not stop until an integer is provided
    param n-> string to be avaliated if is actually number
    return: n, if it really is an int (negative or positive)
    """
    n= n.strip()
    while (not n.isnumeric()):    
        if len(n)>0 and n[0]=='-':
            n=n[1:]
            if n.isnumeric():
                n= int(n)
                n*=-1
                break
            
        else:
            n= print('\033[1;31mERROR! That is not a valid integer! \033[0;30m')
            n= input('Type in an integer: ')
            
    print(f'You typed the number {n}')  

isNumeric(input('Type in an integer: '))
            
