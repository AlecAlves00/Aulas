"""Escreva um programa que leia um número N intero qualquer e mostre na tela os N primeiros elementos de uma sequência de Fibonacci. 

ex: 0 → 1 → 1→ 2 → 3 → 5 → 8 → 13
"""

quantidade = int(input('Digite a quantidade de termo de Fibonacci deseja ver: '))
termo1 = 0
termo2 = 1
contador = 0
print('0', end ='')
while contador < quantidade - 1:
    termo3 = termo1  + termo2
    print(f' → {termo3}',end ='')
    contador += 1
    termo1 = termo2
    termo2 = termo3
print(' → FIM!')
    

    
