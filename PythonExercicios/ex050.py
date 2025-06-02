"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas dos daqueles que forem pares.
Se o valor digitado for impar desconsidere-o."""

soma = 0
for c in range(1,7):
    num = int(input('Digite seis números: '))
    if num % 2 == 0:
        soma += num 
print('A soma de todos os números pares é {}.'.format(soma))

