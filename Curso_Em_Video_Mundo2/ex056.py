#CHALLENGE 56: Weights in a list
#GOAL: Write code that receives the weight of 5 people and then find the highest and lowest weight among them
#SKILL: Learning about for loops

print("Please type in the weight of 5 people")

lst=[]

for i in range(1, 6, 1):
    lst.append(float( input('Weight of the {i}º person: '))) 

low=lst[0]
high=-1

for w in lst:
    if (w < low):
        low=w

    if (w>high):
        high=w

print(f'The highest weight was {high}kg')
print(f'The lowest weight was {low}kg')