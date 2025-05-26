
""" Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. 
calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.
"""

casa = float(input('Qual o valor da casa? R$  '))
salario = float(input('Qual o seu salario? R$  '))
anos =  int(input('Em quantos anos pretende pagar tudo? '))

prestacao = casa / (anos * 12)
exceder = salario * (30/100) 
if prestacao < exceder:
    print('Você pode fazer o emprestimo da casa.')
else:
    print('Você não pode fazer o emprestimo da casa.')
