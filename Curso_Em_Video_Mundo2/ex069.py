#Exercício 69: Analise de dados pessoais contínua
#Aprendendo sobre break pt4

anoA = int(input('Digite o ano atual: '))
i=1
numH=0
numM=0
maiores=0

while True:
    flag= ( (input('Você quer cadastrar mais uma pessoa? (S/N): ')).strip()).upper()
    if(flag=='N'):
        break
    elif(flag!='S'):
        print('Opção Inválida!') 
        continue

    print('================{}=================' .format(i))
    idade=( anoA - (int( input('Informe o ano de nascimento da {}ª pessoa: ' .format(i)) )) )
    sexo= ((input('Informe o sexo da {}ª pessoa (M, F ou I): ' .format(i))).strip())
    print(' ')

    if(sexo=='M'):
        numH+=1

    if(sexo=='F' and idade<20):
        numM+=1

    if(idade>18):
        maiores+=1

print(f'Há {maiores} pessoas maiores de idade no grupo cadastrado')
print(f'Há {numH} pessoas do sexo masculino no grupo')
print(f'Há {numM} mulheres no grupo com menos de 20 anos' )
