#CHALLENGE 8: Unit conversion
#GOAL: Write code that receives a distance in meters and prints out the same measurement but converted, from milimeter to kilometer
#SKILL: Learning about operators and basic data types

n= float( input('Type in a length in meters: ') )
print(f'The measurement {n} in meters corresponds to...')
print(f'{n/1000}km,')
print(f'{n/100}hm,')
print(f'{n/10}dam,')
print(f'{n*10}dm,')
print(f'{n*100}cm,')
print(f'{n*1000}mm,')
