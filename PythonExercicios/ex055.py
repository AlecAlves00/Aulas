"""Faça um programa que leia o peso de  cinco pessoas. No final,mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0

for c in range(1,6):
    peso = int(input('Digite o peso de cinco pessoas:  '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor :
            menor = peso
print(f'O menor peso digitado foi {menor}Kg e o maior é {maior}Kg.')
        
