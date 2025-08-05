#CHALLENGE 101: Voting permissions
#GOAL:Write code that takes in a person's birthyear and prints out if voting is 
#mandatory, optional or not allowed according to Brazillian law 
#SKILL: Learning about functions pt2

def voting(birthYear: int):
    """The function voting() will return a literal depending on the age situation of the voter.
    -> People with less than 16 years old are NOT ALLOWED to vote
    -> For people in between 16-18, as well as over 65 years of age, voting is OPTIONAL
    -> For people in between 18-65 years old, voting is MANDATORY
       
    """
    from datetime import datetime
    currentYear= (datetime.now()).year
    age = currentYear-birthYear

    if age<0:
        return False
    
    elif age<16:
        return [age, 'NOT ALLOWED']

    elif 18<=age<65:
        return [age, 'MANDATORY']
    
    else:
        return [age,'OPTIONAL']
    

info= voting(int(input('What is your birthyear?: ')))
if info:
    print(f'For the age of {info[0]}, voting is {info[1]}')

else:
    print('Invalid input!')

#print(help(voting))


