"""
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final,mostre:

A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.
"""

pessoas = list()
pesos = list()
maior = menor = count = 0
resp = ''
nome_maior = list()
nome_menor = list()

while resp in 'Ss':
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    resp = str(input('Deseja continuar? [S/N]: '))
    pessoas.append([nome, peso])
    pesos.append(peso)
    count += 1
maior = max(pesos)
menor = min(pesos)
for c in pessoas:
    if c[1] == maior:
        nome_maior.append(c[0])
    if c[1] == menor:
        nome_menor.append(c[0])

print(f'A quantidade de pessoas cadastradas é: {count}')
print(f'As pessoas com maior peso {maior} é: {nome_maior}')
print(f'As pessoas com menor peso {menor} é: {nome_menor}')

