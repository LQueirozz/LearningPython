#Exercício 34: Reajuste salarial condicional
#Aprendendo sobre condicionais pt7

salario= float( input('Digite seu salário atual: R$') )

if(salario>1250):
    print('Seu salario era R${:.2f}. Após o reajuste de 10%, ele vira: R${:.2f}' .format(salario, salario*1.1))

else:
    print('Seu salario era R${:.2f}. Após o reajuste de 15%, ele vira: R${:.2f}' .format(salario, salario*1.15))