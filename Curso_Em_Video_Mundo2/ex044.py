#CHALLENGE 44: Payment management
#GOAL: Write code that receives the price of a product and prints out how much the customer should pay according to the payment method
#SKILL: Learning about nested conditionals

p= float(input('Type in the price of the product you are going to buy: R$'))

print('To pay cash up front, type in 1')
print('To pay debit card up front, type in 2')
print('To pay in 2 installments, type in 3')
print('To pay in 3 or more installments, digite 4')

fp= int(input('Which of the options above will you be using to pay?: '))

if(fp==1):
    print(f'By paying in cash up front, You get a 10 % discount. Your purchase rings up to R${(p*0.9):.2f}')

elif(fp==2):
    print(f'By paying with a debit card up front, you get 5% discount. Your purchase rings up to R${(p*0.95):.2f}' )

elif(fp==3):
    print(f'By paying in 2 installments, you pay full price. Your purchase rings up to R${p:.2f}')

elif(fp==4):
    print(f'By paying in 3 installments, you get a 20% tax. Your purchase rings up to R${(p*1.2):.2f}')

else:
    print('That\'s not a valid option! Please choose a number between 1 and 4 next time!')
    exit()
    