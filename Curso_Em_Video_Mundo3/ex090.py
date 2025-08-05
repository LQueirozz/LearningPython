#CHALLENGE 90: student's grades
#GOAL:Write code that receives the name, grade and situation (P for passed and F for failed) of a student
#then store it in a dictionary, and show it into the screen 
#SKILL: Learning about dictionaries

student= dict()
student['name']= input('What is the name of the student?: ')
while True:
    student['grade']=float(input('What is the grade of the student? (0-10): '))
    if student['grade']>10 or student['grade']<0:
        print('That is not a valid grade!')
    else:
        break

if student['grade']<5:
    student['situation']='F'
else:
    student['situation']='P'

for key, value in student.items():
    print(f'The {key} of the student is {value}')
