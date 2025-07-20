#Exercício 11: Cálculo de área de parede para pintar
#Aprendendo sobre operadores pt7

print('Vamos calcular quanto de tinta é necessário para que você pint a sua parede!')
largura= float(input('Digite a largura da sua parede em metros: '))
altura= float(input('Digite a altura da sua parede em metros: ') )

#considere a taxa de 2L de tinta para cada m² de tinta

print('Para sua parede de dimensões {}m X {}m, o que resulta em uma área de {:.2f}m², você precisa de {:.2f}L de tinta' .format(largura, altura, (largura*altura), (largura*altura/2)))