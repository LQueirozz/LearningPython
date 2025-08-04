#CHALLENGE 66: Flags pt2
#GOAL: Write code that takes in as many integers as the user wants and then print out the highest, the lowest and the average
#SKILL: Learning about break

count=0
sum=0

while(True):
    flag= int(input('Type in a positive integer (to exit, type 999): '))
    if(flag==999):
        break
    sum+=flag
    count+=1

print(f'Before typing the exit code (999), you typed {count} numbers that sum up to {sum}')