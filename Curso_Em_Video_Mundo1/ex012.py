#CHALLENGE 12: On sale
#GOAL: Write code that receives the price of a product and prints out how much the customer will have to pay after a 5% discount
#SKILL: Learning about operators and basic data types

n= float( input('Type in the price of a product: R$'))
print(f'This product that costs R${n:.2f} is on a 5% off sale and comes out to R${(n*0.95):.2f}' )
