#CHALLENGE 113: Validating input
#GOAL:Write code that has 2 funtions that can validate if the user input was an integer or a float
#SKILL: Learning about error and exception handling

def validationFloat():
    """
    The function validationFloat() is meant to tell if the user input was a float before type casting
    in order to avoid throwing errors to the user. It's also meant to not stop until a float number 
    is provided
    Param: None
    return: n
    """
    valid= False 
    while not valid: 
        n= input('Type in a float: ').strip()

        try:
            n=float(n)
            valid=True

        except ValueError:
            print(f'\033[1;31mERROR! "{n}" is not a valid float! \033[m')
            valid=False

        else:
            print(f'The float you provided was: {n}')                   
    return n

def validationInt():
    """
    The function validationInt() is meant to tell if the user input was an int before type casting
    in order to avoid throwing errors to the user. It's also meant to not stop until an integer 
    is provided
    Param: None
    return: n
    """
    valid= False 
    while not valid: 
        n= input('Type in an integer: ').strip()

        try:
            n=int(n)
            valid=True

        except ValueError:
            print(f'\033[1;31mERROR! "{n}" is not a valid integer!\033[m')
            valid=False

        else:
            print(f'The int you provided was: {n}')           
    return n

validationFloat()
validationInt()