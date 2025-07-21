#CHALLENGE 31: Ticket price
#GOAL: Write code that calculates how much a train ticket should cost based on how big the trip is
#SKILL: Learning about conditionals

dist= float( input('How long is the trip (in km): ') )

#If >200km, it will cost R$0.45 per km. If it's any shorter than that, it will cost R$0.50 per km 

if(dist>200):
    print(f'For this trip, {dist:.2f}km, the cost of the ticket is R${(dist*0.45):.2f}')

else:
    print(f'For this trip, {dist:.2f}km, the cost of the ticket is R${(dist*0.5):.2f}')
