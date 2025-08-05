#CHALLENGE 87: Matrix pt2
#GOAL:Write code that receives 9 numbers and then display them like a 3x3 matrix. Then show the sum of all even numbers, 
#the sum of the 3rd column and the biggest value of the second line
#SKILL: Learning about nested lists

m=[[],[],[]]
sumE=0
sum3=0

for i in range (0,3):
    for j in range (0,3):
        num=int(input(f'Type in an integer for the position [{i},{j}]: '))
        m[i].append(num)

        if num%2==0:
            sumE+=num

        if j==2:
            sum3+=num


print('='*30)
print(f'||{m[0][0]:^7}||{m[0][1]:^7}||{m[0][2]:^7}||')
print('='*30)
print(f'||{m[1][0]:^7}||{m[1][1]:^7}||{m[1][2]:^7}||')
print('='*30)
print(f'||{m[2][0]:^7}||{m[2][1]:^7}||{m[2][2]:^7}||')
print('='*30)

print(f'The sum of all even numbers was {sumE}')
print(f'The sum of all the numbers in the 3rd column was {sum3}')
print(f'The biggest number in the second row was {max(m[1])}')