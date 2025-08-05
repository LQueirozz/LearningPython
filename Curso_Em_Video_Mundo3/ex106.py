#CHALLENGE 106: Interactive helping system
#GOAL: Write code that uses the interactive help. The user will type a command and the manual will show up
#When the user inputs 'END', the program will stop
#SKILL: Learning about functions pt2

def helpingOut(com: str):
    help(com)

command=''
while True:
    command=input('Python Function or Library > ')
    if command.upper()=='END':
        break

    else:
        helpingOut(command)
