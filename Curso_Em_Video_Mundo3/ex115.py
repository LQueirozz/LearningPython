#CHALLENGE 115: Data Logging
#GOAL: Write code that either takes in a person's name and age or shows all the info on people already stored
#SKILL: Learning about error and exception handling

def validation(msg: str, token: str, contains: list):
    valid= False 
    while not valid: 
        n= (input(f'{msg}')).strip()

        try:
            n=int(n)
            if n not in contains:
                 valid=False
            else:
                valid=True

        except ValueError:
            valid=False

        if not valid:
            print(f'\033[1;31m\nERROR! "{n}" is not a valid {token}!\n\033[m')
           
    return n

ages= list()
for i in range (0,130, 1):
    ages.append(i)

def login(lst: list):
        person = dict()
        person['name']= (input('Please enter the name of the new login: ')).strip()
        person['age']= validation('Please enter the age of the new login: ', 'age', ages)
        lst.append(person.copy())


def readLog(lst: list):
    i=1
    for p in lst:
        print(f'The {i}º person in the list is:')
        i+=1
        for key, value in p.items():
            print(f'{key}: {value}')
        print('')

def menu():
    print('LOGIN OPTIONS:')
    print('1- ADD ANOTHER PERSON TO THE LIST')
    print('2- SEE THE LIST')
    print('3- LEAVE')
    option= validation('What option do you want?: ', 'option', [1,2,3])
    print('')
    return option

info= [] 
while True:
    opt=menu()

    match opt:
        case 1:
            try:
                login(info)
            except Exception:
                print('-> ERROR WHEN ADDING THE NEW LOGIN')
            else:
                print('\n-> Person logged in succefully!\n')

        case 2:
            readLog(info)

        case 3:
            break









    