"""Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no  final quantos palpites foram  necessários para vencer."""

from random import randint

num = randint(0,10)
pessoa = 0
cont = 0
while pessoa != num:
    pessoa = int(input('Tente acertar um número de 0 a 10:  '))
    cont += 1
print(f'Você precisou de tentativas {cont} para acertar o número {num}.')
