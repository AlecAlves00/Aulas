"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
"""

from random import randint
impar = 'I'
par = 'P'
soma = 0
vitorias = 0

while True:
    computador = randint(0,10)
    valorjogador = int(input('Digite o valor que deseja jogar: '))
    escolhajogador = str(input('Deseja jogar IMPAR [I] ou PAR [P]: ')).upper().strip()
    soma = valorjogador + computador
    if soma % 2 == 0 and escolhajogador in 'P':
            vitorias += 1
            print(f'Parabéns você ganhou!! Você jogou {valorjogador},{escolhajogador}, o computador jogou {computador} a soma dos números é {soma} é par')
    elif soma % 2 == 1 and escolhajogador in 'I':
            vitorias += 1
            print(f'Parabéns você ganhou!! Você jogou {valorjogador},{escolhajogador}, o computador jogou {computador} a soma dos números é {soma} é impar')
    elif escolhajogador not in ('P','I'):
        print('Opção invalida. Joga novamente.')
    elif soma % 2 == 0 and escolhajogador in 'I' or soma % 2 == 1 and escolhajogador in 'P':
        print(f'Você perdeu a soma dos números foi {soma}. O número de vitorias foi {vitorias}.')
        break
