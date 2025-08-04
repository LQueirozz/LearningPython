#CHALLENGE 62: Arithmetic progressions with while and more iterations
#GOAL: Write code that receives the first term and the pace of a geometric progression, and prints out the first 10 numbers of the progression,
#Then ask how many mor terms he wants to see until he wishes to quit
#SKILL: Learning about while loops

print('Type in the first term and the pace of a arithmetic progression')
p=int(input('Pace: '))
a0= float(input('First term: '))
a=a0
i=0

lim=10

while(lim!= -1):

    lim+=i
    
    while(a!= (a0 + (lim -1)*p)):
        a= a0 + i*p
        print(f'Term a{i}: {a:.2f}')
        i+=1

    lim= int(input('How many more terms do you want to see? (-1 exits the code): ')) 
