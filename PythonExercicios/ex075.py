"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,mostre:
A)Quantas vezes apareceu o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
cont = 0
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro número: '))
numero4 = int(input('Digite o último número: '))
numeros = (numero1,numero2,numero3,numero4)



if 9 in numeros:
    cont = + 1
    print(f'O número 9 apareceu {cont}')
else:
    print('nenhum número 9 digitado')
if 3 in numeros:
    posiçao = numeros.index(3) + 1
    print(f'A posição em que o primeiro número 3 aparece é {posiçao}')
else:
    print('nenhum numéro 3 digitado')
for c in numeros:
    if c % 2 == 0:
        print(f'Os números pares são {c}')

    