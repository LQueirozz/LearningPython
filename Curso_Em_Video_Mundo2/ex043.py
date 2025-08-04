#CHALLENGE 41: BMI classification
#GOAL: Write code that calculates a person's weight and height and show what BMI categorie they are
#SKILL: Learning about nested conditionals

h = float(input('Type in your height in meters: '))
m = float(input('Type in your weight in kg: '))

imc= m/(h**2)

if(imc<18.5):
    print('BELOW WEIGHT')

elif(imc<=25):
    print('IDEAL WEIGHT')

elif(imc<=30):
    print('OVER WHEIGHT')

elif(imc<=40):
    print('OBESITY')

else:
    print('MORBID OBESITY')

