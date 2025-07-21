#CHALLENGE 11: Paint calculus
#GOAL: Write code that receives the dimensions of a wall, calculates the surface area and prints out how much paint would be necessary 
#to paint it fully (1m² of wall= 2L of paint )
#SKILL: Learning about operators and basic data types

print('We shall calculate how much paint you need in order to paint you wall!')
w= float(input('Type in the width of your wall, in meters: '))
h= float(input('Type in the height of your wall, in meters: '))

print(f'For your wall ({h}m X {w}m), you will need {(w*h/2):.2f}L of paint' )
