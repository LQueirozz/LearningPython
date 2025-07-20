#Exercício 68: Par ou impar
#Aprendendo sobre break pt3

from random import randint
venceu=0

while True:
    comp = randint(0,9)
    pi = ( (input('Você quer par ou impar? (P/I): ')).strip()).upper()

    if(pi!='P' and pi!='I'):
        print('Opção inválida! Escolha P ou I na próxima')

    num = int(input('Digite um número inteiro para jogar: '))

    if((pi=='P') and ((comp+num)%2==0) ) or ((pi == 'I') and ((comp+num)%2==1)):
        venceu+=1
        print(f'Parabéns você venceu! Eu joguei {comp} e você {num}. Jogue mais!')
        continue

    else:
        print(f'Poxa, não foi desta vez! Eu joguei {comp} e você {num}.')
        break

print(f'Você conseguiu um streak de {venceu} vitórias consecutivas')


    


        
