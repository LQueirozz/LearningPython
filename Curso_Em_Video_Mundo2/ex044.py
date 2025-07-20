#Exercício 44: Gerenciador de pagamentos
#Aprendendo sobre condicionais aninhadas pt9

p= float(input('Digite o preço do produto qu você vai comprar: R$'))

print('Para pagar à vista no dinheiro ou cheque, digite 1')
print('Para pagar à vista no cartão, digite 2')
print('Para pagar parcelando em duas vezes, digite 3')
print('Para pagar parcelando em três vezes ou mais, digite 4')

fp= int(input('Qual das formas de pagamento você deseja?: '))

if(fp==1):
    print('Pagando a vista no dinheiro ou cheque, você ganha um desconto de 10%. O valor final da sua compra é R${:.2f}' .format(p*0.9))

elif(fp==2):
    print('Pagando a vista no cartão, você ganha um desconto de 5%. O valor final da sua compra é R${:.2f}' .format(p*0.95))

elif(fp==3):
    print('Parcelando em duas vezes, você não paga juros. O valor final da sua compra é R${:.2f}' .format(p))

elif(fp==4):
    print('Parcelando em três ou mais vezes, você paga juros de 20%. O valor final da sua compra é R${:.2f}' .format(p*1.2))

else:
    print('Isso não é uma opção válida! Por favor, escolha um número entre 1 e 4 na próxima')
    exit()
    