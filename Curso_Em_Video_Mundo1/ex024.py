#CHALLENGE 24: Checking first word of a city
#GOAL: Write code that receives the name of a town and prints out if it's first name is "santo"
#SKILL: Learning about string manipulation

c = ( ( ( input("In what city were you born?: ") ).strip() ).lower() ).split()

print(f'The first word of your birthtown is "santo": {c[0]=='santo'}' )

