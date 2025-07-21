#CHALLENGE 7: Mean of test scores
#GOAL: Write code that receives two test scores and prints out it's mean
#SKILL: Learning about operators and basic data types

n1 = float( input('The first test score of the student was: ') )
n2 = float( input('The second test score of the student was: ') )
mean= (n1+n2)/2

print(f'The mean between the provided test scores is: {mean:.2f}')
