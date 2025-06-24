"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços.na sequência.
No final,mostre uma listagem de preços ,organizando os dados em forma tabular.
"""

listagem = (('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livros',34.90))
print('-' * 40)
print(f'{'Listagem de preços':^40}')
print('-' * 40)

for c in listagem:
    if isinstance(c,str):
        p = '.' * (30-len(c))
        print(f'{c}{p}R$:',end='')
    else:
        print(f'{c:.2f}')

