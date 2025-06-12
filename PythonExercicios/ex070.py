"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A)Qual é o total gasto na compra.
B)Quantos produtos custam mais de R$1000.
C)Qual é o nome do produto mais barato.
 """

caros = 0
barato = 0
nome = ''
soma = 0
nomebarato = ''
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Qual o valor do produto R$: '))
    soma += valor
    continuar = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if valor >= 1000:
        caros += 1
    if barato == 0:
        barato = valor
        nomebarato = nome
    if valor < barato:
        barato = valor
        nomebarato = nome
    if continuar in 'N':
        break
    
print(F'O total gasto foi R${soma:.2f}.\nA quantidade de produtos que custam mais de R$1000 é {caros}.\nO produto mais barato é {nomebarato},R${barato:.2f}')
    
