#CHALLENGE 54: Coming to age
#GOAL: Write code that receives the birth year of 7 people and print out how many are of age (21 yrs)
#SKILL: Learning about for loops


print("Let\'s check how many people have 21yrs or more!")
cYear = int(input('Type in the current year: '))
age=0

lst = []

for i in range(1, 8, 1):
    if( int(input(f'Type in the birth year of the {i}º person: ') )  +21 <=cYear):
        age+=1

print('Between those 7 people, {} of them were of age')