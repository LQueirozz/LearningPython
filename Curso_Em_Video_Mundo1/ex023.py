#CHALLENGE 23: Breaking up the decimal houses of a number
#GOAL: Write code that receives an integer and prints out how many thousands, hundreds, tens and ones it has
#SKILL: Learning about operators

n = int(input('Type in a random integer: '))

print(f'Analysing the number {n} ...')

th = n//1000
n -= th*1000

h = n//100
n -= h*100

te = n//10
n -= te*10

u = n

print(f'Thousands: {th}')
print(f'Hundreds: {h}')
print(f'Tenths: {te}')
print(f'Units: {u}')