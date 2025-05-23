
#Crie um programa que leia um númeor Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Ex: Digite um número: 6.127
#Ex: O número 6.127 tem a parte Inteira 6

from math import trunc

n = float(input('Digite um número:'))
print('O número {} tem a parte Inteira {}'.format(n,trunc(n)))