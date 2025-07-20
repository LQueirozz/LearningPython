#Exercício 29: Radar
#Aprendendo sobre condicionais pt2


vel= int(input('A que velocidade (em km/h) você está indo: ') )

#preço da multa: R$7 por km/h acima de 80km/h

if(vel>80):
    print("Você foi multado! Favor pague R${}" .format( (vel-80)*7 ))

else:
    print("Você é um motorista responsável!")