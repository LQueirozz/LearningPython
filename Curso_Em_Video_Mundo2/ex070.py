#CHALLENGE 70: Product statistics
#GOAL: Write code that collects product information and calculates total spent, expensive items, and cheapest item
#SKILL: Learning about break 

over1000 = 0
i = 1
total = 0
expensive_items = 0
name_list = []
price_list = []
cheapest_index = 0

while True:
    flag = ((input('Do you want to add another product? (Y/N): ')).strip()).upper()
    if(flag == 'N'):
        break
    elif(flag != 'Y'):
        print('Invalid option!') 
        continue

    print('\n================{}=================' .format(i))
    name = ((input(f'Enter the name of the {i}º product: ')).strip())
    price = (float(input(f'Enter the price of the {i}º product: $')))
    print(' ')

    total += price

    if(price > 1000):
        expensive_items += 1

    name_list.append(name)
    price_list.append(price)

    if(i > 2 and price_list[i-1] < price_list[cheapest_index]):
        cheapest_index = i-1

    i += 1

print(f'The total spent was ${total:.2f}')
print(f'You bought {expensive_items} items more expensive than $1000.00')
print(f'The cheapest item you bought was {name_list[cheapest_index]}, which cost ${price_list[cheapest_index]:.2f}')