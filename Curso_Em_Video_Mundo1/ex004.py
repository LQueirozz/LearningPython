#CHALLENGE 4: Dissecting a variable
#GOAL: Write code that receives user input, then prints out it's primitive type and different aspects of it
#SKILL: Learning about operators and basic data types

n = input('Type in something: ')

print(f'The primitive type of your input was: {type(n)}')
print(f'Is your input a number?: {n.isnumeric()}')
print(f'Is your input alphabetic?: {n.isalpha()}')
print(f'Is your input entirely lowercase?: {n.islower()}' )
print(f'Is your input entirely uppercase?: {n.isupper()}' )
print(f'Is your input only white spaces?: {n.isspace()}')
print(f'Is your input alphanumeric?: {n.isalnum()}' ) 
