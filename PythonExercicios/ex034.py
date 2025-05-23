
"""Escrava um programa que pergunte o salário de um funcinário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250.00,calcule um aumento de 10%

#Para os inferiores ou iguais,o aumento é de 15%.

 """

salario = float(input('Digite seu salário para descobrir quanto de aumento você vai receber: '))
if salario > 1250:
    print('O seu novo salário será de: {:.2f}'.format(salario * 0.10 + salario))
else:
    print('O seu novo salário será de: {:.2f}'.format(salario * 0.15 + salario))