#CHALLENGE 10: Conversion from R$ to US$ 
#GOAL: Write code that receives a money amount in Brazillian Reais and converts it to US Dollar (considering US$ 1.00 = R$ 5.54)
#SKILL: Learning about operators and basic data types

n= float(input('How much money do you have in your wallet?: R$') )

print(f'With R${n:.2f}, you could buy US${(n/5.54):.2f}')
