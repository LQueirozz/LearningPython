 #CHALLENGE 73: Football teams
#GOAL: Write code that prints out the first five teams placed in the "Campeonato Brasileiro de Futebol", the last four teams, a list with the teams in alphabetic order, in what position is the team "Fluminense"
#SKILL: Learning about tuples

cbf=('Cruzeiro', 'Flamengo', 'Bragantino', 'Palmeiras', 
     'Botafogo', 'Bahia', 'Mirassol', 'Fluminense',
     'Atlético Mineiro', 'Corinthians', 'Ceará', 'Inter',
     'Grêmio', 'São Paulo', 'Vitória', 'Vasco', 'Santos',
     'Juventude', 'Fortaleza', 'Sport')

print('=======================')
print('The first five teams are:')
for i in range(0, 5):
    print(f'{i+1}º: {cbf[i]}')
print('=======================\n')


print('=======================')
print('The last four teams are:')
for i in range(16, 20):
    print(f'{i+1}º: {cbf[i]}')
print('=======================\n')

print('=======================')
print(f'The list in alphabetical number is: {sorted(cbf)}')
print('=======================\n')

print('=======================')
print(f'The team "Fluminense" is at the {cbf.index('Fluminense') +1}º position')
print('=======================')