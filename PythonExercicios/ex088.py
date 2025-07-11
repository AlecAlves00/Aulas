"""
Faça um programa que ajude um jogador da Mega sena a criar palpites.O programa vai perguntar quantos jogos serão 
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
print('-'*40)
print(f'{'Joga na mega sena':^40}')
print('-'*40)
jogos = list()
quantidade = int(input('Quantos jogos você quer que eu sorteie?: '))
for c in range(quantidade):
    cartelas = []
    while len(cartelas) < 6:
        numeros = randint(1,60)
        if numeros not in cartelas:
            cartelas.append(numeros) 
    jogos.append(cartelas)
    cartelas.sort()
    print(f'Jogo {c+1}º os números sorteados foi:{cartelas}')
    sleep(1)