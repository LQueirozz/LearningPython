#CHALLENGE 29: Speed checker
#GOAL: Write code that checks if the user was speeding. If so, give him a ticket of R$7.00 for every km/h above the limit of 80km/h 
#SKILL: Learning about conditionals

vel= int(input('How fast were you going (km/h): ') )

if(vel>80):
    print(f'That is too fast! Pay a fine of R${(vel-80)*7}')

else:
    print('That is below the speed limit, good job!')
