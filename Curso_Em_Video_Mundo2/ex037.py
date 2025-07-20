#Exercício 37: Conversor de bases numéricas
#Aprendendo sobre condicionais aninhadas pt2

print('Vamos converter um inteiro escolhido por você pra outra base númerica!')
numOrig= int(input('Digite o número que você quer converter: '))

print('Para converter o número {} para binário, digite 1'.format(numOrig))
print('Para converter o número {} para octal, digite 2'.format(numOrig))
print('Para converter o número {} para hexadecimal, digite 3'.format(numOrig))

base= int(input('Qual das bases você deseja?: '))

if(base==1):
    conversão='binário'
    num=bin(numOrig)

elif(base==2):
    conversão= 'octal'
    num=oct(numOrig)

elif(base==3):
    conversão= 'hexadecimal'
    num=hex(numOrig)

else:
    print('Isso não é uma opção válida! Por favor, escolha um número entre 1 e 3 na próxima')
    exit()
    
print('O número {}, quando convertido para a base {}, fica {}' .format(numOrig, conversão, num[2::]))
