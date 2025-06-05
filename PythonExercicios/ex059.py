"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] soma
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

operaçao = 0
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro número: '))
while operaçao != 5:
    operaçao = int(input('''Digite um valor para realizar a operação que deseja\n[1] Soma\n[2] Multiplicar\n[3] Qual o maior número\n[4]Digitar novos números\n[5] Sair do programa\n'''))
    if operaçao == 1:
        soma = num1 + num2
        print(f'A soma dos  números dados {num1} e {num2} é igual a {soma}')
    if operaçao == 2:
        multipli = num1 * num2
        print(f'A multiplicação dos números dados {num1} e {num2} é igual a {multipli}') 
    if operaçao == 3:
        if num1 < num2:
            maior = num2
            print(f'O maior número dos números dados: {num1},{num2} é {maior}')
        else:
            maior = num1
            print('O maior número dos números dados: {num1},{num2} é {maior}')
    if operaçao == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro número: '))