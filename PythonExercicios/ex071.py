"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,pergunte ao usuário qual será o valor a ser 
trocado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS:considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1.
"""

caixa = int(input('Ola, digite o valor que deseja trocar? '))
valor_original = caixa
notas1 = notas10 = notas20 = notas50 = 0
while True:
    if caixa >= 50:
        notas50 = caixa // 50 
        caixa = caixa % 50
    elif caixa >= 20:
        notas20 = caixa // 20
        caixa = caixa % 20
    elif caixa >= 10:
        notas10 = caixa // 10
        caixa = caixa % 10
    elif caixa >= 1:
        notas1 = caixa // 1
        caixa = caixa % 1
    else:
        break
print(f'Com o valor digitado {valor_original}')
print(f'A quantidade de notas de R$50 é: {notas50}')
print(f'A quantidade de notas de R$20 é: {notas20}')
print(f'A quantidade de notas de R$10 é: {notas10}')
print(f'A quantidade de notas de R$1 é: {notas1}')

"""
Jeito que ele fez:

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedulas = 50
totced = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totced = 0
        if total == 0:
            break
"""