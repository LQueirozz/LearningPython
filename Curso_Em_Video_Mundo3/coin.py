#This is a module containing the useful functions for the exercises 107-112

def coin(value: float, currency: str | None= 'R$'):
    """
    The function coin() takes in a numerical value and a currency and formats it
    so that it looks like a monetary value
    -> param value: amount of money to be formatted
    -> param currency: The currency that is being used
    -> return:The amount with two decimal houses after the dot and the currency
    """
    formated= f'{currency.strip()}{value:.2f}'
    return formated


def changing(value: float, amount: float, negative=False, literal=False):
    """The function changing() is meant to cause a percentual decrement or increment of a monetary value
    -> Param value: The initial amount that will be manipulated
    -> Param amount: The amount of percentage points that will be added/subtracted from the initial amount
    -> Param negative: if negative, reduce the initial value, if not, increment the inital value
    -> Param literal: if literal, the return will be a sentence describing the operation, 
    if not, the return will be the float value
    -> Return: The new amount after changing, either in a sentence or a float
    """

    if not negative:
        lit= f'Incrementing {amount}% of the price:'
        amount= (amount+100)/100

    else:
        lit= f'Reducing {amount}% of the price:'
        amount= (100- amount)/100

    if not literal:
        return value*amount
    
    else:
        return lit


def info(value: float, currency:str | None= 'R$', reduce: float | None= 0, increment: float | None= 0 ):
    """
    The function info() is meant to return some mathematical information about a monetary amount, such as
    it's double, it's half, a discount, and an increment
    -> Param value: Monetary amount
    -> Param currency: The currency the value is in
    -> Param reduce: The percentage points that will be discounted from the original value
    -> Param increment: The percentage points that will be incremented to the original value
    """
    valueF=coin(value, currency)
    print('-'*45)
    print((f'Info about {valueF}').center(45))
    print('-'*45)
    print('Double of the price: ', end= ' '*15)
    print(coin(changing(value, 100), currency))
    print('Half of the price: ', end= ' '*17)
    print(coin(changing(value, 50, negative=True), currency))
    if reduce!= 0:
        lit= changing(value, reduce, negative=True, literal=True)
        sze= 36-len(lit)
        print(lit, end= ' '*sze)
        print(coin(changing(value, reduce, negative=True), currency))
    if increment!= 0:
        lit= changing(value, increment, literal=True)
        sze= 36-len(lit)
        print(lit, end= ' '*sze)
        print(coin(changing(value, increment), currency))
    print('-'*45)

def validation():
    """
    The function validation() is meant to be an upgrade of the method .isnumeric, because it
    can catch negative numbers and floats. It's also meant to not stop until a number is provided
    param n-> string to be avaliated if is actually number
    return: n
    """
    while (True): 
        n= input('Type in a monetary amount: ').strip()
        valid= False 
        try:
            n= float(n)
            valid=True
            
        except ValueError:
            valid=False 
       
        if not valid and n.find(',') != -1:
            n= n.replace(',', '.')
            try:
                n= float(n)
                valid=True
            
            except ValueError:
                valid=False           
            
        if not valid:
            n= print(f'\033[1;31mERROR! "{n}" is not a valid monetary value! \033[0;30m')
        else:
            break

    return float(n)
