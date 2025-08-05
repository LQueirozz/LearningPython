#CHALLENGE 97: Special printing
#GOAL:Write code that receives a sentence and prints it out between two lines that adapt to the size of the text
#SKILL: Learning about functions pt1

def write(msg):
    tam= 4+ len(msg)
    print('='*tam)
    print(f'  {msg}  ')
    print('='*tam)


write(str(input('Write in some text: ')))