#CHALLENGE 103: Soccer player stats
#GOAL:Write code that takes in a name and how many goals he made, with default options for lack of input
#SKILL: Learning about functions pt2

def player(name: str, numGoals: str):
    """
    The function player() takes in a name and the amount of goals a soccer player made in the season
    param name: player's name
    param numGoals: Amount of goals
    return: None
    """

    if isNumeric(numGoals):
        numGoals=isNumeric(numGoals)
    else:
        numGoals=0

    if len(name)==0:
        name='<unknown>'
    

    while numGoals<0:
        print('Invalid input')
        numGoals= input('Number of goals: ')
        if isNumeric(numGoals):
            numGoals=isNumeric(numGoals)
        else:
            numGoals=0

    print(f'The player "{name}" made {numGoals} goals this season')

def isNumeric(n: str):
    """
    The function isNumeric() is meant to be an upgrade of the method .isnumeric, because it can catch negative numbers
    param n-> string to be avaliated if is actually number
    return: n, if it really is an int (negative or positive), or False, if not
    """
    n= n.strip()
    if n.isnumeric():
        return int(n)
    
    else:
        if n[0]=='-':
            n=n[1:]
            if n.isnumeric():
                n= int(n)
                n*=-1
                return n
            
        else:
            return False


player(str(input('Player name: ')), str(input('Number of goals: ')))
#print(help(player))
#print(help(isNumeric))
    