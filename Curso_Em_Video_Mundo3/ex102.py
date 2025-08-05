#CHALLENGE 102: Factorials
#GOAL:Write code that takes in an int, an print out it's factorial, with an option to see how the result was reached
#SKILL: Learning about functions pt2

def fact(n: int | None = 1, show: bool | None = False):
    """
    The fact() funtion calculates factorials
    -> Param n: integer whose factorial  we are going to calculate, if not present n=1
    -> Param show: boolean that determines if we should show the process of how we reached the result, if not present, show= False
    -> Return: The result of the factorial, with or without the way we got it    
    """

    fac=1
    process= ''
    for i in range (n, 0, -1):
        fac *= i
        if show:
            process+= f'{i}'
            if i>1:
                process+= ' X '

            else:
                process+= f'= {fac}'
        else:
            process= str(fac)

    return process

f= int(input('What number should we calculate the factorial?: '))
s= bool(input('Do you want to see how to calculate it?: '))
print(f'The factorial of {f} is {fact(f, s)}')
#print(help(fact))



