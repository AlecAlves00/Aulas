"""
Crie um programa que vai gerar cinco números aleatórios e colocar em tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint
num = (randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50))
print(f'Números escolhidos: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nMenor número: {min(num)}')
print(f'Maior número: {max(num)}')
