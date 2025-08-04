#CHALLENGE 36: Bank loan calculator
#GOAL: Write code that calculates monthly payments for a house loan and determines if the loan is approved based on salary constraints
#if the monthly payment is greater than 30% of salary, the loan is denied
#SKILL: Learning about nested conditionals

print('We shall calculate your monthly payments to pay off a house')
houseValue = int( input('Enter the value of the house: ') )
salary = int( input('Enter your monthly salary: ') )
time = (int( input('Enter how many years you plan to finance this house: ') ) )*12

if(houseValue/time > 0.3*salary):
    print('\033[1;31mYour loan was denied!\033[0;30m')

else:
    print('Your monthly payment will be: \033[1;31m${:.2f} \033[0;30m' .format(houseValue/time))