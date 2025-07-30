#CHALLENGE 92: Worker's info
#GOAL:Write code that receives a person's name, birth year and their "Carteira de Trabalho" registry (brazilian document that regulates worker's' employment status)
#If their Carteira de Trabalho registry is different than 0 (which would mean they don't have one), take in as well the year they started working, their sallary,
#and, after storing all this info in a dictionary, print it all out, including the age that the worker will be when they retire (35 years after first employment)
#SKILL: Learning about dictionaries

wrk=dict()
y= int(input('What is the current year?: '))
wrk['name']=str(input('What is your name?: '))
wrk['age']= y- int(input('What year were you born?: '))
wrk['CTR']= int(input('What is your CT registry (type in 0 if you do not have one)?: '))

if wrk['CTR']:
    wrk['year of first employment']= int(input('What year did you start working?: '))
    wrk['salary']=float(input('How much do you make?: R$'))
    wrk['age of retirement'] = wrk['age'] + 35-( y- wrk['year of first employment'] )

for key, value in wrk.items():
    print(f'Your {key} is {value}')
