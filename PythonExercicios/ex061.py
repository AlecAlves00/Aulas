"""Refaça o desafio 051,lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while."""

"""
primeironum = int(input('Digite o primeiro termo: '))
razao = int(input('Qual será a razão da PA: '))
for c in range(10):
    pa = primeironum + c * razao
    print(pa)
"""

num = int(input('Digite o número: '))
razao = int(input('Digite a razao da PA: '))
dezprimeiros = 0

while dezprimeiros < 9:
    dezprimeiros += 1
    pa = num + dezprimeiros * razao
    print(f'{pa} → ' , end='')
