"""Faça um programa que leia 5 valores númericos e aguarde-os em uma lista.
No final,mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

valores = list()
posicao_menor = []
posicao_maior = []


for c in range(0,5):
    valores.append(int(input(f'Digite o número da posição {c} : ')))

maior = menor = valores[0]

for c, v in enumerate(valores):
    if v > maior:
        maior = v
        posicao_maior = [c]
    elif v == maior:
        posicao_maior.append(c)
    if v < menor:
        menor = v
        posicao_menor = [c]
    elif v == menor:
        posicao_menor.append(c)

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for maior in posicao_maior:
    print(f'{maior}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')   
for menor in posicao_menor:
    print(f'{menor}...', end='')
 