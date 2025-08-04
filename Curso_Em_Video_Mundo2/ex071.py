#CHALLENGE 71: ATM machine
#GOAL: Write code that simulates an ATM machine calculating the minimum number of bills needed for withdrawal
#SKILL: Learning about break 

amount = float(input('Hello, I am an ATM machine. Enter how much you want to withdraw: R$'))
print(f'To withdraw R${amount:.2f}, you will need...')

bills_50 = amount // 50
amount = amount - 50 * bills_50

bills_20 = amount // 20
amount = amount - 20 * bills_20

bills_10 = amount // 10
amount = amount - 10 * bills_10

bills_1 = amount

print(f'{bills_50:.0f} bills of R$50.00')
print(f'{bills_20:.0f} bills of R$20.00')
print(f'{bills_10:.0f} bills of R$10.00')
print(f'{bills_1:.0f} bills of R$1.00')