#CHALLENGE 64: Flags
#GOAL: Write code that sums up all the users input until they type in the exit code
#SKILL: Learning about while loops

flag= int(input('Type in a positive integer (to exit, type 999): '))
count=0
sum=0

while(flag!=999):
    sum+=flag
    count+=1
    flag= int(input('Type in a positive integer (to exit, type in 999): '))

print(f'Before typing the exit code (999), you typed {count} numbers that sum up to {sum}')
