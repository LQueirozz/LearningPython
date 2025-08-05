#CHALLENGE 76: Price list with tuples
#GOAL: Write code that has tuple with item names and prices. Then, prints the tuple out in a price table
#SKILL: Learning about tuples

priceT= ('Pencil', 1.75, 
         'Eraser', 2.00, 
         'Notebook', 15.9, 
         'Pencil Case', 25.00, 
         'Protractor', 4.20, 
         'Compass', 9.99, 
         'Backpack', 120.32, 
         'Pens', 22.30, 
         'Book', 34.90 )

print('='*40)
print('Price table'.center(40))
print('='*40)

for pos,item in enumerate(priceT):
    if(pos%2==0):
        print(f'{item:.<30}', end='R$' )
    else:
        print(f'{item:>7.2f}')

print('='*40)