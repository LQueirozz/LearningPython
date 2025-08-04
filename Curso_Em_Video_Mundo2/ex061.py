#CHALLENGE 61: Arithmetic progressions with while
#GOAL: Write code that receives the first term and the pace of a geometric progression, and prints out the first 10 numbers of the progression
#SKILL: Learning about while loops

print(f'Type in the first term and the pace of a arithmetic progression')
p=int(input('Pace: '))
a0= float(input('First term: '))
a=a0
i=0

while(a!= (a0 + 9*p)):
    a= a0 + i*p
    print(f'Term a{i}= {a:.2f}')
    i+=1