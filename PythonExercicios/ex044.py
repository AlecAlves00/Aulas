"""Elabore um programa que calcule o valor a ser pago por um produto,considerando o seu preço normal e condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão : 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
"""

produto = float(input('Qual o valor do produto que deseja comprar?:  '))
forma = int(input('Digite a forma de pagamento. 1 para dinheiro ou cheque, 2 para à vista no cartão, 3 para 2x no cartão sem juros ou 4 para 3x ou mais com juros:  '))
if forma == 1:
    valor = produto - (produto * (10/100))
    produtof = 'Desconto de 10%'
elif forma == 2:
    valor = produto - (produto * (5/100))
    produtof = 'Desconto de 5%'
elif forma == 3:
    valor = produto
    produtof = 'Produto sem desconto'
elif forma == 4:
    valor = produto + (produto * (20/100))
    produtof = 'Juros de 20% encima do seu produto'
elif forma > 4:
    print('Tente novamento nenhuma das opções sugerida foi selecionada.')
print('O valor final a ser pago será de {}, com a condição de {}'.format(valor,produtof))
