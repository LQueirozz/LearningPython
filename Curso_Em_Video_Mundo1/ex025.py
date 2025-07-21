#CHALLENGE 25: Checking for a word inside a name
#GOAL: Write code that receives the user's name prints out if they have "Silva" as a part of their name
#SKILL: Learning about string manipulation

n = ( ( input("Whats your name?: ") ).strip() ).lower() 

print(f'You have "Silva" somewhere in your name: {bool(n.find("silva")+1)}')