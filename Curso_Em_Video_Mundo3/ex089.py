#CHALLENGE 89: Class scores
#GOAL:Write code that receives the name of a student and 2 test scores. 
#Then, show for each student the mean of their grades, and give the user the option to see the individual scores of each student
#SKILL: Learning about nested lists

students=[]
student=[]
grade=[]

while True:
    flag= ( (input('Would you like to add another student to your list? (Y/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='Y'):
        print('That is not a valid option!', end=' ') 
        continue
    
    student.append(input(f'Name: '))
    grade.append( float(input(f'Test score 1: ')))
    grade.append( float(input(f'Test score 2: ')))
    grade.append((grade[0]+grade[1])*0.5)

    student.append(grade[:])
    students.append(student[:])

    grade.clear()
    student.clear()

print('='*48)
print('Grade averages'.center(48))
print('='*48)
print(' Num   Name                         Final score')
for pos,person in enumerate(students):
    print(f' {pos+1}:    {person[0]:.<30}', end='' )
    print(f'{person[1][2]:>7.2f}')
print('='*48)

while True:
    n=int(input('Which student do you want to see both test scores? (search by num, 999 interrupts): '))

    if n==999:
        break

    if (n>(len(students)+1) or n<1):
        print('That is not a valid option!') 
        continue

    print(f"{students[n-1][0]}'s grades were: {students[n-1][1][0]}, {students[n-1][1][1]}")

