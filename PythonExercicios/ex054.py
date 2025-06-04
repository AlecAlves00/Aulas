"""Crie um programa que leia o ano de nascimento de sete pessoas.No final,mostre quantas pessoas 
ainda não atingiram a maioridade e quantas ja são maiores.
#21 a maior idade.
"""

import datetime
ano = datetime.datetime.now().year
maior = 0
menor = 0
for c in range(1,8):
    ano1 = int(input('Digite os sete anos de nascimento: '))
    idade = ano - ano1
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'A quantidade de pessoas com maior idade é {maior} e com menor idade é {menor}')
