#CHALLENGE 26: Looking for A's
#GOAL: Write code that receives any text from the user and prints out how many A's there are in the excerpt as well as it's first and last occurence
#SKILL: Learning about string manipulation

t = ( ( input('Type in any text: ') ).strip() ).lower()

num = t.count('a')
pos1 = t.find('a') + 1
pos2 = t.rfind('a') + 1

print(f'The letter "a" appear {num} times in your text')
print(f'The first time the letter "a" shows up in your text was at position {pos1}')
print(f'The last time the letter "a" shows up in your text was at position {pos2}')
