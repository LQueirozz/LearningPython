#CHALLENGE 72: Writing out numbers
#GOAL: Write code that receives a number between 0 and 20, and prints out that number written out by using a tuple with all the tuples written out
#SKILL: Learning about tuples

numbersT = ('Zero', 'One', 'Two', 'Three', 'Four', 
           'Five', 'Six', 'Seven', 'Eight', 'Nine', 
           'Ten', 'Eleven', 'Twelve', 'Thirteen', 
           'Fourteen', 'Fifthteen', 'Sixteen', 
           'Seventeen', 'Eighteen', 'Nineteen', 'Twenty' )

while True:
    n=int(input('Type in an integer between 0 and 20: '))
    while(n>20 or n<0):
        n=int(input('That is not a valid option! Type in an integer between 0 and 20: '))

    print(f'The number you chose was {numbersT[n]}')

    again=input('Would you like to try again? (Y/N): ').strip()
    
    if(again=='Y'):
        continue

    elif(again=='N'):
        break

    else:
        while(again!='S' and again!='N'):
           again=input('That is not a valid option! Would you like to try again? (Y/N): ').strip() 
        