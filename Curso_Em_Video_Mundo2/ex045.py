#Exercício 45: Pedra, Papel, Tesoura
#Aprendendo sobre condicionais aninhadas pt10

from random import randint

print('Vamos jogar pedra, papel e tesoura!')
print('Para jogar pedra, digite 0')
print('Para jogar papel, digite 1')
print('Para jogar tesoura, digite 2')

n = int(input('O que que você quer jogar?: '))
c = randint(0,2)

lis=['pedra', 'papel', 'tesoura']


if(c==n):
    print('Deu empate, nós dois jogamos {}' .format(lis[n]))
    exit()

elif(n==0):
    if(c==1):
        venceu=False
    else:
        venceu=True

elif(n==1):
    if(c==2):
        venceu=False
    else:
        venceu=True
    
elif(n==2):
    if(c==0):
        venceu=False
    else:
        venceu=True

else:
    print('Isso não é uma opção válida! Por favor, escolha um número entre 1 e 3 na próxima')
    exit()

if(venceu):
    print('Parabéns! Você venceu! Enquanto eu joguei {}, você foi mais esperto e jogou {}!' .format(lis[c], lis[n]))

else:
    print('Poxa! Você perdeu! Eu joguei {}, e você jogou {}! Na próxima você ganha!' .format(lis[c], lis[n]))