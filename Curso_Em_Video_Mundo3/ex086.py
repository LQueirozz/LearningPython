#CHALLENGE 86: Matrix
#GOAL:Write code that receives 9 numbers and then display them like a 3x3 matrix
#SKILL: Learning about nested lists

m=[[],[],[]]

for i in range (0,3):
    for j in range (0,3):
        m[i].append(int(input(f'Type in an integer for the position [{i},{j}]: ')))

print('='*30)
print(f'||{m[0][0]:^7}||{m[0][1]:^7}||{m[0][2]:^7}||')
print('='*30)
print(f'||{m[1][0]:^7}||{m[1][1]:^7}||{m[1][2]:^7}||')
print('='*30)
print(f'||{m[2][0]:^7}||{m[2][1]:^7}||{m[2][2]:^7}||')
print('='*30)