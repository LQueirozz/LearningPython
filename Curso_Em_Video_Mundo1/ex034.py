#CHALLENGE 34: Salary adjustment with conditions
#GOAL: Write code that receives a worker's current salary and prints out their new corrected salary after a pay upgrade
#SKILL: Learning about conditionals

wage= float( input('Type in your current wage: R$') )

#the pay upgrade is 10% if the worker made more than R$1250.00, and 15% if not

if(wage>1250):
   print(f'You received {wage:.2f}, but after your 10% pay raise, you will receive {(wage*1.1):.2f}')

else:
    print(f'You received {wage:.2f}, but after your 15% pay raise, you will receive {(wage*1.15):.2f}')