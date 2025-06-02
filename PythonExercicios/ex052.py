"""Faça um programa que leia um número inteiro diga se ele é ou não um número primo."""

num = int(input('Digite o número que deseja saber se é primo:  '))
if num < 2:
    print('Esse número não é um primo')
else:
    resultado = True
    for c in range (2,int(num** 0.5)+1):
        if num % c == 0:
            resultado = False
            break
    if resultado == True:
        print('Esse número é um primo')
    else:
        print('Esse número não é um primo')

    