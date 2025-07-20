#Exercício 31: Custo da viagem
#Aprendendo sobre condicionais pt4

dist= float( input('Quão longa é a viagem (em km): ') )

#O preço da passagem é R$0,45/km se for mais de 200km, e R$0,50/km se for menos

if(dist>200):
    print('Para uma viagem de {:.2f}km, o custo da passagem é: R${:.2f}' .format(dist, dist*0.45))

else:
    print('Para uma viagem de {:.2f}km, o custo da passagem é: R${:.2f}' .format(dist, dist*0.50))