#CHALLENGE 18: Sin, cos and tan
#GOAL: Write code that receives an angle in degrees and prints out it's sin, cos and tan 
#SKILL: Learning about importations

import math
ang= float( input('Type in an angle in degrees: ') )

s= math.sin(math.radians(ang))
c= math.sqrt( 1 - (s**2) )
t= s/c

print(f'The angle {ang:.2f}º has...')
print(f'sin = {s:.2f} ')
print(f'cos = {c:.2f} ')
print(f'tan = {t:.2f} ')
