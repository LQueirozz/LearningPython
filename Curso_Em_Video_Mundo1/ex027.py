#CHALLENGE 27: Breaking down a name
#GOAL: Write code that receives the user's name and prints out their first and last name
#SKILL: Learning about string manipulation

n = ( ( ( input('What is your name: ') ).strip() ).lower() ).split()

print('Pleasure to meet you!')
print(f'Your first name is {n[0]}')
print(f'Your last name is {n[len(n)-1]}' )