"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120 / 10! = 10x9x8x7x6x5x4x3x2x1 = 3.628.800
"""

num = int(input('Digite o número que deseja saber o fatorial: '))
fatorial = num 
sequencia = num
fatorial2 = num
while fatorial != 1:
    fatorial -= 1 
    sequencia = sequencia * fatorial
    print(f'{fatorial}',end='')
    print(' x ' if fatorial > 1 else' = ',end='')


for fatorial2 in range(num,0,-1):
    sequencia = sequencia * fatorial2
    print(f'{sequencia}')

