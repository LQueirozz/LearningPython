#CHALLENGE 22: Analysing a name
#GOAL: Write code that receives the user's name and prints out their name in all lowercase, in all uppercase, how many letters (not counting spaces) the whole name has and how many letters just the first name has
#SKILL: Learning about string manipulation

n= (input("Type in your name: ")).strip()

nU= n.upper()
nL= n.lower()
nBrk=n.split()
sze = len(n)-n.count(' ')
sze1= len(nBrk[0])

print(f'Your name in all uppercase: {nU}')
print(f'Your name in all lowercase {nL}')
print(f'Your name has {sze} letters' )
print(f'Your first name has {sze1} letters')
