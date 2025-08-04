#CHALLENGE 57: Input validation
#GOAL: Write code that takes in input of a person's sex until they pick between male, female or intersex
#SKILL: Learning about while loops

a = ((input('Type in your sex (M, F ou I): ')).strip()).upper()
while( (a not in 'fF') and (a not in 'mM') and (a not in 'Ii') ):
    a = ((input('That is not a valid option, pleas pick an option among (M, F ou I): ')).strip()).upper()

print(f'Option selected: {a}')
