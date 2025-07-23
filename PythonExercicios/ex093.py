"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feito em cada partida.No final,tudo isso será guardado em um 
dicionário,incluindo o total de gols feitos durante o campeonato.
"""

dados = {}
gols = []
total = 0
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados['nome']} jogou?: '))
for c in range(0,partidas):
    c += 1
    gol = int(input(f'Quantos gols na partida {c}º ?'))
    gols.append(gol)
    total += gol
dados['gols'] = gols
dados['tot'] = total

print(dados)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {dados['nome']} jogou {partidas} partidas.')
for c,v in enumerate(gols):
    c += 1
    print(f'=> Na partida {c}º o jogador fez {v} gols')
print(f'E o total de gols foi {dados["tot"]}')