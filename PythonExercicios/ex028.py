
"""Escreva um programa que faça o computador "pensar" em um número intero entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrevre na tela se o usuário venceu ou perdeu
"""

from random import choice

n = [0,1,2,3,4,5]
e = choice(n)
t = int(input('Tente descobrir o número: '))
if t == e:
    print('Parabéns você acertou!')
else:
    print('Que pena você errou, tente de novo')
print('o número escolhido pelo computador foi: {}.'.format(e))
