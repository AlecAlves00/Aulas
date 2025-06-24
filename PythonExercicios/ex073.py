"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de coloção.
Depois mostre:
A-Apenas os 5 primeiros colocados.
B-Os últimos 4 colocados da tabela.
C-Uma lista com os times em ordem alfabética
D-Em que posição na tabela está o time Mirassol.
"""

times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG',
         'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'São Paulo',
         'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')
print('A Tabela do Campeonato Brasileiro de Futebol é:')
print(times)

print('Os cinco primeiros colocados é: ')
print(times[:5])

print('Os quatro últimos colocados é: ')
print(times[-4:])

print('Lista em ordem alfabética dos times é: ')
print(sorted(times))

print('A posição que o time Mirassol está é: ')
posicao = times.index('Mirassol') + 1
print(posicao)