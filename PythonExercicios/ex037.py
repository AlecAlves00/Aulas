
"""Escreva um programa que leia um  número inteiro qualquer e peça para o usario escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
"""

num = int(input('Digite o número que deseja fazer a conversão:  '))
base = int(input('Digite número 1 para binário, 2 para octal, 3 para hexadecimal: '))

if base == 1:
    binario = bin(num)[2:]
    print('O número binario é {}'.format(binario))
elif base == 2:
    octal = oct(num)[2:]
    print('O número octal é {}'.format(octal))
elif base == 3:
    hexadecimal = hex(num)[2:].upper()
    print('O número hexadecimal é {}'.format(hexadecimal))
else:
    print('Nenhuma das opções.')


