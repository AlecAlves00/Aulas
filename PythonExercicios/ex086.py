"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formação correta.
"""
listageral = [[],[],[]]

for linha in range(3):
    for coluna in range(3):
        num = int(input(f'Digite um valor para [{linha} , {coluna}] : '))
        listageral[linha].append(num)
for linha in listageral:
    for valor in linha:
        print(f'[ {valor:^3} ]', end = '')
    print()