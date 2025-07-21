#CHALLENGE 15: Rental car company
#GOAL: Write code that receives how many km and days a rental car was occupied and prints out how much the renter owns the company 
#SKILL: Learning about operators and basic data types

#Price per day: R$60
#Price per km: R$0,15

days= int( input('Type in how many days you have rented the car: '))
km= float (input('Type in how many kilometers you traveled with the car: '))

print(f'You own R${( (days*60) + (km*0.15) ):.2f}' )