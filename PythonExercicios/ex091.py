'''Crie um programa onde 4 jogadores joguem um dado e o tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse 
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep

jogadores = {
'jogador1': 0,
'jogador2': 0,    
'jogador3': 0,          
'jogador4': 0,
}

print('Valores sorteados:')

for j in jogadores.keys():
    num = randint(1,6)
    jogadores[j] = num
    sleep(1)
    print(f'O {j} tirou {num}')

ordenar = dict(sorted(jogadores.items(), key=lambda item: item[1],reverse=True))

print('Ordem dos jogadores:')

posiçao = 1
for j,v in ordenar.items():
    sleep(1)
    print(f'{posiçao}º lugar: {j} número {v}')
    posiçao += 1