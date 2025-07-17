#Exercício 8: Conversor de unidades de medida
#Aprendendo sobre operadores pt4

n= float( input('Digite uma medida em metros: ') )
print('A medida {} em metros corresponde a...' .format(n))

print('{}km,' .format(n/1000))
print('{}hm,' .format(n/100))
print('{}dam,' .format(n/10))
print('{}dm,' .format(n*10))
print('{}cm,' .format(n*100))
print('{}mm,' .format(n*1000))
